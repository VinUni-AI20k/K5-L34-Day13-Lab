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
    - xem_lai, lam_lai: số phút (cột *_simulated) × luong_phut. Đây là số GIẢ LẬP (simulated).
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
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
    """Cỡ mẫu mỗi nhóm khi so hai tỉ lệ."""
    za, zb = NormalDist().inv_cdf(1 - alpha / 2), NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    return math.ceil((za * math.sqrt(2 * pb * (1 - pb))
                      + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2)


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    PHAM_VI = ['noi_dia', 'hang_nang']
    rp = reqs[reqs.loai.isin(PHAM_VI)]
    mp = mo_hinh(runs, rp)

    print('\n=== A2 · mô hình chi phí (xem_lai, lam_lai, tong, cps: simulated) ===')
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:14s} {gia_tri:>14,.1f}')
    print(f"cps / hóa đơn token+tool mỗi yêu cầu = {ket_qua['cps'] / ket_qua['hoa_don_moi_yc']:.1f} lần")
    for k in ('token', 'tool', 'xem_lai', 'lam_lai'):
        print(f"tỉ trọng {k:8s} {ket_qua[k] / ket_qua['tong'] * 100:5.1f}%")
    print(f"giờ nhân viên (simulated) {(ket_qua['xem_lai'] + ket_qua['lam_lai']) / ket_qua['tong'] * 100:.1f}% tổng")
    print('phút xem lại', reqs.phut_xem_lai_simulated.sum(), '| phút làm lại', reqs.phut_lam_lai_simulated.sum(),
          '| lần gọi tool', runs.tool_calls.sum())
    he_thong = (ket_qua['tong'] + (len(reqs) - ket_qua['thanh_cong']) * BASELINE) / len(reqs)
    print(f"chi phí cả hệ thống / yêu cầu (cộng việc nhân viên làm thay) = {he_thong:,.0f} đ = {he_thong / BASELINE:.2f}x 12.000 [simulated]")

    print('\n=== A3 · theo loại [simulated] ===')
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        r = reqs[reqs.loai == loai]
        m = mo_hinh(runs, r)
        n_run = runs[runs.request_id.isin(r.request_id)].shape[0]
        print(f"{loai:10s} n={len(r):4d} tl_tc={m['thanh_cong'] / len(r) * 100:5.1f}% run/yc={n_run / len(r):.2f} "
              f"cps={m['cps']:8,.0f} x12k={m['cps'] / BASELINE:.2f}")
    ok = runs.merge(reqs[['request_id', 'loai']]).assign(ok=lambda d: (d.status == 'ok') * 1.0)
    print('tỉ lệ ok theo lần thử (đo từ trace):')
    print(ok.pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean').round(3))

    print('\n=== A4 · chi phí cố định, phạm vi noi_dia + hang_nang [simulated] ===')
    ty_le = mp['thanh_cong'] / len(reqs)
    for ten, kl in (('45.000 yc/tháng', 45000), ('một nửa khối lượng', 22500)):
        tc = kl * ty_le
        cd = 40_000_000 / tc
        print(f"{ten}: việc thành công/tháng={tc:,.0f} cố định/việc={cd:,.0f} cps+cố định={mp['cps'] + cd:,.0f} "
              f"x12k={(mp['cps'] + cd) / BASELINE:.2f}  (cps phạm vi={mp['cps']:,.0f}, thành công={mp['thanh_cong']}, n={len(rp)})")

    print('\n=== B1 · độ nhạy [simulated] ===')
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
    print(f'{"Gốc":28s} {goc:8,.0f}')
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        print(f'{ten:28s} {cps:8,.0f} {(cps / goc - 1) * 100:+6.1f}%')
    cps = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    print(f'B2 cặp (token x2 + xem lại x2): {cps:8,.0f} {(cps / goc - 1) * 100:+6.1f}%')

    print('\n=== B3 · giới hạn chạy lại [simulated] ===')
    for k in (1, 2, 3):
        m = mo_hinh(runs, reqs, max_lan_chay=k)
        kt = len(reqs) - m['thanh_cong']
        print(f"{k} lần: tổng trợ lý={m['tong']:,.0f} không thành công={kt} "
              f"cả hệ thống={m['tong'] + kt * BASELINE:,.0f} cps={m['cps']:,.0f}")

    print('\n=== B4 · xem lại 100% (noi_dia + hang_nang) [simulated] ===')
    rid = set(rp.request_id)
    n_xem = runs[(runs.status == 'ok') & runs.request_id.isin(rid)].request_id.nunique()
    lam_lai_ca = rp[rp.ket_qua == 'lam_lai']
    ca_ll = len(lam_lai_ca)
    rr = runs[runs.request_id.isin(rid)]
    tt = (rr.tokens_in / 1000 * GIA_VAO + rr.tokens_out / 1000 * GIA_RA).sum() + (rr.tool_calls * GIA_TOOL).sum()
    for ten, ph in (('9 phút/ca (đề bài)', 9), ('phút thực tế trong dữ liệu', lam_lai_ca.phut_lam_lai_simulated.mean())):
        tong = n_xem * 5 * LUONG_PHUT + ca_ll * ph * LUONG_PHUT + tt
        print(f"{ten}: yc xem lại={n_xem} ca làm lại={ca_ll} ({ph:.1f} phút) token+tool={tt:,.0f} tong={tong:,.0f} "
              f"cps={tong / mp['thanh_cong']:,.0f} x12k={tong / mp['thanh_cong'] / BASELINE:.2f}")
        print(f"   hòa vốn: mỗi lần xem lại <= "
              f"{(BASELINE * mp['thanh_cong'] - ca_ll * ph * LUONG_PHUT - tt) / (n_xem * LUONG_PHUT):.1f} phút")

    print('\n=== D1 · cỡ mẫu (baseline 0,70; alpha 0,05; power 0,8; ICC 0,02) ===')
    ICC = 0.02
    n_a = co_mau(0.70, 0.75)
    de_b = 1 + (75 - 1) * ICC
    ng = math.ceil(n_a * de_b / 75)
    print(f'a) theo yêu cầu: {n_a}')
    print(f'b) m=75: DE={de_b:.2f} n={n_a * de_b:,.0f} -> {ng} người/nhóm, tổng {2 * ng} (LogiX-VN có 40)')
    print(f'c) 20 nv/nhóm: tối đa {20 / ICC:,.0f} vs {n_a} -> {"đạt" if 20 / ICC >= n_a else "không đạt"}')
    print(f'd) 6 depot/nhóm: tối đa {6 / ICC:,.0f}')
    n6 = co_mau(0.70, 0.76)
    m_e = math.ceil(n6 * (1 - ICC) / (20 - n6 * ICC))
    print(f'e) mức chênh 6 điểm: n={n6}  m>={m_e}  DE={1 + (m_e - 1) * ICC:.2f}')
    from statsmodels.stats.power import NormalIndPower
    from statsmodels.stats.proportion import proportion_effectsize
    pw = NormalIndPower().power(proportion_effectsize(0.75, 0.70), nobs1=n6, alpha=0.05, ratio=1)
    print(f'power nếu tác động thật chỉ 5 điểm, n={n6}/nhóm: {pw:.2f}')

    print('\n=== D3 / E1 · chỉ số (trong đợt chạy thử, không có đối chứng) ===')
    print('mở lại 7 ngày toàn mẫu', f'{reqs.mo_lai_trong_7_ngay.mean() * 100:.2f}% ({reqs.mo_lai_trong_7_ngay.sum()}/{len(reqs)})')
    print('mở lại 7 ngày trong phạm vi', f'{rp.mo_lai_trong_7_ngay.mean() * 100:.2f}%')
    chinh = (reqs.dong_trong_24h == 1) & (reqs.mo_lai_trong_7_ngay == 0)
    xem = reqs[reqs.duoc_xem_lai == 1]
    bo_qua = xem.quyet_dinh_xem_lai.isin(['sua', 'bo'])
    print(f'chính {chinh.mean() * 100:.2f}% ({chinh.sum()}/{len(reqs)})  bỏ qua gợi ý {bo_qua.mean() * 100:.2f}% ({bo_qua.sum()}/{len(xem)})')
    print('tỉ lệ làm lại trong phạm vi', f'{(rp.ket_qua == "lam_lai").mean() * 100:.1f}%',
          '| tỉ lệ được xem lại toàn mẫu', f'{reqs.duoc_xem_lai.mean() * 100:.1f}%',
          '| trong phạm vi', f'{rp.duoc_xem_lai.mean() * 100:.1f}%')
    print('số nhân viên', reqs.staff_id.nunique(), '| depot', reqs.depot.nunique(),
          '| yc/nv', round(len(reqs) / reqs.staff_id.nunique(), 1))
    print(reqs.ket_qua.value_counts().to_dict())
