# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`; bản trích sẵn tại `docs/20_ca_loi.md`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Nguyễn Phi Hoàng · Người gắn nhãn 2: Nguyễn Công Hoàn (gắn độc lập trong 8 phút, ngồi tách nhau, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | ✓ | Do người dùng |
| 2 | Hệ thống | Hệ thống | ✓ | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | ✓ | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Hệ thống | ✗ | Giới hạn hệ thống |
| 5 | Hệ thống | Hệ thống | ✓ | Ngầm |
| 6 | Ngữ cảnh | Ngữ cảnh | ✓ | Do người dùng |
| 7 | Hệ thống | Hệ thống | ✓ | Hệ thống |
| 8 | Hệ thống | Hệ thống | ✓ | Hệ thống |
| 9 | Do người dùng | Do người dùng | ✓ | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | ✓ | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | ✓ | Giới hạn hệ thống |
| 12 | Ngầm | Do người dùng | ✗ | Ngầm |
| 13 | Ngữ cảnh | Ngữ cảnh | ✓ | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | ✓ | Do người dùng |
| 15 | Hệ thống | Hệ thống | ✓ | Hệ thống |
| 16 | Ngầm | Ngầm | ✓ | Ngữ cảnh |
| 17 | Ngầm | Ngầm | ✓ | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | ✓ | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | ✓ | Giới hạn hệ thống |
| 20 | Ngầm | Ngầm | ✓ | Hệ thống |

**Tỉ lệ đồng thuận:** 18 / 20 = **90%**

## Quy tắc phân biệt cho các ca không trùng

- **Ca 4 — Giới hạn hệ thống, không phải Hệ thống:** trợ lý không vi phạm thiết kế nào (nói rõ không xác định được và chuyển nhân viên đúng quy trình); gốc là LogiX không có dữ liệu chặng hãng nước ngoài. Quy tắc: *thiếu dữ liệu hoặc ngoài phạm vi thì là Giới hạn hệ thống, kể cả khi trợ lý xử lý tình huống đó đúng thiết kế.*
- **Ca 12 — Ngầm, không phải Do người dùng:** không có đầu vào nào của khách là sai; "sai" ở đây là chi phí token gấp 3 lần depot khác suốt 3 tuần mà không ai nhận ra, chỉ phát hiện qua kiểm tra mẫu. Quy tắc: *"sai" gồm cả sai về chi phí, và khi chưa ai nhận ra cho tới khi kiểm tra mẫu thì là Ngầm.*

## Điều chỉnh sau đối chiếu đáp án

Sau khi hai bộ nhãn độc lập đã so và thống nhất, nhóm đối chiếu cột "Nhãn thống nhất" với bảng nhãn tham khảo trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (điều kiện "tự gắn trước rồi mới xem" đã thoả) và điều chỉnh 5 ca:

- **Ca 5 → Ngầm:** hoàn theo giá trước giảm là sai chính sách, nhưng không khách nào báo, không cảnh báo nào kích; chỉ phát hiện qua kiểm tra mẫu cuối tuần.
- **Ca 6 → Do người dùng:** gốc lỗi là khách chọn mục "Hoàn phí giao trễ" dù nội dung là hàng bị vỡ; trợ lý xử lý đúng mục đã chọn. Việc trợ lý không gợi ý là chỗ cần cải thiện, nằm ở cột khắc phục.
- **Ca 13 → Giới hạn hệ thống:** hoàn phí bảo hiểm là sản phẩm của công ty bảo hiểm đối tác, ngoài phạm vi trợ lý; ngoài phạm vi thì là giới hạn, kể cả khi trợ lý xử lý giới hạn đó kém (trả lời chung chung, không nói rõ không xử lý được).
- **Ca 16 → Ngữ cảnh:** gửi Zalo lúc 2:14 sáng đúng thiết kế "gửi ngay khi xong", kết quả đúng; chỉ giả định khách không bị làm phiền lúc nửa đêm là không khớp hoàn cảnh.
- **Ca 20 → Hệ thống:** thiếu khoá chống trùng khiến hoàn hai lần một đơn là vi phạm thiết kế, và sai đã lộ ra (khách nhận được hai lần tiền); không phải ngầm.


## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội". *Bảng do nhóm duyệt lại từ bảng mẫu trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`; mỗi dòng nhóm phải tự giải thích được trước hội đồng.*

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed`; cảnh báo khi quá 2% số yêu cầu/ngày | Nhận diện mã sàn TMĐT và tra sang mã vận đơn; không tra được thì hướng dẫn kèm ảnh | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát mỗi giờ: tin nhắn "đã hoàn" không có bản ghi sổ cái ok cùng `trace_id`; ngưỡng 0 ca | Chỉ báo "đã hoàn" khi sổ cái trả ok; lỗi 503 sau 3 lần thì báo "đang xử lý" và chuyển nhân viên | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Tỉ lệ mở lại vì số tiền mà kiểm tra thấy đúng, theo tuần | Mẫu tin nhắn luôn ghi cách tính: 30.000 đ × 50% = 15.000 đ | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` với reason = `thieu_du_lieu`, theo loại yêu cầu | Giữ cách chuyển kèm tóm tắt; đưa `quoc_te` ra khỏi pilot | PM trợ lý hoàn phí |
| 17 | Ngầm | Kiểm tra mẫu 100 đơn/tuần so với bảng giá hiện hành; ngưỡng 1% đơn lệch | Xoá bộ nhớ đệm khi có bảng giá mới, ghi phiên bản bảng giá vào trace | Kế toán trưởng |
