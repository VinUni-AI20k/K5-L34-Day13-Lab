"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import argparse
import math
from pathlib import Path
from statistics import NormalDist

import pandas as pd
import yaml

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ D · Cấu hình pilot ----------
PILOT_CONFIG_PATH = Path(__file__).resolve().parents[1] / 'report' / 'team' / 'pilot_plan.yaml'
PILOT_COST_LABEL = 'Ngưỡng chi phí pilot'
PILOT_COST_RATIONALE = '8.000 đ = 0,67× của 12.000 đ, khoảng 2,3 lần 3.414 đ (A4, chưa cộng cố định) [simulated].'


def co_mau_hai_ty_le(p1, p2, alpha=0.05, power=0.80):
    """Cỡ mẫu mỗi nhánh cho phép thử hai tỷ lệ, làm tròn lên."""
    za = NormalDist().inv_cdf(1 - alpha / 2)
    zb = NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    return math.ceil((za * math.sqrt(2 * pb * (1 - pb))
                      + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2
                     / (p2 - p1) ** 2)


def tai_cau_hinh_pilot(path=PILOT_CONFIG_PATH):
    """Nạp và kiểm tra các tham số D1/D2, reopen rate và luật dừng của pilot."""
    with Path(path).open(encoding='utf-8') as file:
        config = yaml.safe_load(file)
    pilot = config['pilot']
    required = ('scope', 'cost_threshold_vnd', 'cost_rule', 'sample_size', 'reopen_rate',
                'identifiability', 'stop_rules')
    missing = [key for key in required if key not in pilot]
    if missing:
        raise ValueError(f'Thiếu khóa cấu hình pilot: {", ".join(missing)}')
    scope = pilot['scope']
    if not isinstance(scope, dict) or not scope.get('included_request_types') or not scope.get('included_depots'):
        raise ValueError('Phạm vi A3 phải có loại yêu cầu và depot được đưa vào pilot.')
    if not isinstance(pilot['cost_threshold_vnd'], (int, float)) or pilot['cost_threshold_vnd'] <= 0:
        raise ValueError('Ngưỡng chi phí pilot phải là số dương theo đồng/việc thành công.')
    if (pilot['assignment'].get('planned_staff_total', 0)
            < 2 * pilot['sample_size']['staff_per_arm']):
        raise ValueError('Pilot cần đủ nhân viên cho 20 cụm mỗi nhánh.')
    cost_rule = pilot['cost_rule']
    if (cost_rule.get('label') != PILOT_COST_LABEL
            or cost_rule.get('justification') != PILOT_COST_RATIONALE
            or cost_rule.get('first_week_100_review_cps_vnd') != 11743
            or not cost_rule.get('excludes_fixed_costs')):
        raise ValueError('Thiếu cấu hình Ngưỡng chi phí pilot hoặc xử lý tuần xem lại 100%.')
    if pilot['assignment']['unit'] != 'staff' or pilot['primary_metric']['clusters_per_arm'] < 20:
        raise ValueError('Pilot phải phân bổ theo nhân viên với ít nhất 20 cụm mỗi nhánh.')
    if pilot['primary_metric']['n_per_arm'] != pilot['sample_size']['accepted_n_per_arm']:
        raise ValueError('n_per_arm phải khớp cỡ mẫu MDE đã chấp nhận.')
    sample = pilot['sample_size']
    if co_mau_hai_ty_le(0.70, 0.75) != sample['request_randomized_n_per_arm']:
        raise ValueError('Cỡ mẫu D1 cho chia theo yêu cầu không khớp.')
    if co_mau_hai_ty_le(0.70, 0.70 + sample['accepted_mde']) != sample['accepted_n_per_arm']:
        raise ValueError('Cỡ mẫu D1 cho MDE đã chấp nhận không khớp.')
    reopen = pilot['reopen_rate']
    if not 0 < reopen['relative_stop_gap'] < reopen['absolute_stop_ceiling'] < 1:
        raise ValueError('Ngưỡng reopen rate không hợp lệ.')
    if len(pilot['stop_rules']) < 3 or any(not all(word in rule for word in ('NẾU', 'TRONG', 'THÌ', 'KHÔNG THÌ'))
                                           for rule in pilot['stop_rules']):
        raise ValueError('Mỗi luật dừng phải có NẾU – TRONG – THÌ – KHÔNG THÌ.')
    return pilot


def danh_gia_reopen_rate(reqs, pilot):
    """Áp dụng phạm vi và ngưỡng reopen trong config vào dữ liệu baseline."""
    scope = pilot['scope']
    in_scope = (reqs['loai'].isin(scope['included_request_types'])
                & reqs['depot'].isin(scope['included_depots']))
    baseline_scope = reqs.loc[in_scope, 'mo_lai_trong_7_ngay'].mean()
    reopen = pilot['reopen_rate']
    return {
        'baseline_all': reqs['mo_lai_trong_7_ngay'].mean(),
        'baseline_scope': baseline_scope,
        'relative_stop_gap': reopen['relative_stop_gap'],
        'absolute_stop_ceiling': reopen['absolute_stop_ceiling'],
        'reopen_aggregation': reopen['aggregation'],
        'hang_nang_reference_rate': reopen['hang_nang_reference_rate'],
        'cost_threshold_label': pilot['cost_rule']['label'],
        'cost_threshold_justification': pilot['cost_rule']['justification'],
        'cost_threshold_vnd': pilot['cost_threshold_vnd'],
        'cost_excludes_fixed_costs': pilot['cost_rule']['excludes_fixed_costs'],
        'first_week_100_review_cps_vnd': pilot['cost_rule']['first_week_100_review_cps_vnd'],
    }


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    # Lần i chỉ chạy khi i-1 lần trước đều sai: xác suất (1-p)^(i-1).
    # Cộng i = 1..k: 1 + (1-p) + ... + (1-p)^(k-1) = (1 - (1-p)^k) / p.
    if k is None:
        return 1 / p                     # k → ∞ thì (1-p)^k → 0
    return (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    # Chỉ thất bại khi sai cả k lần.
    if k is None:
        return 1.0
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    # = số lần chạy trung bình / tỉ lệ thành công; (1 - (1-p)^k) triệt tiêu nên luôn bằng 1/p.
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
    reqs = reqs.copy()                                   # không sửa DataFrame gốc
    runs = runs[runs['request_id'].isin(reqs['request_id'])]   # A3: chỉ giữ lần chạy của các yêu cầu đang xét

    if max_lan_chay is not None:                         # Nhiệm vụ B1, B3: giới hạn số lần chạy
        runs = runs[runs['attempt'] <= max_lan_chay]     # bỏ các lần chạy vượt giới hạn
        vuot = reqs['so_lan_chay'] > max_lan_chay        # yêu cầu cần nhiều lần hơn giới hạn
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'   # → chuyển nhân viên, không còn là thành công
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    # Tử số: MỌI lần chạy, kể cả lần lỗi (lần lỗi vẫn tốn token và tool). Giá tính cho 1.000 token.
    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai   # simulated
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai   # simulated
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai

    # Mẫu số: chỉ yêu cầu thành công.
    thanh_cong = (reqs['ket_qua'] == 'thanh_cong').sum()

    return dict(
        token=tien_token.sum(),
        tool=tien_tool.sum(),
        chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),   # phần của lần chạy thứ 2, 3
        xem_lai=xem_lai,
        lam_lai=lam_lai,
        tong=tong,
        thanh_cong=thanh_cong,
        cps=tong / thanh_cong,                                          # chi phí mỗi việc thành công
        hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs),  # cách tính sai để so sánh
    )


# ---------- Nhiệm vụ E1 · Chỉ số đợt chạy thử ----------
def tinh_chi_so(reqs):
    """Trả về tử số và mẫu số của từng chỉ số, mỗi dòng CSV là một yêu cầu."""
    da_xem_lai = reqs.loc[reqs['duoc_xem_lai'].eq(1)]
    mo_lai = reqs['mo_lai_trong_7_ngay'].eq(1)
    dong_dat = reqs['dong_trong_24h'].eq(1) & reqs['mo_lai_trong_7_ngay'].eq(0)
    bo_qua = da_xem_lai['quyet_dinh_xem_lai'].isin(['sua', 'bo'])
    return {
        'Đóng trong 24 giờ, không mở lại trong 7 ngày': (dong_dat.sum(), len(reqs)),
        'Bỏ qua gợi ý': (bo_qua.sum(), len(da_xem_lai)),
        'Mở lại trong 7 ngày': (mo_lai.sum(), len(reqs)),
    }


def in_chi_so(reqs):
    print('E1 · Chỉ số trong đợt chạy thử')
    for ten, (tu_so, mau_so) in tinh_chi_so(reqs).items():
        ty_le = f'{tu_so / mau_so:.2%}' if mau_so else 'không xác định'
        print(f'{ten}: {tu_so}/{mau_so} ({ty_le})')


def in_rui_ro_kinh_te(runs, reqs):
    """Đối chiếu riêng hai dòng E2; không thay thế bảng B1 của nhóm."""
    # Dùng chung mô hình A/B sau khi merge phần Cường để tránh lệch công thức.
    if not reqs['ket_qua'].eq('thanh_cong').any():
        print('E2 · Không xác định chi phí mỗi việc vì không có việc thành công')
        return
    goc = mo_hinh(runs, reqs)
    token, tool = goc['token'], goc['tool']
    xem_lai, lam_lai = goc['xem_lai'], goc['lam_lai']
    tong, thanh_cong = goc['tong'], goc['thanh_cong']
    print('E2 · Toàn bộ mẫu B1, chi phí simulated; dùng chung mo_hinh của A/B')
    print(f'Token: {token:.3f}; tool: {tool:.3f}')
    print(f'Xem lại: {xem_lai:.3f}; làm lại: {lam_lai:.3f}')
    print(f'Tổng gốc: {tong:.3f}; số việc thành công: {thanh_cong}')
    if not thanh_cong or not tong:
        print('Không xác định chi phí mỗi việc hoặc mức thay đổi do mẫu số bằng 0')
        return
    print(f'Chi phí gốc: {tong / thanh_cong:.2f} đ/việc (simulated)')
    for ten, tang_them in [('Làm lại gấp đôi', lam_lai), ('Xem lại gấp đôi', xem_lai)]:
        print(f'{ten}: {(tong + tang_them) / thanh_cong:.2f} đ/việc; '
              f'+{tang_them / tong:.2%} (simulated)')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--chi-so', action='store_true', help='Chỉ tính ba chỉ số E1')
    parser.add_argument('--rui-ro', action='store_true', help='Đối chiếu hai dòng E2 với mô hình A/B')
    args = parser.parse_args()
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    if args.chi_so or args.rui_ro:
        if args.chi_so:
            in_chi_so(reqs)
        if args.rui_ro:
            in_rui_ro_kinh_te(pd.read_csv('logix_runs.csv'), reqs)
        raise SystemExit(0)

    runs = pd.read_csv('logix_runs.csv')
    pilot = tai_cau_hinh_pilot()
    print('Pilot D · reopen/cost:', danh_gia_reopen_rate(reqs, pilot))
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    print('\n== A2 · Mô hình chi phí (xem_lai, lam_lai, tong, cps là simulated) ==')
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:15s} {gia_tri:>14,.1f}')
    print(f"cps gấp {ket_qua['cps'] / ket_qua['hoa_don_moi_yc']:.1f} lần hoá đơn chia số yêu cầu")
    for khoan in ['token', 'tool', 'xem_lai', 'lam_lai']:
        print(f"  tỉ trọng {khoan:8s} {ket_qua[khoan] / ket_qua['tong'] * 100:5.1f}%")
    # ---------- A3 · Tách theo loại yêu cầu ----------
    print('\n== A3 · Theo loại yêu cầu (cps là simulated) ==')
    print(f"{'loai':10s} {'so_yc':>6s} {'ti_le_tc':>9s} {'lan_chay/yc':>12s} {'cps':>9s} {'so_12000':>9s}")
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        r = reqs[reqs['loai'] == loai]
        kq = mo_hinh(runs, r)                            # mo_hinh tự lọc runs theo request_id
        so_lan_chay = runs['request_id'].isin(r['request_id']).sum() / len(r)
        print(f"{loai:10s} {len(r):6d} {kq['thanh_cong'] / len(r) * 100:8.1f}% "
              f"{so_lan_chay:12.2f} {kq['cps']:9,.0f} {kq['cps'] / BASELINE:8.2f}x")

    # Chạy lại có giúp không: tỉ lệ lần chạy status == 'ok' theo loại và theo lần thử (attempt).
    print('\nTỉ lệ ok theo lần thử (%):')
    ok_theo_lan = (runs.merge(reqs[['request_id', 'loai']], on='request_id')
                   .assign(ok=lambda d: d['status'] == 'ok')
                   .pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean'))
    print((ok_theo_lan * 100).round(1))

    # ---------- A4 · Chi phí cố định cho phạm vi pilot noi_dia + hang_nang ----------
    CO_DINH_THANG = 40_000_000       # đồng / tháng
    YC_THANG = 45_000                # yêu cầu hoàn phí / tháng ở quy mô đầy đủ (mọi loại)
    scope = pilot['scope']
    pham_vi = reqs[reqs['loai'].isin(scope['included_request_types'])
                    & reqs['depot'].isin(scope['included_depots'])]
    kq_pv = mo_hinh(runs, pham_vi)
    # Việc thành công trong phạm vi tính trên toàn bộ 1.200 yêu cầu của mẫu, rồi nhân lên 45.000 / tháng.
    tc_tren_tong = kq_pv['thanh_cong'] / len(reqs)
    print(f"\n== A4 · Chi phí cố định, phạm vi noi_dia + hang_nang (simulated) ==")
    print(f"Phạm vi: {len(pham_vi)} yêu cầu, {kq_pv['thanh_cong']} thành công; "
          f"tổng {kq_pv['tong']:,.0f} đ → cps chưa cố định {kq_pv['cps']:,.0f} đ")
    for ten, he_so in [('45.000 yc/tháng', 1.0), ('Một nửa khối lượng', 0.5)]:
        tc_thang = YC_THANG * he_so * tc_tren_tong
        co_dinh_moi_viec = CO_DINH_THANG / tc_thang
        cps_co_dinh = kq_pv['cps'] + co_dinh_moi_viec
        print(f"{ten:20s} tc/tháng {tc_thang:8,.0f}  cố định/việc {co_dinh_moi_viec:6,.0f} đ  "
              f"cps + cố định {cps_co_dinh:6,.0f} đ = {cps_co_dinh / BASELINE:.2f}x")
    # ---------- B1 · Bảng độ nhạy: đổi từng yếu tố, các yếu tố khác giữ như A2 ----------
    kich_ban = {
        'Giá token gấp đôi':          dict(gia_vao=52, gia_ra=260),   # giá tool giữ nguyên
        'Giá token giảm một nửa':     dict(gia_vao=13, gia_ra=65),
        'Tỉ lệ xem lại gấp đôi':      dict(he_so_xem_lai=2),
        'Tỉ lệ xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
        'Số ca làm lại gấp đôi':      dict(he_so_lam_lai=2),
        'Số ca làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
        'Lương nhân viên tăng 25%':   dict(luong_phut=2500),
        'Chỉ cho chạy tối đa 2 lần':  dict(max_lan_chay=2),
        'Chỉ cho chạy 1 lần':         dict(max_lan_chay=1),
    }
    goc = mo_hinh(runs, reqs)['cps']
    print('\n== B1 · Độ nhạy của chi phí mỗi việc thành công (simulated) ==')
    print(f"{'Gốc (A2)':28s} {goc:8,.0f}")
    for ten, tham_so in kich_ban.items():
        cps = mo_hinh(runs, reqs, **tham_so)['cps']
        print(f'{ten:28s} {cps:8,.0f} {(cps / goc - 1) * 100:+6.1f}%')

    # ---------- B2 · Đổi một cặp yếu tố cùng lúc, rồi xếp hạng ----------
    cps_cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    tong_rieng = sum(mo_hinh(runs, reqs, **kich_ban[k])['cps'] / goc - 1
                     for k in ['Giá token gấp đôi', 'Tỉ lệ xem lại gấp đôi'])
    print('\n== B2 · Giá token gấp đôi + xem lại gấp đôi (simulated) ==')
    print(f'Cặp: {cps_cap:,.0f} đ ({(cps_cap / goc - 1) * 100:+.1f}%); '
          f'tổng hai tác động riêng: {tong_rieng * 100:+.1f}% → bằng nhau vì mô hình cộng tuyến tính')

    # Xếp hạng theo mức thay đổi khi yếu tố tăng (gấp đôi, hoặc +25% với lương).
    tang = {'Số ca làm lại': 'Số ca làm lại gấp đôi', 'Tỉ lệ xem lại': 'Tỉ lệ xem lại gấp đôi',
            'Lương nhân viên': 'Lương nhân viên tăng 25%', 'Giá token': 'Giá token gấp đôi'}
    muc_tang = {yt: mo_hinh(runs, reqs, **kich_ban[kb])['cps'] / goc - 1 for yt, kb in tang.items()}
    print('Xếp hạng:', ' · '.join(f'{i}. {yt} ({v * 100:+.1f}%)' for i, (yt, v)
                                  in enumerate(sorted(muc_tang.items(), key=lambda x: -x[1]), 1)))

    # ---------- B3 · Giới hạn chạy lại: chi phí cho công ty, không chỉ cho trợ lý ----------
    # Chi phí cả hệ thống = tổng chi phí trợ lý + 12.000 đ × số yêu cầu không thành công (nhân viên làm thay).
    print('\n== B3 · Giới hạn số lần chạy (simulated) ==')
    print(f"{'gioi_han':>8s} {'tong_tro_ly':>12s} {'khong_tc':>9s} {'ca_he_thong':>12s} {'cps':>7s}")
    he_thong = {}
    for k in [1, 2, 3]:
        kq = mo_hinh(runs, reqs, max_lan_chay=k)
        khong_tc = len(reqs) - kq['thanh_cong']
        he_thong[k] = kq['tong'] + BASELINE * khong_tc
        print(f"{k:8d} {kq['tong']:12,.0f} {khong_tc:9d} {he_thong[k]:12,.0f} {kq['cps']:7,.0f}")
    print(f'Rẻ nhất cho công ty: tối đa {min(he_thong, key=he_thong.get)} lần chạy')

    # ---------- B4 · Xem lại 100% trong phạm vi noi_dia + hang_nang ----------
    # Giả định đề: mỗi yêu cầu có ít nhất một lần chạy ok được xem lại 5 phút; mỗi ca lam_lai làm lại 9 phút.
    PHUT_XEM, PHUT_LAM = 5, 9
    runs_pv = runs[runs['request_id'].isin(pham_vi['request_id'])]
    so_xem = runs_pv.loc[runs_pv['status'] == 'ok', 'request_id'].nunique()
    so_lam_lai = (pham_vi['ket_qua'] == 'lam_lai').sum()
    token_tool = kq_pv['token'] + kq_pv['tool']                  # mọi lần chạy của 982 yêu cầu
    tc_pv = kq_pv['thanh_cong']

    def cps_xem_100(phut_lam):
        tong = token_tool + so_xem * PHUT_XEM * LUONG_PHUT + so_lam_lai * phut_lam * LUONG_PHUT
        return tong, tong / tc_pv

    def phut_xem_hoa_von(phut_lam):
        # Số phút xem lại tối đa mỗi yêu cầu để cps vẫn ≤ 12.000 đ.
        return (BASELINE * tc_pv - token_tool - so_lam_lai * phut_lam * LUONG_PHUT) / (so_xem * LUONG_PHUT)

    phut_lam_du_lieu = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean()
    print('\n== B4 · Xem lại 100%, phạm vi noi_dia + hang_nang (simulated) ==')
    print(f'{so_xem} yêu cầu được xem lại × {PHUT_XEM} phút; {so_lam_lai} ca lam_lai; '
          f'token + tool {token_tool:,.0f} đ; {tc_pv} việc thành công')
    for nhan, phut_lam in [(f'làm lại {PHUT_LAM} phút (đề)', PHUT_LAM),
                           (f'làm lại {phut_lam_du_lieu:.1f} phút (trung bình dữ liệu)', phut_lam_du_lieu)]:
        tong, cps = cps_xem_100(phut_lam)
        print(f'{nhan:38s} tổng {tong:12,.0f} đ  cps {cps:7,.0f} đ = {cps / BASELINE:.2f}x  '
              f'hoà vốn khi xem lại ≤ {phut_xem_hoa_von(phut_lam):.1f} phút')
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
    in_chi_so(reqs)
