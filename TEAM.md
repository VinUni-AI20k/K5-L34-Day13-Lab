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
- Người viết code nhiệm vụ B (CP2): bảng độ nhạy trong `src/lab13.py`, B1–B4.
- Điền `report/team/bang_chi_phi.md` phần A1–B4.
- Báo cáo cá nhân `report/team/2A202603685_DangVietAnh.md`.

### Đóng góp cụ thể

- Viết ba hàm A1 (`so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`); phép thử ĐẠT (1,20 · 1,25 · 1,25).
- Viết `mo_hinh` (A2), vòng lặp A3 (theo loại yêu cầu) và A4 (chi phí cố định 40 triệu đ/tháng) trong `src/lab13.py`.
- Viết B1–B4 (bảng độ nhạy) trong `src/lab13.py`: đổi từng yếu tố, đổi cặp và xếp hạng, giới hạn chạy lại tính cả hệ thống, xem lại 100%.
- Đối chiếu A2–A4 và B1–B4 với bảng trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`; B4 dùng 15,3 phút/ca làm lại theo hướng dẫn.
- Mở PR và merge: PR #1 (`feat/cp1-a2-mo-hinh`), PR #2 (`feat/cp1-a3-a4-bang-chi-phi`), PR #4 (CP2, nhánh `feat/cp2-bang-do-nhay`).

### Bằng chứng

- Commit `54b87ae` (ba hàm A1), `7715c86` (mo_hinh), `490bac8` (A3, A4, bảng chi phí), `199d9e2` (B1–B4); merge `ecc033a`, `fd71273`, `6d7b97d` trên `main`.
- Output `python lab13.py`: tổng 4.373.585 đ, 978 việc thành công, cps 4.472 đ; A3, A4 và B1–B4 khớp hướng dẫn (B4 là 1,03×).
- File `report/team/bang_chi_phi.md` (A1–B4) và `report/team/2A202603685_DangVietAnh.md`.

## NguyenVanVinh - 2A202603672

### Phần việc phụ trách

- Người gắn nhãn 2, kiêm giữ hồ sơ: điền `report/team/ho_so_launch_v0.md` từ đầu buổi.
- Gắn nhãn độc lập 20 ca lỗi ở CP3 (nhiệm vụ C), cùng người gắn nhãn 1 điền `report/team/bang_loi.md`.
- Báo cáo cá nhân `report/team/2A202603672_NguyenVanVinh.md`.

### Đóng góp cụ thể

- Dựng khung `ho_so_launch_v0.md`: nhóm OPC, lớp L3A; bảy mục, mỗi mục gán một vai trò phụ trách (PM trợ lý hoàn phí, Giám đốc vận hành, Trưởng nhóm CSKH, Kỹ sư trưởng agent), ghi rõ mục nào chờ số từ file nào.
- Điền mục 1 từ A2, A4: 4.472 đ/việc, gấp 16,3 lần hoá đơn token + tool chia số yêu cầu; 4.599 đ khi cộng chi phí cố định ở 45.000 yêu cầu/tháng, 5.784 đ nếu còn một nửa [simulated].
- Điền mục 2 từ B1, B2: xếp hạng làm lại +51,8% · xem lại +40,7% · lương +23,1% [simulated].
- Điền mục 3 từ A3, B3, B4: so với 12.000 đ theo loại (0,22× · 0,69× · 0,85× · 1,88×); cả hệ thống 7.037.585 ÷ 1.200 = 5.865 đ/yêu cầu = 0,49×; con số bất lợi xem lại 100% là 0,98× (1,03× nếu làm lại 15,3 phút) [simulated].
- Gắn nhãn độc lập 20 ca theo năm loại Google PAIR (Do người dùng 4 · Hệ thống 6 · Ngữ cảnh 3 · Giới hạn hệ thống 4 · Ngầm 3), có ghi lý do từng ca; điền cột nhãn người 2 trong `bang_loi.md`.

### Bằng chứng

- Commit `77d3078` (khung hồ sơ), `9edadc3` (mục 1, 3), `30f75f7` (mục 2, 3 từ B1–B4), `82c79b4` (nhãn người 2 trong `bang_loi.md`), `c64f454` (báo cáo cá nhân) trên `main`.
- File `report/team/ho_so_launch_v0.md`, `report/team/bang_loi.md`, `report/team/2A202603672_NguyenVanVinh.md`.
- Phiếu gắn nhãn gốc của người 2 (docx, có lý do từng ca), gắn trước khi so với người gắn nhãn 1.
