# Dẫn chứng gán nhãn C bộ 1 của Chử Thị Ánh

Nguồn mô tả: [đề bài gốc](../../docs/Ngay13_Lab13_De_bai_hoc_vien.docx), mục “Hai mươi ca lỗi”. Mỗi ca bên dưới giữ nguyên văn mô tả trong DOCX để đối chiếu với [bảng nhãn](bang_loi.md).

Bộ nhãn có Codex hỗ trợ. Ngày 21/11/2026, Ánh xác nhận đã review và đồng ý cả 20 nhãn, bao gồm ca 9 giữ nhãn Do người dùng. Đã đối chiếu với bộ nhãn Hà sau merge: khớp 20/20 = 100%. Ánh xác nhận hai người đã rà và quyết định nhãn riêng trước khi so, rồi thống nhất kết quả; giữ ghi nhận có AI hỗ trợ.

## Định nghĩa nhãn theo đề bài

- **Do người dùng:** Người dùng nhập sai hoặc chọn sai.
- **Hệ thống:** Hệ thống trả lời sai hoặc làm sai so với thiết kế và chính sách.
- **Ngữ cảnh:** Hệ thống làm đúng thiết kế nhưng người dùng thấy là sai, vì giả định của hệ thống không khớp hoàn cảnh của họ.
- **Giới hạn hệ thống:** Hệ thống không thể trả lời, do thiếu dữ liệu, ngoài phạm vi, hoặc dạng đầu vào không xử lý được.
- **Ngầm:** Có sai nhưng cả người dùng lẫn hệ thống đều không nhận ra.

## Ca 1

> Khách nhập số tài khoản nhận hoàn tiền thiếu hai chữ số. Trợ lý tạo lệnh hoàn, ngân hàng trả về lỗi.

**Nhãn đề xuất:** Do người dùng.

**Lý do:** Khách nhập thiếu hai chữ số tài khoản.

**Kết luận của Ánh sau review:** Đồng ý giữ nhãn trên (xác nhận ngày 21/11/2026).

## Ca 2

> Kiện nội địa 28 kg. Trợ lý gọi tool tra bảng giá với tham số hàng thường thay vì hàng nặng, hoàn thiếu 45.000 đ. Khách mở lại sau 2 ngày.

**Nhãn đề xuất:** Hệ thống.

**Lý do:** Trợ lý gọi tool sai loại hàng, gây hoàn thiếu.

**Kết luận của Ánh sau review:** Đồng ý giữ nhãn trên (xác nhận ngày 21/11/2026).

## Ca 3

> Theo thiết kế, trợ lý hoàn tiền về ví LogiX trong 5 phút. Khách chờ tiền về tài khoản ngân hàng và báo “chưa được hoàn”.

**Nhãn đề xuất:** Ngữ cảnh.

**Lý do:** Hoàn về ví đúng thiết kế nhưng khách chờ tiền vào ngân hàng.

**Kết luận của Ánh sau review:** Đồng ý giữ nhãn trên (xác nhận ngày 21/11/2026).

## Ca 4

> Khách yêu cầu hoàn phí cho chặng do hãng nước ngoài giao. LogiX không có dữ liệu chặng này. Trợ lý nói không xác định được trạng thái và chuyển cho nhân viên.

**Nhãn đề xuất:** Giới hạn hệ thống.

**Lý do:** Thiếu dữ liệu chặng nước ngoài, trợ lý nhận biết giới hạn và chuyển nhân viên.

**Kết luận của Ánh sau review:** Đồng ý giữ nhãn trên (xác nhận ngày 21/11/2026).

## Ca 5

> Kiểm tra mẫu cuối tuần thấy 14 đơn có mã giảm giá bị hoàn theo giá trước giảm, thừa trung bình 12.000 đ mỗi đơn. Không khách nào báo, không cảnh báo nào kích.

**Nhãn đề xuất:** Ngầm.

**Lý do:** Hoàn thừa nhưng cả khách lẫn hệ thống không phát hiện, chỉ kiểm toán thấy.

**Kết luận của Ánh sau review:** Đồng ý giữ nhãn trên (xác nhận ngày 21/11/2026).

## Ca 6

> Khách chọn mục “Hoàn phí giao trễ” nhưng nội dung mô tả hàng bị vỡ. Trợ lý xử lý theo luồng giao trễ và từ chối vì đơn giao đúng hạn.

**Nhãn đề xuất:** Do người dùng.

**Lý do:** Khách chọn sai mục giao trễ khi thực tế hàng vỡ.

**Kết luận của Ánh sau review:** Đồng ý giữ nhãn trên (xác nhận ngày 21/11/2026).

## Ca 7

> API sổ cái trả lỗi 503 ở bước ghi hoàn tiền. Trợ lý thử lại 3 lần rồi vẫn báo khách “đã hoàn tiền thành công”.

**Nhãn đề xuất:** Hệ thống.

**Lý do:** Ghi sổ thất bại nhưng vẫn báo hoàn tiền thành công.

**Kết luận của Ánh sau review:** Đồng ý giữ nhãn trên (xác nhận ngày 21/11/2026).

## Ca 8

> Trợ lý dẫn “Điều 7.2 chính sách hoàn phí” làm căn cứ. Bản chính sách hiện hành không có điều 7.2. Số tiền hoàn vẫn đúng.

**Nhãn đề xuất:** Hệ thống.

**Lý do:** Dẫn điều khoản không tồn tại là trả lời sai dù tiền đúng; chưa có căn cứ gọi là lỗi ngầm.

**Kết luận của Ánh sau review:** Đồng ý giữ nhãn trên (xác nhận ngày 21/11/2026).

## Ca 9

> Khách nhập mã đơn của sàn thương mại điện tử thay vì mã vận đơn. Trợ lý báo “mã không hợp lệ” rồi dừng, không gợi ý gì.

**Nhãn đề xuất:** Do người dùng.

**Lý do:** Khách dùng mã đơn sàn thay mã vận đơn; hướng dẫn phục hồi cũng cần cải thiện.

**Ý kiến review của Ánh:** Trợ lý nên gợi ý cách tìm mã vận đơn khi khách nhập nhầm; việc báo lỗi rồi dừng cho thấy trải nghiệm hỗ trợ chưa đầy đủ.

**Điểm cần phân biệt:** Nhãn hiện tại xét nguyên nhân đầu vào là sai loại mã. Có thể cân nhắc Hệ thống nếu yêu cầu thiết kế quy định trợ lý phải hướng dẫn phục hồi nhưng không thực hiện; mô tả hiện tại chưa nêu yêu cầu đó. Sau trao đổi, Ánh đã xác nhận đồng ý giữ nhãn Do người dùng.

**Cách khắc phục đề xuất:** Giải thích mã cần nhập, chỉ nơi tìm mã vận đơn và cho khách nhập lại.

**Kết luận của Ánh sau review:** Đồng ý giữ nhãn trên (xác nhận ngày 21/11/2026).

## Ca 10

> Đơn giao trễ do bão. Trợ lý từ chối hoàn theo điều khoản bất khả kháng, đúng chính sách. Khách thấy vô lý vì ứng dụng vẫn hiện “cam kết giao 24 giờ”.

**Nhãn đề xuất:** Ngữ cảnh.

**Lý do:** Đúng chính sách bất khả kháng nhưng không khớp kỳ vọng từ cam kết 24 giờ.

**Kết luận của Ánh sau review:** Đồng ý giữ nhãn trên (xác nhận ngày 21/11/2026).

## Ca 11

> Khách gửi tin nhắn thoại 40 giây. Trợ lý không xử lý được âm thanh, trả lời “vui lòng nhập bằng chữ”.

**Nhãn đề xuất:** Giới hạn hệ thống.

**Lý do:** Âm thanh ngoài khả năng xử lý.

**Kết luận của Ánh sau review:** Đồng ý giữ nhãn trên (xác nhận ngày 21/11/2026).

## Ca 12

> Tool tra đơn của depot D05 trả thiếu một trường. Trợ lý vẫn ra kết quả đúng sau nhiều lần gọi, nên tiền token của D05 gấp 3 lần depot khác suốt 3 tuần mà không ai thấy.

**Nhãn đề xuất:** Ngầm.

**Lý do:** Kết quả đúng nhưng chi phí tăng kéo dài mà không ai phát hiện; lỗi ngầm vận hành.

**Kết luận của Ánh sau review:** Đồng ý giữ nhãn trên (xác nhận ngày 21/11/2026).

## Ca 13

> Khách hỏi hoàn phí bảo hiểm hàng hoá, sản phẩm của công ty bảo hiểm đối tác, ngoài phạm vi trợ lý. Trợ lý trả lời chung chung về phí vận chuyển, không nói rõ là mình không xử lý được.

**Nhãn đề xuất:** Giới hạn hệ thống.

**Lý do:** Phí bảo hiểm đối tác ngoài phạm vi; trả lời chung chung là biểu hiện cần sửa.

**Kết luận của Ánh sau review:** Đồng ý giữ nhãn trên (xác nhận ngày 21/11/2026).

## Ca 14

> Khách bấm nhầm “Xác nhận đã nhận tiền” khi chưa nhận. Yêu cầu bị đóng.

**Nhãn đề xuất:** Do người dùng.

**Lý do:** Khách bấm nhầm xác nhận đã nhận tiền.

**Kết luận của Ánh sau review:** Đồng ý giữ nhãn trên (xác nhận ngày 21/11/2026).

## Ca 15

> Đơn trễ 26 giờ. Chính sách: trễ 24–48 giờ hoàn 50%. Trợ lý tính hoàn 100%. Nhân viên xem lại bắt được trước khi gửi.

**Nhãn đề xuất:** Hệ thống.

**Lý do:** Tính sai mức hoàn, nhân viên bắt được trước khi gửi; không phải lỗi ngầm.

**Kết luận của Ánh sau review:** Đồng ý giữ nhãn trên (xác nhận ngày 21/11/2026).

## Ca 16

> Theo thiết kế “gửi ngay khi xong”, trợ lý gửi thông báo hoàn tiền qua Zalo lúc 2:14 sáng. Khách phản ánh bị làm phiền.

**Nhãn đề xuất:** Ngữ cảnh.

**Lý do:** Gửi ngay đúng thiết kế nhưng giờ gửi không phù hợp hoàn cảnh.

**Kết luận của Ánh sau review:** Đồng ý giữ nhãn trên (xác nhận ngày 21/11/2026).

## Ca 17

> Bảng giá đổi từ ngày 01/11 nhưng trợ lý vẫn dùng bản cũ trong bộ nhớ đệm cho đơn dưới 2 kg. Lệch 1.000–2.000 đ mỗi đơn, 212 đơn trong 9 ngày, không ai mở lại.

**Nhãn đề xuất:** Ngầm.

**Lý do:** Bảng giá cũ gây lệch tiền kéo dài mà không ai mở lại; trọng tâm là sai sót không được nhận ra.

**Kết luận của Ánh sau review:** Đồng ý giữ nhãn trên (xác nhận ngày 21/11/2026).

## Ca 18

> Trợ lý tính đúng: phí giao 30.000 đ, hoàn 50%. Tin nhắn chỉ ghi “Đã hoàn 15.000 đ”, không kèm cách tính. Khách cho là hoàn thiếu và mở lại yêu cầu.

**Nhãn đề xuất:** Ngữ cảnh.

**Lý do:** Tính đúng nhưng thiếu giải thích khiến khách cho là thiếu.

**Kết luận của Ánh sau review:** Đồng ý giữ nhãn trên (xác nhận ngày 21/11/2026).

## Ca 19

> Khách yêu cầu hoàn phí cho đơn từ 14 tháng trước. Trợ lý chỉ truy cập được dữ liệu 12 tháng. Trợ lý nói rõ không tra được và chuyển cho nhân viên kèm tóm tắt.

**Nhãn đề xuất:** Giới hạn hệ thống.

**Lý do:** Yêu cầu vượt cửa sổ dữ liệu 12 tháng, trợ lý nói rõ và chuyển nhân viên.

**Kết luận của Ánh sau review:** Đồng ý giữ nhãn trên (xác nhận ngày 21/11/2026).

## Ca 20

> Khách gửi lại yêu cầu sau 10 phút vì chưa thấy phản hồi. Trợ lý hoàn hai lần cho cùng một đơn vì lệnh thứ hai không có khoá chống trùng.

**Nhãn đề xuất:** Hệ thống.

**Lý do:** Thiếu khóa chống trùng làm hoàn hai lần; lỗi hệ thống dù khách gửi lại.

**Kết luận của Ánh sau review:** Đồng ý giữ nhãn trên (xác nhận ngày 21/11/2026).
