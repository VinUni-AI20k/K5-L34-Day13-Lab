"""Lab 13 · TV3 (Phúc) · Sinh trang UI báo cáo hồ sơ launch v0 cho buổi duyệt Gate 2a.
Chạy trong thư mục src/: python tv3_bao_cao_ui.py
Ghi ra ../report/team/tv3_bao_cao_ui.html (một file, mở offline bằng trình duyệt).

Mọi số tính lại từ hai file CSV bằng mo_hinh() trong lab13.py (TV1) và co_mau() trong tv4_tinh_so.py (TV4).
Phần chữ (luật dừng, bảng lỗi, event, rủi ro, hồ sơ) đọc thẳng từ các file trong report/team/,
nên khi nhóm sửa hồ sơ chỉ cần chạy lại script. Không sửa file nào của người khác.
Script tự đối chiếu số với bang_chi_phi.md / ho_so_launch_v0.md; lệch quá 2% thì dừng.
"""
import json
import math
import re
import subprocess
from pathlib import Path

import pandas as pd
import yaml
from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize

from lab13 import (BASELINE, GIA_RA, GIA_TOOL, GIA_VAO, LUONG_PHUT,
                   he_so_chi_phi_moi_viec_thanh_cong, mo_hinh,
                   so_lan_chay_ky_vong)
from tv4_tinh_so import CO_DINH_THANG, ICC, YC_THANG, co_mau

SRC = Path(__file__).resolve().parent
TEAM = SRC.parent / 'report' / 'team'
TEMPLATE = SRC / 'tv3_bao_cao_ui_template.html'
OUT = TEAM / 'tv3_bao_cao_ui.html'
PHAM_VI = ['noi_dia', 'hang_nang']
LOAI = ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']


# ---------- Đọc bảng markdown trong hồ sơ ----------
def bang_md(path, sau_tieu_de):
    """Trả về list các hàng (list ô) của bảng đầu tiên nằm sau dòng tiêu đề chứa `sau_tieu_de`."""
    dong = Path(path).read_text(encoding='utf-8').splitlines()
    i = next(k for k, s in enumerate(dong) if sau_tieu_de in s)
    while not dong[i].lstrip().startswith('|'):
        i += 1
    hang = []
    while i < len(dong) and dong[i].lstrip().startswith('|'):
        o = [c.strip() for c in dong[i].strip().strip('|').split('|')]
        if not all(re.fullmatch(r':?-+:?', c) for c in o):
            hang.append(o)
        i += 1
    return hang


def tach_luat(luat):
    """Tách một luật dừng thành bốn vế NẾU – TRONG – THÌ – KHÔNG THÌ."""
    m = re.match(r'NẾU (.+?) TRONG (.+?) THÌ (.+) KHÔNG THÌ (.+)$', luat)
    assert m, f'Luật dừng thiếu vế: {luat[:60]}'
    return dict(neu=m[1], trong=m[2], thi=m[3], khong_thi=m[4])


# ---------- Thành phần chi phí cho thanh trượt độ nhạy ----------
def thanh_phan(runs, reqs, k):
    """Các đại lượng thô để trang tính lại CPS với bất kỳ giá/hệ số nào (mô hình tuyến tính).
    Cùng logic với mo_hinh(max_lan_chay=k); kiểm tra lại bằng assert bên dưới."""
    reqs = reqs.copy()
    r = runs[runs['request_id'].isin(reqs['request_id']) & (runs['attempt'] <= k)]
    vuot = reqs['so_lan_chay'] > k
    reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
    reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0
    return dict(tin=int(r['tokens_in'].sum()), tout=int(r['tokens_out'].sum()),
                tool=int(r['tool_calls'].sum()),
                px=float(reqs['phut_xem_lai_simulated'].sum()),
                pl=float(reqs['phut_lam_lai_simulated'].sum()),
                tc=int((reqs['ket_qua'] == 'thanh_cong').sum()), n=len(reqs))


def cps_tu_thanh_phan(t):
    return (t['tin'] / 1000 * GIA_VAO + t['tout'] / 1000 * GIA_RA + t['tool'] * GIA_TOOL
            + (t['px'] + t['pl']) * LUONG_PHUT) / t['tc']


def main():
    runs = pd.read_csv(SRC / 'logix_runs.csv')
    reqs = pd.read_csv(SRC / 'logix_requests.csv', keep_default_na=False)
    pv = reqs[reqs['loai'].isin(PHAM_VI)]

    # A1
    a1 = [dict(ten='Số lần chạy trung bình, tối đa 2 lần', gia_tri=so_lan_chay_ky_vong(0.8, 2), dich=1.20),
          dict(ten='Số lần chạy trung bình, chạy đến khi đúng', gia_tri=so_lan_chay_ky_vong(0.8), dich=1.25),
          dict(ten='Hệ số chi phí mỗi việc thành công, tối đa 3 lần',
               gia_tri=he_so_chi_phi_moi_viec_thanh_cong(0.8, 3), dich=1.25)]
    for t in a1:
        assert abs(t['gia_tri'] - t['dich']) < 1e-9, t

    # A2
    g = mo_hinh(runs, reqs)
    a2 = {k: float(v) for k, v in g.items()}
    a2.update(phut_xem=float(reqs['phut_xem_lai_simulated'].sum()),
              phut_lam=float(reqs['phut_lam_lai_simulated'].sum()),
              tool_calls=int(runs['tool_calls'].sum()), so_run=len(runs), so_yc=len(reqs),
              boi_so_hoa_don=float(g['cps'] / g['hoa_don_moi_yc']))

    # Thành phần cho thanh trượt: phạm vi × giới hạn chạy
    tp = {}
    for ten, df in [('toan_mau', reqs), ('pham_vi', pv)]:
        tp[ten] = {}
        for k in (1, 2, 3):
            t = thanh_phan(runs, df, k)
            assert abs(cps_tu_thanh_phan(t) - mo_hinh(runs, df, max_lan_chay=k)['cps']) < 1e-6
            tp[ten][str(k)] = t

    # A3 + tỉ lệ ok theo lần thử
    a3 = []
    for loai in LOAI:
        df = reqs[reqs['loai'] == loai]
        m = mo_hinh(runs, df)
        r = runs[runs['request_id'].isin(df['request_id'])]
        ok = r.groupby('attempt')['status'].apply(lambda s: [int((s == 'ok').sum()), len(s)])
        a3.append(dict(loai=loai, n=len(df), tc=int(m['thanh_cong']), cps=float(m['cps']),
                       lan_chay=float(df['so_lan_chay'].mean()), ok_theo_lan=[ok.get(i, [0, 0]) for i in (1, 2, 3)],
                       mo_lai=float(df['mo_lai_trong_7_ngay'].mean())))

    # A4
    m_pv = mo_hinh(runs, pv)
    ti_le_tc = m_pv['thanh_cong'] / len(reqs)
    a4 = []
    for yc in (YC_THANG, YC_THANG / 2):
        co_dinh = CO_DINH_THANG / (yc * ti_le_tc)
        a4.append(dict(yc_thang=yc, tc_thang=yc * ti_le_tc, co_dinh=co_dinh, cps=float(m_pv['cps'] + co_dinh)))
    hoa_von = CO_DINH_THANG / ((BASELINE - m_pv['cps']) * ti_le_tc)

    # B1, B2
    kb = [('Giá token gấp đôi', 'token', dict(gia_vao=52, gia_ra=260)),
          ('Giá token giảm một nửa', 'token', dict(gia_vao=13, gia_ra=65)),
          ('Tỉ lệ xem lại gấp đôi', 'xem', dict(he_so_xem_lai=2)),
          ('Tỉ lệ xem lại giảm một nửa', 'xem', dict(he_so_xem_lai=0.5)),
          ('Số ca làm lại gấp đôi', 'lam', dict(he_so_lam_lai=2)),
          ('Số ca làm lại giảm một nửa', 'lam', dict(he_so_lam_lai=0.5)),
          ('Lương nhân viên tăng 25%', 'luong', dict(luong_phut=2500)),
          ('Tối đa 2 lần chạy', 'gioi_han', dict(max_lan_chay=2)),
          ('Tối đa 1 lần chạy', 'gioi_han', dict(max_lan_chay=1))]
    b1 = []
    for ten, nhom, ts in kb:
        c = mo_hinh(runs, reqs, **ts)['cps']
        b1.append(dict(ten=ten, nhom=nhom, cps=float(c), pct=float(c / g['cps'] - 1)))
    cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    b2 = dict(cps=float(cap), pct=float(cap / g['cps'] - 1))

    # B3
    b3 = []
    for k in (1, 2, 3):
        m = mo_hinh(runs, reqs, max_lan_chay=k)
        khong = len(reqs) - int(m['thanh_cong'])
        b3.append(dict(k=k, tong=float(m['tong']), khong_tc=khong,
                       he_thong=float(m['tong'] + khong * BASELINE), cps=float(m['cps'])))

    # B4
    r_pv = runs[runs['request_id'].isin(pv['request_id'])]
    so_xem = int(r_pv.loc[r_pv['status'] == 'ok', 'request_id'].nunique())
    so_lam = int((pv['ket_qua'] == 'lam_lai').sum())
    tt = float(m_pv['token'] + m_pv['tool'])
    phut_tb = round(float(reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean()), 1)
    b4 = dict(so_xem=so_xem, so_lam=so_lam, token_tool=tt, tc=int(m_pv['thanh_cong']), n=len(pv), kich_ban=[])
    for nhan, phut in [('9 phút theo giả định của đề', 9), (f'{phut_tb:.1f} phút theo trung bình mẫu'.replace('.', ','), phut_tb)]:
        tien_ll = so_lam * phut * LUONG_PHUT
        tong = tt + so_xem * 5 * LUONG_PHUT + tien_ll
        b4['kich_ban'].append(dict(nhan=nhan, phut_lam=phut, cps=tong / m_pv['thanh_cong'],
                                   hoa_von=(BASELINE * m_pv['thanh_cong'] - tt - tien_ll) / (so_xem * LUONG_PHUT)))

    # D1
    n5, n6 = co_mau(0.70, 0.75), co_mau(0.70, 0.76)
    de75 = 1 + 74 * ICC
    m_min = math.ceil(n6 * (1 - ICC) / (20 - n6 * ICC))
    pw5 = NormalIndPower().power(effect_size=proportion_effectsize(0.75, 0.70), nobs1=n6, alpha=0.05)
    d1 = dict(n5=n5, n6=n6, de75=de75, n_b=math.ceil(n5 * de75), nv_b=math.ceil(math.ceil(n5 * de75) / 75),
              tran_nv=20 / ICC, tran_depot=6 / ICC, m_min=m_min, de_e=1 + (m_min - 1) * ICC, power5=float(pw5),
              icc=ICC, yc_ngay_pv=1500 * len(pv) / len(reqs))

    # E1
    def chi_so(df):
        xem = df[df['duoc_xem_lai'] == 1]
        return dict(n=len(df),
                    chinh=int(((df['dong_trong_24h'] == 1) & (df['mo_lai_trong_7_ngay'] == 0)).sum()),
                    xem=len(xem), bo_qua=int(xem['quyet_dinh_xem_lai'].isin(['sua', 'bo']).sum()),
                    mo_lai=int(df['mo_lai_trong_7_ngay'].sum()),
                    lam_lai=int((df['ket_qua'] == 'lam_lai').sum()))
    e1 = dict(toan_mau=chi_so(reqs), pham_vi=chi_so(pv))

    # Phần chữ từ hồ sơ
    plan = yaml.safe_load((TEAM / 'pilot_plan.yaml').read_text(encoding='utf-8'))['pilot']
    plan['stop_rules_tach'] = [tach_luat(s) for s in plan['stop_rules']]
    nhan = bang_md(TEAM / 'bang_loi.md', '## Hai bộ nhãn độc lập')[1:]
    khac_phuc = bang_md(TEAM / 'bang_loi.md', '## Bảng khắc phục')[1:]
    su_kien = bang_md(TEAM / 'chi_so.md', '## Danh sách event')[1:]
    rui_ro = bang_md(TEAM / 'chi_so.md', '## E2')[1:]
    ho_so = bang_md(TEAM / 'ho_so_launch_v0.md', '| Mục |')[1:]
    dieu_kien = bang_md(TEAM / 'ho_so_launch_v0.md', '**Đề xuất:**')[1:]
    de_xuat = next(s for s in (TEAM / 'ho_so_launch_v0.md').read_text(encoding='utf-8').splitlines()
                   if s.startswith('**Đề xuất:**')).replace('**Đề xuất:**', '').strip()
    assert len(nhan) == 20 and len(ho_so) == 7 and len(plan['stop_rules']) >= 3

    # Đối chiếu với số đã nộp trong hồ sơ (lệch ≤ 2%)
    da_nop = {'CPS A2': (g['cps'], 4472), 'Bội số hoá đơn': (a2['boi_so_hoa_don'], 16.3),
              'CPS phạm vi': (m_pv['cps'], 3414), 'A4 45.000': (a4[0]['cps'], 4599),
              'A4 22.500': (a4[1]['cps'], 5784), 'Hoà vốn': (hoa_von, 6212),
              'B2': (cap, 6543), 'B3 2 lần': (b3[1]['he_thong'], 6901220),
              'B4 9 phút': (b4['kich_ban'][0]['cps'], 11743), 'D1 n6': (n6, 859), 'D1 m': (m_min, 299),
              'Power 5 điểm': (pw5, 0.64), 'Chính': (e1['toan_mau']['chinh'] / 1200, 0.8283),
              'quoc_te': (a3[2]['cps'], 22515)}
    for ten, (tinh, nop) in da_nop.items():
        assert abs(tinh / nop - 1) <= 0.02, f'{ten}: tính {tinh} khác hồ sơ {nop}'

    try:
        commit = subprocess.run(['git', 'rev-parse', '--short', 'HEAD'], cwd=SRC,
                                capture_output=True, text=True).stdout.strip()
    except OSError:
        commit = ''

    data = dict(
        gia=dict(vao=GIA_VAO, ra=GIA_RA, tool=GIA_TOOL, luong=LUONG_PHUT, baseline=BASELINE,
                 co_dinh=CO_DINH_THANG, yc_thang=YC_THANG),
        a1=a1, a2=a2, tp=tp, a3=a3, a4=a4, hoa_von=hoa_von, b1=b1, b2=b2, b3=b3, b4=b4, d1=d1, e1=e1,
        plan=plan, nhan=nhan, khac_phuc=khac_phuc, su_kien=su_kien, rui_ro=rui_ro,
        ho_so=ho_so, dieu_kien=dieu_kien, de_xuat=de_xuat, commit=commit)

    js = json.dumps(data, ensure_ascii=False).replace('</', '<\\/')
    html = TEMPLATE.read_text(encoding='utf-8').replace('/*__DATA__*/null', js)
    OUT.write_text(html, encoding='utf-8')
    print(f'Đối chiếu {len(da_nop)} số với hồ sơ: ĐẠT (lệch ≤ 2%)')
    print(f'Đã ghi {OUT.relative_to(SRC.parent)} ({OUT.stat().st_size / 1024:.0f} KB)')


if __name__ == '__main__':
    main()
