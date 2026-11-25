# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Đào Ngọc Hân · Người gắn nhãn 2: Trần Trọng Đức Tài (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 20 / 20 = **100%** (đạt mục tiêu ≥ 80%; phân bố: 4 Do người dùng, 5 Hệ thống, 4 Ngữ cảnh, 4 Giới hạn hệ thống, 3 Ngầm).

## Quy tắc phân biệt cho các ca không trùng

Không có ca bất đồng giữa hai bộ nhãn độc lập (đồng thuận 20/20 = 100%). Nhóm chốt thêm 5 quy tắc ranh giới cho các ca dễ lẫn khi bảo vệ Gate 2a:

- **Ca 6, 9 (`Do người dùng`, không phải `Hệ thống`):** Nguyên nhân gốc là khách chọn sai mục hoặc nhập sai loại mã; việc trợ lý thiếu gợi ý sửa là cải tiến nằm ở cột khắc phục.
- **Ca 8, 15 (`Hệ thống`, không phải `Ngầm`):** Lỗi đã lộ ra trước hoặc ngay khi giao tiếp (trích dẫn điều khoản không tồn tại, nhân viên xem lại phát hiện tính sai), còn `Ngầm` chỉ dùng khi cả khách lẫn hệ thống đều không nhận ra cho đến khi kiểm tra mẫu.
- **Ca 12 (`Ngầm`, không phải `Hệ thống`):** Câu trả lời đúng nhưng tiền token ở depot D05 tăng gấp 3 lần suốt 3 tuần không ai phát hiện — lỗi ngầm bao gồm cả sai lệch chi phí kéo dài.
- **Ca 13 (`Giới hạn hệ thống`, không phải `Hệ thống`):** Sản phẩm bảo hiểm đối tác nằm ngoài phạm vi xử lý của trợ lý nên gốc lỗi là giới hạn hệ thống, dù cách trả lời chung chung cần được khắc phục.
- **Ca 18 (`Ngữ cảnh`, không phải `Hệ thống`):** Số tiền hoàn 15.000 đ đúng chính sách (50% của 30.000 đ), chỉ giả định khách tự hiểu cách tính là không khớp hoàn cảnh của khách.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed`; cảnh báo khi vượt 2% tổng số yêu cầu/ngày (tần suất: hằng ngày) | Nhận diện mã sàn TMĐT và tra sang mã vận đơn; không tra được thì hướng dẫn kèm ảnh | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát hằng giờ giữa tin nhắn "đã hoàn" và event `refund_ledger_write` (`ket_qua = ok`) cùng `trace_id`; ngưỡng 0 ca lệch | Chỉ báo "đã hoàn" khi sổ cái trả ok; lỗi 503 sau 3 lần thì báo "đang xử lý" và chuyển nhân viên | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Event `ticket_reopened` (`reopen_reason = khieu_nai_so_tien`) đối chiếu `audit_sample_checked` (`lech_tien = 0`); cảnh báo khi vượt 1% đơn đóng/tuần (tần suất: hằng tuần) | Mẫu tin nhắn luôn ghi rõ cách tính chi tiết: 30.000 đ × 50% = 15.000 đ | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` (`reason = thieu_du_lieu`) tách theo `loai`; cảnh báo khi vượt 5% yêu cầu trong phạm vi pilot/tuần (tần suất: hằng tuần) | Giữ cách chuyển tiếp kèm tóm tắt; loại bỏ loại `quoc_te` ra khỏi phạm vi pilot | PM trợ lý hoàn phí |
| 17 | Ngầm | Event `audit_sample_checked` kiểm tra mẫu 100 đơn/tuần so với bảng giá hiện hành; cảnh báo khi vượt 1% đơn lệch (tần suất: hằng tuần) | Xóa bộ nhớ đệm khi có bảng giá mới, ghi `price_table_version` vào trace | Kế toán trưởng |
