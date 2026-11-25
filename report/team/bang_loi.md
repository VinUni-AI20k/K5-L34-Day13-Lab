# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Nguyễn Ánh Dương (Error & Metrics Analyst) · Người gắn nhãn 2: Trần Việt Anh (Gatekeeper, giữ hồ sơ) (gắn trong 8 phút, không trao đổi)

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

Bốn câu hỏi nhóm dùng khi thống nhất nhãn (theo nguyên nhân gốc):

- **Do người dùng hay Hệ thống:** đầu vào của khách sai thì là Do người dùng, kể cả khi trợ lý xử lý kém; phần "trợ lý nên gợi ý" ghi ở cột khắc phục.
- **Hệ thống hay Ngầm:** sai đã lộ ra (khách mở lại, nhân viên bắt được, trích dẫn nhìn thấy) là Hệ thống; Ngầm chỉ khi 0 người nhận ra cho tới lúc kiểm tra mẫu.
- **Hệ thống hay Ngữ cảnh:** vi phạm thiết kế/chính sách là Hệ thống; làm đúng 100% thiết kế nhưng giả định lệch hoàn cảnh của khách là Ngữ cảnh.
- **Giới hạn hệ thống:** thiếu dữ liệu, ngoài phạm vi hoặc dạng đầu vào không đọc được thì là Giới hạn, kể cả khi trợ lý báo giới hạn đó kém.

## Tác động định lượng của lỗi trong đợt chạy thử

Tính từ `src/logix_runs.csv` và `src/logix_requests.csv` (1.200 yêu cầu, 1.624 lần chạy).

| Dấu hiệu lỗi | Con số trong đợt chạy thử | Ý nghĩa cho bảng khắc phục |
| --- | --- | --- |
| Lần chạy lỗi (`status = loi`) | 572/1.624 lần = 35,2%; tốn 123.179 đ token + tool | Lần lỗi vẫn tốn tiền, nên tử số chi phí tính cả lần lỗi |
| Chạy lại (lần 2 và 3) | 424 lần, 93.804 đ; riêng quoc_te 198 lần, 46.218 đ (49%) | quoc_te lần 1 ok 30%, lần 2 11,4%, lần 3 2,2%: chạy lại không cứu được lỗi Giới hạn |
| Chuyển nhân viên (`chuyen_nhan_vien`) | 148 ca = 12,3%; 91 ca quoc_te, 23 doi_tac | Nhân viên làm thay 148 × 12.000 đ = 1.776.000 đ |
| Làm lại (`lam_lai`) | 74 ca = 6,2%; 1.132 phút = 2.264.000 đ [simulated], 51,8% tổng chi phí [simulated] | Khoản chi phí lớn nhất, nên lỗi Hệ thống là ưu tiên sửa số 1 |
| Lỗi lọt đến khách (`mo_lai_trong_7_ngay`) | 51/1.200 = 4,25%; cả 51 ca đều là `lam_lai` (69% số ca làm lại) | Trong phạm vi noi_dia + hang_nang là 3,97% (39/982): mốc cho luật dừng an toàn |

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| ... | Do người dùng | ... | ... | ... |
| ... | Hệ thống | ... | ... | ... |
| ... | Ngữ cảnh | ... | ... | ... |
| ... | Giới hạn hệ thống | ... | ... | ... |
| ... | Ngầm | ... | ... | ... |
