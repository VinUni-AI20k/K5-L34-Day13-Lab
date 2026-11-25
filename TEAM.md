# Team

## Thông tin nhóm

- Tên nhóm: 5AE
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-5AE-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo: https://github.com/truclamld/K5-L3B-DAY13-5AE-LaunchEconomics
- Nhánh nộp:
- Commit chốt: 

## Thành viên

| STT | Họ tên          | MSSV        | Email                     | GitHub    | Vai trò         |
|----:|-----------------|-------------|---------------------------|-----------|-----------------|
|   1 | Lê Đức Trúc Lâm | 2A202603787 | 26ai.lamldt@vinuni.edu.vn | truclamld | Người viết code |
|   2 | Ngô Chí Vĩnh    | 2A202603724 | 26ai.vinhnc2@vinuni.edu.vn | NgChiVinh | Người kiểm số; phụ trách Nhiệm vụ D |
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

## HoVaTen-MSSV

### Phần việc phụ trách

-

### Đóng góp cụ thể

-

### Bằng chứng

-

## NgoChiVinh-2A202603724

### Phần việc phụ trách

- Nhiệm vụ D (CP4): cỡ mẫu D1 trong `src/lab13.py` và `report/team/pilot_plan.yaml`.
- Người kiểm số: tính tay một con số của Nhiệm vụ A để đối chiếu với code.

### Đóng góp cụ thể

- Viết phần D1 trong `src/lab13.py`: hàm `co_mau`, `he_so_thiet_ke`, `co_mau_hieu_dung`, `m_toi_thieu`, `nhiem_vu_d`.
  - In năm câu D1: 1.251 · 3.103 (42 người mỗi nhóm) · 1.000 · 300 · m ≥ 299.
  - In power 0,64 khi chọn mức chênh 6 điểm.
  - In tỉ lệ mở lại hiện tại: 4,25% toàn mẫu, 3,97% trong phạm vi.
- Điền `pilot_plan.yaml`: chia theo nhân viên 20 + 20, mde 0,06, n 859, DE 6,96; trả lời 5 câu D2; ghi rõ đánh đổi đã chấp nhận.
- Viết 4 luật dừng theo mẫu NẾU – TRONG – THÌ – KHÔNG THÌ: an toàn (mở lại), an toàn (hoàn trùng / sổ cái), chi phí, mức độ sử dụng.
- Đối chiếu số A3, A4 trong `pilot_plan.yaml` với output code A của Lâm: khớp.
- Kiểm tra chéo luật dừng với nhãn ca 7, 20 trong `bang_loi.md` và danh sách event trong `chi_so.md`.

### Bằng chứng

- Commit `615f021` trên nhánh `nhiem-vu-D-Vinh`; PR #4.
- `python lab13.py` chạy từ đầu đến cuối, in phần D1 ở cuối.
- `pilot_plan.yaml` đọc được bằng `yaml.safe_load`, không còn `?` ngoài dòng chú thích.
- Báo cáo cá nhân: `report/team/2A202603724_NgoChiVinh.md`.
