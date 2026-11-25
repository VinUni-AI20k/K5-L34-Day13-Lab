# Báo cáo cá nhân — Đặng Minh Thu - 2A202604009

## 1. Thông tin thành viên

- Họ tên: Đặng Minh Thu
- MSSV: 2A202604009
- Email: 26ai.thudm@vinuni.edu.vn
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): Người kiểm số

## 2. Phần việc phụ trách

Người kiểm số: tính tay một con số để đối chiếu với code, điền bảng A2, A3, A4, B1–B4 trong `report/team/bang_chi_phi.md`, tính ba chỉ số, danh sách event và rủi ro kinh tế trong `report/team/chi_so.md`.

## 3. Đóng góp cụ thể

- Điền `bang_chi_phi.md`: A1, A2 (chi phí mỗi việc thành công 4.472 đ [simulated], gấp 16,3 lần hoá đơn token + tool chia số yêu cầu), A3 (quoc_te 22.515 đ, 1,88× nên loại khỏi phạm vi), A4 (4.599 đ = 0,38× khi cộng chi phí cố định), B1–B4 (xếp hạng: làm lại +51,8%, xem lại +40,7%, lương +23,1%).
- Kiểm số tay: 5.600 lần gọi tool × 15 đ = 84.000 đ; token 3 lần chạy đầu = 506,6 đ; tổng 4.373.585 đ ÷ 978 = 4.472 đ.
- Điền `chi_so.md`: chỉ số chính 82,83%, bỏ qua gợi ý 27,12%, lỗi lọt đến khách 4,25%; 9 event có `trace_id`; 4 dòng rủi ro kinh tế lấy số từ bảng độ nhạy.

## 4. Bằng chứng

- Các file `report/team/bang_chi_phi.md` (mục "Kiểm số tay" cuối file) và `report/team/chi_so.md`.
- Commit trên nhánh `minhthu`.
- Số tính độc lập bằng script riêng trên `logix_runs.csv` và `logix_requests.csv`, khớp bài mẫu trong `docs/`.

## 5. Công cụ AI đã dùng

Claude Code: viết script tính độc lập từ hai file CSV và soạn nháp hai file báo cáo. Tự kiểm tra bằng cách cộng tay tool, token và tổng chi phí; đối chiếu số với hướng dẫn trong `docs/`; kiểm tra "giảm một nửa" bằng nửa "gấp đôi"; rà từ cấm của lab trong hai file.

## 6. Tự đánh giá

Hoàn thành phần việc người kiểm số. Còn phải đối chiếu lại các số này khi `src/lab13.py` của người viết code chạy xong (4.472 đ và 4.373.585 đ).
