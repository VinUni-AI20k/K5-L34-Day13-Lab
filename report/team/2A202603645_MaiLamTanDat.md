# Báo cáo cá nhân — MaiLamTanDat-2A202603645

## 1. Thông tin thành viên

- Họ tên: Mai Lâm Tấn Đạt
- MSSV: 2A202603645
- Email: 26ai.datmlt@vinuni.edu.vn
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): Người kiểm số; người gắn nhãn 2 kiêm giữ hồ sơ

## 2. Phần việc phụ trách

- Người kiểm số: tính lại độc lập các số của CP1, CP2, D1 và E1 để đối chiếu với `src/lab13.py`; ghi cách tính tay vào `report/team/bang_chi_phi.md`.
- Người gắn nhãn 2: gắn nhãn 20 ca lỗi ở CP3.
- Người giữ hồ sơ: điền `report/team/chi_so.md`, cập nhật `report/team/ho_so_launch_v0.md`.

## 3. Đóng góp cụ thể

- Kiểm số: viết script riêng, không import `lab13.py`, đọc CSV và cộng tay từng khoản. Kết quả khớp bản của Tuấn: tổng chi phí 4.373.585 đ, chi phí mỗi việc thành công 4.472 đ [simulated], các bảng A3, A4, B1–B4; D1 (1.251 yêu cầu mỗi nhóm, m ≥ 299, power ≈ 0,64); E1 (82,83% · 27,12% · 4,25%).
- `chi_so.md`: ba chỉ số tính thử, hai chỉ số nhóm đề xuất (tỉ lệ yêu cầu có mở gợi ý; tỉ lệ hoàn trùng hoặc sai số tiền, ngưỡng 0 ca), 8 event có `trace_id`, ba dòng rủi ro kinh tế lấy số từ bảng độ nhạy.
- `ho_so_launch_v0.md`: điền tên nhóm và lớp, cập nhật mục 4, sửa số 12.414 đ thành 12.415 đ ở mục 7.
- Nhãn người 2: cung cấp bộ nhãn 20 ca kèm lý do phân loại; đối chiếu với nhãn của Lam trùng 20/20 (100%) trong `bang_loi.md`.

## 4. Bằng chứng

- `report/team/bang_chi_phi.md`, mục "Kiểm số độc lập".
- `report/team/chi_so.md` và `report/team/ho_so_launch_v0.md`.
- Số chính đã kiểm: chi phí mỗi việc thành công 4.472 đ [simulated], gấp 16,3 lần hoá đơn token + tool chia số yêu cầu (274,7 đ).

## 5. Công cụ AI đã dùng

- Antigravity (trợ lý AI): hỗ trợ viết script kiểm số, soạn nháp `chi_so.md` và các mục hồ sơ.
- Cách tự kiểm tra: tính lại độc lập bằng script riêng và đối chiếu từng số với `lab13.py` và hướng dẫn lab (lệch 0% ở A–B, dưới 0,1% ở D1). Nhãn lỗi do tôi cung cấp; AI chỉ ghi vào `bang_loi.md` và tính tỉ lệ đồng thuận.

## 6. Tự đánh giá

- **Làm tốt:** kiểm số độc lập được toàn bộ A–B, D1, E1 và phát hiện chênh làm tròn 12.414 so với 12.415 đ.
- **Chưa tốt:** mục 6 của hồ sơ chờ `pilot_plan.yaml`; hai bộ nhãn trùng 20/20 nên chưa có ca lệch để thảo luận quy tắc phân biệt.
- **Lần sau:** gắn nhãn độc lập ngay từ đầu buổi để không chặn CP3.
