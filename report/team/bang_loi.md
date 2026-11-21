# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Phân loại theo nguyên nhân gốc, không theo nơi cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Nguyễn Thùy Lam (Lam đã xác nhận bộ nhãn này) · Người gắn nhãn 2: Mai Lâm Tấn Đạt (bộ nhãn do Đạt cung cấp).

> Hai bộ nhãn được ghi nhận như hai người đã cung cấp, theo nguyên tắc gắn theo nguyên nhân gốc. Lý do phân loại của người 2 ở mục bên dưới.

| Ca | Nhãn người 1 (Lam, đã xác nhận) | Nhãn người 2 | Trùng? | Nhãn thống nhất |
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

**Tỉ lệ đồng thuận:** 20/20 ca trùng = 100% (đạt ngưỡng 16/20).

## Quy tắc phân biệt cho các ca không trùng

Hai bộ nhãn trùng 20/20 nên không có ca lệch cần thống nhất lại; các quy tắc dưới đây ghi cách phân biệt cho những ca dễ lẫn. Nguyên tắc: lỗi do đầu vào của khách → Do người dùng; trợ lý vi phạm thiết kế/chính sách → Hệ thống; làm đúng nhưng kỳ vọng hoặc bối cảnh không khớp → Ngữ cảnh; vượt khả năng/dữ liệu → Giới hạn hệ thống; sai mà không ai nhận ra đến lúc kiểm tra → Ngầm.

- Ca 6 và 9: nguyên nhân gốc là khách chọn/nhập sai; trợ lý không hướng dẫn tốt là phần khắc phục.
- Ca 8 và 15: sai sót đã lộ ra trước khi gửi nên là Hệ thống, không phải Ngầm.
- Ca 12 và 17: sai lệch chỉ lộ qua kiểm tra/đối soát nên là Ngầm.
- Ca 13 và 19: ngoài phạm vi hoặc thiếu dữ liệu là Giới hạn hệ thống.
- Ca 18: số tiền đúng nhưng cách giải thích không đáp ứng kỳ vọng khách là Ngữ cảnh.

## Lý do phân loại của người 2

- Ca 1 (Do người dùng): Khách nhập số tài khoản thiếu hai chữ số; đầu vào sai dẫn đến ngân hàng từ chối lệnh hoàn.
- Ca 2 (Hệ thống): Trợ lý truyền sai loại hàng khi gọi tool, khiến đơn 28 kg bị tính theo hàng thường và hoàn thiếu.
- Ca 3 (Ngữ cảnh): Trợ lý hoàn về ví đúng thiết kế, nhưng khách kỳ vọng nhận tiền vào tài khoản ngân hàng.
- Ca 4 (Giới hạn hệ thống): LogiX không có dữ liệu chặng giao của hãng nước ngoài nên trợ lý không thể xác định trạng thái.
- Ca 5 (Ngầm): Hoàn thừa do bỏ qua mã giảm giá nhưng không khách nào báo, không có cảnh báo; chỉ phát hiện khi kiểm tra mẫu.
- Ca 6 (Do người dùng): Khách chọn nhầm loại yêu cầu “giao trễ” trong khi vấn đề thực tế là hàng bị vỡ.
- Ca 7 (Hệ thống): Bước ghi sổ cái thất bại nhưng trợ lý vẫn thông báo hoàn tiền thành công, không đúng kết quả thực thi.
- Ca 8 (Hệ thống): Trợ lý viện dẫn điều khoản không tồn tại trong chính sách hiện hành; số tiền đúng không làm căn cứ viện dẫn trở thành đúng.
- Ca 9 (Do người dùng): Khách nhập mã đơn của sàn thay vì mã vận đơn mà hệ thống yêu cầu. Việc trợ lý không hướng dẫn thêm là điểm cần cải thiện, không thay đổi nguồn gốc đầu vào sai.
- Ca 10 (Ngữ cảnh): Trợ lý từ chối đúng chính sách bất khả kháng, nhưng điều đó xung đột với kỳ vọng do cam kết “giao 24 giờ” trên ứng dụng tạo ra.
- Ca 11 (Giới hạn hệ thống): Tin nhắn thoại là dạng đầu vào trợ lý không xử lý được.
- Ca 12 (Ngầm): Trợ lý vẫn trả kết quả đúng nhưng gọi tool nhiều lần làm chi phí token tăng gấp ba trong ba tuần mà không ai nhận ra.
- Ca 13 (Giới hạn hệ thống): Hoàn phí bảo hiểm của đối tác nằm ngoài phạm vi trợ lý. Câu trả lời chung chung là cách xử lý giới hạn chưa phù hợp.
- Ca 14 (Do người dùng): Khách bấm nhầm xác nhận đã nhận tiền, khiến yêu cầu bị đóng.
- Ca 15 (Hệ thống): Trợ lý tính hoàn 100% thay vì mức 50% theo chính sách; nhân viên đã phát hiện trước khi gửi.
- Ca 16 (Ngữ cảnh): Trợ lý làm đúng thiết kế “gửi ngay khi xong”, nhưng gửi lúc 2:14 sáng không phù hợp hoàn cảnh của khách.
- Ca 17 (Ngầm): Trợ lý dùng bảng giá cũ gây lệch tiền trên 212 đơn, kéo dài chín ngày mà không có khách mở lại yêu cầu.
- Ca 18 (Ngữ cảnh): Số tiền hoàn đúng, nhưng thiếu cách tính khiến khách hiểu là hoàn thiếu.
- Ca 19 (Giới hạn hệ thống): Yêu cầu cần dữ liệu từ 14 tháng trước, vượt quá phạm vi truy cập 12 tháng của trợ lý.
- Ca 20 (Hệ thống): Thiếu khóa chống trùng khiến trợ lý hoàn tiền hai lần cho cùng một đơn; khách gửi lại yêu cầu không phải lý do hợp lệ để hoàn trùng.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Ghi `input_validation_failed`; cảnh báo nếu vượt 2% yêu cầu/ngày | Nhận diện mã sàn và tra sang mã vận đơn; nếu không tra được thì hướng dẫn kèm ảnh | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát mỗi giờ: thông báo “đã hoàn” không có ghi sổ cái `ok` cùng `trace_id`; ngưỡng 0 ca | Chỉ báo hoàn thành khi sổ cái trả `ok`; lỗi 503 sau 3 lần thì chuyển nhân viên và báo đang xử lý | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Theo tuần đếm yêu cầu mở lại do số tiền nhưng kiểm tra thấy số tiền đúng | Hiển thị phép tính, ví dụ 30.000 đ × 50% = 15.000 đ | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Theo dõi event `handoff_to_staff` với `reason=thieu_du_lieu`, phân theo loại yêu cầu | Chuyển nhân viên kèm tóm tắt; không đưa yêu cầu quốc tế vào phạm vi pilot | PM trợ lý hoàn phí |
| 17 | Ngầm | Kiểm tra 100 đơn/tuần với bảng giá hiện hành; cảnh báo nếu trên 1% đơn lệch | Xoá cache khi bảng giá đổi và ghi phiên bản bảng giá vào trace | Kế toán trưởng |
