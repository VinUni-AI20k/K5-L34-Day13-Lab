# Team

## Thông tin nhóm

- Tên nhóm:
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-25112026-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt:

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Phạm ĐứcVinh   | 2A202603849     | 26ai.vinhpd@vinuni.edu.vn      |  vindpd203      | Người viết code (trước giải lao) |
|   2 | Ngô Duy Khánh | 2A202603870 | | | Người kiểm số (sau giải lao nhận viết code) |
|   3 | Bảo    |      |       |        | Người gắn nhãn 1 |
|   4 | Huy    |      |       |        | Người gắn nhãn 2, kiêm giữ hồ sơ |

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

## NgoDuyKhanh-2A202603870

### Phần việc phụ trách

- **Chính:** CP4 · Nhiệm vụ D (`report/team/pilot_plan.yaml`, code tính 5 câu cỡ mẫu D1 và tỉ lệ mở lại trong `src/lab13.py`).
- **Phụ:** CP1 (tính tay kiểm số, điền bảng A1–A4), CP2 (điền bảng độ nhạy B1–B4, tự kiểm tra quy tắc tuyến tính), CP3 (soát lại `bang_chi_phi.md`), CP5 (tính 3 chỉ số E1 trong `src/lab13.py` và điền vào `report/team/chi_so.md`).

### Đóng góp cụ thể

- Tính tay kiểm chứng số liệu chi phí và hoàn thiện toàn bộ các bảng A1–A4, B1–B4 cùng các câu trả lời ngắn gọn kèm nhãn `simulated` trong `report/team/bang_chi_phi.md`.
- Viết code giải 5 bài toán cỡ mẫu D1, tính tỉ lệ `mo_lai_trong_7_ngay` hiện tại (4,25% toàn mẫu; 3,97% trong phạm vi `noi_dia + hang_nang`) và 3 chỉ số E1 trong `src/lab13.py`.
- Chủ trì hoàn thiện `report/team/pilot_plan.yaml` (điền chú thích D1, D2, đánh đổi chấp nhận MDE 6 điểm, 3 luật dừng chuẩn `NẾU – TRONG – THÌ – KHÔNG THÌ`, xoá toàn bộ dấu `?`).
- Cập nhật kết quả tính thử 3 chỉ số E1 (82,83% · 27,12% · 4,25%) vào `report/team/chi_so.md`.

### Bằng chứng

- Code CP4 (D1) và CP5 (E1) trong [src/lab13.py](src/lab13.py).
- File [report/team/bang_chi_phi.md](report/team/bang_chi_phi.md), [report/team/pilot_plan.yaml](report/team/pilot_plan.yaml), [report/team/chi_so.md](report/team/chi_so.md) và báo cáo cá nhân [report/team/2A202603870_NgoDuyKhanh.md](report/team/2A202603870_NgoDuyKhanh.md).

## PhamDucVinh-2A202603849

### Phần việc phụ trách

- **Chính:** chuẩn bị môi trường, CP1 · Nhiệm vụ A, CP2 · Nhiệm vụ B (code trong `src/lab13.py`), đóng gói và nộp bài.
- **Phụ:** CP3 (hoàn thiện B), CP4 (soát `pilot_plan.yaml`), CP5 (chạy lại `lab13.py` trên máy khác), bàn giao code cho Người 2.

### Đóng góp cụ thể

- Viết 3 hàm A1 (ba phép thử ĐẠT: 1,20 · 1,25 · 1,25) và `mo_hinh()` A2: chi phí mỗi việc thành công 4.472 đ [simulated], gấp 16,3 lần hoá đơn chia số yêu cầu.
- Tính A3 theo loại (`quoc_te` 1,88× [simulated], chạy lại không giúp) và A4 cộng chi phí cố định (4.599 đ = 0,38× ở 45.000 yêu cầu/tháng [simulated]).
- Viết B1–B4: 9 kịch bản độ nhạy, một cặp (+46,3%), giới hạn 2 lần rẻ nhất cho công ty (6.901.220 đ [simulated]), xem lại 100% = 0,98×–1,03× [simulated].

### Bằng chứng

- Commit `b9a5f93` trên nhánh `vinh` (merge vào `main` qua pull request #1).
- Code trong [src/lab13.py](src/lab13.py), số trong [report/team/bang_chi_phi.md](report/team/bang_chi_phi.md) và báo cáo cá nhân [report/team/2A202603849_PhamDucVinh.md](report/team/2A202603849_PhamDucVinh.md).

## HoVaTen-MSSV

### Phần việc phụ trách

-

### Đóng góp cụ thể

-

### Bằng chứng

-
