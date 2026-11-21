# Team

## Thông tin nhóm

- Tên nhóm: PD
- Lớp: L3A
- Repo nhóm: `K5-L3A-DAY13-PD-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/buianhdung2kar5/K5-L3A-DAY13-PD-LaunchEconomics · `main` · commit merge cuối cùng trên `main` (bản đã kiểm tra cuối: `c44bfaa`)

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Bùi Anh Dũng | 2A202603687 | 26ai.dungba2@vinuni.edu.vn | buianhdung2kar5 | Người viết code (trước giải lao) → Người kiểm số (sau giải lao) |
|   2 | Lê Minh Phụng | 2A202603693 | phung8282003@gmail.com | okuminhphen | Người gắn nhãn 1 + Người kiểm số (trước giải lao) → Người viết code (sau giải lao) |
|   3 | Mai Văn Thanh | 2A202603696 | maivanthanh36tb@gmail.com | MaiVanThanhDev | Người gắn nhãn 2, kiêm giữ hồ sơ |

Nhóm 3 người nên một người giữ hai vai (Phụng: gắn nhãn 1 và kiểm số). Đổi người viết code sau giờ giải lao: Dũng chuyển sang kiểm số, Phụng chuyển sang viết code, để ít nhất hai người tự tay tính được chi phí.

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

## Cá nhân

Mỗi thành viên có báo cáo riêng trong `report/team/MSSV_HoTen.md`:

- Bùi Anh Dũng: `report/team/2A202603687_BuiAnhDung.md`
- Lê Minh Phụng: `report/team/2A202603693_LeMinhPhung.md`
- Mai Văn Thanh: `report/team/2A202603696_MaiVanThanh.md`

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## BuiAnhDung-2A202603687

### Phần việc phụ trách

- Nhiệm vụ A, B (mô hình chi phí, bảng độ nhạy) trong `src/lab13.py` và `report/team/bang_chi_phi.md`.
- Nhiệm vụ E1, E2 trong `report/team/chi_so.md`.
- Sau giải lao: kiểm số phần D do Phụng viết.

### Đóng góp cụ thể

- Viết ba hàm A1 và `mo_hinh`; ba phép thử đáp án biết trước in ĐẠT (1,20 · 1,25 · 1,25).
- Điền bảng A1–A4, B1–B4 (chi phí mỗi việc thành công 4.472 đ [simulated], gấp 16,3 lần hoá đơn token).
- Tính thử ba chỉ số (82,83% · 27,12% · 4,25%), soạn danh sách event và ba dòng rủi ro kinh tế.

### Bằng chứng

- Commit `22e4359`; file `src/lab13.py`, `report/team/bang_chi_phi.md`, `report/team/chi_so.md`.
- Báo cáo cá nhân: `report/team/2A202603687_BuiAnhDung.md`.

## LeMinhPhung-2A202603693

### Phần việc phụ trách

- CP1: tính tay A1 (1,20 · 1,25 · 1,25) và 1–2 số trong A2 để đối chiếu.
- CP3: gắn nhãn 1 cho 20 ca độc lập, so nhãn với người gắn nhãn 2, tính đồng thuận, chốt ca lệch.
- Sau giải lao: viết code D1 (5 câu cỡ mẫu) và tỉ lệ `mo_lai_trong_7_ngay`; soát `chi_so.md`; chạy kiểm tra cuối. Duyệt chéo phần pilot của nhóm kia.

### Đóng góp cụ thể

- Đối chiếu ba kết quả A1 (1,20 · 1,25 · 1,25), phí token và phí gọi tool ở A2.
- Bổ sung code cho năm câu D1 và tính tỉ lệ mở lại trong 7 ngày: 4,25% toàn mẫu, 3,97% trong phạm vi pilot.
- Chuẩn bị 20 nhãn tham khảo có hỗ trợ AI, soát các event có `trace_id` và góp ý về số cụm, lịch lấy mẫu và luật dừng pilot.

### Bằng chứng

- Commit `d9b5aaf` và `2d4f9ac`, đã merge vào `main` qua PR #2.
- File `src/lab13.py`, `report/team/bang_loi.md`, `report/team/chi_so.md` và [báo cáo cá nhân](report/team/2A202603693_LeMinhPhung.md).

## MaiVanThanh-2A202603696

### Phần việc phụ trách

- Người gắn nhãn 2, kiêm giữ hồ sơ.
- CP1: điền bảng A2, A3 trong `bang_chi_phi.md`.
- CP3: gắn nhãn 2 cho 20 ca độc lập; ghi 2 bộ nhãn, đồng thuận, quy tắc ca lệch và bảng khắc phục vào `bang_loi.md`.
- CP4: điền `pilot_plan.yaml`.
- CP5: hoàn thiện `ho_so_launch_v0.md`, điền `phieu_cham.md`, `group_report.md`.

### Đóng góp cụ thể

- Điền bảng A2 (9 dòng, nhãn *simulated*) và A3 (4 loại) trong `report/team/bang_chi_phi.md`.
- Điền `report/team/pilot_plan.yaml`: D1 (1.251 · 3.103 · 1.000 · 300 · m ≥ 299), D2, chia theo nhân viên 20 + 20, MDE 6 điểm; điều kiện đủ 40 nhân viên, lịch thu mẫu + 7 ngày theo dõi; 5 luật dừng đủ 4 vế, áp dụng theo bước rollout.
- Gắn nhãn 2 cho 20 ca lỗi; ghi hai bộ nhãn, đồng thuận 18/20, quy tắc ca 8 và 13, bảng khắc phục 5 ca trong `report/team/bang_loi.md`.
- Soạn `report/team/ho_so_launch_v0.md` (7 mục, đề xuất Go có điều kiện) và nháp `report/team/group_report.md`.
- Gộp nhánh của Dũng và Phụng, giải quyết xung đột `bang_chi_phi.md` và `bang_loi.md`.

### Bằng chứng

- `report/team/bang_chi_phi.md`, `report/team/pilot_plan.yaml`, `report/team/ho_so_launch_v0.md`
- Commit: `2212a77` (pilot_plan.yaml, hồ sơ, TEAM.md), `2242982` (pilot theo góp ý của Phụng, nhãn người 2), `369be1d` (bảng lỗi CP3, mục 5 hồ sơ), `8f46aa6` (luật dừng theo bước rollout); PR #2, #3
