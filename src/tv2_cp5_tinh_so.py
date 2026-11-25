"""Lab 13 · CP5 · Phần tính và đối chiếu của Thành viên 2 (Nguyễn Tiến Đạt).
Chạy trong thư mục src/: python tv2_cp5_tinh_so.py
Tính độc lập chỉ số sử dụng (E1), kiểm tra toàn vẹn cột xem lại, quan hệ trace_id
và đối chiếu chéo toàn bộ chỉ số E1 với report/team/chi_so.md.
Mọi số tính từ cột *_simulated đều ghi nhãn [simulated].
"""
import pandas as pd

LOAI = ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']
PHAM_VI = ['noi_dia', 'hang_nang']


def doc_du_lieu():
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    return runs, reqs


def pct(x, so_le=2):
    return f'{x * 100:.{so_le}f}'.replace('.', ',') + '%'


def so(x, so_le=2):
    return f'{x:.{so_le}f}'.replace('.', ',')


def cp5_chi_so_su_dung(runs, reqs):
    print('=== CP5 · E1 · Chỉ số sử dụng (tính từ logix_requests.csv) ===')
    # Kiểm tra toàn vẹn cột duoc_xem_lai và quyet_dinh_xem_lai
    lech_co = int(((reqs['duoc_xem_lai'] == 1) & (reqs['quyet_dinh_xem_lai'] == '')).sum())
    lech_khong = int(((reqs['duoc_xem_lai'] == 0) & (reqs['quyet_dinh_xem_lai'] != '')).sum())
    print(f'Kiểm tra toàn vẹn duoc_xem_lai ↔ quyet_dinh_xem_lai: lệch = {lech_co} / {lech_khong}')
    print()

    nhom = [
        ('Toàn mẫu', reqs),
        ('Phạm vi (noi_dia + hang_nang)', reqs[reqs['loai'].isin(PHAM_VI)]),
    ] + [(loai, reqs[reqs['loai'] == loai]) for loai in LOAI]

    print('| Nhóm | Yêu cầu | Có ≥1 lần ok | Được xem lại | giữ | sửa | bỏ '
          '| Bỏ qua gợi ý (sua+bo)/xem | Phút xem lại TB [simulated] |')
    print('| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |')
    for ten, df in nhom:
        co_ok = runs.loc[
            runs['request_id'].isin(df['request_id']) & (runs['status'] == 'ok'),
            'request_id'
        ].nunique()
        xem = df[df['duoc_xem_lai'] == 1]
        giu = int((xem['quyet_dinh_xem_lai'] == 'giu').sum())
        sua = int((xem['quyet_dinh_xem_lai'] == 'sua').sum())
        bo = int((xem['quyet_dinh_xem_lai'] == 'bo').sum())
        bo_qua = sua + bo
        phut_tb = xem['phut_xem_lai_simulated'].mean()
        print(f'| {ten} | {len(df)} | {co_ok} ({pct(co_ok / len(df))}) '
              f'| {len(xem)} ({pct(len(xem) / len(df))}) | {giu} | {sua} | {bo} '
              f'| {bo_qua}/{len(xem)} = {pct(bo_qua / len(xem))} '
              f'| {so(phut_tb)} phút [simulated] |')
    print()

    pv = reqs[reqs['loai'].isin(PHAM_VI)]
    xem_pv = pv[pv['duoc_xem_lai'] == 1]
    print(f"Tổng phút xem lại toàn mẫu: {int(reqs['phut_xem_lai_simulated'].sum())} phút / "
          f"{int((reqs['duoc_xem_lai'] == 1).sum())} lượt [simulated]")
    print(f"Tổng phút xem lại phạm vi:  {int(xem_pv['phut_xem_lai_simulated'].sum())} phút / "
          f"{len(xem_pv)} lượt (trung vị {so(xem_pv['phut_xem_lai_simulated'].median(), 1)} phút) [simulated]")
    print()


def cp5_kiem_tra_trace_va_e1(runs, reqs):
    print('=== CP5 · Đối chiếu cấu trúc trace_id và toàn bộ E1 ===')
    so_req_nhieu_lan = int((reqs['so_lan_chay'] > 1).sum())
    runs_nhieu = runs[runs['request_id'].isin(reqs.loc[reqs['so_lan_chay'] > 1, 'request_id'])]
    print(f"logix_runs.csv: {len(runs)} dòng, {runs['trace_id'].nunique()} trace_id cho "
          f"{runs['request_id'].nunique()} request_id (tối đa {runs.groupby('request_id')['trace_id'].nunique().max()} trace_id/request).")
    print(f"Yêu cầu chạy > 1 lần: {so_req_nhieu_lan} yêu cầu → {len(runs_nhieu)} lần chạy, "
          f"{runs_nhieu['trace_id'].nunique()} trace_id riêng biệt.")
    print()

    pv = reqs[reqs['loai'].isin(PHAM_VI)]
    for ten, df in [('Toàn mẫu', reqs), ('Phạm vi noi_dia + hang_nang', pv)]:
        chinh = (df['dong_trong_24h'] == 1) & (df['mo_lai_trong_7_ngay'] == 0)
        xem = df[df['duoc_xem_lai'] == 1]
        bo_qua = xem['quyet_dinh_xem_lai'].isin(['sua', 'bo'])
        an_toan = df['mo_lai_trong_7_ngay'] == 1
        print(f'{ten}: chính {pct(chinh.mean())} ({int(chinh.sum())}/{len(df)}) · '
              f'bỏ qua gợi ý {pct(bo_qua.mean())} ({int(bo_qua.sum())}/{len(xem)}) · '
              f'mở lại 7 ngày {pct(an_toan.mean())} ({int(an_toan.sum())}/{len(df)})')


if __name__ == '__main__':
    runs, reqs = doc_du_lieu()
    cp5_chi_so_su_dung(runs, reqs)
    cp5_kiem_tra_trace_va_e1(runs, reqs)
