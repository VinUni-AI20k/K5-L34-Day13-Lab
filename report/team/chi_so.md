# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 82,83% (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 27,12% (48/177: 41 sửa + 7 bỏ) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 4,25% (51/1.200) |
| Dùng | Nhóm tự đề xuất: % yêu cầu của nhân viên trong nhóm can thiệp được mở bằng trợ lý mỗi tuần | số yêu cầu có `agent_suggestion_shown` và nhân viên mở ÷ số yêu cầu nhóm can thiệp nhận | Không cần tính |
| An toàn | Nhóm tự đề xuất: % đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần | `so_tien_da_hoan` ≠ `so_tien_dung` ÷ số đơn kiểm mẫu (bắt lỗi ngầm mà khách chưa mở lại) | Không cần tính |

Viết "chỉ số trong đợt chạy thử là 82,83%", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| refund_request_created | App khách | request_id, loai, so_tien, arm, trace_id | Khi khách gửi yêu cầu |
| agent_run_completed | Agent | attempt, tokens_in, tokens_out, tool_calls, status, trace_id | Sau mỗi lần chạy, kể cả lỗi |
| agent_suggestion_shown | Giao diện nhân viên | staff_id, so_tien_de_xuat, trace_id | Khi gợi ý hiện ra |
| staff_review_decision | Nhân viên | quyet_dinh (giu/sua/bo), phut_xem_lai (đo thật), trace_id | Khi bấm gửi, sửa hoặc bỏ |
| staff_rework_completed | Nhân viên | phut_lam_lai, ly_do, trace_id | Khi làm lại xong |
| handoff_to_staff | Agent | reason, tom_tat, trace_id | Khi chuyển nhân viên |
| ticket_closed | Hệ thống ticket | closed_at, trace_id | Khi đóng ticket |
| ticket_reopened | Khách | reopened_at, reason, trace_id | Khi khách mở lại |
| audit_sample_checked | Kế toán | so_tien_da_hoan, so_tien_dung, trace_id | Hằng tuần |

**Kiểm tra chéo:** với mỗi chỉ số, event dùng để tính:

- Chỉ số chính: `refund_request_created` (mẫu số), `ticket_closed` (đóng trong 24 giờ), `ticket_reopened` (loại ca mở lại trong 7 ngày).
- Dùng (bỏ qua gợi ý): `staff_review_decision` (sua, bo trên tổng ca được xem lại).
- An toàn (lỗi lọt đến khách): `ticket_reopened` ÷ `refund_request_created`.
- Dùng tự đề xuất: `agent_suggestion_shown` + `staff_review_decision`.
- An toàn tự đề xuất: `audit_sample_checked`.
- Cả sáu số đều tính được từ danh sách event trên, nối bằng `trace_id`; chi phí làm lại và xem lại cần `staff_rework_completed` và `staff_review_decision` đo phút thật thay cho số simulated.

## E2 · Rủi ro kinh tế

Số lấy từ `bang_chi_phi.md`, mọi số chi phí là [simulated].

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | +51,8%, từ 4.472 đ lên 6.787 đ mỗi việc thành công (B1) | Tỉ lệ `lam_lai` theo tuần > 7% (đợt chạy thử: 4,9% trong phạm vi noi_dia + hang_nang) | Thu hẹp về noi_dia, rà 20 trace làm lại | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | 11.743 đ = 0,98× của 12.000 đ (12.415 đ = 1,03× nếu làm lại 15,3 phút như dữ liệu) (B4) | % yêu cầu được xem lại còn > 50% sau bước 0.25 | Giảm xem lại theo bậc khi tỉ lệ sửa + bỏ < 15% | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến | Cố định 40 triệu/tháng: +1.185 đ/việc ở 45.000 yêu cầu/tháng, +2.370 đ/việc nếu còn một nửa; tổng 5.784 đ = 0,48× (A4) | Số việc thành công theo tuần < 50% kế hoạch | Không mở rộng pilot, xem lại hợp đồng chi phí cố định | PM trợ lý hoàn phí |
| Nhân viên bỏ qua gợi ý nhiều hơn dự kiến | Tỉ lệ xem lại gấp đôi: +40,7% (6.292 đ) (B1) | Tỉ lệ bỏ qua gợi ý (sua + bo) > 40% (hiện 27,12%) | Rà gợi ý bị bỏ theo loại yêu cầu, sửa prompt hoặc thu hẹp phạm vi | Trưởng nhóm CSKH |
