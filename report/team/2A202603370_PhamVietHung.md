# Báo cáo cá nhân — Phạm Việt Hưng

## 1. Thông tin thành viên

- Họ tên: Phạm Việt Hưng
- MSSV: 2A202603370
- Email: hungphamm1507@gmail.com
- Vai trong nhóm: Người 4, phụ trách thiết kế pilot D (`report/team/pilot_plan.yaml`, `src/lab13_d.py`) và gắn nhãn lỗi lần hai ở nhiệm vụ C.

## 2. Phần việc phụ trách

- Tính năm câu cỡ mẫu D1 và bàn giao code cho Người 1 tích hợp vào `src/lab13.py`.
- Phụ trách duy nhất `report/team/pilot_plan.yaml`: phạm vi pilot, cách chia nhóm, cỡ mẫu, đánh đổi thống kê, năm câu kiểm tra D2, ba luật dừng đủ bốn vế, rollback và ngày quyết định.
- Gắn nhãn 20 ca lỗi (người gắn nhãn thứ hai ở nhiệm vụ C) để đối chiếu đồng thuận với Người 3.

## 3. Đóng góp cụ thể

- Viết `co_mau` và `in_d1` trong `src/lab13_d.py` để tính năm câu D1 (`a = 1.251`; `b = 3.103` tức cần 84 > 40 nhân viên; `c = 1.000`; `d = 300`; `e`: với MDE +6 điểm cần `859` hiệu dụng/nhóm, `m >= 299` yêu cầu/nhân viên, `DE = 6,96`) và tính power thực tế còn `0,6411` (~64,1%) nếu hiệu ứng thật chỉ là `+5 điểm`.
- Tính các chỉ số nền từ `src/logix_requests.csv`: tỉ lệ `mo_lai_trong_7_ngay` hiện tại là `4,25%` toàn mẫu (`51/1.200`) và `3,97%` trong `noi_dia + hang_nang` (`39/982`); tỉ lệ bỏ qua gợi ý `(sua + bo)/duoc_xem_lai` là `27,12%` toàn mẫu (`48/177`) và `21,09%` trong phạm vi (`27/128`).
- Hoàn thiện `report/team/pilot_plan.yaml`: thu hẹp `scope` về `noi_dia` (`2.696 đ = 0,22×`) và `hang_nang` (`8.221 đ = 0,69×`) [simulated], loại `quoc_te` (`1,88×`) và `doi_tac` (`0,85×`); chia theo `staff` 20+20 phân tầng theo depot; viết 3 luật dừng đủ bốn vế `NẾU – TRONG – THÌ – KHÔNG THÌ` (ngưỡng chi phí `> 8.000 đ` [simulated] tham chiếu bảng B của Người 2, ngưỡng an toàn chặn ca hoàn trùng và mở lại 7 ngày), rollback trong 30 phút dưới quyền `Giám đốc vận hành LogiX-VN`, và liệt kê đầy đủ `simulated_inputs`.
- Hoàn thiện bộ nhãn 20 ca lỗi theo năm loại Google PAIR để đối chiếu cùng Người 3 trong `report/team/bang_loi.md`.

## 4. Bằng chứng

- [Kế hoạch pilot](pilot_plan.yaml) (commit `16da1d5` trên nhánh `hung`, merge vào `main` tại `2f53eb1`): đọc hợp lệ bằng `yaml.safe_load`, không còn dấu `?` ngoài dòng chú thích, tuân thủ quy tắc 5 trong `README.md`.
- [Code D1 bàn giao Người 1](../../src/lab13_d.py) được import và chạy trực tiếp trong [src/lab13.py](../../src/lab13.py) (`cd src && python lab13.py`).
- Bộ 20 nhãn lỗi nhiệm vụ C đối chiếu với [Bảng lỗi và cách khắc phục](bang_loi.md).

## 5. Công cụ AI đã dùng

- Dùng trợ lý AI (Gemini) để giải thích công thức cỡ mẫu cụm (`DE`, trần `c / ICC`), viết đoạn code D1 (`src/lab13_d.py`), hoàn thiện cấu trúc `report/team/pilot_plan.yaml`, trích xuất 20 ca lỗi từ `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` và hỗ trợ phân loại 20 ca lỗi theo sự cho phép của labcoach.
- Cách tự kiểm tra: chạy `python lab13_d.py` và `python lab13.py` trong thư mục `src/` để kiểm chứng toàn bộ đầu ra A1–A4, B1–B4, D1; kiểm tra lại bằng tính tay cho công thức D1e (`20m / (1 + (m - 1) * 0,02) >= 859`); chạy `yaml.safe_load` và rà soát checklist nộp bài trên `report/team/pilot_plan.yaml`.

## 6. Tự đánh giá

- Đã hoàn thành đầy đủ phần D (`pilot_plan.yaml`, `src/lab13_d.py`) khớp số liệu A, B của Người 1 và Người 2, không có lỗi cú pháp.
- Khi bảo vệ trước hội đồng Gate 2a, cần trình bày rõ đánh đổi nâng MDE lên +6 điểm khiến power ở mức +5 điểm còn `0,64`, đồng thời phối hợp Người 3 và Người 5 rà soát lần cuối trước khi nộp link repo trên LMS.
