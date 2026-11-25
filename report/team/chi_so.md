# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | *(Chờ Hải tính ở Lượt 8)* |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | *(Chờ Hải tính ở Lượt 8)* |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | *(Chờ Hải tính ở Lượt 8)* |
| Dùng | Tỉ lệ mở trợ lý trên nhóm can thiệp | Số yêu cầu nhóm can thiệp có event `agent_suggestion_shown` chia tổng số yêu cầu nhóm can thiệp | Không cần tính |
| An toàn | Tỉ lệ đơn hoàn sai tiền qua kiểm tra mẫu | Số đơn lệch tiền trong `audit_sample_checked` chia tổng số đơn được kiểm tra mẫu hằng tuần | Không cần tính |

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | `request_id`, `loai`, `so_tien_vnd`, `arm`, `trace_id` | Khi khách gửi yêu cầu hoàn phí |
| `agent_run_completed` | Agent | `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status`, `trace_id` | Sau mỗi lần chạy, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | `staff_id`, `so_tien_de_xuat`, `trace_id` | Khi gợi ý của trợ lý hiện ra cho nhân viên |
| `staff_review_decision` | Nhân viên | `quyet_dinh` (`giu`/`sua`/`bo`), `phut_xem_lai`, `trace_id` | Khi nhân viên bấm gửi, sửa hoặc bỏ |
| `staff_rework_completed` | Nhân viên | `phut_lam_lai`, `ly_do`, `trace_id` | Khi nhân viên làm lại xong ca lỗi |
| `refund_ledger_write` | Dịch vụ sổ cái | `idempotency_key`, `so_tien`, `ket_qua`, `trace_id` | Khi ghi nhận giao dịch hoàn tiền vào sổ cái |
| `handoff_to_staff` | Agent | `reason`, `tom_tat`, `trace_id` | Khi agent chuyển yêu cầu sang nhân viên |
| `ticket_closed` | Hệ thống ticket | `closed_at`, `trace_id` | Khi yêu cầu được đóng |
| `ticket_reopened` | Khách | `reopened_at`, `reason`, `trace_id` | Khi khách mở lại yêu cầu |
| `audit_sample_checked` | Kế toán | `so_tien_da_hoan`, `so_tien_dung`, `trace_id` | Khi kiểm tra mẫu đối soát hằng tuần |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- **% yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày:** tính từ `refund_request_created`, `ticket_closed` (`closed_at - created_at <= 24h`) và không có `ticket_reopened` trong 7 ngày (`reopened_at - closed_at <= 7 ngày`).
- **Tỉ lệ bỏ qua gợi ý:** tính từ `agent_suggestion_shown` và `staff_review_decision` (`quyet_dinh` là `sua` hoặc `bo` chia tổng số ca được xem lại).
- **Tỉ lệ lỗi lọt đến khách:** tính từ `ticket_reopened` (trong vòng 7 ngày) chia tổng số `refund_request_created`.
- **Tỉ lệ mở trợ lý trên nhóm can thiệp:** tính từ `agent_suggestion_shown` và `refund_request_created` (lọc `arm = can_thiep`).
- **Tỉ lệ đơn hoàn sai tiền qua kiểm tra mẫu:** tính từ `audit_sample_checked` (`so_tien_da_hoan != so_tien_dung` chia tổng số bản ghi kiểm tra trong tuần).

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | +51,77%, lên **6.787 đ/việc** (simulated) | Tỉ lệ làm lại theo tuần > 7% | Thu hẹp về `noi_dia`, rà 20 `trace_id` làm lại gần nhất | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | **11.743 đ = 0,98×** với 9 phút làm lại/ca; lên **12.415 đ = 1,03×** nếu làm lại 15,3 phút/ca (simulated) | Tỉ lệ yêu cầu được xem lại > 50% cuối bước rollout 0,25 | Giảm tỉ lệ xem lại theo bậc khi tỉ lệ sửa + bỏ < 15% | Trưởng nhóm CSKH |
| Khối lượng chỉ đạt một nửa kế hoạch | Chi phí cố định 40 triệu đ/tháng tăng từ 1.185 đ lên 2.370 đ/việc; CPS phạm vi pilot tăng từ 4.599 đ (0,38×) lên **5.784 đ (0,48×)** (simulated) | Số việc thành công theo tuần < 50% kế hoạch | Dừng mở rộng pilot, rà soát lại chi phí cố định và điều kiện chuyển giao | PM trợ lý hoàn phí |
