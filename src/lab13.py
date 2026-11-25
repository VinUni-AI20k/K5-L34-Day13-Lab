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

CO_DINH_THANG = 40_000_000   # chi phí cố định của trợ lý, đồng/tháng
YC_THANG = 45_000            # số yêu cầu hoàn phí mỗi tháng ở quy mô đầy đủ
PHAM_VI = ['noi_dia', 'hang_nang']


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if k is None:
        return 1 / p
    return (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if k is None:
        return 1.0
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
        # Bỏ các lần chạy vượt giới hạn; yêu cầu cần nhiều lần hơn coi như chuyển nhân viên.
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


# ---------- Nhiệm vụ D1 · Cỡ mẫu ----------
def co_mau(p1, p2, alpha=0.05, power=0.8):
    """Cỡ mẫu mỗi nhóm để so hai tỉ lệ (công thức trong docs/du_lieu_va_cong_thuc.md)."""
    za = NormalDist().inv_cdf(1 - alpha / 2)
    zb = NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    tu = (za * math.sqrt(2 * pb * (1 - pb)) + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2
    return math.ceil(tu / (p2 - p1) ** 2)


def he_so_thiet_ke(m, icc):
    return 1 + (m - 1) * icc


def m_toi_thieu(n_can, c, icc):
    """Số yêu cầu tối thiểu mỗi cụm để c cụm đạt cỡ mẫu hiệu dụng n_can.
    c·m / (1 + (m − 1)·ICC) ≥ n  ⇔  m·(c − n·ICC) ≥ n·(1 − ICC)."""
    if c <= n_can * icc:
        return None  # không bao giờ đạt: trần c / ICC nhỏ hơn n
    return math.ceil(n_can * (1 - icc) / (c - n_can * icc))


# ---------- In bảng ----------
def tieu_de(chu):
    print(f'\n=== {chu} ===')


def in_a2(kq, n_yc):
    tieu_de('A2 · Mô hình chi phí từ trace (toàn bộ 1.200 yêu cầu)')
    dong = [
        ('Token (mọi lần chạy)', kq['token'], 'đo từ trace'),
        ('Tool', kq['tool'], 'đo từ trace'),
        ('  trong đó lần chạy 2 và 3', kq['chay_lai'], 'đo từ trace'),
        ('Xem lại', kq['xem_lai'], 'simulated'),
        ('Làm lại', kq['lam_lai'], 'simulated'),
        ('Tổng chi phí', kq['tong'], 'có phần simulated'),
        ('Số việc thành công', kq['thanh_cong'], ''),
        ('Chi phí mỗi việc thành công', kq['cps'], 'simulated'),
        ('Hoá đơn token+tool / yêu cầu', kq['hoa_don_moi_yc'], 'đo từ trace'),
    ]
    for ten, gt, nhan in dong:
        print(f'{ten:32s} {gt:>14,.1f}  {nhan}')
    print(f'Gấp {kq["cps"] / kq["hoa_don_moi_yc"]:.1f} lần hoá đơn chia số yêu cầu')
    for k in ['lam_lai', 'xem_lai']:
        print(f'Tỉ trọng {k}: {kq[k] / kq["tong"] * 100:.1f}% [simulated]')
    print(f'Giờ nhân viên chiếm {(kq["xem_lai"] + kq["lam_lai"]) / kq["tong"] * 100:.1f}% tổng [simulated]')
    khong_tc = n_yc - kq['thanh_cong']
    he_thong = (kq['tong'] + khong_tc * BASELINE) / n_yc
    print(f'Chi phí cả hệ thống / yêu cầu (cộng {khong_tc} ca nhân viên làm thay × 12.000 đ): '
          f'{he_thong:,.0f} đ = {he_thong / BASELINE:.2f}× [simulated]')


def in_a3(runs, reqs):
    tieu_de('A3 · Tách theo loại yêu cầu [cps là simulated]')
    print(f'{"loai":10s} {"so_yc":>6s} {"ti_le_tc":>9s} {"lan/yc":>7s} {"cps":>9s} {"so_12k":>7s}')
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        r = reqs[reqs['loai'] == loai]
        kq = mo_hinh(runs, r)
        so_lan = runs['request_id'].isin(r['request_id']).sum() / len(r)
        print(f'{loai:10s} {len(r):>6d} {kq["thanh_cong"] / len(r):>9.1%} {so_lan:>7.2f} '
              f'{kq["cps"]:>9,.0f} {kq["cps"] / BASELINE:>6.2f}×')

    print('\nTỉ lệ lần chạy ok theo lần thử (chạy lại có giúp không?):')
    bang = (runs.merge(reqs[['request_id', 'loai']], on='request_id')
                .assign(ok=lambda d: (d['status'] == 'ok').astype(float))
                .pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean'))
    print((bang * 100).round(1).to_string())


def in_a4(runs, reqs):
    tieu_de('A4 · Chi phí cố định 40 triệu/tháng (phạm vi noi_dia + hang_nang)')
    r = reqs[reqs['loai'].isin(PHAM_VI)]
    kq = mo_hinh(runs, r)
    print(f'Phạm vi: {len(r)} yêu cầu, {kq["thanh_cong"]} thành công, '
          f'cps {kq["cps"]:,.0f} đ (tổng {kq["tong"]:,.0f} đ) [simulated]')
    for nhan, khoi_luong in [('45.000 yc/tháng', YC_THANG), ('Một nửa khối lượng', YC_THANG / 2)]:
        tc_thang = khoi_luong * kq['thanh_cong'] / len(reqs)
        co_dinh = CO_DINH_THANG / tc_thang
        tong = kq['cps'] + co_dinh
        print(f'{nhan:20s} tc/tháng {tc_thang:>9,.0f}  cố định/việc {co_dinh:>7,.0f} đ  '
              f'cps+cố định {tong:>7,.0f} đ = {tong / BASELINE:.2f}× [simulated]')


KICH_BAN_B1 = {
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


def in_b(runs, reqs):
    goc = mo_hinh(runs, reqs)['cps']

    tieu_de('B1 · Đổi từng yếu tố [simulated]')
    print(f'{"Gốc (A2)":25s} {goc:8,.0f}')
    thay_doi = {}
    for ten, kw in KICH_BAN_B1.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        thay_doi[ten] = cps / goc - 1
        print(f'{ten:25s} {cps:8,.0f} {thay_doi[ten] * 100:+6.1f}%')

    tieu_de('B2 · Đổi một cặp: giá token gấp đôi + xem lại gấp đôi [simulated]')
    cps = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    tong_rieng = thay_doi['Giá token gấp đôi'] + thay_doi['Xem lại gấp đôi']
    print(f'cps {cps:,.0f} đ ({(cps / goc - 1) * 100:+.1f}%); tổng hai tác động riêng {tong_rieng * 100:+.1f}%')
    xep = sorted(['Giá token gấp đôi', 'Xem lại gấp đôi', 'Làm lại gấp đôi', 'Lương tăng 25%'],
                 key=lambda t: -abs(thay_doi[t]))
    print('Xếp hạng theo mức tăng: ' + ' · '.join(f'{i + 1}. {t} ({thay_doi[t] * 100:+.1f}%)'
                                                  for i, t in enumerate(xep[:3])))

    tieu_de('B3 · Giới hạn số lần chạy và chi phí cả hệ thống [simulated]')
    print(f'{"gioi_han":>8s} {"tong_tro_ly":>12s} {"khong_tc":>9s} {"ca_he_thong":>12s} {"cps":>7s}')
    for k in [1, 2, 3]:
        kq = mo_hinh(runs, reqs, max_lan_chay=k)
        khong_tc = len(reqs) - kq['thanh_cong']
        he_thong = kq['tong'] + khong_tc * BASELINE
        print(f'{k:>8d} {kq["tong"]:>12,.0f} {khong_tc:>9d} {he_thong:>12,.0f} {kq["cps"]:>7,.0f}')

    tieu_de('B4 · Xem lại 100% trong phạm vi noi_dia + hang_nang [simulated]')
    r = reqs[reqs['loai'].isin(PHAM_VI)]
    ru = runs[runs['request_id'].isin(r['request_id'])]
    co_ok = ru.loc[ru['status'] == 'ok', 'request_id'].nunique()
    so_lam_lai = int((r['ket_qua'] == 'lam_lai').sum())
    tc = int((r['ket_qua'] == 'thanh_cong').sum())
    token_tool = (ru['tokens_in'] / 1000 * GIA_VAO + ru['tokens_out'] / 1000 * GIA_RA
                  + ru['tool_calls'] * GIA_TOOL).sum()
    xem = co_ok * 5 * LUONG_PHUT
    phut_lam_lai_tb = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated']
    print(f'{len(r)} yêu cầu; {co_ok} có ≥1 lần chạy ok → xem lại 5 phút = {xem:,.0f} đ')
    print(f'Token + tool: {token_tool:,.0f} đ; việc thành công: {tc}; ca lam_lai: {so_lam_lai}')
    print(f'Phút làm lại thực tế trong dữ liệu: trung bình {phut_lam_lai_tb.mean():.1f}, '
          f'trung vị {phut_lam_lai_tb.median():.1f}')
    for phut in [9, round(phut_lam_lai_tb.mean(), 1)]:
        lam = so_lam_lai * phut * LUONG_PHUT
        tong = token_tool + xem + lam
        hoa_von = (BASELINE * tc - token_tool - lam) / (co_ok * LUONG_PHUT)
        print(f'Làm lại {phut} phút/ca: tổng {tong:,.0f} đ → cps {tong / tc:,.0f} đ = '
              f'{tong / tc / BASELINE:.2f}×; hoà vốn khi mỗi lần xem lại ≤ {hoa_von:.1f} phút')


def in_d1():
    from statsmodels.stats.power import NormalIndPower
    from statsmodels.stats.proportion import proportion_effectsize

    p1, icc = 0.70, 0.02
    tieu_de('D1 · Cỡ mẫu (baseline 0,70; +5 điểm; alpha 0,05; power 0,8; ICC 0,02)')
    n5 = co_mau(p1, 0.75)
    print(f'a) Chia theo yêu cầu: {n5:,} yêu cầu mỗi nhóm')

    de75 = he_so_thiet_ke(75, icc)
    n_b = math.ceil(n5 * de75)
    nv_b = math.ceil(n_b / 75)
    print(f'b) Theo nhân viên, m = 75: DE = {de75:.2f}; n = {n_b:,} mỗi nhóm → {nv_b} nhân viên mỗi nhóm, '
          f'tổng {2 * nv_b} > 40: {"không đủ người" if 2 * nv_b > 40 else "đủ"}')

    tran20 = 20 / icc
    print(f'c) 20 nhân viên mỗi nhóm: trần c/ICC = {tran20:,.0f} < {n5:,}: '
          f'{"không đạt" if tran20 < n5 else "đạt"} (với m = 75 chỉ được {20 * 75 / de75:,.0f})')

    print(f'd) 6 depot mỗi nhóm: trần c/ICC = {6 / icc:,.0f}')

    n6 = co_mau(p1, 0.76)
    m6 = m_toi_thieu(n6, 20, icc)
    print(f'e) Mức chênh 6 điểm: {n6:,} mỗi nhóm; 20 nhân viên mỗi nhóm cần m ≥ {m6} yêu cầu/người '
          f'(DE {he_so_thiet_ke(m6, icc):.2f})')

    es = proportion_effectsize(0.75, p1)
    pw = NormalIndPower().power(effect_size=es, nobs1=n6, alpha=0.05, ratio=1.0)
    print(f'Đánh đổi: thiết kế cho 6 điểm (n = {n6}) mà tác động thật chỉ 5 điểm → power ≈ {pw:.2f}')


def in_so_cho_luat_dung(reqs):
    tieu_de('Số để đặt luật dừng (D3)')
    r = reqs[reqs['loai'].isin(PHAM_VI)]
    for nhan, d in [('Toàn bộ', reqs), ('noi_dia + hang_nang', r)]:
        print(f'{nhan:22s} mở lại 7 ngày {d["mo_lai_trong_7_ngay"].mean():.2%} '
              f'({int(d["mo_lai_trong_7_ngay"].sum())}/{len(d)}); '
              f'làm lại {(d["ket_qua"] == "lam_lai").mean():.2%}')


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:14s} {gia_tri:>14,.0f}')

    in_a2(ket_qua, len(reqs))
    in_a3(runs, reqs)          # CP1 · A3
    in_a4(runs, reqs)          # CP1 · A4
    in_b(runs, reqs)           # CP2 · B1–B4
    in_d1()                    # CP4 · D1
    in_so_cho_luat_dung(reqs)  # CP4 · D3
