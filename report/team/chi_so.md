# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 82,83% (994/1.200 yêu cầu) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 27,12% (48/177 yêu cầu được xem lại) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 4,25% (51/1.200 yêu cầu) |
| Dùng | Nhóm tự đề xuất: % yêu cầu của nhóm can thiệp được mở bằng trợ lý | Số yêu cầu có event `agent_suggestion_shown` chia tổng yêu cầu nhận được của nhóm can thiệp | Không cần tính |
| An toàn | Nhóm tự đề xuất: % đơn hoàn sai tiền qua kiểm tra mẫu hàng tuần | Số đơn phát hiện sai lệch số tiền qua kiểm tra mẫu kế toán chia tổng số đơn kiểm tra ngẫu nhiên | Không cần tính |

*Ghi chú:* Chỉ số trong đợt chạy thử là 82,83% (đóng trong 24h và không mở lại trong 7 ngày); không viết "trợ lý đã nâng chỉ số từ 0,70" vì đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | `request_id`, `loai`, `so_tien`, `arm`, `trace_id` | Khi khách gửi yêu cầu |
| `agent_run_completed` | Agent | `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status`, `trace_id` | Sau mỗi lần chạy agent, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | `staff_id`, `so_tien_de_xuat`, `trace_id` | Khi khung gợi ý của agent hiện ra |
| `staff_review_decision` | Nhân viên | `quyet_dinh` (giu/sua/bo), `phut_xem_lai`, `trace_id` | Khi nhân viên bấm gửi/sửa/bỏ |
| `staff_rework_completed` | Nhân viên | `phut_lam_lai`, `ly_do`, `trace_id` | Khi nhân viên hoàn thành làm lại thủ công |
| `refund_ledger_write` | Dịch vụ sổ cái | `idempotency_key`, `so_tien`, `ket_qua`, `trace_id` | Khi giao dịch ghi vào sổ cái hoàn tiền |
| `ticket_closed` | Hệ thống ticket | `ticket_id`, `closed_at`, `trace_id` | Khi ticket yêu cầu được đóng |
| `ticket_reopened` | Khách | `ticket_id`, `reopened_at`, `reason`, `trace_id` | Khi khách mở lại ticket trong 7 ngày |
| `audit_sample_checked` | Kế toán | `sample_id`, `so_tien_da_hoan`, `so_tien_dung`, `trace_id` | Định kỳ hàng tuần khi kiểm toán mẫu |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- Chỉ số chính (% đóng trong 24h không mở lại 7 ngày): tính từ `ticket_closed` (đo mốc 24h) và `ticket_reopened` (xác định không mở lại trong 7 ngày) theo từng `trace_id`.
- Tỉ lệ bỏ qua gợi ý: tính từ event `staff_review_decision` (đếm quyết định là `sua` hoặc `bo` chia tổng số quyết định).
- Tỉ lệ lỗi lọt đến khách: tính từ event `ticket_reopened` (mở lại trong 7 ngày) chia tổng số event `refund_request_created`.
- Chỉ số dùng đề xuất: tính từ tỉ lệ giữa số event `agent_suggestion_shown` và số event `refund_request_created` của nhóm can thiệp.
- Chỉ số an toàn đề xuất: tính từ event `audit_sample_checked` (tỉ lệ các bản ghi có `so_tien_da_hoan != so_tien_dung`).

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | Chi phí mỗi việc thành công tăng +51,8%, lên 6.787 đ [simulated] | Tỉ lệ làm lại theo tuần > 7% (đợt chạy thử: 4,9% trong phạm vi) | Thu hẹp phạm vi về riêng `noi_dia`, rà soát 20 trace ca làm lại gần nhất | PM trợ lý hoàn phí |
| Phải duy trì xem lại 100% kéo dài | Đạt 11.743 đ = 0,98× (12.414 đ = 1,03× nếu làm lại 15,3 phút như dữ liệu) [simulated], triệt tiêu lợi ích kinh tế | Tỉ lệ yêu cầu cần xem lại vẫn > 50% ở cuối bước rollout 0.25 | Thực hiện giảm xem lại theo bậc khi tỉ lệ sửa + bỏ < 15% | Trưởng nhóm CSKH |
| Khối lượng xử lý thực tế thấp hơn dự kiến | Chi phí cố định 40 triệu/tháng làm tăng chi phí mỗi việc: +1.185 đ ở 45.000 yc/tháng và +2.370 đ nếu khối lượng giảm còn một nửa [simulated] | Số việc thành công hàng tuần đạt < 50% chỉ tiêu kế hoạch | Tạm dừng mở rộng pilot, đàm phán lại hợp đồng chi phí cố định với đối tác | PM trợ lý hoàn phí |
