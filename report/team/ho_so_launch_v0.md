# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

**Bản nháp hồ sơ theo số đối chiếu trong hướng dẫn lab; nhóm cần xác nhận các số với output `src/lab13.py` và hoàn thiện các trường còn phụ thuộc dữ liệu/nhãn thực tế.** Cột trạng thái chỉ dùng: Xong, có bằng chứng · Chưa · Giả lập. Các số từ phút `_simulated` được gắn nhãn.

Nhóm: DTL · Lớp: L3A

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ/việc thành công; 5.865 đ/yêu cầu tính cả phần 222 ca nhân viên làm thay; các số có phần phút simulated | Giả lập | Người kiểm số |
| 2 · Ba yếu tố nhạy nhất | Ca làm lại tăng gấp đôi: +51,8% (6.787 đ); xem lại tăng gấp đôi: +40,7% (6.292 đ); lương tăng 25%: +23,1% (5.506 đ) | Giả lập | Người kiểm số |
| 3 · So với nhân viên tự làm | Chi phí toàn hệ thống mẫu 5.865 đ/yêu cầu, so với 12.000 đ tự làm; phạm vi nội địa + hàng nặng sau phân bổ định phí: 4.599 đ/việc ở 45.000 yêu cầu/tháng, 5.784 đ nếu còn nửa khối lượng | Giả lập | Người kiểm số |
| 4 · Chỉ số chính, dùng, an toàn | Chỉ số trong đợt chạy thử (không có đối chứng, chưa suy ra tác động nhân quả): chính 82,83% (994/1.200); bỏ qua gợi ý 27,12% (48/177); mở lại 7 ngày 4,25% (51/1.200). Thêm chỉ số dùng (tỉ lệ yêu cầu có mở gợi ý) và chỉ số an toàn (hoàn trùng hoặc sai số tiền, ngưỡng 0 ca); 8 event có trace_id trong chi_so.md | Xong, có bằng chứng | Người gắn nhãn 2 kiêm giữ hồ sơ |
| 5 · Bảng lỗi và cách khắc phục | 20 ca thuộc 5 loại; hai bộ nhãn độc lập trùng 20/20 (100%); bảng khắc phục 5 ca đủ năm loại, mỗi dòng có cách phát hiện đo được và vai trò phụ trách | Xong, có bằng chứng | Người gắn nhãn 2 kiêm giữ hồ sơ |
| 6 · Pilot plan | Chỉ nội địa + hàng nặng; chia ngẫu nhiên theo nhân viên 20/20, MDE 6 điểm, 859 yêu cầu/nhóm; giảm xem lại theo bậc và có luật dừng | Giả lập | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Xem lại 100%: 11.743 đ/việc (0,98×) theo giả định 9 phút làm lại; 12.415 đ (1,03×) nếu dùng trung bình simulated 15,3 phút làm lại | Giả lập | PM trợ lý hoàn phí |

**Đề xuất: Go có điều kiện cho pilot giới hạn ở nội địa và hàng nặng; chưa phải phê duyệt vận hành chính thức.** Điều kiện: (1) Kỹ sư trưởng agent sửa chống hoàn trùng và đối soát sổ cái trước ngày bắt đầu; (2) Giám đốc vận hành chấp nhận MDE 6 điểm vì mức chênh thật 5 điểm chỉ đạt power khoảng 0,64 theo hướng dẫn; (3) PM trợ lý hoàn phí bật event có `trace_id` và thay thời lượng simulated bằng đo thật sau tuần đầu; (4) Trưởng nhóm CSKH đặt lộ trình giảm xem lại, vì xem lại 100% có thể lên 12.415 đ/việc với thời lượng làm lại theo dữ liệu simulated. Ngày kiểm tra/ra quyết định cần được nhóm điền trước khi pilot; ngày 2027-01-05 trong ví dụ hướng dẫn chỉ là giá trị mẫu, chưa xác nhận cho nhóm.
