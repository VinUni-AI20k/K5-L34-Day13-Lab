"""Lab 13 · Phần tính của Thành viên 4 (không sửa lab13.py: file đó do Thành viên 1 giữ).
Chạy trong thư mục src/: python3 tv4_tinh_so.py
Mỗi checkpoint một hàm; số in ra để gửi cho người giữ file tương ứng.
Mọi số tính từ cột *_simulated đều ghi nhãn [simulated].
"""
import pandas as pd

GIA_VAO, GIA_RA, GIA_TOOL = 26, 130, 15   # đ / 1.000 token vào, đ / 1.000 token ra, đ / lần gọi tool
LUONG_PHUT = 2000                          # đ / phút nhân viên
BASELINE = 12000                           # đ / yêu cầu khi nhân viên tự làm (6 phút)
CO_DINH_THANG = 40_000_000                 # chi phí cố định của trợ lý, đ / tháng
YC_THANG = 45_000                          # yêu cầu hoàn phí mỗi tháng (1.500 / ngày)
PHAM_VI = ['noi_dia', 'hang_nang']         # phạm vi pilot đề xuất từ A3


def doc_du_lieu():
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    return runs, reqs


def mo_hinh(runs, reqs, gia_vao=GIA_VAO, gia_ra=GIA_RA, gia_tool=GIA_TOOL, luong_phut=LUONG_PHUT,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0):
    """Bản tính độc lập của TV4 để đối chiếu với mo_hinh của TV1.
    Tử số: token + tool của MỌI lần chạy (kể cả lỗi) + phút xem lại + phút làm lại.
    Mẫu số: số yêu cầu ket_qua == 'thanh_cong'."""
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    token = (runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra).sum()
    tool = (runs['tool_calls'] * gia_tool).sum()
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = token + tool + xem_lai + lam_lai
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    return dict(token=token, tool=tool, xem_lai=xem_lai, lam_lai=lam_lai, tong=tong,
                so_yc=len(reqs), thanh_cong=thanh_cong, cps=tong / thanh_cong)


def d(x):
    """Định dạng số tiền kiểu Việt Nam: 1.234.567"""
    return f'{x:,.0f}'.replace(',', '.')


def lan(x):
    """Bội số so với 12.000 đ, dấu phẩy thập phân: 0,38×"""
    return f'{x:.2f}'.replace('.', ',') + '×'


def cp1_a4(runs, reqs):
    print('=== CP1 · A4 · Chi phí cố định cho phạm vi noi_dia + hang_nang ===')
    pv = reqs[reqs['loai'].isin(PHAM_VI)]
    m = mo_hinh(runs, pv)
    ti_le_tc = m['thanh_cong'] / len(reqs)          # việc thành công trong phạm vi / toàn mẫu 1.200
    print(f"Phạm vi: {m['so_yc']} yêu cầu, {m['thanh_cong']} việc thành công / {len(reqs)} yêu cầu của mẫu")
    print(f"Tổng chi phí trợ lý trong phạm vi: {d(m['tong'])} đ [simulated]")
    print(f"Chi phí mỗi việc thành công (chưa cố định): {d(m['cps'])} đ [simulated]")
    print()
    print('| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc '
          '| Chi phí mỗi việc thành công + cố định | So với 12.000 đ |')
    print('| --- | ---: | ---: | ---: | ---: |')
    ket_qua = {}
    for ten, yc_thang in [('45.000 yêu cầu/tháng', YC_THANG), ('Một nửa khối lượng (22.500)', YC_THANG / 2)]:
        tc_thang = yc_thang * ti_le_tc
        co_dinh = CO_DINH_THANG / tc_thang
        tong_viec = m['cps'] + co_dinh
        ket_qua[ten] = tong_viec
        print(f'| {ten} | {d(tc_thang)} | {d(co_dinh)} đ | {d(tong_viec)} đ [simulated] '
              f'| {lan(tong_viec / BASELINE)} [simulated] |')

    # Góc nhìn cả hệ thống: ca không thành công trong phạm vi do nhân viên làm thay (12.000 đ/ca)
    khong_tc = m['so_yc'] - m['thanh_cong']
    yc_pv_thang = YC_THANG * m['so_yc'] / len(reqs)
    he_thong = (m['tong'] + khong_tc * BASELINE) / m['so_yc'] + CO_DINH_THANG / yc_pv_thang
    print()
    print(f'Đối chiếu cả hệ thống (cộng {khong_tc} ca nhân viên làm thay × 12.000 đ, cố định chia '
          f'{d(yc_pv_thang)} yc/tháng): {d(he_thong)} đ / yêu cầu = {lan(he_thong / BASELINE)} [simulated]')

    # Hoà vốn: cps + 40tr / (yc_thang × ti_le_tc) = 12.000  →  yc_thang = 40tr / ((12.000 − cps) × ti_le_tc)
    yc_hoa_von = CO_DINH_THANG / ((BASELINE - m['cps']) * ti_le_tc)
    print(f'Hoà vốn với 12.000 đ khi khối lượng ≈ {d(yc_hoa_von)} yêu cầu/tháng '
          f'({yc_hoa_von / YC_THANG:.0%} của 45.000) [simulated]; dưới mức này chi phí cố định đổi kết luận')
    print()
    return m, ket_qua


if __name__ == '__main__':
    runs, reqs = doc_du_lieu()
    cp1_a4(runs, reqs)
