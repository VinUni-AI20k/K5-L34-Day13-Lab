# Báo cáo cá nhân — NguyenMinhPhuc-MSSV

## 1. Thông tin thành viên

- Họ tên: Nguyễn Minh Phúc
- MSSV:
- Email:
- Vai trong nhóm: người kiểm số (Thành viên 3 theo bảng phân công của nhóm)

## 2. Phần việc phụ trách

- **CP1 · A3:** tách chi phí mỗi việc thành công theo 4 loại yêu cầu; kết luận loại nào không đáng giao cho trợ lý.
- **CP2 · B3:** giới hạn chạy lại 1, 2, 3 lần; tính tổng chi phí cả hệ thống.
- **CP3:** tính tỉ lệ đồng thuận giữa hai bộ nhãn, điều phối thống nhất ca bất đồng, giữ `bang_loi.md`. Phần này còn chờ hai bộ nhãn độc lập của TV1 và TV2.
- **CP4 · D1(e), D2:** cỡ mẫu với mức chênh 6 điểm; năm câu "tách được tác động".
- **CP5:** chỉ số an toàn, đề xuất thêm một chỉ số an toàn, viết bảng rủi ro kinh tế E2.

## 3. Đóng góp cụ thể

- **A3** [simulated]: chi phí mỗi việc thành công là noi_dia 2.696 đ (0,22×), hang_nang 8.221 đ (0,69×), quoc_te 22.515 đ (1,88×), doi_tac 10.215 đ (0,85×). Đề xuất phạm vi pilot noi_dia + hang_nang (982/1.200 yêu cầu). Với quoc_te, tỉ lệ lần chạy `ok` giảm dần qua các lần thử (30,0% → 11,4% → 2,2%), nên chạy lại không giúp được.
- **B3** [simulated]: giới hạn 2 lần rẻ nhất cho công ty, tổng cả hệ thống 6.901.220 đ. Giới hạn 1 lần cho chi phí mỗi việc thành công thấp nhất (4.111 đ) nhưng đẩy thêm 85 việc sang nhân viên.
- **D1(e):** 859 yêu cầu mỗi nhóm, hệ số thiết kế 6,96, cần m ≥ 299 yêu cầu mỗi nhân viên. Con số bất lợi: nếu tác động thật chỉ 5 điểm thì power còn khoảng 0,64.
- **Chỉ số an toàn:** tỉ lệ mở lại trong 7 ngày là 4,25% toàn mẫu và 3,97% trong phạm vi pilot. Riêng hang_nang là 8,23%, vượt trần 6%.
- **Đề xuất thêm:** tỉ lệ mở lại 7 ngày ở ca không được xem lại, hiện là 4,99%.
- **E2 · Rủi ro kinh tế** [simulated], 3 dòng:
  - làm lại gấp đôi: +51,8%, lên 6.787 đ
  - xem lại 100%: 11.743 đ = 0,98× baseline
  - khối lượng thấp hơn dự kiến: hoà vốn ở khoảng 6.212 yêu cầu/tháng
- **Kiểm số chéo:** B3 của mình khớp từng đồng với `in_kich_ban_b` do TV1 viết trong `src/lab13.py`.

## 4. Bằng chứng

- Script: `src/tv3_tinh_so.py`. Chạy trong `src/` bằng lệnh `python tv3_tinh_so.py`.
- File bàn giao: `report/team/tv3_ban_giao.md`. Phần A3 và B3 gửi TV2, phần D1(e), D2, chỉ số an toàn và E2 gửi TV4.
- Commit `b06edcb` (A3, B3, D1(e), D2, chỉ số an toàn), merge qua PR #3.
- Commit `0fea896` (E2 rủi ro kinh tế), merge qua PR #6.

## 5. Công cụ AI đã dùng

- **Claude Code** (trợ lý lập trình trong VS Code) dùng để:
  - tóm tắt đề và bảng phân công
  - viết `src/tv3_tinh_so.py`
  - chạy script để ra số
  - soạn file bàn giao
  - theo dõi commit của nhóm để biết khi nào phần việc phụ thuộc làm được
- **Mọi số đều do code chạy ra**, gọi lại `mo_hinh` trong `src/lab13.py` của nhóm. AI không tự điền số và không gắn nhãn lỗi thay người gắn nhãn.
- **Cách tự kiểm tra:**
  - so mọi số với số tham chiếu trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`, lệch 0%
  - so B3 với output độc lập của TV1
  - kiểm tra lại D1(e) bằng công thức tay (20m ≥ 859 × (0,98 + 0,02m))
  - chạy lệnh grep tìm từ cấm theo checklist CP5, kết quả rỗng

## 6. Tự đánh giá

- **Đã xong:** A3, B3, D1(e), D2, chỉ số an toàn, E2. Tất cả có số, nhãn `simulated` và đã bàn giao cho người giữ file.
- **Chưa xong:** CP3 (đồng thuận và quy tắc cho ca bất đồng), vì còn chờ hai bộ nhãn độc lập.
- **Điểm cần học thêm:** phần lớn code do AI viết. Mình cần tự giải thích được hai điều trước hội đồng:
  - vì sao tử số chi phí tính mọi lần chạy, còn mẫu số chỉ đếm việc thành công
  - cách tính hệ số thiết kế 1 + (m − 1) × ICC
