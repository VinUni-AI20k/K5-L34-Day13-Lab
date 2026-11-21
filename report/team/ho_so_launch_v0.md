# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Gate 2a chỉ duyệt kế hoạch pilot.

Nhóm: NguyenTuanBach · Lớp: L3A

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ [simulated], gấp 16,3× hoá đơn token + tool chia số yêu cầu (274,7 đ); giờ nhân viên chiếm 92,5%. Cộng cố định 40 triệu đ/tháng, phạm vi noi_dia + hang_nang: 4.599 đ ở 45.000 yêu cầu/tháng, 5.784 đ ở một nửa | Giả lập | Người viết code |
| 2 · Ba yếu tố nhạy nhất | 1. số ca làm lại ±51,8% · 2. tỉ lệ xem lại ±40,7% · 3. lương nhân viên +23,1% (giá token chỉ +5,6%) [simulated] | Giả lập | Người kiểm số |
| 3 · So với nhân viên tự làm | Cả hệ thống 5.865 đ/yêu cầu = 0,49× của 12.000 đ [simulated]. Theo loại: noi_dia 0,22×, hang_nang 0,69×, doi_tac 0,85×, quoc_te 1,88× (đắt hơn nhân viên). Xem lại 100%: 0,98× đến 1,04× | Giả lập | Người kiểm số |
| 4 · Chỉ số chính, dùng, an toàn | Chỉ số trong đợt chạy thử là: chính 82,83% (994/1.200) · bỏ qua gợi ý 27,12% (48/177) · mở lại 7 ngày 4,25% (51/1.200). Không có đối chứng nên chưa kết luận trợ lý nâng chỉ số | Xong, có bằng chứng | Người giữ hồ sơ |
| 5 · Bảng lỗi và cách khắc phục | 20 ca gắn nhãn (4 · 5 · 4 · 4 · 3 theo năm loại); bảng khắc phục đủ 5 ca, 5 loại. Đồng thuận 20/20 (xem `bang_loi.md`) | Xong, có bằng chứng | Người gắn nhãn 1 |
| 6 · Pilot plan | Chia theo nhân viên 20 + 20, ngẫu nhiên; mức chênh 6 điểm (859/nhóm; power 0,64 nếu tác động thật 5 điểm); 3 luật dừng; ngày quyết định 2027-01-05 | Xong, có bằng chứng | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Làm lại gấp đôi: 6.787 đ (+51,8%) · xem lại 100% kéo dài: 11.743–12.516 đ (0,98–1,04×) · khối lượng một nửa: cố định +2.370 đ/việc [simulated] | Giả lập | PM trợ lý hoàn phí |

**Đề xuất: Go có điều kiện** cho pilot chỉ noi_dia + hang_nang (không quoc_te, không doi_tac). Con số bất lợi: xem lại 100% gần bằng nhân viên tự làm (0,98×–1,04×), cỡ mẫu không đủ để thấy mức chênh 5 điểm, mở lại 7 ngày hiện 4,25%. Điều kiện:

- Sửa khoá chống trùng và đối soát sổ cái (ca 7, 20) trước ngày bắt đầu. Phụ trách: Kỹ sư trưởng agent. Kiểm tra: trước ngày bắt đầu pilot.
- Giám đốc vận hành ký chấp nhận mức chênh 6 điểm. Phụ trách: Giám đốc vận hành LogiX-VN. Kiểm tra: trước ngày bắt đầu pilot.
- Bật đủ event có `trace_id` và thay phút simulated bằng phút đo thật. Phụ trách: PM trợ lý hoàn phí. Kiểm tra: sau tuần 1 của pilot.
- Có kế hoạch giảm xem lại theo bậc, vì xem lại 100% không tiết kiệm. Phụ trách: Trưởng nhóm CSKH. Kiểm tra: cuối bước rollout 0.25.
