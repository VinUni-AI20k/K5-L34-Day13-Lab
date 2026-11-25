# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Trần Xuân Lộc (P3) · Người gắn nhãn 2: Lê Danh Giang (P4) (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 20 / 20 = 100% (đạt ngưỡng ≥ 80%)

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- Không có ca không trùng (đồng thuận 20/20 = 100%); nhóm ghi nhận thêm 5 quy tắc phân biệt cho các ca dễ nhầm lẫn:
- **Ca 6, 9 là Do người dùng (không phải Hệ thống):** nguyên nhân gốc là khách chọn sai mục hoặc nhập sai mã vận đơn; việc trợ lý chưa gợi ý tốt nằm ở cột khắc phục.
- **Ca 8, 15 là Hệ thống (không phải Ngầm):** lỗi đã lộ ra rõ ràng (trích dẫn điều khoản không tồn tại hiển thị ra ngoài, nhân viên bắt được khi xem lại); nhãn Ngầm chỉ dùng khi không ai nhận ra cho tới khi kiểm tra mẫu hoặc đối soát chi phí.
- **Ca 12 là Ngầm:** câu trả lời vẫn đúng nhưng phát sinh lỗi ngầm về chi phí (token depot D05 gấp 3 lần suốt 3 tuần không ai biết).
- **Ca 13 là Giới hạn hệ thống:** yêu cầu bảo hiểm nằm ngoài phạm vi trợ lý, kể cả khi trợ lý trả lời xử lý tình huống đó kém.
- **Ca 18 là Ngữ cảnh:** tính tiền đúng 100% chính sách (30.000 đ × 50% = 15.000 đ), chỉ giả định "khách tự hiểu cách tính" không khớp kỳ vọng thực tế.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed` (lỗi định dạng mã vận đơn); cảnh báo khi tỉ lệ vượt 2% tổng yêu cầu/ngày | Tự động nhận diện định dạng mã sàn TMĐT để tra chéo sang mã vận đơn LogiX; nếu không tra được thì hiện hướng dẫn kèm ảnh vị trí mã vận đơn | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát tự động mỗi giờ giữa tin nhắn "đã hoàn tiền" và event `refund_ledger_write` có `ket_qua = ok` cùng `trace_id`; ngưỡng cảnh báo > 0 ca | Chỉ cho phép gửi thông báo "đã hoàn tiền" khi nhận được `ok` từ sổ cái; nếu lỗi 503 sau 3 lần thử thì báo "đang xử lý" và tạo event `handoff_to_staff` | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Theo dõi hằng tuần tỉ lệ `ticket_reopened` với lý do "sai số tiền" nhưng kiểm tra lại thấy số tiền đúng chính sách; ngưỡng cảnh báo > 1% số đơn hoàn | Cập nhật mẫu tin nhắn trả lời luôn hiển thị rõ công thức tính tiền (ví dụ: `30.000 đ × 50% = 15.000 đ`) và dẫn chiếu điều khoản áp dụng | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` với `reason = thieu_du_lieu_quoc_te`, thống kê theo loại yêu cầu hằng tuần; ngưỡng theo dõi > 5% tổng yêu cầu | Giữ luồng chuyển nhân viên kèm tóm tắt ngữ cảnh; loại nhóm `quoc_te` ra khỏi phạm vi pilot và định tuyến thẳng sang nhân viên ngay từ đầu | PM trợ lý hoàn phí |
| 17 | Ngầm | Event `audit_sample_checked`: kế toán kiểm tra mẫu ngẫu nhiên 100 đơn/tuần đối chiếu bảng giá hiện hành; ngưỡng cảnh báo ≥ 1% đơn lệch tiền | Thiết lập cơ chế tự động xoá bộ nhớ đệm (cache invalidation) ngay khi phát hành bảng giá mới và lưu `pricing_version` vào mọi `trace_id` | Kế toán trưởng |
