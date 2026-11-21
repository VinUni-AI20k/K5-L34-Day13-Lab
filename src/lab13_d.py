"""Bàn giao Người 1. Import in_d1 rồi gọi in_d1(reqs) sau phần B (hoặc chạy trực tiếp trong src/)."""
import math
from statistics import NormalDist


def co_mau(p1, p2, alpha=0.05, power=0.80):
    """Cỡ mẫu mỗi nhóm khi so hai tỉ lệ p1, p2 (hai phía)."""
    za = NormalDist().inv_cdf(1 - alpha / 2)
    zb = NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    return math.ceil(
        (za * math.sqrt(2 * pb * (1 - pb)) + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2
        / (p2 - p1) ** 2
    )


def in_d1(reqs=None):
    """In kết quả 5 câu D1 (cỡ mẫu pilot) và tỉ lệ mở lại nền để đặt ngưỡng an toàn."""
    icc = 0.02
    n_5 = co_mau(0.70, 0.75)
    de_b = 1 + (75 - 1) * icc
    n_b = math.ceil(n_5 * de_b)
    n_6 = co_mau(0.70, 0.76)
    m_e = math.ceil((n_6 * (1 - icc)) / (20 - n_6 * icc))
    de_e = 1 + (m_e - 1) * icc

    pb5 = (0.70 + 0.75) / 2
    zb_actual = (0.05 * math.sqrt(n_6) - NormalDist().inv_cdf(0.975) * math.sqrt(2 * pb5 * (1 - pb5))) / math.sqrt(
        0.70 * 0.30 + 0.75 * 0.25
    )
    power_5_at_n6 = NormalDist().cdf(zb_actual)

    print('\nD1 · Cỡ mẫu pilot (baseline 0,70; alpha 0,05; power 0,80; ICC 0,02)')
    print(f'  a) Chia theo yêu cầu (+5 điểm): {n_5:,} yêu cầu mỗi nhóm')
    print(f'  b) Theo nhân viên (m=75, DE={de_b:.2f}): {n_b:,} mỗi nhóm -> {math.ceil(n_b / 75)} người/nhóm (tổng > 40)')
    print(f'  c) 20 nhân viên mỗi nhóm: tối đa {20 / icc:,.0f} yêu cầu hiệu dụng/nhóm (< {n_5:,})')
    print(f'  d) 6 depot mỗi nhóm: tối đa {6 / icc:,.0f} yêu cầu hiệu dụng/nhóm (< {n_5:,})')
    print(f'  e) Mức chênh 6 điểm ({n_6}/nhóm), 20 nhân viên/nhóm: m >= {m_e}, DE={de_e:.2f}, power ở +5 điểm={power_5_at_n6:.4f}')

    if reqs is not None:
        mo_lai_all = reqs['mo_lai_trong_7_ngay'].mean()
        nd_hn = reqs[reqs['loai'].isin(('noi_dia', 'hang_nang'))]
        mo_lai_scope = nd_hn['mo_lai_trong_7_ngay'].mean()
        print(f'  Nền mở lại 7 ngày: toàn mẫu {mo_lai_all:.2%}, noi_dia + hang_nang {mo_lai_scope:.2%}')


if __name__ == '__main__':
    import pandas as pd

    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    in_d1(reqs)
