# CP5 · Bàn giao và rà soát của Nguyễn Tiến Đạt (Thành viên 2)

Người giữ file `chi_so.md` và `ho_so_launch_v0.md`: Thành viên 4 (Nguyễn Đức Hải). File này bàn giao phần **chỉ số sử dụng**, **thiết kế event có `trace_id` nối với chỉ số**, và **kết quả rà soát tính nhất quán** toàn bộ hồ sơ CP5 để Hải tổng hợp (không sửa trùng file trên nhánh `dat`).

Mọi con số bên dưới được tính độc lập bằng `src/tv2_cp5_tinh_so.py` từ `src/logix_requests.csv` (đọc với `keep_default_na=False`) và `src/logix_runs.csv`. Số tính từ cột `_simulated` ghi rõ nhãn `simulated`.

## 1. Tính thử chỉ số sử dụng trên 1.200 yêu cầu (E1)

**Công thức:** Tỉ lệ bỏ qua gợi ý = số yêu cầu có `quyet_dinh_xem_lai` là `sua` hoặc `bo` ÷ số yêu cầu có `duoc_xem_lai == 1`. Kiểm tra toàn vẹn dữ liệu: 100% yêu cầu có `duoc_xem_lai == 1` đều có nhãn `giu` / `sua` / `bo`, không có ô lệch (0/0).

| Nhóm | Yêu cầu | Có ≥ 1 lần `ok` | Được xem lại | `giu` | `sua` | `bo` | Bỏ qua gợi ý `(sua+bo)/xem` | Phút xem lại TB (`simulated`) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Toàn mẫu | 1.200 | 1.052 (87,67%) | 177 (14,75%) | 129 | 41 | 7 | **27,12%** (48/177) | 5,03 phút (`simulated`) |
| Phạm vi (`noi_dia` + `hang_nang`) | 982 | 948 (96,54%) | 128 (13,03%) | 101 | 24 | 3 | **21,09%** (27/128) | 5,03 phút (`simulated`) |
| `noi_dia` | 824 | 813 (98,67%) | 93 (11,29%) | 76 | 17 | 0 | **18,28%** (17/93) | 5,06 phút (`simulated`) |
| `hang_nang` | 158 | 135 (85,44%) | 35 (22,15%) | 25 | 7 | 3 | **28,57%** (10/35) | 4,94 phút (`simulated`) |
| `quoc_te` | 150 | 59 (39,33%) | 28 (18,67%) | 15 | 11 | 2 | **46,43%** (13/28) | 5,18 phút (`simulated`) |
| `doi_tac` | 68 | 45 (66,18%) | 21 (30,88%) | 13 | 6 | 2 | **38,10%** (8/21) | 4,81 phút (`simulated`) |

- **Kết quả chính:** Toàn mẫu có tỉ lệ bỏ qua gợi ý **27,12%** (48/177); riêng phạm vi pilot `noi_dia` + `hang_nang` giảm còn **21,09%** (27/128), nằm dưới ngưỡng luật dừng 40% nhưng vẫn cao hơn mốc < 15% cần đạt để giảm tỉ lệ xem lại theo bậc.
- **Củng cố phạm vi pilot:** Hai loại bị loại khỏi pilot có tỉ lệ bỏ qua cao nhất là `quoc_te` **46,43%** (13/28, đã vượt ngưỡng dừng 40%) và `doi_tac` **38,10%** (8/21).
- **Liên kết với B4 (`simulated`):** Thời gian xem lại trung bình trong đợt chạy thử là **5,03 phút/lượt** (890 phút / 177 lượt toàn mẫu; 644 phút / 128 lượt trong phạm vi, `simulated`), sát mức hòa vốn 5,1 phút và đã cao hơn 4,8 phút khi làm lại 15,3 phút (`simulated`), nên bắt buộc phải đo thật `phut_xem_lai` bằng event ngay từ tuần 1.

## 2. Đề xuất thêm một chỉ số sử dụng

- **Chỉ số đề xuất:** `% yêu cầu của nhóm trợ lý có gợi ý được mở` (đồng bộ với [chi_so.md](chi_so.md) và [pilot_plan.yaml](pilot_plan.yaml)).
- **Công thức:** Số yêu cầu có ít nhất một event `agent_suggestion_shown` ÷ tổng số yêu cầu `refund_request_created` theo từng nhánh `arm` (`tro_ly` hoặc `doi_chung`).
- **Lý do chọn:** Chỉ số bỏ qua gợi ý chỉ đo chất lượng khi nhân viên *đã* xem lại (13,03% trong phạm vi), chưa đo được việc nhân viên có mở trợ lý hay không. Tính chỉ số này theo `arm` vừa đo mức tiếp nhận ở `arm = tro_ly`, vừa kiểm soát tràn tác động ở `arm = doi_chung` với mục tiêu **0%** lượt mở.

## 3. Thiết kế event có `trace_id` và kiểm tra chéo với chỉ số

Thống nhất dùng **11 event** trong [chi_so.md](chi_so.md) (vượt tối thiểu 6 event, mọi event đều có `trace_id` và nối `arm` qua `request_id`).

### Bảng nối event ↔ chỉ số, luật dừng và bảng lỗi

| Nhóm đo | Chỉ số / điều kiện cần tính | Event tử số & điều kiện lọc | Event mẫu số / đối chiếu | Đo được? |
| --- | --- | --- | --- | --- |
| E1 · Chính | % đóng trong 24 giờ và không mở lại 7 ngày | `ticket_closed` (`closed_at − created_at ≤ 24h`) và không có `ticket_reopened` trong 7 ngày | `refund_request_created` theo `arm` | Có |
| E1 · Dùng (đề bài) | Tỉ lệ bỏ qua gợi ý `(sua + bo) / xem lại` | `staff_review_decision` với `quyet_dinh ∈ {sua, bo}` | Tổng số `staff_review_decision` | Có |
| E1 · Dùng (đề xuất) | % yêu cầu có gợi ý được mở (và đo tràn tác động) | Số yêu cầu có `agent_suggestion_shown` theo `arm` | `refund_request_created` theo `arm` | Có |
| E1 · An toàn (đề bài) | Tỉ lệ mở lại trong 7 ngày | `ticket_reopened` trong 7 ngày sau `closed_at` | `refund_request_created` theo `arm` | Có |
| E1 · An toàn (TV3) | % mở lại 7 ngày ở ca không được xem lại | `ticket_reopened` ở yêu cầu không có `staff_review_decision` | `refund_request_created` không có `staff_review_decision` | Có |
| Luật dừng 2 & Ca 20 | Hoàn trùng cùng mã đơn (ngưỡng 0 ca) | `refund_ledger_write` có > 1 bản ghi `ket_qua = ok` trên cùng `request_id` / `idempotency_key` | Đối soát mỗi giờ | Có |
| Luật dừng 3 & E2 | Chi phí mỗi việc thành công đo thật (≤ 8.000 đ) | Tử số: `agent_run_completed` (`tokens_in/out`, `tool_calls`) + `staff_review_decision.phut_xem_lai` + `staff_rework_completed.phut_lam_lai` | Mẫu số: `ticket_closed` không `ticket_reopened` (7 ngày), không `handoff_to_staff`, không `staff_rework_completed` | Có |
| Bảng lỗi · Ca 1, 4, 17, 18 | Lỗi đầu vào, chuyển nhân viên, lệch bảng giá, hiểu nhầm cách tính | `refund_ledger_write` (`loi_tai_khoan`), `input_validation_failed`, `handoff_to_staff`, `audit_sample_checked`, `ticket_reopened` (`reason = so_tien`) | Theo ngày hoặc tuần qua `trace_id` | Có |

### Ba điểm kỹ thuật đề xuất Hải bổ sung vào `chi_so.md`

1. **Một `trace_id` gốc cho toàn vòng đời yêu cầu (kèm `request_id`):** Trong `logix_runs.csv` của đợt chạy thử, mỗi lần thử có một `trace_id` riêng (1.624 `trace_id` cho 1.200 `request_id`; 258 yêu cầu chạy lại phát sinh 682 `trace_id`). Khi chạy pilot, cần tạo một `trace_id` gốc tại `refund_request_created` và truyền qua cả `attempt` 1–3 cùng các event xem lại, sổ cái, đóng/mở lại; đồng thời ghi `request_id` ở mọi event để không mất liên kết với nhóm đối chứng.
2. **Đóng kín lỗ hổng đối soát cho Ca 7 (luật dừng số 2):** Luật dừng số 2 bắt ca đã gửi tin nhắn `"đã hoàn"` nhưng không có `refund_ledger_write` `ok` cùng `trace_id`. Đề xuất thêm thuộc tính `thong_bao_da_hoan` (true/false) vào `ticket_closed` hoặc tách event thứ 12 `refund_notification_sent` (có `trace_id`, `request_id`, `kenh`, `sent_at`) để đối soát mỗi giờ hoàn toàn từ danh sách event.
3. **Ghi rõ cả mẫu số của CPS đo thật:** Dòng kiểm tra chéo cuối mục Event trong [chi_so.md](chi_so.md) đã nêu đủ tử số; nên bổ sung mẫu số (`ticket_closed` không mở lại 7 ngày, không chuyển nhân viên, không làm lại) để khớp định nghĩa `thanh_cong`.

## 4. Rà soát tính nhất quán trước giờ chốt 17:00

Đã đối chiếu chéo 5 file hồ sơ chính: [bang_chi_phi.md](bang_chi_phi.md), [bang_loi.md](bang_loi.md), [pilot_plan.yaml](pilot_plan.yaml), [chi_so.md](chi_so.md) và [ho_so_launch_v0.md](ho_so_launch_v0.md).

| Hạng mục kiểm tra | Kết quả đối chiếu | Ghi chú |
| --- | --- | --- |
| Ba chỉ số E1 trên 1.200 yêu cầu & phạm vi | **Khớp 100%** | Chính 82,83% (92,26%), bỏ qua gợi ý 27,12% (21,09%), mở lại 7 ngày 4,25% (3,97%; `hang_nang` 8,23%). Đã dùng cách diễn đạt quan sát, không khẳng định nhân quả so với 0,70 |
| Số chi phí A2, A3, A4 và độ nhạy B1–B4 | **Khớp 100%** | 4.472 đ (16,3×), phạm vi 3.414 đ, +cố định 4.599 đ (0,38×) và 5.784 đ (0,48×), làm lại ×2 lên 6.787 đ (+51,8%), xem lại 100% là 11.743 đ (0,98×) / 12.415 đ (1,03×), hoà vốn 6.212 yêu cầu/tháng, B3 rẻ nhất 2 lần chạy 6.901.220 đ (`simulated`) |
| CP3 (`bang_loi.md` ↔ `ho_so_launch_v0.md`) | **Khớp 100%** | Đồng thuận 20/20 = 100%, phân bố 4 · 5 · 4 · 4 · 3, 5 ca khắc phục (1, 20, 18, 4, 17) |
| CP4 (`pilot_plan.yaml` ↔ `ho_so_launch_v0.md`) | **Khớp 100%** | Chia nhân viên 20 + 20, MDE 6 điểm (859/nhóm, DE 6,96, m ≥ 299), power 0,64 ở 5 điểm, 4 luật dừng đủ 4 vế NẾU – TRONG – THÌ – KHÔNG THÌ, không còn dấu `?` ngoài chú thích, ngày quyết định `2027-01-18` |
| Nhãn `simulated` và quy tắc 5 (`README.md`) | **Đạt** | Mục 1, 2, 3, 7 của `ho_so_launch_v0.md` ghi trạng thái `Giả lập`; toàn bộ số `_simulated` có nhãn; quét toàn bộ `report/team/` và `TEAM.md` không có từ bị cấm theo quy tắc 5 |
| Người phụ trách & đề xuất cuối | **Đạt** | Cả 7 mục và 5 điều kiện của đề xuất **Go có điều kiện** đều ghi một vai trò cụ thể (không ghi "cả đội") |

### Việc cần chốt cùng nhóm trước khi nộp

1. **Hải (TV4):** Cập nhật dòng nguồn đầu [chi_so.md](chi_so.md) dẫn chiếu thêm file bàn giao này của TV2 (`src/tv2_cp5_tinh_so.py`) và cân nhắc bổ sung 3 điểm kỹ thuật về event ở mục 3.
2. **Nhung (TV1):** Bổ sung phần in bảng A3 và cỡ mẫu D1 vào `src/lab13.py` (hiện còn 2 dòng `# TODO CP1` và `# TODO CP4`) để một lệnh `python lab13.py` in đủ A, B, D1 theo checklist nộp bài.
3. **Cả nhóm (sau 17:00):** Hoàn thiện `report/team/phieu_cham.md` khi duyệt chéo, `report/team/group_report.md`, `TEAM.md` và báo cáo cá nhân của từng thành viên (`report/team/MSSV_HoTen.md`).
