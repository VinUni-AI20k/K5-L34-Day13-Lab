# Phiếu gắn nhãn độc lập 20 ca lỗi — Hùng (CP3)

Nguồn: `lab/docs/Ngay13_Lab13_De_bai_hoc_vien.docx`, mục "Hai mươi ca lỗi". Phiếu để trống cột nhãn: **Hùng tự gắn, trong 8 phút, không hỏi Bảo, không xem nhãn của Bảo**. Giữ nguyên bộ nhãn gốc (không sửa sau khi so) để làm bằng chứng cho `bang_loi.md`.

Năm loại (khung Google PAIR), gắn theo **nguyên nhân gốc**, không theo chỗ cần sửa:

| Loại | Cách hiểu ngắn |
| --- | --- |
| Do người dùng | Người dùng nhập hoặc chọn sai |
| Hệ thống | Agent làm sai thiết kế hoặc chính sách (lỗi đã lộ ra) |
| Ngữ cảnh | Kết quả đúng nhưng không phù hợp hoàn cảnh |
| Giới hạn hệ thống | Thiếu dữ liệu hoặc yêu cầu ngoài khả năng xử lý |
| Ngầm | Có sai nhưng chỉ phát hiện khi kiểm tra, đối soát |

| Ca | Mô tả | Nhãn của Hùng |
| --: | --- | --- |
| 1 | Khách nhập số tài khoản nhận hoàn tiền thiếu hai chữ số. Trợ lý tạo lệnh hoàn, ngân hàng trả về lỗi. | |
| 2 | Kiện nội địa 28 kg. Trợ lý gọi tool tra bảng giá với tham số hàng thường thay vì hàng nặng, hoàn thiếu 45.000 đ. Khách mở lại sau 2 ngày. | |
| 3 | Theo thiết kế, trợ lý hoàn tiền về ví LogiX trong 5 phút. Khách chờ tiền về tài khoản ngân hàng và báo "chưa được hoàn". | |
| 4 | Khách yêu cầu hoàn phí cho chặng do hãng nước ngoài giao. LogiX không có dữ liệu chặng này. Trợ lý nói không xác định được trạng thái và chuyển cho nhân viên. | |
| 5 | Kiểm tra mẫu cuối tuần thấy 14 đơn có mã giảm giá bị hoàn theo giá trước giảm, thừa trung bình 12.000 đ mỗi đơn. Không khách nào báo, không cảnh báo nào kích. | |
| 6 | Khách chọn mục "Hoàn phí giao trễ" nhưng nội dung mô tả hàng bị vỡ. Trợ lý xử lý theo luồng giao trễ và từ chối vì đơn giao đúng hạn. | |
| 7 | API sổ cái trả lỗi 503 ở bước ghi hoàn tiền. Trợ lý thử lại 3 lần rồi vẫn báo khách "đã hoàn tiền thành công". | |
| 8 | Trợ lý dẫn "Điều 7.2 chính sách hoàn phí" làm căn cứ. Bản chính sách hiện hành không có điều 7.2. Số tiền hoàn vẫn đúng. | |
| 9 | Khách nhập mã đơn của sàn thương mại điện tử thay vì mã vận đơn. Trợ lý báo "mã không hợp lệ" rồi dừng, không gợi ý gì. | |
| 10 | Đơn giao trễ do bão. Trợ lý từ chối hoàn theo điều khoản bất khả kháng, đúng chính sách. Khách thấy vô lý vì ứng dụng vẫn hiện "cam kết giao 24 giờ". | |
| 11 | Khách gửi tin nhắn thoại 40 giây. Trợ lý không xử lý được âm thanh, trả lời "vui lòng nhập bằng chữ". | |
| 12 | Tool tra đơn của depot D05 trả thiếu một trường. Trợ lý vẫn ra kết quả đúng sau nhiều lần gọi, nên tiền token của D05 gấp 3 lần depot khác suốt 3 tuần mà không ai thấy. | |
| 13 | Khách hỏi hoàn phí bảo hiểm hàng hoá, sản phẩm của công ty bảo hiểm đối tác, ngoài phạm vi trợ lý. Trợ lý trả lời chung chung về phí vận chuyển, không nói rõ là mình không xử lý được. | |
| 14 | Khách bấm nhầm "Xác nhận đã nhận tiền" khi chưa nhận. Yêu cầu bị đóng. | |
| 15 | Đơn trễ 26 giờ. Chính sách: trễ 24–48 giờ hoàn 50%. Trợ lý tính hoàn 100%. Nhân viên xem lại bắt được trước khi gửi. | |
| 16 | Theo thiết kế "gửi ngay khi xong", trợ lý gửi thông báo hoàn tiền qua Zalo lúc 2:14 sáng. Khách phản ánh bị làm phiền. | |
| 17 | Bảng giá đổi từ ngày 01/11 nhưng trợ lý vẫn dùng bản cũ trong bộ nhớ đệm cho đơn dưới 2 kg. Lệch 1.000–2.000 đ mỗi đơn, 212 đơn trong 9 ngày, không ai mở lại. | |
| 18 | Trợ lý tính đúng: phí giao 30.000 đ, hoàn 50%. Tin nhắn chỉ ghi "Đã hoàn 15.000 đ", không kèm cách tính. Khách cho là hoàn thiếu và mở lại yêu cầu. | |
| 19 | Khách yêu cầu hoàn phí cho đơn từ 14 tháng trước. Trợ lý chỉ truy cập được dữ liệu 12 tháng. Trợ lý nói rõ không tra được và chuyển cho nhân viên kèm tóm tắt. | |
| 20 | Khách gửi lại yêu cầu sau 10 phút vì chưa thấy phản hồi. Trợ lý hoàn hai lần cho cùng một đơn vì lệnh thứ hai không có khoá chống trùng. | |

Sau khi so nhãn với Bảo: đồng thuận ___ / 20 (mục tiêu ≥ 16/20). Ca không trùng cần một câu quy tắc phân biệt.

---

## Bộ nhãn gốc lần 1 của Hùng (chưa so với Bảo, không sửa sau khi so)

| Ca | Nhãn | Ca | Nhãn |
| --: | --- | --: | --- |
| 1 | Do người dùng | 11 | Giới hạn hệ thống |
| 2 | Hệ thống | 12 | Ngầm |
| 3 | Hệ thống | 13 | Hệ thống |
| 4 | Giới hạn hệ thống | 14 | Ngầm |
| 5 | Ngầm | 15 | Hệ thống |
| 6 | Ngữ cảnh | 16 | Ngữ cảnh |
| 7 | Hệ thống | 17 | Hệ thống |
| 8 | Ngầm | 18 | Ngữ cảnh |
| 9 | Ngữ cảnh | 19 | Giới hạn hệ thống |
| 10 | Ngữ cảnh | 20 | Giới hạn hệ thống |

Phân bố: Hệ thống 6 · Ngữ cảnh 5 · Ngầm 4 · Giới hạn hệ thống 4 · Do người dùng 1 (đủ năm loại).
