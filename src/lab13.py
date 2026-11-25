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


def tinh_he_thong(ket_qua, so_yc):
    """Chi phí cả hệ thống = tổng chi phí trợ lý + BASELINE × số yêu cầu không thành công (nhân viên làm thay)."""
    khong_tc = so_yc - ket_qua['thanh_cong']
    return ket_qua['tong'] + BASELINE * khong_tc, khong_tc


def bang_a2(runs, reqs):
    kq = mo_hinh(runs, reqs)
    print('\n== A2 · Chi phí từ trace (simulated cho xem_lai, lam_lai, tong, cps) ==')
    for ten, gia_tri in kq.items():
        print(f'{ten:14s} {gia_tri:>14,.1f}')
    print(f'cps / hoá đơn mỗi yêu cầu = {kq["cps"] / kq["hoa_don_moi_yc"]:.1f}×')
    tong_ht, khong_tc = tinh_he_thong(kq, len(reqs))
    print(f'Cả hệ thống: {tong_ht / len(reqs):,.0f} đ/yêu cầu = {tong_ht / len(reqs) / BASELINE:.2f}× của {BASELINE:,} đ [simulated]')
    for ten, cot in (('token', 'token'), ('tool', 'tool'), ('xem_lai', 'xem_lai'), ('lam_lai', 'lam_lai')):
        print(f'  tỉ trọng {ten:8s} {kq[cot] / kq["tong"] * 100:5.1f}%')
    return kq


def bang_a3(runs, reqs):
    print('\n== A3 · Theo loại yêu cầu [simulated] ==')
    print(f'{"loai":10s} {"so_yc":>6s} {"ti_le_tc":>9s} {"lan/yc":>7s} {"cps":>9s} {"vs 12k":>7s}')
    for loai in sorted(reqs['loai'].unique()):
        sub = reqs[reqs['loai'] == loai]
        kq = mo_hinh(runs, sub)
        so_run = runs['request_id'].isin(sub['request_id']).sum()
        print(f'{loai:10s} {len(sub):6d} {kq["thanh_cong"] / len(sub) * 100:8.1f}% '
              f'{so_run / len(sub):7.2f} {kq["cps"]:9,.0f} {kq["cps"] / BASELINE:6.2f}×')
    print('\nTỉ lệ ok theo lần thử (attempt) và loại:')
    gop = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    gop['ok'] = (gop['status'] == 'ok').astype(float)
    print(gop.pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean').round(3).to_string())


def bang_b1(runs, reqs):
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
    goc = mo_hinh(runs, reqs)['cps']
    print(f'\n== B1 · Độ nhạy [simulated] · gốc = {goc:,.0f} đ ==')
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        print(f'{ten:25s} {cps:8,.0f} {(cps / goc - 1) * 100:+6.1f}%')
    # B2
    cps = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    print(f'\n== B2 · Giá token ×2 + xem lại ×2: {cps:,.0f} đ ({(cps / goc - 1) * 100:+.1f}%) [simulated]')


def bang_b3(runs, reqs):
    print('\n== B3 · Giới hạn số lần chạy: chi phí cả hệ thống [simulated] ==')
    print(f'{"gioi han":9s} {"tong_tro_ly":>12s} {"khong_tc":>9s} {"ca_he_thong":>12s} {"cps":>7s}')
    for k in (1, 2, 3):
        kq = mo_hinh(runs, reqs, max_lan_chay=k)
        tong_ht, khong_tc = tinh_he_thong(kq, len(reqs))
        print(f'{k:>5d} lần {kq["tong"]:12,.0f} {khong_tc:9d} {tong_ht:12,.0f} {kq["cps"]:7,.0f}')


def bang_b4(runs, reqs):
    """Xem lại 100% trên noi_dia + hang_nang. Phút làm lại: 9 (đề) và trung bình thật trong dữ liệu."""
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    r = runs[runs['request_id'].isin(pham_vi['request_id'])]
    token_tool = ((r['tokens_in'] / 1000 * GIA_VAO + r['tokens_out'] / 1000 * GIA_RA) + r['tool_calls'] * GIA_TOOL).sum()
    co_ok = r[r['status'] == 'ok']['request_id'].nunique()
    lam_lai = pham_vi[pham_vi['ket_qua'] == 'lam_lai']
    n_lam_lai = len(lam_lai)
    thanh_cong = (pham_vi['ket_qua'] == 'thanh_cong').sum()
    # Theo đáp án mẫu: trung bình phút làm lại trên TOÀN BỘ ca lam_lai của mẫu (74 ca, ≈15,3), không chỉ trong phạm vi
    phut_tb = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean()
    print('\n== B4 · Xem lại 100% (noi_dia + hang_nang) [simulated] ==')
    for nhan, phut in (('9 phút/ca (đề)', 9), (f'{phut_tb:.1f} phút/ca (dữ liệu)', phut_tb)):
        tong = token_tool + co_ok * 5 * LUONG_PHUT + n_lam_lai * phut * LUONG_PHUT
        cps = tong / thanh_cong
        hoa_von = (BASELINE * thanh_cong - token_tool - n_lam_lai * phut * LUONG_PHUT) / (co_ok * LUONG_PHUT)
        print(f'{nhan:24s} tổng {tong:12,.0f}  cps {cps:7,.0f} = {cps / BASELINE:.2f}×  hoà vốn xem lại ≤ {hoa_von:.1f} phút')
    print(f'(yc có ≥1 lần ok: {co_ok}; ca lam_lai: {n_lam_lai}; việc thành công: {thanh_cong})')


PHAM_VI_PILOT = ['noi_dia', 'hang_nang']
CO_DINH_THANG = 40_000_000   # chi phí cố định của trợ lý, đ/tháng
YC_THANG = 45_000            # yêu cầu hoàn phí mỗi tháng ở quy mô đầy đủ


def bang_a4(runs, reqs):
    """Cộng chi phí cố định 40 triệu đ/tháng vào cps của phạm vi noi_dia + hang_nang."""
    kq = mo_hinh(runs, reqs[reqs['loai'].isin(PHAM_VI_PILOT)])
    print(f'\n== A4 · Chi phí cố định, phạm vi noi_dia + hang_nang [simulated] ==')
    print(f'cps phạm vi = {kq["tong"]:,.0f} / {kq["thanh_cong"]} = {kq["cps"]:,.0f} đ')
    for nhan, he_so in (('45.000 yc/tháng', 1), ('một nửa khối lượng', 0.5)):
        viec_thang = YC_THANG * he_so * kq['thanh_cong'] / len(reqs)   # tỉ lệ thành công trong phạm vi / toàn mẫu
        co_dinh = CO_DINH_THANG / viec_thang
        tong = kq['cps'] + co_dinh
        print(f'{nhan:20s} việc TC/tháng {viec_thang:8,.0f}  cố định/việc {co_dinh:6,.0f} đ  '
              f'cps + cố định {tong:6,.0f} đ = {tong / BASELINE:.2f}×')


# ---------- Nhiệm vụ D1 · Cỡ mẫu ----------
P_GOC, MUC_TIEU, ICC = 0.70, 0.05, 0.02


def co_mau(p1, p2, alpha=0.05, power=0.8):
    """Cỡ mẫu mỗi nhóm khi so hai tỉ lệ (công thức 4 trong docs/du_lieu_va_cong_thuc.md)."""
    from statistics import NormalDist
    za, zb = NormalDist().inv_cdf(1 - alpha / 2), NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    return math.ceil((za * math.sqrt(2 * pb * (1 - pb))
                      + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2)


def he_so_thiet_ke(m, icc=ICC):
    return 1 + (m - 1) * icc


def bang_d1():
    from statsmodels.stats.proportion import proportion_effectsize
    from statsmodels.stats.power import NormalIndPower
    print('\n== D1 · Cỡ mẫu (baseline 0,70; +5 điểm; alpha 0,05; power 0,8; ICC 0,02) ==')
    n5 = co_mau(P_GOC, P_GOC + MUC_TIEU)
    print(f'a) chia theo yêu cầu: {n5:,} yêu cầu mỗi nhóm')
    de75 = he_so_thiet_ke(75)
    n_nv = math.ceil(n5 * de75)   # cỡ mẫu làm tròn lên
    print(f'b) theo nhân viên, m = 75: DE = {de75:.2f}; n = {n_nv:,.0f} mỗi nhóm → '
          f'{math.ceil(n_nv / 75)} người mỗi nhóm, tổng {2 * math.ceil(n_nv / 75)} > 40: không đủ người')
    print(f'c) 20 nhân viên mỗi nhóm: n hiệu dụng tối đa = 20 / {ICC} = {20 / ICC:,.0f} < {n5:,}: không đạt')
    print(f'd) 6 depot mỗi nhóm: n hiệu dụng tối đa = 6 / {ICC} = {6 / ICC:,.0f}')
    n6 = co_mau(P_GOC, P_GOC + 0.06)
    c = 20
    m = n6 * (1 - ICC) / (c - n6 * ICC)        # giải c·m / (1 + (m−1)·ICC) ≥ n6
    m = math.ceil(m)
    print(f'e) mức chênh 6 điểm: n = {n6} mỗi nhóm; 20 người mỗi nhóm cần m ≥ {m} yêu cầu/người '
          f'(DE {he_so_thiet_ke(m):.2f}; n hiệu dụng {c * m / he_so_thiet_ke(m):,.0f})')
    es = proportion_effectsize(P_GOC + MUC_TIEU, P_GOC)
    pw = NormalIndPower().power(effect_size=es, nobs1=n6, alpha=0.05, ratio=1)
    print(f'Đánh đổi: thiết kế cho 6 điểm (n = {n6}) mà tác động thật chỉ 5 điểm thì power ≈ {pw:.2f}')


def ti_le_mo_lai(reqs):
    toan_bo = reqs['mo_lai_trong_7_ngay'].mean()
    pv = reqs[reqs['loai'].isin(PHAM_VI_PILOT)]
    print(f'\n== Tỉ lệ mo_lai_trong_7_ngay hiện tại ==')
    print(f'toàn mẫu: {toan_bo:.2%} ({reqs["mo_lai_trong_7_ngay"].sum()}/{len(reqs)}) · '
          f'phạm vi noi_dia + hang_nang: {pv["mo_lai_trong_7_ngay"].mean():.2%} '
          f'({pv["mo_lai_trong_7_ngay"].sum()}/{len(pv)})')


# ---------- Nhiệm vụ E1 · Tính thử ba chỉ số ----------
def bang_e1(reqs):
    chinh = (reqs['dong_trong_24h'] == 1) & (reqs['mo_lai_trong_7_ngay'] == 0)
    xem = reqs[reqs['duoc_xem_lai'] == 1]
    bo_qua = xem['quyet_dinh_xem_lai'].isin(['sua', 'bo'])
    an_toan = reqs['mo_lai_trong_7_ngay'] == 1
    print('\n== E1 · Ba chỉ số trong đợt chạy thử (chưa có đối chứng) ==')
    print(f'Chính   · đóng trong 24h và không mở lại 7 ngày: {chinh.mean():.2%} ({chinh.sum()}/{len(reqs)})')
    print(f'Dùng    · bỏ qua gợi ý (sua + bo) / được xem lại: {bo_qua.mean():.2%} ({bo_qua.sum()}/{len(xem)})')
    print(f'An toàn · mở lại trong 7 ngày: {an_toan.mean():.2%} ({an_toan.sum()}/{len(reqs)})')


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    bang_a2(runs, reqs)
    bang_a3(runs, reqs)
    bang_a4(runs, reqs)
    bang_b1(runs, reqs)
    bang_b3(runs, reqs)
    bang_b4(runs, reqs)
    bang_d1()
    ti_le_mo_lai(reqs)
    bang_e1(reqs)
