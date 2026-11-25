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
    return 1.0 / p if k is None else (1.0 - (1.0 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    return 1.0 if k is None else 1.0 - (1.0 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
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
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())

    return {
        'token': float(tien_token.sum()),
        'tool': float(tien_tool.sum()),
        'chay_lai': float((tien_token + tien_tool)[runs['attempt'] > 1].sum()),
        'xem_lai': float(xem_lai),
        'lam_lai': float(lam_lai),
        'tong': float(tong),
        'thanh_cong': thanh_cong,
        'cps': float(tong / thanh_cong),
        'hoa_don_moi_yc': float((tien_token.sum() + tien_tool.sum()) / len(reqs)),
    }


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    print('--- A1 ---')
    print(f'p=0.8, k=2    : {so_lan_chay_ky_vong(0.8, 2):.2f}')
    print(f'p=0.8, k=None : {so_lan_chay_ky_vong(0.8):.2f}')
    print(f'he_so(0.8, 3) : {he_so_chi_phi_moi_viec_thanh_cong(0.8, 3):.2f}')
    kiem_tra_dap_an_biet_truoc()

    print('\n--- A2 · Mô hình chi phí từ trace ---')
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        if ten == 'hoa_don_moi_yc':
            print(f'{ten:15s} {gia_tri:>14,.1f}')
        else:
            print(f'{ten:15s} {gia_tri:>14,.0f}')
    print(f'Số phút xem lại [simulated] : {reqs["phut_xem_lai_simulated"].sum():.0f}')
    print(f'Số phút làm lại [simulated] : {reqs["phut_lam_lai_simulated"].sum():.0f}')
    print(f'Số lần gọi tool             : {runs["tool_calls"].sum():.0f}')
    print(f'Gấp hoá đơn/yêu cầu         : {ket_qua["cps"] / ket_qua["hoa_don_moi_yc"]:.1f}x')
    print(f'Tỉ trọng làm lại [sim]      : {ket_qua["lam_lai"] / ket_qua["tong"] * 100:.1f}%')
    print(f'Tỉ trọng xem lại [sim]      : {ket_qua["xem_lai"] / ket_qua["tong"] * 100:.1f}%')
    khong_tc = len(reqs) - ket_qua['thanh_cong']
    he_thong_moi_yc = (ket_qua['tong'] + khong_tc * BASELINE) / len(reqs)
    print(f'Cả hệ thống / yc [sim]      : {he_thong_moi_yc:,.0f} đ ({he_thong_moi_yc / BASELINE:.2f}x)')

    print('\n--- A3 · Tách theo loại yêu cầu ---')
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        sub = reqs[reqs['loai'] == loai]
        kq = mo_hinh(runs, sub)
        ti_le_tc = kq['thanh_cong'] / len(sub) * 100
        tb_lan = sub['so_lan_chay'].mean()
        print(
            f'{loai:10s} | yc={len(sub):3d} | tc={kq["thanh_cong"]:3d} ({ti_le_tc:5.1f}%) '
            f'| lan/yc={tb_lan:.2f} | cps [sim]={kq["cps"]:7,.0f} đ ({kq["cps"] / BASELINE:.2f}x)'
        )

    print('\nTỉ lệ status == ok theo từng lần thử (attempt):')
    ok_pivot = (
        runs.assign(ok=(runs['status'] == 'ok').astype(int))
        .merge(reqs[['request_id', 'loai']], on='request_id')
        .pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean')
    )
    print((ok_pivot * 100).round(1))

    print('\n--- A4 · Chi phí cố định (noi_dia + hang_nang) ---')
    co_dinh_thang = 40_000_000
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    kq_pv = mo_hinh(runs, pham_vi)
    ti_le_tc_mau = kq_pv['thanh_cong'] / len(reqs)
    for nhan, khoi_luong in [('45.000 yc/tháng', 45_000), ('Một nửa (22.500)', 22_500)]:
        viec_thang = khoi_luong * ti_le_tc_mau
        co_dinh_viec = co_dinh_thang / viec_thang
        tong_cps = kq_pv['cps'] + co_dinh_viec
        print(
            f'{nhan:18s} | viec_tc/th={viec_thang:8,.0f} | co_dinh/viec={co_dinh_viec:6,.0f} đ '
            f'| cps+cd [sim]={tong_cps:6,.0f} đ ({tong_cps / BASELINE:.2f}x)'
        )
    print('\n--- B1 · Bảng độ nhạy (đổi từng yếu tố) ---')
    goc = ket_qua['cps']
    kich_ban = {
        'Giá token gấp đôi': dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa': dict(gia_vao=13, gia_ra=65),
        'Tỉ lệ xem lại gấp đôi': dict(he_so_xem_lai=2.0),
        'Tỉ lệ xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
        'Số ca làm lại gấp đôi': dict(he_so_lam_lai=2.0),
        'Số ca làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
        'Lương nhân viên tăng 25%': dict(luong_phut=2500),
        'Chỉ cho chạy tối đa 2 lần': dict(max_lan_chay=2),
        'Chỉ cho chạy 1 lần': dict(max_lan_chay=1),
    }
    print(f'{"Gốc (A2)":28s} | {goc:8,.0f} đ [sim]')
    for ten, kw in kich_ban.items():
        cps_kb = mo_hinh(runs, reqs, **kw)['cps']
        pct = (cps_kb / goc - 1.0) * 100
        print(f'{ten:28s} | {cps_kb:8,.0f} đ [sim] | {pct:+6.1f}%')

    print('\n--- B2 · Đổi một cặp và xếp hạng ---')
    kq_cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2.0)
    pct_cap = (kq_cap['cps'] / goc - 1.0) * 100
    print(f'Giá token x2 + Xem lại x2    | {kq_cap["cps"]:8,.0f} đ [sim] | {pct_cap:+6.1f}%')
    tac_dong = [
        ('Số ca làm lại (x2)', abs(mo_hinh(runs, reqs, he_so_lam_lai=2.0)['cps'] / goc - 1.0) * 100),
        ('Tỉ lệ xem lại (x2)', abs(mo_hinh(runs, reqs, he_so_xem_lai=2.0)['cps'] / goc - 1.0) * 100),
        ('Lương nhân viên (+25%)', abs(mo_hinh(runs, reqs, luong_phut=2500)['cps'] / goc - 1.0) * 100),
        ('Giá token (x2)', abs(mo_hinh(runs, reqs, gia_vao=52, gia_ra=260)['cps'] / goc - 1.0) * 100),
    ]
    tac_dong.sort(key=lambda x: x[1], reverse=True)
    print('Xếp hạng 3 yếu tố nhạy nhất:', ' · '.join(f'{i}. {ten} ({val:.1f}%)' for i, (ten, val) in enumerate(tac_dong[:3], 1)))

    print('\n--- B3 · Giới hạn chạy lại có thật sự rẻ hơn ---')
    for gio_han in [1, 2, 3]:
        kq_gh = mo_hinh(runs, reqs, max_lan_chay=gio_han)
        khong_tc_gh = len(reqs) - kq_gh['thanh_cong']
        ca_he_thong = kq_gh['tong'] + khong_tc_gh * BASELINE
        print(
            f'Tối đa {gio_han} lần | tong [sim]={kq_gh["tong"]:10,.0f} đ '
            f'| khong_tc={khong_tc_gh:3d} | ca_he_thong [sim]={ca_he_thong:10,.0f} đ '
            f'| cps [sim]={kq_gh["cps"]:6,.0f} đ'
        )

    print('\n--- B4 · Nếu phải xem lại tất cả (noi_dia + hang_nang) ---')
    runs_pv = runs[runs['request_id'].isin(pham_vi['request_id'])]
    co_ok_pv = runs_pv.loc[runs_pv['status'] == 'ok', 'request_id'].nunique()
    so_lam_lai_pv = int((pham_vi['ket_qua'] == 'lam_lai').sum())
    phi_ai_pv = kq_pv['token'] + kq_pv['tool']
    tc_pv = kq_pv['thanh_cong']
    xem_lai_100 = co_ok_pv * 5 * LUONG_PHUT
    tb_phut_lam_lai = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean()
    for nhan, phut_ll in [('9 phút/ca (đề bài)', 9.0), (f'{tb_phut_lam_lai:.1f} phút/ca (TB dữ liệu)', tb_phut_lam_lai)]:
        lam_lai_100 = so_lam_lai_pv * phut_ll * LUONG_PHUT
        tong_100 = phi_ai_pv + xem_lai_100 + lam_lai_100
        cps_100 = tong_100 / tc_pv
        hoa_von_xem = (tc_pv * BASELINE - phi_ai_pv - lam_lai_100) / (co_ok_pv * LUONG_PHUT)
        print(
            f'{nhan:26s} | tong [sim]={tong_100:10,.0f} đ | cps [sim]={cps_100:7,.0f} đ '
            f'({cps_100 / BASELINE:.2f}x) | hoà vốn xem lại <= {hoa_von_xem:.1f} phút'
        )
    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
