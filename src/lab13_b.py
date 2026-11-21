"""Bàn giao Người 1. Import in_b rồi gọi in_b(runs, reqs, mo_hinh) sau A4."""


def in_b(runs, reqs, mo_hinh):
    kich_ban = [
        ('Giá token gấp đôi', dict(gia_vao=52, gia_ra=260)),
        ('Giá token giảm một nửa', dict(gia_vao=13, gia_ra=65)),
        ('Xem lại gấp đôi', dict(he_so_xem_lai=2)),
        ('Xem lại giảm một nửa', dict(he_so_xem_lai=0.5)),
        ('Làm lại gấp đôi', dict(he_so_lam_lai=2)),
        ('Làm lại giảm một nửa', dict(he_so_lam_lai=0.5)),
        ('Lương tăng 25%', dict(luong_phut=2500)),
        ('Tối đa 2 lần chạy', dict(max_lan_chay=2)),
        ('Chỉ 1 lần chạy', dict(max_lan_chay=1)),
    ]
    goc = mo_hinh(runs, reqs)['cps']
    print(f'\nB1 · Mốc A2: {goc:,.0f} đ/việc [simulated]')
    for ten, tham_so in kich_ban:
        cps = mo_hinh(runs, reqs, **tham_so)['cps']
        print(f'{ten}: {cps:,.0f} đ/việc ({cps / goc - 1:+.1%}) [simulated]')

    ket_hop = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    print(f'\nB2 · Token và xem lại gấp đôi: {ket_hop:,.0f} đ/việc '
          f'({ket_hop / goc - 1:+.1%}) [simulated]')

    muc_tu_lam = 12_000
    print('\nB3 · Lượt tối đa | Trợ lý | Không thành công | Hệ thống | Chi phí/việc [simulated]')
    for gioi_han in (1, 2, 3):
        ket_qua = mo_hinh(runs, reqs, max_lan_chay=gioi_han)
        can_lam_thay = len(reqs) - ket_qua['thanh_cong']
        he_thong = ket_qua['tong'] + muc_tu_lam * can_lam_thay
        print(f"{gioi_han} | {ket_qua['tong']:,.0f} đ | {can_lam_thay:,} | "
              f"{he_thong:,.0f} đ | {ket_qua['cps']:,.0f} đ")

    pilot = reqs[reqs['loai'].isin(('noi_dia', 'hang_nang'))]
    ket_qua = mo_hinh(runs, pilot)
    co_luot_ok = runs['request_id'].isin(pilot['request_id']) & runs['status'].eq('ok')
    so_xem_lai = runs.loc[co_luot_ok, 'request_id'].nunique()
    so_lam_lai = pilot['ket_qua'].eq('lam_lai').sum()
    phut_lam_lai_mau = round(
        reqs.loc[reqs['ket_qua'].eq('lam_lai'), 'phut_lam_lai_simulated'].mean(), 1
    )
    luong_phut = 2_000
    tien_token_tool = ket_qua['token'] + ket_qua['tool']
    print(f'\nB4 · Xem lại {so_xem_lai} yêu cầu có lượt ok, 5 phút/yêu cầu [simulated]')
    for phut_lam_lai in (9, phut_lam_lai_mau):
        truoc_xem_lai = tien_token_tool + so_lam_lai * phut_lam_lai * luong_phut
        cps = (truoc_xem_lai + so_xem_lai * 5 * luong_phut) / ket_qua['thanh_cong']
        phut_hoa_von = ((muc_tu_lam * ket_qua['thanh_cong'] - truoc_xem_lai)
                        / (so_xem_lai * luong_phut))
        print(f'Làm lại {phut_lam_lai:g} phút/ca: {cps:,.0f} đ/việc '
              f'({cps / muc_tu_lam:.2f}× tự làm), hòa vốn ở {phut_hoa_von:.2f} phút xem lại [simulated]')
