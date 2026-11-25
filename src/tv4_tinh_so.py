"""Lab 13 · Phần tính của Thành viên 4 (không sửa lab13.py: file đó do Thành viên 1 giữ).
Chạy trong thư mục src/: python3 tv4_tinh_so.py
Mỗi checkpoint một hàm; số in ra để gửi cho người giữ file tương ứng
(A4, B2, B4 → Thành viên 2 giữ bang_chi_phi.md; rủi ro kinh tế → chi_so.md ở CP5).
Mọi số tính từ cột *_simulated đều ghi nhãn [simulated].
"""
import pandas as pd

from lab13 import mo_hinh, BASELINE, LUONG_PHUT   # dùng đúng mô hình của Thành viên 1

CO_DINH_THANG = 40_000_000     # chi phí cố định của trợ lý, đ / tháng
YC_THANG = 45_000              # yêu cầu hoàn phí mỗi tháng (1.500 / ngày)
PHAM_VI = ['noi_dia', 'hang_nang']
PHUT_XEM_LAI_100 = 5           # B4 (đề bài): mỗi lần xem lại 5 phút
PHUT_LAM_LAI_DE = 9            # B4 (đề bài): mỗi ca làm lại 9 phút


def doc_du_lieu():
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    return runs, reqs


def d(x):
    """Định dạng số tiền kiểu Việt Nam: 1.234.567"""
    return f'{x:,.0f}'.replace(',', '.')


def lan(x):
    """Bội số so với 12.000 đ, dấu phẩy thập phân: 0,38×"""
    return f'{x:.2f}'.replace('.', ',') + '×'


def so(x, so_le=1):
    """Số thập phân dấu phẩy: 15,3"""
    return f'{x:.{so_le}f}'.replace('.', ',')


def pt(x, so_le=1):
    """Phần trăm có dấu, dấu phẩy thập phân: +46,3%"""
    return f'{x * 100:+.{so_le}f}%'.replace('.', ',')


# ---------- CP1 · A4 ----------
def cp1_a4(runs, reqs):
    print('=== CP1 · A4 · Chi phí cố định cho phạm vi noi_dia + hang_nang ===')
    pv = reqs[reqs['loai'].isin(PHAM_VI)]
    m = mo_hinh(runs, pv)
    so_yc = len(pv)
    ti_le_tc = m['thanh_cong'] / len(reqs)          # việc thành công trong phạm vi / toàn mẫu 1.200
    print(f"Phạm vi: {so_yc} yêu cầu, {m['thanh_cong']} việc thành công / {len(reqs)} yêu cầu của mẫu")
    print(f"Tổng chi phí trợ lý trong phạm vi: {d(m['tong'])} đ [simulated]")
    print(f"Chi phí mỗi việc thành công (chưa cố định): {d(m['cps'])} đ [simulated]")
    print()
    print('| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc '
          '| Chi phí mỗi việc thành công + cố định | So với 12.000 đ |')
    print('| --- | ---: | ---: | ---: | ---: |')
    for ten, yc_thang in [('45.000 yêu cầu/tháng', YC_THANG), ('Một nửa khối lượng (22.500)', YC_THANG / 2)]:
        tc_thang = yc_thang * ti_le_tc
        co_dinh = CO_DINH_THANG / tc_thang
        tong_viec = m['cps'] + co_dinh
        print(f'| {ten} | {d(tc_thang)} | {d(co_dinh)} đ | {d(tong_viec)} đ [simulated] '
              f'| {lan(tong_viec / BASELINE)} [simulated] |')

    # Góc nhìn cả hệ thống: ca không thành công trong phạm vi do nhân viên làm thay (12.000 đ/ca)
    khong_tc = so_yc - m['thanh_cong']
    yc_pv_thang = YC_THANG * so_yc / len(reqs)
    he_thong = (m['tong'] + khong_tc * BASELINE) / so_yc + CO_DINH_THANG / yc_pv_thang
    print()
    print(f'Đối chiếu cả hệ thống (cộng {khong_tc} ca nhân viên làm thay × 12.000 đ, cố định chia '
          f'{d(yc_pv_thang)} yc/tháng): {d(he_thong)} đ / yêu cầu = {lan(he_thong / BASELINE)} [simulated]')

    # Hoà vốn: cps + 40tr / (yc_thang × ti_le_tc) = 12.000  →  yc_thang = 40tr / ((12.000 − cps) × ti_le_tc)
    yc_hoa_von = CO_DINH_THANG / ((BASELINE - m['cps']) * ti_le_tc)
    print(f'Hoà vốn với 12.000 đ khi khối lượng ≈ {d(yc_hoa_von)} yêu cầu/tháng '
          f'({yc_hoa_von / YC_THANG:.0%} của 45.000) [simulated]; dưới mức này chi phí cố định đổi kết luận')
    print()


# ---------- CP2 · B2 ----------
def cp2_b2(runs, reqs):
    print('=== CP2 · B2 · Đổi một cặp: giá token gấp đôi + tỉ lệ xem lại gấp đôi ===')
    goc = mo_hinh(runs, reqs)['cps']
    token2 = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260)['cps']
    xem2 = mo_hinh(runs, reqs, he_so_xem_lai=2)['cps']
    cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    tong_rieng = (token2 / goc - 1) + (xem2 / goc - 1)
    print(f'Gốc (A2): {d(goc)} đ [simulated]')
    print(f'Riêng giá token gấp đôi: {d(token2)} đ ({pt(token2 / goc - 1)}) [simulated]')
    print(f'Riêng xem lại gấp đôi:   {d(xem2)} đ ({pt(xem2 / goc - 1)}) [simulated]')
    print(f'Cả cặp:                  {d(cap)} đ ({pt(cap / goc - 1)}) [simulated]')
    print(f'Tổng hai tác động riêng: {pt(tong_rieng)} → bằng tác động của cặp vì mô hình cộng tuyến tính')
    print()


# ---------- CP2 · B4 ----------
def cp2_b4(runs, reqs):
    print('=== CP2 · B4 · Nếu phải xem lại 100% (noi_dia + hang_nang) ===')
    pv = reqs[reqs['loai'].isin(PHAM_VI)]
    runs_pv = runs[runs['request_id'].isin(pv['request_id'])]
    co_ok = runs_pv.loc[runs_pv['status'] == 'ok', 'request_id'].nunique()   # có ít nhất 1 lần chạy ok → có gợi ý để xem lại
    so_lam_lai = int((pv['ket_qua'] == 'lam_lai').sum())
    thanh_cong = int((pv['ket_qua'] == 'thanh_cong').sum())
    m = mo_hinh(runs, pv)
    token_tool = m['token'] + m['tool']
    tien_xem = co_ok * PHUT_XEM_LAI_100 * LUONG_PHUT

    # Phút làm lại thật trong cột simulated (mọi ca lam_lai của mẫu)
    phut_ll = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated']

    print(f'1. Yêu cầu có ≥ 1 lần chạy ok: {co_ok} × {PHUT_XEM_LAI_100} phút × {d(LUONG_PHUT)} đ '
          f'= {d(tien_xem)} đ [simulated]')
    print(f'2. Token + tool mọi lần chạy của {len(pv)} yêu cầu: {d(token_tool)} đ (đo từ trace)')
    print(f'   Việc thành công: {thanh_cong}; ca lam_lai: {so_lam_lai} '
          f'(tỉ lệ làm lại trong phạm vi {so(so_lam_lai / len(pv) * 100)}%)')
    print(f'   Phút làm lại trong cột simulated: trung bình {so(phut_ll.mean())}, '
          f'trung vị {so(phut_ll.median())} ({len(phut_ll)} ca lam_lai toàn mẫu) [simulated]')
    print()
    print('| Phút làm lại mỗi ca | Tiền làm lại | Tổng | Chi phí mỗi việc thành công | So với 12.000 đ '
          '| Hoà vốn: phút xem lại tối đa |')
    print('| --- | ---: | ---: | ---: | ---: | ---: |')
    for nhan, phut in [(f'{PHUT_LAM_LAI_DE} (đề bài)', PHUT_LAM_LAI_DE),
                       (f'{so(phut_ll.mean())} (trung bình dữ liệu)', round(phut_ll.mean(), 1))]:
        tien_ll = so_lam_lai * phut * LUONG_PHUT
        tong = tien_xem + tien_ll + token_tool
        cps = tong / thanh_cong
        hoa_von = (BASELINE * thanh_cong - token_tool - tien_ll) / (co_ok * LUONG_PHUT)
        print(f'| {nhan} | {d(tien_ll)} đ | {d(tong)} đ | {d(cps)} đ [simulated] | {lan(cps / BASELINE)} [simulated] '
              f'| {so(hoa_von)} phút [simulated] |')
    print(f'Tiền xem lại chiếm {tien_xem / (tien_xem + so_lam_lai * PHUT_LAM_LAI_DE * LUONG_PHUT + token_tool):.0%} '
          f'tổng chi phí khi xem lại 100% (làm lại 9 phút) [simulated]')
    print()


# ---------- CP2 → CP5 · Số cho rủi ro kinh tế ----------
def cp2_rui_ro(runs, reqs):
    print('=== CP2 → CP5 · Số chuyển tiếp cho rủi ro kinh tế (chi_so.md, hồ sơ mục 7) ===')
    goc = mo_hinh(runs, reqs)['cps']
    ll2 = mo_hinh(runs, reqs, he_so_lam_lai=2)['cps']
    xl2 = mo_hinh(runs, reqs, he_so_xem_lai=2)['cps']
    pv = reqs[reqs['loai'].isin(PHAM_VI)]
    ti_le_ll = (pv['ket_qua'] == 'lam_lai').mean()
    ti_le_xem = pv['duoc_xem_lai'].mean()
    print(f'- Số ca làm lại gấp đôi: {d(ll2)} đ ({pt(ll2 / goc - 1)}) [simulated]; '
          f'tỉ lệ làm lại trong phạm vi hiện tại {so(ti_le_ll * 100)}%')
    print(f'- Tỉ lệ xem lại gấp đôi: {d(xl2)} đ ({pt(xl2 / goc - 1)}) [simulated]; '
          f'tỉ lệ được xem lại trong phạm vi hiện tại {so(ti_le_xem * 100)}%')
    print('- Xem lại 100%: xem bảng B4 ở trên')
    print('- Khối lượng thấp: xem bảng A4 (cố định 1.185 → 2.370 đ/việc khi khối lượng giảm một nửa)')
    print()


if __name__ == '__main__':
    runs, reqs = doc_du_lieu()
    cp1_a4(runs, reqs)
    cp2_b2(runs, reqs)
    cp2_b4(runs, reqs)
    cp2_rui_ro(runs, reqs)
