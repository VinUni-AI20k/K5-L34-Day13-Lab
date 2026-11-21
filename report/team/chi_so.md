# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | **82,83%** (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | **27,12%** (48/177: 41 `sua` + 7 `bo`) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | **4,25%** (51/1.200); trong phạm vi `noi_dia` + `hang_nang`: 3,97% (39/982) |
| Dùng | Nhóm tự đề xuất: % yêu cầu của nhóm trợ lý mà nhân viên mở gợi ý | Số yêu cầu `arm = tro_ly` có `agent_suggestion_shown`, chia số `refund_request_created` có `arm = tro_ly` | Không cần tính |
| An toàn | Nhóm tự đề xuất: % đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần (bắt lỗi ngầm như ca 5, 12, 17) | Số `audit_sample_checked` có `so_tien_da_hoan` khác `so_tien_dung`, chia số đơn được kiểm tra trong tuần | Không cần tính |

Số do `src/lab13.py` tính (hàm `in_bang_e1`). Chỉ số chính **trong đợt chạy thử là 82,83%**. Đợt chạy thử không có nhóm đối chứng, nên con số này chưa cho biết tác động của trợ lý so với mức 0,70.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | request_id, loai, so_tien_vnd, depot, staff_id, arm (tro_ly / doi_chung), created_at, trace_id | Khi khách gửi yêu cầu |
| `agent_run_completed` | Agent | attempt, tokens_in, tokens_out, tool_calls, status (ok / loi), trace_id | Sau mỗi lần chạy, kể cả lần lỗi |
| `input_validation_failed` | Agent | truong_loi, gia_tri_nhap, trace_id | Khi mã đơn hoặc danh mục khách nhập không hợp lệ (ca 9) |
| `agent_suggestion_shown` | Giao diện nhân viên | staff_id, so_tien_de_xuat, trace_id | Khi gợi ý hiện cho nhân viên |
| `staff_review_decision` | Nhân viên | staff_id, quyet_dinh (giu / sua / bo), phut_xem_lai đo thật, trace_id | Khi nhân viên bấm giữ, sửa hoặc bỏ |
| `staff_rework_completed` | Nhân viên | staff_id, phut_lam_lai đo thật, ly_do, trace_id | Khi làm lại xong |
| `refund_ledger_write` | Dịch vụ sổ cái | idempotency_key, so_tien, ket_qua (ok / loi), trace_id | Khi ghi sổ hoàn tiền (ca 7, ca 20) |
| `handoff_to_staff` | Agent | reason, tom_tat, trace_id | Khi chuyển yêu cầu cho nhân viên |
| `ticket_closed` | Hệ thống ticket | closed_at, ket_qua, trace_id | Khi đóng yêu cầu |
| `ticket_reopened` | Khách | reopened_at, reason, trace_id | Khi khách mở lại |
| `audit_sample_checked` | Kế toán | so_tien_da_hoan, so_tien_dung, pricing_table_version, trace_id | Hằng tuần, mẫu ngẫu nhiên 100 đơn |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- **Chính:** `ticket_closed.closed_at` trừ `refund_request_created.created_at` không quá 24 giờ, và không có `ticket_reopened` trong 7 ngày sau đó. Mẫu số là số `refund_request_created`.
- **Dùng, tỉ lệ bỏ qua gợi ý:** số `staff_review_decision` có `quyet_dinh` là `sua` hoặc `bo`, chia tổng số `staff_review_decision`.
- **An toàn, lỗi lọt đến khách:** số `ticket_reopened` trong 7 ngày, chia số `refund_request_created`.
- **Dùng, tự đề xuất:** số `agent_suggestion_shown` chia số `refund_request_created` có `arm = tro_ly`.
- **An toàn, tự đề xuất:** `audit_sample_checked` có `so_tien_da_hoan` khác `so_tien_dung`. Ca hoàn trùng đếm bằng `refund_ledger_write` trùng `idempotency_key`.
- **Chi phí mỗi việc thành công** (dùng trong luật dừng thứ hai của `pilot_plan.yaml`): token và tool từ `agent_run_completed`, phút từ `staff_review_decision` và `staff_rework_completed`, chia số `ticket_closed` thành công. Nhờ vậy, sau tuần 1 có thể thay phút `simulated` bằng phút đo thật.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | Chi phí mỗi việc thành công tăng **+51,8%**, từ 4.472 đ lên **6.787 đ** (`simulated`) | Tỉ lệ làm lại theo tuần > 7% (trong đợt chạy thử: 4,9% ở phạm vi `noi_dia` + `hang_nang`) | Thu hẹp phạm vi pilot về `noi_dia`, rà soát 20 trace làm lại gần nhất | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | Chi phí trong phạm vi `noi_dia` + `hang_nang` lên **11.743 đ = 0,98×** của 12.000 đ (hoặc **12.415 đ = 1,03×** nếu làm lại 15,3 phút/ca như dữ liệu, `simulated`); không còn tiết kiệm | Tỉ lệ yêu cầu được xem lại vẫn > 50% ở cuối bước rollout 0,25 hoặc thời gian xem lại trung bình > 4,8 phút | Giảm tỉ lệ xem lại theo bậc khi tỉ lệ `sua` + `bo` < 15%; tối ưu giao diện đối chiếu nhanh | Trưởng nhóm CSKH |
| Khối lượng yêu cầu thấp hơn dự kiến | Chi phí cố định 40 triệu đ/tháng làm cộng thêm **+1.185 đ/việc** ở 45.000 yc/tháng (lên 4.599 đ = 0,38×, `simulated`), và tăng gấp đôi lên **+2.370 đ/việc** nếu khối lượng chỉ còn một nửa (lên 5.784 đ = 0,48×, `simulated`) | Số việc thành công theo tuần đạt < 50% kế hoạch (< 4.200 việc/tuần) | Tạm dừng mở rộng bước rollout, đàm phán lại gói hạ tầng chi phí cố định theo mức dùng | PM trợ lý hoàn phí |
