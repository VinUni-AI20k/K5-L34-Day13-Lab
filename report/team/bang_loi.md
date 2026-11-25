# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Quân · Người gắn nhãn 2: Hiếu (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Ngữ cảnh | Hệ thống | Không | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Hệ thống | Không | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Giới hạn hệ thống | Không | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận ban đầu:** 17/20 × 100% = **85%**.

## Quy tắc phân biệt cho các ca không trùng

Nhãn thống nhất cho ba ca dưới đây dựa trên nguyên nhân gốc và [hướng dẫn Nhiệm vụ C](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md#nhãn-tham-khảo-cho-20-ca).

- **Ca 8 — Hệ thống.** Trợ lý viện dẫn điều khoản không tồn tại trong chính sách hiện hành, dù số tiền hoàn đúng.
- **Ca 13 — Giới hạn hệ thống.** Hoàn phí bảo hiểm nằm ngoài phạm vi trợ lý, và câu trả lời cần nói rõ giới hạn đó.
- **Ca 15 — Hệ thống.** Trợ lý có đủ thông tin để áp dụng chính sách nhưng tính hoàn 100% trong khi đơn trễ 26 giờ chỉ được hoàn 50%.

### Lý do gắn nhãn đề xuất cho các ca dễ nhầm

- Ca 12: Kết quả hoàn tiền đúng nhưng chi phí tăng kéo dài mà không ai phát hiện, nên xếp lỗi ngầm.
- Ca 17: Việc dùng bảng giá cũ gây nhiều khoản hoàn lệch mà khách và hệ thống đều không phát hiện, nên xếp lỗi ngầm.
- Ca 18: Kết quả đúng nhưng thông báo thiếu căn cứ mà khách cần để hiểu số tiền, nên xếp lỗi ngữ cảnh.
- Ca 20: Khách gửi lại vì chưa có phản hồi. Việc hệ thống thực hiện hai khoản hoàn cho cùng một nghĩa vụ hoàn tiền là lỗi hệ thống.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Ghi `refund_account_validation_failed` ngay khi số tài khoản không đạt quy tắc định dạng của ngân hàng đã chọn. Đếm số lần lỗi theo ngân hàng mỗi ngày. | Kiểm tra trước khi tạo lệnh hoàn. Chỉ rõ trường sai và cho khách nhập lại, giữ nguyên các thông tin đã nhập ở các trường khác. | Kỹ sư sản phẩm |
| 7 | Hệ thống | Cảnh báo ngay nếu có `refund_success_notified` mà chưa có `ledger_refund_committed` cho cùng `refund_id`. | Chỉ báo hoàn tiền thành công sau khi sổ cái xác nhận đã ghi. Khi hết lượt thử lại, báo đang chờ xử lý và chuyển nhân viên kiểm tra. | Kỹ sư backend |
| 3 | Ngữ cảnh | Ghi `refund_destination_disputed` khi khách báo chưa nhận và nơi nhận khách mong đợi khác với nơi đã hoàn. Đếm số ca theo tuần. | Hiển thị nơi nhận là ví LogiX và thời gian dự kiến trước khi xác nhận. Sau khi hoàn, hướng dẫn khách xem giao dịch trong ví. | Nhân viên thiết kế trải nghiệm |
| 19 | Giới hạn hệ thống | Ghi `refund_outside_retention_window` cho mỗi yêu cầu có đơn cũ hơn 12 tháng. Đếm hằng tuần và kiểm tra các ca thiếu `refund_handoff_created`. | Nêu rõ giới hạn tra cứu, chuyển nhân viên xử lý và gửi kèm mã đơn, ngày giao và lý do yêu cầu. | Điều phối viên hỗ trợ |
| 5 | Ngầm | Đối soát hằng ngày các đơn có mã giảm giá. Ghi `refund_amount_mismatch` khi số đã hoàn cao hơn số tính theo phí sau giảm và chính sách áp dụng. | Lấy phí thực thu sau giảm làm căn cứ tính tiền hoàn. Chuyển mọi khoản chênh lệch phát hiện qua đối soát cho bộ phận tài chính xử lý. | Chuyên viên đối soát tài chính |
