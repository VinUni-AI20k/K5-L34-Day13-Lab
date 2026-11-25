# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | **82,83%** (994/1.200); trong phạm vi `noi_dia` + `hang_nang`: 92,26% (906/982) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | **27,12%** (48/177); trong phạm vi `noi_dia` + `hang_nang`: 21,09% (27/128) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | **4,25%** (51/1.200); trong phạm vi `noi_dia` + `hang_nang`: 3,97% (39/982) |
| Dùng | Nhóm tự đề xuất: Tỉ lệ tiếp nhận sử dụng trợ lý (adoption rate) | Số yêu cầu thuộc nhóm can thiệp có hiển thị gợi ý trợ lý chia tổng số yêu cầu đủ điều kiện của nhóm can thiệp | Không cần tính |
| An toàn | Nhóm tự đề xuất: Tỉ lệ đơn hoàn sai tiền hoặc hoàn trùng qua kiểm tra mẫu hằng tuần | Số đơn lệch tiền trong mẫu kiểm tra 100 đơn/tuần hoặc hoàn trùng trên sổ cái, chia tổng số đơn được kiểm tra | Không cần tính |

Chỉ số trong đợt chạy thử là **82,83%** (tỉ lệ bỏ qua gợi ý là **27,12%**, tỉ lệ lỗi lọt đến khách là **4,25%**), được tính bằng `src/cp5_chi_so.py` trên `src/logix_requests.csv`. Không viết "trợ lý đã nâng chỉ số" vì đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Mười event (vượt mức tối thiểu 6 event), mỗi event đều có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | Ứng dụng khách / cổng CSKH | `request_id`, `loai`, `so_tien`, `arm`, `trace_id` | Khi khách gửi yêu cầu hoàn phí |
| `agent_run_completed` | Trợ lý hoàn phí (Agent) | `request_id`, `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status`, `trace_id` | Sau mỗi lần chạy, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên CSKH | `request_id`, `staff_id`, `so_tien_de_xuat`, `trace_id` | Khi gợi ý của trợ lý hiện ra cho nhân viên |
| `staff_review_decision` | Nhân viên CSKH | `request_id`, `staff_id`, `quyet_dinh` (`giu`/`sua`/`bo`), `phut_xem_lai_thuc`, `trace_id` | Khi nhân viên bấm gửi, sửa hoặc bỏ gợi ý |
| `staff_rework_completed` | Nhân viên CSKH | `request_id`, `staff_id`, `phut_lam_lai_thuc`, `ly_do`, `trace_id` | Khi nhân viên hoàn tất làm lại ca sai |
| `refund_ledger_write` | Dịch vụ sổ cái (Ledger) | `request_id`, `idempotency_key`, `so_tien_hoan`, `ket_qua`, `trace_id` | Khi ghi lệnh hoàn tiền vào sổ cái |
| `handoff_to_staff` | Trợ lý hoàn phí (Agent) | `request_id`, `reason`, `tom_tat`, `trace_id` | Khi trợ lý chuyển yêu cầu sang nhân viên |
| `ticket_closed` | Hệ thống ticket | `request_id`, `closed_at`, `trace_id` | Khi yêu cầu hoàn phí được đóng |
| `ticket_reopened` | Khách hàng / Hệ thống ticket | `request_id`, `reopened_at`, `reason`, `trace_id` | Khi khách mở lại yêu cầu |
| `audit_sample_checked` | Kế toán / Kiểm soát chất lượng | `request_id`, `so_tien_da_hoan`, `so_tien_dung`, `lech_tien`, `trace_id` | Khi kiểm tra mẫu định kỳ 100 đơn/tuần |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Cả 5 chỉ số đều đo được từ 10 event trên khi nối bằng `trace_id` và `request_id`:

- **% đóng trong 24 giờ và không mở lại trong 7 ngày (Chính):** tính từ `refund_request_created` (thời điểm tạo, lọc theo `arm`), `ticket_closed` (`closed_at - created_at <= 24h`) và không phát sinh `ticket_reopened` trong 7 ngày sau `closed_at`. → **Đo được.**
- **Tỉ lệ bỏ qua gợi ý (Dùng):** tính từ `staff_review_decision`, lấy số event có `quyet_dinh` là `sua` hoặc `bo` chia tổng số event `staff_review_decision`. → **Đo được.**
- **Tỉ lệ lỗi lọt đến khách (An toàn):** tính từ số yêu cầu có `ticket_reopened` trong vòng 7 ngày sau `ticket_closed` chia tổng số `refund_request_created`. → **Đo được.**
- **Tỉ lệ tiếp nhận sử dụng trợ lý (Dùng — tự đề xuất):** tính từ số `request_id` duy nhất có `agent_suggestion_shown` chia tổng số `refund_request_created` thuộc nhóm can thiệp trong phạm vi pilot. → **Đo được.**
- **Tỉ lệ đơn hoàn sai tiền hoặc hoàn trùng (An toàn — tự đề xuất):** tính từ `audit_sample_checked` (đếm đơn có `lech_tien != 0`, bắt lỗi ngầm) kết hợp đối soát `refund_ledger_write` (phát hiện hoàn trùng trên cùng `request_id`/`idempotency_key`). → **Đo được.**
- *(Bổ sung đo chi phí thật)* Hai trường `phut_xem_lai_thuc` (`staff_review_decision`) và `phut_lam_lai_thuc` (`staff_rework_completed`) dùng để thay thế hai cột `simulated` sau tuần 1 pilot.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... |
