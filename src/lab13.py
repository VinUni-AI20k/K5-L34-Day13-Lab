"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Phần A tính chi phí; các phần B, D tiếp tục ở TODO CP2, CP4.
Dữ liệu trong hai file CSV là giả lập.
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
CO_DINH_THANG = 40_000_000
YEU_CAU_THANG = 45_000


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# Công thức A1 theo docs/du_lieu_va_cong_thuc.md; giả định các lần chạy độc lập,
# cùng xác suất đúng 0 < p <= 1 và giới hạn k là số nguyên dương.
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
# CP2 gọi lại hàm này với tham số giá, hệ số và giới hạn chạy đã đổi.
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
        vuot_gioi_han = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot_gioi_han, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot_gioi_han, ['phut_xem_lai_simulated',
                               'phut_lam_lai_simulated']] = 0

    tien_token = (runs['tokens_in'] * gia_vao
                  + runs['tokens_out'] * gia_ra) / 1000
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = int(reqs['ket_qua'].eq('thanh_cong').sum())
    return dict(
        token=tien_token.sum(), tool=tien_tool.sum(),
        chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
        xem_lai=xem_lai, lam_lai=lam_lai, tong=tong, thanh_cong=thanh_cong,
        cps=tong / thanh_cong if thanh_cong else math.inf,
        hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs)
        if len(reqs) else math.nan,
    )


def in_phan_a(runs, reqs):
    """In các bảng A2–A4 và số đối chiếu để điền báo cáo chi phí."""
    ket_qua = mo_hinh(runs, reqs)
    print('\nA2 · Mô hình chi phí từ trace (chưa gồm chi phí cố định)')
    cac_dong = [
        ('Token (đ)', 'token'),
        ('Tool (đ)', 'tool'),
        ('Trong đó: lần chạy thứ 2 và 3 (đ)', 'chay_lai'),
        ('Xem lại (đ, simulated)', 'xem_lai'),
        ('Làm lại (đ, simulated)', 'lam_lai'),
        ('Tổng chi phí (đ, simulated)', 'tong'),
        ('Số việc thành công', 'thanh_cong'),
        ('Chi phí mỗi việc thành công (đ, simulated)', 'cps'),
        ('Hoá đơn token + tool / yêu cầu (đ)', 'hoa_don_moi_yc'),
    ]
    for nhan, khoa in cac_dong:
        print(f'{nhan:48s} {ket_qua[khoa]:>14,.2f}')
    print(f'CPS / hoá đơn mỗi yêu cầu: '
          f'{ket_qua["cps"] / ket_qua["hoa_don_moi_yc"]:.2f} lần (simulated)')
    print(f'Tỉ trọng làm lại: {ket_qua["lam_lai"] / ket_qua["tong"]:.2%}; '
          f'xem lại: {ket_qua["xem_lai"] / ket_qua["tong"]:.2%} (simulated)')

    # Theo quy ước so sánh của lab: tính cả phần nhân viên làm thay
    # cho mọi yêu cầu không thành công, với mức 12.000 đ/yêu cầu.
    khong_thanh_cong = len(reqs) - ket_qua['thanh_cong']
    he_thong_moi_yc = (ket_qua['tong'] + khong_thanh_cong * BASELINE) / len(reqs)
    print(f'Chi phí cả hệ thống / yêu cầu: {he_thong_moi_yc:,.2f} đ '
          f'= {he_thong_moi_yc / BASELINE:.2f}× nhân viên tự làm (simulated)')

    print('\nA3 · Tách theo loại yêu cầu (CPS chưa gồm chi phí cố định)')
    bang_loai = []
    for loai, nhom in reqs.groupby('loai', sort=False):
        kq_loai = mo_hinh(runs, nhom)
        bang_loai.append({
            'Loại': loai,
            'Số yêu cầu': len(nhom),
            'Thành công': f'{kq_loai["thanh_cong"] / len(nhom):.1%}',
            'Lần chạy/YC': f'{nhom["so_lan_chay"].mean():.2f}',
            'CPS (đ, simulated)': f'{kq_loai["cps"]:,.2f}',
            'CPS/12.000 (simulated)': f'{kq_loai["cps"] / BASELINE:.2f}×',
        })
    print(pd.DataFrame(bang_loai).to_string(index=False))

    print('\nTỉ lệ status=ok theo loại và lần thử (để đánh giá chạy lại):')
    trace_loai = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    ti_le_ok = (trace_loai.assign(ok=trace_loai['status'].eq('ok'))
                .pivot_table(index='loai', columns='attempt', values='ok',
                             aggfunc='mean'))
    print(ti_le_ok.to_string(float_format=lambda gia_tri: f'{gia_tri:.1%}'))

    print('\nA4 · Cộng chi phí cố định cho noi_dia + hang_nang')
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    kq_pham_vi = mo_hinh(runs, pham_vi)
    # Mẫu gồm mọi loại yêu cầu: lấy thành công trong phạm vi / toàn bộ mẫu
    # để ngoại suy số việc thành công ở tổng khối lượng công ty mỗi tháng.
    ti_le_thanh_cong_trong_mau = kq_pham_vi['thanh_cong'] / len(reqs)
    print(f'Phạm vi: {len(pham_vi)} yêu cầu, {kq_pham_vi["thanh_cong"]} thành công; '
          f'CPS biến đổi: {kq_pham_vi["cps"]:,.2f} đ (simulated)')
    bang_co_dinh = []
    for khoi_luong in (YEU_CAU_THANG, YEU_CAU_THANG / 2):
        thanh_cong_thang = khoi_luong * ti_le_thanh_cong_trong_mau
        co_dinh_moi_viec = CO_DINH_THANG / thanh_cong_thang
        cps_co_co_dinh = kq_pham_vi['cps'] + co_dinh_moi_viec
        bang_co_dinh.append({
            'Yêu cầu/tháng': f'{khoi_luong:,.0f}',
            'Thành công/tháng': f'{thanh_cong_thang:,.0f}',
            'Cố định/việc (đ)': f'{co_dinh_moi_viec:,.2f}',
            'CPS + cố định (đ, simulated)': f'{cps_co_co_dinh:,.2f}',
            'CPS/12.000 (simulated)': f'{cps_co_co_dinh / BASELINE:.2f}×',
        })
    print(pd.DataFrame(bang_co_dinh).to_string(index=False))
    print('Cột CPS/12.000 ở A3–A4 chỉ so chi phí mỗi việc thành công; '
          'để kết luận tiết kiệm cho công ty phải cộng phần nhân viên làm thay.')


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    in_phan_a(runs, reqs)
    # TODO CP2 · Nhiệm vụ B: đổi từng yếu tố, ghi vào bảng độ nhạy.
    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
