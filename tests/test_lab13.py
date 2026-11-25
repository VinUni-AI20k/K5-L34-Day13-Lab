"""Unit & integration tests for src/lab13.py (Lab 13 — Launch & Economics)."""
import os
import sys
import unittest
import pandas as pd

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIR = os.path.join(ROOT_DIR, 'src')
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

import lab13  # noqa: E402


class TestA1RetryEconomics(unittest.TestCase):
    """Pure unit tests for A1 retry economics functions."""

    def test_known_answers_gate(self):
        self.assertAlmostEqual(lab13.so_lan_chay_ky_vong(0.8, 2), 1.20, places=9)
        self.assertAlmostEqual(lab13.so_lan_chay_ky_vong(0.8), 1.25, places=9)
        self.assertAlmostEqual(
            lab13.he_so_chi_phi_moi_viec_thanh_cong(0.8, 3), 1.25, places=9
        )
        lab13.kiem_tra_dap_an_biet_truoc()

    def test_ti_le_thanh_cong(self):
        self.assertAlmostEqual(lab13.ti_le_thanh_cong(0.8, 1), 0.80, places=9)
        self.assertAlmostEqual(lab13.ti_le_thanh_cong(0.8, 2), 0.96, places=9)
        self.assertAlmostEqual(lab13.ti_le_thanh_cong(0.8, None), 1.0, places=9)

    def test_cost_factor_equals_inverse_p_regardless_of_k(self):
        for p in (0.25, 0.5, 0.8):
            for k in (1, 2, 3, 5, None):
                self.assertAlmostEqual(
                    lab13.he_so_chi_phi_moi_viec_thanh_cong(p, k), 1.0 / p, places=9
                )

    def test_invalid_probability_raises(self):
        with self.assertRaises(ValueError):
            lab13.so_lan_chay_ky_vong(0.0, 2)
        with self.assertRaises(ValueError):
            lab13.so_lan_chay_ky_vong(1.2, 2)


class TestCostModelSynthetic(unittest.TestCase):
    """Pure unit tests for mo_hinh using minimal synthetic trace data."""

    def setUp(self):
        self.runs = pd.DataFrame(
            [
                # R1: fails attempt 1, succeeds attempt 2
                dict(
                    run_id='r1', request_id='R1', trace_id='t1', attempt=1,
                    tokens_in=1000, tokens_out=1000, tool_calls=2, status='loi',
                ),
                dict(
                    run_id='r2', request_id='R1', trace_id='t2', attempt=2,
                    tokens_in=1000, tokens_out=1000, tool_calls=2, status='ok',
                ),
                # R2: fails attempt 1, transferred to staff
                dict(
                    run_id='r3', request_id='R2', trace_id='t3', attempt=1,
                    tokens_in=2000, tokens_out=0, tool_calls=1, status='loi',
                ),
            ]
        )
        self.reqs = pd.DataFrame(
            [
                dict(
                    request_id='R1', depot='D01', staff_id='NV001', loai='noi_dia',
                    so_tien_vnd=100000, so_lan_chay=2, ket_qua='thanh_cong',
                    duoc_xem_lai=1, quyet_dinh_xem_lai='giu',
                    phut_xem_lai_simulated=3, phut_lam_lai_simulated=0,
                    dong_trong_24h=1, mo_lai_trong_7_ngay=0,
                ),
                dict(
                    request_id='R2', depot='D01', staff_id='NV001', loai='quoc_te',
                    so_tien_vnd=200000, so_lan_chay=1, ket_qua='chuyen_nhan_vien',
                    duoc_xem_lai=0, quyet_dinh_xem_lai='',
                    phut_xem_lai_simulated=0, phut_lam_lai_simulated=0,
                    dong_trong_24h=1, mo_lai_trong_7_ngay=0,
                ),
            ]
        )

    def test_failed_runs_counted_in_numerator_and_only_success_in_denominator(self):
        kq = lab13.mo_hinh(self.runs, self.reqs)
        # tokens_in total = 4000 -> 4*26 = 104; tokens_out total = 2000 -> 2*130 = 260 => 364
        # tool_calls total = 5 -> 5*15 = 75
        # attempt > 1: r2 has 26 + 130 + 30 = 186
        # xem_lai = 3 * 2000 = 6000; lam_lai = 0
        self.assertAlmostEqual(kq['token'], 364.0, places=6)
        self.assertAlmostEqual(kq['tool'], 75.0, places=6)
        self.assertAlmostEqual(kq['chay_lai'], 186.0, places=6)
        self.assertAlmostEqual(kq['xem_lai'], 6000.0, places=6)
        self.assertAlmostEqual(kq['lam_lai'], 0.0, places=6)
        self.assertEqual(kq['thanh_cong'], 1)
        self.assertAlmostEqual(kq['tong'], 6439.0, places=6)
        self.assertAlmostEqual(kq['cps'], 6439.0, places=6)
        self.assertAlmostEqual(kq['hoa_don_moi_yc'], (364.0 + 75.0) / 2, places=6)

    def test_max_lan_chay_truncates_and_zeroes_simulated_minutes(self):
        kq = lab13.mo_hinh(self.runs, self.reqs, max_lan_chay=1)
        # R1 exceeded max_lan_chay=1 so thanh_cong becomes 0 and xem_lai becomes 0
        self.assertEqual(kq['thanh_cong'], 0)
        self.assertAlmostEqual(kq['xem_lai'], 0.0, places=6)
        self.assertAlmostEqual(kq['chay_lai'], 0.0, places=6)


class TestLab13OnLogixData(unittest.TestCase):
    """End-to-end verification against src/logix_runs.csv and src/logix_requests.csv."""

    @classmethod
    def setUpClass(cls):
        cls.runs = pd.read_csv(os.path.join(SRC_DIR, 'logix_runs.csv'))
        cls.reqs = pd.read_csv(
            os.path.join(SRC_DIR, 'logix_requests.csv'), keep_default_na=False
        )

    def test_a2_trace_cost_model(self):
        kq = lab13.mo_hinh(self.runs, self.reqs)
        self.assertAlmostEqual(kq['token'], 245585, delta=5)
        self.assertAlmostEqual(kq['tool'], 84000, delta=1)
        self.assertAlmostEqual(kq['chay_lai'], 93804, delta=5)
        self.assertAlmostEqual(kq['xem_lai'], 1780000, delta=1)
        self.assertAlmostEqual(kq['lam_lai'], 2264000, delta=1)
        self.assertAlmostEqual(kq['tong'], 4373585, delta=5)
        self.assertEqual(kq['thanh_cong'], 978)
        self.assertAlmostEqual(kq['cps'], 4472, delta=2)
        self.assertAlmostEqual(kq['hoa_don_moi_yc'], 274.7, delta=0.5)
        self.assertAlmostEqual(kq['cps'] / kq['hoa_don_moi_yc'], 16.3, delta=0.1)

    def test_a3_breakdown_by_type_and_attempt_ok_rate(self):
        df_loai = lab13.phan_tich_theo_loai(self.runs, self.reqs)
        self.assertEqual(
            list(df_loai['loai']), ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']
        )
        self.assertEqual(int(df_loai['so_yeu_cau'].sum()), 1200)

        by_loai = df_loai.set_index('loai')
        self.assertEqual(int(by_loai.loc['noi_dia', 'so_yeu_cau']), 824)
        self.assertAlmostEqual(by_loai.loc['noi_dia', 'cps'], 2696, delta=5)
        self.assertEqual(int(by_loai.loc['hang_nang', 'so_yeu_cau']), 158)
        self.assertAlmostEqual(by_loai.loc['hang_nang', 'cps'], 8221, delta=5)
        self.assertEqual(int(by_loai.loc['quoc_te', 'so_yeu_cau']), 150)
        self.assertAlmostEqual(by_loai.loc['quoc_te', 'cps'], 22515, delta=10)
        self.assertEqual(int(by_loai.loc['doi_tac', 'so_yeu_cau']), 68)
        self.assertAlmostEqual(by_loai.loc['doi_tac', 'cps'], 10215, delta=10)

        ok_rate = lab13.ti_le_ok_theo_lan_thu(self.runs, self.reqs)
        self.assertAlmostEqual(ok_rate.loc['quoc_te', 1], 0.30, delta=0.01)
        self.assertAlmostEqual(ok_rate.loc['quoc_te', 2], 0.114, delta=0.01)
        self.assertAlmostEqual(ok_rate.loc['quoc_te', 3], 0.022, delta=0.01)

    def test_a4_fixed_cost_in_pilot_scope(self):
        a4 = lab13.tinh_chi_phi_co_dinh(self.runs, self.reqs)
        self.assertEqual(a4['thanh_cong_mau'], 900)
        self.assertAlmostEqual(a4['cps_bien_doi'], 3414, delta=2)

        full = a4['day_du']
        self.assertAlmostEqual(full['viec_thanh_cong_thang'], 33750, delta=1)
        self.assertAlmostEqual(full['co_dinh_moi_viec'], 1185, delta=2)
        self.assertAlmostEqual(full['cps_cong_co_dinh'], 4599, delta=3)
        self.assertAlmostEqual(full['so_voi_baseline'], 0.38, delta=0.01)

        half = a4['nua_khoi_luong']
        self.assertAlmostEqual(half['viec_thanh_cong_thang'], 16875, delta=1)
        self.assertAlmostEqual(half['co_dinh_moi_viec'], 2370, delta=2)
        self.assertAlmostEqual(half['cps_cong_co_dinh'], 5784, delta=3)
        self.assertAlmostEqual(half['so_voi_baseline'], 0.48, delta=0.01)

    def test_b1_b2_sensitivity_and_linearity(self):
        b = lab13.bang_do_nhay(self.runs, self.reqs)
        b1 = {row['kich_ban']: row for row in b['b1']}
        self.assertEqual(len(b1), 9)

        # Linearity check: half reduction == -0.5 * double increase
        for double_key, half_key in [
            ('Giá token gấp đôi', 'Giá token giảm một nửa'),
            ('Tỉ lệ xem lại gấp đôi', 'Tỉ lệ xem lại giảm một nửa'),
            ('Số ca làm lại gấp đôi', 'Số ca làm lại giảm một nửa'),
        ]:
            self.assertAlmostEqual(
                b1[half_key]['thay_doi_pct'],
                -0.5 * b1[double_key]['thay_doi_pct'],
                places=6,
            )

        self.assertAlmostEqual(b1['Số ca làm lại gấp đôi']['cps'], 6787, delta=3)
        self.assertAlmostEqual(b1['Tỉ lệ xem lại gấp đôi']['cps'], 6292, delta=3)
        self.assertAlmostEqual(b1['Lương nhân viên tăng 25%']['cps'], 5506, delta=3)
        self.assertAlmostEqual(b1['Chỉ cho chạy tối đa 2 lần']['cps'], 4237, delta=3)
        self.assertAlmostEqual(b1['Chỉ cho chạy 1 lần']['cps'], 4111, delta=3)

        # B2 pair additivity
        b2 = b['b2_cap']
        self.assertAlmostEqual(b2['cps'], 6543, delta=3)
        expected_pair_pct = (
            b1['Giá token gấp đôi']['thay_doi_pct']
            + b1['Tỉ lệ xem lại gấp đôi']['thay_doi_pct']
        )
        self.assertAlmostEqual(b2['thay_doi_pct'], expected_pair_pct, places=6)

        self.assertEqual(
            b['top3_yeu_to'],
            ['Số ca làm lại', 'Tỉ lệ xem lại', 'Lương nhân viên'],
        )

    def test_b3_retry_cap_system_cost(self):
        b3 = {row['gioi_han']: row for row in lab13.phan_tich_gioi_han_chay_lai(self.runs, self.reqs)}
        self.assertAlmostEqual(b3[1]['chi_phi_ca_he_thong'], 7449781, delta=10)
        self.assertEqual(b3[1]['khong_thanh_cong'], 319)
        self.assertAlmostEqual(b3[2]['chi_phi_ca_he_thong'], 6901220, delta=10)
        self.assertEqual(b3[2]['khong_thanh_cong'], 234)
        self.assertAlmostEqual(b3[3]['chi_phi_ca_he_thong'], 7037585, delta=10)
        self.assertEqual(b3[3]['khong_thanh_cong'], 222)

        # System cost is cheapest at 2 retries, whereas CPS alone is lowest at 1 retry
        cheapest_sys = min(b3.values(), key=lambda r: r['chi_phi_ca_he_thong'])['gioi_han']
        cheapest_cps = min(b3.values(), key=lambda r: r['cps'])['gioi_han']
        self.assertEqual(cheapest_sys, 2)
        self.assertEqual(cheapest_cps, 1)

    def test_b4_full_review_100_percent(self):
        b4 = lab13.phan_tich_xem_lai_100(self.runs, self.reqs)
        self.assertEqual(b4['so_yeu_cau_pham_vi'], 982)
        self.assertEqual(b4['so_ca_ok'], 948)
        self.assertEqual(b4['so_ca_lam_lai'], 48)
        self.assertEqual(b4['thanh_cong'], 900)
        self.assertAlmostEqual(b4['token_tool'], 224513, delta=5)

        self.assertAlmostEqual(b4['cps_9_phut'], 11743, delta=3)
        self.assertAlmostEqual(b4['ti_so_9_phut'], 0.98, delta=0.01)
        self.assertAlmostEqual(b4['hoa_von_xem_lai_9_phut'], 5.1, delta=0.1)

        self.assertAlmostEqual(b4['phut_lam_lai_tb_du_lieu'], 15.3, delta=0.1)
        self.assertAlmostEqual(b4['cps_du_lieu'], 12414, delta=15)
        self.assertAlmostEqual(b4['ti_so_du_lieu'], 1.03, delta=0.01)
        self.assertAlmostEqual(b4['hoa_von_xem_lai_du_lieu'], 4.8, delta=0.1)

    def test_d1_sample_size_and_normal_ind_power(self):
        d1 = lab13.phan_tich_co_mau_d1()
        self.assertEqual(d1['a_theo_yeu_cau'], 1251)
        # NormalIndPower cross-check within 2%
        self.assertAlmostEqual(
            d1['a_statsmodels_normal_ind_power'], 1251, delta=25
        )
        self.assertAlmostEqual(d1['b_design_effect'], 2.48, places=4)
        self.assertEqual(d1['b_n_moi_nhom'], 3103)
        self.assertEqual(d1['b_nhan_vien_moi_nhom'], 42)
        self.assertEqual(d1['b_tong_nhan_vien'], 84)
        self.assertAlmostEqual(d1['c_hieu_dung_toi_da_20_nv'], 1000.0, places=4)
        self.assertAlmostEqual(d1['d_hieu_dung_toi_da_6_depot'], 300.0, places=4)
        self.assertEqual(d1['e_n_6_diem'], 859)
        self.assertEqual(d1['e_m_toi_thieu'], 299)
        self.assertAlmostEqual(d1['e_design_effect'], 6.96, places=2)
        self.assertAlmostEqual(d1['e_power_tai_5_diem'], 0.64, delta=0.02)

    def test_e1_trial_metrics_and_safety_baseline(self):
        e1 = lab13.chi_so_dot_chay_thu(self.reqs)
        self.assertAlmostEqual(e1['chinh'], 994 / 1200, places=6)
        self.assertAlmostEqual(e1['bo_qua'], 48 / 177, places=6)
        self.assertAlmostEqual(e1['an_toan'], 51 / 1200, places=6)
        self.assertAlmostEqual(e1['an_toan_pham_vi'], 39 / 982, places=6)


if __name__ == '__main__':
    unittest.main()
