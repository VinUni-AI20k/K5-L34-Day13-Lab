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
    raise NotImplementedError('VIẾT Ở ĐÂY')


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    raise NotImplementedError('VIẾT Ở ĐÂY')


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    raise NotImplementedError('VIẾT Ở ĐÂY')


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
    raise NotImplementedError('VIẾT Ở ĐÂY')


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:12s} {gia_tri:>14,.0f}')
    # TODO CP1 · Nhiệm vụ A3: tính lại theo từng giá trị của cột loai.
    # TODO CP2 · Nhiệm vụ B: đổi từng yếu tố, ghi vào bảng độ nhạy.
    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    tinh_co_mau_cp4(reqs)


# ---------- Nhiệm vụ D · Cỡ mẫu và kiểm tra an toàn (CP4) ----------
def co_mau_hai_ti_le(p1, p2, alpha=0.05, power=0.80):
    """Cỡ mẫu mỗi nhóm khi so hai tỉ lệ p1, p2."""
    from statistics import NormalDist
    za = NormalDist().inv_cdf(1 - alpha / 2)
    zb = NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    return math.ceil(
        (za * math.sqrt(2 * pb * (1 - pb)) + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2
        / (p2 - p1) ** 2
    )


def tinh_co_mau_cp4(reqs=None, p1=0.70, mde=0.05, alpha=0.05, power=0.80, icc=0.02):
    """Tính năm câu D1 và tỉ lệ mở lại hiện tại cho pilot_plan.yaml."""
    n_5pt = co_mau_hai_ti_le(p1, p1 + mde, alpha=alpha, power=power)
    de_75 = 1 + (75 - 1) * icc
    n_b = math.ceil(n_5pt * de_75)
    staff_b = math.ceil(n_b / 75)
    max_eff_staff = 20 / icc
    max_eff_depot = 6 / icc

    n_6pt = co_mau_hai_ti_le(p1, p1 + 0.06, alpha=alpha, power=power)
    m_e = math.ceil(n_6pt * (1 - icc) / (20 - n_6pt * icc))
    de_e = 1 + (m_e - 1) * icc
    n_eff_e = 20 * m_e / de_e

    print('\n--- D1 · Cỡ mẫu pilot ---')
    print(f'a) Chia theo yêu cầu (mde=5đ): {n_5pt} yêu cầu/nhóm')
    print(f'b) Theo nhân viên (m=75): DE={de_75:.2f}, cần {n_b}/nhóm -> {staff_b} người/nhóm (tổng {staff_b*2} > 40)')
    print(f'c) 20 nhân viên/nhóm: tối đa {max_eff_staff:.0f} hiệu dụng (< {n_5pt}: không đạt 5đ)')
    print(f'd) 6 depot/nhóm: tối đa {max_eff_depot:.0f} hiệu dụng (< {n_5pt}: không đạt)')
    print(f'e) Mức chênh 6đ ({n_6pt}/nhóm), 20 nhân viên/nhóm: m >= {m_e} yc/người (DE={de_e:.2f}, hiệu dụng={n_eff_e:.1f})')

    try:
        from statsmodels.stats.proportion import proportion_effectsize
        from statsmodels.stats.power import NormalIndPower
        es_5pt = proportion_effectsize(p1 + mde, p1)
        pwr_5pt = NormalIndPower().power(effect_size=es_5pt, nobs1=n_6pt, alpha=alpha, ratio=1.0)
        print(f'   Power nếu tác động thật chỉ 5đ với n={n_6pt}: {pwr_5pt:.2f}')
    except ImportError:
        pass

    if reqs is not None:
        reopen_all = (reqs['mo_lai_trong_7_ngay'] == 1).mean()
        scope = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
        reopen_scope = (scope['mo_lai_trong_7_ngay'] == 1).mean()
        print(f'Tỉ lệ mo_lai_trong_7_ngay toàn bộ: {reopen_all:.2%} | trong phạm vi noi_dia+hang_nang: {reopen_scope:.2%}')
