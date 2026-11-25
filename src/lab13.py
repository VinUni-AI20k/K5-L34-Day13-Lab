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

    tien_token = (runs['tokens_in'] / 1000 * gia_vao
                  + runs['tokens_out'] / 1000 * gia_ra)
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = (reqs['phut_xem_lai_simulated'].sum()
               * luong_phut * he_so_xem_lai)
    lam_lai = (reqs['phut_lam_lai_simulated'].sum()
               * luong_phut * he_so_lam_lai)
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = (reqs['ket_qua'] == 'thanh_cong').sum()

    return dict(token=tien_token.sum(), tool=tien_tool.sum(),
                chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
                xem_lai=xem_lai, lam_lai=lam_lai, tong=tong,
                thanh_cong=thanh_cong, cps=tong / thanh_cong,
                hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs))


def in_kich_ban_b(runs, reqs):
    """Tính và in các bảng độ nhạy B1–B4."""
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
    }
    goc = mo_hinh(runs, reqs)
    ket_qua = {
        ten: mo_hinh(runs, reqs, **tham_so)
        for ten, tham_so in kich_ban.items()
    }

    print('\nB1 · Đổi từng yếu tố (các khoản nhân viên là simulated)')
    print(f'{"Kịch bản":26s} {"CPS (đ)":>12s} {"Thay đổi":>12s}')
    print(f'{"Gốc (A2)":26s} {goc["cps"]:12,.0f} {"—":>12s}')
    for ten, ket_qua_kich_ban in ket_qua.items():
        thay_doi = (ket_qua_kich_ban['cps'] / goc['cps'] - 1) * 100
        print(f'{ten:26s} {ket_qua_kich_ban["cps"]:12,.0f} {thay_doi:+11.1f}%')

    ket_qua_ghep = mo_hinh(
        runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2
    )
    thay_doi_ghep = (ket_qua_ghep['cps'] / goc['cps'] - 1) * 100
    print('\nB2 · Kịch bản kết hợp và xếp hạng')
    print('Token gấp đôi + xem lại gấp đôi: '
          f'{ket_qua_ghep["cps"]:,.0f} đ ({thay_doi_ghep:+.1f}%)')
    xep_hang = [
        ('số ca làm lại', abs(ket_qua['Làm lại gấp đôi']['cps'] - goc['cps'])),
        ('tỉ lệ xem lại', abs(ket_qua['Xem lại gấp đôi']['cps'] - goc['cps'])),
        ('lương nhân viên', abs(ket_qua['Lương tăng 25%']['cps'] - goc['cps'])),
        ('giá token', abs(ket_qua['Giá token gấp đôi']['cps'] - goc['cps'])),
    ]
    xep_hang.sort(key=lambda item: item[1], reverse=True)
    print('Xếp hạng yếu tố ảnh hưởng: ' + ' · '.join(
        f'{hang}. {ten}' for hang, (ten, _) in enumerate(xep_hang[:3], 1)
    ))

    print('\nB3 · Giới hạn chạy lại (chi phí nhân viên là simulated)')
    print(f'{"Giới hạn":>10s} {"Tổng trợ lý (đ)":>18s} '
          f'{"Không thành công":>18s} {"Cả hệ thống (đ)":>18s} {"CPS (đ)":>12s}')
    ket_qua_gioi_han = {1: ket_qua['Chỉ 1 lần chạy'],
                        2: ket_qua['Tối đa 2 lần chạy'],
                        3: goc}
    for gioi_han, ket_qua_mo_hinh in ket_qua_gioi_han.items():
        khong_thanh_cong = len(reqs) - ket_qua_mo_hinh['thanh_cong']
        chi_phi_he_thong = ket_qua_mo_hinh['tong'] + khong_thanh_cong * BASELINE
        print(f'{gioi_han:>8d} lần {ket_qua_mo_hinh["tong"]:18,.0f} '
              f'{khong_thanh_cong:18,d} {chi_phi_he_thong:18,.0f} '
              f'{ket_qua_mo_hinh["cps"]:12,.0f}')

    print('\nB4 · Xem lại 100% (noi_dia + hang_nang; simulated)')
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    ket_qua_pham_vi = mo_hinh(runs, pham_vi)
    run_pham_vi = runs[runs['request_id'].isin(pham_vi['request_id'])]
    so_xem_lai = run_pham_vi.loc[
        run_pham_vi['status'] == 'ok', 'request_id'
    ].nunique()
    ca_lam_lai = pham_vi['ket_qua'] == 'lam_lai'
    so_lam_lai = ca_lam_lai.sum()
    chi_phi_token_tool = ket_qua_pham_vi['token'] + ket_qua_pham_vi['tool']
    tien_xem_lai = so_xem_lai * 5 * LUONG_PHUT
    tien_lam_lai_9_phut = so_lam_lai * 9 * LUONG_PHUT
    tong_9_phut = chi_phi_token_tool + tien_xem_lai + tien_lam_lai_9_phut
    cps_9_phut = tong_9_phut / ket_qua_pham_vi['thanh_cong']

    phut_lam_lai_simulated = reqs.loc[
        reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'
    ].mean().round(1)
    tien_lam_lai_simulated = so_lam_lai * phut_lam_lai_simulated * LUONG_PHUT
    tong_simulated = chi_phi_token_tool + tien_xem_lai + tien_lam_lai_simulated
    cps_simulated = tong_simulated / ket_qua_pham_vi['thanh_cong']
    phut_hoa_von_9 = (
        BASELINE * ket_qua_pham_vi['thanh_cong']
        - chi_phi_token_tool - tien_lam_lai_9_phut
    ) / (so_xem_lai * LUONG_PHUT)
    phut_hoa_von_simulated = (
        BASELINE * ket_qua_pham_vi['thanh_cong']
        - chi_phi_token_tool - tien_lam_lai_simulated
    ) / (so_xem_lai * LUONG_PHUT)

    print(f'Yêu cầu trong phạm vi: {len(pham_vi):,}; thành công: '
          f'{ket_qua_pham_vi["thanh_cong"]:,}; cần xem lại: {so_xem_lai:,}; '
          f'ca làm lại: {so_lam_lai:,}')
    print(f'Token + tool: {chi_phi_token_tool:,.0f} đ; xem lại '
          f'({so_xem_lai:,} × 5 phút × {LUONG_PHUT:,} đ): {tien_xem_lai:,.0f} đ')
    print(f'Giả định 5 phút xem lại + 9 phút làm lại: '
          f'làm lại {tien_lam_lai_9_phut:,.0f} đ; '
          f'{tong_9_phut:,.0f} đ tổng; {cps_9_phut:,.0f} đ/việc '
          f'({cps_9_phut / BASELINE:.2f}× baseline)')
    print(f'Dùng trung bình phut_lam_lai_simulated toàn bộ ca làm lại '
          f'({phut_lam_lai_simulated:,.1f} phút/ca; '
          f'{tien_lam_lai_simulated:,.0f} đ): '
          f'{tong_simulated:,.0f} đ tổng; {cps_simulated:,.0f} đ/việc '
          f'({cps_simulated / BASELINE:.2f}× baseline)')
    print(f'Mức xem lại hòa vốn: tối đa {phut_hoa_von_9:.1f} phút '
          f'(với 9 phút làm lại), hoặc {phut_hoa_von_simulated:.1f} phút '
          '(với thời gian làm lại simulated)')


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:12s} {gia_tri:>14,.0f}')
    # TODO CP1 · Nhiệm vụ A3: tính lại theo từng giá trị của cột loai.
    in_kich_ban_b(runs, reqs)
    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
