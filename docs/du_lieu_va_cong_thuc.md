# Dữ liệu, số liệu dùng chung và công thức

Toàn bộ dữ liệu là **giả lập**. Hai file CSV nằm trong `src/`.

## Hai file dữ liệu

| File | Cột |
| --- | --- |
| `src/logix_runs.csv` | 1.624 lần chạy của agent: `run_id, request_id, trace_id, attempt, tokens_in, tokens_out, tool_calls, status` (`ok` hoặc `loi`) |
| `src/logix_requests.csv` | 1.200 yêu cầu: `depot, staff_id, loai, so_tien_vnd, so_lan_chay, ket_qua, duoc_xem_lai, quyet_dinh_xem_lai, phut_xem_lai_simulated, phut_lam_lai_simulated, dong_trong_24h, mo_lai_trong_7_ngay` |

### Giá trị của một số cột

- `loai`: `noi_dia` (nội địa thường), `hang_nang` (hàng nặng, cồng kềnh), `quoc_te` (quốc tế), `doi_tac` (khách đối tác có điều khoản riêng).
- `ket_qua`: `thanh_cong` (đã đóng, không mở lại trong 7 ngày, không sai tiền), `lam_lai` (trả lời sai, nhân viên phải làm lại), `chuyen_nhan_vien` (chạy hết 3 lần vẫn lỗi, chuyển cho nhân viên).
- `quyet_dinh_xem_lai`: `giu`, `sua`, `bo`; để trống nếu không được xem lại.
- Hai cột đuôi `_simulated` là số phút giả lập. **Mọi con số tính từ hai cột này phải ghi nhãn `simulated`** trong hồ sơ.

## Bối cảnh LogiX-VN

| Thông tin | Giá trị |
| --- | --- |
| Quy mô | 12 depot, khoảng 40 nhân viên CSKH |
| Lượng yêu cầu hoàn phí | khoảng 45.000 / tháng (1.500 / ngày) |
| Đợt chạy thử | 2 tuần ở 6 depot |
| Dữ liệu được phát | mẫu ngẫu nhiên 1.200 yêu cầu, 1.624 lần chạy của agent |

## Số liệu dùng chung (giả định của lab)

| Khoản | Giá trị |
| --- | --- |
| Token đầu vào | 26 đ / 1.000 token |
| Token đầu ra | 130 đ / 1.000 token |
| Gọi tool | 15 đ / lần |
| Thời gian nhân viên | 2.000 đ / phút (đã gồm bảo hiểm, văn phòng) |
| Nhân viên tự làm một yêu cầu | 6 phút = 12.000 đ |
| Chi phí cố định của trợ lý | 40 triệu đ / tháng |

Cho sẵn ở nhiệm vụ D: chỉ số chính hiện tại 0,70; mục tiêu +5 điểm; alpha 0,05; power 0,8; ICC 0,02.

## Sáu công thức của cả ngày

| Tên | Công thức |
| --- | --- |
| Chi phí mỗi việc thành công | (token + tool + xem lại + làm lại) ÷ số việc thành công. Tử số tính **mọi** lần chạy, kể cả lần lỗi |
| Số lần chạy trung bình, tối đa k lần | (1 − (1 − p)^k) ÷ p |
| Tỉ lệ thành công sau tối đa k lần | 1 − (1 − p)^k |
| Cỡ mẫu mỗi nhóm, so hai tỉ lệ | (z₁₋α/₂·√(2p̄(1 − p̄)) + z₁₋β·√(p₁(1 − p₁) + p₂(1 − p₂)))² ÷ (p₂ − p₁)² |
| Hệ số thiết kế | 1 + (m − 1) × ICC, với m là số yêu cầu mỗi cụm |
| Cỡ mẫu hiệu dụng khi chia theo cụm | c × m ÷ hệ số thiết kế, luôn nhỏ hơn c ÷ ICC |
