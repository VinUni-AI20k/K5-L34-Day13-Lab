# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 82,83% (994 / 1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 27,12% (48 / 177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 4,25% (51 / 1.200) |
| Dùng (tự đề xuất) | Tỉ lệ can thiệp được mở bằng trợ lý | Số yêu cầu nhân viên mở tab gợi ý của trợ lý, chia tổng yêu cầu được giao | Không cần tính |
| An toàn (tự đề xuất) | Tỉ lệ đơn hoàn sai tiền qua kiểm tra mẫu hàng tuần | Số đơn sai số tiền bồi thường phát hiện qua kiểm tra ngẫu nhiên, chia tổng số đơn kiểm tra | Không cần tính |

*Lưu ý:* Chỉ số trong đợt chạy thử là 82,83%; không viết "trợ lý đã nâng chỉ số từ 0,70" vì đợt chạy thử trước đó chưa có nhóm đối chứng.

## Danh sách event

Gồm 10 event chuẩn hóa của hệ thống, mỗi event đều có `trace_id` để liên kết xuyên suốt với trace của agent:

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách hàng | `request_id`, `loai`, `so_tien`, `arm`, `trace_id` | Khi khách gửi yêu cầu hoàn phí |
| `agent_run_completed` | Agent trợ lý | `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status`, `trace_id` | Sau mỗi lần agent chạy (kể cả lỗi) |
| `agent_suggestion_shown` | Giao diện CSKH | `staff_id`, `so_tien_de_xuat`, `trace_id` | Khi gợi ý của agent hiển thị cho nhân viên |
| `staff_review_decision` | Nhân viên CSKH | `quyet_dinh` (giu/sua/bo), `phut_xem_lai`, `trace_id` | Khi nhân viên xác nhận quyết định |
| `staff_rework_completed` | Nhân viên CSKH | `phut_lam_lai`, `ly_do`, `trace_id` | Khi nhân viên hoàn thành việc làm lại thủ công |
| `refund_ledger_write` | Dịch vụ sổ cái | `idempotency_key`, `so_tien`, `ket_qua`, `trace_id` | Khi giao dịch hoàn tiền được ghi vào sổ cái |
| `handoff_to_staff` | Agent trợ lý | `reason`, `tom_tat`, `trace_id` | Khi chuyển ca cho nhân viên xử lý tiếp |
| `ticket_closed` | Hệ thống ticket | `closed_at`, `duration_minutes`, `trace_id` | Khi yêu cầu hoàn phí được đóng |
| `ticket_reopened` | Khách hàng | `reopened_at`, `reason`, `trace_id` | Khi khách khiếu nại mở lại yêu cầu trong 7 ngày |
| `audit_sample_checked` | Kế toán kiểm soát | `so_tien_da_hoan`, `so_tien_dung`, `sai_lech`, `trace_id` | Hàng tuần khi kế toán đối soát ngẫu nhiên |

**Kiểm tra chéo:**
- Chỉ số chính đo bằng `ticket_closed` (thời gian đóng $\le 24$h) và không có event `ticket_reopened` trong 7 ngày.
- Chỉ số dùng đo bằng `staff_review_decision` (`quyet_dinh` in ['sua', 'bo']).
- Chỉ số an toàn đo bằng tần suất xuất hiện `ticket_reopened`.
- Chỉ số dùng đề xuất đo bằng `agent_suggestion_shown`.
- Chỉ số an toàn đề xuất đo bằng `audit_sample_checked`.

## E2 · Rủi ro kinh tế

Lấy trực tiếp từ phân tích độ nhạy trong `bang_chi_phi.md`:

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | +51,8% chi phí, CPS tăng lên 6.787 đ [simulated] | Tỉ lệ làm lại theo tuần > 7% (đợt chạy thử: 4,9% trong phạm vi) | Thu hẹp phạm vi về `noi_dia`, rà soát 20 trace làm lại gần nhất | PM trợ lý hoàn phí |
| Phải duy trì xem lại 100% kéo dài | CPS tăng lên 11.743 đ = 0,98× (hoặc 12.516 đ = 1,04× nếu phút làm lại như thực tế) [simulated] | % yêu cầu cần xem lại còn > 50% ở cuối bước rollout 0.25 | Giảm dần tỷ lệ xem lại theo bậc khi tỷ lệ sửa + bỏ < 15% | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến | Cố định 40 triệu đ/tháng: +1.185 đ/việc ở mức 45.000 yc, tăng lên +2.370 đ/việc nếu khối lượng giảm một nửa [simulated] | Khối lượng yêu cầu thành công theo tuần < 50% kế hoạch | Tạm dừng mở rộng pilot, đàm phán lại chi phí cố định hạ tầng | PM trợ lý hoàn phí |
