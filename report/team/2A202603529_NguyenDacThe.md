# Báo cáo cá nhân — Nguyễn Đắc Thể

## 1. Thông tin thành viên

- **Họ tên:** Nguyễn Đắc Thể
- **MSSV:** 2A202603529
- **Email:** dacthebn@gmail.com
- **GitHub:** NguyenDacThe
- **Vai trò:** Người 2, kiểm số CP1–CP2, phụ trách pilot CP4 và tiếp quản code sau bàn giao.

## 2. Phần việc phụ trách

- Kiểm tra kết quả A1–A4 và B1–B4, ghi phép đối chiếu và điền bảng chi phí.
- Tính cỡ mẫu D1, đề xuất thiết kế D2, ngưỡng dừng và phương án quay về luồng thủ công.
- Đối chiếu bảng A/B với bản code nhóm sau bàn giao và ghép phần in D1 vào lệnh chạy chung.

## 3. Đóng góp cụ thể

- Bảng A/B được tính lại từ hai CSV. Ví dụ, lấy chi phí **4.373.585 đ** chia **978** việc thành công cho **4.472 đ/việc** (simulated). Tử số cộng phí của toàn bộ lượt chạy, kể cả lượt lỗi.
- Theo B3, giới hạn **2 lần** có chi phí toàn hệ thống thấp nhất là **6.901.220 đ** (simulated). Chi phí **4.111 đ/việc** với giới hạn **1 lần** (simulated) không phản ánh phần chi phí xử lý thêm **85** yêu cầu chuyển nhân viên.
- CP4 đề xuất chia ngẫu nhiên **20 nhân viên mỗi nhóm**, cần ít nhất **299 yêu cầu mỗi người** để đạt khoảng **859 yêu cầu hiệu dụng mỗi nhóm** ở MDE **6 điểm phần trăm**. Nếu tác động thật chỉ **5 điểm**, power xấp xỉ **0,64**.

## 4. Bằng chứng

- [Bảng chi phí A/B](bang_chi_phi.md) có công thức, nguồn và kết quả đã tính độc lập.
- [Code tính cỡ mẫu CP4](../../src/lab13_cp4.py) in D1 và tỉ lệ mở lại **51/1.200 = 4,25%** toàn mẫu, **39/982 = 3,97%** trong phạm vi.
- [Kế hoạch pilot](pilot_plan.yaml) có đối chứng đồng thời, cỡ mẫu, ngưỡng dừng và rollback. Ngày và ngưỡng trong file là đề xuất để nhóm duyệt.

Sau bàn giao, thêm `from lab13_cp4 import in_ket_qua_cp4` và gọi `in_ket_qua_cp4(reqs)` tại `TODO CP4` trong `src/lab13.py`. Chạy toàn bộ lệnh của nhóm từ `src/` rồi đối chiếu kết quả A/B và D1 với hai báo cáo.

## 5. Công cụ AI đã dùng

Dùng ChatGPT (Codex) hỗ trợ đọc đề, viết mã tính CP4, tính lại A/B bằng Python trên dữ liệu gốc và soạn bản nháp các báo cáo. Các phép tính tiêu biểu được ghi ngay trong bảng chi phí để có thể kiểm tra lại. Phần đối chiếu với code nhóm và tự xác nhận của thành viên sẽ được bổ sung sau bàn giao.

## 6. Tự đánh giá

Nội dung để tự rà trước khi nộp gồm phép tính chi phí, cách giải cỡ mẫu theo cụm và ảnh hưởng của MDE lên khả năng phát hiện mức chênh 5 điểm. Bản nháp này chưa ghi kết quả tự đánh giá của thành viên.
