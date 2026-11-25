# Team

## Thông tin nhóm

- Tên nhóm: LuckyTeam
- Lớp: [Điền L3A hoặc L3B]
- Repo nhóm: `K5-L3A-DAY13-LuckyTeam-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: [Điền trước khi nộp]

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Nguyễn Đức Hải | 2A202603943 | ndhai255.work@gmail.com | ndhai255 | Người viết code (trước giải lao) — Nhiệm vụ A |
|   2 | [Điền họ tên] | [Điền MSSV] | [Điền email] | [Điền GitHub] | Người kiểm số — Nhiệm vụ B & E2 |
|   3 | [Điền họ tên] | [Điền MSSV] | [Điền email] | [Điền GitHub] | Người gắn nhãn 1, viết code sau giải lao — Nhiệm vụ C & D |
|   4 | [Điền họ tên] | [Điền MSSV] | [Điền email] | [Điền GitHub] | Người gắn nhãn 2 kiêm giữ hồ sơ — Nhiệm vụ C (nhãn 2), E1, event & hồ sơ |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py` (Nhiệm vụ A, nối module cuối buổi).
- **Người kiểm số:** tính tay đối chiếu A1–A2, viết `src/cp2_do_nhay.py`, điền B1–B4 và rủi ro kinh tế E2.
- **Người gắn nhãn 1:** gắn nhãn 20 ca độc lập ở CP3, tổng hợp `report/team/bang_loi.md`, viết `src/cp4_co_mau.py` và `report/team/pilot_plan.yaml`.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** gắn nhãn 20 ca độc lập ở CP3, viết `src/cp5_chi_so.py`, điền E1 và danh sách event trong `report/team/chi_so.md`, dựng và cập nhật `report/team/ho_so_launch_v0.md`, `TEAM.md`, `report/team/group_report.md`.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/team/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

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

## [Nguoi2-HoVaTen-MSSV]

### Phần việc phụ trách

- Kiểm số độc lập A1–A2; Nhiệm vụ B (B1–B4) trong `src/cp2_do_nhay.py`, `report/team/bang_chi_phi.md` và Nhiệm vụ E2 trong `report/team/chi_so.md`.

### Đóng góp cụ thể

- [Cập nhật sau khi hoàn thành nhánh `p2-B`]

### Bằng chứng

- [Link commit / output `src/cp2_do_nhay.py`]

## [Nguoi3-HoVaTen-MSSV]

### Phần việc phụ trách

- Người gắn nhãn 1 (20 ca độc lập, tổng hợp `report/team/bang_loi.md`); Nhiệm vụ D (`src/cp4_co_mau.py`, `report/team/pilot_plan.yaml`).

### Đóng góp cụ thể

- [Cập nhật sau khi hoàn thành nhánh `p3-CD`]

### Bằng chứng

- [Link commit / output `src/cp4_co_mau.py` & `yaml.safe_load`]

## [Nguoi4-HoVaTen-MSSV]

### Phần việc phụ trách

- Người gắn nhãn 2 (gắn độc lập 20 ca lỗi CP3 để đối chiếu với Người 3).
- Nhiệm vụ E1 (tính thử 3 chỉ số, đề xuất 2 chỉ số mới) và đặc tả 10 event có `trace_id` kèm kiểm tra chéo.
- Giữ và cập nhật hồ sơ `report/team/ho_so_launch_v0.md`, `TEAM.md`, `report/team/group_report.md`.

### Đóng góp cụ thể

- Gắn nhãn độc lập 20 ca lỗi theo 5 loại Google PAIR dựa trên nguyên nhân gốc để so đồng thuận với Người 3.
- Viết module `src/cp5_chi_so.py` tính ba chỉ số E1 trên 1.200 yêu cầu (`82,83%`, `27,12%`, `4,25%`) và phạm vi pilot (`92,26%`, `21,09%`, `3,97%`).
- Hoàn thiện phần E1, bảng 10 event có `trace_id` và kiểm tra chéo trong `report/team/chi_so.md`.
- Dựng khung 7 mục và đề xuất nháp Go có điều kiện trong `report/team/ho_so_launch_v0.md`; dựng khung `TEAM.md` và `report/team/group_report.md`.

### Bằng chứng

- `src/cp5_chi_so.py`, `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md`, `TEAM.md`, `report/team/group_report.md`.
