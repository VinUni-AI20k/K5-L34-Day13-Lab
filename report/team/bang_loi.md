# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Võ Thị Phương Nhung (TV1) · Người gắn nhãn 2: Nguyễn Tiến Đạt (TV2) (gắn trong 8 phút, không trao đổi). Tổng hợp và tính đồng thuận: Nguyễn Minh Phúc (TV3), bằng `src/tv3_cp3_dong_thuan.py`.

Nguồn: hai bộ nhãn được chép nguyên văn, không sửa.
- Nhãn người 1: `report/team/tv1_cp3_nhan_da_dien.md`, commit `45ce63c`.
- Nhãn người 2: `report/team/tv2_cp3_ban_giao.md`, commit `fc2dd2f`.

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

**Tỉ lệ đồng thuận:** 20 / 20 = 100% (đạt ngưỡng 16/20 = 80%). Cohen's kappa 1,00, ghi để tham khảo.

**Phân bố nhãn thống nhất:** Do người dùng 4 · Hệ thống 5 · Ngữ cảnh 4 · Giới hạn hệ thống 4 · Ngầm 3.

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- Không có ca không trùng: hai bộ nhãn khớp cả 20/20 ca, nên không cần thống nhất lại nhãn hay viết lại định nghĩa.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

Nguồn: bảng khắc phục do Nguyễn Đức Hải (TV4) soạn, lấy từ mục "CP3 · Bảng khắc phục 5 ca" trong `report/team/tv4_ban_giao.md`. Cả 5 ca chính có loại khớp nhãn thống nhất ở trên, nên dùng nguyên, không cần đổi sang ca dự phòng. Mức nền dùng để đặt ngưỡng (`cp3_nguong` trong `src/tv4_tinh_so.py`): chuyển nhân viên 3,5% trong phạm vi noi_dia + hang_nang; mở lại 7 ngày 3,97%; tiền token + tool theo depot cao nhất 1,05× trung vị.

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Event `refund_ledger_write` có `ket_qua = loi_tai_khoan` (ngân hàng từ chối), nối theo `trace_id`; đếm theo ngày, cảnh báo khi > 1% số lệnh hoàn trong ngày | Kiểm tra độ dài số tài khoản theo ngân hàng và tra tên chủ tài khoản, hỏi khách xác nhận trước khi tạo lệnh; sai thì yêu cầu nhập lại, không tạo lệnh | PM trợ lý hoàn phí |
| 20 | Hệ thống | Đối soát mỗi giờ trên `refund_ledger_write`: hơn 1 bản ghi `ok` cho cùng mã đơn; ngưỡng 0 ca, có 1 ca là kích luật dừng an toàn của pilot | Khoá chống trùng `idempotency_key` = mã đơn + loại hoàn; yêu cầu gửi lại khi đang xử lý thì gộp vào trace cũ và báo "đang xử lý"; thu hồi khoản hoàn thừa | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | `ticket_reopened` với `reason = so_tien` mà `audit_sample_checked` xác nhận số tiền đúng; tính theo tuần, cảnh báo khi > 0,5% số yêu cầu (mở lại hiện tại 3,97% trong phạm vi) | Mẫu tin nhắn luôn ghi cách tính và điều khoản: "30.000 đ × 50% (trễ 24–48 giờ) = 15.000 đ" | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | `handoff_to_staff` với `reason = thieu_du_lieu`, theo loại yêu cầu, theo tuần; cảnh báo khi tỉ lệ chuyển trong phạm vi pilot > 7% (gấp đôi mức 3,5% hiện tại) | Nhận diện chặng do hãng nước ngoài giao ngay ở bước đầu, chuyển nhân viên kèm tóm tắt, không chạy lại (quoc_te: lần 2 chỉ đúng 11,4%, lần 3 đúng 2,2%); đưa quoc_te ra khỏi pilot | PM trợ lý hoàn phí |
| 17 | Ngầm | Kiểm tra mẫu 100 đơn/tuần (`audit_sample_checked`) so với bảng giá hiện hành, ngưỡng > 1% đơn lệch; thêm cảnh báo khi phiên bản bảng giá ghi trong trace khác phiên bản hiện hành, ngưỡng 0 ca | Xoá bộ nhớ đệm khi có bảng giá mới; ghi `bang_gia_version` vào trace; tính lại và bù phần lệch cho 212 đơn | Kỹ sư trưởng agent |
