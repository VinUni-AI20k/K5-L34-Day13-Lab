"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas)
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
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:  # dùng cho B1, B3
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0
    # Chia 1.000 trước khi nhân giá token; tính MỌI lần chạy, kể cả lần lỗi
    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai   # simulated
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai   # simulated
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = (reqs['ket_qua'] == 'thanh_cong').sum()
    return dict(token=tien_token.sum(), tool=tien_tool.sum(),
                chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
                xem_lai=xem_lai, lam_lai=lam_lai, tong=tong,
                thanh_cong=thanh_cong, cps=tong / thanh_cong,
                hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs),
                so_yc=len(reqs))


def chi_phi_he_thong(kq):
    """B3: chi phí trợ lý + BASELINE × số yêu cầu không thành công (nhân viên làm thay)."""
    khong_tc = kq['so_yc'] - kq['thanh_cong']
    return kq['tong'] + BASELINE * khong_tc, khong_tc


def in_a(runs, reqs):
    print('\n=== A2 · Mô hình chi phí từ trace (có phần simulated) ===')
    kq = mo_hinh(runs, reqs)
    for ten in ['token', 'tool', 'chay_lai', 'xem_lai', 'lam_lai', 'tong', 'thanh_cong', 'cps', 'hoa_don_moi_yc']:
        print(f'{ten:15s} {kq[ten]:>14,.1f}')
    print(f"cps / hoa_don_moi_yc = {kq['cps'] / kq['hoa_don_moi_yc']:.1f}x")
    for ten in ['xem_lai', 'lam_lai']:
        print(f"ti trong {ten} = {kq[ten] / kq['tong']:.1%} [simulated]")
    print(f"gio nhan vien (xem + lam lai) = {(kq['xem_lai'] + kq['lam_lai']) / kq['tong']:.1%} [simulated]")
    # So với nhân viên tự làm: chi phí cả hệ thống / số yêu cầu
    cht, khong_tc = chi_phi_he_thong(kq)
    print(f"ca he thong/yeu cau = {cht / kq['so_yc']:,.0f} d = {cht / kq['so_yc'] / BASELINE:.2f}x [simulated]")

    print('\n=== A3 · Tách theo loại yêu cầu ===')
    lan = runs.groupby('request_id').size()
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        r = reqs[reqs.loai == loai]
        k = mo_hinh(runs, r)
        print(f"{loai:10s} n={len(r):4d} tc={k['thanh_cong'] / len(r):6.1%} "
              f"lan/yc={lan.reindex(r['request_id']).mean():.2f} "
              f"cps={k['cps']:8,.0f} d = {k['cps'] / BASELINE:.2f}x [simulated]")
    m = runs.merge(reqs[['request_id', 'loai']])
    m['ok'] = (m['status'] == 'ok').astype(float)
    print('Ti le ok theo lan thu:')
    print(m.pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean').round(3))

    print('\n=== A4 · Chi phí cố định 40 triệu đ/tháng (noi_dia + hang_nang) ===')
    pv = reqs[reqs.loai.isin(['noi_dia', 'hang_nang'])]
    k = mo_hinh(runs, pv)
    tc_ti_le = k['thanh_cong'] / len(reqs)  # phần 900/1.200 của MẪU 1.200 yêu cầu
    for ten, yc in [('45.000 yc/thang', 45000), ('mot nua', 22500)]:
        viec = yc * tc_ti_le
        cd = 40_000_000 / viec
        print(f"{ten:16s} viec_tc/thang={viec:8,.0f} co_dinh/viec={cd:6,.0f} "
              f"cps+cd={k['cps'] + cd:7,.0f} d = {(k['cps'] + cd) / BASELINE:.2f}x [simulated]")
    print(f"(chua cong co dinh: cps pham vi = {k['cps']:,.0f} d)")


def in_b(runs, reqs):
    print('\n=== B1 · Đổi từng yếu tố ===')
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
    goc = mo_hinh(runs, reqs)['cps']
    print(f'{"Gốc":26s} {goc:8,.0f}')
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        print(f'{ten:26s} {cps:8,.0f} {(cps / goc - 1) * 100:+6.1f}%')

    print('\n=== B2 · Một cặp ===')
    cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    print(f'Token x2 + xem lại x2: {cap:,.0f} ({(cap / goc - 1) * 100:+.1f}%)')

    print('\n=== B3 · Giới hạn chạy lại ===')
    for k in [1, 2, 3]:
        kq = mo_hinh(runs, reqs, max_lan_chay=k)
        cht, khong_tc = chi_phi_he_thong(kq)
        print(f"{k} lan: tong_tro_ly={kq['tong']:12,.0f} khong_tc={khong_tc:4d} "
              f"ca_he_thong={cht:12,.0f} cps={kq['cps']:7,.0f} [simulated]")

    print('\n=== B4 · Xem lại 100% (noi_dia + hang_nang) ===')
    pv = reqs[reqs.loai.isin(['noi_dia', 'hang_nang'])]
    rp = runs[runs['request_id'].isin(pv['request_id'])]
    ok_any = rp[rp['status'] == 'ok']['request_id'].nunique()
    n_lam_lai = (pv['ket_qua'] == 'lam_lai').sum()
    tien_tt = (rp['tokens_in'] / 1000 * GIA_VAO + rp['tokens_out'] / 1000 * GIA_RA + rp['tool_calls'] * GIA_TOOL).sum()
    tc = (pv['ket_qua'] == 'thanh_cong').sum()
    for phut_ll, nhan in [(9, 'đề cho 9 phút/ca'),
                          # trung bình phút làm lại trên TOÀN BỘ ca lam_lai của mẫu (simulated)
                          (reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean(), 'dữ liệu')]:
        xem = ok_any * 5 * LUONG_PHUT
        lam = n_lam_lai * phut_ll * LUONG_PHUT
        tong = tien_tt + xem + lam
        print(f'{nhan:18s} phut_lam_lai={phut_ll:5.1f} yc_ok={ok_any} ca_lam_lai={n_lam_lai} '
              f'tong={tong:12,.0f} cps={tong / tc:7,.0f} = {tong / tc / BASELINE:.2f}x [simulated]')
        # hoà vốn: số phút xem lại để cps = BASELINE
        hv = (BASELINE * tc - tien_tt - lam) / (ok_any * LUONG_PHUT)
        print(f'   hoa von: moi lan xem lai <= {hv:.2f} phut')


def co_mau_hai_ti_le(p1, p2, alpha, power):
    """Cỡ mẫu mỗi nhóm khi so hai tỉ lệ với kiểm định hai phía và chia 1:1."""
    chuan = NormalDist()
    z_alpha = chuan.inv_cdf(1 - alpha / 2)
    z_power = chuan.inv_cdf(power)
    p_tb = (p1 + p2) / 2
    sai_so_gop = math.sqrt(2 * p_tb * (1 - p_tb))
    sai_so_rieng = math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))
    return math.ceil(((z_alpha * sai_so_gop + z_power * sai_so_rieng) / (p2 - p1)) ** 2)


def in_d1():
    """So sánh cỡ mẫu theo yêu cầu, theo nhân viên và theo depot."""
    print('\n=== D1 · Cỡ mẫu pilot ===')
    p_goc, alpha, power, icc = 0.70, 0.05, 0.80, 0.02
    p_5_diem, p_6_diem = 0.75, 0.76
    n_5_diem = co_mau_hai_ti_le(p_goc, p_5_diem, alpha, power)
    print(f'a) Theo yêu cầu: {n_5_diem:,} yêu cầu/nhóm')

    m = 75
    de = 1 + (m - 1) * icc
    n_theo_nhan_vien = math.ceil(n_5_diem * de)
    so_nhan_vien = math.ceil(n_theo_nhan_vien / m)
    print(f'b) Theo nhân viên (m={m}): DE={de:.2f}, {n_theo_nhan_vien:,} yêu cầu/nhóm, '
          f'{so_nhan_vien} nhân viên/nhóm ({2 * so_nhan_vien} tổng cộng, hiện có 40)')

    nhan_vien_moi_nhom, depot_moi_nhom = 20, 6
    # Khi m tăng vô hạn, cỡ mẫu hiệu dụng tiến tới số cụm / ICC.
    print(f'c) {nhan_vien_moi_nhom} nhân viên/nhóm: giới hạn cỡ mẫu hiệu dụng '
          f'< {nhan_vien_moi_nhom / icc:,.0f}')
    print(f'd) {depot_moi_nhom} depot/nhóm: giới hạn cỡ mẫu hiệu dụng < {depot_moi_nhom / icc:,.0f}')

    n_6_diem = co_mau_hai_ti_le(p_goc, p_6_diem, alpha, power)
    # Giải c*m / (1 + (m - 1)*ICC) >= n khi n thấp hơn giới hạn c/ICC.
    m_toi_thieu = math.ceil(n_6_diem * (1 - icc) / (nhan_vien_moi_nhom - n_6_diem * icc))
    de_6_diem = 1 + (m_toi_thieu - 1) * icc
    n_thuc_te = nhan_vien_moi_nhom * m_toi_thieu
    print(f'e) Chênh 6 điểm: {n_6_diem:,} yêu cầu hiệu dụng/nhóm, '
          f'm tối thiểu {m_toi_thieu} yêu cầu/nhân viên, DE={de_6_diem:.2f}')
    print(f'   {n_thuc_te:,} yêu cầu thực tế/nhóm, {n_thuc_te / de_6_diem:,.2f} yêu cầu hiệu dụng/nhóm')

    # Power xấp xỉ hai phía với Cohen h, ở cỡ mẫu hiệu dụng đã chọn cho mức 6 điểm.
    h = 2 * (math.asin(math.sqrt(p_5_diem)) - math.asin(math.sqrt(p_goc)))
    chuan = NormalDist()
    z_alpha = chuan.inv_cdf(1 - alpha / 2)
    dich_chuyen = h * math.sqrt(n_6_diem / 2)
    power_5_diem = chuan.cdf(dich_chuyen - z_alpha) + chuan.cdf(-dich_chuyen - z_alpha)
    print(f'   Power nếu tác động thực là 5 điểm: {power_5_diem:.2f}')


def in_e(runs, reqs):
    print('\n=== E1 · Chỉ số tính thử trên 1.200 yêu cầu ===')
    chinh = ((reqs.dong_trong_24h == 1) & (reqs.mo_lai_trong_7_ngay == 0))
    xem = reqs[reqs.duoc_xem_lai == 1]
    bo_qua = xem.quyet_dinh_xem_lai.isin(['sua', 'bo'])
    an_toan = reqs.mo_lai_trong_7_ngay == 1
    print(f'Chinh   {chinh.mean():.2%} ({chinh.sum()}/{len(reqs)})')
    print(f'Dung    {bo_qua.mean():.2%} ({bo_qua.sum()}/{len(xem)})')
    print(f'An toan {an_toan.mean():.2%} ({an_toan.sum()}/{len(reqs)})')
    pham_vi = reqs.loai.isin(['noi_dia', 'hang_nang'])
    pv = reqs[pham_vi]
    an_toan_pv = an_toan[pham_vi]
    print(f'An toan trong pham vi noi_dia + hang_nang: {an_toan_pv.mean():.2%} '
          f'({an_toan_pv.sum()}/{len(pv)})')
    print(f"Ti le lam_lai trong pham vi: {(pv.ket_qua == 'lam_lai').mean():.2%} "
          f"({(pv.ket_qua == 'lam_lai').sum()}/{len(pv)})")
    print(f"Ti le duoc xem lai trong pham vi: {pv.duoc_xem_lai.mean():.2%}")


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    in_a(runs, reqs)
    in_b(runs, reqs)
    in_d1()
    in_e(runs, reqs)
