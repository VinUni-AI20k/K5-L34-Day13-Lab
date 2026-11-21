"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26                # đồng cho 1.000 token đầu vào
GIA_RA = 130                # đồng cho 1.000 token đầu ra
GIA_TOOL = 15               # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000           # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000            # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)
CHI_PHI_CO_DINH = 40_000_000  # đồng/tháng cho trợ lý
KHOI_LUONG_THANG = 45_000   # yêu cầu hoàn phí mỗi tháng trên toàn công ty


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    return 1.0 / p if k is None else (1.0 - (1.0 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    return 1.0 if k is None else 1.0 - (1.0 - p) ** k


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
    """Tính chi phí từ trace cho tập yêu cầu reqs và các lần chạy tương ứng.
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × luong_phut. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy).
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        # Yêu cầu vượt giới hạn bị chuyển sang nhân viên tự làm nên không phát sinh phút xem lại/làm lại của trợ lý.
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token_run = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool_run = runs['tool_calls'] * gia_tool

    token = float(tien_token_run.sum())
    tool = float(tien_tool_run.sum())
    chay_lai = float((tien_token_run + tien_tool_run)[runs['attempt'] > 1].sum())
    xem_lai = float(reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai)
    lam_lai = float(reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai)
    tong = token + tool + xem_lai + lam_lai
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    cps = tong / thanh_cong
    hoa_don_moi_yc = (token + tool) / len(reqs)

    return dict(
        token=token,
        tool=tool,
        chay_lai=chay_lai,
        xem_lai=xem_lai,
        lam_lai=lam_lai,
        tong=tong,
        thanh_cong=thanh_cong,
        cps=cps,
        hoa_don_moi_yc=hoa_don_moi_yc,
    )


def in_bang_a1():
    """Chạy và in kết quả ba phép thử A1."""
    print('\n=== A1 · Ba phép thử đáp án biết trước (p = 0,8) ===')
    kiem_tra_dap_an_biet_truoc()
    print(f'  Số lần chạy trung bình, tối đa 2 lần       : {so_lan_chay_ky_vong(0.8, 2):.2f}')
    print(f'  Số lần chạy trung bình, chạy đến khi đúng  : {so_lan_chay_ky_vong(0.8):.2f}')
    print(f'  Hệ số chi phí mỗi việc thành công, tối đa 3: {he_so_chi_phi_moi_viec_thanh_cong(0.8, 3):.2f}')


def in_bang_a2(runs, reqs):
    """In bảng A2 (9 dòng) và đối chiếu công bằng với baseline nhân viên tự làm."""
    kq = mo_hinh(runs, reqs)
    tong_tool = int(runs['tool_calls'].sum())
    phut_xem = reqs['phut_xem_lai_simulated'].sum()
    phut_lam = reqs['phut_lam_lai_simulated'].sum()
    khong_tc = len(reqs) - kq['thanh_cong']
    chi_phi_he_thong_moi_yc = (kq['tong'] + khong_tc * BASELINE) / len(reqs)

    print('\n=== A2 · Mô hình chi phí từ trace ===')
    print(f'  Token (đo từ trace)                        : {kq["token"]:>12,.0f} đ')
    print(f'  Tool ({tong_tool:,} lần, đo từ trace)              : {kq["tool"]:>12,.0f} đ')
    print(f'  Trong đó, lần chạy thứ 2 và 3 (đo từ trace): {kq["chay_lai"]:>12,.0f} đ')
    print(f'  Xem lại ({phut_xem:,.0f} phút) [simulated]             : {kq["xem_lai"]:>12,.0f} đ')
    print(f'  Làm lại ({phut_lam:,.0f} phút) [simulated]           : {kq["lam_lai"]:>12,.0f} đ')
    print(f'  Tổng chi phí [simulated]                   : {kq["tong"]:>12,.0f} đ')
    print(f'  Số việc thành công (ket_qua=thanh_cong)    : {kq["thanh_cong"]:>12,d}')
    print(f'  Chi phí mỗi việc thành công [simulated]    : {kq["cps"]:>12,.0f} đ')
    print(f'  Hoá đơn token + tool / số yêu cầu (trace)  : {kq["hoa_don_moi_yc"]:>12,.1f} đ')
    print(f'  -> CPS gấp hoá đơn/yêu cầu [simulated]     : {kq["cps"] / kq["hoa_don_moi_yc"]:.1f}×')
    print(
        f'  -> Tỉ trọng [simulated]: làm lại {kq["lam_lai"] / kq["tong"] * 100:.1f}%, '
        f'xem lại {kq["xem_lai"] / kq["tong"] * 100:.1f}%, '
        f'tổng giờ NV {(kq["xem_lai"] + kq["lam_lai"]) / kq["tong"] * 100:.1f}%'
    )
    print(
        f'  -> So công bằng (cộng {khong_tc} ca không TC × 12.000 đ) [simulated]: '
        f'{chi_phi_he_thong_moi_yc:,.0f} đ/yc ({chi_phi_he_thong_moi_yc / BASELINE:.2f}× của 12.000 đ)'
    )
    return kq


def in_bang_a3(runs, reqs):
    """Tách chi phí theo loại yêu cầu và tỉ lệ ok theo từng lần thử."""
    cac_loai = ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']
    print('\n=== A3 · Tách theo loại yêu cầu ===')
    print(f'  {"Loại":10s} {"Số YC":>6s} {"TL TC":>8s} {"Lần/YC":>8s} {"CPS [sim]":>12s} {"So 12k":>8s}')
    for loai in cac_loai:
        sub = reqs[reqs['loai'] == loai]
        kq = mo_hinh(runs, sub)
        tl_tc = kq['thanh_cong'] / len(sub) * 100
        lan_yc = sub['so_lan_chay'].mean()
        print(
            f'  {loai:10s} {len(sub):6d} {tl_tc:7.1f}% {lan_yc:8.2f} '
            f'{kq["cps"]:11,.0f} đ {kq["cps"] / BASELINE:7.2f}×'
        )

    merged = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    merged['is_ok'] = merged['status'] == 'ok'
    ty_le_ok = merged.pivot_table(index='loai', columns='attempt', values='is_ok', aggfunc='mean')
    print('\n  Tỉ lệ status == ok theo lần chạy (attempt):')
    print(f'  {"Loại":10s} {"Lần 1":>8s} {"Lần 2":>8s} {"Lần 3":>8s}')
    for loai in cac_loai:
        r = ty_le_ok.loc[loai]
        print(f'  {loai:10s} {r.get(1, 0) * 100:7.1f}% {r.get(2, 0) * 100:7.1f}% {r.get(3, 0) * 100:7.1f}%')


def in_bang_a4(runs, reqs):
    """Cộng chi phí cố định 40 triệu đ/tháng cho phạm vi noi_dia + hang_nang."""
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    kq_pv = mo_hinh(runs, pham_vi)
    ti_le_tc_mau = kq_pv['thanh_cong'] / len(reqs)

    print('\n=== A4 · Chi phí cố định (phạm vi noi_dia + hang_nang) ===')
    print(
        f'  Trong phạm vi mẫu: {kq_pv["thanh_cong"]}/{len(reqs)} việc TC ({ti_le_tc_mau * 100:.1f}%), '
        f'tổng {kq_pv["tong"]:,.0f} đ, CPS biến đổi {kq_pv["cps"]:,.0f} đ [simulated]'
    )
    print(f'  {"Khối lượng":20s} {"TC/tháng":>10s} {"Cố định/việc":>14s} {"CPS + CĐ [sim]":>16s} {"So 12k":>8s}')
    for ten, kl in [('45.000 yc/tháng', KHOI_LUONG_THANG), ('Một nửa (22.500)', KHOI_LUONG_THANG // 2)]:
        viec_tc_thang = kl * ti_le_tc_mau
        co_dinh_viec = CHI_PHI_CO_DINH / viec_tc_thang
        tong_cps = kq_pv['cps'] + co_dinh_viec
        print(
            f'  {ten:20s} {viec_tc_thang:10,.0f} {co_dinh_viec:12,.0f} đ '
            f'{tong_cps:14,.0f} đ {tong_cps / BASELINE:7.2f}×'
        )


def in_bang_b1_b2(runs, reqs, cps_goc):
    """Chạy 9 kịch bản độ nhạy đơn (B1), 1 kịch bản cặp và xếp hạng top 3 (B2)."""
    kich_ban = [
        ('Giá token gấp đôi', dict(gia_vao=52, gia_ra=260), True),
        ('Giá token giảm một nửa', dict(gia_vao=13, gia_ra=65), False),
        ('Tỉ lệ xem lại gấp đôi', dict(he_so_xem_lai=2.0), True),
        ('Tỉ lệ xem lại giảm một nửa', dict(he_so_xem_lai=0.5), False),
        ('Số ca làm lại gấp đôi', dict(he_so_lam_lai=2.0), True),
        ('Số ca làm lại giảm một nửa', dict(he_so_lam_lai=0.5), False),
        ('Lương nhân viên tăng 25%', dict(luong_phut=2500), True),
        ('Chỉ cho chạy tối đa 2 lần', dict(max_lan_chay=2), False),
        ('Chỉ cho chạy 1 lần', dict(max_lan_chay=1), False),
    ]

    print('\n=== B1 · Đổi từng yếu tố ===')
    print(f'  {"Kịch bản":30s} {"CPS [sim]":>12s} {"Thay đổi":>10s}')
    ket_qua_tang = []
    cps_map = {}
    for ten, kw, la_tang in kich_ban:
        cps = mo_hinh(runs, reqs, **kw)['cps']
        pct = (cps / cps_goc - 1.0) * 100
        cps_map[ten] = cps
        if la_tang:
            ket_qua_tang.append((abs(pct), ten, pct))
        print(f'  {ten:30s} {cps:10,.0f} đ {pct:+9.1f}%')

    cps_cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2.0)['cps']
    pct_cap = (cps_cap / cps_goc - 1.0) * 100
    tong_tac_dong_rieng = (
        (cps_map['Giá token gấp đôi'] - cps_goc)
        + (cps_map['Tỉ lệ xem lại gấp đôi'] - cps_goc)
    )
    print('\n=== B2 · Đổi một cặp và xếp hạng ===')
    print(
        f'  Giá token ×2 + Xem lại ×2 [simulated]: {cps_cap:,.0f} đ ({pct_cap:+.1f}%), '
        f'chênh với tổng 2 tác động riêng = {(cps_cap - cps_goc) - tong_tac_dong_rieng:,.2f} đ'
    )
    ket_qua_tang.sort(reverse=True)
    top3 = ' · '.join(f'{i}. {ten} ({pct:+.1f}%)' for i, (_, ten, pct) in enumerate(ket_qua_tang[:3], 1))
    print(f'  Top 3 yếu tố ảnh hưởng mạnh nhất [simulated]: {top3}')


def in_bang_b3(runs, reqs):
    """So sánh chi phí cả hệ thống theo giới hạn số lần chạy (B3)."""
    print('\n=== B3 · Giới hạn chạy lại và chi phí cả hệ thống ===')
    print(f'  {"Giới hạn":10s} {"Tổng trợ lý [sim]":>18s} {"Không TC":>10s} {"Cả hệ thống [sim]":>19s} {"CPS [sim]":>12s}')
    for k in [1, 2, 3]:
        kq = mo_hinh(runs, reqs, max_lan_chay=k)
        khong_tc = len(reqs) - kq['thanh_cong']
        ca_he_thong = kq['tong'] + khong_tc * BASELINE
        print(
            f'  {f"{k} lần":10s} {kq["tong"]:16,.0f} đ {khong_tc:10d} '
            f'{ca_he_thong:17,.0f} đ {kq["cps"]:10,.0f} đ'
        )


def in_bang_b4(runs, reqs):
    """Tính kịch bản xem lại 100% cho noi_dia + hang_nang ở hai mức phút làm lại (B4)."""
    pv = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    runs_pv = runs[runs['request_id'].isin(pv['request_id'])]
    kq_pv = mo_hinh(runs, pv)

    so_co_ok = int(runs_pv.loc[runs_pv['status'] == 'ok', 'request_id'].nunique())
    so_lam_lai = int((pv['ket_qua'] == 'lam_lai').sum())
    so_tc = int((pv['ket_qua'] == 'thanh_cong').sum())
    tien_ai = kq_pv['token'] + kq_pv['tool']

    lam_lai_all = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated']
    tb_lam_lai = float(lam_lai_all.mean())
    trung_vi_lam_lai = float(lam_lai_all.median())

    print('\n=== B4 · Kịch bản xem lại 100% (phạm vi noi_dia + hang_nang) ===')
    print(
        f'  Số YC có ≥1 lần ok: {so_co_ok} (xem lại 5 phút/YC) | '
        f'Ca làm lại: {so_lam_lai} | Thành công: {so_tc} | Token+Tool: {tien_ai:,.0f} đ'
    )
    print(f'  Phút làm lại thực tế toàn mẫu [simulated]: TB {tb_lam_lai:.1f} phút, trung vị {trung_vi_lam_lai:.1f} phút')

    for nhan, phut_ll in [('Giả định đề (9,0 phút/ca)', 9.0), (f'Thực tế ({tb_lam_lai:.1f} phút/ca)', tb_lam_lai)]:
        tien_xem_lai = so_co_ok * 5.0 * LUONG_PHUT
        tien_lam_lai = so_lam_lai * phut_ll * LUONG_PHUT
        tong = tien_ai + tien_xem_lai + tien_lam_lai
        cps = tong / so_tc
        hoa_von_phut = (BASELINE * so_tc - tien_ai - tien_lam_lai) / (so_co_ok * LUONG_PHUT)
        print(
            f'  {nhan:28s} [simulated]: tổng {tong:>10,.0f} đ | CPS {cps:>6,.0f} đ '
            f'({cps / BASELINE:.2f}× 12k) | hoà vốn ≤ {hoa_von_phut:.1f} phút xem lại'
        )


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    in_bang_a1()
    kq_a2 = in_bang_a2(runs, reqs)
    in_bang_a3(runs, reqs)
    in_bang_a4(runs, reqs)
    in_bang_b1_b2(runs, reqs, kq_a2['cps'])
    in_bang_b3(runs, reqs)
    in_bang_b4(runs, reqs)
    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
