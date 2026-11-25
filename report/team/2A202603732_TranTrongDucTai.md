# Báo cáo cá nhân — 2A202603732_TranTrongDucTai

## 1. Thông tin thành viên

- Họ tên: Trần Trọng Đức Tài
- MSSV: 2A202603732
- Email: ductai202603732@gmail.com
- Vai trong nhóm: Người gắn nhãn 2 kiêm giữ hồ sơ

## 2. Phần việc phụ trách

- **Nhiệm vụ C (Gắn nhãn lỗi):** Độc lập gắn nhãn 20 ca lỗi theo chuẩn Google PAIR trong 8 phút (cột Nhãn người 2), phối hợp cùng Người gắn nhãn 1 (Người 3) so nhãn, giải quyết các ca bất đồng và hoàn thiện bảng 5 ca khắc phục.
- **Nhiệm vụ D3 (Kế hoạch pilot):** Chủ trì thiết kế và điền đầy đủ file `report/team/pilot_plan.yaml` (các thông số cỡ mẫu D1, câu trả lời D2, phạm vi, 3 luật dừng chuẩn NẾU - TRONG - THÌ - KHÔNG THÌ, rollback, ngày quyết định).
- **Nhiệm vụ E3 & Điều phối:** Chủ trì tổng hợp hồ sơ launch v0 một trang (`report/team/ho_so_launch_v0.md`), tổng hợp `TEAM.md`, ghi nhận kết quả duyệt chéo tại `report/team/phieu_cham.md` và hoàn thiện báo cáo nhóm `group_report.md`.

## 3. Đóng góp cụ thể

- Hoàn thành bộ 20 nhãn độc lập (cột Nhãn người 2) trong `report/team/bang_loi.md`, đạt độ chính xác cao theo nguyên nhân gốc.
- Tính toán và cấu hình đầy đủ kế hoạch pilot trong `report/team/pilot_plan.yaml`, giải quyết bài toán trade-off cỡ mẫu cụm (chấp nhận MDE 6 điểm với 20 nhân viên mỗi nhóm, m >= 299 yêu cầu/nhân viên).
- Soạn thảo 3 luật dừng bắt buộc cho kế hoạch pilot: luật an toàn (dựa trên baseline 4,25% mở lại trong 7 ngày), luật chi phí (trần 8.000 đ), luật mức sử dụng (tỉ lệ bỏ qua < 40%).
- Khởi tạo và đồng bộ hồ sơ launch v0 một trang bám sát 7 mục bắt buộc và quy chuẩn Gate 2a.

## 4. Bằng chứng

- File kế hoạch pilot: `report/team/pilot_plan.yaml` (hợp lệ cú pháp YAML, không còn dấu hỏi).
- Cột Nhãn người 2 trong: `report/team/bang_loi.md`.
- Hồ sơ launch: `report/team/ho_so_launch_v0.md`.
- File phân công và thông tin nhóm: `TEAM.md`.
- Nhánh Git làm việc: `2A202603732_TranTrongDucTai`.

## 5. Công cụ AI đã dùng

- **Công cụ:** Antigravity AI Assistant.
- **Mục đích:** Hỗ trợ đối chiếu công thức cỡ mẫu cụm, kiểm tra cấu trúc cú pháp file YAML, rà soát tính nhất quán giữa các tài liệu và kiểm tra các quy định liêm chính học thuật (không dùng thuật ngữ vận hành thực tế khi chưa qua Gate 2a, gán vai trò chịu trách nhiệm cụ thể).
- **Cách tự kiểm tra:** Đọc và đối chiếu từng tham số với `docs/du_lieu_va_cong_thuc.md` và `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`; chạy script kiểm tra YAML bằng thư viện `yaml` của Python.

## 6. Tự đánh giá

- Hoàn thành đầy đủ và đúng hạn trách nhiệm của Người gắn nhãn 2 kiêm giữ hồ sơ.
- Đảm bảo tính trung thực số liệu, nắm rõ cơ sở kinh tế và phương pháp luận thiết kế thử nghiệm A/B dạng cụm.
