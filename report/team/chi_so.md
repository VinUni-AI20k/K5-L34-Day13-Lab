# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 82,83% (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 27,12% (48/177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 4,25% (51/1.200) |
| Dùng | Nhóm tự đề xuất: % yêu cầu của nhóm can thiệp được mở bằng trợ lý | Số yêu cầu có `agent_suggestion_shown` chia tổng số yêu cầu của nhóm can thiệp | Không cần tính |
| An toàn | Nhóm tự đề xuất: % đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần | Số đơn sai số tiền trong mẫu `audit_sample_checked` chia tổng số đơn kiểm tra (100 đơn/tuần) | Không cần tính |

Chỉ số trong đợt chạy thử là 82,83% (không viết "trợ lý đã nâng chỉ số", vì đợt chạy thử không có nhóm đối chứng).

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | `request_id`, `loai`, `so_tien`, `arm`, `trace_id` | Khi khách gửi yêu cầu |
| `agent_run_completed` | Agent | `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status`, `trace_id` | Sau mỗi lần chạy, kể cả lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | `staff_id`, `so_tien_de_xuat`, `trace_id` | Khi gợi ý hiện ra |
| `staff_review_decision` | Nhân viên | `quyet_dinh` (`giu`/`sua`/`bo`), `phut_xem_lai`, `trace_id` | Khi nhân viên bấm gửi/sửa/bỏ |
| `staff_rework_completed` | Nhân viên | `phut_lam_lai`, `ly_do`, `trace_id` | Khi nhân viên làm lại xong |
| `refund_ledger_write` | Dịch vụ sổ cái | `idempotency_key`, `so_tien`, `ket_qua`, `trace_id` | Khi ghi lệnh hoàn tiền vào sổ cái |
| `handoff_to_staff` | Agent | `reason`, `tom_tat`, `trace_id` | Khi chuyển yêu cầu cho nhân viên |
| `ticket_closed` | Hệ thống ticket | `closed_at`, `trace_id` | Khi đóng yêu cầu |
| `ticket_reopened` | Khách | `reopened_at`, `reason`, `trace_id` | Khi khách mở lại yêu cầu |
| `audit_sample_checked` | Kế toán | `so_tien_da_hoan`, `so_tien_dung`, `trace_id` | Kiểm tra mẫu hằng tuần |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- **Chỉ số chính (% đóng trong 24h không mở lại 7 ngày):** tính từ `refund_request_created`, `ticket_closed` (trong 24 giờ) và `ticket_reopened` (trong 7 ngày) nối theo `trace_id`.
- **Chỉ số dùng (tỉ lệ bỏ qua gợi ý):** tính từ `staff_review_decision` (`sua` + `bo`) chia cho `agent_suggestion_shown` / tổng lượt xem lại.
- **Chỉ số an toàn (tỉ lệ lỗi lọt đến khách):** tính từ `ticket_reopened` trong 7 ngày chia cho `refund_request_created`.
- **Chỉ số dùng đề xuất (% mở bằng trợ lý):** tính từ `agent_suggestion_shown` chia cho `refund_request_created` (nhóm `arm = treatment`).
- **Chỉ số an toàn đề xuất (% đơn sai tiền):** tính từ `audit_sample_checked` (`so_tien_da_hoan != so_tien_dung`) chia tổng mẫu kiểm tra hằng tuần.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | Chi phí mỗi việc thành công tăng **+51,8%**, lên **6.787 đ** [simulated] | Tỉ lệ làm lại theo tuần > 7% (mẫu phạm vi: 4,9%) | Thu hẹp phạm vi về `noi_dia`, rà 20 trace làm lại để sửa prompt/tool | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | Chi phí mỗi việc thành công lên **11.743 đ = 0,98×** (hoặc **12.415 đ = 1,03×** nếu làm lại 15,3 phút) [simulated] | Tỉ lệ được xem lại > 50% ở cuối tuần rollout 0.25 | Giảm tỉ lệ xem lại theo bậc khi tỉ lệ `sua + bo` < 15% và thời gian xem lại < 4,8 phút | Trưởng nhóm CSKH |
| Khối lượng xử lý thấp hơn dự kiến | Chi phí cố định 40 triệu đ/tháng tăng từ **+1.185 đ/việc** (45.000 yc/tháng) lên **+2.370 đ/việc** nếu còn một nửa [simulated] | Số việc thành công theo tuần < 50% kế hoạch | Không mở rộng bước rollout tiếp theo, rà lại cấu trúc chi phí cố định | PM trợ lý hoàn phí |
