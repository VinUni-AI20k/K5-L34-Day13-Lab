# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Nguyễn Văn Huy · Người gắn nhãn 2: Phạm Công Dũng (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Hệ thống | Không | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Hệ thống | Không | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 18 / 20 = 90%

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- **Ca 6 (Do người dùng vs Hệ thống → thống nhất: Do người dùng):** Gắn nhãn theo nguyên nhân gốc là khách chọn sai danh mục ("Hoàn phí giao trễ" trong khi mô tả hàng bị vỡ), còn việc trợ lý chưa đối chiếu chéo nội dung với danh mục là phần cải thiện ở cột khắc phục.
- **Ca 13 (Giới hạn hệ thống vs Hệ thống → thống nhất: Giới hạn hệ thống):** Yêu cầu hoàn phí bảo hiểm của đối tác nằm ngoài phạm vi thiết kế của trợ lý nên gốc lỗi là Giới hạn hệ thống, kể cả khi trợ lý phản hồi giới hạn đó chưa rõ ràng.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed` (kèm `trace_id`); cảnh báo khi vượt ngưỡng 2% tổng số yêu cầu mỗi ngày | Nhận diện định dạng mã đơn sàn TMĐT và tự tra sang mã vận đơn LogiX; nếu không tra được thì hiện hướng dẫn kèm ảnh vị trí mã vận đơn | PM trợ lý hoàn phí |
| 7 | Hệ thống | Job đối soát mỗi giờ giữa event tin nhắn báo "đã hoàn" và event `refund_ledger_write` có `ket_qua == 'ok'` cùng `trace_id`; ngưỡng cảnh báo: > 0 ca lệch | Chỉ gửi thông báo "đã hoàn tiền thành công" sau khi API sổ cái trả về `ok`; nếu lỗi 503 sau 3 lần thử thì báo "đang xử lý" và chuyển nhân viên (`handoff_to_staff`) | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Thống kê hằng tuần tỉ lệ event `ticket_reopened` có `reason == 'thac_mac_so_tien'` nhưng kiểm tra sổ cái thấy số tiền hoàn đúng chính sách; ngưỡng > 1% đơn hoàn | Cập nhật mẫu tin nhắn hoàn tiền luôn hiển thị rõ công thức và cách tính (ví dụ: `Phí giao 30.000 đ × 50% (trễ 24–48h) = 15.000 đ`) | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` với `reason == 'thieu_du_lieu'` (kèm `trace_id`), thống kê theo từng loại yêu cầu (`loai`) mỗi ngày; cảnh báo khi vượt 10% ở một loại | Giữ cơ chế chuyển nhân viên kèm bản tóm tắt thông tin đã thu thập; loại hoàn toàn phân khúc `quoc_te` (1,88×, thành công 27,3%, `simulated`) khỏi phạm vi pilot | PM trợ lý hoàn phí |
| 17 | Ngầm | Event `audit_sample_checked` kiểm tra mẫu ngẫu nhiên 100 đơn hoàn/tuần đối chiếu với bảng giá hiện hành; ngưỡng cảnh báo khi có ≥ 1% đơn lệch số tiền | Tự động xoá bộ nhớ đệm (invalidate cache) ngay khi bảng giá cập nhật và bắt buộc ghi `pricing_table_version` vào mọi `trace_id` để truy vết | Kế toán trưởng |
