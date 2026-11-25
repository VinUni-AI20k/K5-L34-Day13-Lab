# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 82,83% (994/1.200 yêu cầu) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 27,12% (48/177 yêu cầu được xem lại) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 4,25% (51/1.200 yêu cầu) |
| Dùng | Tỉ lệ nhân viên chủ động mở xem gợi ý trợ lý | Số yêu cầu nhân viên bấm mở xem gợi ý trợ lý chia cho tổng số yêu cầu giao cho nhóm can thiệp | Không cần tính |
| An toàn | Tỉ lệ đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần | Số đơn hoàn tiền sai lệch chia cho 100 đơn kiểm toán mẫu ngẫu nhiên mỗi tuần | Không cần tính |

*Ghi chú:* Chỉ số trong đợt chạy thử là 82,83%, chưa thể kết luận trợ lý đã nâng chỉ số lên mức này vì đợt chạy thử 2 tuần vừa qua chưa có nhóm đối chứng đồng thời.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách hàng | `request_id, loai, so_tien, arm, trace_id` | Khi khách hàng gửi yêu cầu hoàn phí |
| `agent_run_completed` | Agent | `attempt, tokens_in, tokens_out, tool_calls, status, trace_id` | Sau mỗi lần chạy của agent, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | `staff_id, so_tien_de_xuat, trace_id` | Khi thẻ gợi ý của agent hiển thị trên màn hình CSKH |
| `staff_review_decision` | Nhân viên CSKH | `quyet_dinh (giu/sua/bo), phut_xem_lai, trace_id` | Khi nhân viên bấm duyệt giữ, sửa hoặc bỏ qua gợi ý |
| `staff_rework_completed` | Nhân viên CSKH | `phut_lam_lai, ly_do, trace_id` | Khi nhân viên hoàn thành xử lý thủ công ca làm lại |
| `refund_ledger_write` | Dịch vụ sổ cái tài chính | `idempotency_key, so_tien, ket_qua, trace_id` | Khi thực hiện ghi giao dịch hoàn tiền vào sổ cái |
| `handoff_to_staff` | Agent | `reason, tom_tat, trace_id` | Khi agent chạy lỗi 3 lần hoặc đơn ngoài phạm vi, chuyển người |
| `ticket_closed` | Hệ thống ticket | `closed_at, duration_hours, trace_id` | Khi yêu cầu được giải quyết và đóng ticket |
| `ticket_reopened` | Khách hàng | `reopened_at, reason, trace_id` | Khi khách mở lại ticket trong vòng 7 ngày |
| `audit_sample_checked` | Kế toán kiểm toán | `so_tien_da_hoan, so_tien_dung, ket_qua_audit, trace_id` | Khi kiểm toán viên kiểm tra mẫu 100 đơn hằng tuần |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- **Chỉ số chính (% đóng trong 24h và không mở lại trong 7 ngày):** Đo từ thời điểm tạo trong `refund_request_created` đến thời điểm đóng trong `ticket_closed` (hiệu thời gian <= 24 giờ), đồng thời không xuất hiện event `ticket_reopened` trong vòng 7 ngày tiếp theo với cùng `trace_id`.
- **Chỉ số dùng (Tỉ lệ bỏ qua gợi ý):** Đếm các event `staff_review_decision` có `quyet_dinh` thuộc `['sua', 'bo']` chia cho tổng số event `staff_review_decision` được ghi nhận.
- **Chỉ số an toàn (Tỉ lệ lỗi lọt đến khách):** Đếm số event `ticket_reopened` chia cho tổng số event `refund_request_created`.
- **Chỉ số dùng tự đề xuất (Tỉ lệ chủ động mở gợi ý):** Đếm số event `agent_suggestion_shown` chia cho tổng số event `refund_request_created` được gán cho nhóm can thiệp (`arm == 'treatment'`).
- **Chỉ số an toàn tự đề xuất (Tỉ lệ đơn sai tiền qua kiểm toán):** Đếm số event `audit_sample_checked` có `ket_qua_audit == 'sai_lech'` chia cho tổng số event `audit_sample_checked` trong tuần.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | Chi phí mỗi việc thành công tăng +51,8%, lên 6.787 đ [simulated] | Tỉ lệ ca làm lại theo tuần vượt quá 7% (đợt chạy thử là 4,9% trong phạm vi) | Thu hẹp phạm vi về noi_dia, rà soát 20 trace lỗi làm lại gần nhất để cập nhật rule | PM trợ lý hoàn phí |
| Bắt buộc xem lại 100% kéo dài | Chi phí vọt lên 11.743 đ (0,98× của 12.000 đ) hoặc 12.414 đ (1,03× nếu làm lại 15,3 phút như dữ liệu) [simulated], trợ lý đắt hơn người tự làm | Tỉ lệ yêu cầu được xem lại vẫn > 50% ở cuối bước rollout 0.25 | Giảm tỉ lệ xem lại theo bậc dựa trên độ tin cậy khi tỉ lệ sửa+bỏ < 15% | Trưởng nhóm CSKH |
| Khối lượng thực tế sụt giảm một nửa | Chi phí cố định 40 triệu đ/tháng làm tăng thêm 2.370 đ/việc (lên 5.784 đ = 0,48×) [simulated] | Số việc thành công thực tế theo tuần < 50% kế hoạch pilot | Không mở rộng sang giai đoạn tiếp theo, xem xét đàm phán lại chi phí cố định hạ tầng | PM trợ lý hoàn phí |
