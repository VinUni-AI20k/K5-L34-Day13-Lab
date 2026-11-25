# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu (`1.200`) | 82,83% (994 / 1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu có `duoc_xem_lai` bằng 1 (`177`) | 27,12% (48 / 177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu (`1.200`) | 4,25% (51 / 1.200) *(phạm vi `noi_dia + hang_nang`: 3,97%, 39 / 982)* |
| Dùng | Nhóm tự đề xuất: % yêu cầu của nhóm can thiệp có nhân viên mở và xem gợi ý trợ lý | Số `request_id` duy nhất thuộc nhóm can thiệp có event `agent_suggestion_shown`, chia tổng số yêu cầu nhóm can thiệp trong phạm vi pilot | Không cần tính |
| An toàn | Nhóm tự đề xuất: % đơn hoàn sai số tiền qua kiểm tra mẫu hằng tuần | Số đơn có `so_tien_da_hoan != so_tien_dung` trong event `audit_sample_checked`, chia tổng số đơn được kiểm tra mẫu trong tuần (tối thiểu 100 đơn/tuần, bắt lỗi ngầm như Ca 5, Ca 17) | Không cần tính |

**Lưu ý diễn giải:** Chỉ số chính trong đợt chạy thử là **82,83%** (994/1.200 yêu cầu), tỉ lệ bỏ qua gợi ý là **27,12%** (48/177 yêu cầu được xem lại), và tỉ lệ lỗi lọt đến khách là **4,25%** (51/1.200 yêu cầu; phạm vi `noi_dia + hang_nang`: **3,97%**, 39/982). Không viết *"trợ lý đã nâng chỉ số"* vì đợt chạy thử không có nhóm đối chứng. *(Đã đối chiếu khớp 100% với đầu ra `src/lab13.py` và mục bàn giao E1 của Người 2 trong `report/team/bang_chi_phi.md`.)*

## Danh sách event

Gồm 11 event phủ đủ cả 5 chỉ số ở E1, 3 luật dừng trong `pilot_plan.yaml`, và 5 ca phát hiện lỗi trong `bang_loi.md`. Mọi event đều có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách / Hệ thống CSKH | `request_id`, `loai`, `so_tien_vnd`, `depot`, `arm`, `trace_id` | Khi khách gửi yêu cầu hoàn phí |
| `input_validation_failed` | Cổng tiếp nhận / Agent | `request_id`, `error_type`, `raw_code_type`, `trace_id` | Khi đầu vào khách không hợp lệ (ví dụ nhập mã sàn TMĐT thay mã vận đơn — Ca 9) |
| `agent_run_completed` | Agent | `request_id`, `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status`, `price_table_version`, `trace_id` | Sau mỗi lần chạy agent, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | `request_id`, `staff_id`, `arm`, `so_tien_de_xuat`, `trace_id` | Khi gợi ý trợ lý hiển thị cho nhân viên |
| `staff_review_decision` | Giao diện nhân viên | `request_id`, `staff_id`, `quyet_dinh` (`giu`/`sua`/`bo`), `phut_xem_lai_thuc`, `trace_id` | Khi nhân viên bấm giữ, sửa hoặc bỏ gợi ý (đo thời gian thật thay cột `simulated`) |
| `staff_rework_completed` | Giao diện nhân viên | `request_id`, `staff_id`, `phut_lam_lai_thuc`, `ly_do`, `trace_id` | Khi nhân viên hoàn tất làm lại một ca sai (đo thời gian thật thay cột `simulated`) |
| `handoff_to_staff` | Agent | `request_id`, `loai`, `reason`, `tom_tat`, `trace_id` | Khi trợ lý chuyển yêu cầu sang nhân viên (ví dụ `reason = thieu_du_lieu` — Ca 4) |
| `refund_ledger_write` | Dịch vụ sổ cái | `request_id`, `idempotency_key`, `so_tien_da_hoan`, `ket_qua` (`ok`/`loi`), `trace_id` | Khi ghi nhận lệnh hoàn tiền vào sổ cái (đối soát Ca 7 và phát hiện hoàn trùng Ca 20) |
| `ticket_closed` | Hệ thống ticket | `request_id`, `closed_at`, `resolved_within_24h`, `trace_id` | Khi yêu cầu hoàn phí được đóng |
| `ticket_reopened` | App khách / Hệ thống ticket | `request_id`, `reopened_at`, `within_7_days`, `reopen_reason`, `trace_id` | Khi khách mở lại yêu cầu sau khi đóng |
| `audit_sample_checked` | Bộ phận kế toán | `request_id`, `so_tien_da_hoan`, `so_tien_dung`, `lech_tien`, `price_table_version`, `trace_id` | Khi kiểm tra mẫu định kỳ 100 đơn/tuần so với bảng giá hiện hành |

**Kiểm tra chéo:** ánh xạ từng chỉ số ở bảng E1 sang danh sách event (tất cả 5/5 chỉ số đều đo được):

- **% yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày (Chính):** tính từ `refund_request_created` (mẫu số, lọc theo `arm` và `loai`), `ticket_closed` (`resolved_within_24h = true`) và `ticket_reopened` (không có event với `within_7_days = true` cùng `trace_id`).
- **Tỉ lệ bỏ qua gợi ý (Dùng):** tính từ `staff_review_decision` — tử số là số yêu cầu có `quyet_dinh` thuộc `{sua, bo}`, mẫu số là tổng số yêu cầu có event `staff_review_decision`.
- **Tỉ lệ lỗi lọt đến khách (An toàn):** tính từ `ticket_reopened` có `within_7_days = true` (tử số) chia `refund_request_created` (mẫu số), nối qua `trace_id` và tách theo `arm`.
- **% yêu cầu nhóm can thiệp có nhân viên mở và xem gợi ý trợ lý (Dùng — tự đề xuất):** tính từ số `request_id` duy nhất có `agent_suggestion_shown` (`arm = treatment`) chia tổng `refund_request_created` (`arm = treatment`).
- **% đơn hoàn sai số tiền qua kiểm tra mẫu hằng tuần (An toàn — tự đề xuất):** tính từ `audit_sample_checked` — tử số là số đơn có `so_tien_da_hoan != so_tien_dung`, mẫu số là tổng số đơn có `audit_sample_checked` trong tuần.
- **Liên kết với luật dừng và bảng lỗi:** chi phí đo thật trong pilot tính từ `agent_run_completed`, `staff_review_decision` (`phut_xem_lai_thuc`) và `staff_rework_completed` (`phut_lam_lai_thuc`); ca hoàn trùng & đối soát sổ cái (Ca 7, Ca 20, luật dừng an toàn) theo dõi bằng `refund_ledger_write`; phát hiện Ca 9 và Ca 4 dùng `input_validation_failed` và `handoff_to_staff`.

## E2 · Rủi ro kinh tế

Các số liệu dưới đây lấy trực tiếp từ bảng độ nhạy B1, B4 và chi phí cố định A4 đã chốt trong `report/team/bang_chi_phi.md` (tính bởi `src/lab13.py`); mọi con số phụ thuộc cột `_simulated` đều được gắn nhãn `simulated`.

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi (yếu tố nhạy số 1, B1–B2) | Chi phí mỗi việc thành công tăng **+51,8%**, từ 4.472 đ lên **6.787 đ/việc** `[simulated]` *(làm lại chiếm 51,8% tổng chi phí A2)* | Tỉ lệ làm lại theo tuần (`staff_rework_completed / refund_request_created`) > 7% *(đợt chạy thử: 6,17% toàn mẫu; 4,89% trong phạm vi `noi_dia + hang_nang`)* | Giữ nguyên bước rollout, rà 20 trace làm lại gần nhất để sửa nguyên nhân gốc; thu hẹp về `noi_dia` và giới hạn 2 lần chạy (phương án rẻ nhất toàn hệ thống theo B3: 6.901.220 đ `[simulated]`) nếu chi phí > 8.000 đ trong 2 tuần liên tiếp | PM trợ lý hoàn phí |
| Phải duy trì xem lại 100% kéo dài (phạm vi `noi_dia + hang_nang`, B4) | Chi phí mỗi việc thành công tăng lên **11.743 đ = 0,98×** mốc 12.000 đ (với 9 phút làm lại/ca) hoặc **12.415 đ = 1,03×** (với trung bình CSV 15,3 phút/ca) `[simulated]` — không còn tiết kiệm hoặc đắt hơn nhân viên tự làm | Tỉ lệ yêu cầu bị xem lại (`staff_review_decision / agent_suggestion_shown`) vẫn > 50% cuối bước rollout 0,25 hoặc thời gian xem lại thực tế vượt mức hòa vốn (**5,1 phút/ca** với 9 phút làm lại; **4,8 phút/ca** với 15,3 phút làm lại `[simulated]`) | Giảm tỉ lệ xem lại theo bậc với `noi_dia` khi tỉ lệ sửa + bỏ < 15% trong 1 tuần và rút ngắn giao diện xem lại xuống ≤ 4,5 phút/ca; nếu không đạt thì dừng mở rộng | Trưởng nhóm CSKH |
| Khối lượng yêu cầu thấp hơn dự kiến (phạm vi `noi_dia + hang_nang`, A4) | Chi phí cố định 40 triệu đ/tháng đẩy chi phí mỗi việc thành công từ **4.599 đ (0,38×)** ở 45.000 yc/tháng (cố định +1.185 đ/việc) lên **5.784 đ (0,48×)** khi còn một nửa khối lượng (cố định +2.370 đ/việc) `[simulated]` | Số việc thành công hằng tuần trong phạm vi pilot < 50% sản lượng kế hoạch trong 2 tuần liên tiếp | Tạm dừng chuyển bước rollout, không tăng quy mô hạ tầng và đàm phán lại hợp đồng chi phí cố định 40 triệu đ/tháng | PM trợ lý hoàn phí |
