"""Lab 13 · Nhiệm vụ E1 (CP5) · Đặc tả và tính thử chỉ số từ logix_requests.csv.

Module riêng của Người 4 để tránh xung đột khi merge.
- Chạy độc lập trong thư mục src/:  python cp5_chi_so.py
- Gọi từ src/lab13.py:              from cp5_chi_so import chay_chi_so; chay_chi_so(reqs)
"""
from pathlib import Path
import pandas as pd


def tinh_chi_so_e1(reqs: pd.DataFrame) -> dict:
    """Tính ba chỉ số E1 (chính, dùng, an toàn) trên DataFrame yêu cầu.

    Lưu ý: reqs phải được đọc với keep_default_na=False để ô trống ở cột
    quyet_dinh_xem_lai không bị chuyển thành NaN.
    """
    tong = len(reqs)
    chinh_mask = (reqs['dong_trong_24h'] == 1) & (reqs['mo_lai_trong_7_ngay'] == 0)
    chinh_so_ca = int(chinh_mask.sum())
    chinh_ti_le = chinh_so_ca / tong if tong else 0.0

    xem = reqs[reqs['duoc_xem_lai'] == 1]
    duoc_xem_lai_so_ca = len(xem)
    bo_qua_so_ca = int(xem['quyet_dinh_xem_lai'].isin(['sua', 'bo']).sum())
    bo_qua_ti_le = bo_qua_so_ca / duoc_xem_lai_so_ca if duoc_xem_lai_so_ca else 0.0

    an_toan_so_ca = int((reqs['mo_lai_trong_7_ngay'] == 1).sum())
    an_toan_ti_le = an_toan_so_ca / tong if tong else 0.0

    return {
        'tong_yeu_cau': tong,
        'chinh_so_ca': chinh_so_ca,
        'chinh_ti_le': chinh_ti_le,
        'duoc_xem_lai_so_ca': duoc_xem_lai_so_ca,
        'bo_qua_so_ca': bo_qua_so_ca,
        'bo_qua_ti_le': bo_qua_ti_le,
        'an_toan_so_ca': an_toan_so_ca,
        'an_toan_ti_le': an_toan_ti_le,
    }


def chay_chi_so(reqs: pd.DataFrame) -> dict:
    """Tính và in bảng ba chỉ số E1 trên toàn bộ mẫu và trên phạm vi pilot."""
    kq = tinh_chi_so_e1(reqs)

    print('=== Nhiệm vụ E1 · Tính thử ba chỉ số trên mẫu chạy thử ===')
    print(
        f"Chính   (% đóng <=24h và không mở lại 7 ngày): "
        f"{kq['chinh_ti_le'] * 100:6.2f}% ({kq['chinh_so_ca']}/{kq['tong_yeu_cau']})"
    )
    print(
        f"Dùng    (tỉ lệ bỏ qua gợi ý = (sua+bo)/xem):   "
        f"{kq['bo_qua_ti_le'] * 100:6.2f}% ({kq['bo_qua_so_ca']}/{kq['duoc_xem_lai_so_ca']})"
    )
    print(
        f"An toàn (tỉ lệ lỗi lọt đến khách - mở lại 7d): "
        f"{kq['an_toan_ti_le'] * 100:6.2f}% ({kq['an_toan_so_ca']}/{kq['tong_yeu_cau']})"
    )

    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    kq_pv = tinh_chi_so_e1(pham_vi)
    print(
        f"\nTham chiếu phạm vi pilot (noi_dia + hang_nang, n={kq_pv['tong_yeu_cau']}):"
    )
    print(
        f"  Chính:   {kq_pv['chinh_ti_le'] * 100:6.2f}% ({kq_pv['chinh_so_ca']}/{kq_pv['tong_yeu_cau']})"
    )
    print(
        f"  Dùng:    {kq_pv['bo_qua_ti_le'] * 100:6.2f}% ({kq_pv['bo_qua_so_ca']}/{kq_pv['duoc_xem_lai_so_ca']})"
    )
    print(
        f"  An toàn: {kq_pv['an_toan_ti_le'] * 100:6.2f}% ({kq_pv['an_toan_so_ca']}/{kq_pv['tong_yeu_cau']})"
    )
    print(
        "\nLưu ý: Đợt chạy thử không có nhóm đối chứng; chỉ diễn giải là "
        "'chỉ số trong đợt chạy thử là ...', không viết 'trợ lý đã nâng chỉ số'."
    )
    return kq


if __name__ == '__main__':
    csv_path = Path(__file__).resolve().parent / 'logix_requests.csv'
    reqs = pd.read_csv(csv_path, keep_default_na=False)
    chay_chi_so(reqs)
