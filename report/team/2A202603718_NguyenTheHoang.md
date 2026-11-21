# Báo cáo cá nhân — Nguyễn Thế Hoàng (2A202603718)

## 1. Thông tin thành viên

- Họ tên: Nguyễn Thế Hoàng
- MSSV: 2A202603718
- Email: 26ai.hoangnt3@vinuni.edu.vn
- Vai trong nhóm: Người 3, người gắn nhãn 1 và phụ trách phần chỉ số, event, rủi ro kinh tế.

## 2. Phần việc phụ trách

- CP3: Gắn nhãn 20 ca theo nguyên nhân gốc, sau đó đối chiếu với Vũ Đức Anh và hoàn thiện bảng khắc phục.
- CP5: Chuẩn bị chỉ số, event và rủi ro kinh tế để Vũ Đức Anh tổng hợp hồ sơ Gate 2a.

## 3. Đóng góp cụ thể

- Nguyễn Thế Hoàng tự cung cấp bộ nhãn cho 20 ca. Bảng lưu đủ 20 nhãn gốc và chuẩn hóa cách viết tên loại.
- Phần việc của vai Người 3 đã có bảng khắc phục 5 ca, đặc tả 5 chỉ số, 10 event có `trace_id` và 3 dòng rủi ro kinh tế. Codex hỗ trợ chuẩn bị các nội dung này.
- Đối chiếu hai bộ nhãn độc lập của Hoàng và Vũ Đức Anh cho kết quả 17/20 (85%). Hai người thống nhất nhãn cho ca 3, 8 và 13. Bộ nhãn thống nhất khớp 20/20 nhãn tham khảo. Hai dòng rủi ro độ nhạy khớp đầu ra B1 của `src/lab13.py`. Dòng xem lại 100% lấy số từ B4 trong [bảng chi phí nhóm](bang_chi_phi.md). Đã đưa kết quả CP3 và CP5 vào mục 4, 5 và 7 của [hồ sơ launch](ho_so_launch_v0.md).

## 4. Bằng chứng

- [Bảng lỗi CP3](bang_loi.md), hai cột nhãn gốc, kết quả đồng thuận và bảng khắc phục.
- [Đặc tả chỉ số, event và rủi ro CP5](chi_so.md). Số đối chiếu từ CSV là 994/1.200, 48/177 và 51/1.200 cho ba chỉ số đã tính thử.

## 5. Công cụ AI đã dùng

- Dùng Codex để nhập bộ nhãn do Hoàng cung cấp, dự thảo nội dung, đếm lại ba chỉ số từ CSV bằng Python và đối chiếu công thức độ nhạy.

## 6. Tự đánh giá

Tôi gắn nhãn độc lập đủ 20 ca. Bộ nhãn gốc trùng 17 ca với bộ của Vũ Đức Anh. Ba ca khác nhãn cho tôi ba dấu hiệu để phân biệt: ca 3 là chênh lệch kỳ vọng của khách dù trợ lý làm đúng thiết kế, ca 8 là thông tin sai xuất hiện ngay trong câu trả lời, và ca 13 là yêu cầu vượt phạm vi xử lý. Khi rà chỉ số, điểm cần chú ý là mẫu số của tỉ lệ sửa hoặc bỏ gợi ý gồm 177 yêu cầu đã được xem lại. Codex đếm lại từ CSV và đối chiếu hai rủi ro kinh tế với B1. Khi đưa chỉ số vào pilot, tôi cần thống nhất với người phụ trách pilot về thời điểm bắt đầu cửa sổ mở lại 7 ngày.
