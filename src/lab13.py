"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
from statistics import NormalDist
from pathlib import Path
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# Ba hàm dùng giả định các lần chạy độc lập với xác suất p không đổi.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if not 0 < p <= 1 or (k is not None and (not isinstance(k, int) or k < 1)):
        raise ValueError('Cần 0 < p <= 1 và k nguyên dương hoặc None')
    if k is None:
        return 1 / p
    if p == 1:
        return 1.0
    return -math.expm1(k * math.log1p(-p)) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    expected = so_lan_chay_ky_vong(p, k)
    return 1.0 if k is None else p * expected


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT (1.20, 1.25, 1.25)')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# Mô hình dùng lại cho phân tích độ nhạy và giới hạn lần chạy.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs.request_id.isin(reqs.request_id)]
    if max_lan_chay is not None:
        if not isinstance(max_lan_chay, int) or max_lan_chay < 1:
            raise ValueError('Giới hạn chạy phải là số nguyên dương')
        runs = runs[runs.attempt <= max_lan_chay]
        vuot = reqs.so_lan_chay > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0
    token = runs.tokens_in / 1000 * gia_vao + runs.tokens_out / 1000 * gia_ra
    tool = runs.tool_calls * gia_tool
    xem_lai = reqs.phut_xem_lai_simulated.sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs.phut_lam_lai_simulated.sum() * luong_phut * he_so_lam_lai
    tong = token.sum() + tool.sum() + xem_lai + lam_lai
    thanh_cong = int(reqs.ket_qua.eq('thanh_cong').sum())
    return dict(token=float(token.sum()), tool=float(tool.sum()),
                chay_lai=float((token + tool)[runs.attempt > 1].sum()),
                xem_lai=float(xem_lai), lam_lai=float(lam_lai), tong=float(tong),
                thanh_cong=thanh_cong, cps=float(tong / thanh_cong) if thanh_cong else math.inf,
                hoa_don_moi_yc=float((token.sum() + tool.sum()) / len(reqs)) if len(reqs) else math.nan)


def bao_cao_a(runs, reqs):
    """In bảng A1–A4; mọi chi phí có phút nhân viên mang nhãn simulated."""
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    print('\nA2 · Chi phí (tổng, xem lại, làm lại, cps: simulated)')
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:20s} {gia_tri:14,.2f}')
    print(f"CPS / hóa đơn mỗi yêu cầu: {ket_qua['cps'] / ket_qua['hoa_don_moi_yc']:.2f} lần (simulated)")
    print('\nA3 · Loại | số yêu cầu | thành công | lần chạy/yc | cps simulated | /12.000')
    for loai, nhom in reqs.groupby('loai', sort=False):
        m = mo_hinh(runs, nhom)
        print(f"{loai} | {len(nhom)} | {m['thanh_cong']/len(nhom):.2%} | "
              f"{nhom.so_lan_chay.mean():.2f} | {m['cps']:,.2f} | {m['cps']/BASELINE:.3f}")
    ok = runs.assign(ok=runs.status.eq('ok')).merge(reqs[['request_id', 'loai']], on='request_id')
    print('Tỉ lệ ok theo loại và attempt:')
    print(ok.pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean').to_string())
    scope = reqs[reqs.loai.isin(['noi_dia', 'hang_nang'])]
    m = mo_hinh(runs, scope)
    print('\nA4 · Khối lượng tổng/tháng | thành công trong phạm vi | cố định/việc | cps + cố định simulated')
    for volume in (45000, 22500):
        success = volume * m['thanh_cong'] / len(reqs)
        fixed = 40000000 / success
        print(f"{volume} | {success:,.0f} | {fixed:,.2f} | {m['cps']+fixed:,.2f}")


KICH_BAN = {
    'Giá token gấp đôi': dict(gia_vao=52, gia_ra=260),
    'Giá token giảm một nửa': dict(gia_vao=13, gia_ra=65),
    'Tỉ lệ xem lại gấp đôi': dict(he_so_xem_lai=2),
    'Tỉ lệ xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
    'Số ca làm lại gấp đôi': dict(he_so_lam_lai=2),
    'Số ca làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
    'Lương nhân viên tăng 25%': dict(luong_phut=2500),
    'Chỉ cho chạy tối đa 2 lần': dict(max_lan_chay=2),
    'Chỉ cho chạy 1 lần': dict(max_lan_chay=1),
}


def xem_lai_toan_bo(runs, reqs, phut_lam_lai=9, phut_xem_lai=5):
    """B4: chỉ xem lại các yêu cầu có kết quả ok; giữ mẫu số thành công.

    Giả lập thời gian xem lại toàn bộ, không cộng chồng tiền xem lại cũ.
    Giá trị 15,3 phút là giả định làm tròn theo hướng dẫn lab.
    """
    scope = reqs[reqs.loai.isin(['noi_dia', 'hang_nang'])]
    scoped_runs = runs[runs.request_id.isin(scope.request_id)]
    m = mo_hinh(scoped_runs, scope)
    n_review = scoped_runs.loc[scoped_runs.status.eq('ok'), 'request_id'].nunique()
    n_rework = int(scope.ket_qua.eq('lam_lai').sum())
    machine = m['token'] + m['tool']
    review = n_review * phut_xem_lai * LUONG_PHUT
    rework = n_rework * phut_lam_lai * LUONG_PHUT
    tong = machine + review + rework
    return dict(yeu_cau=len(scope), xem_lai=n_review, lam_lai=n_rework,
                thanh_cong=m['thanh_cong'], token_tool=machine,
                tien_xem_lai=review, tien_lam_lai=rework, tong=tong,
                cps=tong / m['thanh_cong'],
                hoa_von_phut_xem_lai=(BASELINE * m['thanh_cong'] - machine - rework) / (n_review * LUONG_PHUT))


def bao_cao_b(runs, reqs):
    print('\nB1 · Kịch bản | cps simulated | thay đổi')
    goc = mo_hinh(runs, reqs)
    for ten, kw in KICH_BAN.items():
        m = mo_hinh(runs, reqs, **kw)
        print(f"{ten} | {m['cps']:,.2f} | {(m['cps']/goc['cps']-1)*100:+.2f}%")
    cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)
    print(f"B2 · Token + xem lại gấp đôi: {cap['cps']:,.2f} ({(cap['cps']/goc['cps']-1)*100:+.2f}%) simulated")
    print('Xếp hạng: số ca làm lại, tỉ lệ xem lại, lương nhân viên.')
    print('\nB3 · Giới hạn | tổng trợ lý | không thành công | tổng hệ thống | cps (chi phí simulated)')
    for k in (1, 2, 3):
        m = mo_hinh(runs, reqs, max_lan_chay=k)
        fail = len(reqs) - m['thanh_cong']
        system = m['tong'] + fail * BASELINE
        print(f"{k} | {m['tong']:,.2f} | {fail} | {system:,.2f} | {m['cps']:,.2f}")
    print('\nB4 · Xem lại 100% kết quả ok trong noi_dia + hang_nang (simulated)')
    for minutes in (9, 15.3):
        m = xem_lai_toan_bo(runs, reqs, phut_lam_lai=minutes)
        print(f"Làm lại {minutes} phút: {m['xem_lai']} ca xem lại, {m['lam_lai']} ca làm lại, "
              f"{m['thanh_cong']} thành công; tổng {m['tong']:,.2f}; cps {m['cps']:,.2f} "
              f"= {m['cps']/BASELINE:.3f}× baseline; hòa vốn xem lại {m['hoa_von_phut_xem_lai']:.2f} phút")
    rework = reqs.loc[reqs.ket_qua.eq('lam_lai'), 'phut_lam_lai_simulated']
    print(f'Phút làm lại trung bình trong dữ liệu: {rework.mean():.4f}, trung vị {rework.median():.2f} (simulated)')


def co_mau(p1, p2, alpha=0.05, power=0.8):
    """D1: cỡ mẫu mỗi nhánh với phép thử hai phía, xấp xỉ chuẩn."""
    za = NormalDist().inv_cdf(1 - alpha / 2)
    zb = NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    return math.ceil((za * math.sqrt(2 * pb * (1 - pb))
                      + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2)


def bao_cao_d_e(runs, reqs):
    n5, n6 = co_mau(.70, .75), co_mau(.70, .76)
    de75 = 1 + 74 * .02
    m = math.ceil(n6 * (1 - .02) / (20 - n6 * .02))
    try:
        from statsmodels.stats.proportion import proportion_effectsize
        from statsmodels.stats.power import NormalIndPower
        power5 = NormalIndPower().power(abs(proportion_effectsize(.70, .75)), nobs1=n6, alpha=.05)
    except ModuleNotFoundError:
        h = abs(2 * (math.asin(math.sqrt(.75)) - math.asin(math.sqrt(.70))))
        z_crit = NormalDist().inv_cdf(1 - .05 / 2)
        z = h * math.sqrt(n6 / 2)
        power5 = (1 - NormalDist().cdf(z_crit - z)) + NormalDist().cdf(-z_crit - z)
    print('\nD1 · a yêu cầu/nhánh:', n5)
    print(f'b: DE={de75:.2f}, cần {math.ceil(n5*de75)} yêu cầu/nhánh; '
          f'{math.ceil(n5*de75/75)} người/nhánh; tổng {2*math.ceil(n5*de75/75)} > 40')
    print('c: trần 20/.02 = 1000 <', n5)
    print('d: trần 6/.02 = 300 <', n5)
    print(f'e: MDE 6 điểm, n={n6}, m={m}, DE={1+(m-1)*.02:.2f}; power ở 5 điểm={power5:.4f}')
    viewed = reqs[reqs.duoc_xem_lai.eq(1)]
    primary = (reqs.dong_trong_24h.eq(1) & reqs.mo_lai_trong_7_ngay.eq(0))
    ignored = viewed.quyet_dinh_xem_lai.isin(['sua', 'bo'])
    safe = reqs.mo_lai_trong_7_ngay.eq(1)
    scope = reqs[reqs.loai.isin(['noi_dia', 'hang_nang'])]
    print(f'\nE1 · Chính: {primary.sum()}/{len(reqs)} = {primary.mean():.2%}')
    print(f'Dùng: {ignored.sum()}/{len(viewed)} = {ignored.mean():.2%}')
    print(f'An toàn: {safe.sum()}/{len(reqs)} = {safe.mean():.2%}')
    print(f'An toàn trong phạm vi: {scope.mo_lai_trong_7_ngay.sum()}/{len(scope)} = {scope.mo_lai_trong_7_ngay.mean():.2%}')
    print(f'Tỉ lệ làm lại trong phạm vi: {scope.ket_qua.eq("lam_lai").mean():.2%}')


if __name__ == '__main__':
    data = Path(__file__).resolve().parent
    runs = pd.read_csv(data / 'logix_runs.csv', keep_default_na=False)
    reqs = pd.read_csv(data / 'logix_requests.csv', keep_default_na=False)
    bao_cao_a(runs, reqs)
    bao_cao_b(runs, reqs)
    bao_cao_d_e(runs, reqs)
