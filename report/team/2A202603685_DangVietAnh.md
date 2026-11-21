# Báo cáo cá nhân — Đặng Việt Anh (2A202603685)

## 1. Thông tin thành viên

- Họ tên: Đặng Việt Anh
- MSSV: 2A202603685
- Email: vietanh.dang282@gmail.com
- Vai trong nhóm: Người viết code (giai đoạn 14:00–15:20, nhiệm vụ A). Sau giải lao bàn giao code cho thành viên khác theo kế hoạch nhóm.

## 2. Phần việc phụ trách

- Nhiệm vụ A (CP1): viết ba hàm A1 trong `src/lab13.py`, hàm `mo_hinh` (A2), vòng lặp A3 và phần A4 (chi phí cố định).
- Nhiệm vụ B (CP2): bảng độ nhạy trong `src/lab13.py` (B1 đổi từng yếu tố, B2 đổi cặp và xếp hạng, B3 giới hạn chạy lại, B4 xem lại 100%) và điền B1–B4 trong `bang_chi_phi.md`.
- Điền `report/team/bang_chi_phi.md` cho A1–B4 (phần kiểm số tính tay do người kiểm số thực hiện).
- Viết báo cáo cá nhân này.

## 3. Đóng góp cụ thể

- Commit `54b87ae`: ba hàm A1 (`so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`). Phép thử ĐẠT (1,20 · 1,25 · 1,25).
- Commit `7715c86` (đã merge qua PR #1, `ecc033a`): hàm `mo_hinh`, trả về các khoá token, tool, chay_lai, xem_lai, lam_lai, tong, thanh_cong, cps, hoa_don_moi_yc, và hỗ trợ `max_lan_chay` cho nhiệm vụ B.
- Commit `490bac8` (đã merge qua PR #2, `fd71273`): A3 (bảng theo loại), A4 (chi phí cố định), điền A1–A4 trong `bang_chi_phi.md`.
- Commit `199d9e2` (nhánh `feat/cp2-bang-do-nhay`, đã merge vào `main` qua commit `6d7b97d`): B1–B4 trong `lab13.py`, điền B1–B4 trong `bang_chi_phi.md`.
- Đối chiếu số A2, A3, A4, B1–B3 với bảng trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`. B4 khớp đáp án với cách tính phút làm lại 15,3 phút/ca (trung bình toàn bộ ca làm lại). Ban đầu tôi tính trung bình chỉ trong phạm vi và được 16,2 phút, đã sửa theo hướng dẫn.
- Kiểm tra lại tỉ lệ thành công theo lần thử của `quoc_te` (30,0% / 11,4% / 2,2%) từ CSV.
- Không commit `src/.venv/`, các thư mục rác trong `src/`, hay chỉnh sửa hai file CSV.

## 4. Bằng chứng

- Commit: `54b87ae`, `7715c86`, `490bac8`, `199d9e2`; merge `ecc033a` (PR #1), `fd71273` (PR #2), `6d7b97d` (CP2, PR #4) trên `main`.
- Output của `python lab13.py`: tổng 4.373.585 đ, 978 việc thành công, cps 4.472 đ; A3, A4 và B1–B4 khớp với hướng dẫn (B4 là 1,03×).
- File: `report/team/bang_chi_phi.md` (A1–B4 đã điền); phần "Kiểm số tính tay" do người kiểm số điền.

## 5. Công cụ AI đã dùng

- Claude (Claude Code) được dùng để viết phần code `mo_hinh`, A3, A4 và nhiệm vụ B (`lab13.py`), và để giải thích công thức. Tôi chỉ định yêu cầu và kiểm tra kết quả.
- Cách tự kiểm tra: so từng khoá output với bảng đối chiếu trong hướng dẫn, chạy lại tỉ lệ thành công theo lần thử từ CSV, và kiểm tra tuyến tính B2 (tổng hai tác động riêng bằng tác động cặp). Các con số không được lấy từ AI mà từ `lab13.py` chạy trên dữ liệu.

## 6. Tự đánh giá

- Đã làm xong A1–A4 và B1–B4, đối chiếu được đáp án.
- Chưa tự tay giải thích hết các công thức trong code. Trước khi bảo vệ, tôi cần đọc lại `mo_hinh` và phần B, và giải thích được:
  - vì sao tử số tính mọi lần chạy còn mẫu số chỉ đếm việc thành công;
  - vì sao xem lại 100% không tiết kiệm;
  - vì sao giới hạn rẻ nhất cho công ty (2 lần) khác giới hạn cho chi phí mỗi việc (1 lần).
- Điểm cần lưu ý: B4 có hai cách tính (9 phút/ca theo đề, 15,3 phút/ca theo dữ liệu). Khi bảo vệ cần nêu cả hai.
- Chưa làm: kiểm số tính tay (người kiểm số), CP3, CP4, CP5.
