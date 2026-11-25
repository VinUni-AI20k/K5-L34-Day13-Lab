# Team

## Thông tin nhóm

- Tên nhóm: 5AE
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-5AE-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo: https://github.com/truclamld/K5-L3B-DAY13-5AE-LaunchEconomics
- Nhánh nộp: `main`
- Commit chốt: 

## Thành viên

| STT | Họ tên          | MSSV        | Email                     | GitHub    | Vai trò         |
|----:|-----------------|-------------|---------------------------|-----------|-----------------|
|   1 | Lê Đức Trúc Lâm | 2A202603787 | 26ai.lamldt@vinuni.edu.vn | truclamld | Người viết code |
|   2 |                 |             |                           |           |                 |
|   3 |                 |             |                           |           |                 |
|   4 |                 |             |                           |           |                 |
|   5 |                 |             |                           |           |                 |

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

## LeDucTrucLam-2A202603787

### Phần việc phụ trách

Phụ trách phần code nhiệm vụ A: hoàn thiện các hàm tính kinh tế chạy lại và mô hình chi phí, phân tích chi phí theo loại yêu cầu và phân bổ chi phí cố định; ghi kết quả vào `report/team/bang_chi_phi.md`.

### Đóng góp cụ thể

Hoàn thiện `so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong` và `mo_hinh`; dùng mô hình để tính A2, tách A3 theo bốn loại yêu cầu và tính A4 cho phạm vi `noi_dia` + `hang_nang`. Ba phép thử A1 đều in `ĐẠT`. Kết quả chính: tổng chi phí 4.373.585 đ, 978 yêu cầu thành công, chi phí 4.472 đ/việc thành công; chi phí cố định làm A4 thành 4.599 đ/việc ở 45.000 yêu cầu/tháng và 5.784 đ ở nửa khối lượng (các kết quả có phần phút nhân viên được ghi nhãn `simulated`).

### Bằng chứng

Commit `db721d65aafa47245711595d6b2858f00e994c69` có thay đổi ở `src/lab13.py` và `report/team/bang_chi_phi.md`. Đã chạy `python lab13.py`: A1 đạt; kết quả A2–A4 khớp số đối chiếu trong hướng dẫn lab. Báo cáo chi phí nằm trong `report/team/bang_chi_phi.md`.


-
