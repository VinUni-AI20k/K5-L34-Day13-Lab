# Nháp bộ nhãn 1 · Nhiệm vụ C (người gắn nhãn 1)

Gắn độc lập trong 8 phút, không trao đổi với người gắn nhãn 2. Gắn theo **nguyên nhân gốc**, không theo chỗ cần sửa. Sau khi đã so nhãn thì không sửa file này; chép cột "Nhãn" sang cột "Nhãn người 1" trong `bang_loi.md`.

Bắt đầu: 14:45 · Kết thúc: 15:05

## Năm loại (Google PAIR)

| Loại | Nghĩa là |
| --- | --- |
| Do người dùng | Người dùng nhập sai hoặc chọn sai |
| Hệ thống | Hệ thống trả lời sai hoặc làm sai so với thiết kế và chính sách |
| Ngữ cảnh | Hệ thống làm đúng thiết kế nhưng người dùng thấy là sai, vì giả định của hệ thống không khớp hoàn cảnh của họ |
| Giới hạn hệ thống | Hệ thống không thể trả lời, do thiếu dữ liệu, ngoài phạm vi, hoặc dạng đầu vào không xử lý được |
| Ngầm | Có sai nhưng cả người dùng lẫn hệ thống đều không nhận ra |

## Bộ nhãn

| Ca | Mô tả | Nhãn | Lý do ngắn (nguyên nhân gốc) |
| --: | --- | --- | --- |
| 1 | Khách nhập số tài khoản nhận hoàn tiền thiếu hai chữ số. Trợ lý tạo lệnh hoàn, ngân hàng trả về lỗi. | Do người dùng | Khách nhập sai số tài khoản; trợ lý làm đúng theo dữ liệu được nhập. |
| 2 | Kiện nội địa 28 kg. Trợ lý gọi tool tra bảng giá với tham số hàng thường thay vì hàng nặng, hoàn thiếu 45.000 đ. Khách mở lại sau 2 ngày. | Hệ thống | Trợ lý gọi tool sai tham số (hàng thường thay vì hàng nặng), tính sai so với bảng giá. |
| 3 | Theo thiết kế, trợ lý hoàn tiền về ví LogiX trong 5 phút. Khách chờ tiền về tài khoản ngân hàng và báo "chưa được hoàn". | Ngữ cảnh | Hoàn về ví đúng thiết kế, nhưng giả định không khớp kỳ vọng của khách (chờ tiền về ngân hàng). |
| 4 | Khách yêu cầu hoàn phí cho chặng do hãng nước ngoài giao. LogiX không có dữ liệu chặng này. Trợ lý nói không xác định được trạng thái và chuyển cho nhân viên. | Giới hạn hệ thống | Thiếu dữ liệu chặng hãng nước ngoài; trợ lý không thể tra được. |
| 5 | Kiểm tra mẫu cuối tuần thấy 14 đơn có mã giảm giá bị hoàn theo giá trước giảm, thừa trung bình 12.000 đ mỗi đơn. Không khách nào báo, không cảnh báo nào kích. | Ngầm | Hoàn thừa sai nhưng không khách nào báo, không cảnh báo nào kích; chỉ lộ qua kiểm tra mẫu. |
| 6 | Khách chọn mục "Hoàn phí giao trễ" nhưng nội dung mô tả hàng bị vỡ. Trợ lý xử lý theo luồng giao trễ và từ chối vì đơn giao đúng hạn. | Do người dùng | Khách chọn sai mục yêu cầu (giao trễ thay vì hàng vỡ); trợ lý xử lý đúng luồng khách chọn. |
| 7 | API sổ cái trả lỗi 503 ở bước ghi hoàn tiền. Trợ lý thử lại 3 lần rồi vẫn báo khách "đã hoàn tiền thành công". | Hệ thống | Ghi sổ cái thất bại mà trợ lý vẫn báo thành công — làm sai so với thiết kế. |
| 8 | Trợ lý dẫn "Điều 7.2 chính sách hoàn phí" làm căn cứ. Bản chính sách hiện hành không có điều 7.2. Số tiền hoàn vẫn đúng. | Hệ thống | Trợ lý bịa căn cứ chính sách không tồn tại (điều 7.2), dù số tiền đúng. |
| 9 | Khách nhập mã đơn của sàn thương mại điện tử thay vì mã vận đơn. Trợ lý báo "mã không hợp lệ" rồi dừng, không gợi ý gì. | Do người dùng | Khách nhập nhầm loại mã (mã đơn sàn thay vì mã vận đơn). |
| 10 | Đơn giao trễ do bão. Trợ lý từ chối hoàn theo điều khoản bất khả kháng, đúng chính sách. Khách thấy vô lý vì ứng dụng vẫn hiện "cam kết giao 24 giờ". | Ngữ cảnh | Từ chối đúng chính sách bất khả kháng, nhưng khách dựa vào cam kết 24 giờ hiển thị trên ứng dụng. |
| 11 | Khách gửi tin nhắn thoại 40 giây. Trợ lý không xử lý được âm thanh, trả lời "vui lòng nhập bằng chữ". | Giới hạn hệ thống | Dạng đầu vào (âm thanh) trợ lý không xử lý được. |
| 12 | Tool tra đơn của depot D05 trả thiếu một trường. Trợ lý vẫn ra kết quả đúng sau nhiều lần gọi, nên tiền token của D05 gấp 3 lần depot khác suốt 3 tuần mà không ai thấy. | Ngầm | Lỗi tool làm tăng chi phí token gấp 3 suốt 3 tuần, kết quả vẫn đúng nên không ai nhận ra. |
| 13 | Khách hỏi hoàn phí bảo hiểm hàng hoá, sản phẩm của công ty bảo hiểm đối tác, ngoài phạm vi trợ lý. Trợ lý trả lời chung chung về phí vận chuyển, không nói rõ là mình không xử lý được. | Giới hạn hệ thống | Bảo hiểm của đối tác nằm ngoài phạm vi trợ lý (cách xử lý mập mờ là chỗ cần sửa, không phải gốc). |
| 14 | Khách bấm nhầm "Xác nhận đã nhận tiền" khi chưa nhận. Yêu cầu bị đóng. | Do người dùng | Khách bấm nhầm nút xác nhận đã nhận tiền. |
| 15 | Đơn trễ 26 giờ. Chính sách: trễ 24–48 giờ hoàn 50%. Trợ lý tính hoàn 100%. Nhân viên xem lại bắt được trước khi gửi. | Hệ thống | Trợ lý áp sai mức hoàn so với chính sách (100% thay vì 50%); đã bị bắt nên không phải ngầm. |
| 16 | Theo thiết kế "gửi ngay khi xong", trợ lý gửi thông báo hoàn tiền qua Zalo lúc 2:14 sáng. Khách phản ánh bị làm phiền. | Ngữ cảnh | Gửi ngay đúng thiết kế, nhưng giả định không tính đến giờ ngủ của khách. |
| 17 | Bảng giá đổi từ ngày 01/11 nhưng trợ lý vẫn dùng bản cũ trong bộ nhớ đệm cho đơn dưới 2 kg. Lệch 1.000–2.000 đ mỗi đơn, 212 đơn trong 9 ngày, không ai mở lại. | Ngầm | Dùng bảng giá cũ trong bộ nhớ đệm, lệch nhỏ trên 212 đơn, không ai mở lại hay phát hiện. |
| 18 | Trợ lý tính đúng: phí giao 30.000 đ, hoàn 50%. Tin nhắn chỉ ghi "Đã hoàn 15.000 đ", không kèm cách tính. Khách cho là hoàn thiếu và mở lại yêu cầu. | Ngữ cảnh | Tính đúng, nhưng tin nhắn không kèm cách tính nên khách hiểu là hoàn thiếu. |
| 19 | Khách yêu cầu hoàn phí cho đơn từ 14 tháng trước. Trợ lý chỉ truy cập được dữ liệu 12 tháng. Trợ lý nói rõ không tra được và chuyển cho nhân viên kèm tóm tắt. | Giới hạn hệ thống | Dữ liệu chỉ có 12 tháng; đơn 14 tháng nằm ngoài phạm vi truy cập. |
| 20 | Khách gửi lại yêu cầu sau 10 phút vì chưa thấy phản hồi. Trợ lý hoàn hai lần cho cùng một đơn vì lệnh thứ hai không có khoá chống trùng. | Hệ thống | Thiếu khoá chống trùng nên hoàn hai lần; khách gửi lại là hành vi bình thường. |

## Đếm nhanh sau khi gắn

| Loại | Các ca | Số ca |
| --- | --- | --: |
| Do người dùng | 1, 6, 9, 14 | 4 |
| Hệ thống | 2, 7, 8, 15, 20 | 5 |
| Ngữ cảnh | 3, 10, 16, 18 | 4 |
| Giới hạn hệ thống | 4, 11, 13, 19 | 4 |
| Ngầm | 5, 12, 17 | 3 |
| **Tổng** | | **20** |
