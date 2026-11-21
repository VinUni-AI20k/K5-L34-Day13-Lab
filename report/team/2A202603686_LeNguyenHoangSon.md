# Báo cáo cá nhân — Lê Nguyễn Hoàng Sơn — 2A202603686

## 1. Thông tin thành viên

- Họ tên: Lê Nguyễn Hoàng Sơn
- MSSV: 2A202603686
- Email: hoangson199205@gmail.com
- Vai trong nhóm: Người gắn nhãn 2 kiêm giữ hồ sơ

## 2. Phần việc phụ trách

Phụ trách gắn nhãn 20 ca lỗi, xây dựng bảng khắc phục và tổng hợp hồ sơ launch v0. Trực tiếp chạy chương trình, đối chiếu số liệu và rà soát tính nhất quán giữa các phần, review lại nội dung.

## 3. Đóng góp cụ thể

- Phần nhãn lỗi người 2: phân loại 20 ca theo năm loại lỗi, giải thích nguyên nhân gốc và ghi quy tắc phân biệt các ca dễ nhầm. So với nhãn người 1 của Toàn: 20/20 theo xác nhận của nhóm, không có ca bất đồng.
- Phần khắc phục: xây dựng bảng đại diện năm loại lỗi, nêu cách phát hiện đo được, hành động xử lý và vai trò chịu trách nhiệm.
- Phần hồ sơ: tổng hợp bảy mục về chi phí, độ nhạy, so sánh với nhân viên, chỉ số, lỗi, pilot và rủi ro kinh tế; ghi nguồn số và nhãn `simulated`.
- Phần kiểm tra đã có bằng chứng thực tế: chạy `src/lab13.py` trên máy cá nhân, cung cấp output A1–E1; ba phép thử A1 ĐẠT và kết quả khớp đầu ra đã lưu của nhóm.

## 4. Bằng chứng

- [Bảng lỗi](bang_loi.md): 20 nhãn người 2 (trong buổi chiều ngày lab), lý do từng ca và bảng khắc phục năm loại. Đối chiếu với nhãn người 1 (Vũ Thành Toàn)
- [Hồ sơ launch v0](ho_so_launch_v0.md): đủ bảy mục, có số liệu, trạng thái và người phụ trách; đề xuất hiện tại là No-go, nêu số bất lợi (xem lại 100% vượt 12.000 đ, power 0,64) để nhóm thống nhất.
- [Đầu ra chương trình](../../src/ket_qua_lab13.txt): CPS toàn mẫu 4.471,97 đ/việc [simulated]; chỉ số chính 994/1.200 = 82,83%; sửa hoặc bỏ gợi ý 48/177 = 27,12%; mở lại 51/1.200 = 4,25%.
- [Chỉ số, event, rủi ro](chi_so.md) và [kế hoạch pilot](pilot_plan.yaml): nhóm đã điền đủ; tôi rà số với đầu ra chương trình.
- Output chạy lại trên máy cá nhân đã cung cấp trong trao đổi, được đối chiếu khớp toàn bộ đầu ra đã lưu khi bỏ qua khoảng trắng. Chưa bổ sung mã commit cho phần việc này.

## 5. Công cụ AI đã dùng

Sử dụng Codex để review nội dung, nhận gợi ý triển khai và xác định các điểm cần kiểm tra. Tôi chịu trách nhiệm đối chiếu số liệu với output chương trình, kiểm tra nguồn và hoàn thiện nội dung cuối cùng.

Codex hỗ trợ soạn lý do từng ca, bảng khắc phục, hồ sơ launch và nội dung báo cáo; trực tiếp chạy chương trình và cung cấp kết quả. Nhãn người 2 do tôi tự gắn, không dùng AI để tạo nhãn.

Cách tự kiểm tra: đối chiếu mọi con số trong hồ sơ với `src/ket_qua_lab13.txt` và `bang_chi_phi.md`; tự đếm số ca trùng giữa hai cột nhãn; rà toàn bộ hồ sơ để không dùng từ bị cấm theo RULES.md; kiểm tra mỗi mục hồ sơ có vai trò phụ trách và số giả lập có nhãn `simulated`.

## 6. Tự đánh giá

Đã chạy được chương trình từ A1 đến E1 và cung cấp kết quả để đối chiếu. Phần hồ sơ đã có nội dung tổng hợp và nêu các điều kiện còn thiếu, nhưng chưa thể coi toàn bộ nhiệm vụ C và kế hoạch pilot đã hoàn tất. 