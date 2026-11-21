"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd
from statistics import NormalDist

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
        raise ValueError('k phải ít nhất là 1')
    return (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if not 0 <= p <= 1:
        raise ValueError('p phải nằm trong [0, 1]')
    if k is None:
        return 1.0
    if k < 1:
        raise ValueError('k phải ít nhất là 1')
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    success = ti_le_thanh_cong(p, k)
    if success == 0:
        return math.inf
    return so_lan_chay_ky_vong(p, k) / success


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
    request_ids = set(reqs['request_id'])
    runs = runs[runs['request_id'].isin(request_ids)].copy()
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = (runs['tokens_in'] / 1000 * gia_vao
                  + runs['tokens_out'] / 1000 * gia_ra)
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].astype(float).sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].astype(float).sum() * luong_phut * he_so_lam_lai
    tong = float(tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai)
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    cps = tong / thanh_cong if thanh_cong else math.inf
    return {
        'token': float(tien_token.sum()),
        'tool': float(tien_tool.sum()),
        'chay_lai': float((tien_token + tien_tool)[runs['attempt'] > 1].sum()),
        'xem_lai': float(xem_lai),
        'lam_lai': float(lam_lai),
        'tong': tong,
        'thanh_cong': thanh_cong,
        'cps': float(cps),
        'hoa_don_moi_yc': float((tien_token.sum() + tien_tool.sum()) / len(reqs)) if len(reqs) else 0.0,
    }


def co_mau(p1, p2, alpha=0.05, power=0.8):
    """Cỡ mẫu cho mỗi nhóm khi so sánh hai tỷ lệ độc lập (xấp xỉ chuẩn)."""
    za = NormalDist().inv_cdf(1 - alpha / 2)
    zb = NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    return math.ceil((za * math.sqrt(2 * pb * (1 - pb))
                     + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2
                     / (p2 - p1) ** 2)


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:12s} {gia_tri:>14,.0f}')
    print('\nA3 · Theo loại yêu cầu (chi phí simulated)')
    for loai in reqs['loai'].unique():
        subreq = reqs[reqs['loai'] == loai]
        sub = mo_hinh(runs, subreq)
        print(f"{loai:12s} n={len(subreq):4d} success={sub['thanh_cong']:4d} "
              f"rate={sub['thanh_cong']/len(subreq):.1%} "
              f"runs/request={subreq['so_lan_chay'].mean():.2f} cps={sub['cps']:,.0f} "
              f"vs_baseline={sub['cps']/BASELINE:.2f}x")
    print('Tỷ lệ chạy ok theo attempt')
    typed_runs = runs.merge(reqs[['request_id', 'loai']], on='request_id', how='inner')
    for loai, group in typed_runs.groupby('loai'):
        rates = group.assign(ok=group['status'].eq('ok')).groupby('attempt')['ok'].mean()
        print(f"{loai:12s} " + ' '.join(f"a{attempt}={rate:.1%}" for attempt, rate in rates.items()))

    print('\nA4 · Chi phí cố định 40 triệu/tháng (noi_dia + hang_nang; simulated)')
    pilot_req = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    pilot_result = mo_hinh(runs, pilot_req)
    pilot_success = pilot_result['thanh_cong']
    # 45k là toàn bộ yêu cầu/tháng; phạm vi pilot chiếm tỷ lệ success/1,200.
    for label, volume in [('45.000 yêu cầu/tháng', 45000), ('Một nửa khối lượng', 22500)]:
        success_volume = volume * pilot_success / len(reqs)
        fixed_per_success = 40_000_000 / success_volume
        variable_cps = pilot_result['cps']
        print(f"{label}: success={success_volume:,.0f}, fixed={fixed_per_success:,.0f}/việc, "
              f"total={variable_cps+fixed_per_success:,.0f} ({(variable_cps+fixed_per_success)/BASELINE:.2f}x)")

    print('\nB1 · Độ nhạy')
    goc = ket_qua['cps']
    kich_ban = {
        'Giá token gấp đôi': dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa': dict(gia_vao=13, gia_ra=65),
        'Xem lại gấp đôi': dict(he_so_xem_lai=2),
        'Xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
        'Làm lại gấp đôi': dict(he_so_lam_lai=2),
        'Làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
        'Lương tăng 25%': dict(luong_phut=2500),
        'Tối đa 2 lần chạy': dict(max_lan_chay=2),
        'Chỉ 1 lần chạy': dict(max_lan_chay=1),
    }
    for ten, kwargs in kich_ban.items():
        kq = mo_hinh(runs, reqs, **kwargs)
        print(f"{ten:25s} cps={kq['cps']:8,.0f} delta={(kq['cps']/goc-1):+7.1%}")
    ket_hop = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)
    print(f"Token x2 + xem lại x2: {ket_hop['cps']:,.0f} ({ket_hop['cps']/goc-1:+.1%})")

    print('\nB3 · Giới hạn chạy (chi phí toàn hệ thống gồm nhân viên xử lý phần thất bại)')
    for limit in (1, 2, 3):
        kq = mo_hinh(runs, reqs, max_lan_chay=limit)
        failed = len(reqs) - kq['thanh_cong']
        system_cost = kq['tong'] + failed * BASELINE
        print(f"{limit} lần: agent={kq['tong']:,.0f}, failed={failed}, "
              f"system={system_cost:,.0f}, cps={kq['cps']:,.0f}")

    print('\nB4 · Xem lại 100% (noi_dia + hang_nang; simulated)')
    scope = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])].copy()
    scope_runs = runs[runs['request_id'].isin(scope['request_id'])]
    # Mỗi yêu cầu có ít nhất một lần chạy thành công được xem lại 5 phút.
    ok_ids = set(scope_runs.loc[scope_runs['status'] == 'ok', 'request_id'])
    review_minutes = len(ok_ids) * 5
    retry_cases = int((scope['ket_qua'] == 'lam_lai').sum())
    retry_minutes = retry_cases * 9  # giả định B4 trong đề: 9 phút mỗi ca làm lại
    simulated_retry_minutes = retry_cases * 15.3  # độ nhạy theo trung bình toàn bộ ca làm lại
    bill = (scope_runs['tokens_in'].sum()/1000*GIA_VAO
            + scope_runs['tokens_out'].sum()/1000*GIA_RA
            + scope_runs['tool_calls'].sum()*GIA_TOOL)
    success = int((scope['ket_qua'] == 'thanh_cong').sum())
    review100_cps = (bill + review_minutes*LUONG_PHUT + retry_minutes*LUONG_PHUT) / success
    print(f"{len(scope)} yêu cầu, {len(ok_ids)} reviewable, {review_minutes} phút; "
          f"cps={review100_cps:,.0f} ({review100_cps/BASELINE:.2f}x baseline); "
          f"làm lại: {retry_cases} ca × 9 phút; phút simulated hiện có={simulated_retry_minutes:.1f}")
    bill_actual_retry = bill + review_minutes*LUONG_PHUT + simulated_retry_minutes*LUONG_PHUT
    print(f"Độ nhạy theo phút làm lại trong dữ liệu: {bill_actual_retry/success:,.0f} "
          f"({bill_actual_retry/success/BASELINE:.2f}x baseline)")

    print('\nD1 · Cỡ mẫu')
    n5 = co_mau(0.70, 0.75)
    n6 = co_mau(0.70, 0.76)
    de75 = 1 + (75 - 1) * 0.02
    de299 = 1 + (299 - 1) * 0.02
    print(f"a yêu cầu độc lập: {n5:,}/nhóm")
    print(f"b theo staff, m=75: DE={de75:.2f}, n={math.ceil(n5*de75):,}/nhóm "
          f"(~{math.ceil(math.ceil(n5*de75)/75)} staff/nhóm; 84 tổng)")
    print(f"c 20 staff/nhóm: trần hiệu dụng={20/0.02:,.0f} < {n5:,}")
    print(f"d 6 depot/nhóm: trần hiệu dụng={6/0.02:,.0f}")
    print(f"e MDE 6 điểm: {n6:,}/nhóm; m=299, DE={de299:.2f}, "
          f"hiệu dụng={20*299/de299:,.1f}/nhóm")

    print('\nE · Chỉ số hiện tại (simulated)')
    primary = ((reqs['dong_trong_24h'].astype(int) == 1)
               & (reqs['mo_lai_trong_7_ngay'].astype(int) == 0)).mean()
    reviewed = reqs[reqs['duoc_xem_lai'].astype(int) == 1]
    override = reviewed['quyet_dinh_xem_lai'].isin(['sua', 'bo']).mean()
    reopened = reqs['mo_lai_trong_7_ngay'].astype(int).mean()
    print(f"primary={primary:.2%}; override={override:.2%}; reopened={reopened:.2%} "
          f"({int(reqs['mo_lai_trong_7_ngay'].astype(int).sum())}/{len(reqs)})")
