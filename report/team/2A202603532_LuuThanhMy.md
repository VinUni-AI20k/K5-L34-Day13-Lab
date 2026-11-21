# Báo cáo cá nhân — Lưu Thanh Mỹ — 2A202603532

## 1. Thông tin thành viên

- Họ tên: Lưu Thanh Mỹ.
- MSSV: 2A202603532.
- Email: Data97688@gmail.com.
- GitHub: aialphaproduct.
- Nhóm: Stech · Lớp: L3A.
- Vai trong nhóm: Trưởng nhóm · Người viết code, phụ trách phần chính CP1–CP2.

## 2. Phần việc phụ trách

- Setup repo nhóm, điều phối phân công và cập nhật thông tin thành viên trong `TEAM.md`.
- Viết phần CP1 trong `src/lab13.py`: ba hàm A1, hàm `mo_hinh()` và tính chi phí từ trace cho A2–A3.
- Viết phần CP2 trong `src/lab13.py`: chín kịch bản B1, kịch bản đổi cặp và xếp hạng B2, giới hạn số lần chạy B3 và kịch bản xem lại 100% B4.
- Phối hợp với Nguyễn Thị Hồng Hạnh đối chiếu độc lập các số A1–B4 và sửa sai lệch được phát hiện trước khi merge.

## 3. Đóng góp cụ thể

- **A1:** cài đặt `so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`; ba phép thử đáp án biết trước đạt `1,20 · 1,25 · 1,25`.
- **A2:** xây dựng `mo_hinh()` cộng chi phí token, tool, xem lại và làm lại; tính được tổng chi phí **4.373.585 đ**, 978 việc thành công và chi phí mỗi việc thành công **4.472 đ** [simulated].
- **A3:** ban đầu gọi `mo_hinh()` với toàn bộ `runs` khi tách theo loại. Sau khi Hạnh kiểm số độc lập phát hiện sai lệch, đã sửa bằng cách lọc `runs` theo `request_id` của từng loại; kết quả khớp bảng kiểm số: `noi_dia` 2.696 đ, `hang_nang` 8.221 đ, `quoc_te` 22.515 đ, `doi_tac` 10.215 đ [simulated].
- **B1–B3:** cài đặt đủ chín kịch bản độ nhạy, xếp hạng ba yếu tố ảnh hưởng mạnh nhất và tính chi phí cả hệ thống; xác định giới hạn 2 lần chạy rẻ nhất cho công ty ở **6.901.220 đ** [simulated].
- **B4:** cài đặt kịch bản xem lại 100% cho `noi_dia + hang_nang`. Khi review, nhóm phát hiện khác biệt giữa 982 yêu cầu trong phạm vi và 948 yêu cầu có ít nhất một lần chạy `ok`; đã ghi rõ hai cách tính để tiếp tục sửa code cho khớp số chuẩn 11.743 đ [simulated].

## 4. Bằng chứng

- Pull Request **#12**: `CP1+CP2: mo hinh chi phi + bang do nhay (My)`.
- Commit `0b072b7`: hoàn thành mô hình chi phí CP1 và bảng độ nhạy CP2.
- Commit `235a91d`: sửa lỗi A3 sau khi đối chiếu độc lập, lọc `runs` đúng theo từng loại yêu cầu.
- File chính: `src/lab13.py`; file đối chiếu: `report/team/bang_chi_phi.md`.

## 5. Công cụ AI đã dùng

- Sử dụng **Claude Sonnet/Claude Code** để hỗ trợ diễn giải công thức, viết cấu trúc Python và rà soát các kịch bản độ nhạy.
- Tự kiểm tra bằng ba phép thử A1, đối chiếu output với bảng tính độc lập của Hạnh và tài liệu `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`.
- Khi kết quả A3 không khớp, kiểm tra lại phạm vi `request_id`, sửa code và chỉ chấp nhận kết quả sau khi bốn loại yêu cầu khớp bảng kiểm số.

## 6. Tự đánh giá

- Hoàn thành phần code chính CP1–CP2 và phản hồi nhanh khi kiểm số phát hiện lỗi A3; việc phối hợp code–kiểm số giúp tránh đưa số sai vào hồ sơ.
- Cần cải thiện: chốt cách hiểu B4 trước khi viết code và bổ sung kiểm thử tự động cho phạm vi dữ liệu, đặc biệt khi hàm được gọi trên tập con theo loại yêu cầu.
