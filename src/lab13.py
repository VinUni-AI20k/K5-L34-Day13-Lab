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
                hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs))


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()

    # ---------- A2 ----------
    goc = mo_hinh(runs, reqs)
    print('\n== A2 · Mô hình chi phí (đ) ==')
    nhan = {'token': 'token (đo từ trace)', 'tool': 'tool (đo từ trace)',
            'chay_lai': 'trong đó lần chạy 2,3',
            'xem_lai': 'xem lại [simulated]', 'lam_lai': 'làm lại [simulated]',
            'tong': 'tổng [simulated]', 'thanh_cong': 'việc thành công',
            'cps': 'chi phí/việc TC [simulated]', 'hoa_don_moi_yc': 'hoá đơn token+tool/yêu cầu'}
    for k, ten in nhan.items():
        print(f'{ten:30s} {goc[k]:>14,.1f}')
    print(f"gấp {goc['cps'] / goc['hoa_don_moi_yc']:.1f} lần hoá đơn/yêu cầu")
    for k in ('token', 'tool', 'xem_lai', 'lam_lai'):
        print(f"  {k}: {goc[k] / goc['tong'] * 100:.1f}% tổng chi phí")

    # ---------- A3 ----------
    print('\n== A3 · Theo loại yêu cầu [simulated] ==')
    print(f"{'loai':10s} {'n':>5s} {'ti le TC':>9s} {'lan/yc':>7s} {'cps':>9s} {'/12000':>7s}")
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        r = reqs[reqs['loai'] == loai]
        m = mo_hinh(runs, r)
        print(f"{loai:10s} {len(r):5d} {m['thanh_cong'] / len(r):9.1%} "
              f"{r['so_lan_chay'].mean():7.2f} {m['cps']:9,.0f} {m['cps'] / BASELINE:6.2f}x")
    print('Tỉ lệ ok theo lần thử và loại:')
    tm = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    tm['ok'] = (tm['status'] == 'ok').astype(float)
    print(tm.pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean').round(3))

    # ---------- A4 ----------
    print('\n== A4 · Chi phí cố định 40 triệu/tháng, noi_dia + hang_nang [simulated] ==')
    pv = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    m_pv = mo_hinh(runs, pv)
    ti_le_tc = m_pv['thanh_cong'] / len(reqs)   # trên 1.200 yêu cầu của mẫu
    for ten, khoi_luong in [('45.000 yc/tháng', 45000), ('một nửa', 22500)]:
        viec_tc = khoi_luong * ti_le_tc
        co_dinh = 40_000_000 / viec_tc
        print(f"{ten:16s} việc TC/tháng {viec_tc:9,.0f} · cố định/việc {co_dinh:7,.0f} · "
              f"tổng {m_pv['cps'] + co_dinh:7,.0f} = {(m_pv['cps'] + co_dinh) / BASELINE:.2f}x")

    # ---------- B1 ----------
    print('\n== B1 · Đổi từng yếu tố [simulated] ==')
    kich_ban = {
        'Giá token gấp đôi':      dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa': dict(gia_vao=13, gia_ra=65),
        'Xem lại gấp đôi':        dict(he_so_xem_lai=2),
        'Xem lại giảm một nửa':   dict(he_so_xem_lai=0.5),
        'Làm lại gấp đôi':        dict(he_so_lam_lai=2),
        'Làm lại giảm một nửa':   dict(he_so_lam_lai=0.5),
        'Lương tăng 25%':         dict(luong_phut=2500),
        'Tối đa 2 lần chạy':      dict(max_lan_chay=2),
        'Chỉ 1 lần chạy':         dict(max_lan_chay=1),
    }
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        print(f"{ten:25s} {cps:8,.0f} {(cps / goc['cps'] - 1) * 100:+6.1f}%")

    # ---------- B2 ----------
    print('\n== B2 · Một cặp [simulated] ==')
    cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    print(f"Giá token x2 + xem lại x2: {cap:,.0f} ({(cap / goc['cps'] - 1) * 100:+.1f}%)")

    # ---------- B3 ----------
    print('\n== B3 · Giới hạn chạy lại [simulated] ==')
    print(f"{'gioi han':9s} {'tong tro ly':>12s} {'khong TC':>9s} {'ca he thong':>12s} {'cps':>8s}")
    for k in (1, 2, 3):
        m = mo_hinh(runs, reqs, max_lan_chay=k)
        khong_tc = len(reqs) - m['thanh_cong']
        print(f"{k:9d} {m['tong']:12,.0f} {khong_tc:9d} "
              f"{m['tong'] + BASELINE * khong_tc:12,.0f} {m['cps']:8,.0f}")

    # ---------- B4 ----------
    print('\n== B4 · Xem lại 100% (noi_dia + hang_nang), 5 phút/lần xem [simulated] ==')
    runs_pv = runs[runs['request_id'].isin(pv['request_id'])]
    token_tool = ((runs_pv['tokens_in'] / 1000 * GIA_VAO + runs_pv['tokens_out'] / 1000 * GIA_RA).sum()
                  + (runs_pv['tool_calls'] * GIA_TOOL).sum())
    co_ok = runs_pv[runs_pv['status'] == 'ok']['request_id'].nunique()
    n_lam_lai = int((pv['ket_qua'] == 'lam_lai').sum())
    n_tc = int((pv['ket_qua'] == 'thanh_cong').sum())
    phut_tb = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean()  # toàn bộ ca lam_lai
    for phut in (9, phut_tb):
        tong = token_tool + co_ok * 5 * LUONG_PHUT + n_lam_lai * phut * LUONG_PHUT
        print(f'làm lại {phut:5.1f} phút/ca: tổng {tong:11,.0f} · cps {tong / n_tc:8,.0f} = '
              f'{tong / n_tc / BASELINE:.2f}x ({co_ok} yc được xem, {n_lam_lai} ca làm lại, {n_tc} thành công)')

    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
