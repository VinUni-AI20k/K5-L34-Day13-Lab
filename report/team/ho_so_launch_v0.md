# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: Hihihuhu · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ/việc [sim], toàn mẫu, chưa cộng chi phí cố định; gấp 16,28 lần cách chỉ lấy hoá đơn token + tool chia số yêu cầu (274,65 đ). Làm lại chiếm 51,77% và xem lại 40,70% tổng chi phí [sim]. — nguồn: `bang_chi_phi.md` A2 | Giả lập | Người kiểm số |
| 2 · Ba yếu tố nhạy nhất | 1) số ca làm lại gấp đôi +51,77% 2) tỉ lệ xem lại gấp đôi +40,70% 3) lương nhân viên +25% → +23,12% [sim]. Giá token gấp đôi chỉ +5,62%. — nguồn: `bang_chi_phi.md` B1, B2 | Giả lập | Người kiểm số |
| 3 · So với nhân viên tự làm | Phạm vi `noi_dia` + `hang_nang`, 45.000 yêu cầu/tháng, đã cộng chi phí cố định 40 triệu/tháng: 4.599 đ/việc = 0,38× so với 12.000 đ; còn một nửa khối lượng: 5.784 đ = 0,48× [sim]. Cả hệ thống (kể cả phần nhân viên làm thay): 5.865 đ/yêu cầu = 0,49× [sim]. `quoc_te`: 22.515 đ = 1,88×, không đáng xử lý. — nguồn: `bang_chi_phi.md` A3, A4 | Giả lập | Người kiểm số |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | chính: ... · dùng: ... · an toàn: ... — nguồn: `chi_so.md` | Chưa | Người gắn nhãn 1 |
| 5 · Bảng lỗi và cách khắc phục | đồng thuận hai người gắn nhãn: ...; 5 cách khắc phục, mỗi cách có người phụ trách — nguồn: `bang_loi.md` | Chưa | Người gắn nhãn 1 |
| 6 · Pilot plan | phạm vi: ...; cỡ mẫu: ...; luật dừng: ngưỡng ..., hạn ..., người có quyền dừng ... — nguồn: `pilot_plan.yaml` | Chưa | Người gắn nhãn 1 |
| 7 · Rủi ro kinh tế | (1) xem lại 100%: 11.743 đ = 0,98× hoặc 12.415 đ = 1,03× nếu làm lại 15,3 phút/ca [sim] → gần như không tiết kiệm. (2) giới hạn chạy lại: 1 lần rẻ nhất mỗi việc (4.111 đ) nhưng 2 lần rẻ nhất cho cả hệ thống (6.901.220 đ vs 7.449.781 đ) vì thêm 85 yêu cầu chuyển nhân viên [sim]. (3) khối lượng giảm một nửa: cố định +1.185 đ/việc (lên 2.370 đ) [sim]. — nguồn: `bang_chi_phi.md` B3, B4, A4; bổ sung từ `chi_so.md` | Giả lập | Người gắn nhãn 1 |

**Đề xuất:** (chọn một, xoá hai cái còn lại) Go · Go có điều kiện · No-go

Go có điều kiện: ghi từng điều kiện, người phụ trách, ngày kiểm tra. No-go: ghi việc phải làm để quay lại cổng.

- Điều kiện / việc 1: ... — người phụ trách: ... — ngày kiểm tra: ...
- Điều kiện / việc 2: ... — người phụ trách: ... — ngày kiểm tra: ...
- Con số bất lợi và cách xử lý: ...
