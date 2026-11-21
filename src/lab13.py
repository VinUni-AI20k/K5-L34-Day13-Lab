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
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    runs_tinh = runs
    hop_le = pd.Series(True, index=reqs.index)

    if max_lan_chay is not None:
        runs_tinh = runs[runs['attempt'] <= max_lan_chay]
        hop_le = reqs['so_lan_chay'] <= max_lan_chay

    token = (
        runs_tinh['tokens_in'] / 1000 * gia_vao
        + runs_tinh['tokens_out'] / 1000 * gia_ra
    ).sum()
    tool = (runs_tinh['tool_calls'] * gia_tool).sum()

    phut_xem_lai = reqs['phut_xem_lai_simulated'].fillna(0).where(hop_le, 0)
    phut_lam_lai = reqs['phut_lam_lai_simulated'].fillna(0).where(hop_le, 0)
    xem_lai = (phut_xem_lai * luong_phut * he_so_xem_lai).sum()
    lam_lai = (phut_lam_lai * luong_phut * he_so_lam_lai).sum()

    tong = token + tool + xem_lai + lam_lai
    thanh_cong = ((reqs['ket_qua'] == 'thanh_cong') & hop_le).sum()

    return {
        'token': token,
        'tool': tool,
        'xem_lai': xem_lai,
        'lam_lai': lam_lai,
        'tong': tong,
        'thanh_cong': thanh_cong,
        'cps': tong / thanh_cong,
    }


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:12s} {gia_tri:>14,.0f}')
    for v in reqs['loai'].unique():
        reqs_loai = reqs[reqs['loai'] == v]
        runs_loai = runs[runs['request_id'].isin(reqs_loai['request_id'])]
        ket_qua_loai = mo_hinh(runs_loai, reqs_loai)
        print(f'{v:12s} cps={ket_qua_loai["cps"]:>12,.0f}')

    baseline_cps = ket_qua['cps']
    b1_kich_ban = [
        ('Gia token gap doi', {'gia_vao': 52, 'gia_ra': 260}),
        ('Gia token giam mot nua', {'gia_vao': 13, 'gia_ra': 65}),
        ('Ti le xem lai gap doi', {'he_so_xem_lai': 2.0}),
        ('Ti le xem lai giam mot nua', {'he_so_xem_lai': 0.5}),
        ('So ca lam lai gap doi', {'he_so_lam_lai': 2.0}),
        ('So ca lam lai giam mot nua', {'he_so_lam_lai': 0.5}),
        ('Luong nhan vien tang 25%', {'luong_phut': 2500}),
        ('Chi cho chay toi da 2 lan', {'max_lan_chay': 2}),
        ('Chi cho chay 1 lan', {'max_lan_chay': 1}),
    ]
    b1_ket_qua = {}
    b1_thay_doi = {}
    for ten_kich_ban, tham_so in b1_kich_ban:
        ket_qua_b1 = mo_hinh(runs, reqs, **tham_so)
        b1_ket_qua[ten_kich_ban] = ket_qua_b1
        cps_val = ket_qua_b1['cps']
        pct = (cps_val - baseline_cps) / baseline_cps * 100
        b1_thay_doi[ten_kich_ban] = pct
        print(f'{ten_kich_ban:32s} cps={cps_val:>12,.0f}  thay_doi={pct:+6.1f}%')

    ket_qua_b2 = mo_hinh(
        runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2.0
    )
    cps_b2 = ket_qua_b2['cps']
    pct_b2 = (cps_b2 - baseline_cps) / baseline_cps * 100
    print(
        f'{"B2 Gia token gap doi + xem lai gap doi":32s} '
        f'cps={cps_b2:>12,.0f}  thay_doi={pct_b2:+6.1f}%'
    )
    xep_hang_b2 = sorted(
        b1_thay_doi.items(), key=lambda muc: abs(muc[1]), reverse=True
    )
    for hang, (ten_kich_ban, pct) in enumerate(xep_hang_b2[:3], start=1):
        print(f'B2 xep hang: {hang}. {ten_kich_ban} ({pct:+.1f}%)')

    for max_lan_chay in [1, 2, 3]:
        ket_qua_b3 = mo_hinh(runs, reqs, max_lan_chay=max_lan_chay)
        so_khong_thanh_cong = 1200 - ket_qua_b3['thanh_cong']
        chi_phi_he_thong = ket_qua_b3['tong'] + so_khong_thanh_cong * 12000
        print(
            f'B3 gioi han {max_lan_chay} lan: '
            f'chi_phi_he_thong={chi_phi_he_thong:>14,.0f}  '
            f'cps={ket_qua_b3["cps"]:>12,.0f}'
        )

    reqs_b4 = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    runs_b4 = runs[runs['request_id'].isin(reqs_b4['request_id'])]
    token_b4 = (
        runs_b4['tokens_in'] / 1000 * GIA_VAO
        + runs_b4['tokens_out'] / 1000 * GIA_RA
    ).sum()
    tool_b4 = (runs_b4['tool_calls'] * GIA_TOOL).sum()
    so_yeu_cau_b4 = len(reqs_b4)
    xem_lai_b4 = so_yeu_cau_b4 * 5 * LUONG_PHUT
    so_lam_lai_b4 = (reqs_b4['ket_qua'] == 'lam_lai').sum()
    lam_lai_b4 = so_lam_lai_b4 * 9 * LUONG_PHUT
    tong_b4 = token_b4 + tool_b4 + xem_lai_b4 + lam_lai_b4
    thanh_cong_b4 = so_yeu_cau_b4 - so_lam_lai_b4
    cps_b4 = tong_b4 / thanh_cong_b4
    print(f'B4 xem lai 100%: cps={cps_b4:>12,.0f}  so_voi_12000={cps_b4/12000:>6.2f}x')
    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
