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
    if max_lan_chay is not None:
        # Bỏ các lần chạy vượt giới hạn; yêu cầu cần nhiều lần hơn coi như chuyển nhân viên, 0 phút xem lại/làm lại
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
    import sys
    sys.stdout.reconfigure(encoding='utf-8')  # console Windows (cp1252) không in được tiếng Việt
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:12s} {gia_tri:>14,.0f}')
    goc = ket_qua['cps']
    print(f"Chi phí mỗi việc thành công gấp {goc / ket_qua['hoa_don_moi_yc']:.1f} lần hoá đơn/yêu cầu [simulated]")
    for k in ('xem_lai', 'lam_lai'):
        print(f"  tỉ trọng {k}: {ket_qua[k] / ket_qua['tong']:.1%} [simulated]")
    he_thong = (ket_qua['tong'] + (len(reqs) - ket_qua['thanh_cong']) * BASELINE) / len(reqs)
    print(f'Chi phí cả hệ thống / yêu cầu (gồm ca nhân viên làm thay): {he_thong:,.0f} đ = {he_thong / BASELINE:.2f}× [simulated]')

    # ---------- A3 · Theo từng loại yêu cầu ----------
    print('\nA3 · loai | n | tỉ lệ thành công | lần chạy/yc | cps [sim] | so với 12.000')
    for loai, nhom in reqs.groupby('loai'):
        m = mo_hinh(runs, nhom)
        so_run = runs['request_id'].isin(nhom['request_id']).sum()
        print(f"{loai:10s} {len(nhom):5d} {m['thanh_cong'] / len(nhom):7.1%} {so_run / len(nhom):6.2f}"
              f" {m['cps']:10,.0f} {m['cps'] / BASELINE:6.2f}×")
    print('Tỉ lệ ok theo từng lần thử (chạy lại có giúp không):')
    ok = runs.merge(reqs[['request_id', 'loai']]).assign(ok=lambda d: d['status'] == 'ok')
    print(ok.pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean').round(3))

    # ---------- A4 · Cộng chi phí cố định 40 triệu đ/tháng cho phạm vi noi_dia + hang_nang ----------
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    m_pv = mo_hinh(runs, pham_vi)
    print(f"\nA4 · phạm vi noi_dia+hang_nang: {len(pham_vi)} yc, {m_pv['thanh_cong']} thành công, cps {m_pv['cps']:,.0f} đ [simulated]")
    for yc_thang in (45000, 22500):
        tc_thang = yc_thang * m_pv['thanh_cong'] / len(reqs)
        co_dinh = 40_000_000 / tc_thang
        tong_cps = m_pv['cps'] + co_dinh
        print(f'  {yc_thang:,} yc/tháng: {tc_thang:,.0f} việc thành công, cố định {co_dinh:,.0f} đ/việc'
              f' → {tong_cps:,.0f} đ = {tong_cps / BASELINE:.2f}× [simulated]')

    # ---------- B1 · Đổi từng yếu tố ----------
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
        # B2 · đổi một cặp: phải bằng tổng hai tác động riêng (mô hình cộng tuyến tính)
        'B2 · Token ×2 + xem lại ×2': dict(gia_vao=52, gia_ra=260, he_so_xem_lai=2),
    }
    print(f'\nB1/B2 · Kịch bản | cps [sim] | thay đổi   (gốc {goc:,.0f} đ)')
    thay_doi = {}
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        thay_doi[ten] = cps / goc - 1
        print(f'{ten:28s} {cps:8,.0f} {thay_doi[ten] * 100:+6.1f}%')
    # Tự kiểm tra: giảm một nửa = nửa mức tăng của gấp đôi
    for x in ('Giá token', 'Xem lại', 'Làm lại'):
        assert abs(thay_doi[f'{x} giảm một nửa'] + thay_doi[f'{x} gấp đôi'] / 2) < 1e-9, x

    # ---------- B3 · Giới hạn số lần chạy: chi phí cả hệ thống ----------
    print('\nB3 · Giới hạn | tổng trợ lý [sim] | không thành công | cả hệ thống | cps')
    for k in (1, 2, 3):
        m = mo_hinh(runs, reqs, max_lan_chay=k)
        khong_tc = len(reqs) - m['thanh_cong']
        print(f"{k} lần {m['tong']:14,.0f} {khong_tc:6d} {m['tong'] + khong_tc * BASELINE:14,.0f} {m['cps']:8,.0f}")

    # ---------- B4 · Xem lại 100% cho noi_dia + hang_nang ----------
    co_ok = runs[runs['status'] == 'ok']['request_id']
    so_xem = pham_vi['request_id'].isin(co_ok).sum()
    so_lam_lai = (pham_vi['ket_qua'] == 'lam_lai').sum()
    token_tool = m_pv['token'] + m_pv['tool']
    phut_lam_lai_tb = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean()
    print(f'\nB4 · {so_xem} yc được xem lại (5 phút), {so_lam_lai} ca làm lại, token+tool {token_tool:,.0f} đ')
    for phut_lam_lai in (9, phut_lam_lai_tb):
        tong = so_xem * 5 * LUONG_PHUT + so_lam_lai * phut_lam_lai * LUONG_PHUT + token_tool
        cps = tong / m_pv['thanh_cong']
        hoa_von = (BASELINE * m_pv['thanh_cong'] - token_tool - so_lam_lai * phut_lam_lai * LUONG_PHUT) / (so_xem * LUONG_PHUT)
        print(f'  làm lại {phut_lam_lai:.1f} phút/ca: tổng {tong:,.0f} đ → {cps:,.0f} đ = {cps / BASELINE:.2f}×'
              f' [simulated]; hoà vốn khi xem lại ≤ {hoa_von:.1f} phút')
    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
