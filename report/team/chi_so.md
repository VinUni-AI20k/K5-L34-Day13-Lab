# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 82,83% (994/1.200 yêu cầu) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 27,12% (48/177 yêu cầu được xem lại) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 4,25% (51/1.200 yêu cầu) |
| Dùng | Nhóm tự đề xuất: Tỉ lệ nhân viên mở gợi ý của trợ lý | Số yêu cầu thuộc nhóm dùng trợ lý có event `agent_suggestion_shown` (theo `staff_id`), chia tổng số yêu cầu được giao cho nhóm dùng trợ lý (`refund_request_created` có `arm = tro_ly`) | Không cần tính |
| An toàn | Nhóm tự đề xuất: Tỉ lệ đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần | Số đơn trong mẫu kiểm tra có `so_tien_da_hoan` khác `so_tien_dung` (event `audit_sample_checked`), chia số đơn được kiểm tra trong tuần. Bắt được cả lỗi sai tiền mà khách không mở lại, nên chỉ số "mở lại 7 ngày" không thấy | Không cần tính |

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
| `handoff_to_staff` | Agent | `reason` (vd. `thieu_du_lieu`, `ngoai_pham_vi`), `tom_tat`, `trace_id` | Khi agent chuyển yêu cầu cho nhân viên |
| `input_validation_failed` | Agent | `reason` (vd. `ma_khong_hop_le`), `truong_loi`, `trace_id` | Khi đầu vào của khách không hợp lệ |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- Chỉ số chính (% đóng trong 24h không mở lại 7 ngày): tính từ `ticket_closed` (`closed_at` trừ thời điểm `refund_request_created` cùng `trace_id` không quá 24 giờ) và `ticket_reopened` (xác định không mở lại trong 7 ngày) theo từng `trace_id`.
- Tỉ lệ bỏ qua gợi ý: tính từ event `staff_review_decision` (đếm quyết định là `sua` hoặc `bo` chia tổng số quyết định).
- Tỉ lệ lỗi lọt đến khách: tính từ event `ticket_reopened` (mở lại trong 7 ngày) chia tổng số event `refund_request_created`.
- Chỉ số dùng đề xuất: tính từ tỉ lệ giữa số event `agent_suggestion_shown` và số event `refund_request_created` có `arm = tro_ly` (nhóm can thiệp).
- Chỉ số an toàn đề xuất: tính từ event `audit_sample_checked` (tỉ lệ các bản ghi có `so_tien_da_hoan != so_tien_dung`).

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | Chi phí mỗi việc thành công 4.472 đ → 6.787 đ (+51,8%), yếu tố nhạy nhất ở B2 [simulated] | Tỉ lệ ca làm lại theo tuần (event `staff_rework_completed` ÷ số yêu cầu nhóm dùng trợ lý) vượt 7% (đợt chạy thử: 48/982 = 4,9% trong phạm vi noi_dia + hang_nang) | Thu hẹp phạm vi về riêng `noi_dia` (rẻ nhất ở A3: 0,22×) [simulated]; rà 20 trace làm lại gần nhất để tìm nguyên nhân gốc | PM trợ lý hoàn phí |
| Tỉ lệ xem lại không giảm được (phải xem lại gần 100%) | Xem lại gấp đôi: 4.472 đ → 6.292 đ (+40,7%); xem lại 100% (noi_dia + hang_nang): 11.743 đ = 0,98× của 12.000 đ, hoặc 12.415 đ = 1,03× nếu làm lại 15,3 phút/ca [simulated] | % yêu cầu được xem lại (event `staff_review_decision`) còn trên 50% ở cuối bước rollout 0,25; phút xem lại đo thật trung bình vượt mức hoà vốn 5,1 phút (4,8 phút nếu làm lại 15,3 phút/ca) [simulated] | Giảm xem lại theo bậc khi tỉ lệ sửa + bỏ dưới 15% (đợt chạy thử: 27,12%); rút gọn màn hình xem lại để giảm phút mỗi lần | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến làm chi phí cố định tăng | Cố định 40 triệu đ/tháng: 1.185 đ/việc ở 45.000 yêu cầu/tháng (tổng 4.599 đ = 0,38×), 2.370 đ/việc nếu còn một nửa (tổng 5.784 đ = 0,48×) [simulated] | Số việc thành công theo tuần (event `ticket_closed` không có `ticket_reopened` trong 7 ngày) dưới 50% kế hoạch | Tạm dừng mở rộng pilot; đàm phán lại hợp đồng chi phí cố định 40 triệu đ/tháng | Giám đốc vận hành |
