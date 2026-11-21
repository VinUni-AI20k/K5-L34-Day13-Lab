# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn

Người gắn nhãn 1: Lê Minh Phụng · Người gắn nhãn 2: Mai Văn Thanh.

- Cột người 1: nhãn của Phụng, có đối chiếu với mục "Nhãn tham khảo cho 20 ca" trong [hướng dẫn Lab 13](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md) (ghi theo báo cáo cá nhân của Phụng).
- Cột người 2: nhãn Thanh tự gắn độc lập, không trao đổi, không xem bảng tham khảo; đã ghi vào file trước khi so.
- Hai cột gốc giữ nguyên sau khi so; chỉ cột "Nhãn thống nhất" ghi kết quả sau thảo luận.

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
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

**Tỉ lệ đồng thuận:** 18 / 20 = 90% (đạt mốc 80%, không cần viết lại định nghĩa).

Phân bố nhãn thống nhất: Do người dùng 4 (1, 6, 9, 14) · Hệ thống 5 (2, 7, 8, 15, 20) · Ngữ cảnh 4 (3, 10, 16, 18) · Giới hạn hệ thống 4 (4, 11, 13, 19) · Ngầm 3 (5, 12, 17).

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- **Ca 8 (Ngầm → Hệ thống):** sai nằm ngay trên nội dung khách và nhân viên nhìn thấy được (trích "Điều 7.2" không tồn tại), nên lỗi đã lộ ra là Hệ thống; chỉ gắn Ngầm khi không có dấu vết nhìn thấy được và chỉ hậu kiểm mới phát hiện, kể cả khi số tiền vẫn đúng.
- **Ca 13 (Hệ thống → Giới hạn hệ thống):** nguyên nhân gốc là yêu cầu nằm ngoài phạm vi (bảo hiểm của đối tác), nên là Giới hạn; việc trợ lý trả lời chung chung thay vì nói rõ không xử lý được là chỗ cần sửa, ghi ở cột khắc phục chứ không đổi nhãn.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội". Event lấy từ danh sách trong `chi_so.md`.

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | `refund_ledger_write` có `ket_qua = loi_tai_khoan` (ngân hàng trả lỗi số tài khoản), đếm theo ngày; cảnh báo khi > 1% số lệnh hoàn trong ngày | Kiểm tra độ dài và định dạng số tài khoản theo từng ngân hàng trước khi tạo lệnh; bắt khách nhập lại lần hai để đối chiếu; sai thì hỏi lại thay vì tạo lệnh | PM trợ lý hoàn phí |
| 20 | Hệ thống | Đối soát sổ cái mỗi giờ: hai bản ghi `refund_ledger_write` thành công cho cùng một mã đơn; ngưỡng 0 ca (gặp 1 ca là kích luật dừng hoàn trùng trong `pilot_plan.yaml`) | Gắn `idempotency_key` = mã đơn + loại hoàn cho mọi lệnh; lệnh gửi lại trả về kết quả của lệnh đầu thay vì tạo lệnh mới | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | `ticket_reopened` có `reason = so_tien` mà `audit_sample_checked` xác nhận số tiền đúng, tính theo tuần; cảnh báo khi > 1% số yêu cầu đã đóng | Mẫu tin nhắn hoàn tiền luôn ghi cách tính, ví dụ "Phí giao 30.000 đ × 50% (trễ 24–48 giờ) = 15.000 đ" | Trưởng nhóm CSKH |
| 19 | Giới hạn hệ thống | `handoff_to_staff` có `reason = ngoai_12_thang`, đếm theo tuần; nếu > 3% số yêu cầu thì xem xét mở rộng quyền truy cập dữ liệu cũ | Kiểm tra ngày tạo đơn ngay ở bước đầu; báo khách rõ là trợ lý không tra được và chuyển nhân viên kèm tóm tắt (giữ cách làm hiện tại), đặt hạn nhân viên phản hồi trong 24 giờ | PM trợ lý hoàn phí |
| 5 | Ngầm | `audit_sample_checked` 100 đơn/tuần, lấy mẫu ưu tiên đơn có mã giảm giá; ngưỡng 1% số đơn kiểm bị lệch hoặc 1 đơn lệch > 10.000 đ | Tính tiền hoàn trên giá sau giảm; thêm ca kiểm thử cho đơn có mã giảm giá trước mỗi lần đổi prompt hoặc tool; thu hồi khoản hoàn thừa đã phát hiện | Kế toán trưởng |
