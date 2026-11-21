# Báo cáo cá nhân — NguyenTienCuong-2A202603425

## 1. Thông tin thành viên

- Họ tên: Nguyễn Tiến Cường
- MSSV: 2A202603425
- Email: cuongdelldz@gmail.com
- GitHub: cuong-sadboi
- Lớp: L3A · Nhóm: Neon
- Vai trong nhóm: Người viết code (14:00–15:20), Người kiểm số (từ 15:35) — Chủ file `src/lab13.py` đến giải lao và chủ file `report/team/pilot_plan.yaml`

## 2. Phần việc phụ trách

- **Chuẩn bị (14:00–14:10):** Cài đặt môi trường ảo `src/.venv`, cài đặt các thư viện trong `src/requirements.txt` và chạy thử `src/lab13.py`.
- **CP1 (14:10–14:53 · Nhiệm vụ A):** Viết 3 hàm A1 (`so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`), hàm `mo_hinh` (A2), tách theo `loai` (A3) và tính chi phí cố định cho phạm vi `noi_dia` + `hang_nang` (A4) trong `src/lab13.py`.
- **CP2 (14:53–15:20 · Nhiệm vụ B):** Triển khai 9 kịch bản đơn B1, kịch bản cặp và xếp hạng B2, chi phí cả hệ thống cho giới hạn 1/2/3 lần chạy B3, kịch bản xem lại 100% B4 trong `src/lab13.py`; commit và push trước giờ giải lao để bàn giao code cho Lập.
- **CP3–CP5 (từ 15:35 · đổi sang Người kiểm số & Chủ file `pilot_plan.yaml`):**
  - Soát `report/team/bang_chi_phi.md` (nhãn `simulated`, độ dài câu ≤ 3 dòng, đối chiếu số).
  - Tính tay đối chiếu công thức cỡ mẫu D1 (`DE`, `m` tối thiểu), soát `report/team/pilot_plan.yaml` (chọn cách chia, đánh đổi, `yaml.safe_load`, kiểm tra hết dấu `?`).
  - Đối chiếu danh sách event có `trace_id` và kiểm tra chéo các chỉ số E1 trong `report/team/chi_so.md`.
- **Đóng gói & duyệt chéo:** Chạy kiểm chứng lại toàn bộ `src/lab13.py` từ đầu đến cuối; rà soát quy tắc trình bày trước khi nộp.

## 3. Đóng góp cụ thể

**Chuẩn bị & CP1 · Nhiệm vụ A — Mô hình chi phí (`src/lab13.py`, commit `aa93465`):**

- Tạo môi trường ảo `src/.venv` (Python 3.15.2), cài đặt đủ `pandas`, `numpy`, `scipy`, `statsmodels`, `pyyaml` và đọc dữ liệu `logix_requests.csv` bằng `keep_default_na=False` để tránh biến ô rỗng của `quyet_dinh_xem_lai` thành `NaN`.
- **A1:** Viết 3 hàm xác suất chạy lại, vượt qua cả 3 phép thử đáp án biết trước (`1,20` · `1,25` · `1,25`) và in `Ba phép thử đáp án biết trước: ĐẠT`.
- **A2 (`mo_hinh`):** Tính chi phí token và tool trên **mọi** lần chạy kể cả lần lỗi (chia 1.000 trước khi nhân giá): token `245.585 đ`, tool `84.000 đ` (`5.600` lần), phần lần chạy 2–3 là `93.804 đ`; cộng phút xem lại (`890` phút = `1.780.000 đ`, `simulated`) và làm lại (`1.132` phút = `2.264.000 đ`, `simulated`) → tổng `4.373.585 đ` (`simulated`) cho `978` việc `thanh_cong`, ra **CPS = `4.472 đ`** (`simulated`), gấp **16,3×** hoá đơn token+tool/yêu cầu (`274,7 đ`). Bổ sung phép so sánh công bằng với baseline `12.000 đ` khi cộng `222` ca không thành công: `5.865 đ/yêu cầu = 0,49×` (`simulated`).
- **A3 (`in_bang_a3`):** Tính CPS theo 4 loại (`noi_dia` `2.696 đ = 0,22×`, `hang_nang` `8.221 đ = 0,69×`, `doi_tac` `10.215 đ = 0,85×`, `quoc_te` `22.515 đ = 1,88×`, `simulated`) kèm bảng tỉ lệ `status == 'ok'` theo `attempt` 1/2/3 (`quoc_te` tụt từ `30,0% → 11,4% → 2,2%`), chứng minh chạy lại không cứu được `quoc_te`.
- **A4 (`in_bang_a4`):** Tính chi phí cố định `40 triệu đ/tháng` cho phạm vi `noi_dia` + `hang_nang` (`900/1.200` = `75,0%`, biến đổi `3.414 đ`, `simulated`): ở `45.000` yc/tháng (`33.750` việc/tháng) cố định `1.185 đ` → tổng `4.599 đ = 0,38×`; ở một nửa khối lượng (`22.500` yc/tháng) cố định `2.370 đ` → tổng `5.784 đ = 0,48×` (`simulated`).

**CP2 · Nhiệm vụ B — Độ nhạy & Tối ưu hệ thống (`src/lab13.py`, commit `aa93465`):**

- **B1 (`in_bang_b1_b2`):** Chạy đủ 9 kịch bản thay đổi tham số và kiểm tra tính đối xứng giảm một nửa / gấp đôi (Token `+5,6% / −2,8%`, Xem lại `+40,7% / −20,3%`, Làm lại `+51,8% / −25,9%`, Lương NV +25% `+23,1%`, Max 2 `−5,2%`, Max 1 `−8,1%`, `simulated`).
- **B2:** Chạy kịch bản cặp (Token ×2 + Xem lại ×2) ra `6.543 đ (+46,3%)`, chênh `0,00 đ` so với tổng 2 tác động riêng, và xếp hạng top 3 yếu tố mạnh nhất: 1. Số ca làm lại (`+51,8%`), 2. Tỉ lệ xem lại (`+40,7%`), 3. Lương nhân viên (`+23,1%`) (`simulated`).
- **B3 (`in_bang_b3`):** Tính chi phí cả hệ thống (cộng `12.000 đ` mỗi ca không thành công) cho giới hạn 1/2/3 lần chạy: giới hạn **2 lần** rẻ nhất cho công ty (**`6.901.220 đ`**, `234` ca không thành công, CPS `4.237 đ`, `simulated`), khác với giới hạn 1 lần có CPS thấp nhất (`4.111 đ` nhưng tổng hệ thống lên `7.449.781 đ` do đẩy thêm `85` ca sang nhân viên).
- **B4 (`in_bang_b4`):** Tính kịch bản xem lại 100% trên phạm vi `noi_dia` + `hang_nang` (`948` YC có ≥1 lần `ok`, `48` ca làm lại, `900` thành công, `224.513 đ` token+tool) ở cả hai mức phút làm lại: `9,0` phút theo đề (`10.568.513 đ`, CPS `11.743 đ = 0,98×`, hoà vốn ≤ `5,1` phút xem lại) và `15,3` phút trung bình thực tế từ dữ liệu (`11.173.054 đ`, CPS `12.415 đ = 1,03×`, hoà vốn ≤ `4,8` phút xem lại, `simulated`).

**CP3–CP5 · Kiểm số, soát `pilot_plan.yaml` & `chi_so.md`:**

- Đối chiếu `report/team/bang_chi_phi.md` với đầu ra `src/lab13.py`: mọi con số A1–A4, B1–B4 khớp với độ lệch `0%` (ngưỡng cho phép `2%`), đủ nhãn `simulated`, câu trả lời ≤ 3 dòng.
- Chạy kiểm chứng lại toàn bộ `src/lab13.py` sau khi Lập cập nhật phần CP4–CP5 (các hàm `co_mau`, `he_so_thiet_ke`, `m_toi_thieu`, `in_bang_d1`, `in_ti_le_mo_lai`, `in_bang_e1`); tính tay kiểm chứng công thức thiết kế cụm `DE = 1 + (m − 1) × ICC` và điều kiện `20m / (0,98 + 0,02m) ≥ 859 ⇒ m ≥ 299` (`DE = 6,96`).
- Soát bản nháp `report/team/pilot_plan.yaml`: kiểm tra cách chia `staff` 20 + 20 (tách được tác động, ≥ 20 cụm/nhóm), nêu rõ con số bất lợi (power `0,64` ở mức chênh 5 điểm), chạy `yaml.safe_load` với `PYTHONUTF8=1` đọc hợp lệ đủ 11 trường, kiểm tra không còn dấu `?` ngoài phần chú thích và 3 luật dừng đủ 4 vế NẾU – TRONG – THÌ – KHÔNG THÌ.
- Đối chiếu bảng 11 event có `trace_id` và phần kiểm tra chéo với các chỉ số E1 trong `report/team/chi_so.md`.

## 4. Bằng chứng

- Commit code CP1–CP2 trên `main`: `aa93465` (`feat(lab13): implement CP1 (A1-A4) and CP2 (B1-B4) in src/lab13.py`).
- File code: [src/lab13.py](../../src/lab13.py) (chạy lại bản cuối sau `git pull` bằng `src/.venv/Scripts/python.exe lab13.py` in đủ từ A1 đến E1, ba phép thử A1 `ĐẠT`).
- File kế hoạch pilot được giao chủ file: [report/team/pilot_plan.yaml](pilot_plan.yaml) (đọc hợp lệ bằng `yaml.safe_load`, không còn `?` ngoài chú thích).
- File đối chiếu số và event: [report/team/bang_chi_phi.md](bang_chi_phi.md), [report/team/chi_so.md](chi_so.md).

## 5. Công cụ AI đã dùng

- **Antigravity:** Dùng để tóm tắt yêu cầu các checkpoint, hỗ trợ cài đặt môi trường `src/.venv`, viết và kiểm thử các hàm CP1 (A1–A4) và CP2 (B1–B4) trong `src/lab13.py`, rà soát quy tắc trình bày và soạn báo cáo cá nhân này.
- **Cách tự kiểm tra:**
  - Chạy `src/lab13.py` xác nhận ba phép thử A1 đều `ĐẠT` (`1,20 · 1,25 · 1,25`) và đối chiếu toàn bộ số A2–A4, B1–B4 khớp bảng đối chiếu trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` với độ lệch `0%`.
  - Kiểm tra đọc `logix_requests.csv` bắt buộc có `keep_default_na=False`; kiểm tra tuyến tính B1 (mức giảm một nửa bằng đúng 1/2 mức tăng gấp đôi) và B2 (`6.543 đ` khớp tổng 2 tác động riêng, chênh `0,00 đ`).
  - Tính tay kiểm chứng D1 câu e (`2,82m ≥ 841,82 ⇒ m ≥ 299`, `DE = 1 + 298 × 0,02 = 6,96`) và chạy `yaml.safe_load` với `PYTHONUTF8=1` cùng bộ lọc dấu `?` ngoài dòng `#` cho `report/team/pilot_plan.yaml`.
  - Rà soát nhãn `simulated` cho mọi con số từ cột `*_simulated` và chạy lệnh tìm từ cấm theo Quy tắc 5 trong `report/team/` xác nhận không có vi phạm.

## 6. Tự đánh giá

- **Làm tốt:** Hoàn thành đúng hạn phần code nền CP1–CP2 trước giải lao (không vướng lỗi bỏ lần chạy lỗi, quên chia 1.000 hay đọc thiếu `keep_default_na=False`) và kiểm chứng lại đầy đủ bản chạy cuối A1–E1 cùng `pilot_plan.yaml`.
- **Bài học rút ra:**
  - Chi phí thật của agent chủ yếu nằm ở **giờ nhân viên** (`92,5%` tổng chi phí, `simulated`), khiến CPS thật (`4.472 đ`) cao gấp `16,3×` hoá đơn token+tool (`274,7 đ`); tối ưu CPS đơn lẻ ở mức 1 lần chạy (`4.111 đ`) thực chất làm tăng tổng chi phí cả hệ thống vì đẩy `85` ca sang nhân viên.
  - Ở `noi_dia` + `hang_nang`, nếu duy trì xem lại 100% (`B4`) thì tổng chi phí chạm mức `0,98×–1,03×` nhân viên tự làm, nên pilot bắt buộc phải đo phút xem lại/làm lại thật sau tuần 1 và có lộ trình giảm tỉ lệ xem lại an toàn.
  - Khi thiết kế pilot với 40 nhân viên và `ICC = 0,02`, trần cỡ mẫu hiệu dụng `c / ICC = 1.000 < 1.251` buộc phải đánh đổi MDE lên 6 điểm (`m ≥ 299`, chấp nhận power `0,64` ở mức 5 điểm) thay vì chọn cách chia theo yêu cầu (tràn tác động) hay theo depot (`c = 6`, trần `300`).
