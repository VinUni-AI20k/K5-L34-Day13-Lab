# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: PD · Lớp: L3A

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ [simulated], gấp 16,3 lần hoá đơn token + tool chia số yêu cầu (274,7 đ); làm lại chiếm 51,8% tổng chi phí | Giả lập | Người viết code |
| 2 · Ba yếu tố nhạy nhất | 1. Số ca làm lại (gấp đôi: +51,8%) · 2. Tỉ lệ xem lại (+40,7%) · 3. Lương nhân viên (+25%: +23,1%); giá token gấp đôi chỉ +5,6% [simulated] | Giả lập | Người viết code |
| 3 · So với nhân viên tự làm | Cả hệ thống 5.865 đ/yêu cầu = 0,49× của 12.000 đ (đã cộng 222 ca không thành công do nhân viên làm thay) [simulated]; phạm vi noi_dia + hang_nang cộng cố định 40 triệu/tháng: 4.599 đ = 0,38× [simulated] | Giả lập | Người kiểm số |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chỉ số trong đợt chạy thử: chính 82,83% (994/1.200) · bỏ qua gợi ý 27,12% (48/177) · mở lại 7 ngày 4,25% (51/1.200); 8 event có `trace_id` trong `chi_so.md` | Xong, có bằng chứng | Người kiểm số |
| 5 · Bảng lỗi và cách khắc phục | Đồng thuận 18/20 = 90% (lệch ca 8, 13, đã có quy tắc); 5 ca khắc phục đủ năm loại (1, 20, 18, 19, 5), mỗi dòng có event, ngưỡng, tần suất; hoàn trùng (ca 20) và hoàn thừa ngầm (ca 5) là hai lỗi tiền phải chặn trước pilot | Xong, có bằng chứng | Người gắn nhãn 1 |
| 6 · Pilot plan | Chia theo nhân viên 20 + 20, chỉ noi_dia + hang_nang; MDE 6 điểm (859/nhóm, m ≥ 299, DE 6,96); power chỉ 0,64 nếu tác động thật là 5 điểm; cần đủ 40 nhân viên; thu mẫu ≥ 5.980 yêu cầu/nhóm + 7 ngày theo dõi, quyết định 2027-01-12; 5 luật dừng (bước 4 người chỉ dùng luật tuyệt đối; so với đối chứng từ 10 người; ngưỡng chi phí 8.000 đ chưa cộng cố định) | Xong, có bằng chứng | Người giữ hồ sơ |
| 7 · Rủi ro kinh tế | Làm lại gấp đôi → 6.787 đ (+51,8%); xem lại 100% → 11.743 đ = 0,98× (1,03× nếu làm lại 15,3 phút); khối lượng còn một nửa → cố định +2.370 đ/việc [simulated] | Giả lập | Người giữ hồ sơ |

**Đề xuất:** Go có điều kiện cho pilot noi_dia + hang_nang, với các điều kiện:

- Giám đốc vận hành ký chấp nhận mức chênh 6 điểm (power 0,64 ở mức 5 điểm) · Giám đốc vận hành · kiểm tra trước ngày bắt đầu.
- Xác nhận đủ 40 nhân viên đủ điều kiện để chia 20 + 20 (dữ liệu chạy thử chỉ có 20); nếu không, chia 10 + 10 với MDE 8 điểm · Giám đốc vận hành · kiểm tra trước ngày bắt đầu 2026-12-07.
- Sửa khoá chống trùng và đối soát sổ cái trước ngày bắt đầu · Kỹ sư trưởng agent · kiểm tra 2026-12-04.
- Bật đủ event có `trace_id`; thay phút simulated bằng phút đo thật sau tuần 1 · PM trợ lý hoàn phí · kiểm tra cuối tuần 1.
- Có kế hoạch giảm xem lại theo bậc (khi tỉ lệ sửa + bỏ < 15%), vì xem lại 100% thì không tiết kiệm (B4: 0,98×–1,03×) · Trưởng nhóm CSKH · kiểm tra cuối bước rollout 0,25.
- Sửa cách tính hoàn cho đơn có mã giảm giá (ca 5) và bật kiểm tra mẫu 100 đơn/tuần với ngưỡng 1% đơn lệch · Kế toán trưởng · kiểm tra trước ngày bắt đầu và hằng tuần.
