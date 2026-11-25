# Báo cáo cá nhân — NguyenAnhDuong-2A202604087

## 1. Thông tin thành viên

- Họ tên: Nguyễn Ánh Dương
- MSSV: 2A202604087
- Email: <anhduongn724@gmail.com>
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): người gắn nhãn 1 · Error & Metrics Analyst

## 2. Phần việc phụ trách

- CP3 · Nhiệm vụ C: sở hữu `report/team/bang_loi.md` (gắn nhãn độc lập 20 ca với vai người gắn nhãn 1, so nhãn với Trần Việt Anh, bảng khắc phục 5 ca).
- CP5 · Nhiệm vụ E1, E2: sở hữu `report/team/chi_so.md` (tính thử 3 chỉ số, đề xuất thêm chỉ số dùng và an toàn, 10 event có `trace_id`, ghép rủi ro kinh tế do Nguyễn Văn Hải Quân gửi).
- Duyệt chéo Gate 2a: giải trình phân loại lỗi, cơ chế chuyển nhân viên và hệ thống event/KPI; chấm mảng lỗi và chỉ số của nhóm n + 1.

## 3. Đóng góp cụ thể

- Khai thác dữ liệu lỗi từ 2 file CSV: 572/1.624 lần chạy lỗi (35,2%), 424 lần chạy lại tốn 93.804 đ, riêng quoc_te chiếm 46.218 đ (49%).
- Chỉ ra quoc_te không cứu được bằng chạy lại: tỉ lệ ok lần 1 là 30%, lần 2 là 11,4%, lần 3 là 2,2%.
- Phát hiện cả 51 ca mở lại trong 7 ngày đều là ca `lam_lai` (69% số ca làm lại), nên giảm làm lại là đòn bẩy chính cho chỉ số an toàn.
- Tính thử 3 chỉ số: chính 82,83% (994/1.200), bỏ qua gợi ý 27,12% (48/177), lỗi lọt đến khách 4,25% (51/1.200); kèm số trong phạm vi noi_dia + hang_nang (92,26%, 21,09%, 3,97%).
- Đề xuất 4 chỉ số bổ sung (2 dùng, 2 an toàn), thiết kế 10 event, kiểm tra chéo để mọi chỉ số đều tính được từ event.
- E2: ghép 4 dòng rủi ro kinh tế theo bàn giao của Nguyễn Văn Hải Quân (làm lại gấp đôi, xem lại 100%, khối lượng thấp, lương tăng 25%), số khớp `bang_chi_phi.md`.
- Gắn nhãn độc lập 20 ca bằng tay: sau khi so, bộ nhãn của tôi khớp nhãn tham khảo 17/20 (lệch ca 7, 15, 20). Đồng thuận với người gắn nhãn 2 ghi trong `bang_loi.md`.

## 4. Bằng chứng

- `report/team/bang_loi.md`: cột nhãn người 1, quy tắc phân biệt, bảng "Tác động định lượng của lỗi", bảng khắc phục 5 ca (ca 1, 2, 3, 11, 12).
- `report/team/chi_so.md`: bảng E1 (7 chỉ số), bảng 10 event, mục kiểm tra chéo, bảng E2 (4 rủi ro).
- Commit trên nhánh `feat/cp3-cp5-anhduong` (PR #2): `02d0f79` (bản đầu) và commit hoàn thiện theo góp ý của trưởng nhóm.

## 5. Công cụ AI đã dùng

- Claude Code: đọc đề và tài liệu trong repo, viết script nháp pandas (để ngoài repo, không commit) để tính các chỉ số, soạn khung bảng event và bảng khắc phục.
- Không dùng AI để gắn nhãn 20 ca: nhãn của tôi được gắn tay, độc lập, trước khi so với người gắn nhãn 2 và với nhãn tham khảo.
- Tự kiểm tra: đối chiếu từng con số với số tham chiếu trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` và `bang_chi_phi.md` (994/1.200, 48/177, 51/1.200, 4.472 đ [simulated], B4 11.743 đ [simulated], 12.415 đ [simulated]), tất cả khớp.

## 6. Tự đánh giá

- Làm tốt: các chỉ số đều có con số và event để đo; bảng lỗi nối được với chi phí (làm lại chiếm 51,8% tổng chi phí [simulated]).
- Cần cải thiện: tôi nhầm Giới hạn hệ thống với Hệ thống ở 3/20 ca (7, 15, 20). Bài học: nếu sửa code hoặc quy trình là làm đúng được thì đó là lỗi Hệ thống, không phải Giới hạn.
