"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python lab13.py (cần pandas).
Dữ liệu trong hai file CSV là giả lập. Không cần khoá API.
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
CHI_PHI_CO_DINH = 40_000_000  # đồng mỗi tháng
YEU_CAU_MOI_THANG = 45_000
PHAM_VI_PILOT = ('noi_dia', 'hang_nang')


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if p == 0:
        return math.inf if k is None else k
    return ti_le_thanh_cong(p, k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if k is None:
        return float(p > 0)
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    xac_suat_thanh_cong = ti_le_thanh_cong(p, k)
    if xac_suat_thanh_cong == 0:
        return math.inf
    return so_lan_chay_ky_vong(p, k) / xac_suat_thanh_cong


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')
    print(f'  Tối đa 2 lần: {so_lan_chay_ky_vong(0.8, 2):.2f}')
    print(f'  Chạy đến khi đúng: {so_lan_chay_ky_vong(0.8):.2f}')
    print(f'  Hệ số chi phí tối đa 3 lần: {he_so_chi_phi_moi_viec_thanh_cong(0.8, 3):.2f}')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
def mo_hinh(runs, reqs, gia_vao=GIA_VAO, gia_ra=GIA_RA, gia_tool=GIA_TOOL, luong_phut=LUONG_PHUT,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Tính chi phí cho các request_id trong reqs, cộng cả lần chạy lỗi.

    Phần chạy lại đã nằm trong token và tool. Tiền xem lại, làm lại và
    các kết quả suy ra từ chúng dùng dữ liệu simulated. Khi giới hạn lần
    chạy, các yêu cầu vượt giới hạn chuyển sang nhân viên theo giả định B.
    """
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        reqs = reqs.copy()
        vuot_gioi_han = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot_gioi_han, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot_gioi_han, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = (runs['tokens_in'] * gia_vao + runs['tokens_out'] * gia_ra) / 1000
    tien_tool = runs['tool_calls'] * gia_tool
    token, tool = tien_token.sum(), tien_tool.sum()
    chay_lai = (tien_token + tien_tool)[runs['attempt'] > 1].sum()
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = token + tool + xem_lai + lam_lai
    thanh_cong = reqs['ket_qua'].eq('thanh_cong').sum()
    return {
        'token': token,
        'tool': tool,
        'chay_lai': chay_lai,
        'xem_lai': xem_lai,
        'lam_lai': lam_lai,
        'tong': tong,
        'thanh_cong': thanh_cong,
        'cps': tong / thanh_cong if thanh_cong else math.nan,
        'hoa_don_moi_yc': (token + tool) / len(reqs) if len(reqs) else math.nan,
    }


def in_a2(ket_qua, so_yeu_cau):
    print('\nA2 · Mô hình chi phí từ trace')
    print(f"Token: {ket_qua['token']:,.0f} đ")
    print(f"Tool: {ket_qua['tool']:,.0f} đ")
    print(f"Trong đó, token và tool của lần chạy thứ 2 trở đi: {ket_qua['chay_lai']:,.0f} đ")
    print(f"Xem lại: {ket_qua['xem_lai']:,.0f} đ [simulated]")
    print(f"Làm lại: {ket_qua['lam_lai']:,.0f} đ [simulated]")
    print(f"Tổng chi phí trợ lý: {ket_qua['tong']:,.0f} đ [simulated]")
    print(f"Số việc thành công: {ket_qua['thanh_cong']:,}/{so_yeu_cau:,}")
    print(f"Chi phí mỗi việc thành công: {ket_qua['cps']:,.0f} đ [simulated]")
    print(f"Hoá đơn token và tool mỗi yêu cầu: {ket_qua['hoa_don_moi_yc']:,.1f} đ")

    gap_hoa_don = ket_qua['cps'] / ket_qua['hoa_don_moi_yc']
    ti_trong_lam_lai = ket_qua['lam_lai'] / ket_qua['tong']
    ti_trong_gio_nhan_vien = (ket_qua['xem_lai'] + ket_qua['lam_lai']) / ket_qua['tong']
    khong_thanh_cong = so_yeu_cau - ket_qua['thanh_cong']
    chi_phi_he_thong = (ket_qua['tong'] + BASELINE * khong_thanh_cong) / so_yeu_cau
    print(f'Chi phí mỗi việc thành công / hoá đơn mỗi yêu cầu: {gap_hoa_don:.1f} lần [simulated]')
    print(f'Tỉ trọng làm lại: {ti_trong_lam_lai:.1%}; giờ nhân viên: {ti_trong_gio_nhan_vien:.1%} [simulated]')
    print(f'Chi phí cả hệ thống trước cố định (bù {khong_thanh_cong} ca): '
          f'{chi_phi_he_thong:,.0f} đ/yêu cầu [simulated]')


def in_a3(runs, reqs):
    print('\nA3 · Chi phí theo loại yêu cầu')
    print('Loại | Số yêu cầu | Thành công | Lần chạy/yêu cầu | Chi phí/việc [simulated] | So với 12.000 đ [simulated]')
    for loai, nhom in reqs.groupby('loai', sort=False):
        ket_qua = mo_hinh(runs, nhom)
        ti_le = ket_qua['thanh_cong'] / len(nhom)
        lan_chay = nhom['so_lan_chay'].mean()
        cps = ket_qua['cps']
        print(f'{loai} | {len(nhom):,} | {ti_le:.1%} | {lan_chay:.2f} | {cps:,.0f} đ | {cps / BASELINE:.2f}×')

    quoc_te_ids = reqs.loc[reqs['loai'].eq('quoc_te'), 'request_id']
    runs_quoc_te = runs[runs['request_id'].isin(quoc_te_ids)]
    ti_le_ok = runs_quoc_te['status'].eq('ok').groupby(runs_quoc_te['attempt']).mean()
    print('Tỉ lệ status=ok của quoc_te theo lần chạy (chỉ tính các lần đã chạy):')
    for lan, ti_le in ti_le_ok.items():
        print(f'  Lần {lan}: {ti_le:.1%}')


def in_a4(runs, reqs):
    print('\nA4 · Chi phí cố định trong phạm vi noi_dia + hang_nang')
    reqs_pilot = reqs[reqs['loai'].isin(PHAM_VI_PILOT)]
    ket_qua = mo_hinh(runs, reqs_pilot)
    # Khối lượng tháng là của toàn hệ thống. Chỉ ngoại suy các ca thành công trong phạm vi.
    ty_le_thanh_cong_tren_toan_mau = ket_qua['thanh_cong'] / len(reqs)
    print(f"Phạm vi: {len(reqs_pilot):,} ca, {ket_qua['thanh_cong']:,} việc thành công; "
          f"chi phí biến đổi {ket_qua['cps']:,.0f} đ/việc [simulated]")
    print('Yêu cầu/tháng | Thành công/tháng | Cố định/việc | Tổng/việc [simulated] | So với 12.000 đ [simulated]')
    for khoi_luong in (YEU_CAU_MOI_THANG, YEU_CAU_MOI_THANG // 2):
        viec_thanh_cong = khoi_luong * ty_le_thanh_cong_tren_toan_mau
        co_dinh_moi_viec = CHI_PHI_CO_DINH / viec_thanh_cong
        tong_moi_viec = ket_qua['cps'] + co_dinh_moi_viec
        print(f'{khoi_luong:,} | {viec_thanh_cong:,.0f} | {co_dinh_moi_viec:,.0f} đ | '
              f'{tong_moi_viec:,.0f} đ | {tong_moi_viec / BASELINE:.2f}×')


if __name__ == '__main__':
    kiem_tra_dap_an_biet_truoc()
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    in_a2(mo_hinh(runs, reqs), len(reqs))
    in_a3(runs, reqs)
    in_a4(runs, reqs)
    # TODO CP2 · Nhiệm vụ B: đổi từng yếu tố, ghi vào bảng độ nhạy.
    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
