# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: CATH · Lớp: L3A

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ [simulated], gấp 16,3 lần hoá đơn token chia số yêu cầu (274,7 đ). Giờ nhân viên chiếm 92,5% tổng chi phí [simulated] | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | 1. Số ca làm lại (+51,8%) · 2. Tỉ lệ xem lại (+40,7%) · 3. Lương nhân viên (+23,1%) [simulated]; giá token chỉ +5,6% | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Cả hệ thống: 5.865 đ/yêu cầu = 0,49× của 12.000 đ [simulated]. Phạm vi noi_dia + hang_nang: 4.599 đ = 0,38× khi đã cộng cố định 40 triệu/tháng ở 45.000 yc/tháng; 5.784 đ = 0,48× nếu khối lượng còn một nửa [simulated] | Giả lập | Kế toán trưởng |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Trong đợt chạy thử (chưa có đối chứng): chính 82,83% đóng trong 24h và không mở lại 7 ngày (994/1.200); dùng 27,12% bỏ qua gợi ý (48/177); an toàn 4,25% mở lại trong 7 ngày (51/1.200), riêng hang_nang 8,23% | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | 20 ca, hai người rà và quyết định nhãn riêng trước khi so (có AI hỗ trợ, đã ghi nguồn trong `bang_loi.md`), khớp 20/20; 5 ca khắc phục đủ 5 loại Google PAIR, mỗi dòng có cách phát hiện đo được và một vai trò phụ trách | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | Chia theo nhân viên, 20 + 20 tại 12 depot, mức chênh 6 điểm: 859 là cỡ mẫu hiệu dụng mỗi nhóm (DE 6,96), tương ứng 20 nhân viên × 299 = 5.980 yêu cầu thực tế mỗi nhóm; power chỉ 0,64 nếu tác động thật là 5 điểm. 3 luật dừng đủ NẾU–TRONG–THÌ–KHÔNG THÌ (an toàn +2 điểm hoặc trần 6%; chi phí > 8.000 đ/việc 2 tuần; bỏ qua gợi ý > 40%). Quyết định: 2027-01-05 | Xong, có bằng chứng | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | Làm lại gấp đôi → 6.787 đ (+51,8%) [simulated]. Xem lại 100% → 11.743 đ = 0,98×, hoặc 12.415 đ = 1,03× nếu làm lại 15,3 phút [simulated]. Khối lượng giảm nửa → cố định +2.370 đ/việc [simulated] | Giả lập | PM trợ lý hoàn phí |

Con số bất lợi và cách xử lý:

- Xem lại 100% gần hoà vốn (0,98×, hoặc 1,03× [simulated]) → giảm xem lại theo bậc, mỗi lần xem lại phải ≤ 5,1 phút.
- hang_nang: mở lại 8,23% (vượt trần 6% nếu tính riêng) và 8.221 đ/việc [simulated] (vượt ngưỡng 8.000 đ) → luật dừng tính trên cả phạm vi; nếu luật chi phí kích hoạt thì thu hẹp về noi_dia.
- Power 0,64 ở mức 5 điểm → Giám đốc vận hành ký chấp nhận trước ngày bắt đầu.

Điều kiện cho Go có điều kiện (mỗi điều kiện có người phụ trách và ngày kiểm tra):

- Sửa khoá chống trùng và đối soát sổ cái (ca 7, 20) trước ngày bắt đầu pilot → **Kỹ sư trưởng agent**, kiểm tra trước 2026-12-20.
- Ký chấp nhận mức chênh 6 điểm (power 0,64 nếu tác động thật là 5 điểm) → **Giám đốc vận hành**, trước 2026-12-15.
- Bật đủ event có `trace_id`; thay phút simulated bằng phút đo thật sau tuần 1 → **Kỹ sư trưởng agent**, kiểm tra cuối tuần 1.
- Giảm xem lại theo bậc khi tỉ lệ sửa + bỏ < 15%, vì xem lại 100% thì chi phí 11.743 đ = 0,98× [simulated] → **Trưởng nhóm CSKH**, kiểm tra cuối bước 0.25.

**Đề xuất: Go có điều kiện** cho pilot phạm vi noi_dia + hang_nang (0,22× và 0,69× so với 12.000 đ [simulated]); loại quoc_te (1,88× [simulated]) và doi_tac (0,85× [simulated]). Điều kiện ở trên.
