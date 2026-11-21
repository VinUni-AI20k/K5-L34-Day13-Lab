"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python lab13.py. Không cần khoá API.
Dữ liệu và các giả định trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import sys
from statistics import NormalDist
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if not 0 < p <= 1 or (k is not None and (not isinstance(k, int) or k < 1)):
        raise ValueError('p phải thuộc (0, 1], k phải là số nguyên dương hoặc None')
    return 1 / p if k is None else (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    so_lan_chay_ky_vong(p, k)  # kiểm tra tham số
    return 1.0 if k is None else 1 - (1 - p) ** k


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
    token = runs['tokens_in'] * gia_vao / 1000 + runs['tokens_out'] * gia_ra / 1000
    tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = token.sum() + tool.sum() + xem_lai + lam_lai
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    return dict(token=token.sum(), tool=tool.sum(),
                chay_lai=(token + tool)[runs['attempt'] > 1].sum(),
                xem_lai=xem_lai, lam_lai=lam_lai, tong=tong,
                thanh_cong=thanh_cong, cps=tong / thanh_cong if thanh_cong else float('inf'),
                hoa_don_moi_yc=(token.sum() + tool.sum()) / len(reqs))


def co_mau(p1, p2, alpha=0.05, power=0.8):
    """Cỡ mẫu mỗi nhóm theo công thức so hai tỉ lệ trong đề."""
    za = NormalDist().inv_cdf(1 - alpha / 2)
    zb = NormalDist().inv_cdf(power)
    trung_binh = (p1 + p2) / 2
    tu = za * math.sqrt(2 * trung_binh * (1 - trung_binh))
    tu += zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))
    return math.ceil(tu ** 2 / (p2 - p1) ** 2)


if __name__ == '__main__':
    # Windows có thể dùng mã trang không hỗ trợ tiếng Việt khi chuyển hướng output.
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    print('\nA2 · Chi phí toàn mẫu (đ)')
    for ten, gia_tri in ket_qua.items():
        nhan = ' [simulated]' if ten in ('xem_lai', 'lam_lai', 'tong', 'cps') else ''
        print(f'{ten:18s} {gia_tri:>14,.2f}{nhan}')
    tong_he_thong = ket_qua['tong'] + (len(reqs) - ket_qua['thanh_cong']) * BASELINE
    print(f'CPS / hóa đơn mỗi yêu cầu: {ket_qua["cps"] / ket_qua["hoa_don_moi_yc"]:.2f} lần [simulated]')
    print(f'Làm lại / tổng: {ket_qua["lam_lai"] / ket_qua["tong"]:.2%} [simulated]')
    print(f'Chi phí cả hệ thống / yêu cầu: {tong_he_thong / len(reqs):,.2f} đ [simulated]')

    print('\nA3 · Theo loại (chi phí và tỉ số: simulated)')
    print('Loại          Số YC  Thành công  Lần chạy/YC     CPS (đ)   /12.000')
    for loai in ('noi_dia', 'hang_nang', 'quoc_te', 'doi_tac'):
        nhom = reqs[reqs['loai'] == loai]
        kq = mo_hinh(runs, nhom)
        print(f'{loai:12s} {len(nhom):6d} {kq["thanh_cong"] / len(nhom):11.1%} '
              f'{nhom["so_lan_chay"].mean():12.2f} {kq["cps"]:12,.0f} {kq["cps"] / BASELINE:9.2f}')
    lan = runs.merge(reqs[['request_id', 'loai']], on='request_id', validate='many_to_one')
    lan['ok'] = lan['status'].eq('ok')
    print('\nTỉ lệ ok theo lần chạy, tính trên các ca có lần chạy đó:')
    print(lan.pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean').to_string(float_format=lambda x: f'{x:.1%}'))

    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    pv = mo_hinh(runs, pham_vi)
    print('\nA4 · Cố định: lượng toàn hệ thống, giữ cơ cấu mẫu [simulated]')
    for luong in (45000, 22500):
        thanh_cong_thang = luong * pv['thanh_cong'] / len(reqs)
        co_dinh = 40000000 / thanh_cong_thang
        print(f'{luong:,} YC/tháng; {thanh_cong_thang:,.0f} việc thành công trong phạm vi; '
              f'cố định {co_dinh:,.0f} đ/việc; CPS + cố định {pv["cps"] + co_dinh:,.0f} đ')

    kich_ban = {
        'Giá token gấp đôi': dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa': dict(gia_vao=13, gia_ra=65),
        'Xem lại gấp đôi': dict(he_so_xem_lai=2),
        'Xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
        'Làm lại gấp đôi': dict(he_so_lam_lai=2),
        'Làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
        'Lương tăng 25%': dict(luong_phut=2500),
        'Tối đa 2 lần': dict(max_lan_chay=2),
        'Tối đa 1 lần': dict(max_lan_chay=1),
        'Token và xem lại gấp đôi': dict(gia_vao=52, gia_ra=260, he_so_xem_lai=2),
    }
    print('\nB1–B2 · Độ nhạy [simulated]')
    for ten, kwargs in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kwargs)['cps']
        print(f'{ten:30s} {cps:10,.0f} đ {cps / ket_qua["cps"] - 1:+8.1%}')

    print('\nB3 · Cả hệ thống = trợ lý + 12.000 đ/YC không thành công [simulated]')
    for k in (1, 2, 3):
        kq = mo_hinh(runs, reqs, max_lan_chay=k)
        khong_thanh_cong = len(reqs) - kq['thanh_cong']
        he_thong = kq['tong'] + khong_thanh_cong * BASELINE
        print(f'{k} lần: trợ lý {kq["tong"]:,.0f} đ; không thành công {khong_thanh_cong}; '
              f'cả hệ thống {he_thong:,.0f} đ; CPS {kq["cps"]:,.0f} đ')

    # B4 sử dụng thời gian xem lại và làm lại theo giả định riêng của đề.
    ok = runs[(runs['request_id'].isin(pham_vi['request_id'])) & (runs['status'] == 'ok')]['request_id'].nunique()
    so_lam_lai = int((pham_vi['ket_qua'] == 'lam_lai').sum())
    print('\nB4 · Xem lại 100%, 5 phút/YC có ít nhất một lần ok [simulated]')
    for phut in (9, 15.3):
        tong = pv['token'] + pv['tool'] + ok * 5 * LUONG_PHUT + so_lam_lai * phut * LUONG_PHUT
        cps = tong / pv['thanh_cong']
        print(f'{ok} YC xem lại; {so_lam_lai} ca làm lại × {phut:g} phút: {cps:,.0f} đ/việc, {cps / BASELINE:.2f} lần 12.000 đ')

    n5, n6, icc = co_mau(0.70, 0.75), co_mau(0.70, 0.76), 0.02
    de75 = 1 + 74 * icc
    n_cum = math.ceil(n5 * de75)
    m6 = math.ceil(n6 * (1 - icc) / (20 - n6 * icc))
    print('\nD1 · Cỡ mẫu mỗi nhóm: alpha=0,05, power=0,80, ICC=0,02')
    print(f'a) Chia theo yêu cầu, chênh 5 điểm: {n5:,} yêu cầu')
    print(f'b) Theo nhân viên, 75 YC/người: DE={de75:.2f}; {n_cum:,} YC, {math.ceil(n_cum / 75)} nhân viên')
    print(f'c) 20 nhân viên: cỡ mẫu hiệu dụng luôn < {20 / icc:,.0f}')
    print(f'd) 6 depot: cỡ mẫu hiệu dụng luôn < {6 / icc:,.0f}')
    print(f'e) Chênh 6 điểm: {n6:,} quan sát độc lập; 20 nhân viên cần ≥ {m6} YC/người; DE={1 + (m6 - 1) * icc:.2f}')

    print('\nE1 · Chỉ số trong mẫu; không suy ra tác động nhân quả')
    chinh = ((reqs['dong_trong_24h'] == 1) & (reqs['mo_lai_trong_7_ngay'] == 0)).sum()
    xem = reqs[reqs['duoc_xem_lai'] == 1]
    bo_qua = xem['quyet_dinh_xem_lai'].isin(['sua', 'bo']).sum()
    mo_lai = reqs['mo_lai_trong_7_ngay'].sum()
    print(f'Đóng trong 24h và không mở lại 7 ngày: {chinh}/{len(reqs)} = {chinh / len(reqs):.2%}')
    print(f'Sửa hoặc bỏ gợi ý trong số đã xem lại: {bo_qua}/{len(xem)} = {bo_qua / len(xem):.2%}')
    print(f'Mở lại trong 7 ngày: {mo_lai}/{len(reqs)} = {mo_lai / len(reqs):.2%}')
    print(f'Mở lại trong phạm vi pilot: {pham_vi["mo_lai_trong_7_ngay"].sum()}/{len(pham_vi)} = {pham_vi["mo_lai_trong_7_ngay"].mean():.2%}')
