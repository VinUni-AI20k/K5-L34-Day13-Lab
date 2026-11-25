# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: Nhom4Nguoi
- Lớp: L3B
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Tính chi phí theo mọi lần chạy và giờ nhân viên, so với baseline 12.000 đ/yêu cầu; chỉ đề xuất pilot có đối chứng. Xem bảng và phương pháp trong `bang_chi_phi.md`.

## 3. Giải pháp

A1–A4 và B1–B4 có trong `src/lab13.py`; D1 và E1 cũng tính bằng script. `chi_so.md` gồm 11 event và bảng đối chiếu; `pilot_plan.yaml` là đề xuất 20+20 staff. Mục C có 17/20 nhãn trùng (85%), ba bất đồng đã thống nhất và đủ năm dòng khắc phục; phiếu chấm chéo chờ hồ sơ nhóm được phân công.

## 4. Kết quả

A1 đạt 1.20/1.25/1.25; A2 4.471,97 đ/việc (simulated). B4 11.742,79 hoặc 12.414,79 đ/việc (simulated). Hồ sơ đề xuất Go có điều kiện; chưa có quyết định hội đồng.

## 5. Khó khăn và cách xử lý

Cài thư viện và push Git cần quyền mạng ngoài sandbox; đã chạy lại sau khi được cấp quyền. Repo tắt Issues nên dùng bình luận commit để bàn giao minh240804. Chưa có xác nhận chạy trên máy thứ hai.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

Thời gian nhân viên vẫn simulated, chưa có đối chứng thật; power 0,6417 khi tác động chỉ 5 điểm. Chưa có kết quả duyệt chéo/hội đồng. LMS do Nguyễn Hoàng Gia An tự nộp theo yêu cầu cập nhật.

## 8. Tài liệu tham khảo

`docs/du_lieu_va_cong_thuc.md`, `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`, `RULES.md`, `SUBMISSION.md`; không thay đổi dữ liệu đề bài.
