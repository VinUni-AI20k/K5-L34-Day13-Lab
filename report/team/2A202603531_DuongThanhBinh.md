# Báo cáo cá nhân — Dương Thanh Bình - 2A202603531

## 1. Thông tin thành viên

- Họ tên: Dương Thanh Bình
- MSSV: 2A202603531
- Email: 26ai.binhdt2@vinuni.edu.vn
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): Người kiểm số (CP1–CP2) và Người viết code sau giờ giải lao (CP4) — Thành viên số 2

## 2. Phần việc phụ trách

- **CP1 – Nhiệm vụ A (A2, A3, A4):** Kiểm tra số liệu, đối chiếu mô hình chi phí mỗi việc thành công từ trace, phân tích tách theo 4 loại yêu cầu và cộng chi phí cố định 40 triệu đ/tháng cho phạm vi pilot (`noi_dia` + `hang_nang`), hoàn thiện `report/team/bang_chi_phi.md`.
- **CP2 – Nhiệm vụ B (B1–B4):** Đối chiếu kết quả 9 kịch bản phân tích độ nhạy, kiểm tra kịch bản đổi một cặp, xếp hạng 3 yếu tố ảnh hưởng mạnh nhất, đánh giá chi phí cả hệ thống theo giới hạn số lần chạy (B3) và kịch bản xem lại 100% (B4) trong `report/team/bang_chi_phi.md`.
- **CP4 – Nhiệm vụ D (D1, D2):** Tiếp quản viết code trong `src/lab13.py` sau giờ giải lao; cài đặt các hàm tính cỡ mẫu, hệ số thiết kế (DE), cỡ mẫu hiệu dụng, phân tích 3 phương án chia nhóm pilot, 5 câu kiểm tra "tách được tác động" (D2) và tính tỉ lệ mở lại trong 7 ngày làm căn cứ đặt luật dừng an toàn.

## 3. Đóng góp cụ thể

- **Hoàn thiện báo cáo chi phí và độ nhạy (`report/team/bang_chi_phi.md`):**
  - Hoàn thiện bảng A1 (3 phép thử đáp án biết trước `1,20 · 1,25 · 1,25` — ĐẠT) và bảng A2 đủ 9 dòng: tổng chi phí `4.373.585 đ` (có phần `simulated`), `978` việc thành công, chi phí mỗi việc thành công `4.472 đ` (`simulated`) — gấp `16,3 lần` hoá đơn token + tool (`274,7 đ`/yêu cầu); chi phí cả hệ thống so công bằng với `12.000 đ` là `5.865 đ/yêu cầu = 0,49×` (`simulated`).
  - Hoàn thiện bảng A3 cho 4 loại yêu cầu (`noi_dia` `0,22×`, `hang_nang` `0,69×`, `quoc_te` `1,88×`, `doi_tac` `0,85×` — `simulated`), chứng minh `quoc_te` không đáng xử lý và chạy lại tới 3 lần không giúp (tỉ lệ `ok` giảm từ `30,0%` → `11,4%` → `2,2%`).
  - Hoàn thiện bảng A4 cộng chi phí cố định `40 triệu đ/tháng` cho phạm vi `noi_dia` + `hang_nang`: `4.599 đ = 0,38×` ở quy mô `45.000` yêu cầu/tháng và `5.784 đ = 0,48×` ở một nửa khối lượng (`simulated`).
  - Hoàn thiện bảng B1 (9 kịch bản độ nhạy), B2 (`token ×2 + xem lại ×2` = `6.543 đ`, `+46,3%` `simulated`, xếp hạng 3 yếu tố: 1. Số ca làm lại, 2. Tỉ lệ xem lại, 3. Lương nhân viên), B3 (giới hạn `2` lần chạy rẻ nhất cả hệ thống với `6.901.220 đ` `simulated`, không trùng với mức chi phí mỗi việc thành công thấp nhất là `1` lần) và B4 (xem lại 100%: `11.743 đ = 0,98×` với 9 phút làm lại và `12.414 đ = 1,03×` với trung bình dữ liệu 15,3 phút — `simulated`).
  - Đảm bảo mọi con số từ cột `_simulated` đều có nhãn `simulated`, câu trả lời súc tích (≤ 3 dòng, có số liệu) và không sử dụng từ cấm theo quy định Gate 2a.
- **Cài đặt tính toán pilot (`src/lab13.py` — CP4):**
  - Viết các hàm `co_mau`, `he_so_thiet_ke`, `co_mau_hieu_dung`, `so_yc_moi_cum_toi_thieu` và `chay_nhiem_vu_d`.
  - Tính đủ 5 câu D1 (`1.251`/nhóm theo yêu cầu; `DE = 2,48` và `3.103`/nhóm → `84 > 40` nhân viên khi `m = 75`; giới hạn `< 1.000` với 20 nhân viên/nhóm và `< 300` với 6 depot/nhóm; mức chênh `+6` điểm cần `859`/nhóm → `m ≥ 299` yêu cầu/người với `DE = 6,96`, đánh đổi power cho `+5` điểm còn `0,64`).
  - Xuất kết quả so sánh 3 phương án chia nhóm (chọn chia theo nhân viên `20 + 20`, phân tầng theo depot), 5 câu kiểm tra D2 và tỉ lệ `mo_lai_trong_7_ngay` hiện tại (`4,25%` toàn mẫu, `3,97%` trong phạm vi pilot) để bàn giao cho thành viên phụ trách `pilot_plan.yaml`.

## 4. Bằng chứng

- **Nhánh làm việc:** `feat/member2-cp1-cp2-cp4`
- **Các commit đã push lên repo nhóm:**
  - `71192b4` — `CP1-A & CP2-B Complete cost analysis and sensitivity report` (cập nhật `report/team/bang_chi_phi.md`, +48/-44 dòng).
  - `9a37383` — `CP4-D Implement pilot calculations` (cập nhật `src/lab13.py`, +98/-9 dòng).
- **File bàn giao:**
  - `report/team/bang_chi_phi.md`: đầy đủ bảng A1–A4 và B1–B4, đạt yêu cầu gắn nhãn `simulated`.
  - `src/lab13.py`: chạy thành công `python lab13.py` trong thư mục `src/`, in đầy đủ kết quả D1, D2 và tỉ lệ mở lại 7 ngày.

## 5. Công cụ AI đã dùng

- **Công cụ:** Trợ lý AI lập trình (Antigravity / Gemini) hỗ trợ viết script kiểm tra dữ liệu từ `logix_runs.csv` và `logix_requests.csv`, định dạng bảng markdown trong `report/team/bang_chi_phi.md` và hoàn thiện các hàm tính cỡ mẫu CP4 trong `src/lab13.py`.
- **Cách tự kiểm tra kết quả:**
  - Tự chạy trực tiếp script Python trên hai file dữ liệu gốc `src/logix_runs.csv` và `src/logix_requests.csv` (với `keep_default_na=False`), đối chiếu từng con số với công thức trong `docs/du_lieu_va_cong_thuc.md` và số tham chiếu trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (sai lệch 0%, nằm gọn trong ngưỡng cho phép 2%).
  - Kiểm tra tính chất tuyến tính của bảng độ nhạy B1 (mức giảm khi giảm một nửa bằng đúng nửa mức tăng khi gấp đôi) và kiểm tra power ở mức chênh 5 điểm bằng `statsmodels` (`NormalIndPower`).
  - Chạy lại `python lab13.py` trong `src/` và rà soát toàn bộ file bàn giao để đảm bảo không có từ cấm và mọi số giả lập đều ghi nhãn `simulated`.

## 6. Tự đánh giá

- **Điểm mạnh:** Hoàn thành đầy đủ, đúng hạn toàn bộ phạm vi công việc của Người 2 (CP1, CP2, CP4) với số liệu khớp chính xác 100% từ dữ liệu trace; code CP4 tách biệt rõ ràng, không gây xung đột với phần code CP1–CP2 của Người 1.
- **Điểm cần cải thiện:** Cần phối hợp chặt chẽ hơn với Người 1 khi hợp nhất code `src/lab13.py` (gỡ khối `try/except` tạm sau khi CP1–CP2 được merge) và với Người 4 để rà soát đồng bộ số liệu D1/D2 trong `report/team/pilot_plan.yaml` trước khi đóng gói bản cuối.
- **Mức độ hoàn thành cá nhân:** 100% phần việc được phân công.
