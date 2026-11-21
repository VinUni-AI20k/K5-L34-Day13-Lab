"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
from statistics import NormalDist
import pandas as pd
try:
    from statsmodels.stats.proportion import proportion_effectsize
    from statsmodels.stats.power import NormalIndPower
    HAS_STATSMODELS = True
except ImportError:
    HAS_STATSMODELS = False

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
    return 1 / p if k is None else (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
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
    runs = runs[runs['request_id'].isin(reqs['request_id'])].copy()
    if max_lan_chay is not None:  # dùng cho B1, B3
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0
    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = (reqs['ket_qua'] == 'thanh_cong').sum()
    return dict(token=tien_token.sum(), tool=tien_tool.sum(),
                chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
                xem_lai=xem_lai, lam_lai=lam_lai, tong=tong,
                thanh_cong=thanh_cong, cps=tong / thanh_cong,
                hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs))


# ---------- Nhiệm vụ D · Cỡ mẫu và phân tích phương án chia nhóm pilot (CP4) ----------
def co_mau(p1, p2, alpha=0.05, power=0.80):
    """Cỡ mẫu mỗi nhóm khi so sánh hai tỉ lệ p1, p2 (kiểm định hai phía)."""
    za = NormalDist().inv_cdf(1 - alpha / 2)
    zb = NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    tu = za * math.sqrt(2 * pb * (1 - pb)) + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))
    return math.ceil((tu ** 2) / ((p2 - p1) ** 2))


def he_so_thiet_ke(m, icc=0.02):
    """Hệ số thiết kế DE = 1 + (m - 1) * ICC khi chia theo cụm kích thước m."""
    return 1 + (m - 1) * icc


def co_mau_hieu_dung(c, m, icc=0.02):
    """Cỡ mẫu hiệu dụng mỗi nhóm với c cụm, mỗi cụm m quan sát."""
    return (c * m) / he_so_thiet_ke(m, icc)


def so_yc_moi_cum_toi_thieu(n_muc_tieu, c, icc=0.02):
    """Tìm m nhỏ nhất để c*m / (1 + (m - 1)*icc) >= n_muc_tieu."""
    mau = c - icc * n_muc_tieu
    if mau <= 0:
        return None  # không tồn tại m hữu hạn vì n_muc_tieu >= c / icc
    return math.ceil(n_muc_tieu * (1 - icc) / mau)


def chay_nhiem_vu_d(reqs, baseline=0.70, mde=0.05, mde_thay_the=0.06,
                    alpha=0.05, power=0.80, icc=0.02):
    """Tính D1 (5 câu cỡ mẫu), phân tích 3 phương án chia nhóm, D2 và tỉ lệ mở lại 7 ngày."""
    n_5 = co_mau(baseline, baseline + mde, alpha=alpha, power=power)
    de_75 = he_so_thiet_ke(75, icc)
    n_b = math.ceil(n_5 * de_75)
    so_nv_moi_nhom = math.ceil(n_b / 75)
    gioi_han_20nv = 20 / icc
    gioi_han_6depot = 6 / icc

    n_6 = co_mau(baseline, baseline + mde_thay_the, alpha=alpha, power=power)
    m_e = so_yc_moi_cum_toi_thieu(n_6, c=20, icc=icc)
    de_e = he_so_thiet_ke(m_e, icc)
    n_hieu_dung_e = co_mau_hieu_dung(20, m_e, icc)
    if HAS_STATSMODELS:
        power_5_tai_n6 = NormalIndPower().power(
            effect_size=proportion_effectsize(baseline + mde, baseline),
            nobs1=n_6,
            alpha=alpha,
        )
        power_str = f"{power_5_tai_n6:.2f}"
    else:
        power_str = "0.64 (xấp xỉ khi không có statsmodels)"

    reopen_all = reqs['mo_lai_trong_7_ngay'].mean()
    sub_pilot = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    reopen_pilot = sub_pilot['mo_lai_trong_7_ngay'].mean()

    print('\n=== NHIỆM VỤ D1 · CỠ MẪU (baseline=0.70, +5 điểm, alpha=0.05, power=0.80, ICC=0.02) ===')
    print(f'a) Chia theo yêu cầu: {n_5:,} yêu cầu mỗi nhóm')
    print(f'b) Theo nhân viên (m=75): DE = {de_75:.2f}, n = {n_b:,}/nhóm -> {so_nv_moi_nhom} người/nhóm (tổng {so_nv_moi_nhom * 2} > 40: KHÔNG ĐỦ NGƯỜI)')
    print(f'c) 20 nhân viên mỗi nhóm: cỡ mẫu hiệu dụng tối đa < c/ICC = {gioi_han_20nv:,.0f} < {n_5:,} (KHÔNG ĐẠT cho +5 điểm)')
    print(f'd) 6 depot mỗi nhóm: cỡ mẫu hiệu dụng tối đa < c/ICC = {gioi_han_6depot:,.0f}')
    print(f'e) Mức chênh +6 điểm (n = {n_6:,}/nhóm), 20 nhân viên/nhóm: cần m >= {m_e} yêu cầu/người (DE = {de_e:.2f}, n_eff = {n_hieu_dung_e:.1f})')
    print(f'   Đánh đổi: nếu tác động thật chỉ +5 điểm ở n = {n_6:,}, power giảm còn {power_str}')

    print('\n=== PHÂN TÍCH 3 PHƯƠNG ÁN CHIA NHÓM PILOT ===')
    print('- Theo yêu cầu      : Đủ mẫu (1.251/nhóm) nhưng cùng nhân viên vừa dùng vừa không dùng -> tràn tác động cao, loại.')
    print('- Theo nhân viên 20+20: Tách tác động tốt (20 cụm/nhóm, ngẫu nhiên phân tầng theo depot), đạt +6 điểm khi m >= 299 -> CHỌN.')
    print('- Theo depot 6+6    : Chỉ 6 cụm (< 20) và n_eff tối đa < 300 -> không đủ mẫu, loại.')

    print('\n=== NHIỆM VỤ D2 · 5 CÂU KIỂM TRA TÁCH ĐƯỢC TÁC ĐỘNG (unit = staff, 20 + 20) ===')
    print('1. Đối chứng chạy cùng thời gian: Có (20 nhân viên đối chứng làm cùng tuần, cùng depot).')
    print('2. Chia ngẫu nhiên hay người chọn: Bốc thăm ngẫu nhiên bằng code với seed chốt trước, phân tầng theo depot.')
    print('3. Ảnh hưởng gián tiếp & cách giảm: Có rủi ro trao đổi trong depot; giảm bằng phân quyền theo staff_id và log truy cập.')
    print('4. Viết trước chỉ số/ngưỡng/ngày quyết định: Có, chốt trước khi bắt đầu pilot.')
    print('5. Ít nhất 20 cụm mỗi nhóm: Có, đúng 20 nhân viên/nhóm.')

    print('\n=== TỈ LỆ MỞ LẠI TRONG 7 NGÀY HIỆN TẠI (CĂN CỨ LUẬT DỪNG AN TOÀN) ===')
    print(f'- Toàn bộ mẫu (1.200 yêu cầu): {reopen_all * 100:.2f}% ({int(reqs["mo_lai_trong_7_ngay"].sum())}/{len(reqs)})')
    print(f'- Phạm vi pilot noi_dia + hang_nang ({len(sub_pilot)} yêu cầu): {reopen_pilot * 100:.2f}% ({int(sub_pilot["mo_lai_trong_7_ngay"].sum())}/{len(sub_pilot)})')

    return dict(
        n_5=n_5, de_75=de_75, n_b=n_b, so_nv_moi_nhom=so_nv_moi_nhom,
        gioi_han_20nv=gioi_han_20nv, gioi_han_6depot=gioi_han_6depot,
        n_6=n_6, m_e=m_e, de_e=de_e,
        reopen_all=reopen_all, reopen_pilot=reopen_pilot,
    )


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)

    print('=== A1: BA PHÉP THỬ ĐÁP ÁN BIẾT TRƯỚC ===')
    kiem_tra_dap_an_biet_truoc()

    print('\n=== A2: MÔ HÌNH CHI PHÍ TỪ TRACE ===')
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:15s} {gia_tri:>14,.2f}')
    print(f"Chi phí mỗi việc thành công gấp: {ket_qua['cps'] / ket_qua['hoa_don_moi_yc']:.1f} lần hoá đơn/yc")

    # TODO CP1 · Nhiệm vụ A3: tính lại theo từng giá trị của cột loai.
    print('\n=== A3: TÁCH THEO LOẠI YÊU CẦU ===')
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        sub_reqs = reqs[reqs['loai'] == loai]
        kq_loai = mo_hinh(runs, sub_reqs)
        so_yc = len(sub_reqs)
        ti_le_tc = kq_loai['thanh_cong'] / so_yc * 100
        lan_chay_tb = sub_reqs['so_lan_chay'].mean()
        cps = kq_loai['cps']
        so_voi_12k = cps / BASELINE
        print(f'{loai:10s} | YC: {so_yc:4d} | TC: {ti_le_tc:5.1f}% | Lần chạy/YC: {lan_chay_tb:.2f} | CPS [sim]: {cps:8,.0f} đ | So 12k: {so_voi_12k:.2f}×')

    # Tỉ lệ ok theo từng lần thử cho quoc_te
    pivot_qt = runs.merge(reqs[['request_id', 'loai']]).pivot_table(
        index='loai', columns='attempt', values='status', aggfunc=lambda s: (s == 'ok').mean()
    )
    print('\nTỉ lệ ok theo attempt:')
    print(pivot_qt)

    # TODO CP2 · Nhiệm vụ B: đổi từng yếu tố, ghi vào bảng độ nhạy.
    print('\n=== B1: ĐỔI TỪNG YẾU TỐ ===')
    kich_ban = {
        'Giá token gấp đôi':        dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa':   dict(gia_vao=13, gia_ra=65),
        'Xem lại gấp đôi':          dict(he_so_xem_lai=2),
        'Xem lại giảm một nửa':     dict(he_so_xem_lai=0.5),
        'Làm lại gấp đôi':          dict(he_so_lam_lai=2),
        'Làm lại giảm một nửa':     dict(he_so_lam_lai=0.5),
        'Lương tăng 25%':           dict(luong_phut=2500),
        'Tối đa 2 lần chạy':        dict(max_lan_chay=2),
        'Chỉ 1 lần chạy':           dict(max_lan_chay=1),
    }
    goc = ket_qua['cps']
    print(f"{'Gốc (A2)':28s} {goc:8,.0f} đ    +0.0%")
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        print(f'{ten:28s} {cps:8,.0f} đ {(cps / goc - 1) * 100:+6.1f}%')

    print('\n=== B2: ĐỔI MỘT CẶP VÀ XẾP HẠNG ===')
    cps_cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    print(f"{'Token x2 + Xem lại x2':28s} {cps_cap:8,.0f} đ {(cps_cap / goc - 1) * 100:+6.1f}%")

    print('\n=== B3: GIỚI HẠN CHẠY LẠI CÓ THẬT SỰ RẺ HƠN ===')
    for m in [1, 2, 3]:
        kw = dict(max_lan_chay=m) if m < 3 else dict()
        kq_m = mo_hinh(runs, reqs, **kw)
        khong_tc = len(reqs) - kq_m['thanh_cong']
        ca_he_thong = kq_m['tong'] + BASELINE * khong_tc
        print(f"Giới hạn {m} lần | Tổng trợ lý: {kq_m['tong']:10,.0f} đ | Không TC: {khong_tc:3d} | Cả hệ thống: {ca_he_thong:10,.0f} đ | CPS: {kq_m['cps']:8,.0f} đ")

    print('\n=== B4: NẾU PHẢI XEM LẠI TẤT CẢ (noi_dia + hang_nang) ===')
    sub_scope = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    sub_runs = runs[runs['request_id'].isin(sub_scope['request_id'])]
    runs_ok_reqs = sub_runs[sub_runs['status'] == 'ok']['request_id'].unique()
    ca_lam_lai = (sub_scope['phut_lam_lai_simulated'] > 0).sum()
    tien_token_tool = (sub_runs['tokens_in']/1000*GIA_VAO + sub_runs['tokens_out']/1000*GIA_RA + sub_runs['tool_calls']*GIA_TOOL).sum()
    tc_scope = (sub_scope['ket_qua'] == 'thanh_cong').sum()
    tong_9p = tien_token_tool + len(runs_ok_reqs)*5*LUONG_PHUT + ca_lam_lai*9*LUONG_PHUT
    cps_9p = tong_9p / tc_scope
    tong_15p = tien_token_tool + len(runs_ok_reqs)*5*LUONG_PHUT + ca_lam_lai*15.3*LUONG_PHUT
    cps_15p = tong_15p / tc_scope
    print(f"Xem lại 100% với 9 phút làm lại : Tổng = {tong_9p:10,.0f} đ | CPS = {cps_9p:8,.0f} đ ({cps_9p/BASELINE:.2f}×)")
    print(f"Xem lại 100% với 15.3 phút làm lại: Tổng = {tong_15p:10,.0f} đ | CPS = {cps_15p:8,.0f} đ ({cps_15p/BASELINE:.2f}×)")

    # CP4 · Nhiệm vụ D: cỡ mẫu, phân tích phương án chia nhóm pilot và D2 của Người 2
    chay_nhiem_vu_d(reqs)
