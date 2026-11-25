# Team

## Thông tin nhóm

- Tên nhóm:
- Lớp: L3A hoặc L3B
- Repo nhóm: `K5-L3A-DAY13-TenNhom-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt:

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Mai Danh Hiếu | 2A202603948 |       |        | Người viết code (CP1–CP2) |
|   2 |        |      |       |        |         |
|   3 |        |      |       |        |         |
|   4 |        |      |       |        |         |

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

## MaiDanhHieu-2A202603948

### Phần việc phụ trách

- Viết và chạy `src/lab13.py` cho CP1 (A1–A4) và CP2 (B1–B4).

### Đóng góp cụ thể

- Hoàn thiện mô hình chi phí từ trace, phân tích theo loại yêu cầu và phân bổ chi phí cố định.
- Tính chín kịch bản độ nhạy, kịch bản kết hợp, chi phí cả hệ thống theo giới hạn chạy lại và chi phí xem lại 100%.
- Điền kết quả A1–B4 vào `report/team/bang_chi_phi.md`, ghi nhãn `simulated` cho các số dùng thời gian giả lập.

### Bằng chứng

- `python lab13.py` chạy được và ba phép thử A1 báo **ĐẠT**.
- `report/team/bang_chi_phi.md`: chi phí gốc 4.472 đ/việc; giới hạn 2 lần chạy cho chi phí cả hệ thống thấp nhất 6.901.220 đ [simulated].
- Báo cáo cá nhân: `report/team/2A202603948_MaiDanhHieu.md`.
