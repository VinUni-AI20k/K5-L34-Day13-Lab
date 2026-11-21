# Báo cáo cá nhân — LucAnhTuan-2A202603634

## 1. Thông tin thành viên

- Họ tên: Lục Anh Tuấn
- MSSV: 2A202603634
- Email: 26ai.tuanla2@vinuni.edu.vn
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): Người viết code

## 2. Phần việc phụ trách

- Viết và chạy `src/lab13.py` cho nhiệm vụ A (A1–A4), B (B1–B4) và D1, kèm các số phụ trợ cho D3 (tỉ lệ mở lại hiện tại) và E1 (ba chỉ số tính thử).
- Điền số vào `report/team/bang_chi_phi.md` (cùng người kiểm số) và phần chú thích D1 trong `report/team/pilot_plan.yaml`.

## 3. Đóng góp cụ thể

- A1: ba hàm `so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`; ba phép thử ĐẠT (1,20 · 1,25 · 1,25).
- A2: hàm `mo_hinh` tính token + tool trên mọi lần chạy, tiền xem lại và làm lại (simulated), chia cho số việc thành công; có tham số giá, hệ số và `max_lan_chay` để B gọi lại.
- A3, A4: tách theo `loai`, tỉ lệ ok theo từng lần thử, cộng chi phí cố định 40 triệu đ/tháng cho phạm vi noi_dia + hang_nang.
- B1–B4: 9 kịch bản độ nhạy, cặp token + xem lại, chi phí cả hệ thống theo giới hạn 1/2/3 lần chạy, kịch bản xem lại 100% kèm mức hoà vốn.
- D1: hàm `co_mau`, `he_so_thiet_ke`, `co_mau_hieu_dung`, `m_toi_thieu`; power khi thiết kế cho 6 điểm mà tác động thật là 5 điểm.

## 4. Bằng chứng

- `src/lab13.py` chạy từ đầu đến cuối bằng `python lab13.py` trong `src/`.
- Số chính: chi phí mỗi việc thành công 4.472 đ [simulated], gấp 16,3 lần hoá đơn token + tool chia số yêu cầu (274,7 đ); quoc_te 22.515 đ = 1,88× [simulated]; giới hạn 2 lần chạy rẻ nhất cho cả hệ thống (6.901.220 đ) [simulated]; cỡ mẫu 1.251 yêu cầu mỗi nhóm, 20 nhân viên mỗi nhóm cần m ≥ 299 cho mức chênh 6 điểm.
- Commit trên nhánh `feature/tuanvtxm6`, merge vào `main`.

## 5. Công cụ AI đã dùng

- Claude Code (Claude): dùng để viết khung code A–D trong `src/lab13.py`, định dạng bảng in ra và điền số vào `bang_chi_phi.md`.
- Cách tự kiểm tra: ba phép thử A1 phải ĐẠT trước khi chạy tiếp; đối chiếu từng con số A2, A3, B1, B3, B4, D1 với bảng số tự đối chiếu trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (đều lệch dưới 2%); kiểm tra "giảm một nửa" bằng đúng nửa "gấp đôi" ở B1, và cặp B2 bằng tổng hai tác động riêng.

## 6. Tự đánh giá

- **Làm tốt:** `src/lab13.py` chạy từ đầu đến cuối, ba phép thử A1 ĐẠT; các số A2, A3, B1, B3, B4, D1 khớp bảng đối chiếu (lệch dưới 2%). Mọi số từ cột `_simulated` đều có nhãn simulated. Hàm `mo_hinh` nhận tham số nên B chỉ cần gọi lại, không phải chép code.
- **Điều rút ra:** chi phí thật nằm ở giờ nhân viên (92,5% tổng, simulated) chứ không ở token (5,6%). Chạy lại nhiều hơn không phải lúc nào cũng tốt: với quoc_te, lần 3 chỉ đúng 2,2%. Giới hạn rẻ nhất cho công ty (2 lần) khác giới hạn cho chi phí mỗi việc thành công thấp nhất (1 lần).
- **Chưa tốt:** phần lớn code viết cùng Claude Code, nên tôi phải tự đọc lại `mo_hinh` và `co_mau` để giải thích được trước hội đồng. Tôi làm luôn D1 thay vì đổi người viết code sau giờ giải lao như hướng dẫn. Nhóm cần một bạn khác tự tính lại D1 và một con số A2 để đối chiếu.
- **Lần sau:** chia nhỏ commit theo từng checkpoint để có bằng chứng tiến độ rõ hơn; nhờ người kiểm số tính tay trước khi điền bảng.
