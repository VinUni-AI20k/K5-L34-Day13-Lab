# Báo cáo cá nhân — NguyenTuanBach-2A202603596

## 1. Thông tin thành viên

- Họ tên: Nguyen Tuan Bach
- MSSV: 2A202603596
- Email: 26ai.bachnt@vinuni.edu.vn
- GitHub: https://github.com/NguyenTuanBach
- Vai trong nhóm: viết code, kiểm số, gắn nhãn, giữ hồ sơ

## 2. Phần việc phụ trách

Viết `src/lab13.py` (A1, A2, A3, A4, B1–B4, D1, chỉ số E1) và điền các file hồ sơ `bang_chi_phi.md`, `pilot_plan.yaml`, `chi_so.md`, `ho_so_launch_v0.md`; gắn nhãn 20 ca lỗi và lập bảng khắc phục ở `bang_loi.md`.

## 3. Đóng góp cụ thể

- Ba hàm A1 và `mo_hinh` (tử số tính mọi lần chạy kể cả lần lỗi, mẫu số chỉ đếm `thanh_cong`); hàm `co_mau` cho D1.
- Chạy 9 kịch bản độ nhạy, giới hạn chạy lại 1/2/3 lần, kịch bản xem lại 100%.
- Chọn chia pilot theo nhân viên 20 + 20 với mức chênh 6 điểm, viết ba luật dừng.

## 4. Bằng chứng

- `cd src && python lab13.py` in `Ba phép thử đáp án biết trước: ĐẠT` (1,20 · 1,25 · 1,25).
- Chi phí mỗi việc thành công 4.472 đ [simulated], gấp 16,3× hoá đơn token + tool; khoản lớn nhất là làm lại 51,8% [simulated].
- Cỡ mẫu D1: 1.251 · 3.102 (42 người/nhóm, vượt 40 nhân viên) · tối đa 1.000 · tối đa 300 · m ≥ 299.

## 5. Công cụ AI đã dùng

Claude Code (Claude Sonnet 5.5): gợi ý và viết code `lab13.py`, soạn bản nháp các file hồ sơ. Tự kiểm tra: ba phép thử A1 phải ĐẠT; đối chiếu số in ra với bảng đáp án trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (lệch dưới 2%; chênh duy nhất là phút làm lại thực tế trong phạm vi 16,2 so với 15,3 trên toàn mẫu của tài liệu); kiểm tra B1: kịch bản "giảm một nửa" bằng đúng nửa mức tăng của "gấp đôi". Mọi con số trong hồ sơ lấy từ output của `lab13.py`.

Cần tự làm thêm: giải thích được vì sao tử số tính mọi lần chạy, cách tính cỡ mẫu hiệu dụng theo cụm, và lý do đề xuất Go có điều kiện (hội đồng có thể hỏi trực tiếp).

## 6. Tự đánh giá

Phần code và số liệu A, B, D1, E1 đã chạy và khớp đáp án. Số giả lập (phút xem lại, làm lại) cần thay bằng phút đo thật sau tuần 1 của pilot; mẫu D1 chỉ có 40 nhân viên nên chỉ đủ cho mức chênh 6 điểm.
