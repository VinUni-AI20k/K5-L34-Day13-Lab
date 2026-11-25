# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | ... |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | ... |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | ... |
| Dùng | Nhóm tự đề xuất: ... | ... | Không cần tính |
| An toàn | Nhóm tự đề xuất: ... | ... | Không cần tính |

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách / Hệ thống CSKH | `request_id, depot, loai, so_tien_vnd, arm, trace_id` | Khi khách gửi yêu cầu hoàn phí |
| `agent_run_completed` | Trợ lý hoàn phí (Agent) | `run_id, request_id, attempt, tokens_in, tokens_out, tool_calls, status, trace_id` | Sau mỗi lần chạy của agent (kể cả khi lỗi) |
| `agent_suggestion_shown` | Giao diện nhân viên CSKH | `request_id, staff_id, so_tien_de_xuat, trace_id` | Khi gợi ý của trợ lý hiển thị trên màn hình nhân viên |
| `staff_review_decision` | Nhân viên CSKH | `request_id, staff_id, quyet_dinh (giu/sua/bo), phut_xem_lai (đo thật), trace_id` | Khi nhân viên bấm Giữ, Sửa hoặc Bỏ gợi ý |
| `staff_rework_completed` | Nhân viên CSKH | `request_id, staff_id, phut_lam_lai (đo thật), ly_do, trace_id` | Khi nhân viên hoàn tất xử lý lại một ca sai |
| `refund_ledger_write` | Dịch vụ sổ cái (Ledger) | `request_id, idempotency_key, so_tien_vnd, ket_qua (ok/loi), trace_id` | Khi hệ thống ghi nhận lệnh hoàn tiền vào sổ cái |
| `handoff_to_staff` | Trợ lý hoàn phí (Agent) | `request_id, reason, tom_tat, attempt_cuoi, trace_id` | Khi agent không xử lý được và chuyển cho nhân viên |
| `ticket_closed` | Hệ thống ticket | `request_id, closed_at, closed_within_24h, trace_id` | Khi yêu cầu hoàn phí được đóng |
| `ticket_reopened` | Khách hàng / CSKH | `request_id, reopened_at, reason, days_since_close, trace_id` | Khi khách mở lại yêu cầu sau khi đã đóng |
| `audit_sample_checked` | Bộ phận Kế toán | `request_id, so_tien_da_hoan, so_tien_dung, lech_tien (0/1), trace_id` | Khi kế toán kiểm tra mẫu hằng tuần (100 đơn/tuần) |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- **Chỉ số chính (`% yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày`):** tính từ `refund_request_created` (mẫu số tổng yêu cầu + mốc thời gian tạo), `ticket_closed` (kiểm tra `closed_at - created_at <= 24h`) và `ticket_reopened` (kiểm tra không phát sinh sự kiện mở lại trong 7 ngày sau `closed_at`), nối theo `trace_id` / `request_id`.
- **Chỉ số dùng (`Tỉ lệ bỏ qua gợi ý`):** tính từ `staff_review_decision` (số bản ghi có `quyet_dinh` thuộc `{sua, bo}` chia cho tổng số bản ghi `staff_review_decision` đã xem lại), đối chiếu với `agent_suggestion_shown` qua `trace_id`.
- **Chỉ số an toàn (`Tỉ lệ lỗi lọt đến khách`):** tính từ `ticket_reopened` (số yêu cầu có `days_since_close <= 7`) chia cho tổng số yêu cầu từ `refund_request_created`, nối qua `trace_id`.
- **Chỉ số dùng tự đề xuất (`% yêu cầu của nhóm can thiệp có mở gợi ý trợ lý`):** tính từ `agent_suggestion_shown` chia cho số yêu cầu thuộc nhóm `arm = treatment` trong `refund_request_created`, nối qua `trace_id`.
- **Chỉ số an toàn tự đề xuất (`% đơn hoàn sai tiền phát hiện qua kiểm tra mẫu hằng tuần`):** tính từ `audit_sample_checked` (số bản ghi có `lech_tien == 1` chia cho tổng số đơn kiểm tra mẫu), đối chiếu giao dịch gốc qua `refund_ledger_write` bằng `trace_id`.
- **Chi phí thực tế khi chạy pilot (thay thế số `simulated`):** đo trực tiếp `tokens_in`, `tokens_out`, `tool_calls` từ `agent_run_completed`, `phut_xem_lai` thật từ `staff_review_decision` và `phut_lam_lai` thật từ `staff_rework_completed`, nối qua `trace_id`.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... |
