# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: GREEN · Lớp: L3B · Người giữ hồ sơ: Thành viên 4 (Nguyễn Đức Hải)

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | **4.472 đ** toàn mẫu, gấp 16,3 lần hoá đơn token + tool chia số yêu cầu (274,7 đ); giờ nhân viên chiếm 92,5%. Trong phạm vi noi_dia + hang_nang 3.414 đ; cộng cố định 40 triệu đ/tháng thành 4.599 đ [simulated]. [bang_chi_phi.md](bang_chi_phi.md) | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | 1. Số ca làm lại gấp đôi **+51,8%** · 2. Tỉ lệ xem lại gấp đôi **+40,7%** · 3. Lương tăng 25% **+23,1%**; giá token gấp đôi chỉ +5,6% [simulated]. | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Trong phạm vi: **0,38×** của 12.000 đ (0,48× nếu khối lượng còn một nửa); cộng 82 ca nhân viên làm thay: 0,43×. **Bất lợi:** xem lại 100% thành 0,98×, hoặc 1,03× nếu làm lại 15,3 phút [simulated]. quoc_te 1,88×, doi_tac 0,85× nên để ngoài pilot. | Giả lập | Giám đốc vận hành LogiX-VN |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Trong đợt chạy thử (không có đối chứng): chính **82,83%** (994/1.200), bỏ qua gợi ý **27,12%** (48/177), mở lại 7 ngày **4,25%** (51/1.200). Trong phạm vi: 92,26% · 21,09% · 3,97%; hang_nang mở lại 8,23%. 12 event có `trace_id`. **Bất lợi:** xem lại trung bình 5,03 phút/lượt, sát hoà vốn 5,1 phút [simulated]. [chi_so.md](chi_so.md) | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | Đồng thuận **20/20 = 100%**; phân bố 4 · 5 · 4 · 4 · 3. Khắc phục 5 ca (1, 20, 18, 4, 17), mỗi ca có event, ngưỡng, tần suất; ca 20 (hoàn trùng) ngưỡng 0 ca. [bang_loi.md](bang_loi.md) | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | Chia theo nhân viên 20 + 20, MDE **6 điểm** (859/nhóm, DE 6,96, m ≥ 299). **Bất lợi:** 5 điểm thì power chỉ 0,64. 4 luật dừng đủ NẾU – TRONG – THÌ – KHÔNG THÌ; quyết định 2027-01-18. [pilot_plan.yaml](pilot_plan.yaml) | Xong, có bằng chứng | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Làm lại gấp đôi: 6.787 đ (+51,8%); xem lại 100%: 11.743 đ = 0,98×; khối lượng giảm một nửa: +2.370 đ/việc, hoà vốn ≈ 6.212 yêu cầu/tháng [simulated]. [chi_so.md](chi_so.md) | Giả lập | PM trợ lý hoàn phí |

**Đề xuất:** **Go có điều kiện** cho pilot noi_dia + hang_nang, bắt đầu 2026-12-07. Lý do: trong phạm vi chỉ 0,38× của 12.000 đ [simulated], nhưng chưa có đối chứng, xem lại 100% gần như xoá phần tiết kiệm, và lỗi hoàn trùng (ca 20) chưa sửa.

| Điều kiện | Người phụ trách | Ngày kiểm tra |
| --- | --- | --- |
| Sửa khoá chống trùng và chỉ báo "đã hoàn" khi sổ cái trả ok (ca 20, ca 7); đối soát mỗi giờ chạy được, ngưỡng 0 ca | Kỹ sư trưởng agent | 2026-12-04 |
| Ký chấp nhận MDE 6 điểm (power 0,64 nếu tác động thật chỉ 5 điểm) và 4 luật dừng, commit trước ngày bắt đầu | Giám đốc vận hành LogiX-VN | 2026-12-04 |
| Bật đủ 12 event, một `trace_id` gốc cho cả vòng đời yêu cầu; từ tuần 1 thay phút `_simulated` bằng phút xem lại, làm lại đo thật | PM trợ lý hoàn phí | 2026-12-14 |
| Giảm xem lại theo bậc 100% → 50% → 25% khi sua + bo < 15% (hiện 21,1%), mỗi lần xem lại ≤ 5 phút; không đạt thì không mở bước 0.50 | Trưởng nhóm CSKH | 2026-12-20 |
| hang_nang mở lại 8,23% đã cao hơn trần 6%: so riêng với hang_nang của nhóm đối chứng, cao hơn ≥ 2 điểm thì thu hẹp về noi_dia | PM trợ lý hoàn phí | 2026-12-20 |
