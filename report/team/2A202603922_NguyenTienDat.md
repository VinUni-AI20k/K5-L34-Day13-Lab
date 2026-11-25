# Báo cáo cá nhân — NguyenTienDat-2A202603922

## 1. Thông tin thành viên

- Họ tên: Nguyễn Tiến Đạt
- MSSV: 2A202603922
- Email: ntdkhongdeptrailam5924@gmail.com
- Vai trong nhóm: người kiểm số kiêm người gắn nhãn 2 (Thành viên 2 theo bảng phân công của nhóm; giữ file `report/team/bang_chi_phi.md` ở CP1–CP2)

## 2. Phần việc phụ trách

- **CP1 · A1–A4:** đọc công thức, tính và đối chiếu độc lập A1 (3 phép thử) cùng các khoản A2 từ CSV; giữ và tổng hợp `report/team/bang_chi_phi.md` (ghép A3 của TV3 và A4 của TV4).
- **CP2 · B1–B4:** tổng hợp bảng độ nhạy B1 đủ 9 kịch bản, tính phần trăm thay đổi so với A2, xếp hạng 3 yếu tố ảnh hưởng mạnh nhất; tiếp tục giữ `report/team/bang_chi_phi.md` (ghép B2, B3, B4).
- **CP3 · Gắn nhãn độc lập 20 ca lỗi:** đọc 20 ca lỗi theo khung Google PAIR, chốt độc lập bộ nhãn số 2 trước khi xem bộ nhãn số 1 và bàn giao cho TV3 tính đồng thuận.
- **CP4 · D1(b–d):** tính cỡ mẫu khi chia nhóm theo nhân viên và theo depot, tính hệ số thiết kế `DE` và giới hạn cỡ mẫu hiệu dụng `c / ICC` để làm rõ phương án nào không đủ mẫu.
- **CP5 · E1 (chỉ số sử dụng, event `trace_id`) và rà soát nhất quán:** tính thử chỉ số sử dụng, đề xuất thêm một chỉ số sử dụng, nối 11 event có `trace_id` với toàn bộ chỉ số / luật dừng / bảng lỗi, rà soát chéo 5 file hồ sơ chính trước giờ chốt hội đồng 17:00.

## 3. Đóng góp cụ thể

- **CP1 (`bang_chi_phi.md`):**
  - Đối chiếu 3 phép thử A1 đạt `1,20 · 1,25 · 1,25` và 9 dòng A2 khớp giữa `src/lab13.py` với tính độc lập từ CSV (`token` 245.585 đ, `tool` 84.000 đ trên đủ 1.624 lần chạy kể cả lần lỗi; `xem_lai` 1.780.000 đ và `lam_lai` 2.264.000 đ [`simulated`]; tổng 4.373.585 đ trên 978 việc `thanh_cong` → **4.472 đ/việc** [`simulated`], gấp **16,3 lần** hoá đơn 274,7 đ/yêu cầu).
  - Tích hợp A3 (`noi_dia` 2.696 đ = 0,22×, `hang_nang` 8.221 đ = 0,69×, `quoc_te` 22.515 đ = 1,88×, `doi_tac` 10.215 đ = 0,85× [`simulated`]) và A4 (+cố định 40 triệu đ/tháng: 4.599 đ = 0,38× ở 45.000 yêu cầu/tháng; 5.784 đ = 0,48× ở 22.500 yêu cầu/tháng; hòa vốn ~6.212 yêu cầu/tháng [`simulated`]).
- **CP2 (`bang_chi_phi.md`):**
  - Hoàn thiện bảng B1 đủ 9 kịch bản trên mốc 4.471,9684 đ [`simulated`], kiểm chứng tính đối xứng nửa/gấp đôi và xếp hạng 3 yếu tố nhạy nhất: **1. số ca làm lại** (+51,8%, lên 6.787 đ), **2. tỉ lệ xem lại** (+40,7%, lên 6.292 đ), **3. lương nhân viên tăng 25%** (+23,1%, lên 5.506 đ) [`simulated`]; giá token gấp đôi chỉ +5,6%.
  - Ghép và đối chiếu B2 (token ×2 + xem lại ×2 = 6.543 đ, +46,3% [`simulated`]), B3 (2 lần chạy rẻ nhất cho cả hệ thống: 6.901.220 đ [`simulated`]), B4 (xem lại 100%: 11.743 đ = 0,98× với 9 phút làm lại, 12.415 đ = 1,03× với 15,3 phút làm lại [`simulated`]; hòa vốn ≤ 5,1 phút hoặc 4,8 phút).
- **CP3 (`tv2_cp3_ban_giao.md`):**
  - Chốt độc lập 20/20 nhãn theo nguyên nhân gốc (Do người dùng 4 · Hệ thống 5 · Ngữ cảnh 4 · Giới hạn hệ thống 4 · Ngầm 3). Sau khi TV3 đối chiếu với bộ nhãn độc lập của TV1 trong `report/team/bang_loi.md`, đạt đồng thuận **20/20 = 100%** (vượt ngưỡng 80%, Cohen's kappa 1,00).
- **CP4 (`tv2_cp4_ban_giao.md`):**
  - Tính D1(b): với `m = 75` yêu cầu/nhân viên và `ICC = 0,02`, `DE = 2,48`, cần 3.103 yêu cầu/nhánh = 42 người/nhánh (tổng 84 > 40 nhân viên hiện có → không đủ người).
  - Tính D1(c–d): chia 20 nhân viên/nhánh có cỡ mẫu hiệu dụng tối đa `20 / 0,02 = 1.000 < 1.251`; chia 6 depot/nhánh chỉ đạt trần `6 / 0,02 = 300 < 1.251` → cả hai cách chia cụm đều không đủ mẫu cho mức chênh 5 điểm.
  - Đối chiếu chuyển sang phương án D1(e) của TV3 (20 + 20 nhân viên, MDE 6 điểm, `m ≥ 299`, `DE = 6,96`, 859 hiệu dụng/nhánh; nêu rõ con số bất lợi power ≈ 0,64 nếu tác động thật chỉ 5 điểm) để TV4 hoàn thiện `pilot_plan.yaml`.
- **CP5 (`src/tv2_cp5_tinh_so.py`, `tv2_cp5_ban_giao.md`):**
  - Tính độc lập chỉ số sử dụng: tỉ lệ bỏ qua gợi ý `(sua + bo) / duoc_xem_lai` là **27,12%** (48/177) toàn mẫu và **21,09%** (27/128) trong phạm vi `noi_dia` + `hang_nang` (`noi_dia` 18,28%, `hang_nang` 28,57%, `quoc_te` 46,43%, `doi_tac` 38,10%); thời gian xem lại trung bình **5,03 phút/lượt** [`simulated`].
  - Đề xuất chỉ số sử dụng `% yêu cầu có gợi ý được mở` (`agent_suggestion_shown` ÷ `refund_request_created` theo `arm`) vừa đo tiếp nhận ở nhóm trợ lý, vừa đo tràn tác động mục tiêu 0% ở nhóm đối chứng.
  - Lập bảng nối 11 event có `trace_id` với toàn bộ E1, 4 luật dừng và 5 ca khắc phục; phát hiện `logix_runs.csv` đang sinh 1.624 `trace_id` cho 1.200 `request_id` để góp ý chuẩn hoá 1 `trace_id` gốc/yêu cầu + `request_id`, thêm cờ `thong_bao_da_hoan` cho ca 7 và ghi rõ mẫu số CPS đo thật.
  - Rà soát nhất quán cả 5 file hồ sơ (`bang_chi_phi.md`, `bang_loi.md`, `pilot_plan.yaml`, `chi_so.md`, `ho_so_launch_v0.md`): khớp 100% số liệu, đủ nhãn `simulated`, 0 từ bị cấm theo quy tắc 5 trong `README.md`.

## 4. Bằng chứng

- **Nhánh làm việc:** `dat` (các PR đã merge vào `main`: #4, #7, #11, #16, #19 và nhánh CP5 mới nhất).
- **CP1:** `report/team/bang_chi_phi.md` — commit `edf5976` (PR #4, merge `672ef68`).
- **CP2:** `report/team/bang_chi_phi.md` — commit `716345c` (PR #7, merge `e16763d`).
- **CP3:** `report/team/tv2_cp3_ban_giao.md` — commit `a9e3133` (PR #11, merge `89ebbd1`) và commit `fc2dd2f` (PR #16, merge `3cd5e85`), đối chiếu trong `report/team/bang_loi.md`.
- **CP4:** `report/team/tv2_cp4_ban_giao.md` — commit `5e7f94e` (PR #19, merge `ab1ce93`).
- **CP5:** `src/tv2_cp5_tinh_so.py` (chạy trong `src/`: `python tv2_cp5_tinh_so.py`) và `report/team/tv2_cp5_ban_giao.md` — commit `0dd1727`.

## 5. Công cụ AI đã dùng

- **Trợ lý AI lập trình (Antigravity / Gemini trong IDE):** dùng để tóm tắt phân công checkpoint, viết script kiểm chứng `src/tv2_cp5_tinh_so.py`, trình bày bảng bàn giao CP4–CP5, kiểm tra tính nhất quán giữa 5 file hồ sơ và quét tự động nhãn `simulated` / từ bị cấm theo quy tắc 5.
- **Giới hạn sử dụng theo `RULES.md`:** không dùng AI bịa số và không để AI thay thế việc đối chiếu độc lập. Mọi con số đều được tính từ hai file CSV qua Python (`src/lab13.py`, `src/tv2_cp5_tinh_so.py`) hoặc tính tay theo công thức trong `docs/du_lieu_va_cong_thuc.md`.
- **Cách tự kiểm tra:**
  - Chạy trực tiếp `python lab13.py` và `python tv2_cp5_tinh_so.py` trong `src/`, đối chiếu khớp 0% sai lệch với số tham chiếu và với kết quả của TV1, TV3, TV4.
  - Tự kiểm tra tay công thức hệ số thiết kế `DE = 1 + (m − 1) × ICC`, trần cỡ mẫu hiệu dụng `c / ICC` và tính cộng tuyến tính của B1/B2.
  - Quét toàn bộ `report/team/` và `TEAM.md` để xác nhận không có từ bị cấm theo quy tắc 5 và không còn dấu `?` ngoài chú thích trong `pilot_plan.yaml`.

## 6. Tự đánh giá

- **Đã hoàn thành tốt:** giữ kỷ luật nhánh riêng (không sửa trùng file người khác giữ), hoàn thành đúng hạn cả 5 checkpoint từ A1–A4, B1–B4, gắn nhãn CP3, tính cụm D1(b–d) đến E1 sử dụng / event `trace_id` và rà soát toàn bộ hồ sơ.
- **Điểm cần chuẩn bị kỹ cho phiên bảo vệ Gate 2a:**
  - Giải thích rõ vì sao chi phí mỗi việc thành công (4.472 đ [`simulated`]) gấp 16,3 lần hoá đơn token + tool và vì sao giới hạn 2 lần chạy (6.901.220 đ [`simulated`]) rẻ hơn cho công ty dù 1 lần chạy có CPS thấp hơn.
  - Giải thích trực quan vì sao chia 20 nhân viên/nhánh bị chặn bởi trần `c / ICC = 1.000 < 1.251`, dẫn đến phải chấp nhận MDE 6 điểm (power 0,64 nếu tác động thật chỉ 5 điểm).
  - Giải thích cách 11 event có `trace_id` thay thế hai cột `_simulated` bằng phút xem lại, làm lại đo thật ngay từ tuần 1 pilot.
