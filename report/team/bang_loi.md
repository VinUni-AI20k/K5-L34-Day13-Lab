# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Vũ Thành Toàn — 2A202603654. Người gắn nhãn 2: Lê Nguyễn Hoàng Sơn — 2A202603686.


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

**Tỉ lệ trùng theo xác nhận:** 20/20 = 100%; không có ca bất đồng. Theo khai báo của Sơn và Toàn, hai người gắn nhãn trong buổi chiều của ngày lab; chưa có phiếu gốc ghi giờ và chưa xác minh được hai bộ nhãn có gắn độc lập trước khi xem nhãn nhau hay không. Giữ nguyên các nhãn đã ghi.


## Giải thích 20 ca, có AI hỗ trợ biên soạn

| Ca | Căn cứ từ mô tả và quy tắc nguyên nhân gốc |
| --: | --- |
| 1 | Khách nhập số tài khoản thiếu 2 chữ số; lỗi đầu vào dẫn đến ngân hàng từ chối. |
| 2 | Kiện 28 kg nhưng trợ lý truyền loại hàng thường vào tool; sai tham số so với thiết kế, hoàn thiếu 45.000 đ và khách phát hiện. |
| 3 | Hoàn về ví trong 5 phút đúng thiết kế; khách lại mong nhận vào ngân hàng. |
| 4 | Không có dữ liệu chặng nước ngoài; trợ lý không đủ khả năng xác định và chuyển nhân viên. |
| 5 | Kiểm tra mẫu mới thấy 14 đơn hoàn thừa trung bình 12.000 đ; trước đó khách và hệ thống đều không phát hiện. |
| 6 | Khách chọn luồng giao trễ trong khi hàng bị vỡ; nguyên nhân gốc là chọn sai mục. |
| 7 | Sổ cái lỗi 503 qua 3 lần thử nhưng trợ lý vẫn báo thành công; trạng thái trả khách trái kết quả ghi sổ. |
| 8 | Dẫn điều 7.2 không tồn tại là lỗi có thể thấy ngay khi đối chiếu chính sách; số tiền đúng không làm trích dẫn trở thành đúng. |
| 9 | Khách đưa mã đơn sàn thay mã vận đơn; thiếu hướng dẫn là điểm cần khắc phục, nguyên nhân gốc vẫn là sai đầu vào. |
| 10 | Từ chối do bão đúng điều khoản bất khả kháng; kỳ vọng của khách bị lệch bởi cam kết 24 giờ trên ứng dụng. |
| 11 | Tin nhắn thoại 40 giây thuộc dạng đầu vào trợ lý chưa hỗ trợ. |
| 12 | Kết quả đúng nhưng chi phí token D05 gấp 3 lần trong 3 tuần mà không ai thấy; lỗi ngầm nằm ở chi phí. |
| 13 | Bảo hiểm đối tác nằm ngoài phạm vi; trả lời chung chung là xử lý giới hạn kém, không thay đổi nguyên nhân thiếu phạm vi. |
| 14 | Khách bấm nhầm xác nhận đã nhận tiền, khiến yêu cầu đóng sai. |
| 15 | Trễ 26 giờ chỉ được hoàn 50%, trợ lý tính 100%; nhân viên đã bắt lỗi trước khi gửi nên không phải lỗi ngầm. |
| 16 | Thông báo lúc 2:14 đúng thiết kế gửi ngay; thiết kế không phù hợp giờ nghỉ của khách. |
| 17 | Bộ nhớ đệm bảng giá cũ làm lệch 212 đơn trong 9 ngày, không ai mở lại; sai sót bị che khuất đến lúc rà soát. |
| 18 | 30.000 đ × 50% = 15.000 đ là đúng; thiếu cách tính khiến khách tưởng bị hoàn thiếu. |
| 19 | Đơn 14 tháng vượt cửa sổ truy cập 12 tháng; trợ lý nói rõ giới hạn rồi chuyển kèm tóm tắt. |
| 20 | Thiếu khóa chống trùng ở lệnh thứ 2 khiến cùng một đơn được hoàn hai lần; vi phạm yêu cầu xử lý một lần. |

Nguồn ca: [đề bài gốc](../../docs/Ngay13_Lab13_De_bai_hoc_vien.docx), mục “Hai mươi ca lỗi”. Quy tắc và đối chiếu: [hướng dẫn nhiệm vụ C](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md), slide 71 trong [slide ngày 13](../../docs/Ngay13_Slide_Launch_Economics.pdf).

## Quy tắc phân biệt cho các ca không trùng

Theo xác nhận của Toàn, không có ca bất đồng trong 20 ca. Khi so thực tế, ghi từng ca không trùng: hai nhãn ban đầu, nhãn thống nhất và một câu quy tắc; nếu dưới 16/20 thì bổ sung định nghĩa đã viết lại.

Các quy tắc dùng để giải thích, chưa phải kết quả hòa giải:

- Ca 6, 9: đầu vào hoặc lựa chọn sai thuộc Do người dùng; cải thiện giao diện nằm ở cách khắc phục.
- Ca 8, 15: lỗi đã lộ qua đối chiếu hoặc xem lại thuộc Hệ thống; Ngầm cần có sai sót chưa được nhận ra trước kiểm tra.
- Ca 12: kết quả đúng vẫn có lỗi Ngầm khi chi phí bất thường không ai phát hiện.
- Ca 13: ngoài phạm vi thuộc Giới hạn hệ thống; việc trả lời không rõ giới hạn là vấn đề cần sửa.
- Ca 18: phép tính đúng nhưng kỳ vọng khách lệch thuộc Ngữ cảnh, không đổi thành Hệ thống chỉ vì khách mở lại.
- Slide 71 chấp nhận lập luận Hệ thống ở ca 6 và 13 trong một số cách giải thích; phải giữ nhãn độc lập ban đầu rồi ghi lý do thống nhất riêng.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed` có `trace_id`, `request_id`, `input_type`, `reason`; hằng ngày cảnh báo nếu sai loại mã >2% yêu cầu nhập mã. | Nhận diện mã đơn sàn, đổi sang mã vận đơn nếu có liên kết; nếu không tra được thì hướng dẫn vị trí mã và cho sửa trước khi gửi lại. | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát mỗi giờ `refund_success_notified` với `refund_ledger_write` theo `request_id`, `trace_id`; cảnh báo ngay khi ≥1 thông báo thành công không có ghi sổ `ok`. | Chỉ báo đã hoàn sau xác nhận ghi sổ; hết 3 lần thử mà vẫn lỗi thì báo đang xử lý, chuyển nhân viên; dùng khóa chống trùng cho các lần thử. | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Hằng tuần so `ticket_reopened` có `reason=so_tien` với `audit_sample_checked`; cảnh báo nếu >2% yêu cầu hoàn đã đóng bị mở lại dù số tiền được kiểm là đúng. | Hiển thị phí gốc, tỷ lệ và phép tính 30.000 đ × 50% = 15.000 đ; kiểm tra lại tỷ lệ mở lại theo tuần. | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` có `reason=thieu_du_lieu_chang_quoc_te`, `trace_id`; kiểm tra hằng ngày, cảnh báo khi ≥1 ca thiếu dữ liệu nhưng không chuyển nhân viên. | Chặn tự xử lý chặng không có dữ liệu, chuyển kèm tóm tắt và danh sách dữ liệu thiếu; loại quốc tế khỏi phạm vi pilot. | PM trợ lý hoàn phí |
| 17 | Ngầm | Kiểm toán ngẫu nhiên 100 đơn/tuần bằng `audit_sample_checked`, đối chiếu phiên bản bảng giá theo ngày hiệu lực; cảnh báo khi ≥1/100 đơn sai tiền hoặc ≥1 lượt dùng phiên bản hết hiệu lực. | Vô hiệu bộ nhớ đệm khi bảng giá đổi; ghi `policy_version` và `tariff_version` vào trace; kế toán rà 212 đơn bị ảnh hưởng trước khi điều chỉnh. | Kế toán trưởng |

Các event, ngưỡng và hành động trên là **đề xuất**, chưa có bằng chứng đã triển khai hay kiểm thử. Mỗi event cần thêm thời điểm phát sinh và `trace_id`; chủ nhiệm vụ E đưa các event này vào đặc tả chung. Ca 20 cần kiểm thử khóa chống trùng trước khi mở pilot, dù không nằm trong 5 ca đại diện.
