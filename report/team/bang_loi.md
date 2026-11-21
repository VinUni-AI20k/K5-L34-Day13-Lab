# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Phân loại theo nguyên nhân gốc, không theo nơi cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Nguyễn Thùy Lam · Người gắn nhãn 2: **Chờ thành viên thứ hai tự gắn nhãn độc lập**.

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Chờ nhãn độc lập | — | Chờ so nhãn |
| 2 | Hệ thống | Chờ nhãn độc lập | — | Chờ so nhãn |
| 3 | Ngữ cảnh | Chờ nhãn độc lập | — | Chờ so nhãn |
| 4 | Giới hạn hệ thống | Chờ nhãn độc lập | — | Chờ so nhãn |
| 5 | Ngầm | Chờ nhãn độc lập | — | Chờ so nhãn |
| 6 | Do người dùng | Chờ nhãn độc lập | — | Chờ so nhãn |
| 7 | Hệ thống | Chờ nhãn độc lập | — | Chờ so nhãn |
| 8 | Hệ thống | Chờ nhãn độc lập | — | Chờ so nhãn |
| 9 | Do người dùng | Chờ nhãn độc lập | — | Chờ so nhãn |
| 10 | Ngữ cảnh | Chờ nhãn độc lập | — | Chờ so nhãn |
| 11 | Giới hạn hệ thống | Chờ nhãn độc lập | — | Chờ so nhãn |
| 12 | Ngầm | Chờ nhãn độc lập | — | Chờ so nhãn |
| 13 | Giới hạn hệ thống | Chờ nhãn độc lập | — | Chờ so nhãn |
| 14 | Do người dùng | Chờ nhãn độc lập | — | Chờ so nhãn |
| 15 | Hệ thống | Chờ nhãn độc lập | — | Chờ so nhãn |
| 16 | Ngữ cảnh | Chờ nhãn độc lập | — | Chờ so nhãn |
| 17 | Ngầm | Chờ nhãn độc lập | — | Chờ so nhãn |
| 18 | Ngữ cảnh | Chờ nhãn độc lập | — | Chờ so nhãn |
| 19 | Giới hạn hệ thống | Chờ nhãn độc lập | — | Chờ so nhãn |
| 20 | Hệ thống | Chờ nhãn độc lập | — | Chờ so nhãn |

**Tỉ lệ đồng thuận:** Chưa tính; điền sau khi hai người tự gắn nhãn độc lập và cùng đối chiếu.

## Quy tắc phân biệt cho các ca không trùng

Điền sau khi hai người gắn nhãn độc lập và so sánh. Mỗi ca bất đồng cần một câu quy tắc dựa trên nguyên nhân gốc.

- Ca ...: ...

## Bảng khắc phục cho 5 ca, mỗi loại một ca

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Ghi event `input_validation_failed`; cảnh báo nếu vượt 2% yêu cầu/ngày | Nhận diện mã đơn sàn và tra sang mã vận đơn; nếu không khớp thì hướng dẫn khách kèm ví dụ | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát mỗi giờ thông báo “đã hoàn” với bản ghi sổ cái `ok` theo `trace_id`; ngưỡng 0 ca không khớp | Chỉ xác nhận hoàn tiền khi sổ cái trả `ok`; sau 3 lỗi 503 thì báo đang xử lý và chuyển nhân viên | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Theo tuần đếm ticket mở lại vì tiền hoàn, kiểm tra mẫu xác nhận số tiền đúng | Hiển thị phép tính tiền hoàn trong tin nhắn cho khách | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Theo dõi `handoff_to_staff` với lý do thiếu dữ liệu, phân theo loại yêu cầu mỗi tuần | Chuyển nhân viên kèm tóm tắt; loại ngoài phạm vi khỏi pilot | PM trợ lý hoàn phí |
| 17 | Ngầm | Kiểm tra 100 đơn/tuần với bảng giá hiện hành; cảnh báo nếu trên 1% đơn sai | Làm mới cache khi bảng giá đổi và ghi phiên bản bảng giá vào trace | Kế toán trưởng |
