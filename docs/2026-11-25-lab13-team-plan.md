# Lab 13 · Kế hoạch làm việc cho nhóm 4 người

> Nguồn: README, CHECKPOINTS, RUBRIC, SUBMISSION, RULES, `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`.
> Mục tiêu: nộp đủ 100 điểm (70 đối chiếu + 30 hội đồng), push trước 23h59 GMT+7 ngày lab; hồ sơ sẵn sàng lúc 17:00.

## 1. Vai trò (điền vào `TEAM.md` lúc 14:00)

| Ký hiệu | Vai | Trước giải lao (14:00–15:20) | Sau giải lao (15:35–18:00) |
|---|---|---|---|
| **P1** | Người viết code | Viết `src/lab13.py` (A1, A2, A3, B) | Đổi sang **kiểm số** |
| **P2** | Người kiểm số | Tính tay 1 số/nhiệm vụ, điền `bang_chi_phi.md` | Đổi sang **viết code** (D1, E1) |
| **P3** | Gắn nhãn 1 | Đọc đề, theo dõi "Xong khi"; hỗ trợ B | Gắn nhãn 20 ca (C), viết `pilot_plan.yaml` (D) |
| **P4** | Gắn nhãn 2 + giữ hồ sơ | Điền dần `ho_so_launch_v0.md`, `TEAM.md` | Gắn nhãn 20 ca (C), viết `chi_so.md`, hồ sơ (E) |

Đổi người viết code sau giải lao là yêu cầu của đề: ít nhất hai người phải tự tay tính được chi phí.

## 2. Việc làm trước buổi lab (nhóm trưởng, 15 phút)

- [ ] Fork/đổi tên repo thành `K5-L3B-DAY13-TenNhom-LaunchEconomics` (public hoặc mời giảng viên). Cả nhóm clone **repo nhóm**.
- [ ] Mỗi người cài môi trường: `cd src; python -m venv .venv; .\.venv\Scripts\Activate.ps1; pip install -r requirements.txt` và chạy thử import (`pandas, numpy, scipy, statsmodels`); kiểm tra thêm `pyyaml` (hướng dẫn dùng `yaml.safe_load`).
- [ ] Cả nhóm đọc `RULES.md` và 5 quy tắc của lab. Hai người gắn nhãn **không đọc** mục "Nhãn tham khảo cho 20 ca" (dòng 270–300) trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` trước khi gắn nhãn xong, vì sẽ làm mất tính độc lập.

## 3. Lịch theo checkpoint

### 14:00 · Khởi động (10 phút) — cả nhóm
- [ ] Chốt vai, điền `TEAM.md`. Chạy `python lab13.py` (báo `NotImplementedError` là bình thường).
- Dữ liệu đọc bằng `pd.read_csv('logix_requests.csv', keep_default_na=False)` (bắt buộc).

### CP1 · Nhiệm vụ A (14:10–14:53) — 20 điểm
| Việc | Người | Đầu ra / số đối chiếu |
|---|---|---|
| A1: 3 hàm `so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong` | P1 | `kiem_tra_dap_an_biet_truoc()` in ĐẠT (1,20 · 1,25 · 1,25). **Chưa đạt thì dừng**, chưa làm tiếp |
| A2: `mo_hinh(...)` | P1 | cps ≈ **4.472 đ**, tổng 4.373.585, 978 việc thành công, hoá đơn/yêu cầu ≈ 274,7, gấp **16,3×** |
| Kiểm tay: ví dụ token 245.585 + tool 84.000 + xem lại 1.780.000 + làm lại 2.264.000 | P2 | Ghi cách tính vào báo cáo cá nhân |
| A3: vòng lặp theo `loai` (4 dòng) | P1 | noi_dia 2.696 · hang_nang 8.221 · quoc_te 22.515 · doi_tac 10.215; thêm pivot tỉ lệ ok theo attempt |
| A4: chi phí cố định 40 triệu | P2 | 1.185 đ/việc → 4.599 đ (0,38×); nửa khối lượng: 5.784 đ (0,48×) |
| So với 12.000 đ: cả hệ thống 5.865 đ/yêu cầu = 0,49× (phải cộng 222 ca nhân viên làm thay) | P2 | Không viết "0,37×" |
| Điền `bang_chi_phi.md` (A2 đủ 9 dòng, A3 đủ 4 dòng, **nhãn `simulated`**) | P4 | |
| Trang hồ sơ: mục 1 (chi phí/việc), mục 3 (so nhân viên) | P4 | Trạng thái "Giả lập" |

Cẩn thận: chia token cho 1.000; mẫu số là 978 chứ không phải 1.200; tử số gồm cả lần chạy lỗi.

### CP2 · Nhiệm vụ B (14:53–15:20) — 15 điểm
| Việc | Người | Đầu ra |
|---|---|---|
| B1: 9 kịch bản bằng vòng lặp gọi `mo_hinh` | P1 | 4.723 · 4.346 · 6.292 · 3.562 · 6.787 · 3.315 · 5.506 · 4.237 · 4.111 |
| Tự kiểm: "giảm nửa" = một nửa mức tăng của "gấp đôi" (5,6→2,8; 40,7→20,3) | P2 | |
| B2: cặp token×2 + xem lại×2 = 6.543 đ (+46,3%); xếp hạng **1. làm lại · 2. xem lại · 3. lương** | P3 | |
| B3: giới hạn 1/2/3 lần, chi phí cả hệ thống (2 lần rẻ nhất: 6.901.220 đ) | P2 | ≤ 3 dòng, có số |
| B4: xem lại 100% = 11.743 đ (0,98×); với 15,3 phút làm lại = 12.414 đ (1,03×); hoà vốn ≤ 5,1 / 4,8 phút | P1 | ≤ 3 dòng, có số |
| Điền `bang_chi_phi.md` phần B | P4 | |

### Giải lao 15:20–15:35 — **đổi vai** (P1↔P2 cho code/kiểm số)

### CP3 · Nhiệm vụ C (15:35–16:08) — 10 điểm
1. **8 phút**: P3 và P4 ngồi tách nhau, gắn nhãn độc lập 20 ca (nguồn: `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`, mục "Hai mươi ca lỗi"). Nguyên tắc: nhãn theo **nguyên nhân gốc**. P1/P2 chốt nốt phần B còn dở.
2. **3 phút**: so nhãn, tính đồng thuận (cần ≥ 16/20). **Không sửa** hai bộ nhãn gốc sau khi so.
3. **5 phút**: ca không trùng → nhãn thống nhất + một câu quy tắc phân biệt. Dưới 80% → viết lại định nghĩa.
4. **14 phút**: chọn 5 ca, mỗi loại một ca. Mỗi dòng cần: cách phát hiện **đo được** (event, ngưỡng, tần suất) + **một vai trò** phụ trách (không ghi "cả đội"). Ghi vào `bang_loi.md` (P4 gõ, P3 soát).

### CP4 · Nhiệm vụ D (16:08–16:36) — 15 điểm
| Việc | Người | Đầu ra |
|---|---|---|
| D1: hàm `co_mau`, DE, cỡ mẫu hiệu dụng (thêm vào `lab13.py`) | P2 | a) 1.251 · b) 3.103/nhóm (84 người > 40) · c) tối đa 1.000 < 1.251 · d) tối đa 300 · e) m ≥ 299 (DE 6,96) |
| D2: 5 câu "tách được tác động" | P3 | Mỗi câu một dòng |
| Tính `mo_lai_trong_7_ngay` hiện tại | P2 | 4,25% (3,97% trong phạm vi) → luật an toàn so với đối chứng (+2 điểm) kèm trần 6% |
| Điền `pilot_plan.yaml` (bỏ hết dấu `?`): chia theo **staff 20+20**, MDE 6 điểm, n=859, DE 6,96, đủ `identifiability`, `simulated_inputs` | P3 | Ghi rõ đánh đổi: power ≈ 0,64 nếu tác động thật 5 điểm |
| ≥ 3 luật dừng đủ NẾU – TRONG – THÌ – KHÔNG THÌ (an toàn, chi phí, mức độ sử dụng) | P3 + P4 soát | Có người có quyền dừng, ngưỡng, thời hạn |

Kiểm: `python -c "import yaml; yaml.safe_load(open('../report/team/pilot_plan.yaml', encoding='utf-8'))"` và không còn `?` ngoài dòng chú thích.

### CP5 · Nhiệm vụ E (16:36–17:00) — 10 điểm
| Việc | Người | Đầu ra |
|---|---|---|
| E1: 3 chỉ số tính thử (chính 82,83% · bỏ qua gợi ý 27,12% (48/177) · an toàn 4,25%) + 1 chỉ số dùng và 1 chỉ số an toàn tự đề xuất | P2 (code) + P3 | `chi_so.md` |
| Danh sách ≥ 6 event có `trace_id`; kiểm chéo mỗi chỉ số tính được từ event nào | P4 | |
| E2: ≥ 2 dòng rủi ro kinh tế (làm lại gấp đôi +51,8%; xem lại 100% = 0,98×; chi phí cố định) | P1 | Lấy số từ bảng B |
| E3: `ho_so_launch_v0.md` một trang, 7 mục, mỗi mục có số chính + trạng thái (Xong, có bằng chứng · Chưa · Giả lập) + 1 vai trò | P4 | Mục 1, 2, 3, 7 là "Giả lập" |
| Đề xuất cuối: Go / Go có điều kiện / No-go. Gợi ý: **Go có điều kiện** cho pilot noi_dia + hang_nang (hoặc No-go nếu nhóm thấy số bất lợi nặng hơn); điều kiện có người phụ trách và ngày kiểm tra. Nêu rõ cả con số bất lợi (quoc_te 1,88×, xem lại 100% = 0,98–1,03×, power 0,64) | cả nhóm thống nhất | |

### 17:00–17:45 · Duyệt chéo Gate 2a
- 17:00 gửi hồ sơ cho nhóm n−1 (nhóm n chấm nhóm n+1). Nhóm hội đồng nhận hồ sơ nhóm khác.
- 17:10 P3+P4 đọc và chấm hồ sơ nhóm khác → `phieu_cham.md` (quyết định + lý do + 1 câu hỏi); P1+P2 luyện trả lời 3 câu hỏi gợi ý (xem lại 100%? ≥ 20 cụm? ngưỡng an toàn có dừng ngay tuần đầu?).
- 17:25 trình bày 1 phút, hội đồng công bố 1 phút, trả lời 1 phút. Người trình bày nên là P1 hoặc P2 (hiểu số), người trả lời về pilot là P3.

### 17:45–18:00 · Đóng gói
- [ ] P1: `cd src; python lab13.py` chạy hết, in bảng A2, A3, B, D1; ba phép thử ĐẠT; chạy thử trên máy người khác.
- [ ] Mỗi người copy `report/team/MSSV_HoTen.md` → `report/team/<MSSV>_<HoTenKhongDau>.md` (giữ file mẫu); ghi công cụ AI đã dùng và cách tự kiểm tra.
- [ ] P4: `TEAM.md`, `group_report.md` (mục 5 ghi khó khăn nếu có lỗi kỹ thuật).
- [ ] Kiểm tra lần cuối (PowerShell, chạy ở thư mục gốc):
  - `Select-String -Path report\team\* -Pattern 'production' -CaseSensitive:$false` → không có kết quả
  - Mọi số từ cột `_simulated` có nhãn `simulated`
  - Không "cả đội" ở cột người phụ trách; không commit `.venv/`, `.env`
- [ ] Commit và push (commit mới nếu sửa sau deadline). **Cả 4 người** nộp cùng link repo trên LMS trước 23h59 — ai không nộp thì không có điểm.

## 4. Các điểm dễ mất điểm (checklist chung)

1. Quên cộng giờ nhân viên (cps chỉ gấp 1–2× hoá đơn).
2. Chia cho 1.200 thay vì 978; quên chia 1.000 cho giá token.
3. Thiếu nhãn `simulated` (bị trừ điểm); dùng chữ "production".
4. Hai người gắn nhãn trao đổi trước khi so; sửa nhãn gốc sau khi so.
5. Chia pilot theo depot; ngưỡng dừng không dựa trên tỉ lệ mở lại hiện tại (4,25%); luật dừng thiếu vế KHÔNG THÌ.
6. Viết "trợ lý đã nâng chỉ số" (chưa có đối chứng) thay vì "chỉ số trong đợt chạy thử là…".
7. File hồ sơ sai tên hoặc nằm ngoài `report/team/`; không ghi mỗi mục một vai trò.

## 5. Phân bổ điểm → người chịu trách nhiệm chính

| Tiêu chí | Điểm | Chính | Soát lại |
|---|---:|---|---|
| A (mô hình chi phí) | 20 | P1 | P2 |
| B (độ nhạy) | 15 | P1 | P2 |
| C (bảng lỗi) | 10 | P3, P4 | P1 |
| D (pilot plan) | 15 | P3 | P2 |
| E (chỉ số, hồ sơ) | 10 | P4 | P2 |
| Hội đồng (đề xuất, nhãn simulated, pilot) | 30 | cả nhóm, P4 tổng hợp | P1 |

---

## 6. Kế hoạch chi tiết từng người (input · output · bàn giao)

Quy ước: **Input** = thứ người đó cần có trước khi bắt đầu (và lấy từ ai); **Output** = file/số người đó phải giao; **Giao cho** = người nhận. "Xong khi" là điều kiện tự kiểm tra.

### 6.0 Sơ đồ phụ thuộc (ai cần số của ai)

| Số/sản phẩm | Do ai tạo | Ai dùng | Dùng vào đâu |
|---|---|---|---|
| `mo_hinh()` chạy đúng + A1 ĐẠT | P1 (CP1) | P2, P3, P4 | Mọi số A, B, E2, hồ sơ |
| cps 4.472 đ; 16,3×; 0,49× | P1 → P2 kiểm | P4 | `bang_chi_phi.md`, hồ sơ mục 1, 3 |
| Bảng A3 theo loại (quoc_te 1,88×, doi_tac 0,85×) | P1 | P3, P4 | `scope` trong yaml; mục 6 hồ sơ |
| B1–B4 (xếp hạng, 0,98×/1,03×, giới hạn 2 lần) | P1 (code), P2 (kiểm) | P4, P1 | Hồ sơ mục 2, E2 rủi ro, stop-rule chi phí |
| Cỡ mẫu D1 (859, DE 6,96, 20 cụm) | P2 (code, sau đổi vai) | P3 | `pilot_plan.yaml` |
| Tỉ lệ mở lại 4,25% / 3,97% | P2 | P3 | Ngưỡng stop-rule an toàn |
| 3 chỉ số tính thử (82,83% · 27,12% · 4,25%) | P2 | P4 | `chi_so.md`, hồ sơ mục 4 |
| Nhãn thống nhất + bảng 5 ca | P3 + P4 | P1 (soát), P4 | `bang_loi.md`, hồ sơ mục 5 |
| 5 ca khắc phục (vai trò, event) | P3 + P4 | P4 | Danh sách event trong `chi_so.md` (phải có event để phát hiện) |

Đường găng: **A1 ĐẠT → mo_hinh → B → (E2, hồ sơ)**. P3 và P4 không bị chặn bởi code trong CP3, nhưng D cần số của A3 (scope) và B4 (stop-rule), nên P1 phải đẩy kết quả bảng lên kênh chung ngay khi xong, không chờ cuối checkpoint.

### 6.1 P1 — Người viết code (trước giải lao) → Kiểm số (sau giải lao)

**Input cần có**
- `src/logix_runs.csv`, `src/logix_requests.csv` (đọc `keep_default_na=False` cho requests); bảng giá cố định ở đầu `lab13.py`.
- Công thức A1 và quy tắc "tử số mọi lần chạy, mẫu số chỉ `thanh_cong`" (từ hướng dẫn chi tiết, mục A).
- Từ P2: đối chiếu tay các khoản 245.585 / 84.000 / 1.780.000 / 2.264.000.

**Việc và output**
| # | Việc | Output | Giao cho | Xong khi |
|---|---|---|---|---|
| 1 | 3 hàm A1 | `kiem_tra_dap_an_biet_truoc()` in ĐẠT | cả nhóm (chặn mọi việc sau) | in đúng "Ba phép thử đáp án biết trước: ĐẠT" |
| 2 | `mo_hinh(runs, reqs, ...)` | dict: token, tool, chay_lai, xem_lai, lam_lai, tong, thanh_cong, cps, hoa_don_moi_yc | P2, P4 | cps ≈ 4.472, tổng 4.373.585, 978, 274,7 (±2%) |
| 3 | Vòng lặp A3 + pivot ok theo attempt | In 4 dòng theo `loai`; bảng tỉ lệ ok theo lần thử | P4 (điền md), P3 (scope) | 2.696 / 8.221 / 22.515 / 10.215 |
| 4 | B1 (9 kịch bản), B2, B3, B4 trong `__main__` | Bảng in ra console, 9 dòng B1 + 3 dòng B3 + 2 số B4 | P4, P2 | "giảm nửa" = nửa mức "gấp đôi" |
| 5 | Bàn giao `lab13.py` cho P2 lúc 15:20 | Commit + push, báo "đã push" vào kênh nhóm | P2 | P2 chạy được trên máy mình |
| 6 | (Sau giải lao) Kiểm số: tự tính tay ≥ 1 số của D1 hoặc E1 | Ghi chú cách tính | P2 | khớp ≤ 2% với code |
| 7 | E2: ≥ 2 dòng rủi ro kinh tế | Bảng trong `chi_so.md` (rủi ro · tác động đã tính · dấu hiệu · hành động · vai trò) | P4 | số lấy từ B, có nhãn simulated |
| 8 | 17:45 chạy thử toàn bộ `lab13.py` trên máy khác | Ảnh/ghi chú output | P4 (group_report) | chạy hết, không `NotImplementedError` |

**Tệp sở hữu:** `src/lab13.py` (phần A, B). **Không** sửa 2 file CSV.
**Báo cáo cá nhân:** ghi AI đã dùng cho code và cách tự kiểm (so với đáp án A1, so tay).

### 6.2 P2 — Người kiểm số (trước giải lao) → Người viết code (sau giải lao)

**Input cần có**
- Từ P1: `lab13.py` chạy được (từ 14:25 cho A, từ 15:00 cho B); kết quả A2, B1.
- Số giả định chung (giá token, 2.000 đ/phút, 12.000 đ/yêu cầu, cố định 40 triệu).
- Sau giải lao: `lab13.py` do P1 push; công thức D1 (hàm `co_mau`, DE = 1 + (m−1)·ICC).

**Việc và output**
| # | Việc | Output | Giao cho | Xong khi |
|---|---|---|---|---|
| 1 | Kiểm tay A2: tổng = 245.585 + 84.000 + 1.780.000 + 2.264.000 | Dòng "kiểm tay" trong `bang_chi_phi.md`/báo cáo cá nhân | P1, P4 | 4.373.585 |
| 2 | A4 chi phí cố định (45.000×900/1.200 = 33.750 việc/tháng) | 1.185 đ/việc; 4.599 đ (0,38×); kịch bản nửa khối lượng 5.784 đ (0,48×) | P4 | số đúng ±2%, ghi "simulated" |
| 3 | So với 12.000 đ ở cấp hệ thống | 5.865 đ/yêu cầu = 0,49× (đã cộng 222 ca × 12.000) | P4 (mục 3 hồ sơ) | không có "0,37×" |
| 4 | B3: chi phí cả hệ thống 1/2/3 lần | 7.449.781 / **6.901.220** / 7.037.585; câu trả lời ≤ 3 dòng | P4 | nêu giới hạn 2 lần rẻ nhất cho công ty, khác giới hạn tối ưu cps (1 lần) |
| 5 | Nhận code, thêm D1 vào `lab13.py`: `co_mau(p1,p2)`, DE, n hiệu dụng | In 5 dòng a–e: 1.251 · 3.103 · 1.000 · 300 · m≥299 | P3 | khớp bảng đối chiếu; thêm `proportion_effectsize`/`NormalIndPower` để tính power 0,64 |
| 6 | Tỉ lệ mở lại hiện tại | 4,25% (51/1.200); 3,97% trong noi_dia + hang_nang | P3 | in ra trước khi P3 chốt stop-rule an toàn |
| 7 | E1 code: chỉ số chính / bỏ qua gợi ý / an toàn | 82,83% (994/1.200) · 27,12% (48/177) · 4,25% (51/1.200) | P4 (`chi_so.md`), P3 | dùng `keep_default_na=False` |
| 8 | Soát điểm A, B, D, E trước khi đóng gói | Danh sách lỗi (nếu có) | P1/P3/P4 | mỗi số simulated có nhãn |

**Tệp sở hữu:** `src/lab13.py` (phần D1, E1, sau giải lao). Một người sửa tại một thời điểm; P1 và P2 không cùng sửa file — dùng nhánh/commit ngắn, `git pull` trước khi sửa.
**Báo cáo cá nhân:** nêu đã tự tay tính được con số nào và khớp ra sao.

### 6.3 P3 — Gắn nhãn 1 (+ lead pilot plan)

**Input cần có**
- Trước 15:35: đọc đề `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` (mục "Hai mươi ca lỗi"), **không** đọc bảng nhãn tham khảo. Năm loại PAIR và 5 câu hỏi nhận biết (hướng dẫn mục C).
- Từ P1: A3 (loại nào đáng đưa vào pilot), B4 (xem lại 100%) cho scope và stop-rule.
- Từ P2: 5 con số D1, tỉ lệ mở lại 4,25%/3,97%.
- Từ P4: nhãn P4 chỉ nhận **sau** khi P3 nộp nhãn của mình.

**Việc và output**
| # | Việc | Output | Giao cho | Xong khi |
|---|---|---|---|---|
| 1 | CP1–CP2: theo dõi "Xong khi", hỗ trợ B2 (xếp hạng 3 yếu tố) | Dòng xếp hạng: làm lại > xem lại > lương | P4 | khớp B1 |
| 2 | 15:35–15:43 gắn nhãn 20 ca độc lập (ngồi tách P4) | Bộ nhãn 1 (cột "Nhãn người 1") — nộp cho P4 sau khi xong, không sửa nữa | P4 | đủ 20 dòng, nhãn theo nguyên nhân gốc |
| 3 | So nhãn, ghi quy tắc cho ca không trùng | Cột "Trùng?" + 1 câu quy tắc/ca | P4 | đồng thuận ≥ 16/20 (nếu < 80% thì viết lại định nghĩa) |
| 4 | Soát bảng khắc phục 5 ca | Nhận xét cho P4 | P4 | mỗi dòng có event + ngưỡng + tần suất + 1 vai trò |
| 5 | D2: 5 câu "tách được tác động" | Chú thích đầu `pilot_plan.yaml` | P4, P2 | mỗi câu một dòng, có số |
| 6 | Điền `pilot_plan.yaml`: owner, scope, assignment=staff, rollout, primary_metric (mde 0,06, n_per_arm 859, DE 6,96, clusters 20), identifiability, rollback, decision_date, simulated_inputs | File đọc được bằng `yaml.safe_load` | P4, P2 (soát) | không còn `?` ngoài chú thích |
| 7 | Viết ≥ 3 luật dừng NẾU–TRONG–THÌ–KHÔNG THÌ (an toàn / chi phí / sử dụng) | Mục `stop_rules` | P4 | mỗi luật có ngưỡng, thời hạn, **một** vai trò có quyền dừng, vế KHÔNG THÌ |
| 8 | Ghi đánh đổi: mức chênh 6 điểm, power ≈ 0,64 nếu thật 5 điểm | Dòng "Đánh đổi" trong chú thích yaml | P4 (đưa vào hồ sơ mục 6, điều kiện Go) | có con số |
| 9 | Phiếu chấm duyệt chéo (cùng P4) | Phần "Quyết định + lý do + 1 câu hỏi" | P4 | khớp bằng chứng của nhóm kia |

**Tệp sở hữu:** `report/team/pilot_plan.yaml`; cột "Nhãn người 1" trong `bang_loi.md`.
**Lưu ý:** mở file YAML bằng UTF-8 (`encoding='utf-8'`) vì có tiếng Việt, kiểm bằng lệnh trong mục CP4.

### 6.4 P4 — Gắn nhãn 2 + giữ hồ sơ

**Input cần có**
- Bắt đầu 14:00: mẫu `ho_so_launch_v0.md`, `TEAM.md`, `bang_chi_phi.md`; 7 mục hồ sơ (chi phí, 3 yếu tố nhạy nhất, so nhân viên, chỉ số, bảng lỗi, pilot plan, rủi ro).
- Từ P1/P2: số A2, A3, A4, B1–B4 (dán vào khi nhận, đánh dấu simulated); số E1.
- Từ P3: yaml, đánh đổi power 0,64, danh sách stop-rule; nhãn người 1 (sau khi P4 nộp xong nhãn của mình).
- Bảng khắc phục 5 ca cần ít nhất 6 event có `trace_id` để phát hiện lỗi (event list viết sau CP3).

**Việc và output**
| # | Việc | Output | Giao cho | Xong khi |
|---|---|---|---|---|
| 1 | 14:00 `TEAM.md`: tên nhóm, thành viên, vai | `TEAM.md` | cả nhóm | đủ 4 dòng |
| 2 | CP1: điền `bang_chi_phi.md` A2 (9 dòng) + A3 (4 dòng) | Bảng có cột nhãn (đo từ trace / simulated) | P2 (kiểm), chấm điểm | 9 + 4 dòng, khớp ±2% |
| 3 | CP2: điền bảng B1 (9 dòng), B2, B3, B4 | `bang_chi_phi.md` hoàn chỉnh | chấm điểm | ≤ 3 dòng/câu, có số |
| 4 | Hồ sơ mục 1, 2, 3 điền dần từ CP1–CP2 | Nháp `ho_so_launch_v0.md` | P1/P2 soát | trạng thái "Giả lập" |
| 5 | 15:35 gắn nhãn 20 ca độc lập (ngồi tách P3) | Cột "Nhãn người 2" | P3 | không trao đổi trước khi so |
| 6 | Sau khi so nhãn: điền cột "Trùng?", "Nhãn thống nhất", quy tắc, tỉ lệ đồng thuận | `bang_loi.md` phần 1–2 | P3 | ≥ 16/20 |
| 7 | Bảng khắc phục 5 ca (mỗi loại một ca), P3 soát | `bang_loi.md` phần 3 | P1 | cách phát hiện đo được, một vai trò |
| 8 | `chi_so.md`: đặc tả 3 chỉ số + 2 chỉ số tự đề xuất, danh sách ≥ 6 event (`trace_id`), kiểm chéo chỉ số ↔ event, rủi ro (từ P1) | `chi_so.md` | P3, P1 | mỗi chỉ số tính được từ event đã liệt kê |
| 9 | `ho_so_launch_v0.md` hoàn chỉnh: 7 mục (số chính, trạng thái, một vai trò) + dòng đề xuất | 1 trang | gửi nhóm hội đồng 17:00 | đúng tên, không "production"; mục 1, 2, 3, 7 là "Giả lập" |
| 10 | Chốt đề xuất cả nhóm: Go / Go có điều kiện / No-go, nêu số bất lợi (quoc_te 1,88×, xem lại 100% = 0,98–1,03×, power 0,64) | Dòng cuối hồ sơ | cả nhóm ký duyệt | mỗi điều kiện có vai trò + ngày kiểm tra |
| 11 | 17:10 `phieu_cham.md`: chấm nhóm khác (cùng P3) | Phiếu | nhóm được chấm | quyết định + lý do + 1 câu hỏi |
| 12 | 17:45 `group_report.md` + nhắc cả nhóm làm báo cáo cá nhân và nộp LMS | Báo cáo nhóm | — | đủ mục, có phần khó khăn nếu có |

**Tệp sở hữu:** `TEAM.md`, `bang_chi_phi.md`, `bang_loi.md` (cột P4 + ghép), `chi_so.md`, `ho_so_launch_v0.md`, `phieu_cham.md`, `group_report.md`.
**Rủi ro:** P4 là điểm nghẽn về văn bản. Giảm tải: P1 viết sẵn bảng markdown từ output code (xuất bằng `to_markdown()` hoặc copy console), P4 chỉ ghép nhãn và diễn giải.

### 6.5 Quy tắc phối hợp chung

- **Kênh nhóm:** mỗi khi xong một bảng, gửi "CPx xong, số chính = …" kèm commit hash; người nhận kiểm ±2% rồi mới dùng.
- **Git:** chỉ một người sửa mỗi file tại một thời điểm (xem "Tệp sở hữu"). `git pull --rebase` trước khi push; commit nhỏ sau mỗi checkpoint; không force-push.
- **Khoá nhãn:** P3 và P4 nộp bộ nhãn riêng (ảnh chụp hoặc commit riêng) *trước* khi nhìn nhau; sau khi so, không sửa cột nhãn gốc.
- **Mọi số simulated:** ghi `[simulated]` ngay khi dán vào hồ sơ, không để lúc cuối.
- **Đề xuất cuối:** thảo luận 3 phút lúc 16:50, người phản biện là P2 (thử bẻ bằng số bất lợi) trước khi P4 chốt chữ.
