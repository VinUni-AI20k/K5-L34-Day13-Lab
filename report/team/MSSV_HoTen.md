# Báo cáo cá nhân — HoVaTen-MSSV

Copy file này và đổi tên theo quy tắc `MSSV_HoTen.md`. Giữ nguyên file mẫu.

Ví dụ: `20241234_NguyenVanAn.md`.

## 1. Thông tin thành viên

- Họ tên: Nguyễn Thị Thanh Thúy
- MSSV: 2A202603523
- Email: (cần bổ sung)
- Vai trong nhóm: Người viết code — phụ trách mô hình chi phí A1–A4; hỗ trợ B khi được phân công.

## 2. Phần việc phụ trách

Phụ trách hoàn thiện `src/lab13.py` cho Checkpoint 1 (A1–A4) và Checkpoint 2 (B1–B4). Cập nhật các bảng chi phí/độ nhạy trong `report/team/bang_chi_phi.md`; bổ sung rủi ro kinh tế từ kết quả B vào `chi_so.md`, đồng thời cập nhật `ho_so_launch_v0.md` và `group_report.md`.

## 3. Đóng góp cụ thể

Triển khai phép tính từ toàn bộ trace, kể cả lần chạy lỗi; tính chi phí xem lại/làm lại từ các cột `*_simulated`; chỉ đếm `ket_qua == 'thanh_cong'` làm mẫu số CPS. Phân tích 4 loại yêu cầu và phạm vi pilot `noi_dia` + `hang_nang`. Với CP2, chạy 9 kịch bản B1, kịch bản ghép B2, so sánh chi phí trợ lý/toàn hệ thống ở B3 và mô hình hoá 100% xem lại ở B4. Chạy `python lab13.py`, xác nhận ba phép thử A1 đạt và đối chiếu đầu ra B1–B4 với hướng dẫn lab.

## 4. Bằng chứng

Commit, file, bảng hoặc con số do bạn làm.

`src/lab13.py`; `report/team/bang_chi_phi.md`; `report/team/chi_so.md`; `report/team/ho_so_launch_v0.md`; `report/team/group_report.md`. Các commit đã đẩy lên nhánh `thanhthuy`: `7d259a4` (mô hình A1–A4) và `83d5b61` (hoàn tất Checkpoint 1); phần CP2 đang ở working tree, chưa commit. Kết quả chính: A2 4.472 đ/việc; A4 4.599 đ/việc ở quy mô đầy đủ; B2 xếp hạng làm lại (51,8%), xem lại (40,7%), lương (23,1%); B3 chọn giới hạn 2 lần theo tổng chi phí hệ thống (6.901.220 đ); B4 11.743–12.415 đ/việc tuỳ giả định thời gian làm lại. Các chi phí nhân viên giả lập gắn nhãn `simulated`.

## 5. Công cụ AI đã dùng

Công cụ nào, dùng vào việc gì, bạn tự kiểm tra kết quả ra sao.

Đã dùng Codex để đọc yêu cầu, triển khai và cập nhật báo cáo. Tôi tự kiểm tra bằng cách chạy chương trình trên CSV của lab, xác nhận ba phép thử A1 đạt, đối chiếu 9 kịch bản B1, tổng chi phí B3 và hai giả định B4 với hướng dẫn. Báo cáo CP1 đã commit; các cập nhật CP2 hiện chưa được commit.

## 6. Tự đánh giá

Hoàn thành code và báo cáo A/B, phân biệt CPS của trợ lý với tổng chi phí hệ thống ở B3, đồng thời ghi rõ các giả định `simulated` ở B4. Tôi cần bổ sung thông tin cá nhân ở mục 1; các phần C–E thuộc phạm vi thành viên khác.
