# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: ... · Người gắn nhãn 2: ... (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | ... | ... | ... | ... |
| 2 | ... | ... | ... | ... |
| 3 | ... | ... | ... | ... |
| 4 | ... | ... | ... | ... |
| 5 | ... | ... | ... | ... |
| 6 | ... | ... | ... | ... |
| 7 | ... | ... | ... | ... |
| 8 | ... | ... | ... | ... |
| 9 | ... | ... | ... | ... |
| 10 | ... | ... | ... | ... |
| 11 | ... | ... | ... | ... |
| 12 | ... | ... | ... | ... |
| 13 | ... | ... | ... | ... |
| 14 | ... | ... | ... | ... |
| 15 | ... | ... | ... | ... |
| 16 | ... | ... | ... | ... |
| 17 | ... | ... | ... | ... |
| 18 | ... | ... | ... | ... |
| 19 | ... | ... | ... | ... |
| 20 | ... | ... | ... | ... |

**Tỉ lệ đồng thuận:** ... / 20 = ...%

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

**Trạng thái: chưa có nhãn do hai người tự gắn; chưa có kết quả đồng thuận.**
Không dùng gợi ý hoặc đáp án mẫu để điền hai bộ nhãn độc lập. Mỗi người ghi riêng trong 8 phút; chỉ ghép vào bảng trên sau khi cả hai đã chốt. Không sửa nhãn ban đầu sau khi so sánh.

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
- [ ] Hoàn thành độc lập đủ 20 ca, lưu nguyên hai bộ nhãn.
- [ ] Tính đồng thuận từ nhãn thực tế; giải thích các ca bất đồng.
- [ ] Gắn số ca thực tế vào 5 dòng khắc phục, điều chỉnh biện pháp đúng mô tả ca.
- [ ] TV4 kiểm tra event ở bảng khắc phục được đặc tả trong chi_so.md.
