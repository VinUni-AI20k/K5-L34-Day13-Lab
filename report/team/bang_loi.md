# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Đoàn Xuân Duy Bảo · Người gắn nhãn 2: Vũ Tiến Hùng *(chờ gắn nhãn độc lập)* (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | ... | ... | ... |
| 2 | Hệ thống | ... | ... | ... |
| 3 | Ngữ cảnh | ... | ... | ... |
| 4 | Giới hạn hệ thống | ... | ... | ... |
| 5 | Ngầm | ... | ... | ... |
| 6 | Do người dùng | ... | ... | ... |
| 7 | Hệ thống | ... | ... | ... |
| 8 | Hệ thống | ... | ... | ... |
| 9 | Do người dùng | ... | ... | ... |
| 10 | Ngữ cảnh | ... | ... | ... |
| 11 | Giới hạn hệ thống | ... | ... | ... |
| 12 | Ngầm | ... | ... | ... |
| 13 | Giới hạn hệ thống | ... | ... | ... |
| 14 | Do người dùng | ... | ... | ... |
| 15 | Hệ thống | ... | ... | ... |
| 16 | Ngữ cảnh | ... | ... | ... |
| 17 | Ngầm | ... | ... | ... |
| 18 | Ngữ cảnh | ... | ... | ... |
| 19 | Giới hạn hệ thống | ... | ... | ... |
| 20 | Hệ thống | ... | ... | ... |

**Tỉ lệ đồng thuận:** ... / 20 = ...% *(chờ so nhãn với Hùng)*

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- *(Chờ so nhãn với Hùng)*

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội". *(Bản nháp của Bảo, sẽ rà lại sau khi so nhãn với Hùng)*

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed`; cảnh báo khi vượt 2% tổng yêu cầu/ngày | Nhận diện định dạng mã đơn sàn TMĐT để tra sang mã vận đơn; nếu không tra được thì hiển thị hướng dẫn kèm ảnh minh hoạ | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát mỗi giờ giữa tin nhắn "đã hoàn" và event `refund_ledger_write` có `ket_qua = ok` cùng `trace_id`; ngưỡng 0 ca lệch | Chỉ gửi thông báo "đã hoàn" khi sổ cái trả `ok`; sau 3 lần lỗi 503 thì báo "đang xử lý" và phát `handoff_to_staff` | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Tỉ lệ `ticket_reopened` với lý do thiếu tiền nhưng kiểm tra sổ cái thấy đúng chính sách, tổng hợp theo tuần; cảnh báo khi vượt 1% yêu cầu tuần | Cập nhật mẫu tin nhắn luôn hiển thị phép tính chi tiết (ví dụ: `30.000 đ × 50% = 15.000 đ`) | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` với `reason = thieu_du_lieu_hang_ngoai` theo loại yêu cầu, theo dõi hằng ngày | Giữ cơ chế chuyển nhân viên kèm tóm tắt; loại nhóm `quoc_te` khỏi phạm vi pilot | PM trợ lý hoàn phí |
| 17 | Ngầm | Kiểm tra mẫu ngẫu nhiên 100 đơn/tuần (`audit_sample_checked`) đối chiếu bảng giá hiện hành; ngưỡng cảnh báo ≥ 1% đơn lệch | Xoá bộ nhớ đệm khi cập nhật bảng giá mới và ghi `price_table_version` vào mọi `trace_id` | Kế toán trưởng |
