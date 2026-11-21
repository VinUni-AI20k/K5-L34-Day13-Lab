# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Thành viên 3 · Người gắn nhãn 2: Thành viên 4 (gắn độc lập trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | :---: | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Hệ thống | Không | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Ngầm | Không | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Hệ thống | Không | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 17 / 20 = 85,0% (Đạt yêu cầu tối thiểu ≥ 80%).

## Quy tắc phân biệt cho các ca không trùng

- **Ca 6 (Do người dùng vs Hệ thống):** Khách chọn sai danh mục vận đơn; nguyên nhân gốc do dữ liệu người dùng cung cấp sai lệch, việc trợ lý không nhận diện ra nằm ở khâu khắc phục.
- **Ca 8 (Hệ thống vs Ngầm):** Lỗi đã lộ ra công khai trong log và nhân viên phát hiện được ngay trên giao diện; không phải lỗi ngầm vì lỗi ngầm chỉ phát hiện được khi đối soát mẫu định kỳ.
- **Ca 13 (Giới hạn hệ thống vs Hệ thống):** Yêu cầu nằm ngoài phạm vi chính sách hiện hành của LogiX-VN (ngoài phạm vi quy định là giới hạn hệ thống, kể cả khi thông báo của trợ lý chưa tối ưu).

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed`; cảnh báo khi tỷ lệ > 2% số yêu cầu/ngày | Nhận diện mã sàn TMĐT và ánh xạ sang mã vận đơn nội bộ; nếu không tra được thì trả hướng dẫn kèm hình minh họa | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát tự động mỗi giờ: tin nhắn "đã hoàn" nhưng không có bản ghi sổ cái `ok` cùng `trace_id`; ngưỡng cảnh báo = 0 ca | Chỉ gửi thông báo "đã hoàn" sau khi sổ cái xác nhận thành công; nếu lỗi 503 quá 3 lần thì đánh dấu "đang xử lý" và chuyển nhân viên | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Theo dõi hàng tuần tỷ lệ khiếu nại/mở lại vì lý do số tiền nhưng kiểm tra lại thấy tính đúng | Chuẩn hóa mẫu tin nhắn phản hồi luôn ghi rõ công thức: Số tiền bồi thường = 30.000 đ × 50% = 15.000 đ | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` với thuộc tính `reason = thieu_du_lieu`, phân tích theo loại yêu cầu | Tự động tổng hợp dữ liệu kèm bản tóm tắt ngắn khi chuyển cho nhân viên; loại bỏ loại `quoc_te` khỏi phạm vi pilot | PM trợ lý hoàn phí |
| 17 | Ngầm | Kiểm tra ngẫu nhiên mẫu 100 hồ sơ/tuần đối soát với bảng giá hiện hành; ngưỡng kích hoạt cảnh báo khi sai lệch > 1% số đơn | Tự động làm mới bộ nhớ đệm (cache) khi ban hành bảng giá mới; gắn nhãn số phiên bản bảng giá vào từng `trace_id` | Kế toán trưởng |
