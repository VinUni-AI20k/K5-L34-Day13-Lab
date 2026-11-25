"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. CP1–CP2 và CP4 đã hoàn thiện. Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import sys
from statistics import NormalDist
import pandas as pd
from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def kiem_tra_tham_so(p, k):
    if not 0 < p <= 1:
        raise ValueError('p phải thuộc (0, 1].')
    if k is not None and (isinstance(k, bool) or not isinstance(k, int) or k < 1):
        raise ValueError('k phải là số nguyên dương hoặc None.')


def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    kiem_tra_tham_so(p, k)
    return 1 / p if k is None else (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    kiem_tra_tham_so(p, k)
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
# CP2 dùng lại mô hình với tham số giá, hệ số hoặc giới hạn khác.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy(deep=True)
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        kiem_tra_tham_so(1, max_lan_chay)
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0
    token = (runs['tokens_in'] * gia_vao + runs['tokens_out'] * gia_ra) / 1000
    tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = token.sum() + tool.sum() + xem_lai + lam_lai
    thanh_cong = int(reqs['ket_qua'].eq('thanh_cong').sum())
    return dict(token=token.sum(), tool=tool.sum(),
                chay_lai=(token + tool)[runs['attempt'] > 1].sum(),
                xem_lai=xem_lai, lam_lai=lam_lai, tong=tong,
                thanh_cong=thanh_cong, cps=tong / thanh_cong if thanh_cong else math.inf,
                hoa_don_moi_yc=(token.sum() + tool.sum()) / len(reqs) if len(reqs) else math.nan)


def tao_bao_cao(runs, reqs):
    """Tạo bảng A–B từ CSV; cùng nội dung dùng cho stdout và báo cáo Markdown."""
    def so(value, decimals=0):
        return f'{value:,.{decimals}f}'.translate(str.maketrans(',.', '.,'))

    lines = []

    def bang(headers, rows):
        lines.append('| ' + ' | '.join(headers) + ' |')
        lines.append('| ' + ' | '.join(['---'] * len(headers)) + ' |')
        lines.extend('| ' + ' | '.join(map(str, row)) + ' |' for row in rows)
        lines.append('')

    goc = mo_hinh(runs, reqs)
    lines.extend(['# Bảng chi phí · Nhiệm vụ A và B', '',
                  'Tính bằng `src/lab13.py` từ hai CSV giả lập, theo `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`. '
                  'Giá tiền theo giả định của lab; không làm tròn trong phép tính.', '',
                  'Các chi phí, tỷ số và thay đổi phụ thuộc phút nhân viên được ghi nhãn **simulated**. '
                  'Chi phí mỗi việc thành công (CPS) chưa gồm chi phí cố định hoặc xử lý thủ công bổ sung, trừ khi ghi rõ.', '',
                  '## A1 · Ba phép thử đáp án biết trước', ''])
    bang(['Phép thử (p = 0,8)', 'Kết quả của nhóm'], [
        ['Số lần chạy trung bình, tối đa 2 lần', so(so_lan_chay_ky_vong(.8, 2), 2)],
        ['Số lần chạy trung bình, chạy đến khi đúng', so(so_lan_chay_ky_vong(.8), 2)],
        ['Hệ số chi phí mỗi việc thành công, tối đa 3 lần', so(he_so_chi_phi_moi_viec_thanh_cong(.8, 3), 2)]])
    lines.extend(['## A2 · Mô hình chi phí từ trace', ''])
    bang(['Khoản', 'Giá trị (đ, trừ số việc)', 'Nguồn', 'Nhãn'], [
        ['Token', so(goc['token']), 'Mọi trace: tokens_in, tokens_out', 'đo từ trace'],
        ['Tool', so(goc['tool']), 'Mọi trace: tool_calls', 'đo từ trace'],
        ['Trong đó, phần của lần chạy thứ 2 và 3', so(goc['chay_lai']), 'attempt > 1; đã nằm trong token + tool', 'đo từ trace'],
        ['Xem lại', so(goc['xem_lai']), 'phut_xem_lai_simulated × 2.000', 'simulated'],
        ['Làm lại', so(goc['lam_lai']), 'phut_lam_lai_simulated × 2.000', 'simulated'],
        ['Tổng chi phí', so(goc['tong']), 'Token + tool + xem lại + làm lại', 'simulated'],
        ['Số việc thành công', so(goc['thanh_cong']), "ket_qua == 'thanh_cong'", 'đếm từ dữ liệu'],
        ['Chi phí mỗi việc thành công', so(goc['cps']), 'Tổng / số việc thành công', 'simulated'],
        ['Hóa đơn token và tool chia cho số yêu cầu', so(goc['hoa_don_moi_yc'], 1), '(Token + tool) / số yêu cầu', 'đo từ trace']])
    lines.extend([f"- CPS gấp **{so(goc['cps'] / goc['hoa_don_moi_yc'], 1)} lần** hóa đơn mỗi yêu cầu (simulated); tử số tính mọi lần chạy vì đều phát sinh tiền, mẫu số chỉ đếm {goc['thanh_cong']} việc thành công.",
                  f"- Làm lại chiếm nhiều nhất: **{so(goc['lam_lai'] / goc['tong'] * 100, 1)}%** tổng chi phí (simulated).", '',
                  '## A3 · Tách theo loại yêu cầu', ''])
    rows = []
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        subset = reqs[reqs['loai'].eq(loai)]
        result = mo_hinh(runs, subset)
        rows.append([loai, len(subset), so(result['thanh_cong'] / len(subset) * 100, 1) + '%',
                     so(len(runs[runs.request_id.isin(subset.request_id)]) / len(subset), 2),
                     so(result['cps']), so(result['cps'] / BASELINE, 2) + '×'])
    bang(['Loại', 'Số yêu cầu', 'Tỉ lệ thành công', 'Lần chạy/yêu cầu', 'CPS (đ, simulated)', 'CPS / 12.000 (simulated)'], rows)
    qt = reqs[reqs.loai.eq('quoc_te')]
    qt_runs = runs[runs.request_id.isin(qt.request_id)]
    rates = qt_runs.assign(ok=qt_runs.status.eq('ok')).groupby('attempt')['ok'].mean()
    lines.extend([f"- Quốc tế không đáng xử lý: CPS {so(mo_hinh(runs, qt)['cps'])} đ (simulated); tỷ lệ trace ok ở lần 1/2/3 là "
                  + ' / '.join(so(rates.get(k, 0) * 100, 1) + '%' for k in [1, 2, 3])
                  + ', chạy lại đến lần 3 có hiệu quả rất thấp. Phạm vi đề xuất: noi_dia + hang_nang.',
                  '- Cột so với 12.000 chỉ là tỷ số CPS, chưa chứng minh mức tiết kiệm của toàn hệ thống; B3 cộng xử lý thủ công cho các yêu cầu không thành công.', '',
                  '## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)', ''])
    scope = reqs[reqs.loai.isin(['noi_dia', 'hang_nang'])]
    scoped = mo_hinh(runs, scope)
    rows = []
    for volume in [45000, 22500]:
        success = volume * scoped['thanh_cong'] / len(reqs)
        fixed = 40000000 / success
        rows.append([so(volume) + ' yêu cầu/tháng', so(success), so(fixed), so(scoped['cps'] + fixed), so((scoped['cps'] + fixed) / BASELINE, 2) + '×'])
    bang(['Khối lượng toàn công ty', 'Việc thành công trong phạm vi/tháng', 'Cố định/việc (đ)', 'CPS + cố định (đ, simulated)', 'So với 12.000 (simulated)'], rows)
    lines.extend([f"- Quy đổi số thành công bằng khối lượng toàn công ty × {scoped['thanh_cong']}/{len(reqs)}; giả định cơ cấu yêu cầu và hiệu suất giữ nguyên.",
                  f"- Cố định chưa đổi kết luận CPS dưới 12.000 đ ở cả hai mức: {rows[0][3]} và {rows[1][3]} đ/việc (simulated); chưa gồm xử lý thủ công bổ sung.", '',
                  '## B1 · Đổi từng yếu tố', ''])
    scenarios = [
        ('Giá token gấp đôi', '52 và 260 đ/1.000 token; giữ giá tool', dict(gia_vao=52, gia_ra=260)),
        ('Giá token giảm một nửa', '13 và 65 đ/1.000 token', dict(gia_vao=13, gia_ra=65)),
        ('Tỉ lệ xem lại gấp đôi', 'Tiền xem lại × 2', dict(he_so_xem_lai=2)),
        ('Tỉ lệ xem lại giảm một nửa', 'Tiền xem lại ÷ 2', dict(he_so_xem_lai=.5)),
        ('Số ca làm lại gấp đôi', 'Tiền làm lại × 2', dict(he_so_lam_lai=2)),
        ('Số ca làm lại giảm một nửa', 'Tiền làm lại ÷ 2', dict(he_so_lam_lai=.5)),
        ('Lương nhân viên tăng 25%', '2.500 đ/phút', dict(luong_phut=2500)),
        ('Chỉ cho chạy tối đa 2 lần', 'Giới hạn 2 lần', dict(max_lan_chay=2)),
        ('Chỉ cho chạy 1 lần', 'Giới hạn 1 lần', dict(max_lan_chay=1))]
    values = [mo_hinh(runs, reqs, **kw)['cps'] for _, _, kw in scenarios]
    bang(['Kịch bản', 'Cách tính', 'CPS (đ, simulated)', 'Thay đổi (%, simulated)'],
         [[name, desc, so(cps), ('+' if cps >= goc['cps'] else '') + so((cps / goc['cps'] - 1) * 100, 1) + '%']
          for (name, desc, _), cps in zip(scenarios, values)])
    for up, down in [(0, 1), (2, 3), (4, 5)]:
        assert math.isclose(values[up] - goc['cps'], 2 * (goc['cps'] - values[down]), abs_tol=1e-8)
    lines.extend(['Giới hạn chạy: bỏ trace vượt giới hạn; yêu cầu vượt giới hạn chuyển nhân viên, phút xem lại/làm lại bằng 0.', '',
                  '## B2 · Đổi một cặp và xếp hạng', ''])
    pair = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    assert math.isclose(pair - goc['cps'], values[0] + values[2] - 2 * goc['cps'], abs_tol=1e-8)
    # Mỗi yếu tố chỉ xuất hiện một lần; lấy kịch bản có tác động lớn nhất của yếu tố.
    factors = [('Giá token', 0), ('Tỉ lệ xem lại', 2), ('Số ca làm lại', 4),
               ('Lương nhân viên', 6), ('Giới hạn chạy lại', 8)]
    ranking = sorted([(name, (values[i] / goc['cps'] - 1) * 100) for name, i in factors],
                     key=lambda x: abs(x[1]), reverse=True)[:3]
    lines.extend([f"- Token và xem lại cùng gấp đôi: **{so(pair)} đ/việc, +{so((pair / goc['cps'] - 1) * 100, 1)}%** (simulated); bằng tổng hai tác động riêng vì các khoản cộng tuyến tính, mẫu số không đổi.",
                  '- Ba yếu tố mạnh nhất theo độ lớn thay đổi trong B1 (simulated): ' + ' · '.join(f'{i}. {name}: {so(change, 1)}%' for i, (name, change) in enumerate(ranking, 1)) + '.', '',
                  '## B3 · Giới hạn chạy lại có thật sự rẻ hơn', ''])
    limits = [(k, mo_hinh(runs, reqs, max_lan_chay=k)) for k in [1, 2, 3]]
    bang(['Giới hạn', 'Tổng trợ lý (đ, simulated)', 'Không thành công', 'Cả hệ thống (đ, simulated)', 'CPS (đ, simulated)'],
         [[k, so(r['tong']), len(reqs) - r['thanh_cong'], so(r['tong'] + BASELINE * (len(reqs) - r['thanh_cong'])), so(r['cps'])] for k, r in limits])
    best = min(limits, key=lambda kr: kr[1]['tong'] + BASELINE * (len(reqs) - kr[1]['thanh_cong']))[0]
    best_cps = min(limits, key=lambda kr: kr[1]['cps'])[0]
    lines.extend(['Chi phí hệ thống = tổng trợ lý + 12.000 × số yêu cầu không thành công (gồm làm lại và chuyển nhân viên), theo quy ước B3; chưa cộng cố định.', '',
                  f'- Giới hạn **{best} lần** rẻ nhất cho công ty; CPS thấp nhất ở **{best_cps} lần** (simulated). Hai mục tiêu cho quyết định khác nhau vì chi phí xử lý thủ công nằm ngoài CPS.', '',
                  '## B4 · Nếu phải xem lại tất cả', ''])
    scope_runs = runs[runs.request_id.isin(scope.request_id)]
    n_review = scope_runs.loc[scope_runs.status.eq('ok'), 'request_id'].nunique()
    n_redo = int(scope.ket_qua.eq('lam_lai').sum())
    trace_cost = scoped['token'] + scoped['tool']
    mean_redo = reqs.loc[reqs.ket_qua.eq('lam_lai'), 'phut_lam_lai_simulated'].mean()
    rows = []
    for minutes in [9, 15.3]:
        review_cost = n_review * 5 * LUONG_PHUT
        redo_cost = n_redo * minutes * LUONG_PHUT
        total = trace_cost + review_cost + redo_cost
        cps = total / scoped['thanh_cong']
        breakeven = (BASELINE * scoped['thanh_cong'] - trace_cost - redo_cost) / (n_review * LUONG_PHUT)
        rows.append([so(minutes, 1), so(review_cost), so(redo_cost), so(total), so(cps), so(cps / BASELINE, 2) + '×', so(breakeven, 2)])
    lines.extend([f"Phạm vi {len(scope)} yêu cầu: {n_review} yêu cầu có trace ok, {n_redo} ca làm lại, {scoped['thanh_cong']} việc thành công; token + tool = {so(trace_cost)} đ.",
                  f"Mỗi yêu cầu có trace ok được xem lại đúng một lần, 5 phút; giữ nguyên số thành công. Phút làm lại trung bình toàn mẫu = {so(mean_redo, 2)} (simulated); kịch bản bổ sung dùng 15,3 theo hướng dẫn.", ''])
    bang(['Phút làm lại/ca', 'Tiền xem lại (đ)', 'Tiền làm lại (đ)', 'Tổng (đ)', 'CPS (đ)', 'CPS / 12.000', 'Phút xem lại hòa vốn'], rows)
    lines.extend(['Toàn bộ giá trị tiền, tỷ số và ngưỡng hòa vốn trong bảng B4 là **simulated**; chưa cộng cố định và xử lý thủ công bổ sung.', '',
                  f"- Xem lại 100% cho CPS **{rows[0][4]} đ ({rows[0][5]})** với 9 phút làm lại; tăng lên **{rows[1][4]} đ ({rows[1][5]})** với 15,3 phút (simulated), vượt 12.000 đ.",
                  f"- Pilot cần đo tỷ lệ xem lại an toàn và thời gian thực tế: hòa vốn CPS ở ≤ **{rows[0][6]} phút** xem lại (làm lại 9 phút), hoặc ≤ **{rows[1][6]} phút** (làm lại 15,3 phút), simulated.", ''])
    return '\n'.join(lines)


# ---------- Nhiệm vụ D · Tính toán cỡ mẫu ----------
def co_mau(p1, p2, alpha=0.05, power=0.8):
    """Cỡ mẫu mỗi nhóm khi so sánh hai tỉ lệ độc lập."""
    za, zb = NormalDist().inv_cdf(1 - alpha / 2), NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    return math.ceil((za * math.sqrt(2 * pb * (1 - pb))
                      + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2)


def tinh_toan_d1():
    print('\n--- KẾT QUẢ TÍNH CỠ MẪU NHIỆM VỤ D1 ---')
    n_yc = co_mau(0.70, 0.75)
    de_nv = 1 + (75 - 1) * 0.02
    n_nv = math.ceil(n_yc * de_nv)
    c_nv = math.ceil(n_nv / 75)
    print(f'a) Chia theo yêu cầu (5 điểm): {n_yc} yêu cầu/nhóm')
    print(f'b) Theo nhân viên, m = 75: DE = {de_nv:.2f}, n = {n_nv} mỗi nhóm -> cần {c_nv} nhân viên/nhóm (tổng 84 > 40: KHÔNG ĐỦ)')
    print(f'c) 20 nhân viên mỗi nhóm: trần n_eff = {20 / 0.02:.0f} (< {n_yc}: KHÔNG ĐẠT)')
    print(f'd) 6 depot mỗi nhóm: trần n_eff = {6 / 0.02:.0f}')
    
    n_target = 859
    c = 20
    icc = 0.02
    m_min = math.ceil(n_target * (1 - icc) / (c - n_target * icc))
    de_e = 1 + (m_min - 1) * icc
    es = proportion_effectsize(0.70, 0.75)
    power_at_5 = NormalIndPower().power(effect_size=es, nobs1=859, alpha=0.05, ratio=1.0)
    print(f'e) Mức chênh 6 điểm ({n_target}/nhóm), 20 nhân viên/nhóm: m >= {m_min} yêu cầu/người (DE = {de_e:.2f})')
    print(f'   Power nếu hiệu quả thật chỉ 5 điểm: {power_at_5:.2f}')


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    print(tao_bao_cao(runs, reqs))
    tinh_toan_d1()
