# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Đoàn Xuân Duy Bảo · Người gắn nhãn 2: Vũ Tiến Hùng (gắn độc lập trong 8 phút, không trao đổi; giữ nguyên bộ nhãn gốc của Hùng từ `report/team/nhan_doc_lap_hung.md` trên nhánh `hungvt`)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Hệ thống | Không | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Ngữ cảnh | Không | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Ngầm | Không | Hệ thống |
| 9 | Do người dùng | Ngữ cảnh | Không | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Hệ thống | Không | Giới hạn hệ thống |
| 14 | Do người dùng | Ngầm | Không | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Hệ thống | Không | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Giới hạn hệ thống | Không | Hệ thống |

**Tỉ lệ đồng thuận:** 12 / 20 = 60%

## Quy tắc phân biệt cho các ca không trùng

Vì đồng thuận ban đầu là 60% (< 80%), hai người gắn nhãn thống nhất lại định nghĩa 5 loại theo **nguyên nhân gốc** trước khi chốt nhãn:

- **Định nghĩa đã viết lại (do đồng thuận < 80%):**
  - **Do người dùng:** Nguyên nhân gốc là khách nhập sai định dạng, chọn sai mục hoặc bấm nhầm thao tác, dù trợ lý có thể cải thiện gợi ý/cảnh báo ở bước khắc phục.
  - **Hệ thống:** Trợ lý làm sai thiết kế, sai chính sách hoặc thiếu cơ chế kỹ thuật (như khoá chống trùng) và lỗi đã lộ ra cho khách hoặc nhân viên thấy.
  - **Ngữ cảnh:** Trợ lý làm đúng thiết kế và đúng chính sách, nhưng giả định về thói quen, thời điểm hoặc kênh nhận thông tin của khách không khớp thực tế.
  - **Giới hạn hệ thống:** Yêu cầu nằm ngoài phạm vi sản phẩm hoặc thiếu dữ liệu/năng lực đầu vào để xử lý, kể cả khi trợ lý giao tiếp lại phần giới hạn đó chưa tốt.
  - **Ngầm:** Có sai sót (về số tiền hoặc chi phí) nhưng cả khách lẫn hệ thống đều không phát hiện trong vận hành thường ngày, chỉ lộ ra khi kiểm tra mẫu hoặc đối soát.

- **Ca 3 (`Ngữ cảnh`):** Trợ lý hoàn tiền về ví LogiX trong 5 phút là đúng thiết kế, chỉ là giả định khách biết tiền về ví thay vì tài khoản ngân hàng không khớp hoàn cảnh.
- **Ca 6 (`Do người dùng`):** Nguyên nhân gốc là khách chọn nhầm mục "Hoàn phí giao trễ" dù hàng bị vỡ; việc trợ lý không đối chiếu nội dung mô tả là hướng khắc phục.
- **Ca 8 (`Hệ thống`):** Lỗi bịa trích dẫn "Điều 7.2" lộ ra ngay trong nội dung trả lời khách thấy được, không phải lỗi ẩn chỉ thấy khi kiểm tra mẫu nên không xếp vào Ngầm.
- **Ca 9 (`Do người dùng`):** Nguyên nhân gốc là khách nhập mã đơn sàn TMĐT thay vì mã vận đơn; việc trợ lý chưa gợi ý định dạng đúng nằm ở cột khắc phục.
- **Ca 13 (`Giới hạn hệ thống`):** Hoàn phí bảo hiểm đối tác nằm ngoài phạm vi dữ liệu và nghiệp vụ của trợ lý; cách trả lời chung chung chỉ là xử lý giới hạn chưa khéo.
- **Ca 14 (`Do người dùng`):** Nguyên nhân gốc là khách bấm nhầm nút "Xác nhận đã nhận tiền" khi chưa nhận, khiến hệ thống đóng yêu cầu theo đúng luồng.
- **Ca 17 (`Ngầm`):** Sai lệch 1.000–2.000 đ/đơn trên 212 đơn suốt 9 ngày mà không khách nào mở lại hay cảnh báo nào kích hoạt, chỉ phát hiện khi đối soát bảng giá.
- **Ca 20 (`Hệ thống`):** Hoàn tiền hai lần cho cùng một đơn do thiếu khoá chống trùng là lỗi thiết kế kỹ thuật của hệ thống, không phải giới hạn khả năng.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed`; cảnh báo khi vượt 2% tổng yêu cầu/ngày | Nhận diện định dạng mã đơn sàn TMĐT để tra sang mã vận đơn; nếu không tra được thì hiển thị hướng dẫn kèm ảnh minh hoạ | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát mỗi giờ giữa tin nhắn "đã hoàn" và event `refund_ledger_write` có `ket_qua = ok` cùng `trace_id`; ngưỡng 0 ca lệch | Chỉ gửi thông báo "đã hoàn" khi sổ cái trả `ok`; sau 3 lần lỗi 503 thì báo "đang xử lý" và phát `handoff_to_staff` | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Tỉ lệ `ticket_reopened` với lý do thiếu tiền nhưng kiểm tra sổ cái thấy đúng chính sách, tổng hợp theo tuần; cảnh báo khi vượt 1% yêu cầu tuần | Cập nhật mẫu tin nhắn luôn hiển thị phép tính chi tiết (ví dụ: `30.000 đ × 50% = 15.000 đ`) | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` với `reason = thieu_du_lieu_hang_ngoai` theo loại yêu cầu, theo dõi hằng ngày | Giữ cơ chế chuyển nhân viên kèm tóm tắt; loại nhóm `quoc_te` khỏi phạm vi pilot | PM trợ lý hoàn phí |
| 17 | Ngầm | Kiểm tra mẫu ngẫu nhiên 100 đơn/tuần (`audit_sample_checked`) đối chiếu bảng giá hiện hành; ngưỡng cảnh báo ≥ 1% đơn lệch | Xoá bộ nhớ đệm khi cập nhật bảng giá mới và ghi `price_table_version` vào mọi `trace_id` | Kế toán trưởng |
