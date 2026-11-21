"""TV3: tinh D1 va baseline an toan; chay: python src/tv3_pilot_checks.py."""
import csv
import math
from pathlib import Path
from statistics import NormalDist


def co_mau(p1, p2, alpha=0.05, power=0.8):
    z = NormalDist()
    pb = (p1 + p2) / 2
    return math.ceil((z.inv_cdf(1-alpha/2)*math.sqrt(2*pb*(1-pb))
                      + z.inv_cdf(power)*math.sqrt(p1*(1-p1)+p2*(1-p2)))**2/(p2-p1)**2)


if __name__ == '__main__':
    n5 = co_mau(.70, .75)
    n6 = co_mau(.70, .76)
    de75 = 1 + 74*.02
    minimum_m = math.ceil(n6*(1-.02)/(20-n6*.02))
    print(f'D1a: {n5} yeu cau/nhom')
    print(f'D1b: DE={de75:.2f}; n={math.ceil(n5*de75)}; '
          f'{math.ceil(n5*de75/75)} nhan vien/nhom')
    print(f'D1c: gioi han hieu dung < {20/.02:.0f}/nhom; khong du cho +5 diem')
    print(f'D1d: gioi han hieu dung < {6/.02:.0f}/nhom')
    print(f'D1e: n={n6}/nhom; m>={minimum_m}; '
          f'DE={1+(minimum_m-1)*.02:.2f}; '
          f'n_hieu_dung={20*minimum_m/(1+(minimum_m-1)*.02):.2f}')
    path = Path(__file__).resolve().parent / 'logix_requests.csv'
    with path.open(encoding='utf-8-sig', newline='') as stream:
        rows = list(csv.DictReader(stream))
    for name, subset in [('toan_mau', rows), ('noi_dia+hang_nang',
            [r for r in rows if r['loai'] in ('noi_dia', 'hang_nang')])]:
        count = sum(int(r['mo_lai_trong_7_ngay']) for r in subset)
        print(f'Baseline mo lai {name}: {count}/{len(subset)} = {count/len(subset):.4%}')
