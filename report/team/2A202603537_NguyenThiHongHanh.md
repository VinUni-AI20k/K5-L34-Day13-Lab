# Báo cáo cá nhân — NguyenThiHongHanh-2A202603537

## 1. Thông tin thành viên

- Họ tên: Nguyễn Thị Hồng Hạnh
- MSSV: 2A202603537
- Email: 26ai.hanhnth2@vinuni.edu.vn
- Vai trong nhóm: Người kiểm số (phần chính CP1 + CP2, làm với Mỹ là người viết code)

## 2. Phần việc phụ trách

- Tính độc lập chi phí mỗi việc thành công để đối chiếu với `src/lab13.py` của Mỹ (lệch không quá 2%).
- Điền đầy đủ `report/team/bang_chi_phi.md`: A1, A2, A3, A4, B1, B2, B3, B4 (issue #2).
- Review lại toàn bộ `bang_chi_phi.md` trước khi nộp.

## 3. Đóng góp cụ thể

- Điền bảng A2 đủ 9 dòng (hai dòng xem lại / làm lại có nhãn `simulated`), A3 đủ 4 loại, A4 hai mức khối lượng, B1 đủ 9 kịch bản, B2 đổi cặp và xếp hạng, B3 ba giới hạn, B4 hai mức phút làm lại.
- Tính tay loại `noi_dia` để đối chiếu: (77.002 + 53.985 + 47.700 + 942.000 + 990.000) ÷ 783 = **2.696 đ** [simulated].
- **Phát hiện lỗi trong code A3** của Mỹ nhờ đối chiếu: code cũ không lọc lần chạy theo loại, `noi_dia` ra 2.888 đ thay vì 2.696 đ, `doi_tac` lệch tới 80%. Mỹ đã sửa trong PR #12 (commit `235a91d`), sau khi sửa khớp 100%.
- Đối chiếu output `lab13.py` (PR #12): A2, A3, B1, B2 (cặp), B3 khớp từng đồng. Báo thêm hạng 3 trong xếp hạng B2 bị trùng yếu tố "làm lại"; hạng 3 đúng là lương nhân viên (+23,1%).
- B4: cách hiểu khác với code — chỉ xem lại 948 ca có câu trả lời và chia 900 việc thành công (11.743 đ = 0,98×), code xem lại 982 và chia 934 (11.679 đ = 0,97×). Lệch 0,55%, nhóm thống nhất ghi cả hai số và lý do vào B4.

## 4. Bằng chứng

- PR #9 (đã merge): `bang_chi_phi.md` A1–B4, ba commit `d13d616`, `032c09f`, `b15beee`.
- Nhánh `fix/b4-doi-chieu`, commit `54fdd24`: ghi đối chiếu B4 với code.
- Bình luận của Mỹ trên PR #9 và PR #12 xác nhận lỗi A3 được phát hiện qua đối chiếu với bảng kiểm số.
- Số chính: chi phí mỗi việc thành công 4.472 đ [simulated], gấp 16,3 lần hoá đơn token chia số yêu cầu (274,7 đ); giới hạn 2 lần chạy rẻ nhất cho công ty (6.901.220 đ [simulated]).

## 5. Công cụ AI đã dùng

- **Claude Code**: đọc đề, viết một script Python riêng (không dùng pandas, không dùng `lab13.py`) đọc thẳng hai file CSV để tính các bảng A và B, giải thích công thức.
- Tự kiểm tra: (1) so mọi số với số đối chiếu trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` — lệch dưới 0,1%; (2) so với output `lab13.py` của Mỹ — chính phép so này bắt được lỗi A3; (3) đọc lại đề B4 từng câu để xác định 948 / 900; (4) tự kiểm tra B1: mỗi kịch bản "giảm một nửa" giảm đúng nửa mức tăng của "gấp đôi"; (5) tự tính tay bên ngoài để đối chiếu với kết quả script, ví dụ loại `noi_dia` ra 2.696 đ.

## 6. Tự đánh giá

- Làm tốt: hoàn thành đủ bảng chi phí trước khi code chạy xong; kiểm số độc lập phát hiện được một lỗi thật, giúp A3 của nhóm từ lệch 7–80% về khớp 100%.
- Cần cải thiện: nên chốt sớm cách hiểu đề B4 với người viết code ngay từ đầu, để tránh hai số khác nhau (11.743 đ và 11.679 đ) phải giải thích lúc cuối.
