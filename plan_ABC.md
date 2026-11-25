# Kế hoạch phân công Nhiệm vụ A, B, C (4 vai trò)

> Tài liệu điều phối nội bộ cho Nhiệm vụ A, B, C (chưa thực hiện D và E).  
> Lưu ý: Không thay đổi tên các file nộp bắt buộc trong `report/team/` theo quy định tại [SUBMISSION.md](SUBMISSION.md).

## 1. Bảng phân công nhanh

| Vai trò | Thành viên phụ trách | Nhiệm vụ | File làm việc chính | Điểm Rubric liên quan |
| --- | --- | --- | --- | --- |
| **Vai trò 1: Người viết code** | *(Điền tên)* | A, B | `src/lab13.py` | C1 (20đ), C2 (15đ) |
| **Vai trò 2: Người kiểm số** | Nguyễn Tuấn Dũng (`2A202603859`) | A, B | `report/team/bang_chi_phi.md` | C1 (20đ), C2 (15đ) |
| **Vai trò 3: Người gắn nhãn 1** | *(Điền tên)* | C | `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`, `report/team/bang_loi.md` | C3 (10đ) |
| **Vai trò 4: Người gắn nhãn 2 (kiêm giữ hồ sơ)** | *(Điền tên)* | C | `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`, `report/team/bang_loi.md` | C3 (10đ) |

> **Gợi ý phối hợp:** Nhánh A+B (Vai trò 1 & 2) và Nhánh C (Vai trò 3 & 4) có thể chạy **song song ngay từ đầu** sau khi cả nhóm điền thông tin thành viên vào [TEAM.md](TEAM.md).

---

## 2. Chi tiết công việc từng vai trò

### Vai trò 1: Người viết code (Nhiệm vụ A & B)

**File phụ trách:** [src/lab13.py](src/lab13.py)  
**Không sửa:** `src/lab13_starter.py`, `src/logix_runs.csv`, `src/logix_requests.csv`.

- [ ] **Chuẩn bị môi trường (10 phút):**
  - Chạy lệnh trong thư mục `src/` theo [src/README.md](src/README.md): tạo `.venv`, cài `requirements.txt`, kiểm tra `python -c "import pandas, numpy, scipy, statsmodels; print('san sang')"`.
  - Đảm bảo đọc dữ liệu bằng `pd.read_csv('logix_requests.csv', keep_default_na=False)` (bắt buộc có `keep_default_na=False`).
- [ ] **Nhiệm vụ A1 (`TODO CP1`):**
  - Viết 3 hàm: `so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`.
  - Chạy `python3 lab13.py` phải in `Ba phép thử đáp án biết trước: ĐẠT` (`1,20 · 1,25 · 1,25`) mới được làm tiếp.
- [ ] **Nhiệm vụ A2 (`TODO CP1`):**
  - Viết hàm `mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000, he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None)`.
  - Tử số: token + tool trên **mọi** lần chạy (kể cả lần lỗi), tách riêng phần `attempt > 1`; cộng tiền xem lại (`phut_xem_lai_simulated`) và làm lại (`phut_lam_lai_simulated`).
  - Mẫu số: chỉ đếm yêu cầu có `ket_qua == 'thanh_cong'`.
- [ ] **Nhiệm vụ A3 (`TODO CP1`):**
  - Gọi `mo_hinh` cho từng giá trị cột `loai` (`noi_dia`, `hang_nang`, `quoc_te`, `doi_tac`).
  - Tính tỉ lệ `ok` theo từng `attempt` cho từng `loai` để kiểm tra chạy lại có giúp không.
- [ ] **Nhiệm vụ A4:**
  - Tính chi phí cố định (40 triệu đ/tháng) cho phạm vi `noi_dia` + `hang_nang` ở mức 45.000 yêu cầu/tháng và một nửa khối lượng.
- [ ] **Nhiệm vụ B1 (`TODO CP2`):**
  - Gọi `mo_hinh` cho 9 kịch bản đổi từng yếu tố (giá token ×2 / ÷2; xem lại ×2 / ÷2; làm lại ×2 / ÷2; lương +25%; tối đa 2 lần chạy; tối đa 1 lần chạy).
  - Với giới hạn chạy: bỏ `attempt > max_lan_chay`, các yêu cầu `so_lan_chay > max_lan_chay` coi là `chuyen_nhan_vien` và đặt phút simulated = `0`.
- [ ] **Nhiệm vụ B2, B3, B4 (`TODO CP2`):**
  - **B2:** Chạy kịch bản kết hợp `gia_vao=52, gia_ra=260, he_so_xem_lai=2` và xếp hạng 3 yếu tố ảnh hưởng mạnh nhất.
  - **B3:** Tính chi phí cả hệ thống (`tổng chi phí trợ lý + 12.000 đ × số yêu cầu không thành công`) cho giới hạn 1, 2, 3 lần.
  - **B4:** Lọc `noi_dia` + `hang_nang`, tính kịch bản xem lại 100% theo cả 2 mức phút làm lại (9 phút giả định và trung bình thực tế của cột `phut_lam_lai_simulated`), tìm mức phút xem lại hoà vốn.
- [ ] **Xong khi:** `cd src && python3 lab13.py` chạy hoàn chỉnh trên một máy khác trong nhóm, in ĐẠT ở A1 và đầy đủ số liệu cho A2–A4, B1–B4.

---

### Vai trò 2: Người kiểm số & Điền bảng (Nhiệm vụ A & B)

**File phụ trách:** [report/team/bang_chi_phi.md](report/team/bang_chi_phi.md)  
**Tài liệu đối chiếu:** [docs/du_lieu_va_cong_thuc.md](docs/du_lieu_va_cong_thuc.md)

- [ ] **Nắm công thức & đơn giá:** Đọc 6 công thức và bảng giả định đơn giá (26 đ/1k token vào, 130 đ/1k token ra, 15 đ/tool, 2.000 đ/phút nhân viên, baseline 12.000 đ/yêu cầu, cố định 40 triệu đ/tháng).
- [ ] **Tính tay đối chiếu:** Tự tính tay ít nhất 1–2 con số (kiểm tra công thức A1, tỉ số CPS / hoá đơn chia số yêu cầu ở A2, phép chia chi phí cố định ở A4) để phát hiện lỗi code như quên chia 1.000 token, chia nhầm 1.200 thay vì 978, hoặc thiếu giờ nhân viên.
- [ ] **Điền Phần A vào `bang_chi_phi.md`:**
  - Bảng **A1** (3 dòng).
  - Bảng **A2** (9 dòng + trả lời 2 câu hỏi).
  - Bảng **A3** (4 dòng + trả lời câu hỏi loại nào không đáng xử lý và chạy lại 3 lần có giúp không).
  - Bảng **A4** (2 dòng + trả lời chi phí cố định có đổi kết luận không).
- [ ] **Kiểm tra & điền Phần B vào `bang_chi_phi.md`:**
  - Bảng **B1** (9 dòng): kiểm tra tự động tính nhất quán (mỗi kịch bản "giảm một nửa" giảm đúng bằng nửa mức tăng của kịch bản "gấp đôi" tương ứng).
  - Mục **B2** (kịch bản cặp + xếp hạng 3 yếu tố mạnh nhất).
  - Bảng **B3** (3 dòng giới hạn 1, 2, 3 lần + trả lời câu hỏi giới hạn rẻ nhất cho công ty).
  - Mục **B4** (ghi đủ số liệu cả hai mức phút làm lại và mức hoà vốn + ý nghĩa cho pilot).
- [ ] **Rà soát quy tắc bắt buộc:**
  - Mọi số tính từ cột `_simulated` **phải có nhãn `simulated`**.
  - Mỗi câu trả lời **≤ 3 dòng** và **có ít nhất 1 con số**.
  - Không dùng từ `"production"`.
  - Đối chiếu số liệu không lệch quá 2% khi giảng viên chiếu slide chữa.

---

### Vai trò 3: Người gắn nhãn 1 (Nhiệm vụ C)

**File phụ trách:** `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` (mục *Hai mươi ca lỗi*) và [report/team/bang_loi.md](report/team/bang_loi.md)

- [ ] **Chuẩn bị:** Đọc kỹ định nghĩa 5 loại lỗi Google PAIR (**Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**) và quy tắc: **gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa**.
- [ ] **Gắn nhãn độc lập (8 phút):** Ngồi tách riêng khỏi Người gắn nhãn 2, tự gắn cả 20 ca vào ghi chú cá nhân. **Tuyệt đối không trao đổi** trước khi so và **không sửa bộ nhãn độc lập** sau khi đã so.
- [ ] **So nhãn & tính đồng thuận (3 phút):** Nhập bộ nhãn của mình vào cột `Nhãn người 1` trong `bang_loi.md`, cùng Người gắn nhãn 2 điền cột `Trùng?` và tính `tỉ lệ đồng thuận = số ca trùng ÷ 20`.
- [ ] **Thống nhất các ca lệch (5 phút):**
  - Thảo luận để chốt cột `Nhãn thống nhất`.
  - Viết **mỗi ca không trùng một câu quy tắc phân biệt** vào mục `Quy tắc phân biệt cho các ca không trùng`.
  - Nếu đồng thuận `< 80%` (dưới 16/20 ca), phải viết lại định nghĩa phân biệt trước khi đi tiếp.
- [ ] **Phối hợp lập bảng khắc phục 5 ca (14 phút):** Chọn 5 ca đại diện đủ 5 loại, cùng Người gắn nhãn 2 đề xuất `Phát hiện bằng gì` và `Khắc phục thế nào`.
- [ ] **Xong khi:** Đồng thuận ≥ 80% (và khớp đáp án ≥ 16/20 ca khi đối chiếu), hoàn chỉnh bảng 20 ca và quy tắc phân biệt.

---

### Vai trò 4: Người gắn nhãn 2 (kiêm giữ hồ sơ) (Nhiệm vụ C)

**File phụ trách:** `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` và [report/team/bang_loi.md](report/team/bang_loi.md)

- [ ] **Gắn nhãn độc lập (8 phút):** Ngồi tách riêng khỏi Người gắn nhãn 1, tự gắn cả 20 ca theo nguyên nhân gốc, không trao đổi.
- [ ] **So nhãn & hoàn thiện bảng 20 ca (8 phút):** Điền tên hai người gắn nhãn, cột `Nhãn người 2`, tính tỉ lệ đồng thuận, ghi nhãn thống nhất và quy tắc phân biệt cho các ca không trùng.
- [ ] **Hoàn thiện bảng khắc phục 5 ca (14 phút):** Chọn đủ 5 loại lỗi (mỗi loại 1 ca) và kiểm tra chặt tiêu chí Rubric C3:
  - Cột `Phát hiện bằng gì`: **phải đo được** (nêu rõ *event*, *ngưỡng*, *tần suất*).
  - Cột `Ai phụ trách`: **chỉ ghi một vai trò cụ thể** có quyền quyết định (ví dụ: *PM trợ lý hoàn phí*, *Kỹ sư trưởng agent*, *Trưởng nhóm CSKH*, *Kế toán trưởng*); **không ghi "cả đội"**.
- [ ] **Giữ hồ sơ (chuẩn bị cho D & E sau này):**
  - Ghi nhận các con số chốt từ `bang_chi_phi.md` (A, B) và kết quả từ `bang_loi.md` (C) để phục vụ điền `ho_so_launch_v0.md` ở bước sau.
  - Nhắc cả 4 thành viên lưu lại commit/bằng chứng cá nhân cho [TEAM.md](TEAM.md) và `report/team/MSSV_HoTen.md`.

---

## 3. Quy tắc chung cần nhớ (tránh mất điểm)

1. **Qua A1 trước:** Phải đạt cả 3 phép thử A1 (`1,20 · 1,25 · 1,25`) rồi mới tính tiếp.
2. **Nhãn `simulated`:** Mọi con số tính từ `phut_xem_lai_simulated` hoặc `phut_lam_lai_simulated` phải ghi nhãn `simulated`.
3. **Độ dài câu trả lời:** Trong `bang_chi_phi.md`, mỗi câu trả lời **không quá 3 dòng** và **có ít nhất 1 con số**.
4. **Cấm từ `"production"`:** Gate 2a chỉ duyệt kế hoạch pilot, không dùng từ `"production"` trong các file hồ sơ.
5. **Trung thực dữ liệu & gắn nhãn:** Hai người gắn nhãn độc lập trước khi so, không sửa bộ nhãn độc lập sau khi đối chiếu; không dùng AI bịa số liệu hay nhãn lỗi.
