# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Phân loại theo nguyên nhân gốc, không theo nơi cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Nguyễn Thùy Lam (bản nháp cần Lam xác nhận) · Người gắn nhãn 2: **Chờ thành viên thứ hai tự gắn nhãn độc lập**.

> Chưa thể tính đồng thuận: hiện chưa có bộ nhãn độc lập của người thứ hai. Không sao chép nhãn của người 1 sang cột người 2; hãy để người đó tự phân loại trước khi xem bảng này.

| Ca | Nhãn người 1 (bản nháp) | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Chờ gắn độc lập | — | Chờ so nhãn |
| 2 | Hệ thống | Chờ gắn độc lập | — | Chờ so nhãn |
| 3 | Ngữ cảnh | Chờ gắn độc lập | — | Chờ so nhãn |
| 4 | Giới hạn hệ thống | Chờ gắn độc lập | — | Chờ so nhãn |
| 5 | Ngầm | Chờ gắn độc lập | — | Chờ so nhãn |
| 6 | Do người dùng | Chờ gắn độc lập | — | Chờ so nhãn |
| 7 | Hệ thống | Chờ gắn độc lập | — | Chờ so nhãn |
| 8 | Hệ thống | Chờ gắn độc lập | — | Chờ so nhãn |
| 9 | Do người dùng | Chờ gắn độc lập | — | Chờ so nhãn |
| 10 | Ngữ cảnh | Chờ gắn độc lập | — | Chờ so nhãn |
| 11 | Giới hạn hệ thống | Chờ gắn độc lập | — | Chờ so nhãn |
| 12 | Ngầm | Chờ gắn độc lập | — | Chờ so nhãn |
| 13 | Giới hạn hệ thống | Chờ gắn độc lập | — | Chờ so nhãn |
| 14 | Do người dùng | Chờ gắn độc lập | — | Chờ so nhãn |
| 15 | Hệ thống | Chờ gắn độc lập | — | Chờ so nhãn |
| 16 | Ngữ cảnh | Chờ gắn độc lập | — | Chờ so nhãn |
| 17 | Ngầm | Chờ gắn độc lập | — | Chờ so nhãn |
| 18 | Ngữ cảnh | Chờ gắn độc lập | — | Chờ so nhãn |
| 19 | Giới hạn hệ thống | Chờ gắn độc lập | — | Chờ so nhãn |
| 20 | Hệ thống | Chờ gắn độc lập | — | Chờ so nhãn |

**Tỉ lệ đồng thuận:** Chưa tính / 20; cần bộ nhãn độc lập thứ hai.

## Quy tắc phân biệt cho các ca không trùng

Ghi sau khi so nhãn. Nguyên tắc: lỗi do đầu vào của khách → Do người dùng; trợ lý vi phạm thiết kế/chính sách → Hệ thống; làm đúng nhưng kỳ vọng hoặc bối cảnh không khớp → Ngữ cảnh; vượt khả năng/dữ liệu → Giới hạn hệ thống; sai mà không ai nhận ra đến lúc kiểm tra → Ngầm.

- Ca 6 và 9: nguyên nhân gốc là khách chọn/nhập sai; trợ lý không hướng dẫn tốt là phần khắc phục.
- Ca 8 và 15: sai sót đã lộ ra trước khi gửi nên là Hệ thống, không phải Ngầm.
- Ca 12 và 17: sai lệch chỉ lộ qua kiểm tra/đối soát nên là Ngầm.
- Ca 13 và 19: ngoài phạm vi hoặc thiếu dữ liệu là Giới hạn hệ thống.
- Ca 18: số tiền đúng nhưng cách giải thích không đáp ứng kỳ vọng khách là Ngữ cảnh.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Ghi `input_validation_failed`; cảnh báo nếu vượt 2% yêu cầu/ngày | Nhận diện mã sàn và tra sang mã vận đơn; nếu không tra được thì hướng dẫn kèm ảnh | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát mỗi giờ: thông báo “đã hoàn” không có ghi sổ cái `ok` cùng `trace_id`; ngưỡng 0 ca | Chỉ báo hoàn thành khi sổ cái trả `ok`; lỗi 503 sau 3 lần thì chuyển nhân viên và báo đang xử lý | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Theo tuần đếm yêu cầu mở lại do số tiền nhưng kiểm tra thấy số tiền đúng | Hiển thị phép tính, ví dụ 30.000 đ × 50% = 15.000 đ | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Theo dõi event `handoff_to_staff` với `reason=thieu_du_lieu`, phân theo loại yêu cầu | Chuyển nhân viên kèm tóm tắt; không đưa yêu cầu quốc tế vào phạm vi pilot | PM trợ lý hoàn phí |
| 17 | Ngầm | Kiểm tra 100 đơn/tuần với bảng giá hiện hành; cảnh báo nếu trên 1% đơn lệch | Xoá cache khi bảng giá đổi và ghi phiên bản bảng giá vào trace | Kế toán trưởng |
