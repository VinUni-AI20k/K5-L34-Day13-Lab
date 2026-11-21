# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: TV3 (chờ điền họ tên; bộ nhãn do người dùng cung cấp) · Người gắn nhãn 2: ...

Yêu cầu: gắn độc lập trong 8 phút, không trao đổi. TV4 chỉ xem bộ nhãn 1 sau khi đã chốt bộ nhãn riêng; chưa xác nhận thời điểm thực hiện của từng người.

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | ... | ... | ... |
| 2 | Hệ thống | ... | ... | ... |
| 3 | Ngữ cảnh | ... | ... | ... |
| 4 | Giới hạn hệ thống | ... | ... | ... |
| 5 | Ngầm | ... | ... | ... |
| 6 | Do người dùng | ... | ... | ... |
| 7 | Hệ thống | ... | ... | ... |
| 8 | Hệ thống | ... | ... | ... |
| 9 | Do người dùng | ... | ... | ... |
| 10 | Ngữ cảnh | ... | ... | ... |
| 11 | Giới hạn hệ thống | ... | ... | ... |
| 12 | Ngầm | ... | ... | ... |
| 13 | Giới hạn hệ thống | ... | ... | ... |
| 14 | Do người dùng | ... | ... | ... |
| 15 | Hệ thống | ... | ... | ... |
| 16 | Ngữ cảnh | ... | ... | ... |
| 17 | Ngầm | ... | ... | ... |
| 18 | Ngữ cảnh | ... | ... | ... |
| 19 | Giới hạn hệ thống | ... | ... | ... |
| 20 | Hệ thống | ... | ... | ... |

**Tỉ lệ đồng thuận:** Chưa tính — chờ bộ nhãn 2; chưa có nhãn thống nhất.

## Bộ nhãn 1 — giải thích do người dùng cung cấp

Giữ nguyên phân loại và lập luận người dùng đã gửi; chỉ bỏ thẻ HTML và khoảng trắng thừa. Chưa có bộ nhãn 2 để tính đồng thuận.

| Ca | Loại lỗi | Giải thích ngắn gọn |
| --: | --- | --- |
| 1 | Do người dùng | Khách nhập thiếu 2 chữ số tài khoản (thao tác/nhập liệu sai từ phía người dùng). |
| 2 | Hệ thống | Kiện 28 kg thuộc hàng nặng nhưng trợ lý gọi tool sai tham số (hàng thường), dẫn đến hoàn thiếu tiền và bị mở lại. |
| 3 | Ngữ cảnh | Trợ lý làm đúng thiết kế (hoàn về ví LogiX trong 5 phút), nhưng người dùng kỳ vọng tiền về tài khoản ngân hàng nên thấy sai. |
| 4 | Giới hạn hệ thống | Thiếu dữ liệu chặng do hãng nước ngoài giao nên trợ lý không xác định được trạng thái và chuyển cho nhân viên. |
| 5 | Ngầm | Tính hoàn sai trên 14 đơn có mã giảm giá nhưng không ai phát hiện (không khách nào báo, không có cảnh báo) cho đến khi kiểm tra mẫu cuối tuần. |
| 6 | Do người dùng | Khách chọn nhầm mục "Hoàn phí giao trễ" trong khi nội dung mô tả là hàng bị vỡ. |
| 7 | Hệ thống | API sổ cái lỗi 503 và thử lại 3 lần không thành công nhưng trợ lý vẫn báo "đã hoàn tiền thành công" (lỗi chức năng trong phạm vi). |
| 8 | Hệ thống | Trợ lý dẫn sai căn cứ ("Điều 7.2" không tồn tại trong bản chính sách hiện hành). |
| 9 | Do người dùng | Khách nhập sai loại mã (mã đơn sàn TMĐT thay vì mã vận đơn). |
| 10 | Ngữ cảnh | Trợ lý xử lý đúng chính sách bất khả kháng khi bão, nhưng kỳ vọng của khách bị lệch vì app vẫn hiển thị "cam kết giao 24 giờ". |
| 11 | Giới hạn hệ thống | Đầu vào âm thanh (tin nhắn thoại 40 giây) không xử lý được do năng lực/định dạng hỗ trợ của trợ lý. |
| 12 | Ngầm | Tool ở depot D05 trả thiếu trường làm tăng gấp 3 lần chi phí token suốt 3 tuần mà không ai nhận ra cho đến khi rà soát/kiểm tra. |
| 13 | Giới hạn hệ thống | Bảo hiểm hàng hóa của đối tác nằm ngoài phạm vi hỗ trợ của trợ lý. |
| 14 | Do người dùng | Khách bấm nhầm nút "Xác nhận đã nhận tiền" khi chưa nhận khiến yêu cầu bị đóng. |
| 15 | Hệ thống | Đơn trễ 26 giờ (đúng ra hoàn 50%) nhưng trợ lý tính hoàn 100% — sai so với chính sách. |
| 16 | Ngữ cảnh | Trợ lý làm đúng thiết kế ("gửi ngay khi xong") nhưng gửi lúc 2:14 sáng không phù hợp hoàn cảnh/kỳ vọng nghỉ ngơi của người dùng. |
| 17 | Ngầm | Dùng bảng giá cũ trong bộ nhớ đệm làm lệch tiền 212 đơn suốt 9 ngày nhưng không ai mở lại, chỉ lộ ra khi kiểm tra/đối soát. |
| 18 | Ngữ cảnh | Trợ lý tính đúng số tiền nhưng thiếu giải thích cách tính khiến người dùng hiểu nhầm là hoàn thiếu và mở lại yêu cầu. |
| 19 | Giới hạn hệ thống | Dữ liệu đơn từ 14 tháng trước vượt quá giới hạn truy cập dữ liệu 12 tháng của trợ lý. |
| 20 | Hệ thống | Thiếu cơ chế khóa chống trùng (idempotency/dedup) ở lệnh thứ hai khiến hệ thống hoàn tiền hai lần cho cùng một đơn. |

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- ...

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| ... | Do người dùng | ... | ... | ... |
| ... | Hệ thống | ... | ... | ... |
| ... | Ngữ cảnh | ... | ... | ... |
| ... | Giới hạn hệ thống | ... | ... | ... |
| ... | Ngầm | ... | ... | ... |

## Hướng dẫn thực hiện CP3 (TV3 chuẩn bị)

**Trạng thái: đã lưu bộ nhãn 1 do người dùng cung cấp; chờ bộ nhãn 2 và chưa có kết quả đồng thuận.**
Không dùng gợi ý hoặc đáp án mẫu để điền hai bộ nhãn độc lập. Mỗi người ghi riêng trong 8 phút; chỉ đối chiếu hai bộ nhãn sau khi cả hai đã chốt. Không sửa nhãn ban đầu sau khi so sánh.

### Định nghĩa thao tác trước khi gắn nhãn

| Loại | Câu hỏi để phân biệt |
| --- | --- |
| Do người dùng | Đầu vào hoặc thao tác của người dùng sai có phải nguyên nhân gốc không |
| Hệ thống | Chức năng trong phạm vi có bị lỗi và lỗi đã lộ ra trong xử lý không |
| Ngữ cảnh | Hệ thống có hiểu sai hoàn cảnh, nhu cầu hoặc kỳ vọng dù thao tác/kết quả kỹ thuật có thể đúng không |
| Giới hạn hệ thống | Yêu cầu có vượt phạm vi, năng lực hoặc dữ liệu hệ thống được thiết kế để xử lý không |
| Ngầm | Sai sót có tồn tại mà người dùng/nhân viên không nhận ra, chỉ phát hiện khi kiểm tra hoặc đối soát không |

Gắn theo nguyên nhân gốc; nơi cần sửa không tự quyết định loại lỗi. Nếu chưa rõ nguyên nhân, ghi lý do cần kiểm chứng, không tự bịa dữ kiện của ca.

### Cách tính và lưu bằng chứng

- Sau khi hai người chốt: số ca trùng = tổng các dòng có cùng nhãn ban đầu; đồng thuận = số ca trùng / 20 × 100%.
- Đạt từ 16/20 = 80%. Nếu thấp hơn: ghi định nghĩa đã sửa, lưu nguyên kết quả lần đầu; tách riêng mọi lần gắn lại.
- Với mỗi ca bất đồng, ghi số ca, hai nhãn ban đầu, nhãn thống nhất và một câu quy tắc phân biệt dựa trên mô tả ca.
- Mỗi loại chọn một ca sau khi thống nhất. Bảng dưới chỉ là đề xuất thiết kế, chưa phải kết quả phân loại 20 ca và chưa thay bảng nộp ở trên.

### Thư viện khắc phục đề xuất — cần đối chiếu ca thực tế

Các ngưỡng sau là ngưỡng đề xuất của nhóm, không phải số liệu quan sát.

| Loại | Phát hiện đo được (đề xuất) | Khắc phục (đề xuất) | Vai trò phụ trách |
| --- | --- | --- | --- |
| Do người dùng | Event input_validation_failed có trace_id, reason; rà hằng ngày nếu >2% yêu cầu | Kiểm tra định dạng, chỉ rõ trường cần sửa; không suy đoán mã đơn | PM trợ lý hoàn phí |
| Hệ thống | Đối soát refund_ledger_write với thông báo hoàn mỗi giờ; cảnh báo ngay khi có 1 thông báo thành công không có ghi sổ thành công | Chỉ xác nhận sau khi ghi sổ thành công; khóa chống trùng, chuyển nhân viên nếu ghi sổ lỗi | Kỹ sư trưởng agent |
| Ngữ cảnh | Ghi reason của ticket_reopened; rà hằng tuần mọi ca mở lại do chưa hiểu cách tính | Hiển thị cách tính, điều kiện áp dụng; hỏi lại khi thiếu thông tin ngữ cảnh | Trưởng nhóm CSKH |
| Giới hạn hệ thống | Event handoff_to_staff có reason, loai, trace_id; kiểm tra hằng tuần số ca ngoài phạm vi vẫn tự xử lý, ngưỡng 0 | Chặn ngoài phạm vi; chuyển nhân viên kèm tóm tắt và lý do | PM trợ lý hoàn phí |
| Ngầm | Event audit_sample_checked; kiểm tra ngẫu nhiên 100 đơn/tuần so với chính sách hiện hành, cảnh báo khi ít nhất 1 đơn lệch | Ghi phiên bản chính sách/bảng giá, vô hiệu hóa cache cũ; đối soát và sửa các đơn chịu ảnh hưởng | Kế toán trưởng |

### Việc còn lại do hai người gắn nhãn thực hiện

- [ ] Điền tên và thời điểm chốt của từng người.
- [x] Lưu bộ nhãn 1 đủ 20 ca và giải thích do người dùng cung cấp.
- [ ] TV4 hoàn thành và chốt bộ nhãn 2 độc lập trước khi xem bộ nhãn 1.
- [ ] Tính đồng thuận từ nhãn thực tế; giải thích các ca bất đồng.
- [ ] Gắn số ca thực tế vào 5 dòng khắc phục, điều chỉnh biện pháp đúng mô tả ca.
- [ ] TV4 kiểm tra event ở bảng khắc phục được đặc tả trong chi_so.md.
