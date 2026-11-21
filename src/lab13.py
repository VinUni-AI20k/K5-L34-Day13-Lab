"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import os
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
    runs = runs[runs['request_id'].isin(reqs['request_id'])].copy()
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
    thanh_cong = (reqs['ket_qua'] == 'thanh_cong').sum()
    chay_lai = (tien_token + tien_tool)[runs['attempt'] > 1].sum()
    cps = tong / thanh_cong if thanh_cong > 0 else 0
    hoa_don_moi_yc = (tien_token.sum() + tien_tool.sum()) / len(reqs)
    return dict(token=tien_token.sum(), tool=tien_tool.sum(),
                chay_lai=chay_lai, xem_lai=xem_lai, lam_lai=lam_lai,
                tong=tong, thanh_cong=thanh_cong, cps=cps,
                hoa_don_moi_yc=hoa_don_moi_yc)


if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.abspath(__file__)) if '__file__' in locals() else '.'
    runs_file = os.path.join(base_dir, 'logix_runs.csv') if os.path.exists(os.path.join(base_dir, 'logix_runs.csv')) else 'logix_runs.csv'
    reqs_file = os.path.join(base_dir, 'logix_requests.csv') if os.path.exists(os.path.join(base_dir, 'logix_requests.csv')) else 'logix_requests.csv'
    runs = pd.read_csv(runs_file)
    reqs = pd.read_csv(reqs_file, keep_default_na=False)
    
    # CP1 · A1: Kiểm tra đáp án biết trước
    kiem_tra_dap_an_biet_truoc()
    
    # CP1 · A2: Mô hình chi phí từ trace
    print('\n' + '='*50)
    print('A2 · MÔ HÌNH CHI PHÍ TỪ TRACE')
    print('='*50)
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:16s} {gia_tri:>14,.0f}')
    print(f"Chi phí mỗi việc thành công gấp: {ket_qua['cps'] / ket_qua['hoa_don_moi_yc']:.1f}x hoá đơn token+tool")
    
    # CP1 · A3: Phân tích theo loại yêu cầu
    print('\n' + '='*50)
    print('A3 · PHÂN TÍCH THEO LOẠI YÊU CẦU')
    print('='*50)
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        sub_reqs = reqs[reqs['loai'] == loai]
        sub_res = mo_hinh(runs, sub_reqs)
        n_yc = len(sub_reqs)
        tl_tc = sub_res['thanh_cong'] / n_yc * 100
        lan_chay_tb = sub_reqs['so_lan_chay'].mean()
        cps = sub_res['cps']
        so_sanh = cps / BASELINE
        print(f'{loai:10s} | YC: {n_yc:4d} | TC: {tl_tc:5.1f}% | Lần chạy: {lan_chay_tb:.2f} | CPS: {cps:7.0f} đ [sim] | So với 12k: {so_sanh:.2f}x')
    
    # CP1 · A4: Chi phí cố định (noi_dia + hang_nang)
    print('\n' + '='*50)
    print('A4 · CHI PHÍ CỐ ĐỊNH (noi_dia + hang_nang)')
    print('='*50)
    sub_scope = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    res_scope = mo_hinh(runs, sub_scope)
    tc_thang_45k = 45000 * res_scope['thanh_cong'] / len(reqs)
    cp_cd_45k = 40000000 / tc_thang_45k
    cps_tong_45k = res_scope['cps'] + cp_cd_45k
    print(f'45k/tháng : TC/tháng={tc_thang_45k:,.0f} | CĐ/việc={cp_cd_45k:,.0f} đ | Tổng CPS={cps_tong_45k:,.0f} đ [sim] ({cps_tong_45k/BASELINE:.2f}x)')
    
    tc_thang_half = tc_thang_45k / 2
    cp_cd_half = 40000000 / tc_thang_half
    cps_tong_half = res_scope['cps'] + cp_cd_half
    print(f'22.5k/tháng: TC/tháng={tc_thang_half:,.0f} | CĐ/việc={cp_cd_half:,.0f} đ | Tổng CPS={cps_tong_half:,.0f} đ [sim] ({cps_tong_half/BASELINE:.2f}x)')

    # CP2 · B1: Phân tích độ nhạy 9 kịch bản
    print('\n' + '='*50)
    print('B1 · ĐỘ NHẠY 9 KỊCH BẢN')
    print('='*50)
    kich_ban = {
        'Giá token gấp đôi':          dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa':     dict(gia_vao=13, gia_ra=65),
        'Tỉ lệ xem lại gấp đôi':      dict(he_so_xem_lai=2.0),
        'Tỉ lệ xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
        'Số ca làm lại gấp đôi':      dict(he_so_lam_lai=2.0),
        'Số ca làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
        'Lương nhân viên tăng 25%':   dict(luong_phut=2500),
        'Chỉ cho chạy tối đa 2 lần':  dict(max_lan_chay=2),
        'Chỉ cho chạy 1 lần':         dict(max_lan_chay=1),
    }
    goc = ket_qua['cps']
    for ten, kw in kich_ban.items():
        res = mo_hinh(runs, reqs, **kw)
        cps = res['cps']
        pct = (cps / goc - 1) * 100
        print(f'{ten:28s} | CPS: {cps:7.0f} đ [sim] | Thay đổi: {pct:+6.1f}%')

    # CP2 · B2: Đổi một cặp và xếp hạng
    print('\n' + '='*50)
    print('B2 · ĐỔI MỘT CẶP VÀ XẾP HẠNG')
    print('='*50)
    res_cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2.0)
    print(f"Token x2 + Xem lại x2: CPS = {res_cap['cps']:,.0f} đ [sim] ({(res_cap['cps']/goc - 1)*100:+6.1f}%)")

    # CP2 · B3: Giới hạn chạy lại
    print('\n' + '='*50)
    print('B3 · GIỚI HẠN CHẠY LẠI CẢ HỆ THỐNG')
    print('='*50)
    for k in [1, 2, 3]:
        max_k = k if k < 3 else None
        res_k = mo_hinh(runs, reqs, max_lan_chay=max_k)
        khong_tc = len(reqs) - res_k['thanh_cong']
        ca_he_thong = res_k['tong'] + khong_tc * BASELINE
        print(f"k={k} | Trợ lý: {res_k['tong']:>10,.0f} đ [sim] | Không TC: {khong_tc:3d} | Cả hệ thống: {ca_he_thong:>10,.0f} đ [sim] | CPS: {res_k['cps']:>6,.0f} đ [sim]")

    # CP2 · B4: Xem lại 100%
    print('\n' + '='*50)
    print('B4 · XEM LẠI 100% (noi_dia + hang_nang)')
    print('='*50)
    scope_reqs = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])].copy()
    scope_runs = runs[runs['request_id'].isin(scope_reqs['request_id'])].copy()
    ok_reqs = scope_runs[scope_runs['status'] == 'ok']['request_id'].unique()
    n_ok_reqs = len(ok_reqs)
    tien_token_tool_scope = (scope_runs['tokens_in']/1000*26 + scope_runs['tokens_out']/1000*130 + scope_runs['tool_calls']*15).sum()
    n_lam_lai = (scope_reqs['ket_qua'] == 'lam_lai').sum()
    thanh_cong_scope = (scope_reqs['ket_qua'] == 'thanh_cong').sum()
    
    tong_9m = tien_token_tool_scope + n_ok_reqs * 5 * 2000 + n_lam_lai * 9 * 2000
    cps_9m = tong_9m / thanh_cong_scope
    print(f"Làm lại 9m : Tổng = {tong_9m:,.0f} đ | CPS = {cps_9m:,.0f} đ [sim] ({cps_9m/BASELINE:.2f}x)")
    
    avg_lam_lai = reqs[reqs['ket_qua'] == 'lam_lai']['phut_lam_lai_simulated'].mean()
    tong_15m = tien_token_tool_scope + n_ok_reqs * 5 * 2000 + n_lam_lai * avg_lam_lai * 2000
    cps_15m = tong_15m / thanh_cong_scope
    print(f"Làm lại 15.3m: Tổng = {tong_15m:,.0f} đ | CPS = {cps_15m:,.0f} đ [sim] ({cps_15m/BASELINE:.2f}x)")

    # TODO CP4 · Nhiệm vụ D: cỡ mẫu (dành cho Người 2 tiếp quản sau)
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
