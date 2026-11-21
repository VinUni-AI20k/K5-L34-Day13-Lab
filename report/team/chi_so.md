# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 82,83% (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 27,12% (48/177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 4,25% (51/1.200) |
| Dùng | Nhóm tự đề xuất: Tỉ lệ yêu cầu được xử lý qua trợ lý | Số yêu cầu được mở qua giao diện trợ lý chia cho tổng số yêu cầu của nhóm can thiệp | Không cần tính |
| An toàn | Nhóm tự đề xuất: Tỉ lệ sai sót tiền hoàn qua kiểm tra mẫu ngẫu nhiên | Số đơn lệch tiền hoàn chia cho số đơn kiểm tra đối soát độc lập hằng tuần (bắt lỗi ngầm) | Không cần tính |

*Lưu ý:* Chỉ số trong đợt chạy thử là 82,83%, không viết "trợ lý đã nâng chỉ số từ 0,70" vì đợt chạy thử chưa có nhóm đối chứng đồng thời.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent. Thiết kế chuẩn 10 event:

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách hàng | `request_id`, `loai`, `so_tien`, `arm`, `trace_id` | Khi khách hàng gửi yêu cầu hoàn phí |
| `agent_run_completed` | Trợ lý agent | `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status`, `trace_id` | Sau mỗi lần agent chạy xong (kể cả lỗi) |
| `agent_suggestion_shown` | UI CSKH | `staff_id`, `so_tien_de_xuat`, `trace_id` | Khi đề xuất hoàn tiền hiện lên màn hình |
| `staff_review_decision` | Nhân viên CSKH | `decision` (giu/sua/bo), `phut_xem_lai`, `trace_id` | Khi nhân viên bấm duyệt, sửa hoặc bỏ qua |
| `staff_rework_completed` | Nhân viên CSKH | `phut_lam_lai`, `ly_do`, `trace_id` | Khi hoàn thành xử lý lại ca bị lỗi |
| `refund_ledger_write` | Dịch vụ sổ cái | `idempotency_key`, `so_tien`, `status`, `trace_id` | Khi thực hiện ghi lệnh hoàn tiền vào sổ cái |
| `handoff_to_staff` | Trợ lý agent | `reason`, `tom_tat`, `trace_id` | Khi agent bỏ cuộc chuyển cho nhân viên làm |
| `ticket_closed` | Hệ thống ticket | `closed_at`, `duration_hours`, `trace_id` | Khi ticket khiếu nại hoàn tất đóng |
| `ticket_reopened` | Khách hàng | `reopened_at`, `reason`, `trace_id` | Khi khách hàng mở lại ticket trong vòng 7 ngày |
| `audit_sample_checked` | Ban kiểm toán/Kế toán | `so_tien_da_hoan`, `so_tien_chuan`, `ket_luan`, `trace_id` | Khi kiểm tra ngẫu nhiên mẫu đối soát hàng tuần |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- **Chỉ số chính (% đóng 24h & không mở lại 7 ngày):** Tính từ `ticket_closed` (xác định đóng trong 24h) và kiểm tra không phát sinh event `ticket_reopened` với cùng `trace_id` / `request_id` trong 7 ngày tiếp theo.
- **Chỉ số dùng (Tỉ lệ bỏ qua gợi ý):** Đếm các event `staff_review_decision` có thuộc tính `decision` thuộc `['sua', 'bo']` chia cho tổng số event `staff_review_decision` phát sinh.
- **Chỉ số an toàn (Tỉ lệ lỗi lọt đến khách):** Đếm số `request_id` phát sinh event `ticket_reopened` trong vòng 7 ngày chia cho tổng số `refund_request_created`.
- **Chỉ số dùng tự đề xuất (% yêu cầu mở qua trợ lý):** Đếm `agent_suggestion_shown` chia cho tổng `refund_request_created` của nhóm can thiệp (dựa trên trường `arm`).
- **Chỉ số an toàn tự đề xuất (% sai lệch kiểm toán):** Đếm số event `audit_sample_checked` có `so_tien_da_hoan != so_tien_chuan` chia cho tổng số event `audit_sample_checked`.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy trực tiếp từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | Chi phí mỗi việc tăng +51,8% lên 6.787 đ [simulated] | Tỉ lệ ca làm lại theo tuần > 7% (đợt chạy thử: 4,9% trong phạm vi) | Thu hẹp phạm vi về riêng `noi_dia`, rà soát 20 trace làm lại gần nhất | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | Chi phí lên 11.743 đ = 0,98× (hoặc 12.415 đ = 1,03× nếu làm lại 15,3 phút), trợ lý mất hoàn toàn lợi thế kinh tế [simulated] | Tỉ lệ yêu cầu phải xem lại vẫn > 50% ở cuối bước rollout 0.25 | Thực hiện giảm xem lại theo bậc dựa trên độ tin cậy khi tỉ lệ sửa/bỏ < 15% | Trưởng nhóm CSKH |
| Khối lượng xử lý thấp hơn dự kiến | Chi phí cố định 40 tr/tháng phân bổ tăng từ 1.185 đ/việc lên 2.370 đ/việc nếu khối lượng giảm một nửa [simulated] | Số việc thành công hàng tuần đạt < 50% kế hoạch (dưới 3.900 việc/tuần) | Tạm dừng mở rộng pilot, đàm phán lại hợp đồng chi phí cố định hạ tầng | PM trợ lý hoàn phí |
