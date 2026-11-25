# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | **82,83% (994/1.200)** |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | **27,12% (48/177)** |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | **4,25% (51/1.200)** |
| Dùng (đề xuất) | Tỉ lệ hiển thị gợi ý | Trong nhóm dùng trợ lý, số yêu cầu đủ điều kiện có ít nhất một gợi ý hiển thị chia cho tổng số yêu cầu đủ điều kiện. | Không cần tính |
| An toàn (đề xuất) | Tỉ lệ hoàn sai tiền qua đối soát | Số yêu cầu được đối soát có `so_tien_da_hoan` khác `so_tien_dung` chia cho tổng số yêu cầu đã đối soát. | Không cần tính |

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Dùng `request_id` để gom event theo yêu cầu và `trace_id` để truy vết lần xử lý. Hệ thống tiếp nhận và hệ thống ticket ghi `trace_id` cho cả nhóm dùng trợ lý và nhóm đối chứng.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | Hệ thống tiếp nhận | `request_id`, `trace_id`, `created_at`, `loai`, `arm`, `du_dieu_kien` | Khi tiếp nhận yêu cầu ở một trong hai nhóm pilot. |
| `agent_run_completed` | Agent | `request_id`, `trace_id`, `staff_id`, `attempt`, `status`, `tokens_in`, `tokens_out`, `tool_calls` | Khi một lượt chạy kết thúc, kể cả lượt lỗi. |
| `agent_suggestion_shown` | Giao diện CSKH | `request_id`, `trace_id`, `staff_id`, `shown_at` | Khi gợi ý hiện trên màn hình nhân viên. |
| `staff_review_decision` | Giao diện CSKH | `request_id`, `trace_id`, `decision` (`giu`, `sua`, `bo`), `decided_at`, `phut_xem_lai` đo thực tế | Khi nhân viên xác nhận quyết định xem lại. |
| `staff_rework_completed` | Giao diện CSKH | `request_id`, `trace_id`, `phut_lam_lai` đo thực tế, `ly_do` | Khi nhân viên xác nhận đã làm lại xong. |
| `ticket_closed` | Hệ thống ticket | `request_id`, `trace_id`, `closed_at` | Mỗi lần đóng yêu cầu, ở cả hai nhóm. |
| `ticket_reopened` | Hệ thống ticket | `request_id`, `trace_id`, `reopened_at`, `reason` | Mỗi lần mở lại yêu cầu, ở cả hai nhóm. |
| `audit_sample_checked` | Hệ thống đối soát | `request_id`, `trace_id`, `so_tien_da_hoan`, `so_tien_dung`, `checked_at` | Khi hoàn tất đối soát một yêu cầu được lấy mẫu. |
| `input_validation_failed` | Giao diện tiếp nhận | `request_id`, `trace_id`, `ly_do` | Khi phát hiện thông tin đầu vào sai định dạng trước khi tạo lệnh hoàn. |
| `refund_ledger_write` | Dịch vụ sổ cái | `request_id`, `trace_id`, `refund_entitlement_id`, `ledger_transaction_id`, `idempotency_key`, `status` | Khi có kết quả ghi sổ, kể cả lần ghi thất bại. |
| `order_lookup_completed` | Dịch vụ tra đơn | `request_id`, `trace_id`, `status` | Khi tra đơn kết thúc, kể cả khi đơn ngoài khoảng dữ liệu lưu trữ. |

### Kiểm tra chéo chỉ số và event

Nối event với `refund_request_created` qua `request_id` để lấy `arm` và đếm mỗi yêu cầu một lần trong từng nhóm. Lấy lần đóng đầu để xác định mốc 24 giờ từ khi tiếp nhận và cửa sổ theo dõi mở lại 7 ngày. Chốt chỉ số sau khi các yêu cầu đã đóng trong kỳ đo có đủ thời gian theo dõi. Các yêu cầu chưa đóng vẫn nằm trong mẫu số tổng yêu cầu.

| Chỉ số | Event dùng để tính | Cách tính từ event |
| --- | --- | --- |
| Đóng trong 24 giờ và không mở lại trong 7 ngày | `refund_request_created`, `ticket_closed`, `ticket_reopened` | Đếm yêu cầu đóng lần đầu trong 24 giờ kể từ `created_at` và không có `reopened_at` trong 7 ngày sau lần đóng đó. Chia cho tổng số yêu cầu trong kỳ đo. |
| Tỉ lệ bỏ qua gợi ý | `staff_review_decision` | Chia số yêu cầu có quyết định xem lại cuối là `sua` hoặc `bo` cho số yêu cầu có quyết định xem lại. |
| Tỉ lệ mở lại trong 7 ngày | `refund_request_created`, `ticket_closed`, `ticket_reopened` | Chia số yêu cầu mở lại trong 7 ngày sau lần đóng đầu cho tổng số yêu cầu trong kỳ đo. |
| Tỉ lệ hiển thị gợi ý (đề xuất cho chỉ số dùng bổ sung) | `refund_request_created`, `agent_suggestion_shown` | Trong nhóm dùng trợ lý, chia số yêu cầu đủ điều kiện có ít nhất một gợi ý hiển thị cho tổng số yêu cầu đủ điều kiện. |
| Tỉ lệ hoàn sai tiền qua đối soát (đề xuất cho chỉ số an toàn bổ sung) | `audit_sample_checked` | Chia số yêu cầu được đối soát có `so_tien_da_hoan` khác `so_tien_dung` cho tổng số yêu cầu đã đối soát. |

- **Hoàn tiền trùng:** Từ `refund_ledger_write`, cảnh báo khi cùng `refund_entitlement_id` có ít nhất hai `ledger_transaction_id` thành công khác nhau. Áp dụng luật dừng an toàn khi phát hiện từ một ca. [Kế hoạch pilot](pilot_plan.yaml)
- **Tách nhóm đối chứng:** Đối chiếu `staff_id` trong `agent_run_completed` với danh sách phân nhóm. Số lượt gọi trợ lý từ tài khoản đối chứng phải bằng 0. [Kế hoạch pilot](pilot_plan.yaml)

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | B1: chi phí tăng **51,8%**, lên **6.787 đ/việc thành công `simulated`** | Tỉ lệ yêu cầu phải làm lại và số phút làm lại mỗi ca | Rà `ly_do` và phút làm lại theo loại yêu cầu mỗi tuần. Nếu chi phí biến đổi vượt **6.000 đ/việc thành công** trong hai tuần liên tiếp, áp giới hạn hai lượt chạy và thu hẹp về `noi_dia` theo luật dừng. | Quản lý sản phẩm trợ lý hoàn phí |
| Xem lại 100% kéo dài trong phạm vi `noi_dia` và `hang_nang` | B4: **11.743–12.415 đ/việc thành công `simulated`**, bằng **0,98–1,03×** mốc 12.000 đ, tuỳ thời gian làm lại | Tỉ lệ yêu cầu được xem lại và số phút xem lại mỗi ca | Đo `phut_xem_lai` và so tỉ lệ mở lại trong bảy ngày với đối chứng. Giảm mức xem lại từng bước sau khi đủ thời gian theo dõi và đạt ngưỡng an toàn. Nếu chạm luật dừng, báo Giám đốc vận hành xử lý theo kế hoạch pilot. | Trưởng nhóm CSKH |

Các vai trò trong bảng là phân công đề xuất cho pilot. [Luật dừng của pilot](pilot_plan.yaml)
