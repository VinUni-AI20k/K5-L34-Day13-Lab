# Team

## Thông tin nhóm

- Tên nhóm: Stech
- Lớp: L3A
- Repo nhóm: `K5-L3A-DAY13-Stech-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/aialphaproduct/K5-L3A-DAY13-Stech-LaunchEconomics

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Lưu Thanh Mỹ | 2A202603532 | Data97688@gmail.com | aialphaproduct | Trưởng nhóm · Người viết code (phần chính, CP1–CP2) |
|   2 | Nguyễn Thị Hồng Hạnh | 2A202603537 | hanhnth.ai@gmail.com | hanhshi96 | Người kiểm số (phần chính, CP1–CP2) |
|   3 | Phạm Đức Hồng Đức | 2A202603558 | Phamduchongduc15@gmail.com | DucPham1501 | Người gắn nhãn 1 (phần phụ, CP3) |
|   4 | Bùi Lê Công Tuấn | 2A202603610 | blct15102004@gmail.com | blct15102004 | Người gắn nhãn 2 · Viết `pilot_plan.yaml` (phần phụ, CP3–CP4) · Giữ hồ sơ + review cuối (CP5) |

Bốn vai của lab:

- **Người viết code (phần chính):** viết và chạy `src/lab13.py` cho CP1–CP2 — Mỹ.
- **Người kiểm số (phần chính):** tính tay một con số để đối chiếu, điền `bang_chi_phi.md` cho CP1–CP2 — Hạnh.
- **Người gắn nhãn 1 (phần phụ):** đọc đề, gắn nhãn 20 ca độc lập ở CP3 — Đức.
- **Người gắn nhãn 2, kiêm giữ hồ sơ + review cuối (phần phụ):** gắn nhãn 20 ca độc lập ở CP3; viết phần D (cỡ mẫu) ở CP4; CP5 tổng hợp `ho_so_launch_v0.md`, review toàn bộ hồ sơ trước khi nộp — Tuấn.

Phân công theo "phần chính / phần phụ": Mỹ + Hạnh làm CP1–CP2 (mô hình chi phí và độ nhạy — nền của mọi phần sau); Đức + Tuấn làm CP3–CP4 (gắn nhãn lỗi, kế hoạch pilot) và Tuấn tổng hợp + review cuối ở CP5.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## LuuThanhMy-2A202603532

### Phần việc phụ trách

- Setup repo, fork, điền TEAM.md
- Viết `src/lab13.py` phần CP1 (hàm A1, `mo_hinh`, A2–A4) — phần chính
- Viết `src/lab13.py` phần CP2 (B1–B4) — phần chính

### Đóng góp cụ thể

-

### Bằng chứng

-

---

## NguyenThiHongHanh-2A202603537

### Phần việc phụ trách

- Kiểm số bằng tay, điền `report/team/bang_chi_phi.md` (bảng A2, A3, A4, B1–B4) — phần chính

### Đóng góp cụ thể

-

### Bằng chứng

-

---

## PhamDucHongDuc-2A202603558

### Phần việc phụ trách

- Gắn nhãn 20 ca lỗi (nhãn 1, CP3) — phần phụ
- Hỗ trợ điền `report/team/bang_loi.md` (bảng khắc phục 5 ca)

### Đóng góp cụ thể

-

### Bằng chứng

-

---

## BuiLeCongTuan-2A202603610

### Phần việc phụ trách

- Gắn nhãn 20 ca lỗi (nhãn 2, CP3) — phần phụ
- Viết `src/lab13.py` phần CP4 (tính cỡ mẫu D1, D2), điền `report/team/pilot_plan.yaml`
- CP5: điền `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md`
- Review toàn bộ hồ sơ trước khi nộp; điều phối Gate 2a: `report/team/phieu_cham.md`, `report/team/group_report.md`, commit + push

### Đóng góp cụ thể

- CP3: Gắn nhãn độc lập 20 ca lỗi theo 5 loại Google PAIR (cột `Nhãn người 2`) và lập bảng khắc phục 5 ca (mỗi loại 1 ca) trong `report/team/bang_loi.md`.
- CP4: Viết hàm `co_mau_hai_ti_le` và `tinh_co_mau_cp4` trong `src/lab13.py` tính 5 câu D1 và tỉ lệ `mo_lai_trong_7_ngay` hiện tại; hoàn thiện toàn bộ `report/team/pilot_plan.yaml` (cỡ mẫu, 5 câu kiểm tra D2, đánh đổi MDE 6 điểm, 3 luật dừng 4 vế).
- CP5: Tính thử 3 chỉ số E1, liệt kê 10 event có `trace_id`, lập bảng 3 rủi ro kinh tế E2 trong `report/team/chi_so.md`; tổng hợp 7 mục và đề xuất `Go có điều kiện` trong `report/team/ho_so_launch_v0.md`.

### Bằng chứng

- Nhánh `feat/cp3-cp4-pilot-plan` (PR #10), các commit `48fdce8`, `41c83ac`.
- Các file đã cập nhật: `src/lab13.py`, `report/team/bang_loi.md`, `report/team/pilot_plan.yaml`, `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md`.
