# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: chưa điền
- Lớp: L3A
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Nhóm đang xây dựng hồ sơ Gate 2a cho pilot trợ lý hoàn phí LogiX-VN. Checkpoint 1 (A1–A4) và Checkpoint 2 (B1–B4) đã được tính trên mẫu giả lập 1.200 yêu cầu và 1.624 lần chạy. Các nhiệm vụ C–E chưa được tổng hợp.

## 3. Giải pháp

Tóm tắt cách nhóm làm từng nhiệm vụ A–E và link tới file hồ sơ tương ứng.

Nhiệm vụ A tính chi phí từ tất cả lần chạy của agent, cộng thời gian xem lại/làm lại (các cột `*_simulated`) và chia cho số yêu cầu thành công. Nhiệm vụ B chạy 9 kịch bản độ nhạy, mô hình hoá giới hạn retry và kiểm tra trường hợp xem lại 100%. Báo cáo chi tiết: [bang_chi_phi.md](bang_chi_phi.md). Các nhiệm vụ C–E sẽ được bổ sung sau khi hoàn tất.

## 4. Kết quả

Chi phí A2 là 4.472 đ/việc thành công; A4 trong phạm vi pilot là 4.599 đ/việc ở 45.000 yêu cầu/tháng. Ước tính toàn hệ thống là 5.865 đ/yêu cầu (0,49× baseline) sau khi cộng 222 ca chuyển nhân viên. B1 cho thấy làm lại tăng gấp đôi làm CPS tăng 51,8% lên 6.787 đ; xem lại tăng gấp đôi làm CPS tăng 40,7% lên 6.292 đ. Ở giới hạn 2 lần chạy, tổng chi phí hệ thống thấp nhất: 6.901.220 đ. Xem lại 100% cho pilot cho CPS 11.743 đ với giả định làm lại 9 phút, hoặc 12.415 đ với mức 15,3 phút/ca [simulated]. Chưa có kết luận cuối hoặc kết quả duyệt chéo.

## 5. Khó khăn và cách xử lý

Checkpoint 1 đã chạy thành công sau khi cấu hình đầu ra UTF-8 trên Windows; ba phép thử A1 đều đạt. Khi phân tích, cần phân biệt chi phí trên việc trợ lý hoàn thành (4.472 đ) với chi phí toàn hệ thống vì các ca chuyển nhân viên chưa có phút xử lý trong cột giả lập.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

Chưa hoàn tất: phân loại lỗi C, cỡ mẫu và kế hoạch pilot D, chỉ số và rủi ro E. Tên nhóm, thông tin thành viên và kết quả duyệt chéo cần được nhóm bổ sung.

## 8. Tài liệu tham khảo

...
