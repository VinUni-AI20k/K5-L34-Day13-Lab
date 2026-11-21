# Báo cáo cá nhân — BuiLeCongTuan-2A202603610

## 1. Thông tin thành viên

- Họ tên: Bùi Lê Công Tuấn
- MSSV: 2A202603610
- Email: blct15102004@gmail.com
- Vai trong nhóm: Người gắn nhãn 2 · Viết `pilot_plan.yaml` (phần phụ, CP3–CP4) · Giữ hồ sơ + review cuối (CP5)

## 2. Phần việc phụ trách

- CP3: Gắn nhãn 20 ca lỗi (nhãn 2) và lập bảng khắc phục 5 ca trong `report/team/bang_loi.md`.
- CP4: Viết `src/lab13.py` phần CP4 (tính cỡ mẫu D1, D2) và điền `report/team/pilot_plan.yaml`.
- CP5: Điền `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md`; review toàn bộ hồ sơ trước khi nộp và điều phối Gate 2a (`phieu_cham.md`, `group_report.md`).

## 3. Đóng góp cụ thể

- **CP3 (`report/team/bang_loi.md`):** Gắn nhãn độc lập 20 ca lỗi vào cột `Nhãn người 2` theo 5 loại Google PAIR (`Do người dùng`, `Hệ thống`, `Ngữ cảnh`, `Giới hạn hệ thống`, `Ngầm`); xây dựng bảng khắc phục cho 5 ca đại diện (`9`, `7`, `18`, `4`, `17`) với cách phát hiện đo được (event, ngưỡng, tần suất) và vai trò phụ trách cụ thể.
- **CP4 (`src/lab13.py`, `report/team/pilot_plan.yaml`):**
  - Viết `co_mau_hai_ti_le` và `tinh_co_mau_cp4` tính đủ 5 câu D1 (`1.251` yc/nhóm theo yêu cầu; `3.103` yc/nhóm ở `m=75`, cần 42 người/nhóm; trần `1.000` với 20 nhân viên/nhóm; trần `300` với 6 depot/nhóm; MDE 6 điểm đạt `859` yc/nhóm với `m >= 299`, `DE = 6,96`) và tỉ lệ `mo_lai_trong_7_ngay` hiện tại (`4,25%` toàn bộ, `3,97%` trong phạm vi `noi_dia + hang_nang`).
  - Hoàn thiện `pilot_plan.yaml`: điền toàn bộ chú thích D1–D2, nêu rõ đánh đổi (`power` còn ~0,64 nếu tác động thật chỉ 5 điểm), không còn dấu `?` ngoài comment, đủ 3 luật dừng 4 vế `NẾU – TRONG – THÌ – KHÔNG THÌ`.
- **CP5 (`report/team/chi_so.md`, `report/team/ho_so_launch_v0.md`):**
  - Tính thử 3 chỉ số trên 1.200 yêu cầu (`82,83%`, `27,12%`, `4,25%`), đề xuất thêm 2 chỉ số dùng/an toàn, liệt kê 10 event có `trace_id`, đối chiếu chéo từng chỉ số với event và lập 3 dòng rủi ro kinh tế lấy số `simulated` từ `bang_chi_phi.md`.
  - Tổng hợp 7 mục vào `ho_so_launch_v0.md` và đưa ra đề xuất **`Go có điều kiện`** kèm 3 điều kiện kiểm tra cụ thể.

## 4. Bằng chứng

- Pull Request **#10** (`feat/cp3-cp4-pilot-plan` → `main`), các commit `48fdce8`, `41c83ac`.
- Các file đã thực hiện: `src/lab13.py`, `report/team/bang_loi.md`, `report/team/pilot_plan.yaml`, `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md`, `TEAM.md`.

## 5. Công cụ AI đã dùng

- Sử dụng **Antigravity** để gợi ý cấu trúc code Python tính cỡ mẫu CP4 (`co_mau_hai_ti_le`, `tinh_co_mau_cp4`), rà soát cú pháp YAML/Markdown và kiểm tra tính nhất quán giữa các file hồ sơ.
- Tự kiểm tra lại bằng cách chạy script Python trực tiếp trên `src/logix_requests.csv` để đối chiếu toàn bộ số liệu D1 (`1251`, `3103`, `859`, `299`, `6.96`) và E1 (`994/1200 = 82,83%`, `48/177 = 27,12%`, `51/1200 = 4,25%`), kiểm tra `yaml.safe_load` cho `pilot_plan.yaml` và rà soát không vi phạm quy tắc từ cấm của Gate 2a hay còn dấu `?` ngoài chú thích.

## 6. Tự đánh giá

- Hoàn thành đúng hạn các phần CP3 (Nhãn người 2), CP4 và CP5 được phân công; số liệu tự kiểm tra khớp với hướng dẫn và dữ liệu CSV.
- Còn phần việc phối hợp cuối buổi: chờ ghép `Nhãn người 1` của Đức để chốt đồng thuận CP3, cập nhật `ho_so_launch_v0.md` Mục 5, và tham gia chấm chéo Gate 2a (`phieu_cham.md`) cùng nhóm.
