"""Tính cỡ mẫu và đối chiếu tỉ lệ mở lại của CP4."""

import csv
import math
from pathlib import Path
from statistics import NormalDist

PHAM_VI_PILOT = {'noi_dia', 'hang_nang'}


def co_mau_moi_nhom(baseline, target, alpha, power):
    """Cỡ mẫu độc lập tối thiểu mỗi nhóm để so hai tỉ lệ (kiểm định hai phía)."""
    normal = NormalDist()
    z_alpha = normal.inv_cdf(1 - alpha / 2)
    z_power = normal.inv_cdf(power)
    trung_binh = (baseline + target) / 2
    phuong_sai_gop = 2 * trung_binh * (1 - trung_binh)
    phuong_sai_rieng = baseline * (1 - baseline) + target * (1 - target)
    sai_so = z_alpha * math.sqrt(phuong_sai_gop) + z_power * math.sqrt(phuong_sai_rieng)
    return math.ceil((sai_so / (target - baseline)) ** 2)


def he_so_thiet_ke(m, icc):
    return 1 + (m - 1) * icc


def power_hai_phia(p1, p2, n_moi_nhom, alpha):
    """Xấp xỉ chuẩn hai phía với cỡ hiệu ứng Cohen h và hai nhóm bằng nhau."""
    normal = NormalDist()
    h = 2 * (math.asin(math.sqrt(p2)) - math.asin(math.sqrt(p1)))
    trung_binh = abs(h) * math.sqrt(n_moi_nhom / 2)
    nguong = normal.inv_cdf(1 - alpha / 2)
    return normal.cdf(trung_binh - nguong) + normal.cdf(-trung_binh - nguong)


def doc_yeu_cau():
    """Đọc cùng CSV với lệnh chính, không cần pandas khi kiểm riêng CP4."""
    duong_dan = Path(__file__).with_name('logix_requests.csv')
    with duong_dan.open(encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))


def in_ket_qua_cp4(reqs):
    baseline, alpha, power, icc = 0.70, 0.05, 0.80, 0.02
    nhan_vien, depot = 20, 6  # số cụm mỗi nhóm khi chia đôi
    n_5 = co_mau_moi_nhom(baseline, 0.75, alpha, power)
    n_6 = co_mau_moi_nhom(baseline, 0.76, alpha, power)

    de_75 = he_so_thiet_ke(75, icc)
    n_theo_nhan_vien = math.ceil(n_5 * de_75)
    cum_can = math.ceil(n_theo_nhan_vien / 75)
    # Giải c*m / (1 + (m - 1)*ICC) >= n_6 với c = 20 và c > n_6*ICC.
    m_toi_thieu = math.ceil(n_6 * (1 - icc) / (nhan_vien - n_6 * icc))
    de = he_so_thiet_ke(m_toi_thieu, icc)
    n_hieu_dung = nhan_vien * m_toi_thieu / de
    power_5 = power_hai_phia(baseline, 0.75, n_6, alpha)

    print(f'D1a · Chia theo yêu cầu: {n_5} yêu cầu mỗi nhóm để đo +5 điểm %')
    print(f'D1b · m=75: DE={de_75:.2f}, {n_theo_nhan_vien} yêu cầu, {cum_can} người mỗi nhóm')
    print(f'D1c · 20 nhân viên mỗi nhóm: cỡ mẫu hiệu dụng < {nhan_vien / icc:.0f}')
    print(f'D1d · 6 depot mỗi nhóm: cỡ mẫu hiệu dụng < {depot / icc:.0f}')
    print(f'D1e · +6 điểm %: cần {n_6} hiệu dụng mỗi nhóm, m tối thiểu {m_toi_thieu}')
    print(f'      DE={de:.2f}, {nhan_vien * m_toi_thieu} thực tế và {n_hieu_dung:.2f} hiệu dụng mỗi nhóm')
    print(f'      Power ở +5 điểm % với {n_6} hiệu dụng mỗi nhóm: {power_5:.3f}')

    pham_vi = [row for row in reqs if row['loai'] in PHAM_VI_PILOT]
    for nhom, du_lieu in [('Toàn mẫu', reqs), ('Phạm vi pilot', pham_vi)]:
        mo_lai = sum(int(row['mo_lai_trong_7_ngay']) == 1 for row in du_lieu)
        print(f'{nhom} · Mở lại 7 ngày: {mo_lai}/{len(du_lieu)} ({mo_lai / len(du_lieu):.2%})')


if __name__ == '__main__':
    in_ket_qua_cp4(doc_yeu_cau())
