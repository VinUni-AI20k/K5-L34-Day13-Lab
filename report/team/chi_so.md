# Đặc tả chỉ số, event và rủi ro kinh tế · E1, E2

Người phụ trách: Nguyễn Hoàng Gia An — Trưởng nhóm. Nguồn: `src/lab13.py`, kết quả lưu tại `report/evidence/lab13-output.txt`; toàn bộ CSV của lab là dữ liệu giả lập.

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Tử số / mẫu số | Kết quả đợt chạy thử | Cửa sổ, phân nhóm | Người phụ trách |
| --- | --- | --- | --- | --- | --- |
| Chính | Đóng trong 24 giờ, không mở lại 7 ngày | Yêu cầu có dong_trong_24h=1 và mo_lai_trong_7_ngay=0 / tổng yêu cầu | 994/1.200 = 82,83% | Đo theo cohort tạo yêu cầu đã đủ 7 ngày; tách arm, depot, loai; ITT theo phân bổ ban đầu | PM trợ lý hoàn phí |
| Dùng | Tỉ lệ bỏ qua gợi ý | Yêu cầu được xem lại, quyết định cuối là sua hoặc bo / yêu cầu được xem lại | 48/177 = 27,12% | Theo tuần, tách staff_id và loai; mỗi request_id một quyết định cuối | Trưởng nhóm CSKH |
| An toàn | Mở lại trong 7 ngày, chỉ báo lỗi lọt đến khách | Yêu cầu có ít nhất một lần mở lại trong 7 ngày / tổng yêu cầu đủ 7 ngày | 51/1.200 = 4,25%; phạm vi pilot 39/982 = 3,97% | Cohort theo ngày tạo và arm; cửa sổ 7 ngày đầy đủ | Giám đốc vận hành |
| Dùng tự đề xuất | Tỉ lệ tiếp nhận trợ lý | Yêu cầu arm=treatment trong phạm vi có agent_workspace_opened / tổng yêu cầu arm=treatment trong phạm vi | Chưa có event thật; không tính từ CSV | Theo tuần, distinct request_id; mở lại giao diện không tăng tử số | Trưởng nhóm CSKH |
| An toàn tự đề xuất | Tỉ lệ sai tiền qua kiểm toán | Yêu cầu có số tiền đã hoàn khác số tiền đúng theo chính sách / số yêu cầu đã kiểm toán | Chưa có dữ liệu kiểm toán; không suy diễn từ mo_lai_trong_7_ngay | Lấy ngẫu nhiên 100 yêu cầu đã hoàn/tuần, tách arm; mỗi yêu cầu một kết luận kiểm toán | Kế toán trưởng |

Đợt chạy thử có chỉ số chính 82,83%, chưa có đối chứng nên không suy ra mức tăng so với baseline giả định 70%. Mở lại là chỉ báo thay thế, không chứng minh mọi yêu cầu không mở lại đều đúng tiền.

Chỉ đưa cohort đủ 7 ngày vào báo cáo kết quả; chưa đủ cửa sổ phải ghi “chưa trưởng thành”, không tính là không mở lại. Mẫu số 0 hiển thị “chưa đủ dữ liệu”. Mục tiêu chính pilot: +6 điểm phần trăm, cỡ mẫu 859 hiệu dụng/nhánh; nếu tác động thật +5 điểm thì power chỉ 0,6417.

## Danh sách event

Đây là thiết kế cần triển khai, chưa phải log đã phát sinh. Mỗi event bắt buộc có `event_id`, `occurred_at` (UTC), `request_id`, `trace_id`, `arm`, `depot`, `loai`; các cột dưới đây là thuộc tính bổ sung. `event_id` khử trùng khi gửi lại; giữ nguyên arm theo phân bổ nhân viên đầu kỳ. Không ghi nội dung khách hay định danh cá nhân trực tiếp.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| refund_request_created | App khách | trace_id, staff_id, so_tien_vnd, scope_version, assignment_version | Khi nhận yêu cầu, gồm cả đối chứng và luồng làm tay |
| agent_workspace_opened | Giao diện CSKH | trace_id, staff_id, session_id | Nhân viên mở trợ lý cho yêu cầu trong phạm vi |
| agent_run_completed | Agent | trace_id, run_id, attempt, tokens_in, tokens_out, tool_calls, status, pricing_version | Kết thúc từng lần chạy, kể cả lỗi |
| agent_suggestion_shown | Giao diện CSKH | trace_id, staff_id, suggestion_id, so_tien_de_xuat | Khi gợi ý đã hiển thị thành công |
| staff_review_decision | Giao diện CSKH | trace_id, staff_id, suggestion_id, decision=giu/sua/bo, phut_xem_lai_measured, is_final | Khi chốt quyết định xem lại |
| staff_rework_completed | Giao diện CSKH | trace_id, staff_id, phut_lam_lai_measured, reason, rework_id | Khi hoàn tất làm lại |
| refund_ledger_write | Dịch vụ sổ cái | trace_id, ledger_entry_id, idempotency_key, so_tien_vnd, result, tariff_version | Sau mỗi lần ghi sổ hoặc từ chối trùng |
| handoff_to_staff | Agent | trace_id, staff_id, reason, summary_ref | Khi chuyển nhân viên |
| ticket_closed | Dịch vụ ticket | trace_id, closed_at, outcome, final_refund_amount | Khi đóng yêu cầu |
| ticket_reopened | Dịch vụ ticket | trace_id, reopened_at, reason | Khi yêu cầu mở lại |
| audit_sample_checked | Công cụ kế toán | trace_id, audit_id, audit_week, sampled_at, refunded_amount, correct_amount, policy_version, verdict | Khi kiểm tra mẫu ngẫu nhiên hằng tuần |

Một request_id có thể có nhiều trace_id (lần chạy/giao dịch); nối qua request_id và bảng ánh xạ trace của từng lần chạy. Yêu cầu làm tay vẫn tạo trace_id cấp yêu cầu. Không gộp mẫu số bằng cách đếm trace_id.

## Bảng kiểm tra chéo chỉ số và event

| Chỉ số / phép kiểm | Event tử số | Event mẫu số / nối | Kiểm tra chất lượng |
| --- | --- | --- | --- |
| Chính: đóng 24 giờ, không mở 7 ngày | ticket_closed và không có ticket_reopened trong 7 ngày tính từ created_at | refund_request_created; nối request_id, trace_id; giữ arm ban đầu | closed_at − created_at ≤24h; ≥0; dữ liệu đủ 7 ngày và qua độ trễ 24h |
| Bỏ qua gợi ý | staff_review_decision có decision=sua/bo và is_final=true | staff_review_decision cuối mỗi request_id được xem lại; đối chiếu agent_suggestion_shown | Quyết định không có suggestion_id hợp lệ phải báo thiếu log; không coi thiếu quyết định là giu |
| Mở lại 7 ngày | ticket_reopened có reopened_at trong 7 ngày tính từ created_at | refund_request_created đủ cửa sổ 7 ngày | Đếm distinct request_id, đối chiếu ticket_closed; không bỏ trường hợp mở lại nhiều lần |
| Tiếp nhận trợ lý | agent_workspace_opened trong arm=treatment, đúng scope_version | refund_request_created của treatment trong phạm vi | Distinct request_id; phát hiện event mở trợ lý ở đối chứng để đo tràn tác động |
| Sai tiền kiểm toán | audit_sample_checked có refunded_amount != correct_amount | audit_sample_checked thuộc mẫu ngẫu nhiên đã hoàn, kết luận cuối mỗi request_id | Nối refund_ledger_write thành công, kiểm policy_version; 100 yêu cầu/tuần, thiếu mẫu phải báo |
| Chi phí/việc thành công | agent_run_completed + staff_review_decision + staff_rework_completed | ticket_closed.outcome=thanh_cong, chốt sau 7 ngày và đối soát sổ cái | Cộng mọi run_id kể cả lỗi; đo phút thật, không cộng các bản gửi lại |
| Hoàn trùng | refund_ledger_write thành công có cùng idempotency_key hơn 1 ledger_entry_id | refund_request_created, refund_ledger_write | Ngưỡng ≥1 ca: cảnh báo ngay, không chờ đủ 3 ngày |

## E2 · Rủi ro kinh tế

Các giá trị từ thời gian nhân viên, chi phí tổng, CPS và tỉ số chi phí dưới đây đều **simulated**; chưa dùng để khẳng định tiết kiệm thật. Số đối chiếu tại `bang_chi_phi.md`.

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | Toàn mẫu: CPS 4.471,97 → 6.786,90 đ, +51,77% (simulated) | Tỉ lệ làm lại phạm vi >7%/tuần; hiện 48/982 =4,89% | Thu hẹp về noi_dia, rà 20 trace làm lại trong 3 ngày | PM trợ lý hoàn phí |
| Xem lại 100% kéo dài | Phạm vi: CPS 11.742,79 đ với 9 phút làm lại; 12.414,79 đ với 15,3 phút; lần lượt 0,979× và 1,035× baseline (simulated) | >50% yêu cầu vẫn cần xem lại cuối bước rollout 0,25; đo phút thật hằng ngày | Giữ bước rollout; chỉ giảm xem lại theo bậc khi sửa+bỏ <15% và kiểm toán không vượt 1% sai tiền | Trưởng nhóm CSKH |
| Khối lượng giảm một nửa | Cố định 40 triệu/tháng: 1.185,19 → 2.370,37 đ/việc; CPS + cố định 4.599,09 → 5.784,27 đ (simulated) | Việc thành công trong phạm vi <50% mức dự kiến 33.750/tháng | Chưa mở rộng, rà lại hợp đồng và phân bổ cố định | PM trợ lý hoàn phí |
