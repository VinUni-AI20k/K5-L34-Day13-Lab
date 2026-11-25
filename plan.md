# Kế hoạch chia task Lab 13 (Nhóm 3 người — 3npc · L3B)

> **Repo:** `K5-L3B-DAY13-3npc-LaunchEconomics`  
> **Khung giờ tại lớp:** 14:00 – 18:00 (giải lao 15:20 – 15:35)  
> **Mốc chốt hồ sơ duyệt chéo Gate 2a:** 17:00  
> **Deadline nộp link LMS (cá nhân):** 23:59 GMT+7

---

## 1. Quy tắc bắt buộc & cơ cấu điểm

- **Điểm (100đ, không có bonus):** 70đ đối chiếu đáp án (CP1: 20đ, CP2: 15đ, CP3: 10đ, CP4: 15đ, CP5: 10đ; sai số ≤ 2%) + 30đ hội đồng duyệt chéo Gate 2a (C6–C8, mỗi tiêu chí 10đ).
- **5 quy tắc sống còn:**
  1. Qua đủ **3 phép thử A1** (`1,20 · 1,25 · 1,25`) mới làm tiếp.
  2. Mọi số tính từ cột `*_simulated` phải gắn nhãn **`simulated`** (trong `ho_so_launch_v0.md` ghi trạng thái `Giả lập`).
  3. Đối chiếu ngay khi slide chữa hiện lên; bài sau dùng lại số bài trước.
  4. Mỗi câu trả lời **≤ 3 dòng**, có **ít nhất 1 con số**.
  5. **Cấm dùng từ `"production"`** trong mọi file hồ sơ. Người phụ trách phải là **1 vai trò cụ thể**, không ghi `"cả đội"`.

---

## 2. Phân vai cho 3 thành viên

| Thành viên | Họ tên / MSSV | Vai ghi trong `TEAM.md` | Trọng tâm chính |
| --- | --- | --- | --- |
| **Người 1 (Dev 1)** | *(điền)* | Người viết code (CP1–CP2) + Kiểm soát kỹ thuật | Code A1–A4, B1–B4 (`src/lab13.py`); thiết kế event `trace_id` & luật dừng/rollback kỹ thuật |
| **Người 2 (Data/QA)** | *(điền)* | Người kiểm số (CP1–CP2) + Gắn nhãn 1 (CP3) + Người viết code (CP4–CP5) | Tính tay đối chiếu & viết `bang_chi_phi.md`; gắn nhãn độc lập 20 ca; **đổi vai code** D1 & E1 trên máy thứ 2; viết `chi_so.md` |
| **Người 3 (PM/Doc)** | *(điền)* | Người gắn nhãn 2 kiêm giữ hồ sơ | Giữ nhịp thời gian, điền `ho_so_launch_v0.md` từ đầu buổi; gắn nhãn độc lập 20 ca; lead `pilot_plan.yaml`, pitch Gate 2a & tổng hợp nộp bài |

---

## 3. Phân công chi tiết theo mốc thời gian & Checkpoint

### Mốc 0 · Khởi động & cài môi trường (14:00 – 14:10 · 10 phút)

- **Người 1:**
  - [ ] Cài `.venv` trong `src/`, chạy `pip install -r requirements.txt`.
  - [ ] Chạy kiểm tra `python -c "import pandas, numpy, scipy, statsmodels; print('san sang')"` và chạy thử `python lab13.py`.
- **Người 2:**
  - [ ] Cài `.venv` tương tự trên máy thứ 2 (để đổi vai code ở CP4 và đạt checklist chạy trên 2 máy).
  - [ ] Đọc nhanh `docs/du_lieu_va_cong_thuc.md`.
- **Người 3:**
  - [ ] Điền thông tin nhóm, thành viên, vai vào `TEAM.md`.
  - [ ] Mở sẵn `report/team/ho_so_launch_v0.md` và theo dõi 5 quy tắc.

---

### CP1 · Nhiệm vụ A — Mô hình chi phí mỗi việc thành công (14:10 – 14:53 · 40 + 3 phút)

- **Người 1 (`src/lab13.py`):**
  - [ ] Viết 3 hàm A1 (`so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`), chạy đảm bảo in `Ba phép thử đáp án biết trước: ĐẠT` (`1,20 · 1,25 · 1,25`).
  - [ ] Viết `mo_hinh(runs, reqs, ...)` (A2) hỗ trợ sẵn các tham số cho CP2 (`gia_vao`, `gia_ra`, `gia_tool`, `luong_phut`, `he_so_xem_lai`, `he_so_lam_lai`, `max_lan_chay`). Đọc `logix_requests.csv` với `keep_default_na=False`.
  - [ ] Viết đoạn in bảng A3 (theo 4 `loai` + tỉ lệ `ok` theo `attempt`) và tính A4 (chi phí cố định 40 triệu đ/tháng cho phạm vi `noi_dia + hang_nang` ở 45.000 yc/tháng và nửa khối lượng).
  - [ ] Commit & push `src/lab13.py`.
- **Người 2 (`report/team/bang_chi_phi.md`):**
  - [ ] Tính tay đối chiếu ít nhất 1 con số A1 và 1 khoản A2/A4 (kiểm tra đã chia 1.000 token và chia mẫu số 978 việc thành công).
  - [ ] Điền bảng A1, A2 (đủ 9 dòng, có nhãn `simulated`), A3 (đủ 4 dòng), A4 và các câu trả lời (≤ 3 dòng, có số; lưu ý so với 12.000 đ cần cộng phần `chuyen_nhan_vien`).
- **Người 3 (`report/team/ho_so_launch_v0.md`):**
  - [ ] Đối chiếu slide chữa A lúc 14:50 (sai số ≤ 2%).
  - [ ] Điền **Mục 1** (Chi phí mỗi việc thành công) và **Mục 3** (So với nhân viên tự làm) vào `ho_so_launch_v0.md` (Trạng thái = `Giả lập`, Người phụ trách = 1 vai trò cụ thể).

**Điều kiện xong CP1:** `python lab13.py` in ĐẠT + bảng A2/A3/A4; `bang_chi_phi.md` hoàn tất phần A và đủ nhãn `simulated`.

---

### CP2 · Nhiệm vụ B — Bảng độ nhạy (14:53 – 15:20 · 25 + 2 phút)

- **Người 1 (`src/lab13.py`):**
  - [ ] Tại `TODO CP2`, chạy **9 kịch bản B1** và **1 kịch bản cặp B2** (giá token ×2 + xem lại ×2).
  - [ ] Tính **B3**: giới hạn 1, 2, 3 lần chạy → tổng chi phí trợ lý, số ca không thành công, **chi phí cả hệ thống** (`trợ lý + 12.000 × không thành công`).
  - [ ] Tính **B4**: xem lại 100% cho `noi_dia + hang_nang` với cả 2 mức làm lại (9 phút theo đề và 15,3 phút trung bình thực tế trong dữ liệu).
  - [ ] Commit & push `src/lab13.py` trước 15:20.
- **Người 2 (`report/team/bang_chi_phi.md`):**
  - [ ] Tự kiểm tra đối xứng B1 (giảm một nửa = ½ mức tăng của gấp đôi).
  - [ ] Điền bảng B1 (9 dòng), kết quả B2 + xếp hạng 3 yếu tố nhạy nhất (`1. làm lại · 2. xem lại · 3. lương nhân viên`), bảng B3, câu trả lời B3 & B4 (≤ 3 dòng, có số, có nhãn `simulated`).
  - [ ] Commit & push `report/team/bang_chi_phi.md`.
- **Người 3 (`report/team/ho_so_launch_v0.md` + chuẩn bị CP3):**
  - [ ] Đối chiếu slide chữa B lúc 15:18.
  - [ ] Cập nhật **Mục 2** (Ba yếu tố nhạy nhất) vào `ho_so_launch_v0.md` (Trạng thái = `Giả lập`).
  - [ ] Mở sẵn 20 ca lỗi trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` cho Người 2 và Người 3 (chưa trao đổi trước).

> **Giải lao: 15:20 – 15:35 (15 phút).** Sau giải lao, **Người 2** đổi vai sang viết code.

---

### CP3 · Nhiệm vụ C — Bảng lỗi và cách khắc phục (15:35 – 16:08 · 30 + 3 phút)

- **Giai đoạn 1 (15:35 – 15:43 · 8 phút — KHÔNG trao đổi giữa Người 2 & Người 3):**
  - **Người 2 (Gắn nhãn 1):** [ ] Ngồi tách riêng, gắn độc lập cả 20 ca lỗi theo 5 loại Google PAIR (*Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm*) theo **nguyên nhân gốc**.
  - **Người 3 (Gắn nhãn 2):** [ ] Ngồi tách riêng, gắn độc lập cả 20 ca lỗi.
  - **Người 1:** [ ] Dọn sạch code CP1–CP2 trong `src/lab13.py`, chuẩn bị sẵn công thức D1 và cấu trúc `pilot_plan.yaml`.
- **Giai đoạn 2 (15:43 – 15:51 · 8 phút — So nhãn & thống nhất):**
  - **Người 2 + Người 3:**
    - [ ] So 2 bộ nhãn, tính `% đồng thuận = số ca trùng / 20` (**không sửa ngược 2 cột nhãn độc lập**).
    - [ ] Nếu < 80% (< 16/20), viết lại định nghĩa rồi chốt. Ghi 1 câu quy tắc phân biệt cho mỗi ca không trùng.
- **Giai đoạn 3 (15:51 – 16:05 · 14 phút — Bảng khắc phục 5 ca):**
  - **Người 1:** [ ] Đề xuất cách phát hiện đo được (event, ngưỡng, tần suất) & cách khắc phục cho các ca kỹ thuật (Hệ thống, Giới hạn, Ngầm).
  - **Người 2:** [ ] Điền đầy đủ bảng 20 ca, tỉ lệ đồng thuận, quy tắc phân biệt và bảng khắc phục 5 ca (đủ 5 loại) vào `report/team/bang_loi.md`, commit & push.
  - **Người 3:** [ ] Soát cột *"Ai phụ trách"* (1 vai trò cụ thể) và cập nhật **Mục 5** của `ho_so_launch_v0.md`.

**Điều kiện xong CP3:** `bang_loi.md` có 2 bộ nhãn độc lập, đồng thuận ≥ 80%, đủ 5 loại lỗi trong bảng khắc phục.

---

### CP4 · Nhiệm vụ D — Kế hoạch pilot `pilot_plan.yaml` (16:08 – 16:36 · 25 + 3 phút)

- **Người 2 (Đổi vai sang Dev — `src/lab13.py`):**
  - [ ] `git pull --rebase` để lấy code mới nhất của Người 1.
  - [ ] Tại `TODO CP4`, viết code tính **5 câu D1** (`a` theo yêu cầu, `b` theo nhân viên m=75, `c` 20 NV/nhóm, `d` 6 depot/nhóm, `e` chênh 6 điểm với 20 NV/nhóm → m ≥ 299, DE = 6,96), power còn lại ở mức 5 điểm (~0,64), và tỉ lệ `mo_lai_trong_7_ngay` hiện tại (4,25% toàn mẫu; 3,97% trong phạm vi).
  - [ ] Chạy toàn bộ `python lab13.py` trên máy mình (xác nhận chạy sạch trên máy thứ 2), commit & push.
- **Người 3 (Lead `report/team/pilot_plan.yaml`):**
  - [ ] Điền phần chú thích đầu file: 5 câu D1, 5 câu D2 ("tách được tác động"), đánh đổi đã chấp nhận (MDE = 6 điểm, power 0,64 ở 5 điểm), tỉ lệ mở lại hiện tại.
  - [ ] Điền các trường YAML: `owner`, `scope` (`noi_dia + hang_nang`), `assignment`, `rollout`, `primary_metric`, `identifiability`, `interim_looks`, `decision_date`, `simulated_inputs`.
  - [ ] Cập nhật **Mục 6** của `ho_so_launch_v0.md`.
- **Người 1 (Luật dừng & Kiểm tra — `report/team/pilot_plan.yaml`):**
  - [ ] Viết **≥ 3 luật dừng** (an toàn, chi phí, mức độ sử dụng) đủ 4 vế **`NẾU … TRONG … THÌ … KHÔNG THÌ …`** (ngưỡng an toàn tham chiếu 4,25% hiện tại) và điền `rollback`.
  - [ ] Chạy lệnh kiểm tra `yaml.safe_load` và đảm bảo không còn dấu `?` ngoài dòng chú thích.

**Điều kiện xong CP4:** `yaml.safe_load` chạy không lỗi, không còn dấu `?` ngoài comment, đủ D1–D2 và ≥ 3 luật dừng đủ 4 vế.

---

### CP5 · Nhiệm vụ E — Chỉ số, rủi ro & Hồ sơ launch v0 (16:36 – 17:00 · 20 + 4 phút)

- **Người 2 (`src/lab13.py` & `report/team/chi_so.md` — E1 chỉ số & E2 rủi ro):**
  - [ ] Tính thử 3 chỉ số E1 trên 1.200 yêu cầu (Chính: 82,83%; Dùng: 27,12%; An toàn: 4,25%) và đề xuất thêm 1 chỉ số Dùng + 1 chỉ số An toàn. Viết đúng mẫu *"chỉ số trong đợt chạy thử là…"*.
  - [ ] Điền bảng **E2 Rủi ro kinh tế** (≥ 2–3 dòng lấy số từ `bang_chi_phi.md`, có nhãn `simulated` và 1 vai trò phụ trách).
- **Người 1 (`report/team/chi_so.md` — Event & Kiểm tra chéo):**
  - [ ] Viết bảng **≥ 6 event** (khuyến nghị 8–10 event), mọi event đều có `trace_id`.
  - [ ] Viết mục **Kiểm tra chéo**: chỉ rõ mỗi chỉ số E1 tính từ event nào.
- **Người 3 (`report/team/ho_so_launch_v0.md` — CHỐT TRƯỚC 17:00):**
  - [ ] Điền **Mục 4** (Chỉ số) và **Mục 7** (Rủi ro kinh tế — Trạng thái `Giả lập`).
  - [ ] Viết dòng cuối **Đề xuất** (`Go` / `Go có điều kiện` / `No-go`), nêu thẳng các con số bất lợi (power 0,64; xem lại 100% ở B4; ca 7/20) và điều kiện + người phụ trách + ngày kiểm tra.
  - [ ] Rà soát đủ 7 mục trong 1 trang, không có từ `"production"`, gửi nhóm hội đồng lúc **17:00**.

---

### Duyệt chéo Gate 2a (17:00 – 17:45 · 45 phút)

- **17:00 – 17:10:** [ ] Người 3 gửi `ho_so_launch_v0.md` cho nhóm hội đồng; phân vai trả lời câu hỏi (Người 1: chi phí/kỹ thuật, Người 2: cỡ mẫu/power, Người 3: trình bày chính).
- **17:10 – 17:25 (Chấm nhóm n+1 vào `report/team/phieu_cham.md`):**
  - **Người 1:** [ ] Chấm tiêu chí C8 (tách tác động, 20 cụm, luật dừng 4 vế, ngưỡng an toàn).
  - **Người 2:** [ ] Chấm tiêu chí C7 (nhãn `simulated`, thu hẹp phạm vi có số, B4).
  - **Người 3:** [ ] Chấm tiêu chí C6 (đề xuất khớp bằng chứng & số bất lợi), tổng hợp điểm, quyết định, lý do và 1 câu hỏi vào `phieu_cham.md`.
- **17:25 – 17:45:** [ ] Người 3 trình bày 1 phút; cả nhóm trả lời 1 phút câu hỏi hội đồng và ghi lại câu trả lời của nhóm bạn vào `phieu_cham.md`.

---

### Đóng gói, báo cáo & nộp bài (17:45 – 18:00 · 15 phút, hạn LMS 23:59)

- **Cả 3 người:**
  - [ ] Copy `report/team/MSSV_HoTen.md` thành file riêng (`report/team/<MSSV>_<HoTenKhongDau>.md`), giữ nguyên file mẫu, điền đủ 6 mục (gồm mục 5: công cụ AI & cách tự kiểm tra).
  - [ ] Cập nhật phần đóng góp & bằng chứng cá nhân trong `TEAM.md`.
- **Người 2 + Người 3:**
  - [ ] Hoàn thiện `report/team/group_report.md` (≤ 2 trang, dẫn link các file hồ sơ và ghi kết quả duyệt chéo nhận được).
- **Người 1 (Chốt kiểm tra & Push):**
  - [ ] Chạy bộ lệnh kiểm tra cuối (mục 4 bên dưới), commit & push toàn bộ lên `main`.
- **Cả 3 người:**
  - [ ] Kiểm tra repo public/đã mời giảng viên và **từng thành viên tự nộp link repo trên LMS trước 23:59 GMT+7**.

---

## 4. Quy ước Git & lệnh kiểm tra nhanh trước khi nộp

- **Tránh conflict:** Cuối mỗi CP, người chỉnh file chạy `git add <file> && git commit -m "cpX: ..." && git push`; đầu CP tiếp theo các thành viên chạy `git pull --rebase`.
- **Lệnh kiểm tra cuối (PowerShell, chạy từ root repo):**

```powershell
# 1. Chạy toàn bộ code trong src/ (phải in ĐẠT cho 3 phép thử A1)
Push-Location src
python lab13.py

# 2. Kiểm tra pilot_plan.yaml đọc được và không còn dấu ? ngoài comment
python -c "import yaml; yaml.safe_load(open('../report/team/pilot_plan.yaml', encoding='utf-8')); print('YAML OK')"
Select-String -Path ..\report\team\pilot_plan.yaml -Pattern '\?' | Where-Object { $_.Line -notmatch '^\s*#' }

# 3. Kiểm tra không có từ "production" trong toàn bộ report/team/
Select-String -Path ..\report\team\* -Pattern 'production'

# 4. Kiểm tra không dính .venv hoặc .env
Pop-Location
git status
```
