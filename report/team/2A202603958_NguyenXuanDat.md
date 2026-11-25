# Báo cáo cá nhân — NguyenXuanDat-2A202603958

## 1. Thông tin thành viên

- Họ tên: Nguyễn Xuân Đạt
- MSSV: 2A202603958
- Email: xuandat31804@gmail.com
- Vai trong nhóm: Người kiểm số (P2), chuyển sang người viết code cho phần D1 (`src/lab13.py`)

## 2. Phần việc phụ trách

- **Kiểm chứng số liệu (CP1–CP2):** Kiểm tra độc lập các con số từ hai file CSV gốc (`logix_runs.csv`, `logix_requests.csv`) và đối chiếu output của P1 (A1–A4, B1–B4) đảm bảo sai số dưới 2%.
- **Điền bảng chi phí và độ nhạy (CP1–CP2):** Hoàn thiện toàn bộ `report/team/bang_chi_phi.md` (A1–A4, B1–B4), đảm bảo gắn nhãn `simulated` cho mọi con số giả lập và tuân thủ quy tắc trình bày.
- **Viết code cỡ mẫu D1 và tỉ lệ mở lại (CP4):** Tiếp nhận `src/lab13.py` từ P1, triển khai hàm tính cỡ mẫu cho 5 câu D1 (a–e), tính power đánh đổi (bonus) và tỉ lệ `mo_lai_trong_7_ngay` để bàn giao cho P3 và P4.
- **Phối hợp duyệt chéo Gate 2a (CP5):** Cung cấp số liệu chi phí/độ nhạy (A–B) và cỡ mẫu (D1) làm đầu vào cho mục E2 trong `chi_so.md`, `pilot_plan.yaml`, `ho_so_launch_v0.md`, và tham gia duyệt chéo hồ sơ cùng nhóm.

## 3. Đóng góp cụ thể

- Cài đặt môi trường Python (`.venv`, `pandas`, `numpy`, `scipy`, `statsmodels`, `pyyaml`), kéo code của P1 và kiểm chứng độc lập trên dữ liệu gốc: xác nhận 1.624 lần chạy, 1.200 yêu cầu, 978 việc thành công, 5.600 lần gọi tool (`84.000 đ`), chi phí mỗi việc thành công `4.472 đ` (`simulated`, gấp 16,3 lần hoá đơn token + tool chia số yêu cầu `274,7 đ`), lệch 0% so với kết quả của P1.
- Hoàn thiện đầy đủ 9 dòng bảng A2, 4 dòng bảng A3, 2 dòng bảng A4, 9 kịch bản B1, phân tích B2–B4 trong `report/team/bang_chi_phi.md`, kiểm tra không còn dấu `...`, đủ nhãn `simulated` và không dùng từ cấm.
- Viết phần D1 trong `src/lab13.py` tính cỡ mẫu theo cả công thức `NormalDist` và `statsmodels`: a) `1.251` yc/nhóm (`statsmodels`: `1.250`); b) `DE = 2,48`, `3.103` yc/nhóm (cần 84 > 40 nhân viên); c) 20 nhân viên/nhóm tối đa `1.000`; d) 6 depot/nhóm tối đa `300`; e) mức chênh 6 điểm (`859`/nhóm) cần `m ≥ 299` yc/người (`DE = 6,96`); bonus power khi tác động thật 5 điểm là `0,64`.
- Tính tỉ lệ `mo_lai_trong_7_ngay` hiện tại: `4,25%` toàn mẫu (`51/1.200`) và `3,97%` phạm vi `noi_dia + hang_nang` (`39/982`), gửi bàn giao kịp thời cho P3 thiết lập ngưỡng dừng an toàn trong `pilot_plan.yaml` và cho P4 hoàn thiện các mục 1, 2, 3, 7 của `ho_so_launch_v0.md`.

## 4. Bằng chứng

- **Commit & PR:** `ebc27b4` (`feat(p2): fill bang_chi_phi.md (A-B) and add D1 sample size in lab13.py`) trên nhánh `feat/p2-kiem-so`, đã merge vào `main` tại PR #1 (`f43294c`).
- **File đóng góp chính:**
  - `report/team/bang_chi_phi.md`: hoàn thiện toàn bộ bảng và câu trả lời A1–A4, B1–B4.
  - `src/lab13.py`: thêm phần D1 (5 câu cỡ mẫu a–e, bonus power `0,64`) và 2 tỉ lệ `mo_lai_trong_7_ngay`; chạy đạt 3 phép thử A1 (`1,20 · 1,25 · 1,25`) và in đầy đủ bảng A–D1.

## 5. Công cụ AI đã dùng

- **Công cụ:** Antigravity (trợ lý AI tích hợp trong IDE).
- **Mục đích sử dụng:** Tóm tắt yêu cầu lab, hỗ trợ cài môi trường và soát lỗi code/quy tắc nộp bài, gợi ý cấu trúc hàm tính cỡ mẫu D1 (`NormalDist`, `NormalIndPower`) và kiểm tra định dạng bảng trong `bang_chi_phi.md`.
- **Cách tự kiểm tra:** Tự chạy trực tiếp `src/lab13.py` trong `.venv` trên máy cá nhân, đối chiếu độc lập số liệu thô trực tiếp từ `logix_runs.csv` và `logix_requests.csv` (`thanh_cong = 978`, `tool_calls × 15 = 84.000 đ`), kiểm tra tính chất tuyến tính ở bảng độ nhạy B1/B2 (giảm một nửa bằng đúng 1/2 mức tăng gấp đôi), kiểm tra không còn ký tự `...` hay từ cấm trong file báo cáo, và đối chiếu kết quả cuối cùng với tài liệu hướng dẫn (lệch 0%).

## 6. Tự đánh giá

- **Điểm mạnh:** Hoàn thành sớm toàn bộ phần kiểm số, bảng chi phí A–B và code cỡ mẫu D1 trước giờ giải lao; bàn giao số liệu kịp thời để P3 và P4 làm song song không bị nghẽn.
- **Điểm cần lưu ý cuối buổi:** Tham gia duyệt chéo Gate 2a lúc 17:00 cùng nhóm và tự nộp link repo nhóm trên LMS đúng hạn.
