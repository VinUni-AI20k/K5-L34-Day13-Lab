# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 82,83% (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 27,12% (48/177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 4,25% (51/1.200) |
| Dùng | Nhóm tự đề xuất: % nhân viên nhóm trợ lý dùng trợ lý mỗi tuần | Số `staff_id` nhóm trợ lý có ít nhất 1 `staff_review_decision` trong tuần, chia số nhân viên nhóm trợ lý | Không cần tính |
| An toàn | Nhóm tự đề xuất: % đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần | Số mẫu có `so_tien_da_hoan` khác `so_tien_dung`, chia số mẫu kế toán kiểm trong tuần (bắt lỗi ngầm mà mở lại không thấy) | Không cần tính |

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

Cách tính: đếm trực tiếp trên `src/logix_requests.csv` theo đúng công thức ở cột 3; ba chỉ số này không dùng cột `_simulated`. Trong phạm vi `noi_dia` + `hang_nang`, tỉ lệ mở lại 7 ngày là 3,97% (39/982), là mức nền để đặt luật an toàn trong `pilot_plan.yaml`.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| refund_request_created | Hệ thống ticket | request_id, depot, staff_id, loai, so_tien_vnd, arm (trợ lý / đối chứng), created_at, trace_id | Khi khách gửi yêu cầu hoàn phí |
| agent_run_completed | Agent | attempt, tokens_in, tokens_out, tool_calls, status (ok / loi), trace_id | Sau mỗi lần chạy, kể cả lần lỗi |
| handoff_to_staff | Agent | reason, so_lan_chay, tom_tat, trace_id | Khi chạy hết 3 lần vẫn lỗi hoặc thiếu dữ liệu |
| agent_suggestion_shown | Giao diện nhân viên | staff_id, so_tien_de_xuat, trace_id | Khi gợi ý hiện ra cho nhân viên |
| staff_review_decision | Nhân viên | quyet_dinh (giu / sua / bo), phut_xem_lai đo thật, trace_id | Khi bấm giữ, sửa hoặc bỏ |
| staff_rework_completed | Nhân viên | phut_lam_lai đo thật, ly_do, trace_id | Khi làm lại xong |
| refund_ledger_write | Dịch vụ sổ cái | idempotency_key, so_tien, ket_qua, trace_id | Khi ghi sổ hoàn tiền |
| ticket_closed | Hệ thống ticket | closed_at, trace_id | Khi ticket đóng |
| ticket_reopened | Hệ thống ticket | reopened_at, reason, trace_id | Khi khách mở lại trong 7 ngày |
| audit_sample_checked | Kế toán | so_tien_da_hoan, so_tien_dung, trace_id | Hằng tuần, trên mẫu ngẫu nhiên |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- Chính: `ticket_closed` (closed_at − created_at của `refund_request_created` ≤ 24 giờ) và không có `ticket_reopened` trong 7 ngày, chia số `refund_request_created`.
- Dùng (bỏ qua gợi ý): số `staff_review_decision` có quyet_dinh là sua hoặc bo, chia tổng số `staff_review_decision`.
- An toàn (lỗi lọt đến khách): số `ticket_reopened` trong 7 ngày, chia số `refund_request_created`.
- Dùng (tự đề xuất): `staff_review_decision` nhóm theo staff_id và tuần, mẫu số là staff_id có arm = trợ lý trong `refund_request_created`.
- An toàn (tự đề xuất): `audit_sample_checked`, so so_tien_da_hoan với so_tien_dung.
- Chi phí mỗi việc thành công (A): `agent_run_completed` cho token và tool, `staff_review_decision` và `staff_rework_completed` cho phút đo thật thay cột `_simulated`.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... |
