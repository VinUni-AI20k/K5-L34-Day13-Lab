# Chuẩn bị gắn nhãn lỗi CP3

Tài liệu giúp người gắn nhãn 1 chuẩn bị cho nhiệm vụ C: hiểu năm loại lỗi và đọc trước 20 tình huống của trợ lý hoàn phí LogiX-VN. Toàn bộ tình huống thuộc bài lab giả lập. Bảng dưới đây tóm tắt tình huống để bạn tự gắn nhãn độc lập trong 8 phút ở CP3.

Nguồn: [Đề bài học viên](Ngay13_Lab13_De_bai_hoc_vien.docx), các mục “Nhiệm vụ C”, “Năm loại lỗi, theo Google PAIR” và “Hai mươi ca lỗi”. Các định nghĩa dưới đây diễn giải theo đề bài; các câu hỏi phân biệt là gợi ý đọc hiểu.

## 1. Năm loại lỗi cần nắm

| Loại lỗi | Nghĩa theo đề bài | Câu hỏi giúp nhận biết |
| --- | --- | --- |
| **Do người dùng** | Người dùng nhập sai hoặc chọn sai. | Người dùng có cung cấp sai thông tin hay bấm nhầm lựa chọn không? |
| **Hệ thống** | Hệ thống trả lời sai hoặc thực hiện sai so với thiết kế và chính sách. | Hệ thống có tính sai, dẫn sai căn cứ, gọi sai tool hoặc báo sai kết quả không? |
| **Ngữ cảnh** | Hệ thống làm đúng thiết kế nhưng người dùng thấy sai vì giả định của hệ thống không khớp hoàn cảnh của họ. | Kết quả có đúng theo thiết kế nhưng không khớp kỳ vọng, cách hiểu hoặc thời điểm của khách không? |
| **Giới hạn hệ thống** | Hệ thống không thể trả lời vì thiếu dữ liệu, ngoài phạm vi hoặc không xử lý được dạng đầu vào. | Hệ thống có thiếu khả năng hoặc dữ liệu cần thiết để giải quyết yêu cầu không? |
| **Ngầm** | Có sai nhưng cả người dùng lẫn hệ thống đều không nhận ra. | Sai sót có tiếp diễn mà không ai báo và không cảnh báo nào phát hiện không? |

### Những điểm dễ nhầm

- **Hệ thống không chỉ là lỗi kỹ thuật:** tính sai tiền hoặc viện dẫn điều khoản không tồn tại cũng thuộc phạm vi định nghĩa này.
- **Ngữ cảnh và hệ thống:** kiểm tra trước xem hệ thống có làm đúng thiết kế, chính sách không; sau đó xét sự khác biệt với hoàn cảnh và kỳ vọng của khách.
- **Giới hạn và hệ thống:** phân biệt “không có khả năng hoặc dữ liệu để làm” với “có nhiệm vụ phải làm nhưng thực hiện sai”.
- **Ngầm và hệ thống:** chú ý chi tiết không ai nhận ra, không có cảnh báo, chỉ phát hiện khi kiểm tra về sau. Lỗi ngầm có thể liên quan cả tiền và chi phí vận hành.
- **Nguyên nhân gốc và cách khắc phục:** việc cần sửa giao diện hoặc thêm kiểm tra đầu vào chưa đủ để quyết định nhãn. Đọc nguyên nhân được mô tả trong từng ca.

## 2. Tóm tắt 20 ca lỗi

Giữ nguyên số thứ tự để đối chiếu với đề gốc và `report/team/bang_loi.md`. Khi phân vân, đọc lại mô tả đầy đủ trong file Word trước khi chọn nhãn.

| Ca | Tình huống tóm tắt |
| ---: | --- |
| 1 | Khách nhập tài khoản nhận tiền thiếu 2 chữ số. Trợ lý vẫn tạo lệnh hoàn; ngân hàng trả lỗi. |
| 2 | Kiện nội địa nặng 28 kg nhưng trợ lý tra giá hàng thường thay vì hàng nặng, hoàn thiếu 45.000 đ. Khách mở lại sau 2 ngày. |
| 3 | Thiết kế hoàn tiền về ví LogiX trong 5 phút; khách lại chờ tiền vào tài khoản ngân hàng và báo chưa được hoàn. |
| 4 | Yêu cầu liên quan chặng giao của hãng nước ngoài mà LogiX không có dữ liệu. Trợ lý nói không xác định được trạng thái và chuyển nhân viên. |
| 5 | Kiểm tra cuối tuần phát hiện 14 đơn có mã giảm giá bị hoàn theo giá trước giảm, thừa trung bình 12.000 đ/đơn. Không khách nào báo, không cảnh báo nào kích hoạt. |
| 6 | Khách chọn lý do giao trễ nhưng mô tả hàng vỡ. Trợ lý đi theo luồng giao trễ và từ chối vì đơn giao đúng hạn. |
| 7 | API sổ cái lỗi 503 khi ghi hoàn tiền. Trợ lý thử lại 3 lần nhưng vẫn báo khách đã hoàn thành công. |
| 8 | Trợ lý dẫn Điều 7.2 không tồn tại trong chính sách hiện hành; số tiền hoàn vẫn đúng. |
| 9 | Khách nhập mã đơn của sàn thương mại điện tử thay cho mã vận đơn. Trợ lý báo mã không hợp lệ rồi dừng, không hướng dẫn thêm. |
| 10 | Đơn trễ do bão; trợ lý từ chối hoàn đúng điều khoản bất khả kháng. Khách phản đối vì ứng dụng vẫn hiển thị cam kết giao trong 24 giờ. |
| 11 | Khách gửi tin nhắn thoại 40 giây. Trợ lý không xử lý được âm thanh và yêu cầu nhập chữ. |
| 12 | Tool tra đơn D05 thiếu một trường; trợ lý gọi nhiều lần rồi vẫn trả đúng. Chi phí token depot này cao gấp 3 lần nơi khác trong 3 tuần mà không ai nhận thấy. |
| 13 | Khách hỏi hoàn phí bảo hiểm của đối tác, ngoài phạm vi trợ lý. Trợ lý trả lời chung về phí vận chuyển, không nói rõ giới hạn. |
| 14 | Khách bấm nhầm xác nhận đã nhận tiền dù chưa nhận; yêu cầu bị đóng. |
| 15 | Đơn trễ 26 giờ, chính sách quy định hoàn 50% cho mức trễ 24–48 giờ. Trợ lý tính 100%; nhân viên phát hiện trước khi gửi. |
| 16 | Trợ lý làm theo thiết kế gửi ngay khi xong, thông báo qua Zalo lúc 2:14 sáng. Khách phản ánh bị làm phiền. |
| 17 | Bảng giá đổi từ 01/11 nhưng cache vẫn giữ bản cũ cho đơn dưới 2 kg. Có 212 đơn lệch 1.000–2.000 đ trong 9 ngày, không ai mở lại yêu cầu. |
| 18 | Phí giao 30.000 đ, hoàn 50% đúng bằng 15.000 đ. Tin nhắn chỉ nêu tiền hoàn, thiếu cách tính; khách nghĩ bị hoàn thiếu và mở lại. |
| 19 | Khách hỏi đơn từ 14 tháng trước nhưng trợ lý chỉ truy cập được 12 tháng. Trợ lý nói rõ giới hạn và chuyển nhân viên kèm tóm tắt. |
| 20 | Khách gửi lại yêu cầu sau 10 phút chưa có phản hồi. Trợ lý hoàn tiền 2 lần cho cùng đơn vì lệnh thứ hai thiếu khóa chống trùng. |

## 3. Cách dùng tài liệu khi bắt đầu CP3

1. Tự đọc đủ 20 ca và chọn một trong năm nhãn cho mỗi ca trong **8 phút**, không trao đổi hoặc xem bộ nhãn của Tuấn.
2. Với mỗi lựa chọn, ghi một lý do ngắn dựa trên chi tiết trong tình huống. Giữ nguyên bộ nhãn ban đầu sau khi đối chiếu.
3. Khi cả hai đã xong, so nhãn và tính: **số ca trùng / 20 × 100%**. Mục tiêu từ **16/20 = 80%**; đây chưa phải kết quả của nhóm.
4. Với ca khác nhau, thống nhất nhãn và viết một câu quy tắc phân biệt. Nếu đồng thuận dưới 80%, viết lại định nghĩa trước khi làm tiếp.
5. Chọn 5 ca, mỗi loại một ca, để cùng điền cách phát hiện đo được, cách khắc phục và một vai trò phụ trách vào [bảng lỗi](../report/team/bang_loi.md).

## 4. Checklist chuẩn bị

- [ ] Phân biệt được năm loại lỗi theo định nghĩa của đề.
- [ ] Đã đọc đủ 20 tình huống, chú ý các số tiền, thời gian và phản hồi của khách.
- [ ] Có chỗ ghi riêng nhãn và lý do cho từng ca.
- [ ] Chỉ so kết quả sau khi cả mình và Tuấn đã gắn nhãn độc lập xong.

Tài liệu này là phần đọc trước; nhãn của người 1, nhãn của Tuấn, tỉ lệ đồng thuận và nhãn thống nhất sẽ được ghi từ quá trình làm thực tế.
