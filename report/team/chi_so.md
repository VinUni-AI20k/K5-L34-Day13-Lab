# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 994/1.200 = 82,83% |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 48/177 = 27,12% |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 51/1.200 = 4,25% |
| Dùng | Nhóm tự đề xuất: % yêu cầu của nhân viên nhóm can thiệp được mở bằng trợ lý | số `agent_suggestion_shown` chia số `refund_request_created` của nhóm can thiệp, theo tuần | Không cần tính |
| An toàn | Nhóm tự đề xuất: % đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần (bắt lỗi ngầm như ca 5, 17) | (`so_tien_da_hoan` khác `so_tien_dung`) chia số đơn kiểm, từ `audit_sample_checked` | Không cần tính |

Viết "chỉ số trong đợt chạy thử là 82,83%", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | request_id, loai, so_tien, arm, trace_id | Khi khách gửi yêu cầu |
| `agent_run_completed` | Agent | attempt, tokens_in/out, tool_calls, status, trace_id | Sau mỗi lần chạy, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | staff_id, so_tien_de_xuat, trace_id | Khi gợi ý hiện ra |
| `staff_review_decision` | Nhân viên | giu/sua/bo, phut_xem_lai (đo thật), trace_id | Khi bấm gửi, sửa hoặc bỏ |
| `staff_rework_completed` | Nhân viên | phut_lam_lai, ly_do, trace_id | Khi làm lại xong |
| `refund_ledger_write` | Dịch vụ sổ cái | idempotency_key, so_tien, ket_qua, trace_id | Khi ghi sổ |
| `handoff_to_staff` | Agent | reason, tom_tat, trace_id | Khi chuyển nhân viên |
| `ticket_closed` | Hệ thống ticket | closed_at, trace_id | Khi đóng yêu cầu |
| `ticket_reopened` | Khách | reopened_at, reason, trace_id | Khi khách mở lại |
| `audit_sample_checked` | Kế toán | so_tien_da_hoan, so_tien_dung, trace_id | Hằng tuần |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, event dùng để tính.

- Chỉ số chính: `refund_request_created`, `ticket_closed` (closed_at trừ thời điểm tạo, hạn 24 giờ) và `ticket_reopened` (trong 7 ngày).
- Tỉ lệ bỏ qua gợi ý: `staff_review_decision` (giu/sua/bo).
- Tỉ lệ lỗi lọt đến khách: `ticket_reopened`, chia số `refund_request_created`.
- Chỉ số dùng tự đề xuất: `agent_suggestion_shown` và `refund_request_created` theo `arm`.
- Chỉ số an toàn tự đề xuất: `audit_sample_checked`.
- Cả năm chỉ số tính được từ danh sách event trên, theo dữ liệu hiện có. Phút xem lại và làm lại thật cần `staff_review_decision` và `staff_rework_completed`, chưa có dữ liệu.

## E2 · Rủi ro kinh tế

Số lấy từ bảng độ nhạy (`bang_chi_phi.md`); mọi con số dưới đây là **simulated**.

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | CPS +51,8%, lên 6.787 đ [simulated] (B1) | Tỉ lệ làm lại theo tuần trên 7% (đợt chạy thử: 48/982 = 4,89% trong phạm vi) | Thu hẹp về noi_dia, rà 20 trace làm lại | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | 11.743 đ/việc = 0,98 lần 12.000 đ; 12.415 đ = 1,03 lần nếu làm lại 15,3 phút [simulated] (B4) | % yêu cầu được xem lại còn trên 50% cuối bước 0,25 | Giảm xem lại theo bậc khi tỉ lệ sửa + bỏ dưới 15% | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến | Cố định 40 triệu đ/tháng: +1.185 đ/việc ở 45.000 yêu cầu/tháng, +2.370 đ/việc nếu còn một nửa [simulated] (A4) | Số việc thành công theo tuần dưới 50% kế hoạch | Không mở rộng pilot, xem lại hợp đồng chi phí cố định | PM trợ lý hoàn phí |
