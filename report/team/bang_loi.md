# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1 là **Nguyễn Thế Hoàng**. Người gắn nhãn 2 là **Vũ Đức Anh**. Hai bộ nhãn được ghi độc lập trước khi đối chiếu.

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Giới hạn hệ thống | Ngữ cảnh | Không | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Ngầm | Hệ thống | Không | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Hệ thống | Giới hạn hệ thống | Không | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận trước khi thảo luận:** 17/20 ca trùng = **85%**, đạt ngưỡng 80%. Hai bộ nhãn gốc khác nhau ở ca 3, 8 và 13.

## Quy tắc phân biệt cho các ca không trùng

Hai người thống nhất ba ca khác nhãn theo các dấu hiệu về nguyên nhân gốc dưới đây.

- **Ca 3 – Ngữ cảnh.** Trợ lý hoàn tiền vào ví LogiX đúng thiết kế, trong khi khách chờ tiền về tài khoản ngân hàng.
- **Ca 8 – Hệ thống.** Trợ lý viện dẫn một điều khoản không có trong chính sách hiện hành. Sai sót xuất hiện ngay trong nội dung trả lời, dù số tiền hoàn đúng.
- **Ca 13 – Giới hạn hệ thống.** Hoàn phí bảo hiểm thuộc sản phẩm của đối tác và nằm ngoài phạm vi trợ lý. Cách trả lời mơ hồ là điểm cần khắc phục khi gặp yêu cầu ngoài phạm vi.

Nguồn đối chiếu: [đề bài 20 ca](../../docs/Ngay13_Lab13_De_bai_hoc_vien.docx) và [nhãn tham khảo](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md#nhãn-tham-khảo-cho-20-ca). Bộ nhãn thống nhất khớp **20/20** nhãn tham khảo.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Năm ca dưới đây đại diện cho năm loại lỗi theo bộ nhãn thống nhất.

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Kiểm tra định dạng tài khoản ngay khi khách nhập. Chặn gửi nếu số chữ số không đúng định dạng đã cấu hình cho ngân hàng đã chọn | Báo trường cần sửa và yêu cầu khách xác nhận lại trước khi tạo lệnh | Quản lý sản phẩm luồng hoàn phí |
| 7 | Hệ thống | Đối soát mỗi thông báo thành công với bản ghi sổ cái theo `trace_id`. Cảnh báo ngay khi có một thông báo thiếu bản ghi thành công | Chỉ xác nhận hoàn tiền sau khi sổ cái trả thành công. Nếu hết số lần thử, báo đang xử lý và chuyển nhân viên | Kỹ sư trưởng phụ trách trợ lý |
| 18 | Ngữ cảnh | Khi soạn thông báo, kiểm tra các ca hoàn một phần có đủ phí gốc, tỉ lệ và số tiền hoàn. Báo thiếu nếu thiếu bất kỳ trường nào | Hiển thị phép tính trong thông báo. Nếu thiếu dữ liệu, chuyển nhân viên giải thích cho khách | Trưởng nhóm CSKH |
| 19 | Giới hạn hệ thống | Kiểm tra tuổi đơn ở mỗi yêu cầu. Ghi sự kiện chuyển nhân viên nếu đơn nằm ngoài cửa sổ truy cập 12 tháng | Giải thích giới hạn cho khách và chuyển cùng bản tóm tắt để nhân viên tra cứu hồ sơ cũ | Trưởng ca vận hành hoàn phí |
| 17 | Ngầm | Đối chiếu mẫu đơn dưới 2 kg với phiên bản bảng giá có hiệu lực sau mỗi lần cập nhật và hằng tuần. Mở sự cố khi phát hiện ít nhất một khoản lệch | Làm mới bộ nhớ đệm khi đổi giá, lưu phiên bản bảng giá trong trace và rà soát các khoản hoàn bị ảnh hưởng | Kế toán trưởng |
