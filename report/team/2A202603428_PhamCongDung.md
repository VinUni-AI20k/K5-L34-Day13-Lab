# Báo cáo cá nhân — PhamCongDung-2A202603428

## 1. Thông tin thành viên

- Họ tên: Phạm Công Dũng
- MSSV: 2A202603428
- Lớp: L3A · Nhóm: Neon
- Vai trong nhóm: Người gắn nhãn 2, kiêm giữ hồ sơ (`report/team/ho_so_launch_v0.md`, `report/team/phieu_cham.md`)

## 2. Phần việc phụ trách

- **Chuẩn bị (14:00–14:10):** Mở `report/team/ho_so_launch_v0.md`, dựng khung 7 mục với các cột: Con số chính, Trạng thái, Người phụ trách.
- **CP1 (Nhiệm vụ A):** Viết 3 câu trả lời phân tích cho A2, A3, A4 (mỗi câu ≤ 3 dòng, có con số cụ thể và nhãn `simulated`) trong `report/team/bang_chi_phi.md`. Ghi Mục 1 (Chi phí mỗi việc thành công) và Mục 3 (So với nhân viên tự làm 12.000 đ) vào `report/team/ho_so_launch_v0.md`.
- **CP2 (Nhiệm vụ B):** Ghi Mục 2 (Ba yếu tố nhạy nhất) vào `report/team/ho_so_launch_v0.md`; soạn nháp các dòng rủi ro kinh tế từ bảng độ nhạy B1/B4 vào `report/team/chi_so.md` (mục E2).
- **CP3 (Nhiệm vụ C):** Gắn nhãn độc lập 20 ca lỗi theo 5 loại Google PAIR, đối chiếu đồng thuận với Huy, điền 2 dòng khắc phục (Giới hạn hệ thống, Ngầm) trong `report/team/bang_loi.md` và cập nhật Mục 5 hồ sơ.
- **CP4–CP5 (Nhiệm vụ D, E & Duyệt chéo):** Viết 3 luật dừng (NẾU – TRONG – THÌ – KHÔNG THÌ) vào `report/team/pilot_plan.yaml`, hoàn thiện đủ 7 mục + dòng đề xuất trong `report/team/ho_so_launch_v0.md`, kiểm tra không chứa từ cấm và tổng hợp `report/team/phieu_cham.md`.

## 3. Đóng góp cụ thể

**Tại CP1 (Nhiệm vụ A — Mô hình chi phí mỗi việc thành công):**

- **Viết câu trả lời A2 trong `report/team/bang_chi_phi.md`:**
  - Chỉ ra chi phí mỗi việc thành công là **4.472 đ** (`simulated`), gấp **16,3 lần** hoá đơn token + tool chia số yêu cầu (**274,7 đ**).
  - Xác định khoản chiếm tỉ trọng lớn nhất là **làm lại (51,8% = 2.264.000 đ)** và **xem lại (40,7% = 1.780.000 đ)**; tổng giờ nhân viên chiếm **92,5%** tổng chi phí (`simulated`).
  - Nêu phép so sánh công bằng với baseline 12.000 đ của nhân viên: khi cộng thêm 222 ca không thành công (`148 chuyen_nhan_vien + 74 lam_lai`) × 12.000 đ, chi phí cả hệ thống là **5.865 đ/yêu cầu = 0,49×** của 12.000 đ (`simulated`).
- **Viết câu trả lời A3 & A4 trong `report/team/bang_chi_phi.md`:**
  - Phân tích bảng tách theo loại yêu cầu: kết luận loại **`quoc_te`** không đáng để trợ lý xử lý vì tỉ lệ thành công chỉ **27,3%**, chi phí **22.515 đ = 1,88×** của 12.000 đ (`simulated`). Giải thích việc cho chạy lại tới 3 lần không giúp ích vì tỉ lệ `status == 'ok'` của `quoc_te` giảm mạnh qua từng lần thử (lần 1: **30,0%**, lần 2: **11,4%**, lần 3: **2,2%**) do lỗi lặp lại trên cùng yêu cầu. Đề xuất loại cả `quoc_te` và `doi_tac` (**10.215 đ = 0,85×**, có điều khoản riêng) khỏi phạm vi pilot.
  - Phân tích chi phí cố định 40 triệu đ/tháng trên phạm vi `noi_dia` + `hang_nang` (biến đổi **3.414 đ/việc**, 900/1.200 việc thành công): ở quy mô 45.000 yêu cầu/tháng (33.750 việc thành công), cố định là **1.185 đ/việc** → tổng **4.599 đ = 0,38×** (`simulated`); ở một nửa khối lượng (22.500 yêu cầu/tháng), cố định tăng gấp đôi lên **2.370 đ/việc** → tổng **5.784 đ = 0,48×** (`simulated`).
- **Cập nhật `report/team/ho_so_launch_v0.md` (Mục 1, Mục 3):**
  - Điền Mục 1 (Chi phí mỗi việc thành công: 4.472 đ toàn mẫu; 3.414 đ biến đổi và 4.599 đ có cố định cho phạm vi pilot, trạng thái `Giả lập`, phụ trách: `PM trợ lý hoàn phí`).
  - Điền Mục 3 (So với nhân viên tự làm 12.000 đ: cả hệ thống 5.865 đ = 0,49×; thu hẹp phạm vi pilot về `noi_dia` 0,22× và `hang_nang` 0,69×, trạng thái `Giả lập`, phụ trách: `Giám đốc vận hành LogiX-VN`).

**Tại CP2 (Nhiệm vụ B — Bảng độ nhạy & Nháp rủi ro kinh tế):**

- **Ghi Mục 2 (Ba yếu tố nhạy nhất) vào `report/team/ho_so_launch_v0.md`:**
  - Tổng hợp từ bảng độ nhạy B1 & B2: Xếp hạng 3 yếu tố làm chi phí mỗi việc thành công thay đổi mạnh nhất là **1. Số ca làm lại** (gấp đôi → **6.787 đ, +51,8%**, giảm một nửa → **3.315 đ, −25,9%** `simulated`) · **2. Tỉ lệ xem lại** (gấp đôi → **6.292 đ, +40,7%**, giảm một nửa → **3.562 đ, −20,3%** `simulated`) · **3. Lương nhân viên** (tăng 25% → **5.506 đ, +23,1%** `simulated`).
  - Đối chiếu kịch bản đổi cặp B2 (Giá token ×2 + Tỉ lệ xem lại ×2 → **6.543 đ, +46,3%** `simulated`, bằng đúng tổng hai tác động riêng `+5,6% + 40,7%` do mô hình cộng tuyến tính) và kịch bản giới hạn chạy lại B3 (giới hạn **2 lần chạy** giúp tổng chi phí cả hệ thống rẻ nhất cho công ty ở mức **6.901.220 đ** `simulated`, tiết kiệm 136.365 đ so với 3 lần và 548.561 đ so với 1 lần).
  - Gán trạng thái `Giả lập` và người phụ trách là `PM trợ lý hoàn phí`.
- **Soạn nháp bảng Rủi ro kinh tế (cho mục E2) trong `report/team/chi_so.md` từ số liệu bảng độ nhạy B1 & B4:**
  - **Rủi ro 1 (Số ca làm lại tăng gấp đôi):** Tác động làm chi phí mỗi việc thành công tăng **+51,8%** (từ 4.472 đ lên **6.787 đ**, `simulated`). Dấu hiệu theo dõi: tỉ lệ làm lại theo tuần > 7% (so với 4,9% trong đợt chạy thử ở phạm vi `noi_dia` + `hang_nang`). Hành động: thu hẹp pilot về `noi_dia` và rà soát 20 trace làm lại gần nhất. Phụ trách: `PM trợ lý hoàn phí`.
  - **Rủi ro 2 (Phải xem lại 100% kéo dài — từ kết quả B4):** Tác động làm chi phí trong phạm vi `noi_dia` + `hang_nang` tăng lên **11.743 đ = 0,98×** của 12.000 đ (hoặc **12.415 đ = 1,03×** nếu dùng phút làm lại thực tế 15,3 phút/ca trong dữ liệu, `simulated`), mất toàn bộ lợi thế tiết kiệm. Dấu hiệu theo dõi: % yêu cầu được xem lại vẫn > 50% cuối bước rollout 0,25 hoặc thời gian xem lại > 4,8 phút/ca. Hành động: giảm tỉ lệ xem lại theo bậc khi tỉ lệ `sua` + `bo` < 15%. Phụ trách: `Trưởng nhóm CSKH`.
  - **Rủi ro 3 (Khối lượng thấp hơn dự kiến — từ kết quả A4):** Chi phí cố định 40 triệu đ/tháng làm cộng thêm **+1.185 đ/việc** ở 45.000 yc/tháng (**4.599 đ = 0,38×**, `simulated`) và tăng gấp đôi lên **+2.370 đ/việc** khi khối lượng giảm một nửa (**5.784 đ = 0,48×**, `simulated`). Phụ trách: `PM trợ lý hoàn phí`.

## 4. Bằng chứng

- File hồ sơ tổng hợp: [report/team/ho_so_launch_v0.md](ho_so_launch_v0.md) (đã điền Mục 1, 2, 3 với đầy đủ con số, nhãn `simulated`, trạng thái `Giả lập` và vai trò phụ trách).
- File bảng chi phí: [report/team/bang_chi_phi.md](bang_chi_phi.md) (các câu trả lời phân tích ở mục A2, A3, A4 tuân thủ quy tắc ≤ 3 dòng, có số liệu và nhãn `simulated`).
- File chỉ số và rủi ro: [report/team/chi_so.md](chi_so.md) (bảng E2 Rủi ro kinh tế lấy số trực tiếp từ CP1 & CP2).
- Kết quả chạy kiểm tra `python lab13.py` trong `src/` khớp 100% với các con số đã ghi vào hồ sơ.

## 5. Công cụ AI đã dùng

- **Antigravity (Gemini)** trong IDE, dùng để giải thích yêu cầu từng checkpoint, kiểm tra chéo các phép tính tỷ trọng chi phí ở CP1 (A2, A3, A4), rà soát quy tắc trình bày (≤ 3 dòng/câu, gắn nhãn `simulated`, không dùng từ cấm) và hỗ trợ tổng hợp nội dung vào `ho_so_launch_v0.md` và báo cáo cá nhân.
- **Cách tự kiểm tra:**
  - Tự tính tay kiểm chứng lại các con số trong câu trả lời A2–A4:
    - Tỉ lệ CPS so với hoá đơn/yêu cầu: `4.472 / 274,7 = 16,28 ≈ 16,3 lần`.
    - Tỉ trọng làm lại và xem lại: `2.264.000 / 4.373.585 = 51,77% ≈ 51,8%`; `1.780.000 / 4.373.585 = 40,70% ≈ 40,7%`.
    - Chi phí cả hệ thống trên mỗi yêu cầu: `(4.373.585 + 222 × 12.000) / 1.200 = 7.037.585 / 1.200 = 5.864,65 ≈ 5.865 đ (0,49×)`.
    - Chi phí cố định mỗi việc ở phạm vi `noi_dia` + `hang_nang`: `40.000.000 / (45.000 × 900 / 1.200) = 40.000.000 / 33.750 = 1.185,18 ≈ 1.185 đ`; cộng CPS biến đổi `3.413,90 + 1.185,18 = 4.599 đ (0,38×)`.
  - Tự kiểm tra số liệu độ nhạy ở CP2 (B1, B2, B4):
    - Tính cộng tuyến tính B2: `(4.723 − 4.472) + (6.292 − 4.472) = 251 + 1.820 = 2.071 đ` → `4.472 + 2.071 = 6.543 đ (+46,3%)`, khớp với `+5,6% + 40,7% = +46,3%`.
    - Kịch bản xem lại 100% (B4) trên `noi_dia` + `hang_nang`: `948 ca có ≥1 lần ok × 5 phút × 2.000 đ = 9.480.000 đ`; `48 ca làm lại × 9 phút × 2.000 đ = 864.000 đ`; cộng token+tool `224.513 đ` = `10.568.513 đ / 900 việc = 11.743 đ (0,98×)`. Với trung bình thực tế `15,3125 phút/ca làm lại`: `(9.480.000 + 48 × 15,3125 × 2.000 + 224.513) / 900 = 11.174.513 / 900 = 12.416 đ ≈ 12.415 đ (1,03×)`.
  - Kiểm tra định dạng: xác nhận mọi con số có nguồn từ `phut_xem_lai_simulated` và `phut_lam_lai_simulated` đều đi kèm nhãn `simulated`, người phụ trách là một vai trò cụ thể.

## 6. Tự đánh giá

- Hoàn thành đúng và đầy đủ nhiệm vụ của vai **Người giữ hồ sơ** ở CP1 (và phần liên kết sang CP2/E2): các câu trả lời A2, A3, A4 ngắn gọn (≤ 3 dòng), đi thẳng vào bản chất kinh tế của agent; Mục 1, 2, 3 trong `ho_so_launch_v0.md` có số liệu chính xác, khớp 100% với `bang_chi_phi.md`.
- Bài học rút ra: Khi đánh giá kinh tế một AI Agent để trình duyệt Gate 2a, không được nhìn vào hoá đơn token chia đầu yêu cầu (274,7 đ) hay chỉ chia cho số ca thành công mà bỏ quên chi phí nhân viên xử lý các ca chuyển giao/làm lại. Ngoài ra, việc bóc tách chi phí theo từng phân khúc (`loai`) là bước quyết định giúp loại bỏ các phân khúc gây lỗ (`quoc_te` 1,88×) trước khi chạy pilot.
