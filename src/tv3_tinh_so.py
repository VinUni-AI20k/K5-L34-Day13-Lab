"""Lab 13 · Phần tính của Thành viên 3 (không sửa lab13.py: file đó do Thành viên 1 giữ).
Chạy trong thư mục src/: python3 tv3_tinh_so.py
Mỗi checkpoint một hàm; số in ra để gửi cho người giữ file tương ứng
(A3, B3 → Thành viên 2 giữ bang_chi_phi.md; D1e, D2, chỉ số an toàn → Thành viên 4 giữ pilot_plan.yaml / chi_so.md).
Mọi số tính từ cột *_simulated đều ghi nhãn [simulated].
"""
import math
from statistics import NormalDist

import pandas as pd
from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize

from lab13 import mo_hinh, BASELINE   # dùng đúng mô hình của Thành viên 1

LOAI = ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']
PHAM_VI = ['noi_dia', 'hang_nang']
ICC = 0.02


def doc_du_lieu():
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    return runs, reqs


def d(x):
    """Định dạng số tiền kiểu Việt Nam: 1.234.567"""
    return f'{x:,.0f}'.replace(',', '.')


def pct(x, so_le=1):
    return f'{x * 100:.{so_le}f}'.replace('.', ',') + '%'


def so(x, so_le=2):
    return f'{x:.{so_le}f}'.replace('.', ',')


def cp1_a3(runs, reqs):
    print('=== CP1 · A3 · Tách theo loại yêu cầu ===')
    print('| Loại | Số yêu cầu | Tỉ lệ thành công | Lần chạy / yêu cầu '
          '| Chi phí mỗi việc thành công [simulated] | So với 12.000 đ [simulated] |')
    print('| --- | ---: | ---: | ---: | ---: | ---: |')
    for loai in LOAI:
        r = reqs[reqs['loai'] == loai]
        m = mo_hinh(runs, r)
        so_chay = runs['request_id'].isin(r['request_id']).sum()
        print(f"| {loai} | {len(r)} | {pct(m['thanh_cong'] / len(r))} | {so(so_chay / len(r))} "
              f"| {d(m['cps'])} đ | {so(m['cps'] / BASELINE)}× |")

    # Chạy lại có giúp không: tỉ lệ ok của từng lần thử, theo loại
    rr = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    rr['ok'] = (rr['status'] == 'ok').astype(float)
    bang = rr.pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean').reindex(LOAI)
    print()
    print('Tỉ lệ lần chạy ok theo lần thử (đo từ trace):')
    print('| Loại | Lần 1 | Lần 2 | Lần 3 |')
    print('| --- | ---: | ---: | ---: |')
    for loai, hang in bang.iterrows():
        print(f'| {loai} | ' + ' | '.join(pct(v) for v in hang.values) + ' |')
    print()


def cp2_b3(runs, reqs):
    print('=== CP2 · B3 · Giới hạn chạy lại và chi phí cả hệ thống ===')
    print('| Giới hạn | Tổng trợ lý [simulated] | Không thành công | Nhân viên làm thay (× 12.000 đ) '
          '| Cả hệ thống [simulated] | Chi phí mỗi việc thành công [simulated] |')
    print('| --- | ---: | ---: | ---: | ---: | ---: |')
    kq = {}
    for k in [1, 2, 3]:
        m = mo_hinh(runs, reqs, max_lan_chay=k)
        khong_tc = len(reqs) - m['thanh_cong']
        nv = khong_tc * BASELINE
        he_thong = m['tong'] + nv
        kq[k] = (he_thong, m['cps'], khong_tc)
        print(f"| {k} lần | {d(m['tong'])} đ | {khong_tc} | {d(nv)} đ | {d(he_thong)} đ | {d(m['cps'])} đ |")
    re_nhat = min(kq, key=lambda k: kq[k][0])
    cps_thap = min(kq, key=lambda k: kq[k][1])
    print(f'Rẻ nhất cho công ty: {re_nhat} lần ({d(kq[re_nhat][0])} đ) [simulated]; '
          f'chi phí mỗi việc thành công thấp nhất: {cps_thap} lần ({d(kq[cps_thap][1])} đ) [simulated]; '
          f'chọn {cps_thap} lần đẩy thêm {kq[cps_thap][2] - kq[re_nhat][2]} việc sang nhân viên')
    print()


def co_mau(p1, p2, alpha=0.05, power=0.8):
    za, zb = NormalDist().inv_cdf(1 - alpha / 2), NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    return math.ceil((za * math.sqrt(2 * pb * (1 - pb))
                      + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2)


def cp4_d1e():
    print('=== CP4 · D1(e) · Mức chênh 6 điểm, 20 nhân viên mỗi nhóm ===')
    n_tay = co_mau(0.70, 0.76)
    es = proportion_effectsize(0.76, 0.70)
    n_sm = NormalIndPower().solve_power(effect_size=es, alpha=0.05, power=0.8, ratio=1)
    print(f'Cỡ mẫu mỗi nhóm (công thức tay): {n_tay}; statsmodels (Cohen h): {math.ceil(n_sm)}')
    c = 20
    # c·m / (1 + (m−1)·ICC) ≥ n  →  m ≥ n·(1 − ICC) / (c − n·ICC)
    m_min = math.ceil(n_tay * (1 - ICC) / (c - n_tay * ICC))
    de = 1 + (m_min - 1) * ICC
    print(f'm ≥ {m_min} yêu cầu mỗi nhân viên, DE = {so(de)}, '
          f'n hiệu dụng = {d(c * m_min / de)} (trần c/ICC = {d(c / ICC)})')
    pw = NormalIndPower().power(effect_size=proportion_effectsize(0.75, 0.70), nobs1=n_tay, alpha=0.05)
    print(f'Nếu tác động thật chỉ 5 điểm mà cỡ mẫu {n_tay}/nhóm: power ≈ {so(pw)}')
    print()


def cp5_an_toan(reqs):
    print('=== CP5 · Chỉ số an toàn: mở lại trong 7 ngày (hiện tại) ===')
    t = reqs['mo_lai_trong_7_ngay'].astype(int)
    print(f'Toàn mẫu: {pct(t.mean(), 2)} ({t.sum()}/{len(reqs)})')
    pv = reqs['loai'].isin(PHAM_VI)
    print(f'Phạm vi noi_dia + hang_nang: {pct(t[pv].mean(), 2)} ({t[pv].sum()}/{pv.sum()})')
    for loai in LOAI:
        s = t[reqs['loai'] == loai]
        print(f'  {loai:10s} {pct(s.mean(), 2)} ({s.sum()}/{len(s)})')
    # Chỉ số an toàn đề xuất thêm: mở lại 7 ngày tách theo có/không được xem lại.
    # Dùng để biết giảm tỉ lệ xem lại (đòn bẩy chi phí ở B1) có làm lỗi lọt đến khách tăng không.
    xem = reqs['duoc_xem_lai'].astype(int) == 1
    khong = t[~xem]
    giu = t[reqs['quyet_dinh_xem_lai'] == 'giu']
    print(f'Đề xuất thêm · mở lại 7 ngày ở ca KHÔNG được xem lại: {pct(khong.mean(), 2)} '
          f'({khong.sum()}/{len(khong)}); ở ca xem lại và giữ: {pct(giu.mean(), 2)} ({giu.sum()}/{len(giu)})')
    lai = reqs.groupby('ket_qua')['mo_lai_trong_7_ngay'].apply(lambda s: int(s.astype(int).sum()))
    print('Ca mở lại theo ket_qua: ' + ', '.join(f'{k}={v}' for k, v in lai.items()))
    print()


if __name__ == '__main__':
    runs, reqs = doc_du_lieu()
    cp1_a3(runs, reqs)
    cp2_b3(runs, reqs)
    cp4_d1e()
    cp5_an_toan(reqs)
