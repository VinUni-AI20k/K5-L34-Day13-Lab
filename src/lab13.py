"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
from statistics import NormalDist

import pandas as pd
from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26                    # đồng cho 1.000 token đầu vào
GIA_RA = 130                    # đồng cho 1.000 token đầu ra
GIA_TOOL = 15                   # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000               # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000                # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)
CHI_PHI_CO_DINH_THANG = 40_000_000  # đồng / tháng
KHOI_LUONG_THANG = 45_000       # yêu cầu / tháng (1.500 yêu cầu / ngày)
THU_TU_LOAI = ('noi_dia', 'hang_nang', 'quoc_te', 'doi_tac')
PHAM_VI_PILOT = ('noi_dia', 'hang_nang')


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def _kiem_tra_xac_suat(p):
    if not (0 < p <= 1):
        raise ValueError(f'Xác suất p phải nằm trong (0, 1], nhận được {p}')


def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    _kiem_tra_xac_suat(p)
    if k is None:
        return 1.0 / p
    return (1.0 - (1.0 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    _kiem_tra_xac_suat(p)
    if k is None:
        return 1.0
    return 1.0 - (1.0 - p) ** k


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
def mo_hinh(runs, reqs, gia_vao=GIA_VAO, gia_ra=GIA_RA, gia_tool=GIA_TOOL,
            luong_phut=LUONG_PHUT, he_so_xem_lai=1.0, he_so_lam_lai=1.0,
            max_lan_chay=None):
    """Trả về dict gồm: token, tool, chay_lai, xem_lai, lam_lai, tong, thanh_cong, cps, hoa_don_moi_yc.
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × luong_phut. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
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

    tien_token = runs['tokens_in'] / 1000.0 * gia_vao + runs['tokens_out'] / 1000.0 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    token_tong = float(tien_token.sum())
    tool_tong = float(tien_tool.sum())
    chay_lai = float((tien_token + tien_tool)[runs['attempt'] > 1].sum())
    xem_lai = float(reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai)
    lam_lai = float(reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai)
    tong = token_tong + tool_tong + xem_lai + lam_lai
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    cps = tong / thanh_cong if thanh_cong > 0 else float('inf')
    hoa_don_moi_yc = (token_tong + tool_tong) / len(reqs) if len(reqs) > 0 else 0.0

    return dict(
        token=token_tong,
        tool=tool_tong,
        chay_lai=chay_lai,
        xem_lai=xem_lai,
        lam_lai=lam_lai,
        tong=tong,
        thanh_cong=thanh_cong,
        cps=cps,
        hoa_don_moi_yc=hoa_don_moi_yc,
    )


# ---------- Nhiệm vụ A3 · Tách theo loại yêu cầu ----------
def phan_tich_theo_loai(runs, reqs):
    """Tính bảng chi phí và hiệu năng theo từng loại yêu cầu."""
    dong = []
    for loai in THU_TU_LOAI:
        sub = reqs[reqs['loai'] == loai]
        if len(sub) == 0:
            continue
        kq = mo_hinh(runs, sub)
        dong.append(
            dict(
                loai=loai,
                so_yeu_cau=len(sub),
                thanh_cong=kq['thanh_cong'],
                ti_le_thanh_cong=kq['thanh_cong'] / len(sub),
                lan_chay_tb=float(sub['so_lan_chay'].mean()),
                cps=kq['cps'],
                so_voi_baseline=kq['cps'] / BASELINE,
            )
        )
    return pd.DataFrame(dong)


def ti_le_ok_theo_lan_thu(runs, reqs):
    """Tỉ lệ status == 'ok' theo từng loại yêu cầu và từng lần thử (attempt)."""
    ghep = runs.merge(reqs[['request_id', 'loai']], on='request_id', how='inner')
    ghep['la_ok'] = (ghep['status'] == 'ok').astype(float)
    bang = ghep.pivot_table(index='loai', columns='attempt', values='la_ok', aggfunc='mean')
    return bang.reindex([loai for loai in THU_TU_LOAI if loai in bang.index])


# ---------- Nhiệm vụ A4 · Chi phí cố định trong phạm vi pilot ----------
def tinh_chi_phi_co_dinh(runs, reqs, pham_vi=PHAM_VI_PILOT,
                         chi_phi_co_dinh=CHI_PHI_CO_DINH_THANG,
                         khoi_luong_thang=KHOI_LUONG_THANG):
    """Cộng chi phí cố định 40 triệu đ/tháng vào chi phí mỗi việc thành công (simulated)."""
    reqs_pv = reqs[reqs['loai'].isin(pham_vi)]
    kq = mo_hinh(runs, reqs_pv)
    ty_le_trong_mau = kq['thanh_cong'] / len(reqs)

    def _theo_khoi_luong(khoi_luong):
        viec_thang = khoi_luong * ty_le_trong_mau
        co_dinh_moi_viec = chi_phi_co_dinh / viec_thang
        cps_cong = kq['cps'] + co_dinh_moi_viec
        return dict(
            khoi_luong_thang=khoi_luong,
            viec_thanh_cong_thang=viec_thang,
            co_dinh_moi_viec=co_dinh_moi_viec,
            cps_cong_co_dinh=cps_cong,
            so_voi_baseline=cps_cong / BASELINE,
        )

    return dict(
        pham_vi=pham_vi,
        so_yeu_cau_mau=len(reqs_pv),
        thanh_cong_mau=kq['thanh_cong'],
        tong_bien_doi=kq['tong'],
        cps_bien_doi=kq['cps'],
        day_du=_theo_khoi_luong(khoi_luong_thang),
        nua_khoi_luong=_theo_khoi_luong(khoi_luong_thang / 2),
    )


# ---------- Nhiệm vụ B · Bảng độ nhạy (B1, B2, B3, B4) ----------
def bang_do_nhay(runs, reqs):
    """Chạy 9 kịch bản đơn yếu tố (B1) và 1 kịch bản đổi cặp (B2)."""
    goc = mo_hinh(runs, reqs)['cps']
    kich_ban = [
        ('Giá token gấp đôi', dict(gia_vao=52, gia_ra=260)),
        ('Giá token giảm một nửa', dict(gia_vao=13, gia_ra=65)),
        ('Tỉ lệ xem lại gấp đôi', dict(he_so_xem_lai=2.0)),
        ('Tỉ lệ xem lại giảm một nửa', dict(he_so_xem_lai=0.5)),
        ('Số ca làm lại gấp đôi', dict(he_so_lam_lai=2.0)),
        ('Số ca làm lại giảm một nửa', dict(he_so_lam_lai=0.5)),
        ('Lương nhân viên tăng 25%', dict(luong_phut=2500)),
        ('Chỉ cho chạy tối đa 2 lần', dict(max_lan_chay=2)),
        ('Chỉ cho chạy 1 lần', dict(max_lan_chay=1)),
    ]

    ket_qua_b1 = []
    for ten, kw in kich_ban:
        cps = mo_hinh(runs, reqs, **kw)['cps']
        ket_qua_b1.append(
            dict(kich_ban=ten, cps=cps, thay_doi_pct=(cps / goc - 1.0) * 100.0)
        )

    cps_cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2.0)['cps']
    b2_cap = dict(
        kich_ban='Giá token gấp đôi + Tỉ lệ xem lại gấp đôi',
        cps=cps_cap,
        thay_doi_pct=(cps_cap / goc - 1.0) * 100.0,
    )

    anh_huong = {
        'Số ca làm lại': abs(ket_qua_b1[4]['thay_doi_pct']),
        'Tỉ lệ xem lại': abs(ket_qua_b1[2]['thay_doi_pct']),
        'Lương nhân viên': abs(ket_qua_b1[6]['thay_doi_pct']),
        'Giới hạn chạy lại': abs(ket_qua_b1[8]['thay_doi_pct']),
        'Giá token': abs(ket_qua_b1[0]['thay_doi_pct']),
    }
    top3 = sorted(anh_huong, key=anh_huong.get, reverse=True)[:3]

    return dict(cps_goc=goc, b1=ket_qua_b1, b2_cap=b2_cap, top3_yeu_to=top3)


def phan_tich_gioi_han_chay_lai(runs, reqs, gioi_han_list=(1, 2, 3)):
    """B3 · So sánh tổng chi phí cả hệ thống theo giới hạn số lần chạy."""
    ket_qua = []
    tong_yeu_cau = len(reqs)
    for k in gioi_han_list:
        kq = mo_hinh(runs, reqs, max_lan_chay=k)
        khong_thanh_cong = tong_yeu_cau - kq['thanh_cong']
        chi_phi_ca_he_thong = kq['tong'] + khong_thanh_cong * BASELINE
        ket_qua.append(
            dict(
                gioi_han=k,
                tong_tro_ly=kq['tong'],
                thanh_cong=kq['thanh_cong'],
                khong_thanh_cong=khong_thanh_cong,
                chi_phi_ca_he_thong=chi_phi_ca_he_thong,
                cps=kq['cps'],
            )
        )
    return ket_qua


def phan_tich_xem_lai_100(runs, reqs, pham_vi=PHAM_VI_PILOT,
                          phut_xem_lai=5.0, phut_lam_lai_de=9.0):
    """B4 · Kịch bản xem lại 100% cho phạm vi pilot (kèm độ nhạy phút làm lại thực từ dữ liệu)."""
    reqs_pv = reqs[reqs['loai'].isin(pham_vi)]
    runs_pv = runs[runs['request_id'].isin(reqs_pv['request_id'])]

    so_ca_ok = int(runs_pv.loc[runs_pv['status'] == 'ok', 'request_id'].nunique())
    so_ca_lam_lai = int((reqs_pv['ket_qua'] == 'lam_lai').sum())
    thanh_cong = int((reqs_pv['ket_qua'] == 'thanh_cong').sum())

    tien_token = float(
        (runs_pv['tokens_in'] / 1000.0 * GIA_VAO + runs_pv['tokens_out'] / 1000.0 * GIA_RA).sum()
    )
    tien_tool = float((runs_pv['tool_calls'] * GIA_TOOL).sum())
    token_tool = tien_token + tien_tool
    tien_xem_lai = so_ca_ok * phut_xem_lai * LUONG_PHUT

    # Kịch bản 1: 9 phút làm lại theo giả định đề bài
    tien_lam_lai_9 = so_ca_lam_lai * phut_lam_lai_de * LUONG_PHUT
    tong_9 = token_tool + tien_xem_lai + tien_lam_lai_9
    cps_9 = tong_9 / thanh_cong
    hoa_von_9 = (BASELINE * thanh_cong - token_tool - tien_lam_lai_9) / (so_ca_ok * LUONG_PHUT)

    # Kịch bản 2: trung bình phut_lam_lai_simulated trên toàn bộ ca lam_lai trong dữ liệu (~15,3 phút)
    phut_lam_lai_tb = float(
        reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean()
    )
    tien_lam_lai_dl = so_ca_lam_lai * phut_lam_lai_tb * LUONG_PHUT
    tong_dl = token_tool + tien_xem_lai + tien_lam_lai_dl
    cps_dl = tong_dl / thanh_cong
    hoa_von_dl = (BASELINE * thanh_cong - token_tool - tien_lam_lai_dl) / (so_ca_ok * LUONG_PHUT)

    return dict(
        pham_vi=pham_vi,
        so_yeu_cau_pham_vi=len(reqs_pv),
        so_ca_ok=so_ca_ok,
        so_ca_lam_lai=so_ca_lam_lai,
        thanh_cong=thanh_cong,
        token_tool=token_tool,
        tien_xem_lai=tien_xem_lai,
        tien_lam_lai_9_phut=tien_lam_lai_9,
        tong_9_phut=tong_9,
        cps_9_phut=cps_9,
        ti_so_9_phut=cps_9 / BASELINE,
        hoa_von_xem_lai_9_phut=hoa_von_9,
        phut_lam_lai_tb_du_lieu=phut_lam_lai_tb,
        tien_lam_lai_du_lieu=tien_lam_lai_dl,
        tong_du_lieu=tong_dl,
        cps_du_lieu=cps_dl,
        ti_so_du_lieu=cps_dl / BASELINE,
        hoa_von_xem_lai_du_lieu=hoa_von_dl,
    )


# ---------- Nhiệm vụ D1 · Cỡ mẫu & kiểm chứng NormalIndPower (CP4) ----------
def co_mau_hai_ti_le(p1, p2, alpha=0.05, power=0.80):
    """Cỡ mẫu mỗi nhóm theo công thức chuẩn so hai tỉ lệ (docs/du_lieu_va_cong_thuc.md)."""
    za = NormalDist().inv_cdf(1.0 - alpha / 2.0)
    zb = NormalDist().inv_cdf(power)
    p_bar = (p1 + p2) / 2.0
    tu_so = (
        za * math.sqrt(2.0 * p_bar * (1.0 - p_bar))
        + zb * math.sqrt(p1 * (1.0 - p1) + p2 * (1.0 - p2))
    ) ** 2
    return math.ceil(tu_so / (p2 - p1) ** 2)


def co_mau_normal_ind_power(p1, p2, alpha=0.05, power=0.80):
    """Kiểm chứng chéo cỡ mẫu mỗi nhóm bằng statsmodels NormalIndPower (Cohen's h)."""
    h = abs(proportion_effectsize(p2, p1))
    n = NormalIndPower().solve_power(
        effect_size=h, power=power, alpha=alpha, ratio=1.0, alternative='two-sided'
    )
    return math.ceil(float(n))


def tinh_power_thuc(p1, p2, n_per_arm, alpha=0.05):
    """Tính power thực tế ở mức chênh (p2 - p1) với cỡ mẫu hiệu dụng n_per_arm."""
    h = abs(proportion_effectsize(p2, p1))
    return float(
        NormalIndPower().power(
            effect_size=h, nobs1=n_per_arm, alpha=alpha, ratio=1.0, alternative='two-sided'
        )
    )


def phan_tich_co_mau_d1(p1=0.70, mde=0.05, mde_mo_rong=0.06, alpha=0.05, power=0.80,
                        icc=0.02, m_mac_dinh=75, so_nv_moi_nhom=20, so_depot_moi_nhom=6):
    """Tính đủ 5 câu D1 và kiểm chứng chéo với statsmodels NormalIndPower."""
    p2 = p1 + mde
    p2_6 = p1 + mde_mo_rong

    n_req = co_mau_hai_ti_le(p1, p2, alpha=alpha, power=power)
    n_req_sm = co_mau_normal_ind_power(p1, p2, alpha=alpha, power=power)

    de_b = 1.0 + (m_mac_dinh - 1) * icc
    n_b = math.ceil(n_req * de_b)
    nv_moi_nhom = math.ceil(n_b / m_mac_dinh)

    max_eff_nv = so_nv_moi_nhom / icc
    max_eff_depot = so_depot_moi_nhom / icc

    n_6 = co_mau_hai_ti_le(p1, p2_6, alpha=alpha, power=power)
    n_6_sm = co_mau_normal_ind_power(p1, p2_6, alpha=alpha, power=power)
    # Giải: c * m / (1 + (m - 1) * icc) >= n_6
    m_e = math.ceil(n_6 * (1.0 - icc) / (so_nv_moi_nhom - n_6 * icc))
    de_e = 1.0 + (m_e - 1) * icc
    power_tai_5pt = tinh_power_thuc(p1, p2, n_6, alpha=alpha)

    return dict(
        a_theo_yeu_cau=n_req,
        a_statsmodels_normal_ind_power=n_req_sm,
        b_design_effect=de_b,
        b_n_moi_nhom=n_b,
        b_nhan_vien_moi_nhom=nv_moi_nhom,
        b_tong_nhan_vien=nv_moi_nhom * 2,
        c_hieu_dung_toi_da_20_nv=max_eff_nv,
        d_hieu_dung_toi_da_6_depot=max_eff_depot,
        e_n_6_diem=n_6,
        e_n_6_diem_statsmodels=n_6_sm,
        e_m_toi_thieu=m_e,
        e_design_effect=de_e,
        e_power_tai_5_diem=power_tai_5pt,
    )


# ---------- Hỗ trợ đồng bộ D3 & E1 · Chỉ số đợt chạy thử ----------
def chi_so_dot_chay_thu(reqs, pham_vi=PHAM_VI_PILOT):
    """Tính thử ba chỉ số E1 và tỉ lệ mở lại trong 7 ngày làm nền cho luật an toàn D3."""
    chinh_so = int(((reqs['dong_trong_24h'] == 1) & (reqs['mo_lai_trong_7_ngay'] == 0)).sum())
    xem = reqs[reqs['duoc_xem_lai'] == 1]
    bo_qua_so = int(xem['quyet_dinh_xem_lai'].isin(['sua', 'bo']).sum())
    an_toan_so = int((reqs['mo_lai_trong_7_ngay'] == 1).sum())
    reqs_pv = reqs[reqs['loai'].isin(pham_vi)]
    an_toan_pv_so = int((reqs_pv['mo_lai_trong_7_ngay'] == 1).sum())

    return dict(
        chinh=chinh_so / len(reqs),
        chinh_tu=chinh_so,
        chinh_mau=len(reqs),
        bo_qua=bo_qua_so / len(xem),
        bo_qua_tu=bo_qua_so,
        bo_qua_mau=len(xem),
        an_toan=an_toan_so / len(reqs),
        an_toan_tu=an_toan_so,
        an_toan_mau=len(reqs),
        an_toan_pham_vi=an_toan_pv_so / len(reqs_pv),
        an_toan_pham_vi_tu=an_toan_pv_so,
        an_toan_pham_vi_mau=len(reqs_pv),
    )


def in_bao_cao(runs, reqs):
    """Chạy toàn bộ pipeline A1–A4, B1–B4, D1 và E1, in kết quả rõ ràng ra stdout."""
    print('=== NHIỆM VỤ A1 · BA PHÉP THỬ ĐÁP ÁN BIẾT TRƯỚC ===')
    kiem_tra_dap_an_biet_truoc()
    print(f'  so_lan_chay_ky_vong(0.8, 2)               = {so_lan_chay_ky_vong(0.8, 2):.2f}')
    print(f'  so_lan_chay_ky_vong(0.8)                  = {so_lan_chay_ky_vong(0.8):.2f}')
    print(f'  he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) = {he_so_chi_phi_moi_viec_thanh_cong(0.8, 3):.2f}')

    print('\n=== NHIỆM VỤ A2 · MÔ HÌNH CHI PHÍ TỪ TRACE ===')
    kq = mo_hinh(runs, reqs)
    nhan_a2 = {
        'token': '[đo từ trace]',
        'tool': '[đo từ trace]',
        'chay_lai': '[đo từ trace · attempt > 1]',
        'xem_lai': '[simulated]',
        'lam_lai': '[simulated]',
        'tong': '[có phần simulated]',
        'thanh_cong': '[ket_qua == thanh_cong]',
        'cps': '[simulated]',
        'hoa_don_moi_yc': '[đo từ trace]',
    }
    for ten, gia_tri in kq.items():
        if ten == 'hoa_don_moi_yc':
            print(f'  {ten:15s} {gia_tri:>14,.1f}  {nhan_a2[ten]}')
        else:
            print(f'  {ten:15s} {gia_tri:>14,.0f}  {nhan_a2[ten]}')

    he_so_gap = kq['cps'] / kq['hoa_don_moi_yc']
    ty_trong_lam_lai = kq['lam_lai'] / kq['tong'] * 100
    ty_trong_xem_lai = kq['xem_lai'] / kq['tong'] * 100
    chi_phi_ht_moi_yc = (kq['tong'] + (len(reqs) - kq['thanh_cong']) * BASELINE) / len(reqs)
    print(f'  CPS / hoá đơn mỗi yêu cầu = {he_so_gap:.1f}x [simulated]')
    print(f'  Tỉ trọng làm lại = {ty_trong_lam_lai:.1f}% [simulated], xem lại = {ty_trong_xem_lai:.1f}% [simulated]')
    print(
        f'  Chi phí cả hệ thống / yêu cầu = {chi_phi_ht_moi_yc:,.0f} đ '
        f'({chi_phi_ht_moi_yc / BASELINE:.2f}x của 12.000 đ) [simulated]'
    )

    print('\n=== NHIỆM VỤ A3 · TÁCH THEO LOẠI YÊU CẦU ===')
    df_loai = phan_tich_theo_loai(runs, reqs)
    print(f'  {"Loại":10s} {"Số YC":>6s} {"Thành công":>11s} {"Lần/YC":>8s} {"CPS [sim]":>12s} {"So 12k":>8s}')
    for _, r in df_loai.iterrows():
        print(
            f'  {r["loai"]:10s} {int(r["so_yeu_cau"]):6d} {r["ti_le_thanh_cong"] * 100:10.1f}% '
            f'{r["lan_chay_tb"]:8.2f} {r["cps"]:11,.0f}đ {r["so_voi_baseline"]:7.2f}x'
        )

    print('\n  Tỉ lệ status == ok theo lần thử (attempt):')
    ok_rate = ti_le_ok_theo_lan_thu(runs, reqs)
    for loai, row in ok_rate.iterrows():
        chi_tiet = ' | '.join(f'Lần {int(c)}: {row[c] * 100:5.1f}%' for c in ok_rate.columns if pd.notna(row[c]))
        print(f'    {loai:10s}: {chi_tiet}')

    print('\n=== NHIỆM VỤ A4 · CHI PHÍ CỐ ĐỊNH (noi_dia + hang_nang) ===')
    a4 = tinh_chi_phi_co_dinh(runs, reqs)
    print(f'  CPS biến đổi trong phạm vi = {a4["cps_bien_doi"]:,.0f} đ ({a4["thanh_cong_mau"]} việc thành công) [simulated]')
    for nhan, muc in [('45.000 yc/tháng', a4['day_du']), ('22.500 yc/tháng (1/2)', a4['nua_khoi_luong'])]:
        print(
            f'  {nhan:22s}: {muc["viec_thanh_cong_thang"]:>7,.0f} việc/tháng | '
            f'cố định {muc["co_dinh_moi_viec"]:>5,.0f} đ | '
            f'CPS+CĐ {muc["cps_cong_co_dinh"]:>6,.0f} đ ({muc["so_voi_baseline"]:.2f}x) [simulated]'
        )

    print('\n=== NHIỆM VỤ B1 & B2 · BẢNG ĐỘ NHẠY ===')
    b = bang_do_nhay(runs, reqs)
    print(f'  Gốc (A2): {b["cps_goc"]:,.0f} đ [simulated]')
    for row in b['b1']:
        print(f'  {row["kich_ban"]:30s} {row["cps"]:8,.0f} đ ({row["thay_doi_pct"]:+6.1f}%) [simulated]')
    b2 = b['b2_cap']
    print(f'  B2 · {b2["kich_ban"]}: {b2["cps"]:,.0f} đ ({b2["thay_doi_pct"]:+6.1f}%) [simulated]')
    print(f'  Top 3 yếu tố ảnh hưởng mạnh nhất: 1. {b["top3_yeu_to"][0]} · 2. {b["top3_yeu_to"][1]} · 3. {b["top3_yeu_to"][2]}')

    print('\n=== NHIỆM VỤ B3 · GIỚI HẠN CHẠY LẠI & CHI PHÍ CẢ HỆ THỐNG ===')
    b3 = phan_tich_gioi_han_chay_lai(runs, reqs)
    print(f'  {"Giới hạn":8s} {"Trợ lý [sim]":>14s} {"Không TC":>9s} {"Cả hệ thống [sim]":>18s} {"CPS [sim]":>11s}')
    for row in b3:
        print(
            f'  {row["gioi_han"]:>2d} lần   {row["tong_tro_ly"]:>13,.0f}đ '
            f'{row["khong_thanh_cong"]:>9d} {row["chi_phi_ca_he_thong"]:>17,.0f}đ '
            f'{row["cps"]:>10,.0f}đ'
        )

    print('\n=== NHIỆM VỤ B4 · XEM LẠI 100% (noi_dia + hang_nang) ===')
    b4 = phan_tich_xem_lai_100(runs, reqs)
    print(
        f'  Phạm vi: {b4["so_yeu_cau_pham_vi"]} yêu cầu | {b4["so_ca_ok"]} ca ok | '
        f'{b4["so_ca_lam_lai"]} ca làm lại | {b4["thanh_cong"]} thành công | '
        f'token+tool = {b4["token_tool"]:,.0f} đ'
    )
    print(
        f'  Giả định làm lại 9 phút/ca:    CPS = {b4["cps_9_phut"]:,.0f} đ ({b4["ti_so_9_phut"]:.2f}x) '
        f'[simulated] | hoà vốn xem lại <= {b4["hoa_von_xem_lai_9_phut"]:.1f} phút'
    )
    print(
        f'  Dữ liệu TB {b4["phut_lam_lai_tb_du_lieu"]:.1f} phút/ca:       '
        f'CPS = {b4["cps_du_lieu"]:,.0f} đ ({b4["ti_so_du_lieu"]:.2f}x) '
        f'[simulated] | hoà vốn xem lại <= {b4["hoa_von_xem_lai_du_lieu"]:.1f} phút'
    )

    print('\n=== NHIỆM VỤ D1 · CỠ MẪU & KIỂM CHỨNG NormalIndPower (CP4) ===')
    d1 = phan_tich_co_mau_d1()
    print(
        f'  a) Chia theo yêu cầu (+5 điểm): {d1["a_theo_yeu_cau"]:,} / nhóm '
        f'(statsmodels NormalIndPower: {d1["a_statsmodels_normal_ind_power"]:,})'
    )
    print(
        f'  b) Theo nhân viên (m=75):       DE = {d1["b_design_effect"]:.2f}, '
        f'n = {d1["b_n_moi_nhom"]:,}/nhóm → {d1["b_nhan_vien_moi_nhom"]} NV/nhóm '
        f'(tổng {d1["b_tong_nhan_vien"]} > 40: không đủ người)'
    )
    print(f'  c) 20 nhân viên / nhóm:         n_hiệu_dụng tối đa = {d1["c_hieu_dung_toi_da_20_nv"]:,.0f} (< 1.251: không đạt)')
    print(f'  d) 6 depot / nhóm:              n_hiệu_dụng tối đa = {d1["d_hieu_dung_toi_da_6_depot"]:,.0f} (< 1.251: không đạt)')
    print(
        f'  e) Mức chênh 6 điểm (20 NV/nhóm): n = {d1["e_n_6_diem"]:,}/nhóm '
        f'(NormalIndPower: {d1["e_n_6_diem_statsmodels"]:,}) → '
        f'm >= {d1["e_m_toi_thieu"]} yc/NV (DE = {d1["e_design_effect"]:.2f}) | '
        f'power thực ở mức 5 điểm = {d1["e_power_tai_5_diem"]:.2f}'
    )

    print('\n=== THAM CHIẾU E1 & D3 · CHỈ SỐ ĐỢT CHẠY THỬ (KHÔNG CÓ ĐỐI CHỨNG) ===')
    e1 = chi_so_dot_chay_thu(reqs)
    print(f'  Chỉ số chính (đóng 24h & không mở lại 7 ngày): {e1["chinh"] * 100:.2f}% ({e1["chinh_tu"]}/{e1["chinh_mau"]})')
    print(f'  Chỉ số dùng  (tỉ lệ bỏ qua sua+bo):            {e1["bo_qua"] * 100:.2f}% ({e1["bo_qua_tu"]}/{e1["bo_qua_mau"]})')
    print(f'  Chỉ số an toàn (mở lại 7 ngày · toàn mẫu):     {e1["an_toan"] * 100:.2f}% ({e1["an_toan_tu"]}/{e1["an_toan_mau"]})')
    print(
        f'  Chỉ số an toàn (mở lại 7 ngày · phạm vi pilot): '
        f'{e1["an_toan_pham_vi"] * 100:.2f}% ({e1["an_toan_pham_vi_tu"]}/{e1["an_toan_pham_vi_mau"]})'
    )


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    in_bao_cao(runs, reqs)
