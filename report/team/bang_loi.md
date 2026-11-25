# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Cao Trung Hiếu · Người gắn nhãn 2: (điền tên) (gắn trong 8 phút, không trao đổi)

Cột "Nhãn người 2", "Trùng?" và "Nhãn thống nhất" do người gắn nhãn 2 và nhóm điền sau khi so nhãn.

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | ... | ... | ... |
| 2 | Hệ thống | ... | ... | ... |
| 3 | Ngữ cảnh | ... | ... | ... |
| 4 | Giới hạn hệ thống | ... | ... | ... |
| 5 | Ngầm | ... | ... | ... |
| 6 | Do người dùng | ... | ... | ... |
| 7 | Hệ thống | ... | ... | ... |
| 8 | Hệ thống | ... | ... | ... |
| 9 | Do người dùng | ... | ... | ... |
| 10 | Ngữ cảnh | ... | ... | ... |
| 11 | Giới hạn hệ thống | ... | ... | ... |
| 12 | Ngầm | ... | ... | ... |
| 13 | Giới hạn hệ thống | ... | ... | ... |
| 14 | Do người dùng | ... | ... | ... |
| 15 | Hệ thống | ... | ... | ... |
| 16 | Ngữ cảnh | ... | ... | ... |
| 17 | Ngầm | ... | ... | ... |
| 18 | Ngữ cảnh | ... | ... | ... |
| 19 | Giới hạn hệ thống | ... | ... | ... |
| 20 | Hệ thống | ... | ... | ... |

**Tỉ lệ đồng thuận:** ... / 20 = ...%

### Căn cứ nhãn của người gắn nhãn 1

Mỗi ca trả lời các câu hỏi nhận ra của hướng dẫn (Đầu vào khách sai? Vi phạm thiết kế/chính sách? Kết quả đúng nhưng giả định lệch? Làm được không? Chỉ lộ qua kiểm tra mẫu?).

| Ca | Nhãn | Căn cứ từ chính mô tả ca |
| --: | --- | --- |
| 1 | Do người dùng | Khách nhập thiếu hai chữ số tài khoản; ngân hàng báo lỗi là hệ quả của đầu vào sai. |
| 2 | Hệ thống | Gọi tool với tham số hàng thường cho kiện 28 kg, trái thiết kế (phải dùng hàng nặng); sai lộ ra khi khách mở lại. |
| 3 | Ngữ cảnh | Hoàn về ví LogiX trong 5 phút đúng thiết kế; khách giả định tiền về ngân hàng. |
| 4 | Giới hạn hệ thống | LogiX không có dữ liệu chặng hãng nước ngoài; trợ lý nói rõ và chuyển nhân viên. |
| 5 | Ngầm | 14 đơn hoàn thừa 12.000 đ; không khách báo, không cảnh báo kích, chỉ lộ qua kiểm tra mẫu. |
| 6 | Do người dùng | Khách chọn sai mục "giao trễ" cho hàng vỡ; trợ lý làm đúng luồng đã chọn. |
| 7 | Hệ thống | Sổ cái lỗi 503 mà vẫn báo "đã hoàn thành công"; trái thiết kế, sai nhìn thấy được (nhật ký lỗi, khách hỏi lại). |
| 8 | Hệ thống | Dẫn Điều 7.2 không tồn tại; trích dẫn sai lộ ra (nhìn thấy được) nên không phải ngầm. |
| 9 | Do người dùng | Khách nhập mã đơn sàn thay mã vận đơn. Việc không gợi ý là chỗ cần cải thiện, không phải nguyên nhân gốc. |
| 10 | Ngữ cảnh | Từ chối bất khả kháng đúng chính sách; khách thấy vô lý vì giao diện còn hiện "cam kết 24 giờ". |
| 11 | Giới hạn hệ thống | Không xử lý được âm thanh, dạng đầu vào ngoài khả năng. |
| 12 | Ngầm | Câu trả lời đúng nhưng token D05 gấp 3 lần suốt 3 tuần mà không ai thấy; sai nằm ở chi phí. |
| 13 | Giới hạn hệ thống | Bảo hiểm hàng hoá ngoài phạm vi; ngoài phạm vi là giới hạn, kể cả khi trợ lý xử lý kém. |
| 14 | Do người dùng | Khách bấm nhầm "Xác nhận đã nhận tiền". |
| 15 | Hệ thống | Tính 100% thay vì 50% theo chính sách trễ 24–48 giờ; nhân viên bắt được nên sai đã lộ. |
| 16 | Ngữ cảnh | Gửi Zalo lúc 2:14 sáng đúng thiết kế "gửi ngay khi xong"; khách thấy phiền. |
| 17 | Ngầm | Dùng bảng giá cũ trong bộ nhớ đệm, 212 đơn trong 9 ngày, không ai mở lại, không ai nhận ra. |
| 18 | Ngữ cảnh | Tính đúng (30.000 × 50% = 15.000); chỉ thiếu cách tính nên khách hiểu lệch. |
| 19 | Giới hạn hệ thống | Dữ liệu chỉ 12 tháng, đơn 14 tháng trước không tra được; trợ lý nói rõ và chuyển nhân viên. |
| 20 | Hệ thống | Hoàn hai lần vì lệnh thứ hai không có khoá chống trùng; trái thiết kế, lộ ra khi đối soát số lệnh hoàn trên một đơn. |

Lưu ý minh bạch: người thực hiện bản nhãn này đã xem bảng "Nhãn tham khảo" trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` trước khi gắn, nên bộ nhãn này chưa độc lập thật sự. Nên để người gắn nhãn 2 tự gắn, rồi so với cột trên. Nếu nhóm cần bộ nhãn "người 1" độc lập đúng nghĩa thì người gắn nhãn 1 nên tự gắn lại không nhìn cột này.

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

Điền sau khi so nhãn. Các quy tắc sau áp dụng cho nhóm ca dễ lẫn, dùng khi nhãn của hai người lệch nhau:

- Ca 6, 9: gốc lỗi là khách chọn sai mục hoặc nhập sai mã, nên là Do người dùng; việc trợ lý không gợi ý chỉ là cách khắc phục.
- Ca 13: ngoài phạm vi là Giới hạn hệ thống, kể cả khi trợ lý xử lý giới hạn đó kém.
- Ca 8, 15: sai đã lộ ra (trích dẫn nhìn thấy được, nhân viên bắt được) nên là Hệ thống; Ngầm chỉ dùng khi không ai nhận ra cho tới khi kiểm tra.
- Ca 18: số tiền đúng chính sách, chỉ giả định "khách hiểu cách tính" không khớp, nên là Ngữ cảnh.
- Ca 12: kết quả đúng nhưng chi phí sai suốt 3 tuần không ai thấy, nên là Ngầm (sai có thể là sai về chi phí).

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 14 | Do người dùng | Event `confirm_received_clicked` mà sau đó có `reopen_request` hoặc khiếu nại trong 7 ngày; cảnh báo khi vượt 1% số yêu cầu đóng mỗi tuần | Thêm bước xác nhận hai lần ("Bạn đã thấy tiền trong tài khoản?") và cho mở lại yêu cầu trong 48 giờ sau khi xác nhận | PM trợ lý hoàn phí |
| 20 | Hệ thống | Đối soát mỗi giờ: một `order_id` có từ 2 bản ghi `refund_issued` trở lên; ngưỡng 0 ca | Thêm khoá chống trùng (idempotency key) theo đơn cho lệnh hoàn; lệnh thứ hai trả lại kết quả của lệnh đầu | Kỹ sư trưởng agent |
| 16 | Ngữ cảnh | Event `notification_sent` ngoài khung 22:00–07:00 và tỉ lệ phản ánh bị làm phiền theo tuần; ngưỡng 0 tin ngoài khung | Giữ tin đến 07:00 sáng, vẫn ghi nhận hoàn tiền ngay; cho khách chọn giờ nhận | Trưởng nhóm CSKH |
| 19 | Giới hạn hệ thống | Event `handoff_to_staff` với `reason = ngoai_du_lieu_12_thang`, theo tuần; theo dõi tỉ lệ chuyển nhân viên | Giữ cách chuyển kèm tóm tắt; thêm quy tắc từ chối sớm đơn quá 12 tháng và báo trước điều kiện cho khách | PM trợ lý hoàn phí |
| 12 | Ngầm | So token mỗi yêu cầu theo depot với trung vị 12 depot; cảnh báo khi cao hơn 1,5 lần trong 3 ngày liên tiếp; kiểm tra mẫu hàng tuần | Sửa tool tra đơn D05 để trả đủ trường; thêm cảnh báo chi phí theo depot và ghi `tool_schema_version` vào trace | Kỹ sư trưởng agent |
