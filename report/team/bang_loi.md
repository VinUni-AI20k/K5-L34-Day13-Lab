# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Phạm Đức Hồng Đức · Người gắn nhãn 2: Bùi Lê Công Tuấn

Đức và Tuấn tự gắn nhãn độc lập đủ 20 ca, không trao đổi và không xem bộ nhãn của nhau. Sau khi cả hai chốt kết quả, nhóm mới mở hai bộ nhãn để đối chiếu, tính tỉ lệ đồng thuận và thống nhất bảng dưới đây.

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

**Tỉ lệ đồng thuận:** 20 / 20 × 100% = **100%**, đạt yêu cầu từ 16/20 = 80%. Đây là độ trùng giữa hai bộ nhãn, không phải tỉ lệ khớp đáp án giảng viên.

## Quy tắc phân biệt cho các ca không trùng

Không có ca không trùng (0/20), nên không phát sinh quy tắc giải quyết bất đồng và không cần viết lại định nghĩa do đồng thuận dưới 80%. Cột nhãn thống nhất giữ nhãn chung của hai bộ hiện có.

Các nguyên tắc dùng để giải thích những ca dễ nhầm:

- Ca 1, 6, 9, 14: chọn Do người dùng vì nhập sai, chọn sai hoặc bấm nhầm là nguyên nhân gốc; việc cần thêm kiểm tra đầu vào không tự đổi nhãn sang Hệ thống.
- Ca 7, 8, 15, 20: chọn Hệ thống vì báo sai trạng thái, dẫn căn cứ không tồn tại, áp dụng sai chính sách hoặc hoàn trùng; số tiền đúng ở ca 8 không làm viện dẫn sai trở thành đúng.
- Ca 3, 10, 16, 18: chọn Ngữ cảnh khi hệ thống làm đúng thiết kế/chính sách hoặc tính đúng tiền nhưng không khớp kỳ vọng, thời điểm hay cách hiểu của khách.
- Ca 4, 11, 13, 19: chọn Giới hạn hệ thống vì thiếu dữ liệu, thiếu khả năng xử lý đầu vào hoặc ngoài phạm vi; ca 13 còn cần cải thiện thông báo giới hạn.
- Ca 5, 12, 17: chọn Ngầm vì sai sót tiền hoặc chi phí kéo dài mà không bị nhận ra; ca 15 được nhân viên phát hiện nên khác đặc điểm này.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

Các event, ngưỡng và tần suất dưới đây là **đề xuất giám sát cho pilot**, không phải kết quả đã đo hay cơ chế đã được triển khai. Event ghi `request_id` và `trace_id` để nối tình huống với trace.

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed` có `reason = wrong_id_type`; hằng ngày đếm số yêu cầu duy nhất gặp lỗi chia tổng yêu cầu, cảnh báo khi > 2% | Nhận diện mã đơn sàn TMĐT và tra sang mã vận đơn nếu có nguồn ánh xạ; nếu không có thì hướng dẫn nơi lấy mã đúng kèm ảnh minh hoạ | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát mỗi giờ event `refund_success_notified` với `refund_ledger_write`: cảnh báo khi có ≥ 1 thông báo thành công thiếu bản ghi sổ cái `ok` tương ứng theo `request_id`, `trace_id` | Chỉ báo "đã hoàn" khi sổ cái xác nhận `ok`; lỗi 503 sau 3 lần thử thì báo chưa xác nhận hoàn tiền và chuyển nhân viên đối soát trước khi thử lại, giữ cùng khóa chống trùng | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Hằng tuần nối `ticket_reopened` có `reason = amount_dispute` với `audit_sample_checked` xác nhận tiền đúng; chia số yêu cầu này cho tổng yêu cầu đã đóng của cùng cohort đủ 7 ngày theo dõi, cảnh báo khi > 1% | Chuẩn hoá mẫu tin nhắn luôn kèm công thức tính (ví dụ: 30.000 đ × 50% = 15.000 đ) | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Hằng ngày đối chiếu `agent_scope_check` có `reason = thieu_du_lieu` với `handoff_to_staff`; cảnh báo khi có ≥ 1 yêu cầu thiếu dữ liệu không được chuyển nhân viên trong 5 phút | Kiểm tra dữ liệu trước khi kết luận; chuyển nhân viên kèm tóm tắt và nói rõ giới hạn; loại `quoc_te` khỏi phạm vi pilot theo quyết định phạm vi của nhóm | PM trợ lý hoàn phí |
| 17 | Ngầm | Kiểm tra mẫu ngẫu nhiên 100 đơn/tuần đối chiếu bảng giá có hiệu lực tại thời điểm tính hoàn; ghi `audit_sample_checked`, cảnh báo khi > 1% mẫu lệch tiền (từ 2/100 đơn) | Xoá cache khi cập nhật bảng giá, chọn phiên bản theo ngày hiệu lực và ghi thuộc tính `price_table_version` trong event/trace; rà soát các đơn dùng phiên bản sai để điều chỉnh | Kế toán trưởng |
