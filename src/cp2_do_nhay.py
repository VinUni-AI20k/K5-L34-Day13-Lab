"""Lab 13 · Nhiệm vụ Người 2 (CP2): Kiểm số độc lập A1–A2 và Bảng độ nhạy B1–B4 + số liệu E2.

Chạy độc lập trong thư mục src/:
    python cp2_do_nhay.py

Khi Người 1 hoàn thiện mo_hinh() trong src/lab13.py, có thể gọi trong lab13.py:
    from cp2_do_nhay import chay_do_nhay
    chay_do_nhay(mo_hinh, runs, reqs)

Toàn bộ dữ liệu trong logix_runs.csv và logix_requests.csv là giả lập.
Mọi con số tính từ cột *_simulated đều được gắn nhãn [simulated].
"""
from __future__ import annotations

import pandas as pd

GIA_VAO = 26                  # đồng cho 1.000 token đầu vào
GIA_RA = 130                  # đồng cho 1.000 token đầu ra
GIA_TOOL = 15                 # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000             # đồng cho 1 phút của nhân viên
BASELINE = 12000              # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)
CHI_PHI_CO_DINH_THANG = 40_000_000
KHOI_LUONG_THANG = 45_000


def _mo_hinh_tam(
    runs: pd.DataFrame,
    reqs: pd.DataFrame,
    gia_vao: float = GIA_VAO,
    gia_ra: float = GIA_RA,
    gia_tool: float = GIA_TOOL,
    luong_phut: float = LUONG_PHUT,
    he_so_xem_lai: float = 1.0,
    he_so_lam_lai: float = 1.0,
    max_lan_chay: int | None = None,
) -> dict[str, float]:
    """Bản thay thế tạm thời cho lab13.mo_hinh theo hướng dẫn A2 để chạy độc lập."""
    reqs_cp = reqs.copy()
    runs_cp = runs[runs['request_id'].isin(reqs_cp['request_id'])].copy()
    if max_lan_chay is not None:
        runs_cp = runs_cp[runs_cp['attempt'] <= max_lan_chay]
        vuot = reqs_cp['so_lan_chay'] > max_lan_chay
        reqs_cp.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs_cp.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = runs_cp['tokens_in'] / 1000 * gia_vao + runs_cp['tokens_out'] / 1000 * gia_ra
    tien_tool = runs_cp['tool_calls'] * gia_tool
    xem_lai = reqs_cp['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs_cp['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = float(tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai)
    thanh_cong = int((reqs_cp['ket_qua'] == 'thanh_cong').sum())
    return dict(
        token=float(tien_token.sum()),
        tool=float(tien_tool.sum()),
        chay_lai=float((tien_token + tien_tool)[runs_cp['attempt'] > 1].sum()),
        xem_lai=float(xem_lai),
        lam_lai=float(lam_lai),
        tong=tong,
        thanh_cong=thanh_cong,
        cps=tong / thanh_cong,
        hoa_don_moi_yc=float((tien_token.sum() + tien_tool.sum()) / len(reqs_cp)),
    )


def kiem_tra_a1_a2_doc_lap(runs: pd.DataFrame, reqs: pd.DataFrame, mo_hinh=None) -> dict[str, float]:
    """Việc 1 (Người 2): Tính tay A1 và A2 độc lập bằng pandas để đối chiếu với Người 1."""
    print('=== KIỂM SỐ ĐỘC LẬP A1 & A2 (NGƯỜI 2) ===')

    # A1: tính trực tiếp bằng phân phối hình học
    p = 0.8
    a1_k2 = 1.0 + (1.0 - p)                     # lần 1 chắc chắn chạy (1), lần 2 chạy với XS (1-p)
    a1_inf = 1.0 / p                            # chạy đến khi đúng
    e_k3 = 1.0 + (1.0 - p) + (1.0 - p) ** 2
    p_k3 = 1.0 - (1.0 - p) ** 3
    a1_hs_k3 = e_k3 / p_k3
    assert abs(a1_k2 - 1.20) < 1e-9
    assert abs(a1_inf - 1.25) < 1e-9
    assert abs(a1_hs_k3 - 1.25) < 1e-9
    print(f'A1 độc lập: k=2 -> {a1_k2:.2f} | vô hạn -> {a1_inf:.2f} | hệ số k=3 -> {a1_hs_k3:.2f} (ĐẠT)')

    # A2: tổng hợp độc lập từ hai bảng CSV
    tong_tokens_in = float(runs['tokens_in'].sum())
    tong_tokens_out = float(runs['tokens_out'].sum())
    tong_tool_calls = int(runs['tool_calls'].sum())

    token = tong_tokens_in / 1000 * GIA_VAO + tong_tokens_out / 1000 * GIA_RA
    tool = tong_tool_calls * GIA_TOOL

    runs_retry = runs.query('attempt > 1')
    chay_lai = float(
        runs_retry['tokens_in'].sum() / 1000 * GIA_VAO
        + runs_retry['tokens_out'].sum() / 1000 * GIA_RA
        + runs_retry['tool_calls'].sum() * GIA_TOOL
    )

    phut_xem_lai = float(reqs['phut_xem_lai_simulated'].sum())
    phut_lam_lai = float(reqs['phut_lam_lai_simulated'].sum())
    xem_lai = phut_xem_lai * LUONG_PHUT
    lam_lai = phut_lam_lai * LUONG_PHUT

    tong = token + tool + xem_lai + lam_lai
    dem_kq = reqs['ket_qua'].value_counts().to_dict()
    thanh_cong = int(dem_kq.get('thanh_cong', 0))
    lam_lai_ca = int(dem_kq.get('lam_lai', 0))
    chuyen_nv_ca = int(dem_kq.get('chuyen_nhan_vien', 0))
    cps = tong / thanh_cong
    hoa_don_moi_yc = (token + tool) / len(reqs)
    he_so_gap = cps / hoa_don_moi_yc
    chi_phi_he_thong_moi_yc = (tong + (len(reqs) - thanh_cong) * BASELINE) / len(reqs)

    ket_qua = dict(
        token=token,
        tool=tool,
        chay_lai=chay_lai,
        xem_lai=xem_lai,
        lam_lai=lam_lai,
        tong=tong,
        thanh_cong=thanh_cong,
        lam_lai_ca=lam_lai_ca,
        chuyen_nv_ca=chuyen_nv_ca,
        cps=cps,
        hoa_don_moi_yc=hoa_don_moi_yc,
        he_so_gap=he_so_gap,
        chi_phi_he_thong_moi_yc=chi_phi_he_thong_moi_yc,
    )

    print(f'Token (đo từ trace):                 {token:>12,.0f} đ')
    print(f'Tool ({tong_tool_calls:,} lần, đo từ trace):    {tool:>12,.0f} đ')
    print(f'Trong đó attempt > 1 (đo từ trace):  {chay_lai:>12,.0f} đ')
    print(f'Xem lại ({phut_xem_lai:,.0f} phút, simulated):   {xem_lai:>12,.0f} đ ({xem_lai / tong * 100:.1f}%)')
    print(f'Làm lại ({phut_lam_lai:,.0f} phút, simulated): {lam_lai:>12,.0f} đ ({lam_lai / tong * 100:.1f}%)')
    print(f'Tổng chi phí [có phần simulated]:    {tong:>12,.0f} đ')
    print(f'Số việc thành công:                  {thanh_cong:>12,d} / {len(reqs)} (làm lại: {lam_lai_ca}, chuyển NV: {chuyen_nv_ca})')
    print(f'CPS [simulated]:                     {cps:>12,.1f} đ (gấp {he_so_gap:.1f}× hoá đơn/yc {hoa_don_moi_yc:,.1f} đ)')
    print(f'Cả hệ thống / yêu cầu [simulated]:   {chi_phi_he_thong_moi_yc:>12,.1f} đ ({chi_phi_he_thong_moi_yc / BASELINE:.2f}× của 12.000 đ)')

    if mo_hinh is not None:
        kq_mh = mo_hinh(runs, reqs)
        for k in ('token', 'tool', 'chay_lai', 'xem_lai', 'lam_lai', 'tong', 'thanh_cong', 'cps', 'hoa_don_moi_yc'):
            if k in kq_mh:
                assert abs(kq_mh[k] - ket_qua[k]) < 1e-6, f'Lệch đối chiếu A2 ở {k}: {kq_mh[k]} vs {ket_qua[k]}'
        print('Đối chiếu A2 độc lập với mo_hinh(): KHỚP 100%')

    return ket_qua


def chay_do_nhay(mo_hinh, runs: pd.DataFrame, reqs: pd.DataFrame) -> dict:
    """Chạy toàn bộ Nhiệm vụ B (B1, B2, B3, B4) và các số liệu hỗ trợ cho E2."""
    goc_dict = mo_hinh(runs, reqs)
    goc = goc_dict['cps']

    # ---------- B1 · Đổi từng yếu tố ----------
    print('\n=== B1 · BẢNG ĐỘ NHẠY (ĐỔI TỪNG YẾU TỐ) [simulated] ===')
    kich_ban = {
        'Giá token gấp đôi': dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa': dict(gia_vao=13, gia_ra=65),
        'Tỉ lệ xem lại gấp đôi': dict(he_so_xem_lai=2.0),
        'Tỉ lệ xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
        'Số ca làm lại gấp đôi': dict(he_so_lam_lai=2.0),
        'Số ca làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
        'Lương nhân viên tăng 25%': dict(luong_phut=2500),
        'Chỉ cho chạy tối đa 2 lần': dict(max_lan_chay=2),
        'Chỉ cho chạy 1 lần': dict(max_lan_chay=1),
    }

    b1 = {}
    print(f'{"Gốc (A2)":28s} {goc:>10,.1f} đ    (0.0%)')
    for ten, kw in kich_ban.items():
        kq = mo_hinh(runs, reqs, **kw)
        cps = kq['cps']
        pct = (cps / goc - 1.0) * 100.0
        b1[ten] = dict(cps=cps, pct=pct, tong=kq['tong'], thanh_cong=kq['thanh_cong'])
        print(f'{ten:28s} {cps:>10,.1f} đ ({pct:+6.1f}%)')

    # Tự kiểm tra CP2: giảm một nửa == đúng nửa mức tăng của gấp đôi
    cap_kiem_tra = [
        ('Giá token gấp đôi', 'Giá token giảm một nửa'),
        ('Tỉ lệ xem lại gấp đôi', 'Tỉ lệ xem lại giảm một nửa'),
        ('Số ca làm lại gấp đôi', 'Số ca làm lại giảm một nửa'),
    ]
    for ten_x2, ten_nua in cap_kiem_tra:
        tang = b1[ten_x2]['cps'] - goc
        giam = goc - b1[ten_nua]['cps']
        assert abs(giam - 0.5 * tang) < 1e-6, f'Sai tuyến tính ở {ten_x2} / {ten_nua}'
    print('Tự kiểm tra B1 (giảm một nửa = 1/2 mức tăng gấp đôi): ĐẠT')

    # ---------- B2 · Đổi một cặp và xếp hạng ----------
    print('\n=== B2 · ĐỔI MỘT CẶP VÀ XẾP HẠNG [simulated] ===')
    cap_kq = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2.0)
    cap_cps = cap_kq['cps']
    cap_pct = (cap_cps / goc - 1.0) * 100.0
    tong_hai_pct = b1['Giá token gấp đôi']['pct'] + b1['Tỉ lệ xem lại gấp đôi']['pct']
    assert abs(cap_pct - tong_hai_pct) < 1e-9, 'Tác động cặp phải bằng tổng hai tác động riêng'

    xep_hang_nguon = [
        ('Số ca làm lại (×2)', b1['Số ca làm lại gấp đôi']['pct']),
        ('Tỉ lệ xem lại (×2)', b1['Tỉ lệ xem lại gấp đôi']['pct']),
        ('Lương nhân viên (+25%)', b1['Lương nhân viên tăng 25%']['pct']),
        ('Giới hạn chạy 1 lần', b1['Chỉ cho chạy 1 lần']['pct']),
        ('Giá token (×2)', b1['Giá token gấp đôi']['pct']),
    ]
    xep_hang = sorted(xep_hang_nguon, key=lambda x: abs(x[1]), reverse=True)
    print(f'Token ×2 + Xem lại ×2: {cap_cps:,.1f} đ ({cap_pct:+.1f}%) = tổng riêng ({tong_hai_pct:+.1f}%)')
    print('Xếp hạng yếu tố ảnh hưởng mạnh nhất:', ' · '.join(f'{i}. {t} ({p:+.1f}%)' for i, (t, p) in enumerate(xep_hang[:3], 1)))

    b2 = dict(cps=cap_cps, pct=cap_pct, top3=xep_hang[:3])

    # ---------- B3 · Giới hạn chạy lại có thật sự rẻ hơn ----------
    print('\n=== B3 · CHI PHÍ CẢ HỆ THỐNG THEO GIỚI HẠN CHẠY LẠI [simulated] ===')
    b3 = {}
    for k in (1, 2, 3):
        kq = mo_hinh(runs, reqs, max_lan_chay=k)
        khong_tc = len(reqs) - int(kq['thanh_cong'])
        ca_he_thong = kq['tong'] + BASELINE * khong_tc
        b3[k] = dict(
            tong=kq['tong'],
            thanh_cong=int(kq['thanh_cong']),
            khong_thanh_cong=khong_tc,
            ca_he_thong=ca_he_thong,
            cps=kq['cps'],
        )
        print(
            f'Tối đa {k} lần | Trợ lý: {kq["tong"]:>10,.0f} đ | Không TC: {khong_tc:>3d} '
            f'| Cả hệ thống: {ca_he_thong:>10,.0f} đ | CPS: {kq["cps"]:>7,.0f} đ'
        )
    re_nhat_he_thong = min(b3, key=lambda k: b3[k]['ca_he_thong'])
    thap_nhat_cps = min(b3, key=lambda k: b3[k]['cps'])
    print(
        f'Rẻ nhất cả hệ thống: {re_nhat_he_thong} lần ({b3[re_nhat_he_thong]["ca_he_thong"]:,.0f} đ) '
        f'| CPS thấp nhất: {thap_nhat_cps} lần ({b3[thap_nhat_cps]["cps"]:,.0f} đ) '
        f'| Chênh việc đẩy sang NV: {b3[thap_nhat_cps]["khong_thanh_cong"] - b3[re_nhat_he_thong]["khong_thanh_cong"]} ca'
    )

    # ---------- B4 · Nếu phải xem lại tất cả (noi_dia + hang_nang) ----------
    print('\n=== B4 · XEM LẠI 100% TRONG PHẠM VI noi_dia + hang_nang [simulated] ===')
    reqs_pv = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])].copy()
    runs_pv = runs[runs['request_id'].isin(reqs_pv['request_id'])].copy()

    req_co_ok = runs_pv.loc[runs_pv['status'] == 'ok', 'request_id'].nunique()
    so_ca_lam_lai = int((reqs_pv['ket_qua'] == 'lam_lai').sum())
    so_thanh_cong = int((reqs_pv['ket_qua'] == 'thanh_cong').sum())
    tien_token_tool_pv = float(
        (runs_pv['tokens_in'] / 1000 * GIA_VAO
         + runs_pv['tokens_out'] / 1000 * GIA_RA
         + runs_pv['tool_calls'] * GIA_TOOL).sum()
    )

    tien_xem_lai_100 = req_co_ok * 5 * LUONG_PHUT

    # Trường hợp 1: đề bài giả định 9 phút/ca làm lại
    tien_lam_lai_9 = so_ca_lam_lai * 9 * LUONG_PHUT
    tong_b4_9 = tien_token_tool_pv + tien_xem_lai_100 + tien_lam_lai_9
    cps_b4_9 = tong_b4_9 / so_thanh_cong
    hoa_von_9 = (BASELINE * so_thanh_cong - tien_token_tool_pv - tien_lam_lai_9) / (req_co_ok * LUONG_PHUT)

    # Trường hợp 2: độ nhạy theo phút làm lại thực tế trung bình trên toàn bộ ca lam_lai trong dữ liệu
    phut_lam_lai_tb_toan_bo = float(reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean())
    phut_lam_lai_tv_toan_bo = float(reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].median())
    phut_lam_lai_tb_pv = float(reqs_pv.loc[reqs_pv['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean())

    tien_lam_lai_tb = so_ca_lam_lai * phut_lam_lai_tb_toan_bo * LUONG_PHUT
    tong_b4_tb = tien_token_tool_pv + tien_xem_lai_100 + tien_lam_lai_tb
    cps_b4_tb = tong_b4_tb / so_thanh_cong
    hoa_von_tb = (BASELINE * so_thanh_cong - tien_token_tool_pv - tien_lam_lai_tb) / (req_co_ok * LUONG_PHUT)

    print(f'Phạm vi: {len(reqs_pv)} yêu cầu | Có ít nhất 1 lần ok: {req_co_ok} | Làm lại: {so_ca_lam_lai} ({so_ca_lam_lai / len(reqs_pv) * 100:.1f}%) | Thành công: {so_thanh_cong}')
    print(f'Token + Tool phạm vi (đo từ trace):    {tien_token_tool_pv:>12,.0f} đ')
    print(f'Xem lại 100% ({req_co_ok} × 5p, simulated):   {tien_xem_lai_100:>12,.0f} đ ({tien_xem_lai_100 / tong_b4_9 * 100:.1f}% tổng TH 9p)')
    print(f'TH1 (9 phút/ca làm lại) [simulated]:   Tổng {tong_b4_9:>10,.0f} đ -> CPS {cps_b4_9:,.0f} đ ({cps_b4_9 / BASELINE:.2f}×) | Hoà vốn <= {hoa_von_9:.2f} phút/xem lại')
    print(
        f'TH2 ({phut_lam_lai_tb_toan_bo:.1f}p TB toàn bộ, TV {phut_lam_lai_tv_toan_bo:.1f}p; '
        f'riêng PV {phut_lam_lai_tb_pv:.1f}p) [simulated]: '
        f'Tổng {tong_b4_tb:>10,.0f} đ -> CPS {cps_b4_tb:,.0f} đ ({cps_b4_tb / BASELINE:.2f}×) | Hoà vốn <= {hoa_von_tb:.2f} phút/xem lại'
    )

    b4 = dict(
        so_yeu_cau=len(reqs_pv),
        req_co_ok=req_co_ok,
        so_ca_lam_lai=so_ca_lam_lai,
        ti_le_lam_lai_pv=so_ca_lam_lai / len(reqs_pv),
        so_thanh_cong=so_thanh_cong,
        token_tool=tien_token_tool_pv,
        tien_xem_lai_100=tien_xem_lai_100,
        tong_9p=tong_b4_9,
        cps_9p=cps_b4_9,
        ty_so_9p=cps_b4_9 / BASELINE,
        hoa_von_9p=hoa_von_9,
        phut_lam_lai_tb=phut_lam_lai_tb_toan_bo,
        phut_lam_lai_tv=phut_lam_lai_tv_toan_bo,
        tong_tb=tong_b4_tb,
        cps_tb=cps_b4_tb,
        ty_so_tb=cps_b4_tb / BASELINE,
        hoa_von_tb=hoa_von_tb,
    )

    # ---------- Số liệu hỗ trợ E2 (rủi ro khối lượng / chi phí cố định) ----------
    viec_tc_thang_100 = KHOI_LUONG_THANG * so_thanh_cong / len(reqs)
    co_dinh_moi_viec_100 = CHI_PHI_CO_DINH_THANG / viec_tc_thang_100
    co_dinh_moi_viec_50 = CHI_PHI_CO_DINH_THANG / (viec_tc_thang_100 / 2)
    cps_pv_goc = mo_hinh(runs, reqs_pv)['cps']
    print('\n=== SỐ LIỆU HỖ TRỢ E2 (CHI PHÍ CỐ ĐỊNH TRONG PHẠM VI) ===')
    print(
        f'CPS phạm vi gốc [simulated]: {cps_pv_goc:,.0f} đ | '
        f'Cố định 45k yc/tháng ({viec_tc_thang_100:,.0f} việc TC): +{co_dinh_moi_viec_100:,.0f} đ -> {cps_pv_goc + co_dinh_moi_viec_100:,.0f} đ | '
        f'Một nửa khối lượng: +{co_dinh_moi_viec_50:,.0f} đ -> {cps_pv_goc + co_dinh_moi_viec_50:,.0f} đ'
    )

    e2 = dict(
        ti_le_lam_lai_pv_pct=so_ca_lam_lai / len(reqs_pv) * 100.0,
        cps_pv_goc=cps_pv_goc,
        viec_tc_thang_100=viec_tc_thang_100,
        co_dinh_moi_viec_100=co_dinh_moi_viec_100,
        co_dinh_moi_viec_50=co_dinh_moi_viec_50,
    )

    return dict(goc=goc_dict, b1=b1, b2=b2, b3=b3, b4=b4, e2=e2)


def _chon_mo_hinh(runs: pd.DataFrame, reqs: pd.DataFrame):
    """Dùng lab13.mo_hinh nếu Người 1 đã viết xong, nếu chưa thì dùng bản tạm."""
    try:
        from lab13 import mo_hinh as mo_hinh_chinh

        mo_hinh_chinh(runs, reqs)
        print('Đang dùng: lab13.mo_hinh (bản chính của Người 1)')
        return mo_hinh_chinh
    except (ImportError, NotImplementedError):
        print('Đang dùng: _mo_hinh_tam (bản tạm để chạy độc lập trước khi merge p1-A)')
        return _mo_hinh_tam


if __name__ == '__main__':
    runs_df = pd.read_csv('logix_runs.csv')
    reqs_df = pd.read_csv('logix_requests.csv', keep_default_na=False)
    mh = _chon_mo_hinh(runs_df, reqs_df)
    kiem_tra_a1_a2_doc_lap(runs_df, reqs_df, mo_hinh=mh)
    chay_do_nhay(mh, runs_df, reqs_df)
