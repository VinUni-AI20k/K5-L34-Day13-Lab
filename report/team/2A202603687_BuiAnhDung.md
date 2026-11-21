# Báo cáo cá nhân — HoVaTen-MSSV

Copy file này và đổi tên theo quy tắc `MSSV_HoTen.md`. Giữ nguyên file mẫu.

Ví dụ: `20241234_NguyenVanAn.md`.

## 1. Thông tin thành viên

- Họ tên: Bùi Anh Dũng
- MSSV: 2A202603687
- Email:26ai.dungba2@vinuni.edu.vn
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): Người viết code (trước giờ giải lao), sau giải lao chuyển sang người kiểm số. Nhóm 3 người: Bùi Anh Dũng, Phụng, Thanh.

## 2. Phần việc phụ trách

- Nhiệm vụ A (CP1): mô hình chi phí mỗi việc thành công trong `src/lab13.py`: ba hàm A1, hàm `mo_hinh`, bảng A3 theo loại yêu cầu, A4 chi phí cố định.
- Nhiệm vụ B (CP2, CP3): bảng độ nhạy B1, B2, B3, B4.
- Nhiệm vụ E1, E2: tính thử ba chỉ số và lấy số cho các dòng rủi ro kinh tế trong `chi_so.md`.
- Sau giải lao: kiểm số phần D do Phụng viết (cỡ mẫu, `pilot_plan.yaml`).

## 3. Đóng góp cụ thể

- Viết `so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`; ba phép thử đáp án biết trước in ĐẠT (1,20 · 1,25 · 1,25).
- Viết `mo_hinh(runs, reqs, ...)`: tử số cộng mọi lần chạy kể cả lần lỗi, mẫu số chỉ đếm `ket_qua == 'thanh_cong'`; có tham số giá, hệ số và `max_lan_chay` để chạy lại cho nhiệm vụ B.
- Thêm các hàm in bảng A, B và chỉ số E1 vào `lab13.py`; `python lab13.py` chạy hết từ đầu đến cuối.
- Điền `report/team/bang_chi_phi.md` (A1–A4, B1–B4) và `report/team/chi_so.md` (E1, danh sách event, E2). Mọi số từ cột `_simulated` có nhãn simulated.

## 4. Bằng chứng

- File: `src/lab13.py`, `report/team/bang_chi_phi.md`, `report/team/chi_so.md`.
- Số chính (simulated): chi phí mỗi việc thành công 4.472 đ, gấp 16,3 lần hoá đơn token chia số yêu cầu (274,7 đ); chi phí cả hệ thống 0,49× của 12.000 đ.
- `quoc_te` 1,88× và thành công 27,3%, chạy lại không giúp (ok theo lần thử 30,0% → 11,4% → 2,2%).
- Ba yếu tố nhạy nhất: số ca làm lại (+51,8%), tỉ lệ xem lại (+40,7%), lương nhân viên (+23,1%).
- Giới hạn 2 lần chạy rẻ nhất cho công ty (6.901.220 đ); xem lại 100% cho 11.743 đ = 0,98× (12.415 đ = 1,03× nếu làm lại 15,3 phút).
- Chỉ số tính thử: chính 82,83% (994/1.200), dùng 27,12% (48/177), an toàn 4,25% (51/1.200).
- Commit: điền mã commit sau khi commit.

## 5. Công cụ AI đã dùng

- Claude Code: giúp đọc đề và các file checkpoint, hướng dẫn viết code A, B, E1 trong `lab13.py`
- Cách kiểm tra kết quả:
  - Chạy `python lab13.py`, ba phép thử A1 in ĐẠT.
  - Đối chiếu số A2, A3, A4, B1–B4 với số tham khảo trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`; tất cả khớp, trong sai số 2%. Riêng dòng B4 theo dữ liệu ra 12.415 đ so với 12.414 đ trong hướng dẫn, chênh do làm tròn.
  - Kiểm "giảm một nửa" bằng nửa mức tăng của "gấp đôi" (5,6 → 2,8; 40,7 → 20,3; 51,8 → 25,9) và B2 bằng tổng hai tác động riêng (5,6 + 40,7 = 46,3).

## 6. Tự đánh giá

- Làm được: A1, A2, A3, A4, B1–B4 và E1, E2 chạy được, số khớp số tham khảo, có nhãn simulated.
- Hạn chế: số đối chiếu chỉ lấy từ hướng dẫn, chưa có đáp án gốc khác; phần event trong `chi_so.md` mới được soạn, cần Phụng soát lại.
- Cần hiểu rõ khi bảo vệ: vì sao tử số tính mọi lần chạy còn mẫu số chỉ đếm việc thành công; vì sao giới hạn 2 lần rẻ nhất cho công ty nhưng không trùng với giới hạn cho chi phí mỗi việc thành công thấp nhất.
