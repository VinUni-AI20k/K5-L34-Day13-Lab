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
    if not 0 < p <= 1:
        raise ValueError('p phải nằm trong (0, 1]')
    if k is None:
        return 1 / p
    if k < 1:
        raise ValueError('k phải >= 1')
    return (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if not 0 < p <= 1:
        raise ValueError('p phải nằm trong (0, 1]')
    if k is None:
        return 1.0
    if k < 1:
        raise ValueError('k phải >= 1')
    return 1 - (1 - p) ** k


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
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'].astype(int) > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].astype(float).sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].astype(float).sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    if thanh_cong == 0:
        cps = float('inf')
    else:
        cps = tong / thanh_cong
    mask_retry = runs['attempt'] > 1
    return dict(token=tien_token.sum(), tool=tien_tool.sum(),
                chay_lai=(tien_token + tien_tool)[mask_retry].sum(),
                xem_lai=xem_lai, lam_lai=lam_lai, tong=tong,
                thanh_cong=thanh_cong, cps=cps,
                hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs))


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:12s} {gia_tri:>14,.0f}')
    print('\nA3 · Chi phí theo loại (đ; phần phút nhân viên simulated)')
    for loai in reqs['loai'].unique():
        r = reqs[reqs['loai'] == loai]
        out = mo_hinh(runs, r)
        print(f'{loai:12s} n={len(r):4d} success={out["thanh_cong"]/len(r):.1%} '
              f'runs/request={r.so_lan_chay.sum()/len(r):.2f} '
              f'cps={out["cps"]:,.0f} ({out["cps"]/BASELINE:.2f}x baseline)')

    print('\nA4 · Chi phí cố định, phạm vi noi_dia + hang_nang')
    scope = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    scope_out = mo_hinh(runs, scope)
    # 45.000 là tổng khối lượng mọi loại; phạm vi chỉ chiếm 982/1.200 nên chia cho len(reqs)
    full_month_success = 45000 * scope_out['thanh_cong'] / len(reqs)
    fixed_per_success = 40_000_000 / full_month_success
    variable_cps = scope_out['tong'] / scope_out['thanh_cong']
    print(f'45,000 requests/month: success={full_month_success:,.0f}, fixed={fixed_per_success:,.0f}, '
          f'all-in={variable_cps+fixed_per_success:,.0f} ({(variable_cps+fixed_per_success)/BASELINE:.2f}x)')
    print(f'Half volume: fixed={fixed_per_success*2:,.0f}, all-in={variable_cps+fixed_per_success*2:,.0f} '
          f'({(variable_cps+fixed_per_success*2)/BASELINE:.2f}x)')

    print('\nB1 · Độ nhạy (chi phí mỗi việc thành công; phút simulated)')
    scenarios = {
        'Gốc': {}, 'Giá token gấp đôi': {'gia_vao': 52, 'gia_ra': 260},
        'Giá token giảm một nửa': {'gia_vao': 13, 'gia_ra': 65},
        'Xem lại gấp đôi': {'he_so_xem_lai': 2}, 'Xem lại giảm một nửa': {'he_so_xem_lai': .5},
        'Làm lại gấp đôi': {'he_so_lam_lai': 2}, 'Làm lại giảm một nửa': {'he_so_lam_lai': .5},
        'Lương tăng 25%': {'luong_phut': 2500}, 'Tối đa 2 lần chạy': {'max_lan_chay': 2},
        'Chỉ 1 lần chạy': {'max_lan_chay': 1}}
    baseline = ket_qua['cps']
    for name, kwargs in scenarios.items():
        val = mo_hinh(runs, reqs, **kwargs)['cps']
        print(f'{name:27s} {val:9,.0f} {((val/baseline)-1)*100:+6.1f}%')
    pair = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)
    print(f'B2 · Token gấp đôi + xem lại gấp đôi: {pair["cps"]:,.0f} ({(pair["cps"]/baseline-1)*100:+.1f}%)')

    print('\nB3 · Chi phí hệ thống theo giới hạn chạy (phút simulated)')
    for k in (1, 2, 3):
        out = mo_hinh(runs, reqs, max_lan_chay=k)
        failed = len(reqs) - out['thanh_cong']
        print(f'{k} lần: trợ lý={out["tong"]:,.0f}, fail={failed}, '
              f'hệ thống={out["tong"]+failed*BASELINE:,.0f}, cps={out["cps"]:,.0f}')

    print('\nB4 · Xem lại 100% (noi_dia + hang_nang; chi phí phút simulated)')
    b4 = mo_hinh(runs, scope, he_so_xem_lai=0, he_so_lam_lai=0)
    successful_with_run = scope['request_id'].isin(runs.loc[runs.status == 'ok', 'request_id']).sum()
    review_100 = successful_with_run * 5 * LUONG_PHUT
    rework_9 = int((scope['ket_qua'] == 'lam_lai').sum()) * 9 * LUONG_PHUT
    total_100 = b4['token'] + b4['tool'] + review_100 + rework_9
    print(f'{total_100/scope_out["thanh_cong"]:,.0f} đ = '
          f'{total_100/scope_out["thanh_cong"]/BASELINE:.2f}x baseline (using 9 min/rework case)')

    from math import ceil
    from statistics import NormalDist
    def co_mau(p1, p2, alpha=.05, power=.8):
        za, zb = NormalDist().inv_cdf(1-alpha/2), NormalDist().inv_cdf(power)
        pb = (p1+p2)/2
        return ceil((za*math.sqrt(2*pb*(1-pb)) + zb*math.sqrt(p1*(1-p1)+p2*(1-p2)))**2/(p2-p1)**2)
    n5, n6 = co_mau(.70, .75), co_mau(.70, .76)
    design_effect = 1 + (75-1)*.02
    print('\nD1 · Cỡ mẫu')
    print(f'a) 5 điểm: {n5:,}/arm; b) staff m=75: {ceil(n5*design_effect):,}/arm, '
          f'{ceil(n5*design_effect/75)} staff/arm')
    print(f'c) 20 staff/arm upper bound: {int(20/.02):,}; d) 6 depot/arm upper bound: {int(6/.02):,}')
    print(f'e) 6 điểm: {n6:,}/arm; m >= {ceil(n6*.98/(20-n6*.02))} requests/staff, '
          f'DE={1+(ceil(n6*.98/(20-n6*.02))-1)*.02:.2f}')
