# Bàn giao của Thành viên 4: A4, B2, B4, số cho rủi ro kinh tế

Mọi số do `src/tv4_tinh_so.py` in ra (chạy trong `src/`: `python tv4_tinh_so.py`), dùng `mo_hinh` của `src/lab13.py`. Số tính từ cột `_simulated` có nhãn **simulated**.

| Phần | Gửi cho | File đích |
| --- | --- | --- |
| A4, B2, B4 | Thành viên 2 (người giữ) | `report/team/bang_chi_phi.md` |
| Số cho rủi ro kinh tế | Thành viên 3 (viết rủi ro) · Thành viên 4 (giữ) | `report/team/chi_so.md` (E2), `report/team/ho_so_launch_v0.md` (mục 7) |

## CP1 · A4: Chi phí cố định (phạm vi noi_dia + hang_nang)

Phạm vi có 982 yêu cầu, 900 việc thành công trên 1.200 yêu cầu của mẫu. Chi phí mỗi việc thành công trong phạm vi, chưa cộng cố định: 3.072.513 ÷ 900 = **3.414 đ** [simulated].
Việc thành công mỗi tháng = khối lượng × 900 / 1.200; chi phí cố định mỗi việc = 40.000.000 ÷ số việc thành công mỗi tháng.

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ [simulated] | 0,38× [simulated] |
| Một nửa khối lượng | 16.875 | 2.370 đ | 5.784 đ [simulated] | 0,48× [simulated] |

- **Chi phí cố định có đổi kết luận không?** Không đổi ở cả hai mức khối lượng (0,38× và 0,48× [simulated]). Kết luận chỉ đổi khi khối lượng còn dưới khoảng **6.212 yêu cầu/tháng** (14% kế hoạch); dưới mức đó trợ lý đắt hơn 12.000 đ [simulated].
- **Con số bất lợi cần nêu:** nếu cộng 82 ca trong phạm vi do nhân viên làm thay (× 12.000 đ), chi phí cả hệ thống là **5.217 đ/yêu cầu = 0,43×** [simulated], cao hơn con số 0,38×.

## CP2 · B2: Đổi một cặp

| Kịch bản | Chi phí mỗi việc thành công | Thay đổi |
| --- | ---: | ---: |
| Gốc (A2) | 4.472 đ [simulated] | |
| Riêng giá token gấp đôi | 4.723 đ [simulated] | +5,6% |
| Riêng tỉ lệ xem lại gấp đôi | 6.292 đ [simulated] | +40,7% |
| **Cả cặp** (`gia_vao=52, gia_ra=260, he_so_xem_lai=2`) | **6.543 đ** [simulated] | **+46,3%** |

- Tác động của cặp đúng bằng tổng hai tác động riêng (5,6% + 40,7% = 46,3%) vì mô hình cộng tuyến tính: mỗi khoản chi phí cộng độc lập vào tử số, mẫu số không đổi.
- Giá token gấp đôi chỉ thêm 5,6%; xem lại gấp đôi thêm 40,7% [simulated]. Pilot nên theo dõi giờ nhân viên, không phải giá token.

## CP2 · B4: Nếu phải xem lại 100% (noi_dia + hang_nang)

Cách tính (đề bài: mỗi lần xem lại 5 phút, mỗi ca làm lại 9 phút):
1. Yêu cầu có ít nhất một lần chạy `ok`: **948** × 5 phút × 2.000 đ = 9.480.000 đ [simulated].
2. Ca `lam_lai`: **48** × 9 phút × 2.000 đ = 864.000 đ [simulated].
3. Token + tool của mọi lần chạy thuộc 982 yêu cầu: 224.513 đ (đo từ trace).
4. Tổng 10.568.513 đ ÷ 900 việc thành công = **11.743 đ = 0,98×** của 12.000 đ [simulated].

| Phút làm lại mỗi ca | Tổng | Chi phí mỗi việc thành công | So với 12.000 đ | Hoà vốn: phút xem lại tối đa |
| --- | ---: | ---: | ---: | ---: |
| 9 (đề bài) | 10.568.513 đ | 11.743 đ [simulated] | 0,98× [simulated] | 5,1 phút [simulated] |
| 15,3 (trung bình cột `phut_lam_lai_simulated`, 74 ca) | 11.173.313 đ | 12.415 đ [simulated] | 1,03× [simulated] | 4,8 phút [simulated] |

- **Trả lời B4:** xem lại 100% làm chi phí lên 11.743 đ = 0,98× [simulated], gần như không tiết kiệm. Nếu làm lại mất 15,3 phút như dữ liệu thì 12.415 đ = 1,03× [simulated], đắt hơn nhân viên tự làm. Tiền xem lại chiếm 90% tổng.
- **Pilot cần học được gì:** tỉ lệ xem lại giảm an toàn xuống mức nào, và mỗi lần xem lại có dưới 5,1 phút không (4,8 phút nếu làm lại 15,3 phút) [simulated]. Vì vậy phút xem lại phải được đo thật bằng event, thay cho cột simulated.

## CP2 → CP5 · Số chuyển tiếp cho rủi ro kinh tế

| Rủi ro | Tác động đã tính | Mức hiện tại để đặt dấu hiệu theo dõi |
| --- | --- | --- |
| Số ca làm lại tăng gấp đôi | 6.787 đ, +51,8% [simulated] (B1) | Tỉ lệ làm lại trong phạm vi: 4,9% (48/982) |
| Tỉ lệ xem lại tăng gấp đôi | 6.292 đ, +40,7% [simulated] (B1) | Tỉ lệ được xem lại trong phạm vi: 13,0% |
| Phải xem lại 100% kéo dài | 11.743 đ = 0,98× (12.415 đ = 1,03× nếu làm lại 15,3 phút) [simulated] (B4) | Phút xem lại thật phải ≤ 5,1 phút |
| Khối lượng thấp hơn dự kiến | Cố định +1.185 đ/việc ở 45.000 yc/tháng, +2.370 đ/việc nếu còn một nửa; hoà vốn ở ~6.212 yc/tháng [simulated] (A4) | Số việc thành công theo tuần so với kế hoạch (33.750/tháng) |
