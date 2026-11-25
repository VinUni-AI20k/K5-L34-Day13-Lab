# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

Người giữ file: Thành viên 4. Nguồn từng phần:
- Chỉ số chính: `cp5_chi_so` trong `src/tv4_tinh_so.py`, TV2 đối chiếu khớp.
- Chỉ số dùng, chỉ số dùng đề xuất, bảng nối event với chỉ số: [bàn giao CP5 của Thành viên 2](tv2_cp5_ban_giao.md) (`src/tv2_cp5_tinh_so.py`).
- Chỉ số an toàn đề xuất và E2: [bàn giao của Thành viên 3](tv3_ban_giao.md) (`src/tv3_tinh_so.py`).

Thành viên 4 đã chạy lại cả ba script, số khớp nhau. Số từ cột `_simulated` có nhãn `simulated`.

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | **82,83%** (994/1.200); trong phạm vi noi_dia + hang_nang 92,26% (906/982) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | **27,12%** (48/177); trong phạm vi 21,09% (27/128): noi_dia 18,28%, hang_nang 28,57%; ngoài phạm vi quoc_te 46,43%, doi_tac 38,10% |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | **4,25%** (51/1.200); trong phạm vi 3,97% (39/982), riêng hang_nang 8,23% |
| Dùng | Nhóm tự đề xuất (TV2): % yêu cầu của nhóm trợ lý có gợi ý được mở | Số yêu cầu nhóm trợ lý có `agent_suggestion_shown`, chia số yêu cầu nhóm trợ lý (`refund_request_created`, `arm = tro_ly`). Cùng công thức cho nhóm đối chứng đo tràn tác động, mục tiêu 0% | Không cần tính |
| An toàn | Nhóm tự đề xuất (TV3): % mở lại 7 ngày ở ca không được xem lại | Số `ticket_reopened` trong 7 ngày ở yêu cầu không có `staff_review_decision`, chia số yêu cầu không được xem lại | Không cần tính. Đối chiếu từ dữ liệu: 4,99% (51/1.023) ở ca không xem lại, 0,00% (0/129) ở ca xem lại và giữ nguyên; cả 51 ca mở lại đều là `lam_lai` |

- Đây là chỉ số trong đợt chạy thử: 82,83% (92,26% trong phạm vi). Đợt chạy thử không có nhóm đối chứng, nên chưa nói được trợ lý làm chỉ số tăng hay giảm so với mức 0,70 khi chỉ có nhân viên.
- Tỉ lệ bỏ qua gợi ý trong phạm vi là 21,09%: dưới ngưỡng luật dừng 40%, nhưng vẫn cao hơn mốc < 15% cần đạt để giảm xem lại theo bậc. Hai loại bị loại khỏi pilot có tỉ lệ cao nhất (quoc_te 46,43% đã vượt 40%), củng cố lý do thu hẹp phạm vi.
- **Con số bất lợi:** mỗi lượt xem lại trong đợt chạy thử mất trung bình 5,03 phút (644 phút / 128 lượt trong phạm vi) [simulated], sát mức hoà vốn 5,1 phút và đã cao hơn 4,8 phút nếu làm lại mất 15,3 phút (B4) [simulated]. Vì vậy `phut_xem_lai` phải được đo thật bằng event ngay từ tuần 1.
- Chỉ số dùng đề xuất bổ sung cho chỉ số bỏ qua gợi ý: chỉ số bỏ qua chỉ đo khi nhân viên đã xem lại (13,03% yêu cầu trong phạm vi), chưa đo nhân viên có mở trợ lý hay không.
- Chỉ số an toàn đề xuất cần thiết vì giảm xem lại là đòn bẩy chi phí lớn thứ hai (B1: +40,7% khi xem lại gấp đôi [simulated]); chỉ số này cho biết giảm xem lại có làm lỗi lọt đến khách tăng không.

## Danh sách event

Mười hai event, mỗi event có `trace_id` và `request_id`. Theo đề xuất của TV2, mỗi yêu cầu có **một `trace_id` gốc** tạo tại `refund_request_created` và truyền qua cả 3 lần chạy cùng mọi event sau đó. Trong đợt chạy thử, mỗi lần chạy có `trace_id` riêng (1.624 `trace_id` cho 1.200 yêu cầu; 258 yêu cầu chạy lại sinh 682 `trace_id`), nên khó nối lại cả vòng đời một yêu cầu. `request_id` dùng để nối với `arm` (tro_ly hoặc doi_chung).

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | request_id, loai, so_tien, depot, staff_id, arm, created_at, trace_id | Khi khách gửi yêu cầu |
| `agent_run_completed` | Agent | attempt, tokens_in, tokens_out, tool_calls, status, bang_gia_version, trace_id | Sau mỗi lần chạy, kể cả lần lỗi |
| `input_validation_failed` | Agent | ly_do, truong_loi, trace_id | Khi đầu vào của khách không hợp lệ |
| `agent_suggestion_shown` | Giao diện nhân viên | staff_id, so_tien_de_xuat, trace_id | Khi gợi ý hiện ra cho nhân viên |
| `staff_review_decision` | Nhân viên | quyet_dinh (giu, sua, bo), phut_xem_lai đo thật, trace_id | Khi bấm gửi, sửa hoặc bỏ |
| `staff_rework_completed` | Nhân viên | phut_lam_lai đo thật, ly_do, trace_id | Khi làm lại xong |
| `refund_ledger_write` | Dịch vụ sổ cái | idempotency_key, so_tien, ket_qua (ok, loi_tai_khoan, loi_he_thong), trace_id | Khi ghi lệnh hoàn vào sổ cái |
| `refund_notification_sent` | Agent | request_id, kenh, noi_dung (da_hoan, dang_xu_ly), sent_at, trace_id | Khi gửi tin nhắn kết quả hoàn cho khách |
| `handoff_to_staff` | Agent | reason (thieu_du_lieu, ngoai_12_thang, het_lan_chay), tom_tat, trace_id | Khi chuyển yêu cầu cho nhân viên |
| `ticket_closed` | Hệ thống ticket | closed_at, trace_id | Khi yêu cầu được đóng |
| `ticket_reopened` | Khách, qua hệ thống ticket | reopened_at, reason (so_tien, chua_nhan_tien, khac), trace_id | Khi khách mở lại yêu cầu |
| `audit_sample_checked` | Kế toán | so_tien_da_hoan, so_tien_dung, bang_gia_version, trace_id | Hằng tuần, mẫu 100 đơn |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- **Chính:** `refund_request_created` (mẫu số, chia theo `arm`) + `ticket_closed` (`closed_at − created_at ≤ 24 giờ`) + `ticket_reopened` (không có trong 7 ngày sau khi đóng). Đo được.
- **Dùng, bỏ qua gợi ý:** `staff_review_decision` với `quyet_dinh` là sua hoặc bo, chia tổng số `staff_review_decision`. Đo được.
- **An toàn, mở lại 7 ngày:** `ticket_reopened` trong 7 ngày, chia `refund_request_created`. Đo được.
- **Dùng, đề xuất:** `agent_suggestion_shown` chia `refund_request_created` theo `arm`. Đo được; phần nhóm đối chứng dùng cho luật tràn tác động trong `pilot_plan.yaml`.
- **An toàn, đề xuất (TV3):** `ticket_reopened` ở yêu cầu không có `staff_review_decision`. Đo được. TV3 đặt tên tạm `review_completed` và `case_reopened`; nhóm thống nhất dùng `staff_review_decision` và `ticket_reopened`.
- **Ngoài E1, cho luật dừng và bảng lỗi** (bảng nối đầy đủ trong [bàn giao CP5 của TV2](tv2_cp5_ban_giao.md)):
  - Chi phí mỗi việc thành công đo thật (luật dừng 3): tử số là `agent_run_completed` + `phut_xem_lai` của `staff_review_decision` + `phut_lam_lai` của `staff_rework_completed`. Mẫu số là số yêu cầu có `ticket_closed`, không có `ticket_reopened` trong 7 ngày, không có `handoff_to_staff` và không có `staff_rework_completed`, khớp định nghĩa `thanh_cong`.
  - Hoàn trùng (luật dừng 2, ca 20): hơn 1 bản ghi `refund_ledger_write` `ok` cho cùng `request_id`, đối soát mỗi giờ.
  - Báo "đã hoàn" khi sổ cái chưa ghi (luật dừng 2, ca 7): `refund_notification_sent` với `noi_dung = da_hoan` không có `refund_ledger_write` `ok` cùng `trace_id`, đối soát mỗi giờ. Event này do TV2 đề xuất thêm, vì 11 event ban đầu không đo được ca 7.
  - Lỗi ngầm (ca 5, 17): `audit_sample_checked`.

## E2 · Rủi ro kinh tế

Số lấy từ bảng độ nhạy (`bang_chi_phi.md`) và A4. Ba dòng do Thành viên 3 soạn, Thành viên 4 đối chiếu với `src/tv4_tinh_so.py`.

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi (yếu tố mạnh nhất ở B1) | +51,8%, chi phí mỗi việc thành công lên 6.787 đ [simulated] | Tỉ lệ `lam_lai` theo tuần > 7% (đợt chạy thử: 4,89% = 48/982 trong phạm vi) | Thu hẹp về noi_dia, rà 20 trace làm lại gần nhất | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài (B4) | 11.743 đ/việc = 0,98× của 12.000 đ; 12.415 đ = 1,03× nếu làm lại 15,3 phút như dữ liệu; hoà vốn khi mỗi lần xem lại ≤ 5,1 phút (4,8 phút) [simulated] | % yêu cầu được xem lại > 50% vào cuối bước rollout 0.25 (đợt chạy thử: 13,0%) | Giảm xem lại theo bậc khi tỉ lệ sua + bo < 15% (đợt chạy thử: 21,1%) | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến (A4) | Chi phí cố định 40 triệu đ/tháng: +1.185 đ/việc ở 45.000 yêu cầu/tháng, +2.370 đ/việc nếu còn một nửa; hoà vốn ở ≈ 6.212 yêu cầu/tháng [simulated] | Số việc thành công theo tuần < 50% kế hoạch (33.750/tháng) | Không mở rộng pilot, đàm phán lại chi phí cố định | PM trợ lý hoàn phí |

- Mô hình cộng tuyến tính (B2: +5,6% + 40,7% = +46,3% [simulated]), nên khi nhiều rủi ro xảy ra cùng lúc, tác động cộng dồn.
