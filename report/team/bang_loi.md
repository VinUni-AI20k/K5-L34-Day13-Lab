# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Hoàng Minh Diệp · Người gắn nhãn 2: Nguyễn Đức Mạnh. Hai bộ nhãn được thực hiện độc lập; ba trường hợp bất đồng đã được thảo luận và thống nhất ở cột cuối.

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Hệ thống | Không | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Hệ thống | Không | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Hệ thống | Không | Hệ thống |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 17 / 20 = 85%

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- **Ca 6 — Do người dùng / Hệ thống:** khách chọn nhầm luồng, nhưng mô tả “hàng bị vỡ” mâu thuẫn với lựa chọn. Gộp về Do người dùng vì nguyên nhân trực tiếp là chọn sai; thêm bước xác nhận khi lựa chọn và nội dung không khớp.
- **Ca 13 — Giới hạn hệ thống / Hệ thống:** yêu cầu nằm ngoài phạm vi nên là giới hạn; câu trả lời chung chung là lỗi xử lý giới hạn. Gộp về Giới hạn hệ thống theo nguyên nhân gốc là phạm vi năng lực.
- **Ca 18 — Ngữ cảnh / Hệ thống:** tiền tính đúng nhưng khách hiểu là thiếu do thiếu cách tính. Gộp về Hệ thống vì đầu ra cần giải thích số tiền; đây là thiếu hụt trong phản hồi, không phải sai lệch chính sách.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, ghi rõ một vai trò chịu trách nhiệm.

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | `bank_account_validation_failed`; chặn lệnh và yêu cầu sửa ngay mỗi lần số tài khoản sai định dạng/thiếu ký tự. | Kiểm tra độ dài/định dạng trước khi tạo lệnh; nêu rõ trường nào cần sửa. | Người viết code |
| 2 | Hệ thống | `refund_quote_check`; chặn trước khi gửi nếu nhóm giá từ cân nặng khác nhóm giá tool dùng (kiểm tra 100% ca). | Đối chiếu cân nặng với bảng phân loại giá hiện hành; yêu cầu người kiểm tra duyệt mọi lệch số tiền. | Người viết code |
| 3 | Ngữ cảnh | `refund_destination_complaint`; theo dõi hàng tuần, cảnh báo nếu khiếu nại về nơi nhận tiền đạt ≥5% yêu cầu hoàn về ví trong tuần. | Trước xác nhận, nói rõ tiền về ví LogiX và thời gian dự kiến; hỏi khách có muốn tiếp tục không. | Người gắn nhãn 1 |
| 4 | Giới hạn hệ thống | `out_of_scope_detected` và `human_handoff_created`; cảnh báo ngay nếu có yêu cầu ngoài phạm vi mà không tạo chuyển tiếp. | Phát hiện yêu cầu hãng ngoài; nói rõ giới hạn, chuyển nhân viên và kèm tóm tắt trace. | Người gắn nhãn 2, kiêm giữ hồ sơ |
| 5 | Ngầm | `coupon_refund_reconciled`; chạy đối soát hàng ngày, cảnh báo nếu tiền hoàn lệch khỏi số đủ điều kiện dù chỉ 1 đ. | Đối soát giá sau giảm với số tiền hoàn; tạm dừng lệnh lệch và rà soát các đơn cùng quy tắc. | Người kiểm số |
