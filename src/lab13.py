"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Dữ liệu trong hai file CSV là giả lập.
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
CO_DINH_THANG = 40_000_000   # chi phí cố định của trợ lý mỗi tháng
YEU_CAU_THANG = 45_000       # số yêu cầu hoàn phí mỗi tháng ở quy mô đầy đủ


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
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
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × luong_phut. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
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
    return dict(token=tien_token.sum(), tool=tien_tool.sum(),
                chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
                xem_lai=xem_lai, lam_lai=lam_lai, tong=tong,
                thanh_cong=thanh_cong, cps=tong / thanh_cong,
                hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs),
                so_yeu_cau=len(reqs))


# ---------- Nhiệm vụ D1 · Cỡ mẫu ----------
def co_mau(p1, p2, alpha=0.05, power=0.8):
    """Cỡ mẫu mỗi nhóm khi so hai tỉ lệ (z chính xác)."""
    za, zb = NormalDist().inv_cdf(1 - alpha / 2), NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    return math.ceil((za * math.sqrt(2 * pb * (1 - pb))
                      + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2)


def he_so_thiet_ke(m, icc=0.02):
    return 1 + (m - 1) * icc


def m_toi_thieu(n_can, c, icc=0.02):
    """m nhỏ nhất sao cho c*m / (1 + (m-1)*icc) >= n_can."""
    # c*m >= n_can*(1-icc) + n_can*icc*m  →  m >= n_can*(1-icc) / (c - n_can*icc)
    return math.ceil(n_can * (1 - icc) / (c - n_can * icc))


def in_bang(tieu_de, rows):
    print(f'\n== {tieu_de} ==')
    for r in rows:
        print(r)


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()

    # ---- A2 ----
    goc = mo_hinh(runs, reqs)
    print('\n== A2 · Mô hình chi phí (xem_lai, lam_lai, tong, cps là simulated) ==')
    for ten, gia_tri in goc.items():
        print(f'{ten:15s} {gia_tri:>14,.1f}')
    print(f"cps / hoá đơn mỗi yêu cầu = {goc['cps'] / goc['hoa_don_moi_yc']:.1f}x")
    for k in ('lam_lai', 'xem_lai'):
        print(f"tỉ trọng {k}: {goc[k] / goc['tong'] * 100:.1f}%")
    gio_nv = (goc['xem_lai'] + goc['lam_lai']) / goc['tong'] * 100
    print(f'giờ nhân viên chiếm {gio_nv:.1f}% tổng chi phí')
    khong_tc = (reqs['ket_qua'] != 'thanh_cong').sum()
    he_thong = (goc['tong'] + khong_tc * BASELINE) / len(reqs)
    print(f'Chi phí cả hệ thống / yêu cầu = {he_thong:,.0f} đ = {he_thong / BASELINE:.2f}x của 12.000 đ '
          f'({khong_tc} yêu cầu không thành công, simulated)')

    # ---- A3 ----
    print('\n== A3 · Theo loại yêu cầu (simulated) ==')
    print(f"{'loai':10s}{'n':>6s}{'tc%':>8s}{'lan/yc':>8s}{'cps':>10s}{'x12000':>8s}")
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        rq = reqs[reqs['loai'] == loai]
        m = mo_hinh(runs, rq)
        lan = rq['so_lan_chay'].mean()
        print(f"{loai:10s}{len(rq):6d}{m['thanh_cong'] / len(rq) * 100:8.1f}{lan:8.2f}"
              f"{m['cps']:10,.0f}{m['cps'] / BASELINE:8.2f}")
    r = runs.merge(reqs[['request_id', 'loai']])
    r['ok'] = (r['status'] == 'ok').astype(float)
    print('\nTỉ lệ ok theo lần thử:')
    print(r.pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean').round(3))

    # ---- A4 ----
    pv = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    mp = mo_hinh(runs, pv)
    print('\n== A4 · Chi phí cố định (phạm vi noi_dia + hang_nang, simulated) ==')
    for ten, khoi_luong in [('45.000 yêu cầu/tháng', YEU_CAU_THANG), ('một nửa khối lượng', YEU_CAU_THANG / 2)]:
        tc_thang = khoi_luong * mp['thanh_cong'] / len(reqs)
        cd = CO_DINH_THANG / tc_thang
        tot = mp['cps'] + cd
        print(f'{ten:22s} việc thành công/tháng={tc_thang:9,.0f} cố định/việc={cd:7,.0f} '
              f"cps phạm vi={mp['cps']:6,.0f} cps+cố định={tot:7,.0f} = {tot / BASELINE:.2f}x")

    # ---- B1 ----
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
    print('\n== B1 · Độ nhạy (simulated) ==')
    print(f"{'Gốc':26s} {goc['cps']:8,.0f}")
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        print(f'{ten:26s} {cps:8,.0f} {(cps / goc["cps"] - 1) * 100:+6.1f}%')

    # ---- B2 ----
    cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    print(f'\n== B2 · Giá token x2 + xem lại x2: {cap:,.0f} ({(cap / goc["cps"] - 1) * 100:+.1f}%)')

    # ---- B3 ----
    print('\n== B3 · Giới hạn chạy lại (simulated) ==')
    print(f"{'gioi han':>8s}{'tong tro ly':>14s}{'khong TC':>10s}{'ca he thong':>14s}{'cps':>9s}")
    for k in (1, 2, 3):
        m = mo_hinh(runs, reqs, max_lan_chay=k)
        khong = len(reqs) - m['thanh_cong']
        print(f"{k:8d}{m['tong']:14,.0f}{khong:10d}{m['tong'] + khong * BASELINE:14,.0f}{m['cps']:9,.0f}")

    # ---- B4 ----
    print('\n== B4 · Xem lại 100% (noi_dia + hang_nang, simulated) ==')
    ok_ids = set(runs.loc[runs['status'] == 'ok', 'request_id'])
    n_xem = pv['request_id'].isin(ok_ids).sum()
    n_lam = (pv['ket_qua'] == 'lam_lai').sum()
    tt = mp['token'] + mp['tool']
    tc = mp['thanh_cong']
    phut_thuc = pv.loc[pv['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean()
    for phut_lam in (9, phut_thuc):
        tong = n_xem * 5 * LUONG_PHUT + n_lam * phut_lam * LUONG_PHUT + tt
        cps = tong / tc
        hoa_von = (tc * BASELINE - n_lam * phut_lam * LUONG_PHUT - tt) / (n_xem * LUONG_PHUT)
        print(f'làm lại {phut_lam:5.1f} phút/ca: {n_xem} yc xem lại, {n_lam} ca làm lại, tổng {tong:,.0f}, '
              f'cps {cps:,.0f} = {cps / BASELINE:.2f}x; hoà vốn xem lại ≤ {hoa_von:.1f} phút')

    # ---- D1 ----
    print('\n== D1 · Cỡ mẫu (baseline 0,70; alpha 0,05; power 0,8; ICC 0,02) ==')
    n5 = co_mau(0.70, 0.75)
    de75 = he_so_thiet_ke(75)
    n_cum = math.ceil(n5 * de75)
    print(f'a) theo yêu cầu: {n5} mỗi nhóm')
    print(f'b) theo nhân viên m=75: DE={de75:.2f}, n={n_cum} mỗi nhóm → {math.ceil(n_cum / 75)} người mỗi nhóm, '
          f'tổng {2 * math.ceil(n_cum / 75)} > 40 → không đủ người')
    print(f'c) 20 nhân viên mỗi nhóm: tối đa {20 / 0.02:.0f} < {n5} → không đạt')
    print(f'd) 6 depot mỗi nhóm: tối đa {6 / 0.02:.0f} < {n5} → không đạt')
    n6 = co_mau(0.70, 0.76)
    m6 = m_toi_thieu(n6, 20)
    print(f'e) mức chênh 6 điểm: {n6} mỗi nhóm; 20 người mỗi nhóm cần m ≥ {m6} yêu cầu/người '
          f'(DE {he_so_thiet_ke(m6):.2f})')
    try:
        from statsmodels.stats.power import NormalIndPower
        from statsmodels.stats.proportion import proportion_effectsize
        es = proportion_effectsize(0.75, 0.70)
        pw = NormalIndPower().power(effect_size=es, nobs1=n6, alpha=0.05, ratio=1)
        print(f'power nếu tác động thật chỉ 5 điểm với n={n6}: {pw:.2f} (statsmodels, tính trên cỡ mẫu chưa nhân DE)')
        print(f'kiểm: statsmodels solve_power 0,70 vs 0,75 = '
              f'{NormalIndPower().solve_power(effect_size=es, alpha=0.05, power=0.8, ratio=1):.0f}')
    except ImportError:
        print('(chưa cài statsmodels nên bỏ qua kiểm chéo power)')
    print(f"\nTỉ lệ mo_lai_trong_7_ngay: toàn mẫu {reqs['mo_lai_trong_7_ngay'].astype(int).mean() * 100:.2f}%, "
          f"noi_dia+hang_nang {pv['mo_lai_trong_7_ngay'].astype(int).mean() * 100:.2f}%")
