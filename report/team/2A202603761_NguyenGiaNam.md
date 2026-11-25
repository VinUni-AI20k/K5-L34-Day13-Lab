# Báo cáo cá nhân — Nguyễn Gia Nam (2A202603761)

## 1. Thông tin thành viên

- Họ tên: Nguyễn Gia Nam
- MSSV: 2A202603761
- Email: mrbasrot@gmail.com
- Vai trong nhóm: Người 2 — kiểm số, phụ trách độ nhạy B và cỡ mẫu D1

## 2. Phần việc phụ trách

- Kiểm tra mô hình chi phí từ trace và đối chiếu một số bằng phép tính độc lập.
- Tính các kịch bản độ nhạy B1–B2, chi phí toàn hệ thống B3 và kiểm tra xem lại 100% ở B4.
- Tính cỡ mẫu D1; bàn giao các chỉ số E1 và tỷ lệ mở lại cho Người 3, Người 4.
- Hoàn thiện bảng chi phí A–B trong `report/team/bang_chi_phi.md`.

## 3. Đóng góp cụ thể

- Bổ sung hàm độ nhạy, chi phí toàn hệ thống, kịch bản xem lại 100% và cỡ mẫu vào `src/lab13.py`.
- Tính D1: 1.251 yêu cầu mỗi nhánh cho mức chênh 5 điểm; 859 mỗi nhánh cho 6 điểm; 299 yêu cầu mỗi nhân viên với 20 nhân viên mỗi nhánh.
- Tính chỉ số chính 82,83%, bỏ qua gợi ý 27,12%, mở lại 7 ngày 4,25%; trong phạm vi nội địa + hàng nặng, mở lại 3,97%.

## 4. Bằng chứng

- `src/lab13.py`: hàm B1–B4, D1 và phần in kết quả.
- `report/team/bang_chi_phi.md`: bảng A–B và kết quả D1, bàn giao E1.
- Lệnh chạy: `cd src; python -X utf8 lab13.py`. Ba phép thử A1 đạt và chương trình in kết quả B, D1, E1.

## 5. Công cụ AI đã dùng

- Dùng ChatGPT/Codex để hỗ trợ cấu trúc hàm và rà phép tính.
- Tự kiểm tra bằng cách chạy code trên hai CSV của repo, đối chiếu các đáp án hướng dẫn và kiểm tra kết quả cỡ mẫu bằng công thức.

## 6. Tự đánh giá

- Đã hoàn thành phần tính toán Người 2 và kiểm tra bằng output chương trình. Nhóm cần tiếp tục rà chéo hồ sơ trước khi nộp.
