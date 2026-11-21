# Team

## Thông tin nhóm

- Tên nhóm:
- Lớp: L3A hoặc L3B
- Repo nhóm: `K5-L3A-DAY13-TenNhom-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt:

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 |     Đặng Việt Anh   |   2A202603685   |  vietanh.dang282@gmail.com     |        |     Người viết code    |
|   2 |     Hà Huy Thái   |    2A202603682  |   thailc0903@gmail.com    |    thailc0903    |     Người kiểm số    |
|   3 |   Nguyễn Văn Vinh     |   2A202603672   |    nguyenvanvinh2819@gmail.com   |   VINH1811     |     Người gắn nhãn 2, kiêm giữ hồ sơ    |
|   4 |     Vũ Quang Minh   |    2A202603657  |    vuquangminh897@gmail.com   |   Minh8246     |    Người gắn nhãn 1     |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## DangVietAnh - 2A202603685

### Phần việc phụ trách

- Người viết code giai đoạn đầu (14:00–15:20): nhiệm vụ A (CP1) trong `src/lab13.py`.
- Điền `report/team/bang_chi_phi.md` phần A1–A4.
- Báo cáo cá nhân `report/team/2A202603685_DangVietAnh.md`.

### Đóng góp cụ thể

- Viết ba hàm A1 (`so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`); phép thử ĐẠT (1,20 · 1,25 · 1,25).
- Viết `mo_hinh` (A2) và vòng lặp A3 (theo loại yêu cầu) và A4 (chi phí cố định 40 triệu đ/tháng) trong `src/lab13.py`.
- Đối chiếu A2, A3, A4 với bảng trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`; kiểm tra lại tỉ lệ thành công theo lần thử của `quoc_te` từ CSV.
- Mở PR và merge: PR #1 (nhánh `feat/cp1-a2-mo-hinh`), PR #2 (nhánh `feat/cp1-a3-a4-bang-chi-phi`).

### Bằng chứng

- Commit `54b87ae` (ba hàm A1), `7715c86` (mo_hinh), `490bac8` (A3, A4, bảng chi phí); merge `ecc033a` (PR #1) và `fd71273` (PR #2) trên `main`.
- Output `python lab13.py`: tổng 4.373.585 đ, 978 việc thành công, cps 4.472 đ; A3 và A4 khớp hướng dẫn.
- File `report/team/bang_chi_phi.md` (A1–A4) và `report/team/2A202603685_DangVietAnh.md`.
