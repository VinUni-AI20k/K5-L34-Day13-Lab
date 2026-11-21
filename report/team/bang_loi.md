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
| 1 | Do người dùng | Event `bank_account_rejected` (ngân hàng trả lỗi sai số tài khoản, có `trace_id`). Dashboard đếm theo ngày; cảnh báo khi vượt 1% số lệnh hoàn/ngày | Trước khi tạo lệnh: kiểm độ dài và checksum số tài khoản, gọi API tra tên chủ tài khoản và cho khách xác nhận. Sai thì yêu cầu nhập lại, chưa tạo lệnh | PM trợ lý hoàn phí |
| 7 | Hệ thống | Event `refund_reported_success` không có `ledger_write_ok` cùng `trace_id`. Đối soát tự động mỗi giờ; ngưỡng **0** ca (1 ca là cảnh báo ngay) | Chỉ báo "đã hoàn tiền" khi sổ cái xác nhận ghi thành công. Lỗi 503 sau 3 lần thử thì báo "đang xử lý", đưa vào hàng đợi thử lại và chuyển nhân viên nếu quá 30 phút | Kỹ sư backend phụ trách tích hợp sổ cái |
| 3 | Ngữ cảnh | Event `refund_reopened` với lý do "chưa nhận tiền" trong khi `refund_channel = vi_logix` và đã ghi thành công. Báo cáo theo tuần; cảnh báo khi vượt 3% số yêu cầu hoàn về ví | Hỏi khách chọn kênh nhận (ví LogiX hoặc ngân hàng) trước khi hoàn. Tin nhắn ghi rõ "Đã hoàn X đ vào ví LogiX" kèm hướng dẫn rút về ngân hàng | Designer trải nghiệm hội thoại (UX writer) |
| ... | Giới hạn hệ thống | ... | ... | ... |
| ... | Ngầm | ... | ... | ... |
