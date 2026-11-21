# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | Tỉ lệ yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | Đếm yêu cầu có `dong_trong_24h = 1` và `mo_lai_trong_7_ngay = 0`, chia tổng số yêu cầu | 994 / 1.200 = **82,83%** |
| Dùng | Tỉ lệ bỏ qua gợi ý | Trong các yêu cầu có `duoc_xem_lai = 1`, đếm yêu cầu có `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 48 / 177 = **27,12%** |
| An toàn | Tỉ lệ mở lại trong 7 ngày, dùng làm tín hiệu lỗi lọt đến khách | Đếm yêu cầu có `mo_lai_trong_7_ngay = 1`, chia tổng số yêu cầu | 51 / 1.200 = **4,25%** |
| Dùng | Tỉ lệ yêu cầu được hiện gợi ý | Theo tuần, đếm yêu cầu đủ điều kiện của nhóm can thiệp đã hiện ít nhất một gợi ý, chia tổng số yêu cầu đủ điều kiện của nhóm can thiệp | Không cần tính |
| An toàn | Tỉ lệ yêu cầu hoàn sai tiền trong mẫu kiểm toán | Theo tuần, đếm yêu cầu trong mẫu có số tiền thực hoàn khác số tiền đúng chính sách, chia tổng số yêu cầu đã kiểm xong | Không cần tính |

Ba kết quả mô tả đợt chạy thử. Mẫu này chưa có nhóm đối chứng để ước lượng tác động của trợ lý. Nguồn là [logix_requests.csv](../../src/logix_requests.csv), đếm một lần theo `request_id`. Trong phạm vi `noi_dia` và `hang_nang` mà [kế hoạch pilot](pilot_plan.yaml) đã chọn, tỉ lệ mở lại tham chiếu là **39 / 982 = 3,97%**. Dùng cùng phạm vi và cửa sổ theo dõi khi so sánh hai nhóm pilot.

## Danh sách event

Mỗi event có `trace_id`, `request_id` và thời điểm phát sinh `event_at`. Tạo mã ngay khi tiếp nhận để nối được cả yêu cầu ở nhóm đối chứng. Khi nhiều event thuộc một yêu cầu, đếm một lần theo `request_id`.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | Hệ thống tiếp nhận | `trace_id`, `request_id`, `event_at`, `arm`, `loai`, `eligible` | Khi nhận yêu cầu và ghi phân nhóm |
| `agent_run_completed` | Dịch vụ trợ lý | `trace_id`, `request_id`, `event_at`, `run_id`, `attempt`, `status`, `tokens_in`, `tokens_out`, `tool_calls` | Sau mỗi lượt chạy, kể cả lượt lỗi và lượt chạy lại |
| `agent_suggestion_shown` | Giao diện CSKH | `trace_id`, `request_id`, `event_at`, `staff_id` | Khi giao diện hiển thị gợi ý cho nhân viên |
| `staff_review_decision` | Giao diện CSKH | `trace_id`, `request_id`, `event_at`, `staff_id`, `decision` (`giu`, `sua`, `bo`), `review_minutes` | Khi nhân viên lưu quyết định xem lại |
| `staff_rework_completed` | Giao diện CSKH | `trace_id`, `request_id`, `event_at`, `reason`, `rework_minutes` | Khi nhân viên làm lại xong vì kết quả trợ lý sai |
| `refund_ledger_write` | Dịch vụ sổ cái | `trace_id`, `request_id`, `event_at`, `refund_key`, `idempotency_key`, `ledger_entry_id`, `amount_vnd`, `status` | Khi có kết quả ghi sổ hoặc thử ghi lại |
| `handoff_to_staff` | Hệ thống điều phối hoàn phí | `trace_id`, `request_id`, `event_at`, `reason`, `staff_id` | Khi chuyển yêu cầu sang luồng nhân viên |
| `ticket_closed` | Hệ thống ticket | `trace_id`, `request_id`, `event_at` | Khi đóng yêu cầu |
| `ticket_reopened` | Hệ thống ticket | `trace_id`, `request_id`, `event_at`, `reason` | Khi mở lại yêu cầu |
| `audit_sample_checked` | Hệ thống kiểm toán | `trace_id`, `request_id`, `event_at`, `refund_paid_vnd`, `refund_due_vnd` | Khi hoàn tất đối chiếu số tiền theo chính sách |

**Đối chiếu chỉ số với event**

- **Chính.** Dùng `refund_request_created` và lần `ticket_closed` đầu để tính thời gian đóng. Đề xuất lấy thời điểm đóng đầu tiên làm mốc bắt đầu cửa sổ mở lại 7 ngày, dùng giống nhau cho hai nhánh. Người phụ trách pilot cần xác nhận mốc này trước khi triển khai vì CSV chỉ có cờ mở lại và kế hoạch pilot hiện chưa ghi thời điểm bắt đầu. Chỉ chốt lô yêu cầu khi đã đủ cửa sổ quan sát, kể cả 24 giờ để đóng và 7 ngày theo dõi sau đó.
- **Bỏ qua gợi ý.** Từ `staff_review_decision`, lấy quyết định cuối của mỗi yêu cầu được xem lại trong cửa sổ đo. Đếm `sua` và `bo`, chia số yêu cầu có quyết định xem lại.
- **Mở lại trong 7 ngày.** Nối `refund_request_created`, lần `ticket_closed` đầu và `ticket_reopened`. Đếm yêu cầu có ít nhất một lần mở lại trong cửa sổ, chia tổng yêu cầu của cùng lô đã đủ thời gian quan sát theo chỉ số chính.
- **Được hiện gợi ý.** Lọc nhóm can thiệp đủ điều kiện từ `refund_request_created`. Nối `agent_suggestion_shown` và đếm mỗi yêu cầu một lần trong tuần đo.
- **Hoàn sai tiền.** Từ `audit_sample_checked`, đối chiếu `refund_paid_vnd` với `refund_due_vnd` trên mẫu đã kiểm xong trong tuần. Chọn mẫu theo cùng quy tắc giữa hai nhóm.

**Đối chiếu chi phí và luật dừng pilot**

- Tính chi phí token và tool theo từng `run_id` từ `agent_run_completed`, gồm cả lần lỗi và chạy lại. Ghép phút xem lại từ `staff_review_decision` và phút làm lại từ `staff_rework_completed`. Dùng `handoff_to_staff` để theo dõi phần việc trợ lý chuyển cho nhân viên.
- Kiểm tra ca hoàn trùng bằng `refund_ledger_write`. Hai bút toán thành công có `ledger_entry_id` khác nhau cho cùng một khoản phải hoàn (`refund_key`) là tín hiệu cần đối soát. Giữ `refund_key` ổn định khi khách gửi lại yêu cầu và dùng `trace_id` để truy ngược từng lượt xử lý. Áp dụng luật dừng hoàn trùng trong [kế hoạch pilot](pilot_plan.yaml).

## E2 · Rủi ro kinh tế

Hai kịch bản tăng gấp đôi dùng B1 trên toàn bộ 1.200 yêu cầu và khớp đầu ra của `src/lab13.py`. Kịch bản xem lại 100% dùng B4 trong phạm vi `noi_dia` và `hang_nang`. Nguồn số là [bảng chi phí nhóm](bang_chi_phi.md).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Khối lượng làm lại tăng gấp đôi | 4.472 → 6.787 đ/việc thành công, **+51,8%** (simulated) | Số yêu cầu có `staff_rework_completed` chia số yêu cầu được tiếp nhận, theo dõi theo tuần và theo loại | Tạm giữ phạm vi khi chi phí vượt ngưỡng đã duyệt. Xem lại trace của các ca làm lại để xác định loại cần thu hẹp | PM trợ lý hoàn phí |
| Chi phí xem lại tăng gấp đôi | 4.472 → 6.292 đ/việc thành công, **+40,7%** (simulated) | Tỉ lệ có `staff_review_decision` trên số yêu cầu tiếp nhận, theo dõi hằng tuần. Dùng `review_minutes` để tách tần suất và thời lượng | Xác định loại yêu cầu tốn thời gian xem lại. Chỉ giảm bước xem lại theo luật an toàn trong pilot | Trưởng nhóm CSKH |
| Duy trì xem lại 100% trong phạm vi pilot | **11.743 đ/việc thành công** nếu làm lại 9 phút/ca, hoặc **12.414 đ/việc thành công** nếu làm lại 15,3 phút/ca, tương ứng **0,98×** và **1,03×** mức nhân viên tự làm 12.000 đ (simulated, B4) | Theo tuần, đếm yêu cầu có `staff_review_decision` trên số yêu cầu đủ điều kiện xem lại trong nhánh trợ lý. Đo thêm `review_minutes` và `rework_minutes` | Dùng thời gian đo thực tế sau tuần đầu để tính lại chi phí. Chỉ giảm xem lại theo bậc khi tỉ lệ sửa hoặc bỏ dưới 15% và vẫn đạt ngưỡng an toàn của pilot | Trưởng nhóm CSKH |

**Cách đối chiếu số.** Cộng token và tool của cả 1.624 lượt chạy theo [đơn giá đề bài](../../docs/du_lieu_va_cong_thuc.md) được 329.585,132 đ. Xem lại 890 phút × 2.000 đ = 1.780.000 đ (simulated). Làm lại 1.132 phút × 2.000 đ = 2.264.000 đ (simulated). Cộng ba khoản và chia 978 việc thành công được 4.471,97 đ (simulated). Mỗi kịch bản B1 nhân đôi đúng khoản tương ứng, giữ nguyên 978 việc thành công rồi tính lại mức thay đổi so với số gốc.
