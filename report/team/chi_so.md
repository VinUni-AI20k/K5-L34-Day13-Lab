# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 82,83% (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 27,12% (48/177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 4,25% (51/1.200) |
| Dùng | Nhóm tự đề xuất: % yêu cầu của nhân viên nhóm trợ lý được mở bằng trợ lý | `agent_suggestion_shown` chia `refund_request_created` của nhóm trợ lý, theo tuần | Không cần tính |
| An toàn | Nhóm tự đề xuất: % đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần (bắt lỗi ngầm như ca 5, 17) | `so_tien_da_hoan` khác `so_tien_dung` trong `audit_sample_checked`, chia số đơn kiểm | Không cần tính |

Chỉ số trong đợt chạy thử là 82,83%: đợt chạy thử không có nhóm đối chứng nên không viết "trợ lý đã nâng chỉ số". Mọi số trên đo từ cột không phải `_simulated` của `logix_requests.csv`.

## Danh sách event

Mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | request_id, loai, so_tien, arm, trace_id | Khi khách gửi yêu cầu |
| `agent_run_completed` | Agent | attempt, tokens_in, tokens_out, tool_calls, status, trace_id | Sau mỗi lần chạy, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | staff_id, so_tien_de_xuat, trace_id | Khi gợi ý hiện ra |
| `staff_review_decision` | Nhân viên | giu / sua / bo, phut_xem_lai (đo thật), trace_id | Khi bấm gửi, sửa hoặc bỏ |
| `staff_rework_completed` | Nhân viên | phut_lam_lai, ly_do, trace_id | Khi làm lại xong |
| `refund_ledger_write` | Dịch vụ sổ cái | idempotency_key, so_tien, ket_qua, trace_id | Khi ghi sổ |
| `handoff_to_staff` | Agent | reason, tom_tat, trace_id | Khi chuyển nhân viên |
| `ticket_closed` | Hệ thống ticket | closed_at, trace_id | Khi đóng ticket |
| `ticket_reopened` | Khách | reopened_at, reason, trace_id | Khi khách mở lại |
| `audit_sample_checked` | Kế toán | so_tien_da_hoan, so_tien_dung, trace_id | Hằng tuần |

**Kiểm tra chéo:** event dùng để tính từng chỉ số.

- Chỉ số chính: `refund_request_created` (mẫu số), `ticket_closed` (đóng trong 24 giờ, so `closed_at` với thời điểm tạo) và `ticket_reopened` (loại trừ nếu mở lại trong 7 ngày).
- Tỉ lệ bỏ qua gợi ý: `staff_review_decision` (giu / sua / bo).
- Tỉ lệ lỗi lọt đến khách: `ticket_reopened` chia `refund_request_created`.
- Chỉ số dùng tự đề xuất: `agent_suggestion_shown` chia `refund_request_created`, theo `staff_id` và `arm`.
- Chỉ số an toàn tự đề xuất: `audit_sample_checked`.
- Cả năm chỉ số tính được từ danh sách event; `phut_xem_lai` và `phut_lam_lai` đo thật (từ `staff_review_decision`, `staff_rework_completed`) thay các cột `_simulated` sau tuần 1.

## E2 · Rủi ro kinh tế

Số lấy từ `bang_chi_phi.md` (tất cả simulated).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | +51,8%, từ 4.472 lên 6.787 đ mỗi việc thành công [simulated] | Tỉ lệ làm lại theo tuần vượt 7% (đợt chạy thử: 4,9% trong phạm vi) | Thu hẹp về `noi_dia`, rà 20 trace làm lại | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | 11.743 đ = 0,98× của 12.000 đ; 12.516 đ = 1,04× nếu làm lại 16,2 phút như dữ liệu [simulated] | % yêu cầu được xem lại vượt 50% vào cuối bước 0.25 (đợt chạy thử: 14,8%) | Giảm xem lại theo bậc khi tỉ lệ sửa + bỏ dưới 15% | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến | Cố định 40 triệu đ/tháng: +1.185 đ/việc ở 45.000 yêu cầu/tháng, +2.370 đ/việc nếu còn một nửa [simulated] | Số việc thành công theo tuần dưới 50% kế hoạch | Không mở rộng pilot; xem lại hợp đồng chi phí cố định | PM trợ lý hoàn phí |
