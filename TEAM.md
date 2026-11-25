# Team

## Thông tin nhóm

- Tên nhóm:
- Lớp: L3A hoặc L3B
- Repo nhóm: `K5-L3A-DAY13-TenNhom-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt:

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Nguyễn Đức Hải | 2A202603943 |       | ndhai255 | Người viết code (trước giải lao) |
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

## HoVaTen-MSSV

### Phần việc phụ trách

-

### Đóng góp cụ thể

-

### Bằng chứng

-

## NguyenDucHai-2A202603943

### Phần việc phụ trách

- Người viết code trước giải lao: nhiệm vụ A (CP1) trong `src/lab13.py` và phần A1–A4 của `report/team/bang_chi_phi.md`.
- Merge các nhánh `p1-A` → `p2-B` → `p3-CD` → `p4-E`, nối module vào `src/lab13.py` để chạy hết từ đầu đến cuối.
- Duyệt chéo Gate 2a cùng Người 2, chấm vào `report/team/phieu_cham.md`.

### Đóng góp cụ thể

- A1: ba hàm kinh tế của việc chạy lại, qua ba phép thử 1,20 · 1,25 · 1,25.
- A2: `mo_hinh` (có nhánh `max_lan_chay`, trả thêm `chay_lai`, `hoa_don_moi_yc`); chi phí mỗi việc thành công 4.472 đ [simulated], gấp 16,3 lần hoá đơn token chia số yêu cầu.
- A3: tách theo 4 loại và tỉ lệ ok theo `attempt`; chỉ ra `quoc_te` không đáng xử lý (1,88× của 12.000 đ [simulated], tỉ lệ ok 30,0% → 11,4% → 2,2%).
- A4: cộng chi phí cố định 40 triệu đ/tháng cho `noi_dia` + `hang_nang`: 4.599 đ = 0,38× ở 45.000 yc/tháng, 5.784 đ = 0,48× ở một nửa khối lượng [simulated].

### Bằng chứng

- Nhánh `p1-A`, commit `5e91a4b` (A1–A4) và `1bd58d8` (báo cáo cá nhân).
- `cd src && python lab13.py` in `Ba phép thử đáp án biết trước: ĐẠT` và các bảng A2, A3, A4.
- Báo cáo cá nhân: [report/team/2A202603943_NguyenDucHai.md](report/team/2A202603943_NguyenDucHai.md).
