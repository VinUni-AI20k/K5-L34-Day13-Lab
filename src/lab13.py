"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
from statistics import NormalDist
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


# ---------- Nhiệm vụ D1 · Cỡ mẫu ----------
def co_mau(p1, p2, alpha=0.05, power=0.8):
    za = NormalDist().inv_cdf(1 - alpha / 2)
    zb = NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    return math.ceil((za * math.sqrt(2 * pb * (1 - pb))
                      + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2)


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

    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    print('\n=== D1: CỠ MẪU ===')
    n_req = co_mau(0.70, 0.75)
    de_75 = 1 + 74 * 0.02
    n_75 = math.ceil(n_req * de_75)
    print(f"a) Chia theo yêu cầu : {n_req} yêu cầu mỗi nhóm")
    print(f"b) Theo NV (m=75)   : DE = {de_75:.2f} -> {n_75} yêu cầu/nhóm ({n_75/75:.1f} nhân viên/nhóm > 20)")
    print(f"c) 20 NV mỗi nhóm    : Giới hạn c/ICC = {20/0.02:.0f} < {n_req} (không đạt)")
    print(f"d) 6 depot mỗi nhóm  : Giới hạn c/ICC = {6/0.02:.0f} (không đạt)")
    n_6pt = co_mau(0.70, 0.76)
    m_req = (n_6pt * 0.98) / (20 - n_6pt * 0.02)
    print(f"e) MDE 6 điểm (859/nhóm): 20 NV -> m >= {math.ceil(m_req)} yêu cầu/nhân viên (DE = {1 + (math.ceil(m_req)-1)*0.02:.2f})")
