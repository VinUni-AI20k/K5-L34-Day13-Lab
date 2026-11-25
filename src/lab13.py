"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import sys
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
        raise ValueError('p phải nằm trong khoảng (0, 1]')
    if k is not None and k < 1:
        raise ValueError('k phải là số lần chạy dương')
    return 1 / p if k is None else (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if not 0 < p <= 1:
        raise ValueError('p phải nằm trong khoảng (0, 1]')
    if k is not None and k < 1:
        raise ValueError('k phải là số lần chạy dương')
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
    thanh_cong = (reqs['ket_qua'] == 'thanh_cong').sum()
    return dict(
        token=tien_token.sum(),
        tool=tien_tool.sum(),
        chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
        xem_lai=xem_lai,
        lam_lai=lam_lai,
        tong=tong,
        thanh_cong=thanh_cong,
        cps=tong / thanh_cong,
        hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs),
    )


def kich_ban_do_nhay(runs, reqs):
    base = mo_hinh(runs, reqs)
    params = {
        'Giá token gấp đôi': {'gia_vao': 52, 'gia_ra': 260},
        'Giá token giảm một nửa': {'gia_vao': 13, 'gia_ra': 65},
        'Tỉ lệ xem lại gấp đôi': {'he_so_xem_lai': 2},
        'Tỉ lệ xem lại giảm một nửa': {'he_so_xem_lai': .5},
        'Số ca làm lại gấp đôi': {'he_so_lam_lai': 2},
        'Số ca làm lại giảm một nửa': {'he_so_lam_lai': .5},
        'Lương nhân viên tăng 25%': {'luong_phut': 2500},
        'Chỉ cho chạy tối đa 2 lần': {'max_lan_chay': 2},
        'Chỉ cho chạy 1 lần': {'max_lan_chay': 1},
    }
    result = {}
    for name, kw in params.items():
        row = mo_hinh(runs, reqs, **kw)
        result[name] = {**row, 'thay_doi_pct': (row['cps'] / base['cps'] - 1) * 100}
    pair = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)
    result['Giá token gấp đôi và xem lại gấp đôi'] = {
        **pair, 'thay_doi_pct': (pair['cps'] / base['cps'] - 1) * 100}
    return base, result


def chi_phi_ca_he_thong(runs, reqs, k):
    row = mo_hinh(runs, reqs, max_lan_chay=k)
    failed = len(reqs) - row['thanh_cong']
    return {**row, 'khong_thanh_cong': failed,
            'tong_ca_he_thong': row['tong'] + failed * BASELINE}


def kich_ban_xem_lai_100_phan_tram(runs, reqs, phut_lam_lai=9):
    q = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])].copy()
    ids = set(q['request_id'])
    r = runs[runs['request_id'].isin(ids)]
    ok_ids = set(r.loc[r['status'] == 'ok', 'request_id'])
    n_review = len(ok_ids)
    n_rework = int((q['ket_qua'] == 'lam_lai').sum())
    token = (r['tokens_in'] / 1000 * GIA_VAO + r['tokens_out'] / 1000 * GIA_RA).sum()
    tool = (r['tool_calls'] * GIA_TOOL).sum()
    review_cost = n_review * 5 * LUONG_PHUT
    rework_cost = n_rework * phut_lam_lai * LUONG_PHUT
    success = int((q['ket_qua'] == 'thanh_cong').sum())
    total = token + tool + review_cost + rework_cost
    return {'so_yeu_cau': len(q), 'so_yeu_cau_duoc_xem': n_review,
            'so_lam_lai': n_rework, 'thanh_cong': success,
            'token_tool': float(token + tool), 'tong': float(total),
            'cps': float(total / success), 'baseline_ratio': float(total / success / BASELINE)}


def co_mau_hai_ty_le(p1=.70, p2=.75, alpha=.05, power=.80):
    from statistics import NormalDist
    za, zb = NormalDist().inv_cdf(1 - alpha / 2), NormalDist().inv_cdf(power)
    pbar = (p1 + p2) / 2
    numerator = (za * math.sqrt(2 * pbar * (1 - pbar))
                 + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2
    return math.ceil(numerator / (p2 - p1) ** 2)


def bang_co_mau_d1(icc=.02):
    n5, n6 = co_mau_hai_ty_le(.70, .75), co_mau_hai_ty_le(.70, .76)
    de75 = 1 + 74 * icc
    adjusted = math.ceil(n5 * de75)
    per_staff = math.ceil(adjusted / 75)
    m6 = math.ceil(n6 * (1 - icc) / (20 - n6 * icc))
    return {'a_n_moi_nhanh_5_diem': n5, 'b_design_effect_m_75': de75,
            'b_n_dieu_chinh_moi_nhanh': adjusted,
            'b_nhan_vien_moi_nhanh': per_staff, 'b_tong_nhan_vien': per_staff * 2,
            'c_tran_hieu_dung_moi_nhanh_20_nhan_vien': 20 / icc,
            'd_tran_hieu_dung_moi_nhanh_6_depot': 6 / icc,
            'e_n_moi_nhanh_6_diem': n6, 'e_yeu_cau_moi_nhan_vien': m6,
            'e_design_effect': 1 + (m6 - 1) * icc}


def in_bang_do_nhay(runs, reqs):
    base, scenarios = kich_ban_do_nhay(runs, reqs)
    print('\nB1 · CPS simulated; giá token theo bảng giả định')
    print(f'Gốc: {base["cps"]:,.0f} đ')
    for name, row in list(scenarios.items())[:9]:
        print(f'{name}: {row["cps"]:,.0f} đ ({row["thay_doi_pct"]:+.1f}%)')
    pair = scenarios['Giá token gấp đôi và xem lại gấp đôi']
    print(f'B2 · Cặp token ×2 và xem lại ×2: {pair["cps"]:,.0f} đ ({pair["thay_doi_pct"]:+.1f}%). Xếp hạng: làm lại, xem lại, lương.')
    print('\nB3 · Chi phí cả hệ thống')
    for k in (1, 2, 3):
        row = chi_phi_ca_he_thong(runs, reqs, k)
        print(f'{k} lần: agent {row["tong"]:,.0f}; thất bại {row["khong_thanh_cong"]}; hệ thống {row["tong_ca_he_thong"]:,.0f}; CPS {row["cps"]:,.0f}')
    print('\nB4 · Kiểm tra 100%')
    for minutes in (9, 15.3):
        row = kich_ban_xem_lai_100_phan_tram(runs, reqs, minutes)
        print(f'{minutes:g} phút làm lại: {row["cps"]:,.0f} đ ({row["baseline_ratio"]:.2f}× baseline)')
    print('\nD1 · Cỡ mẫu')
    for name, value in bang_co_mau_d1().items():
        print(f'{name}: {value}')
    for name, frame in [('toàn mẫu', reqs), ('nội địa + hàng nặng', reqs[reqs.loai.isin(["noi_dia", "hang_nang"])])]:
        n = frame['mo_lai_trong_7_ngay'].astype(int).sum()
        print(f'Mở lại 7 ngày {name}: {n}/{len(frame)} = {n/len(frame):.2%}')
    review = reqs[reqs['duoc_xem_lai'].astype(int) == 1]
    ignored = review['quyet_dinh_xem_lai'].isin(['sua', 'bo']).sum()
    primary = ((reqs['dong_trong_24h'].astype(int) == 1) & (reqs['mo_lai_trong_7_ngay'].astype(int) == 0)).sum()
    print(f'E1 chính: {primary}/{len(reqs)} = {primary/len(reqs):.2%}')
    print(f'E1 bỏ qua gợi ý: {ignored}/{len(review)} = {ignored/len(review):.2%}')


if __name__ == '__main__':
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    nhan_gia_tri = {
        'xem_lai': 'simulated',
        'lam_lai': 'simulated',
        'tong': 'có phần simulated',
        'cps': 'simulated',
    }
    for ten, gia_tri in ket_qua.items():
        nhan = nhan_gia_tri.get(ten, '')
        print(f'{ten:12s} {gia_tri:>14,.0f} {nhan}')

    # Nhiệm vụ A3 · Tách chi phí theo loại yêu cầu.
    print('\nA3 · Chi phí theo loại yêu cầu')
    for loai in reqs['loai'].unique():
        nhom = reqs[reqs['loai'] == loai]
        kq = mo_hinh(runs, nhom)
        n = len(nhom)
        print(
            f'{loai:12s} yeu_cau={n:4,d}  '
            f'thanh_cong={kq["thanh_cong"] / n:6.1%}  '
            f'lan_chay/yc={nhom["so_lan_chay"].sum() / n:5.2f}  '
            f'cps={kq["cps"]:9,.0f} [simulated]  '
            f'so_baseline={kq["cps"] / BASELINE:5.2f}x [simulated]'
        )

    # Tỉ lệ ok theo lần thử giúp giải thích liệu chạy lại có cải thiện A3 không.
    runs_theo_loai = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    ty_le_ok = runs_theo_loai.assign(ok=runs_theo_loai['status'] == 'ok').pivot_table(
        index='loai', columns='attempt', values='ok', aggfunc='mean'
    )
    print('\nA3 · Tỉ lệ chạy ok theo lần thử')
    print(ty_le_ok.to_string(float_format=lambda x: f'{x:.1%}'))

    # Nhiệm vụ A4 · Chi phí cố định trong phạm vi nội địa + hàng nặng.
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    kq_pham_vi = mo_hinh(runs, pham_vi)
    ty_le_thanh_cong_pham_vi = kq_pham_vi['thanh_cong'] / len(reqs)
    print('\nA4 · Chi phí cố định (noi_dia + hang_nang)')
    for he_so_khoi_luong in (1, 0.5):
        yeu_cau_thang = 45000 * he_so_khoi_luong
        thanh_cong_thang = yeu_cau_thang * ty_le_thanh_cong_pham_vi
        co_dinh_moi_viec = 40_000_000 / thanh_cong_thang
        cps_pham_vi = kq_pham_vi['cps'] + co_dinh_moi_viec
        print(
            f'{yeu_cau_thang:,.0f} yeu_cau/thang  '
            f'thanh_cong={thanh_cong_thang:,.0f}  '
            f'co_dinh/viec={co_dinh_moi_viec:,.0f}  '
            f'cps+co_dinh={cps_pham_vi:,.0f} [simulated]  '
            f'so_baseline={cps_pham_vi / BASELINE:.2f}x [simulated]'
        )

    in_bang_do_nhay(runs, reqs)
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
