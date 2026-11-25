# Bảng lỗi và cách khắc phục · Nhiệm vụ C

## Hai bộ nhãn độc lập

Người gắn nhãn 1 · Trương Văn Hải. Người gắn nhãn 2 · Nguyễn Xuân Khánh Linh. Mỗi người ghi riêng đủ 20 nhãn trong 8 phút rồi mới nhập vào cột của mình và so kết quả.

Chọn nhãn theo nguyên nhân gốc. Mỗi ca dùng một trong năm nhãn sau.

- **Do người dùng** · Người dùng nhập sai hoặc chọn sai.
- **Hệ thống** · Trợ lý trả lời sai hoặc làm sai so với thiết kế hoặc chính sách.
- **Ngữ cảnh** · Trợ lý làm đúng thiết kế nhưng giả định trong thiết kế lệch với hoàn cảnh của người dùng.
- **Giới hạn hệ thống** · Yêu cầu ngoài phạm vi, thiếu dữ liệu cần thiết hoặc có dạng đầu vào chưa hỗ trợ.
- **Ngầm** · Lỗi chưa được người dùng hay hệ thống nhận ra và chỉ lộ khi kiểm tra.

<details>
<summary>20 tình huống trích từ đề bài</summary>

| Ca | Mô tả |
| --: | --- |
| 1 | Khách nhập số tài khoản nhận hoàn tiền thiếu hai chữ số. Trợ lý tạo lệnh hoàn, ngân hàng trả về lỗi. |
| 2 | Kiện nội địa 28 kg. Trợ lý gọi tool tra bảng giá với tham số hàng thường thay vì hàng nặng, hoàn thiếu 45.000 đ. Khách mở lại sau 2 ngày. |
| 3 | Theo thiết kế, trợ lý hoàn tiền về ví LogiX trong 5 phút. Khách chờ tiền về tài khoản ngân hàng và báo “chưa được hoàn”. |
| 4 | Khách yêu cầu hoàn phí cho chặng do hãng nước ngoài giao. LogiX không có dữ liệu chặng này. Trợ lý nói không xác định được trạng thái và chuyển cho nhân viên. |
| 5 | Kiểm tra mẫu cuối tuần thấy 14 đơn có mã giảm giá bị hoàn theo giá trước giảm, thừa trung bình 12.000 đ mỗi đơn. Không khách nào báo, không cảnh báo nào kích. |
| 6 | Khách chọn mục “Hoàn phí giao trễ” nhưng nội dung mô tả hàng bị vỡ. Trợ lý xử lý theo luồng giao trễ và từ chối vì đơn giao đúng hạn. |
| 7 | API sổ cái trả lỗi 503 ở bước ghi hoàn tiền. Trợ lý thử lại 3 lần rồi vẫn báo khách “đã hoàn tiền thành công”. |
| 8 | Trợ lý dẫn “Điều 7.2 chính sách hoàn phí” làm căn cứ. Bản chính sách hiện hành không có điều 7.2. Số tiền hoàn vẫn đúng. |
| 9 | Khách nhập mã đơn của sàn thương mại điện tử thay vì mã vận đơn. Trợ lý báo “mã không hợp lệ” rồi dừng, không gợi ý gì. |
| 10 | Đơn giao trễ do bão. Trợ lý từ chối hoàn theo điều khoản bất khả kháng, đúng chính sách. Khách thấy vô lý vì ứng dụng vẫn hiện “cam kết giao 24 giờ”. |
| 11 | Khách gửi tin nhắn thoại 40 giây. Trợ lý không xử lý được âm thanh, trả lời “vui lòng nhập bằng chữ”. |
| 12 | Tool tra đơn của depot D05 trả thiếu một trường. Trợ lý vẫn ra kết quả đúng sau nhiều lần gọi, nên tiền token của D05 gấp 3 lần depot khác suốt 3 tuần mà không ai thấy. |
| 13 | Khách hỏi hoàn phí bảo hiểm hàng hoá, sản phẩm của công ty bảo hiểm đối tác, ngoài phạm vi trợ lý. Trợ lý trả lời chung chung về phí vận chuyển, không nói rõ là mình không xử lý được. |
| 14 | Khách bấm nhầm “Xác nhận đã nhận tiền” khi chưa nhận. Yêu cầu bị đóng. |
| 15 | Đơn trễ 26 giờ. Chính sách: trễ 24–48 giờ hoàn 50%. Trợ lý tính hoàn 100%. Nhân viên xem lại bắt được trước khi gửi. |
| 16 | Theo thiết kế “gửi ngay khi xong”, trợ lý gửi thông báo hoàn tiền qua Zalo lúc 2:14 sáng. Khách phản ánh bị làm phiền. |
| 17 | Bảng giá đổi từ ngày 01/11 nhưng trợ lý vẫn dùng bản cũ trong bộ nhớ đệm cho đơn dưới 2 kg. Lệch 1.000–2.000 đ mỗi đơn, 212 đơn trong 9 ngày, không ai mở lại. |
| 18 | Trợ lý tính đúng: phí giao 30.000 đ, hoàn 50%. Tin nhắn chỉ ghi “Đã hoàn 15.000 đ”, không kèm cách tính. Khách cho là hoàn thiếu và mở lại yêu cầu. |
| 19 | Khách yêu cầu hoàn phí cho đơn từ 14 tháng trước. Trợ lý chỉ truy cập được dữ liệu 12 tháng. Trợ lý nói rõ không tra được và chuyển cho nhân viên kèm tóm tắt. |
| 20 | Khách gửi lại yêu cầu sau 10 phút vì chưa thấy phản hồi. Trợ lý hoàn hai lần cho cùng một đơn vì lệnh thứ hai không có khoá chống trùng. |

Nguồn [Đề bài Lab 13, mục Hai mươi ca lỗi](../../docs/Ngay13_Lab13_De_bai_hoc_vien.docx).

</details>

| Ca | Nhãn Trương Văn Hải | Nhãn Nguyễn Xuân Khánh Linh | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | | Do người dùng | | |
| 2 | | Hệ thống | | |
| 3 | | Ngữ cảnh | | |
| 4 | | Giới hạn hệ thống | | |
| 5 | | Ngầm | | |
| 6 | | Ngữ cảnh | | |
| 7 | | Hệ thống | | |
| 8 | | Ngầm | | |
| 9 | | Do người dùng | | |
| 10 | | Ngữ cảnh | | |
| 11 | | Giới hạn hệ thống | | |
| 12 | | Ngầm | | |
| 13 | | Giới hạn hệ thống | | |
| 14 | | Do người dùng | | |
| 15 | | Hệ thống | | |
| 16 | | Ngữ cảnh | | |
| 17 | | Ngầm | | |
| 18 | | Ngữ cảnh | | |
| 19 | | Giới hạn hệ thống | | |
| 20 | | Hệ thống | | |

**Tỉ lệ đồng thuận** · Linh đã ghi đủ 20 nhãn, chờ bộ nhãn độc lập của Hải. Lấy số ca trùng chia 20 rồi nhân 100. Cần ít nhất 16/20 ca để đạt 80%.

## Quy tắc phân biệt cho các ca không trùng

Sau khi so, mỗi ca khác nhãn ghi một quy tắc dựa trên dấu hiệu trong tình huống. Nếu trùng dưới 16/20, ghi định nghĩa đã làm rõ. Giữ hai cột nhãn ban đầu để đối chiếu.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Biện pháp, event và ngưỡng dưới đây là gợi ý. Sau khi chốt nhãn, chọn một ca cho mỗi loại rồi chỉnh biện pháp theo dấu hiệu của ca đó. Mỗi event gắn `trace_id` để truy lại yêu cầu.

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| Chờ chọn | Do người dùng | Đếm `input_validation_failed` theo trường mỗi ngày. Chặn ngay khi 1 dữ liệu bắt buộc không hợp lệ. | Hiển thị lỗi tại trường, đưa ví dụ nhập đúng và giữ các thông tin đã điền. | Kỹ sư giao diện |
| Chờ chọn | Hệ thống | Đối chiếu số tiền đề xuất với bộ tính theo chính sách trước mỗi lệnh hoàn. Kích hoạt `refund_policy_mismatch` khi lệch bất kỳ số tiền nào. | Tạm giữ lệnh, chuyển nhân viên xác nhận và thêm ca vào bộ kiểm thử chính sách. | Kỹ sư trợ lý hoàn phí |
| Chờ chọn | Ngữ cảnh | Theo dõi `ticket_reopened` do khách hiểu khác thông báo. Rà nội dung khi có từ 3 ca cùng lý do trong 7 ngày. | Nêu rõ điều kiện và kết quả dự kiến ở bước xác nhận, sau đó thử lại với nhân viên CSKH. | PM trợ lý hoàn phí |
| Chờ chọn | Giới hạn hệ thống | Ghi `handoff_to_staff` theo lý do. Kiểm mỗi ngày xem có yêu cầu ngoài phạm vi nào thiếu bản tóm tắt. | Nêu rõ giới hạn với khách và chuyển nhân viên kèm dữ liệu đã thu thập. | Trưởng nhóm CSKH |
| Chờ chọn | Ngầm | Kiểm tra mẫu 50 giao dịch/tuần qua `audit_sample_checked`. Mở điều tra ngay khi có 1 giao dịch lệch. | Đối soát lại các giao dịch cùng quy tắc và sửa kết quả theo sổ cái sau khi xác minh. | Kế toán trưởng |
