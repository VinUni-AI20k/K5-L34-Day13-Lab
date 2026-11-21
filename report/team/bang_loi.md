# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Vũ Quang Minh · Người gắn nhãn 2: Nguyễn Văn Vinh (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Ngầm | Do người dùng | Không | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Giới hạn hệ thống | Ngữ cảnh | Không | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Ngữ cảnh | Hệ thống | Không | Hệ thống |
| 9 | Giới hạn hệ thống | Do người dùng | Không | Do người dùng |
| 10 | Giới hạn hệ thống | Ngữ cảnh | Không | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Hệ thống | Ngầm | Không | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Hệ thống | Ngữ cảnh | Không | Ngữ cảnh |
| 17 | Hệ thống | Ngầm | Không |Ngầm |
| 18 | Ngữ cảnh | Hệ thống | Không |Ngữ cảnh  |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 11 / 20 = 55%

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

### Định nghĩa đã viết lại (đồng thuận 55% < 80%)

Hai người lẫn nhau ở bốn cặp loại. Từ nay hỏi theo thứ tự dưới đây, dừng ở câu đầu tiên trả lời "có":

1. **Do người dùng trước tiên:** đầu vào hoặc thao tác của khách có sai không? Có thì là Do người dùng; cách trợ lý phản ứng với đầu vào sai thuộc cột khắc phục, không đổi nhãn.
2. **Giới hạn hệ thống ↔ Ngữ cảnh:** Giới hạn chỉ dùng khi trợ lý không thể đưa ra kết quả (thiếu dữ liệu, ngoài phạm vi, dạng đầu vào không xử lý được). Đã đưa ra kết quả đúng thiết kế thì không phải Giới hạn.
3. **Hệ thống ↔ Ngữ cảnh:** so mọi phần của đầu ra (số tiền, hành động, căn cứ trích dẫn, thông báo) với thiết kế và chính sách. Có một phần sai là Hệ thống; tất cả đều đúng mà khách vẫn thấy sai là Ngữ cảnh.
4. **Hệ thống ↔ Ngầm:** sai đã lộ ra (khách phản ánh, nhân viên bắt được, cảnh báo kích) là Hệ thống; chỉ phát hiện qua kiểm tra mẫu hoặc đối soát là Ngầm. "Sai" gồm cả sai về chi phí, không chỉ sai câu trả lời.

### Quy tắc cho từng ca không trùng

- **Ca 1 (Do người dùng):** gốc lỗi là khách nhập thiếu hai chữ số tài khoản; ngân hàng đã trả lỗi nên sai đã lộ ra, không phải Ngầm.
- **Ca 3 (Ngữ cảnh):** trợ lý hoàn về ví LogiX trong 5 phút đúng thiết kế; chỉ giả định "khách biết tiền về ví" không khớp, và trợ lý vẫn làm được nên không phải Giới hạn.
- **Ca 8 (Hệ thống):** trích dẫn điều 7.2 không tồn tại là đầu ra sai so với chính sách và nhìn thấy được, nên là Hệ thống dù số tiền hoàn đúng.
- **Ca 9 (Do người dùng):** gốc lỗi là khách nhập mã đơn của sàn thay vì mã vận đơn; việc trợ lý không gợi ý gì là chỗ cần sửa, không phải nguyên nhân gốc.
- **Ca 10 (Ngữ cảnh):** từ chối theo điều khoản bất khả kháng là đúng chính sách; khách thấy vô lý vì ứng dụng vẫn hiện "cam kết giao 24 giờ", tức giả định không khớp hoàn cảnh.
- **Ca 12 (Ngầm):** kết quả đúng nhưng tiền token của D05 gấp 3 lần suốt 3 tuần mà không ai thấy; sai về chi phí và chưa lộ ra nên là Ngầm, không phải Hệ thống.
- **Ca 16 (Ngữ cảnh):** gửi Zalo lúc 2:14 sáng đúng thiết kế "gửi ngay khi xong", không vi phạm chính sách; chỉ giả định giờ gửi không khớp hoàn cảnh khách.
- **Ca 17 (Ngầm):** dùng bảng giá cũ là sai, nhưng 212 đơn trong 9 ngày không ai mở lại và không cảnh báo nào kích, nên là Ngầm.
- **Ca 18 (Ngữ cảnh):** 15.000 đ là đúng chính sách (30.000 đ × 50%); chỉ giả định "khách hiểu cách tính" không khớp, nên là Ngữ cảnh, không phải Hệ thống.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `ma_don_khong_hop_le` (kèm `trace_id`, định dạng mã khách nhập); cảnh báo khi > 3% yêu cầu trong ngày, xem báo cáo hằng ngày | Nhận diện định dạng mã đơn của sàn TMĐT, tự tra ra mã vận đơn tương ứng hoặc chỉ khách chỗ lấy mã vận đơn; không dừng ở "mã không hợp lệ" | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát mỗi giờ theo `trace_id`: event `bao_khach_da_hoan` không có bản ghi tương ứng trong sổ cái; ngưỡng > 0 ca thì cảnh báo ngay | Chỉ báo "đã hoàn" khi sổ cái xác nhận ghi thành công; lỗi sau 3 lần thử thì báo khách "đang xử lý" và chuyển nhân viên kèm `trace_id` | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Event `mo_lai_yeu_cau` với lý do "hoàn thiếu" mà số tiền đã hoàn đúng chính sách; cảnh báo khi > 2% số yêu cầu đã hoàn trong tuần, xem hằng tuần | Tin nhắn hoàn tiền luôn kèm cách tính (ví dụ: phí giao 30.000 đ × 50% = 15.000 đ) và điều khoản áp dụng | PM trợ lý hoàn phí |
| 13 | Giới hạn hệ thống | Event `ngoai_pham_vi` theo chủ đề (bảo hiểm hàng hoá); kiểm tra mẫu 20 hội thoại chủ đề ngoài phạm vi mỗi tuần, ngưỡng > 0 ca trợ lý trả lời chung chung thay vì chuyển | Nhận diện yêu cầu ngoài phạm vi, nói rõ trợ lý không xử lý được và chuyển sang nhân viên hoặc đối tác bảo hiểm kèm tóm tắt, như cách đã làm ở ca 19 | Trưởng nhóm CSKH |
| 12 | Ngầm | Event `agent_run` có `depot`, `tokens_in`, `tokens_out`, `tool_calls`; cảnh báo khi chi phí token trung bình mỗi yêu cầu của một depot > 1,5 lần trung vị các depot trong 3 ngày liên tiếp, chạy hằng ngày | Sửa tool tra đơn của D05 để trả đủ trường; giới hạn số lần gọi tool mỗi yêu cầu và ghi lỗi khi tool trả thiếu trường | Kỹ sư trưởng agent |
