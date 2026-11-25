# Bàn giao của Thành viên 4: A4, B2, B4, số cho rủi ro kinh tế

Mọi số do `src/tv4_tinh_so.py` in ra (chạy trong `src/`: `python tv4_tinh_so.py`), dùng `mo_hinh` của `src/lab13.py`. Số tính từ cột `_simulated` có nhãn **simulated**.

| Phần | Gửi cho | File đích |
| --- | --- | --- |
| A4, B2, B4 | Thành viên 2 (người giữ) | `report/team/bang_chi_phi.md` |
| Số cho rủi ro kinh tế | Thành viên 3 (viết rủi ro) · Thành viên 4 (giữ) | `report/team/chi_so.md` (E2), `report/team/ho_so_launch_v0.md` (mục 7) |
| Bảng khắc phục 5 ca | Thành viên 3 (người giữ) | `report/team/bang_loi.md` (mục "Bảng khắc phục") |

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

## CP3 · Bảng khắc phục 5 ca, mỗi loại một ca

> **Gửi cho TV3 sau khi TV1 và TV2 đã chốt hai bộ nhãn độc lập.** Bảng dưới có ghi loại cho từng ca, nên không để người gắn nhãn xem trước.
> Loại ở đây là loại dự kiến theo định nghĩa Google PAIR. Nếu nhãn thống nhất của nhóm xếp ca chính vào loại khác, dùng ca dự phòng của loại đó.

Mức nền từ đợt chạy thử dùng để đặt ngưỡng (`cp3_nguong` trong `src/tv4_tinh_so.py`, đo từ dữ liệu):
- Chuyển nhân viên: 3,5% trong phạm vi noi_dia + hang_nang; quoc_te 60,7%.
- Mở lại 7 ngày trong phạm vi: 3,97% (39/982).
- Token + tool mỗi yêu cầu theo depot: trung vị 273 đ, depot cao nhất chỉ 1,05× trung vị.

### Bảng chính (chọn ca có nhãn rõ nhất cho mỗi loại)

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Event `refund_ledger_write` có `ket_qua = loi_tai_khoan` (ngân hàng từ chối), nối theo `trace_id`; đếm theo ngày, cảnh báo khi > 1% số lệnh hoàn trong ngày | Kiểm tra độ dài số tài khoản theo ngân hàng và tra tên chủ tài khoản, hỏi khách xác nhận trước khi tạo lệnh; sai thì yêu cầu nhập lại, không tạo lệnh | PM trợ lý hoàn phí |
| 20 | Hệ thống | Đối soát mỗi giờ trên `refund_ledger_write`: hơn 1 bản ghi `ok` cho cùng mã đơn; ngưỡng 0 ca, có 1 ca là kích luật dừng an toàn của pilot | Khoá chống trùng `idempotency_key` = mã đơn + loại hoàn; yêu cầu gửi lại khi đang xử lý thì gộp vào trace cũ và báo "đang xử lý"; thu hồi khoản hoàn thừa | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | `ticket_reopened` với `reason = so_tien` mà `audit_sample_checked` xác nhận số tiền đúng; tính theo tuần, cảnh báo khi > 0,5% số yêu cầu (mở lại hiện tại 3,97% trong phạm vi) | Mẫu tin nhắn luôn ghi cách tính và điều khoản: "30.000 đ × 50% (trễ 24–48 giờ) = 15.000 đ" | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | `handoff_to_staff` với `reason = thieu_du_lieu`, theo loại yêu cầu, theo tuần; cảnh báo khi tỉ lệ chuyển trong phạm vi pilot > 7% (gấp đôi mức 3,5% hiện tại) | Nhận diện chặng do hãng nước ngoài giao ngay ở bước đầu, chuyển nhân viên kèm tóm tắt, không chạy lại (quoc_te: lần 2 chỉ đúng 11,4%, lần 3 đúng 2,2%); đưa quoc_te ra khỏi pilot | PM trợ lý hoàn phí |
| 17 | Ngầm | Kiểm tra mẫu 100 đơn/tuần (`audit_sample_checked`) so với bảng giá hiện hành, ngưỡng > 1% đơn lệch; thêm cảnh báo khi phiên bản bảng giá ghi trong trace khác phiên bản hiện hành, ngưỡng 0 ca | Xoá bộ nhớ đệm khi có bảng giá mới; ghi `bang_gia_version` vào trace; tính lại và bù phần lệch cho 212 đơn | Kỹ sư trưởng agent |

### Ca dự phòng (dùng khi nhãn thống nhất khác loại dự kiến)

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed` với `ly_do = ma_khong_hop_le`; cảnh báo khi > 2% số yêu cầu mỗi ngày | Nhận diện mã đơn của sàn thương mại điện tử và tra sang mã vận đơn; không tra được thì hướng dẫn kèm ảnh chỗ lấy mã vận đơn | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát mỗi giờ: tin nhắn "đã hoàn" không có bản ghi `refund_ledger_write` `ok` cùng `trace_id`; ngưỡng 0 ca | Chỉ báo "đã hoàn" khi sổ cái trả `ok`; lỗi 503 sau 3 lần thì báo "đang xử lý" và chuyển nhân viên | Kỹ sư trưởng agent |
| 3 | Ngữ cảnh | `ticket_reopened` với `reason = chua_nhan_tien` trong khi sổ cái ghi hoàn vào ví `ok`; theo tuần, cảnh báo khi > 0,5% số yêu cầu | Hỏi khách muốn nhận qua ví LogiX hay ngân hàng trước khi hoàn; tin nhắn ghi rõ "đã hoàn vào ví LogiX" | Trưởng nhóm CSKH |
| 19 | Giới hạn hệ thống | `handoff_to_staff` với `reason = ngoai_12_thang`; đếm theo tuần, theo dõi thời gian nhân viên xử lý ca chuyển (đo bằng `staff_rework_completed`) | Giữ cách chuyển kèm tóm tắt; nói rõ ngay câu đầu là đơn quá 12 tháng | PM trợ lý hoàn phí |
| 12 | Ngầm | Tiền token + tool mỗi yêu cầu theo depot, theo ngày (từ `agent_run_completed`); cảnh báo khi một depot > 1,5× trung vị các depot 3 ngày liền (hiện cao nhất 1,05×) | Sửa tool tra đơn của D05 để trả đủ trường; giới hạn số lần gọi tool mỗi lần chạy | Kỹ sư trưởng agent |

### Liên kết sang CP4 và CP5
- Ca 20 và ca 7 là điều kiện của đề xuất "Go có điều kiện": phải sửa khoá chống trùng và đối soát sổ cái trước ngày bắt đầu pilot.
- Các event dùng ở đây (`refund_ledger_write`, `ticket_reopened`, `handoff_to_staff`, `audit_sample_checked`, `agent_run_completed`, `input_validation_failed`, `staff_rework_completed`) cần có trong danh sách event ở `chi_so.md`, mỗi event có `trace_id`.
