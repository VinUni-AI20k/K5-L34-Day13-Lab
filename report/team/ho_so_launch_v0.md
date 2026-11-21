# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức.

Nhóm: dimuon · Lớp: L3A

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ toàn mẫu; trong phạm vi pilot (`noi_dia` + `hang_nang`): 3.414 đ (chưa cố định), 4.599 đ (cộng 40 tr/tháng ở 45.000 yc) | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | 1. Số ca làm lại (±51,8%) · 2. Tỉ lệ xem lại (±40,7%) · 3. Lương nhân viên (+23,1%). Giá token x2 chỉ tăng 5,6% | Giả lập | Kỹ sư trưởng agent |
| 3 · So với nhân viên tự làm | Trong phạm vi pilot: 0,38× ở 45.000 yc/tháng, 0,48× ở một nửa khối lượng (so với 12.000 đ nhân viên tự làm) | Giả lập | Giám đốc tài chính |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chạy thử: đóng trong 24h & không mở lại 7 ngày = 82,83%; bỏ qua gợi ý = 27,12%; mở lại 7 ngày = 4,25% | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | 20 ca phân vào 5 loại Google PAIR (đồng thuận 85%); 5 ca khắc phục mẫu có event đo và vai trò chịu trách nhiệm | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | Chia theo nhân viên (20 đối chứng + 20 can thiệp); MDE 6 điểm; n = 859 yc/nhóm; 3 luật dừng định lượng | Xong, có bằng chứng | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | Nếu xem lại 100% kéo dài: CPS tăng lên 11.743 đ (0,98×) đến 12.516 đ (1,04×); làm lại x2 tăng CPS lên 6.787 đ | Giả lập | PM trợ lý hoàn phí |

---

### Đề xuất: Go có điều kiện

Nhóm đề xuất phê duyệt triển khai pilot cho trợ lý hoàn phí trong phạm vi thu hẹp (`noi_dia` và `hang_nang` tại 6 depot thử nghiệm, giới hạn tối đa 2 lần chạy cho mỗi yêu cầu) với 4 điều kiện tiên quyết:

1. **Khắc phục lỗi ghi nhận sổ cái và chống hoàn trùng (Ca 7, Ca 20):** Bắt buộc tích hợp khóa chống trùng (idempotency key) và chỉ xác nhận hoàn phí khi có phản hồi `ok` từ hệ thống sổ cái trước ngày khởi động pilot.  
   *Người phụ trách:* Kỹ sư trưởng agent · *Thời hạn hoàn thành:* 2026-12-05.
2. **Ký duyệt văn bản chấp nhận đánh đổi cỡ mẫu và rủi ro thống kê:** Giám đốc vận hành phê duyệt văn bản chấp nhận MDE 6 điểm (cần 859 yêu cầu/nhóm; chấp nhận power giảm còn 0,64 nếu mức tác động thực tế chỉ đạt 5 điểm).  
   *Người phụ trách:* Giám đốc vận hành · *Thời hạn hoàn thành:* 2026-12-07.
3. **Kích hoạt hạ tầng ghi log 10 event có `trace_id`:** Triển khai đầy đủ các event định lượng thời gian thật (thay thế số đo phút giả lập bằng dữ liệu thực tế sau tuần chạy đầu tiên).  
   *Người phụ trách:* Kỹ sư trưởng agent · *Thời hạn hoàn thành:* 2026-12-08.
4. **Lộ trình giảm tỷ lệ nhân viên xem lại theo từng bước:** Thiết lập cơ chế giảm tỷ lệ xem lại từ 100% xuống dưới 30% khi tỷ lệ nhân viên sửa/bỏ gợi ý giảm xuống dưới 15% (nhằm tránh rủi ro chi phí vượt ngưỡng hòa vốn 12.000 đ như đã chỉ ra ở phân tích B4).  
   *Người phụ trách:* Trưởng nhóm CSKH · *Thời hạn hoàn thành:* 2026-12-10.
