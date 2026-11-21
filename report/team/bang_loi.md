# Bảng lỗi và cách khắc phục · Nhiệm vụ C

> **Trạng thái hiện tại:** `PENDING – Đã khóa bộ nhãn độc lập 20/20 của Người 2 (Hoàng Minh Huy); đang chờ bộ nhãn độc lập của Người 1 (Bùi Quang Huy) để đối chiếu`.
> Hai người gắn nhãn hoàn thành độc lập cả 20 ca trước khi so sánh. Tuyệt đối không trao đổi hoặc sửa bộ nhãn độc lập sau khi đã so.

## Định nghĩa 5 nhóm taxonomy chính thức (Google PAIR)

1. **Do người dùng:** Người dùng nhập sai dữ liệu, thao tác nhầm, chọn sai danh mục hoặc có kỳ vọng khác với thiết kế sản phẩm.
2. **Hệ thống:** Lỗi kỹ thuật/code/hạ tầng/tích hợp (API lỗi, cache cũ, thiếu khóa chống trùng, gọi sai tham số/tính sai quy tắc) đã hoặc có thể lộ ra trong vận hành.
3. **Ngữ cảnh:** Hệ thống hoạt động đúng kỹ thuật/chính sách nhưng thiếu hoặc lệch ngữ cảnh thực tế/giao tiếp/hiển thị (thời điểm gửi, thiếu giải thích cách tính, thông điệp ứng dụng mâu thuẫn).
4. **Giới hạn hệ thống:** Yêu cầu nằm ngoài phạm vi dữ liệu, kênh tiếp nhận hoặc nghiệp vụ mà trợ lý được thiết kế để xử lý (âm thanh, dữ liệu quá hạn, sản phẩm đối tác ngoài phạm vi).
5. **Ngầm:** Lỗi xảy ra âm thầm (sai tiền hoàn, tốn token bất thường, sai dữ liệu) nhưng hệ thống vẫn trả kết quả có vẻ bình thường, không kích hoạt cảnh báo và không ai nhận ra cho tới khi kiểm tra/audit.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Bùi Quang Huy (`2A202603469`) · Người gắn nhãn 2: Hoàng Minh Huy (`2A202603495`) (gắn trong 8 phút, không trao đổi)

| Ca | Mô tả tình huống (trích nguyên văn đề bài) | Nhãn người 1 | Nhãn người 2 | Lý do ngắn (Người 2) | Confidence | Trùng? | Nhãn thống nhất | Trạng thái |
| --: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Khách nhập số tài khoản nhận hoàn tiền thiếu hai chữ số. Trợ lý tạo lệnh hoàn, ngân hàng trả về lỗi. | ... | Do người dùng | Khách nhập số tài khoản thiếu hai chữ số, dữ liệu đầu vào không chính xác. | Cao | ... | ... | Chờ N1 |
| 2 | Kiện nội địa 28 kg. Trợ lý gọi tool tra bảng giá với tham số hàng thường thay vì hàng nặng, hoàn thiếu 45.000 đ. Khách mở lại sau 2 ngày. | ... | Hệ thống | Trợ lý truyền sai tham số loại hàng khi gọi tool bảng giá, dẫn đến hoàn thiếu tiền. | Cao | ... | ... | Chờ N1 |
| 3 | Theo thiết kế, trợ lý hoàn tiền về ví LogiX trong 5 phút. Khách chờ tiền về tài khoản ngân hàng và báo “chưa được hoàn”. | ... | Ngữ cảnh | Khách kỳ vọng nhận tiền vào tài khoản ngân hàng trong khi thiết kế hoàn về ví LogiX; thiếu thông tin làm rõ kênh nhận tiền. | Cao | ... | ... | Chờ N1 |
| 4 | Khách yêu cầu hoàn phí cho chặng do hãng nước ngoài giao. LogiX không có dữ liệu chặng này. Trợ lý nói không xác định được trạng thái và chuyển cho nhân viên. | ... | Giới hạn hệ thống | Chặng do hãng nước ngoài giao không có trong dữ liệu xử lý của LogiX. | Cao | ... | ... | Chờ N1 |
| 5 | Kiểm tra mẫu cuối tuần thấy 14 đơn có mã giảm giá bị hoàn theo giá trước giảm, thừa trung bình 12.000 đ mỗi đơn. Không khách nào báo, không cảnh báo nào kích. | ... | Ngầm | Hoàn tiền theo giá trước giảm gây sai số tiền nhưng không có cảnh báo, chỉ được phát hiện khi kiểm tra mẫu. | Cao | ... | ... | Chờ N1 |
| 6 | Khách chọn mục “Hoàn phí giao trễ” nhưng nội dung mô tả hàng bị vỡ. Trợ lý xử lý theo luồng giao trễ và từ chối vì đơn giao đúng hạn. | ... | Do người dùng | Khách chọn nhầm danh mục giao trễ trong khi nội dung thực tế là hàng bị vỡ. | Trung bình | ... | ... | Chờ N1 |
| 7 | API sổ cái trả lỗi 503 ở bước ghi hoàn tiền. Trợ lý thử lại 3 lần rồi vẫn báo khách “đã hoàn tiền thành công”. | ... | Hệ thống | API sổ cái trả lỗi 503 nhưng trợ lý vẫn thông báo hoàn tiền thành công. | Cao | ... | ... | Chờ N1 |
| 8 | Trợ lý dẫn “Điều 7.2 chính sách hoàn phí” làm căn cứ. Bản chính sách hiện hành không có điều 7.2. Số tiền hoàn vẫn đúng. | ... | Ngữ cảnh | Số tiền đúng nhưng trợ lý viện dẫn điều khoản không tồn tại, khiến căn cứ giải thích không chính xác. | Trung bình | ... | ... | Chờ N1 |
| 9 | Khách nhập mã đơn của sàn thương mại điện tử thay vì mã vận đơn. Trợ lý báo “mã không hợp lệ” rồi dừng, không gợi ý gì. | ... | Do người dùng | Khách nhập mã đơn của sàn thương mại điện tử thay vì mã vận đơn. | Cao | ... | ... | Chờ N1 |
| 10 | Đơn giao trễ do bão. Trợ lý từ chối hoàn theo điều khoản bất khả kháng, đúng chính sách. Khách thấy vô lý vì ứng dụng vẫn hiện “cam kết giao 24 giờ”. | ... | Ngữ cảnh | Quyết định từ chối đúng chính sách nhưng thông điệp cam kết giao 24 giờ trên ứng dụng tạo kỳ vọng trái chiều. | Cao | ... | ... | Chờ N1 |
| 11 | Khách gửi tin nhắn thoại 40 giây. Trợ lý không xử lý được âm thanh, trả lời “vui lòng nhập bằng chữ”. | ... | Giới hạn hệ thống | Trợ lý không hỗ trợ đầu vào âm thanh, yêu cầu nằm ngoài kênh xử lý được thiết kế. | Cao | ... | ... | Chờ N1 |
| 12 | Tool tra đơn của depot D05 trả thiếu một trường. Trợ lý vẫn ra kết quả đúng sau nhiều lần gọi, nên tiền token của D05 gấp 3 lần depot khác suốt 3 tuần mà không ai thấy. | ... | Ngầm | Tool thiếu trường khiến hệ thống gọi lại nhiều lần, làm chi phí token tăng bất thường nhưng không có cảnh báo. | Cao | ... | ... | Chờ N1 |
| 13 | Khách hỏi hoàn phí bảo hiểm hàng hoá, sản phẩm của công ty bảo hiểm đối tác, ngoài phạm vi trợ lý. Trợ lý trả lời chung chung về phí vận chuyển, không nói rõ là mình không xử lý được. | ... | Giới hạn hệ thống | Phí bảo hiểm của đối tác nằm ngoài phạm vi nghiệp vụ trợ lý được thiết kế để xử lý. | Cao | ... | ... | Chờ N1 |
| 14 | Khách bấm nhầm “Xác nhận đã nhận tiền” khi chưa nhận. Yêu cầu bị đóng. | ... | Do người dùng | Khách bấm nhầm xác nhận đã nhận tiền, khiến yêu cầu bị đóng sai. | Cao | ... | ... | Chờ N1 |
| 15 | Đơn trễ 26 giờ. Chính sách: trễ 24–48 giờ hoàn 50%. Trợ lý tính hoàn 100%. Nhân viên xem lại bắt được trước khi gửi. | ... | Hệ thống | Trợ lý áp dụng mức hoàn 100% thay vì 50% theo chính sách trễ 24–48 giờ. | Cao | ... | ... | Chờ N1 |
| 16 | Theo thiết kế “gửi ngay khi xong”, trợ lý gửi thông báo hoàn tiền qua Zalo lúc 2:14 sáng. Khách phản ánh bị làm phiền. | ... | Ngữ cảnh | Thông báo được gửi lúc 2:14 sáng theo logic gửi ngay nhưng không xét đến thời điểm phù hợp với khách hàng. | Cao | ... | ... | Chờ N1 |
| 17 | Bảng giá đổi từ ngày 01/11 nhưng trợ lý vẫn dùng bản cũ trong bộ nhớ đệm cho đơn dưới 2 kg. Lệch 1.000–2.000 đ mỗi đơn, 212 đơn trong 9 ngày, không ai mở lại. | ... | Ngầm | Cache sử dụng bảng giá cũ gây sai lệch trên nhiều đơn nhưng không kích hoạt cảnh báo. | Cao | ... | ... | Chờ N1 |
| 18 | Trợ lý tính đúng: phí giao 30.000 đ, hoàn 50%. Tin nhắn chỉ ghi “Đã hoàn 15.000 đ”, không kèm cách tính. Khách cho là hoàn thiếu và mở lại yêu cầu. | ... | Ngữ cảnh | Số tiền hoàn đúng nhưng thiếu giải thích cách tính khiến khách hiểu nhầm là hoàn thiếu. | Cao | ... | ... | Chờ N1 |
| 19 | Khách yêu cầu hoàn phí cho đơn từ 14 tháng trước. Trợ lý chỉ truy cập được dữ liệu 12 tháng. Trợ lý nói rõ không tra được và chuyển cho nhân viên kèm tóm tắt. | ... | Giới hạn hệ thống | Yêu cầu vượt quá cửa sổ dữ liệu 12 tháng mà trợ lý có thể truy cập. | Cao | ... | ... | Chờ N1 |
| 20 | Khách gửi lại yêu cầu sau 10 phút vì chưa thấy phản hồi. Trợ lý hoàn hai lần cho cùng một đơn vì lệnh thứ hai không có khoá chống trùng. | ... | Hệ thống | Thiếu khóa chống trùng khiến cùng một yêu cầu tạo hai lệnh hoàn tiền. | Cao | ... | ... | Chờ N1 |

**Ghi chú của Người 2 (Hoàng Minh Huy) trước khi đối chiếu với Người 1:**
- **Ca 6:** Có thể tranh luận giữa *Do người dùng* và *Ngữ cảnh*; chọn *Do người dùng* vì khách chọn sai danh mục.
- **Ca 8:** Có thể tranh luận giữa *Ngữ cảnh* và *Hệ thống*; chọn *Ngữ cảnh* vì số tiền đúng, vấn đề nằm ở căn cứ giải thích sai.
- **Ca 15:** Lỗi tính toán/áp dụng chính sách nên xếp *Hệ thống*.
- **Ca 17:** Dù nguyên nhân kỹ thuật là cache cũ, đề bài nhấn mạnh lỗi không ai phát hiện trong thời gian dài nên xếp *Ngầm*.

**Công thức tỉ lệ đồng thuận:** `Số ca có Nhãn người 1 == Nhãn người 2 ÷ 20 × 100%` (yêu cầu đạt $\ge 16/20 = 80\%$).
**Tỉ lệ đồng thuận:** `PENDING` / 20 = `PENDING`%

## Quy tắc phân biệt cho các ca không trùng (Reconciliation)

Mỗi ca không trùng ghi một câu quy tắc phân biệt. Nếu đồng thuận dưới 80%, phải ghi định nghĩa đã viết lại trước khi gắn nhãn lại.

| Ca | Nhãn người 1 | Nhãn người 2 | Nhãn thống nhất | Quy tắc phân biệt (1 câu) |
| --: | --- | --- | --- | --- |
| `PENDING` | ... | ... | ... | `[CHỜ ĐỐI CHIẾU SAU KHI NGƯỜI 1 KHÓA BỘ NHÃN ĐỘC LẬP]` |

## Bảng khắc phục cho 5 ca, mỗi loại một ca

> Yêu cầu rubric: chọn 5 ca đã thống nhất nhãn (mỗi nhóm taxonomy một ca); cách phát hiện phải đo được bằng event, ngưỡng và tần suất; người phụ trách là một vai trò cụ thể (không ghi "cả đội").

| Ca | Loại lỗi | Phát hiện bằng gì (event, ngưỡng, tần suất) | Chỉ số theo dõi | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- | --- |
| `PENDING` | Do người dùng | `[CHỜ chọn ca đại diện sau đối chiếu; xác định event + ngưỡng + tần suất]` | ... | ... | `[1 vai trò cụ thể, vd: Trưởng nhóm CSKH / Product Designer]` |
| `PENDING` | Hệ thống | `[CHỜ chọn ca đại diện sau đối chiếu; xác định event + ngưỡng + tần suất]` | ... | ... | `[1 vai trò cụ thể, vd: Kỹ sư Backend]` |
| `PENDING` | Ngữ cảnh | `[CHỜ chọn ca đại diện sau đối chiếu; xác định event + ngưỡng + tần suất]` | ... | ... | `[1 vai trò cụ thể, vd: PM trợ lý hoàn phí]` |
| `PENDING` | Giới hạn hệ thống | `[CHỜ chọn ca đại diện sau đối chiếu; xác định event + ngưỡng + tần suất]` | ... | ... | `[1 vai trò cụ thể, vd: Kỹ sư AI / PM trợ lý hoàn phí]` |
| `PENDING` | Ngầm | `[CHỜ chọn ca đại diện sau đối chiếu; xác định event + ngưỡng + tần suất]` | ... | ... | `[1 vai trò cụ thể, vd: Kế toán / Kiểm soát chất lượng]` |
