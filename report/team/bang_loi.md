# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Chử Thị Ánh · Người gắn nhãn 2: Hà.

**Ánh xác nhận hai người đã rà và quyết định nhãn riêng trước khi so, sau đó thống nhất cả 20 ca.** Bộ 1 có Codex hỗ trợ, bộ 2 có Claude hỗ trợ; giữ ghi nhận nguồn AI. Việc rà riêng được ghi theo xác nhận của Ánh, không ghi nhận hai bộ nhãn được tự tạo từ đầu không có AI. Giữ nguyên hai bộ nhãn đã so theo RULES.md.

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | ✓ | Do người dùng |
| 2 | Hệ thống | Hệ thống | ✓ | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | ✓ | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | ✓ | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | ✓ | Ngầm |
| 6 | Do người dùng | Do người dùng | ✓ | Do người dùng |
| 7 | Hệ thống | Hệ thống | ✓ | Hệ thống |
| 8 | Hệ thống | Hệ thống | ✓ | Hệ thống |
| 9 | Do người dùng | Do người dùng | ✓ | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | ✓ | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | ✓ | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | ✓ | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | ✓ | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | ✓ | Do người dùng |
| 15 | Hệ thống | Hệ thống | ✓ | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | ✓ | Ngữ cảnh |
| 17 | Ngầm | Ngầm | ✓ | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | ✓ | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | ✓ | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | ✓ | Hệ thống |

**Tỉ lệ đồng thuận:** 20 / 20 = 100% (tính từ hai cột nhãn đã lưu; Ánh xác nhận hai người đã rà riêng trước khi so và đồng ý kết quả).

## Quy tắc phân biệt cho các ca không trùng

Không có ca không trùng giữa hai bộ nhãn đề xuất. Quy tắc phân biệt đã dùng:

- **Hệ thống vs. Ngầm:** nếu có người (khách hoặc nhân viên) nhận ra sai → Hệ thống; nếu chỉ phát hiện khi kiểm tra mẫu → Ngầm (ca 15 là Hệ thống vì nhân viên bắt được; ca 8 là Hệ thống do viện dẫn điều khoản không tồn tại, không có chi tiết nói nhân viên phát hiện; ca 5, 12, 17 là Ngầm).
- **Do người dùng vs. Hệ thống:** gốc lỗi là khách nhập sai/chọn sai → Do người dùng, dù trợ lý chưa gợi ý tốt (ca 6, 9).
- **Giới hạn vs. Hệ thống:** yêu cầu ngoài phạm vi trợ lý → Giới hạn, kể cả khi trợ lý xử lý giới hạn kém (ca 13).
- **Ngữ cảnh:** kết quả đúng chính sách nhưng giả định không khớp hoàn cảnh khách (ca 18: số tiền đúng nhưng khách không hiểu cách tính).

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed`; cảnh báo khi quá 2% số yêu cầu/ngày | Nhận diện mã sàn TMĐT và tra sang mã vận đơn; không tra được thì hướng dẫn kèm ảnh | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát mỗi giờ: tin nhắn "đã hoàn" không có bản ghi sổ cái ok cùng `trace_id`; ngưỡng 0 ca | Chỉ báo "đã hoàn" khi sổ cái trả ok; lỗi 503 sau 3 lần thì báo "đang xử lý" và chuyển nhân viên | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Tỉ lệ mở lại vì số tiền mà kiểm tra thấy đúng, theo tuần | Mẫu tin nhắn luôn ghi cách tính: 30.000 đ × 50% = 15.000 đ | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` với reason = `thieu_du_lieu`, theo loại yêu cầu | Giữ cách chuyển kèm tóm tắt; đưa quoc_te ra khỏi pilot | PM trợ lý hoàn phí |
| 17 | Ngầm | Kiểm tra mẫu 100 đơn/tuần so với bảng giá hiện hành; ngưỡng 1% đơn lệch | Xoá bộ nhớ đệm khi có bảng giá mới, ghi phiên bản bảng giá vào trace | Kế toán trưởng |

## Lý do đề xuất bộ 1 để Ánh tự rà

Xem [dẫn chứng từng ca](dan_chung_nhan_C_bo1_Anh.md): nguyên văn 20 ca từ DOCX, nhãn đề xuất, lý do và ghi chú review của Ánh ở ca 9.

Nguồn: `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`, mục “Hai mươi ca lỗi”. Lý do bộ 1 không phải đáp án chính thức; kết quả thống nhất với Hà được ghi ở bảng phía trên.

| Ca | Lý do |
| --: | --- |
| 1 | Khách nhập thiếu hai chữ số tài khoản. |
| 2 | Trợ lý gọi tool sai loại hàng, gây hoàn thiếu. |
| 3 | Hoàn về ví đúng thiết kế nhưng khách chờ tiền vào ngân hàng. |
| 4 | Thiếu dữ liệu chặng nước ngoài, trợ lý nhận biết giới hạn và chuyển nhân viên. |
| 5 | Hoàn thừa nhưng cả khách lẫn hệ thống không phát hiện, chỉ kiểm toán thấy. |
| 6 | Khách chọn sai mục giao trễ khi thực tế hàng vỡ. |
| 7 | Ghi sổ thất bại nhưng vẫn báo hoàn tiền thành công. |
| 8 | Dẫn điều khoản không tồn tại là trả lời sai dù tiền đúng; chưa có căn cứ gọi là lỗi ngầm. |
| 9 | Khách dùng mã đơn sàn thay mã vận đơn; hướng dẫn phục hồi cũng cần cải thiện. |
| 10 | Đúng chính sách bất khả kháng nhưng không khớp kỳ vọng từ cam kết 24 giờ. |
| 11 | Âm thanh ngoài khả năng xử lý. |
| 12 | Kết quả đúng nhưng chi phí tăng kéo dài mà không ai phát hiện; lỗi ngầm vận hành. |
| 13 | Phí bảo hiểm đối tác ngoài phạm vi; trả lời chung chung là biểu hiện cần sửa. |
| 14 | Khách bấm nhầm xác nhận đã nhận tiền. |
| 15 | Tính sai mức hoàn, nhân viên bắt được trước khi gửi; không phải lỗi ngầm. |
| 16 | Gửi ngay đúng thiết kế nhưng giờ gửi không phù hợp hoàn cảnh. |
| 17 | Bảng giá cũ gây lệch tiền kéo dài mà không ai mở lại; trọng tâm là sai sót không được nhận ra. |
| 18 | Tính đúng nhưng thiếu giải thích khiến khách cho là thiếu. |
| 19 | Yêu cầu vượt cửa sổ dữ liệu 12 tháng, trợ lý nói rõ và chuyển nhân viên. |
| 20 | Thiếu khóa chống trùng làm hoàn hai lần; lỗi hệ thống dù khách gửi lại. |
