# Báo cáo cá nhân — Bùi Phương Ngọc (2A202603788)

## 1. Thông tin thành viên

- Họ tên: Bùi Phương Ngọc
- MSSV: 2A202603788
- Email: thengoc041012@gmail.com
- Vai trong nhóm: Người viết code (Người 1)

## 2. Phần việc phụ trách

- Chuẩn bị môi trường Python và chủ trì nhiệm vụ A: A1–A4 trong `src/lab13.py`.
- Tính mô hình chi phí từ trace, phân tích bốn loại yêu cầu và ảnh hưởng của chi phí cố định 40 triệu đồng/tháng.
- Bàn giao mô hình và số liệu A cho Người 2; theo phân công, phối hợp kiểm tra B3, B4, D1 và chạy bản cuối trên máy khác.

## 3. Đóng góp cụ thể

- Tạo môi trường `.venv` bằng Python 3.13 và cài các thư viện trong `src/requirements.txt`.
- Viết ba hàm A1; các phép thử cho kết quả 1,20 · 1,25 · 1,25.
- Viết `mo_hinh(...)`: tính token và tool trên mọi lần chạy, kể cả lần lỗi; tính thời gian xem lại/làm lại từ cột `_simulated`; chia tổng chi phí cho số yêu cầu thành công. Chi phí chạy lại được báo riêng nhưng không cộng hai lần.
- Tính A2: tổng chi phí 4.373.585đ (có phần simulated); 978 việc thành công; 4.472đ/việc thành công [simulated].
- Tính A3 cho bốn loại yêu cầu. `quoc_te` có CPS 22.515đ [simulated] (1,88× baseline). Giới hạn từ 1 lên 2 lần tăng số thành công từ 32 lên 41/150 nhưng CPS tăng từ 20.403đ [simulated] lên 20.605đ [simulated]; lần thứ 3 không thêm thành công, CPS là 22.515đ [simulated].
- Tính A4 cho `noi_dia` + `hang_nang`: 4.599đ/việc thành công ở 45.000 yêu cầu/tháng và 5.784đ ở nửa khối lượng [simulated].
- Điền các kết quả A1–A4 và kết luận vào `report/team/bang_chi_phi.md`.

## 4. Bằng chứng

- File: `src/lab13.py`, `report/team/bang_chi_phi.md`.
- Các commit A1–A4 và cập nhật theo review: `8ac8446`, `942f8b9`; PR được merge vào `main` tại `39194b6`.
- Chạy `python lab13.py` trong `src/`: A1 in `ĐẠT`; đầu ra A2–A4 khớp các số đã ghi trong bảng chi phí. `git diff --check` không báo lỗi.

## 5. Công cụ AI đã dùng

- Dùng ChatGPT/Codex để giải thích yêu cầu A1–A4, hỗ trợ triển khai và rà soát mô hình chi phí, cùng xử lý lỗi encoding stdout trên Windows.
- Kiểm tra kết quả bằng cách chạy script trên hai CSV của bài, đối chiếu A1 với ba đáp án biết trước và đối chiếu A2–A4 với hướng dẫn/số liệu của lab. Không gọi model thật và không dùng API key.

## 6. Tự đánh giá

- Đã hoàn thành sản phẩm A1–A4. Trước khi bảo vệ, cần tự tính lại CPS và luyện giải thích vì sao tử số tính mọi lần chạy nhưng mẫu số chỉ tính yêu cầu thành công.
- Cần hoàn tất phần phối hợp theo phân công: kiểm B3, B4, D1 và chạy bản chốt trên máy khác; khi bảo vệ cần phân biệt `status == 'ok'` của một lần chạy với `ket_qua == 'thanh_cong'` của yêu cầu.
