"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import sys
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
    if not 0 < p <= 1:
        raise ValueError('p must be in (0, 1]')
    if k is None:
        return 1.0 / p
    if not isinstance(k, int) or k < 1:
        raise ValueError('k must be a positive integer or None')
    return (1.0 - (1.0 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if not 0 < p <= 1:
        raise ValueError('p must be in (0, 1]')
    if k is None:
        return 1.0
    if not isinstance(k, int) or k < 1:
        raise ValueError('k must be a positive integer or None')
    return 1.0 - (1.0 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    success = ti_le_thanh_cong(p, k)
    return so_lan_chay_ky_vong(p, k) / success


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
    runs = runs[runs['request_id'].isin(reqs['request_id'])].copy()
    if max_lan_chay is not None:
        if not isinstance(max_lan_chay, int) or max_lan_chay < 1:
            raise ValueError('max_lan_chay must be a positive integer or None')
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0
    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    token = tien_token.sum()
    tool = tien_tool.sum()
    tong = token + tool + xem_lai + lam_lai
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    chay_lai = (tien_token + tien_tool)[runs['attempt'] > 1].sum()
    return dict(token=token, tool=tool, chay_lai=chay_lai, xem_lai=xem_lai,
                lam_lai=lam_lai, tong=tong, thanh_cong=thanh_cong,
                cps=tong / thanh_cong if thanh_cong else math.nan,
                hoa_don_moi_yc=(token + tool) / len(reqs) if len(reqs) else math.nan)


if __name__ == '__main__':
    # Keep Vietnamese status labels printable in Windows consoles using legacy code pages.
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:12s} {gia_tri:>14,.0f}')
    # A3 · Chi phí theo loại yêu cầu
    print('A3 · Chi phí theo loại')
    for loai in reqs['loai'].drop_duplicates():
        loai_reqs = reqs[reqs['loai'] == loai]
        subset = mo_hinh(runs, loai_reqs)
        n_req = len(loai_reqs)
        print(f'{loai:12s} yc={n_req:4d} thanh_cong={subset["thanh_cong"]:4d} '
              f'ty_le={subset["thanh_cong"] / n_req:.1%} '
              f'lan_chay/yc={loai_reqs["so_lan_chay"].mean():.2f} '
              f'cps={subset["cps"]:,.0f}d so_voi_baseline={subset["cps"] / BASELINE:.2f}x')
    # A4 · Phân bổ 40 triệu đồng/tháng cho phạm vi pilot.
    pilot = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    pilot_cost = mo_hinh(runs, pilot)
    # Giữ mẫu số là toàn bộ mẫu để khớp tỷ lệ thành công của phạm vi trên tổng tải.
    pilot_success_rate = pilot_cost['thanh_cong'] / len(reqs)
    monthly_success = 45000 * pilot_success_rate
    fixed_per_success = 40_000_000 / monthly_success
    half_volume_fixed = fixed_per_success * 2
    print('A4 · Chi phí cố định')
    print(f'pham_vi=noi_dia+hang_nang thanh_cong_mau={pilot_cost["thanh_cong"]} '
          f'ty_le={pilot_success_rate:.1%} thanh_cong_thang={monthly_success:,.0f}')
    print(f'chi_phi_co_dinh/viec={fixed_per_success:,.0f}d '
          f'tong_cps={pilot_cost["cps"] + fixed_per_success:,.0f}d')
    print(f'nua_san_luong: chi_phi_co_dinh/viec={half_volume_fixed:,.0f}d '
          f'tong_cps={pilot_cost["cps"] + half_volume_fixed:,.0f}d')
    # TODO CP2 · Nhiệm vụ B: đổi từng yếu tố, ghi vào bảng độ nhạy.
    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
