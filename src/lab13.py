"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    # Lần chạy thứ i xảy ra khi i-1 lần trước đều sai: tổng (1-p)^(i-1), i = 1..k
    # = (1 - (1-p)^k) / p ; khi k → ∞ thì = 1/p (phân phối hình học).
    if k is None:
        return 1 / p
    return (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    # Thất bại chỉ khi cả k lần đều sai.
    if k is None:
        return 1.0
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    # = số lần chạy kỳ vọng / xác suất thành công = 1/p với mọi k (tử và mẫu cùng chứa 1-(1-p)^k).
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    # Chỉ lấy các lần chạy thuộc các yêu cầu đang xét (để A3 gọi lại với reqs đã lọc theo loai).
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        # B1/B3: bỏ các lần chạy vượt giới hạn; yêu cầu cần nhiều lần hơn coi như chuyển nhân viên.
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    # Tử số: MỌI lần chạy, kể cả lần lỗi (lần lỗi vẫn tốn token và tool).
    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    # Phút nhân viên: số GIẢ LẬP (simulated).
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    # Mẫu số: chỉ đếm yêu cầu thành công.
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    return dict(
        token=tien_token.sum(),
        tool=tien_tool.sum(),
        chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),  # phần của lần chạy thứ 2, 3
        xem_lai=xem_lai,
        lam_lai=lam_lai,
        tong=tong,
        thanh_cong=thanh_cong,
        cps=tong / thanh_cong,
        hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs),
    )


CHI_PHI_CO_DINH = 40_000_000   # đồng / tháng
KHOI_LUONG_THANG = 45_000      # yêu cầu / tháng
PHAM_VI = ['noi_dia', 'hang_nang']


def in_a2(runs, reqs):
    kq = mo_hinh(runs, reqs)
    nhan = {'token': 'đo từ trace', 'tool': 'đo từ trace', 'chay_lai': 'đo từ trace',
            'xem_lai': 'simulated', 'lam_lai': 'simulated', 'tong': 'có phần simulated',
            'thanh_cong': '', 'cps': 'simulated', 'hoa_don_moi_yc': 'đo từ trace'}
    print('\n=== A2 · Mô hình chi phí từ trace ===')
    print(f"(tool: {runs['tool_calls'].sum():,} lần gọi · xem lại: {reqs['phut_xem_lai_simulated'].sum():,} phút"
          f" · làm lại: {reqs['phut_lam_lai_simulated'].sum():,} phút)")
    for ten, gia_tri in kq.items():
        print(f'{ten:15s} {gia_tri:>14,.1f}  {nhan[ten]}')
    print(f"Chi phí mỗi việc thành công gấp {kq['cps'] / kq['hoa_don_moi_yc']:.1f} lần hoá đơn chia số yêu cầu")
    for k in ['token', 'tool', 'xem_lai', 'lam_lai']:
        print(f"  tỉ trọng {k:8s} {kq[k] / kq['tong'] * 100:5.1f}%")
    khong_tc = int((reqs['ket_qua'] != 'thanh_cong').sum())
    he_thong = (kq['tong'] + khong_tc * BASELINE) / len(reqs)
    print(f"Chi phí cả hệ thống mỗi yêu cầu (cộng {khong_tc} ca nhân viên làm thay × 12.000 đ): "
          f"{he_thong:,.0f} đ = {he_thong / BASELINE:.2f}× [simulated]")
    return kq


def in_a3(runs, reqs):
    print('\n=== A3 · Tách theo loại yêu cầu ===')
    print(f"{'loai':10s} {'so_yc':>6s} {'ti_le_tc':>9s} {'chay/yc':>8s} {'cps':>9s} {'so_12k':>7s}")
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        r = reqs[reqs['loai'] == loai]
        kq = mo_hinh(runs, r)
        so_chay = runs['request_id'].isin(r['request_id']).sum()
        print(f"{loai:10s} {len(r):6d} {kq['thanh_cong'] / len(r) * 100:8.1f}% {so_chay / len(r):8.2f}"
              f" {kq['cps']:9,.0f} {kq['cps'] / BASELINE:6.2f}×")
    # Chạy lại có giúp không: tỉ lệ ok theo từng lần thử.
    bang = (runs.merge(reqs[['request_id', 'loai']], on='request_id')
                .assign(ok=lambda d: (d['status'] == 'ok').astype(float))
                .pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean'))
    print('\nTỉ lệ lần chạy ok theo lần thử (attempt):')
    print((bang * 100).round(1).to_string())


def in_a4(runs, reqs):
    print('\n=== A4 · Chi phí cố định (phạm vi noi_dia + hang_nang) ===')
    r = reqs[reqs['loai'].isin(PHAM_VI)]
    kq = mo_hinh(runs, r)
    print(f"Trong phạm vi: {len(r)} yêu cầu, {kq['thanh_cong']} việc thành công, "
          f"tổng {kq['tong']:,.0f} đ, cps {kq['cps']:,.0f} đ [simulated]")
    for ten, khoi_luong in [('45.000 yc/tháng', KHOI_LUONG_THANG), ('Một nửa khối lượng', KHOI_LUONG_THANG / 2)]:
        # Quy ra số việc thành công mỗi tháng theo tỉ lệ trong mẫu 1.200 yêu cầu.
        tc_thang = khoi_luong * kq['thanh_cong'] / len(reqs)
        co_dinh = CHI_PHI_CO_DINH / tc_thang
        tong_moi_viec = kq['cps'] + co_dinh
        print(f"{ten:20s} việc TC/tháng {tc_thang:>8,.0f} · cố định/việc {co_dinh:>6,.0f} đ"
              f" · cps + cố định {tong_moi_viec:>6,.0f} đ = {tong_moi_viec / BASELINE:.2f}× [simulated]")


if __name__ == '__main__':
    import sys
    sys.stdout.reconfigure(encoding='utf-8')  # tránh lỗi in tiếng Việt trên console Windows
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    print('=== A1 ===')
    print(f'so_lan_chay_ky_vong(0.8, 2)            = {so_lan_chay_ky_vong(0.8, 2):.2f}')
    print(f'so_lan_chay_ky_vong(0.8)               = {so_lan_chay_ky_vong(0.8):.2f}')
    print(f'he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) = {he_so_chi_phi_moi_viec_thanh_cong(0.8, 3):.2f}')
    kiem_tra_dap_an_biet_truoc()
    ket_qua = in_a2(runs, reqs)
    in_a3(runs, reqs)
    in_a4(runs, reqs)
    # TODO CP2 · Nhiệm vụ B: đổi từng yếu tố, ghi vào bảng độ nhạy.
    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
