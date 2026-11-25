# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

Tính thử trên `src/logix_requests.csv` (đọc với `keep_default_na=False`). Ba dòng đầu không dùng cột `_simulated`.

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | **82,83%** (994/1.200); phạm vi noi_dia + hang_nang: 92,26% (906/982) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | **27,12%** (48/177: 41 sửa + 7 bỏ); phạm vi noi_dia + hang_nang: 21,09% (27/128) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | **4,25%** (51/1.200); phạm vi noi_dia + hang_nang: 3,97% (39/982) |
| Dùng | Nhóm tự đề xuất: % yêu cầu của nhóm dùng trợ lý được xử lý qua trợ lý | Số `trace_id` có `agent_suggestion_shown` chia số `refund_request_created` có `arm = tro_ly`, theo tuần | Không cần tính; mục tiêu ≥ 80%/tuần, dưới 80% nghĩa là nhân viên đang bỏ qua trợ lý |
| Dùng | Nhóm tự đề xuất: số phút xem lại trung vị (đo thật) | Trung vị `phut_xem_lai` trong `staff_review_decision`, theo tuần | Không cần tính; mốc hoà vốn B4 là ≤ 5,1 phút/lần xem lại [simulated] |
| An toàn | Nhóm tự đề xuất: số ca hoàn trùng | Số mã vận đơn có ≥ 2 bản ghi `refund_ledger_write` với `ket_qua = ok`, theo ngày | Không cần tính; ngưỡng 0 ca, 1 ca là kích luật dừng an toàn |
| An toàn | Nhóm tự đề xuất: % đơn hoàn sai tiền qua kiểm tra mẫu | Số đơn `audit_sample_checked` có `so_tien_da_hoan` khác `so_tien_dung`, chia 100 đơn mẫu/tuần | Không cần tính; ngưỡng 1%; bắt lỗi ngầm mà tỉ lệ mở lại không thấy |

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

- Chỉ số chính trong đợt chạy thử là 82,83%, nhưng không so trực tiếp được với baseline 0,70 vì đợt chạy thử không có nhóm đối chứng chạy cùng thời gian.
- Cả 51 ca mở lại đều là ca `lam_lai` (51/74 = 69% số ca làm lại), nên giảm làm lại là cách chính để giảm chỉ số an toàn.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách / kênh CSKH | request_id, depot, staff_id, loai, so_tien_vnd, arm (tro_ly / doi_chung), trace_id | Khi khách gửi yêu cầu |
| `agent_run_completed` | Agent | attempt, tokens_in, tokens_out, tool_calls, status (ok / loi), depot, trace_id | Sau mỗi lần chạy, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | staff_id, so_tien_de_xuat, can_cu_chinh_sach, trace_id | Khi gợi ý hiện cho nhân viên |
| `staff_review_decision` | Nhân viên | staff_id, quyet_dinh (giu / sua / bo), phut_xem_lai (đo thật), trace_id | Khi nhân viên bấm gửi / sửa / bỏ |
| `staff_rework_completed` | Nhân viên | staff_id, phut_lam_lai (đo thật), ly_do, trace_id | Khi làm lại xong |
| `handoff_to_staff` | Agent | reason (thieu_du_lieu / ngoai_pham_vi / dau_vao_khong_ho_tro / het_3_lan), tom_tat, trace_id | Khi chuyển cho nhân viên |
| `refund_ledger_write` | Dịch vụ sổ cái | idempotency_key, ma_van_don, so_tien, kenh_nhan (vi / ngan_hang), ket_qua, trace_id | Khi ghi sổ hoàn tiền |
| `ticket_closed` | Hệ thống ticket | closed_at, created_at, trace_id | Khi yêu cầu đóng |
| `ticket_reopened` | Khách | reopened_at, reason, trace_id | Khi khách mở lại trong 7 ngày |
| `audit_sample_checked` | Kế toán | so_tien_da_hoan, so_tien_dung, phien_ban_bang_gia, trace_id | Hằng tuần, 100 đơn mẫu |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- Chính: `refund_request_created` (mẫu số, tách theo arm) + `ticket_closed` (closed_at − created_at ≤ 24 giờ) + `ticket_reopened` (không có trong 7 ngày).
- Dùng · bỏ qua gợi ý: `staff_review_decision` (sua + bo chia tổng số quyết định).
- An toàn · lỗi lọt đến khách: `ticket_reopened` chia `refund_request_created`.
- Dùng · % xử lý qua trợ lý: `agent_suggestion_shown` chia `refund_request_created` có arm = tro_ly.
- Dùng · phút xem lại: `staff_review_decision.phut_xem_lai`; thay cột `phut_xem_lai_simulated` bằng phút đo thật sau tuần 1.
- An toàn · hoàn trùng: `refund_ledger_write` nhóm theo ma_van_don; an toàn · sai tiền: `audit_sample_checked`.
- Chi phí mỗi việc thành công cũng đo được: `agent_run_completed` (token, tool) + `staff_review_decision` + `staff_rework_completed`, chia số yêu cầu thành công.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`). Gốc: 4.472 đ mỗi việc thành công [simulated].

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | +51,8%, lên 6.787 đ mỗi việc thành công [simulated]; yếu tố nhạy nhất | Tỉ lệ `staff_rework_completed` theo tuần > 7% (đợt chạy thử: 4,9% trong phạm vi, 48/982) | Thu hẹp về noi_dia, rà 20 trace làm lại gần nhất, giới hạn 2 lần chạy | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | 11.743 đ = 0,98× của 12.000 đ (12.415 đ = 1,03× nếu làm lại 15,3 phút như dữ liệu) [simulated] | % yêu cầu được xem lại còn > 50% cuối bước rollout 0,25; phút xem lại trung vị > 5,1 | Giảm xem lại theo bậc khi tỉ lệ sua + bo < 15% trong 1 tuần | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến | Cố định 40 triệu đ/tháng: +1.185 đ/việc ở 33.750 việc/tháng, +2.370 đ/việc nếu còn một nửa [simulated] | Số việc thành công theo tuần < 50% kế hoạch (dưới khoảng 3.900 việc/tuần) | Không mở rộng pilot; đàm phán lại chi phí cố định theo khối lượng | PM trợ lý hoàn phí |
| Lương nhân viên tăng 25% | +23,1%, lên 5.506 đ mỗi việc thành công [simulated]; yếu tố nhạy thứ 3; mốc nhân viên tự làm cũng lên 6 × 2.500 = 15.000 đ nên tỉ lệ vẫn 0,37× | Đơn giá phút nhân viên trong ngân sách quý > 2.000 đ; tổng phút xem lại + làm lại theo tuần từ event | Ưu tiên giảm phút xem lại và làm lại, vì mỗi phút giảm được nhân với lương mới | Giám đốc vận hành |
