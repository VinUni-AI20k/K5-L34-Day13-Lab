# Team

## Thông tin nhóm

- Tên nhóm:
- Lớp: L3A 
- Repo nhóm: `K5-L3A-DAY13-TenNhom-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/GaGionCay/K5-L3A-DAY13-CATH-LaunchEconomics · `main` · `4beac6b`

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Nguyễn Thế Cường | 2A202603355 | 26ai.cuongnt2@vinuni.edu.vn | Chill2004 | Người viết code (A, B); sau giải lao kiểm số D1 |
|   2 | Hoàng Ngọc Minh Trí | 2A202603379 | 26ai.trihnm@vinuni.edu.vn |        | Người kiểm số (nhiệm vụ D) |
|   3 | Chử Thị Ánh | 2A202603360 | ai26.anhct@vinuni.edu.vn |        | Người gắn nhãn 1 (nhiệm vụ C bộ 1, E) |
|   4 | Nguyễn Thị Thu Hà | 23001603 | nha253158@gmail.com | nha253158-hub | Người gắn nhãn 2, kiêm giữ hồ sơ |

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

## NguyenTheCuong-2A202603355

### Phần việc phụ trách

- Người viết code nhiệm vụ A (CP1) và B (CP2) trong `src/lab13.py`; điền `report/team/bang_chi_phi.md`.
- Sau giải lao: kiểm số D1 (câu e) cho người viết code phần D.

### Đóng góp cụ thể

- A1–A4: ba hàm chạy lại (ba phép thử ĐẠT), hàm `mo_hinh()`, tách theo loại, chi phí cố định. Chi phí mỗi việc thành công 4.472 đ, gấp 16,3× hoá đơn token; quoc_te 1,88× nên loại khỏi pilot; phạm vi noi_dia + hang_nang 0,38× khi cộng cố định [simulated].
- B1–B4: 9 kịch bản độ nhạy; xếp hạng làm lại (+51,8%) · xem lại (+40,7%) · lương (+23,1%); giới hạn 2 lần rẻ nhất cho công ty (6.901.220 đ); xem lại 100% cho 0,98× [simulated].
- Kiểm chéo D1 câu e: n = 859 mỗi nhóm, m ≥ 299, hệ số thiết kế 6,96; power 0,64 ở mức 5 điểm.

### Bằng chứng

- Commit trên nhánh `ntc`: `28695bd`, `b81ec83` (CP1), `5e444db` (CP2).
- File: `src/lab13.py`, `report/team/bang_chi_phi.md`, `report/team/2A202603355_NguyenTheCuong.md`.

## HoangNgocMinhTri-2A202603379

### Phần việc phụ trách

- Nhiệm vụ D: cỡ mẫu D1, năm điều kiện D2, tỉ lệ mở lại, ba luật dừng
- Hoàn thiện A3 (phạm vi pilot) và `report/team/pilot_plan.yaml`

### Đóng góp cụ thể

- D1: 1.251 yêu cầu/nhóm (MDE 5 điểm); thiết kế chấp nhận 20 nhân viên/nhóm, MDE 6 điểm, 859 mẫu hiệu dụng, DE 6,96
- Ba luật dừng đủ NẾU – TRONG – THÌ – KHÔNG THÌ; ngưỡng chi phí 8.000 đ/việc thành công
- Cập nhật `lab13.py` đọc phạm vi pilot từ YAML

### Bằng chứng

- `report/team/pilot_plan.yaml`, `src/lab13.py`, `report/team/2A202603379_HoangNgocMinhTri.md`

## ChuThiAnh-2A202603360

### Phần việc phụ trách

- Nhiệm vụ C: bộ nhãn 1 (20 ca)
- Nhiệm vụ E: E1 chỉ số và event, E2 rủi ro kinh tế

### Đóng góp cụ thể

- E1: ba chỉ số (82,83%; 27,12%; 4,25%), hai chỉ số đề xuất, tám event có `trace_id`
- E2: hai dòng rủi ro đối chiếu với B1 của Cường, cảnh báo B4
- Bộ nhãn 1 có Codex hỗ trợ; Ánh đã review và xác nhận ngày 21/11

### Bằng chứng

- `report/team/chi_so.md`, `report/team/dan_chung_nhan_C_bo1_Anh.md`, `report/team/2A202603360_ChuThiAnh.md`

## NguyenThiThuHa-23001603

### Phần việc phụ trách

- Nhiệm vụ C: gắn nhãn bộ 2 (20 ca), viết `report/team/bang_loi.md`
- Giữ hồ sơ: `report/team/ho_so_launch_v0.md`, ghép hồ sơ cuối buổi
- Viết `report/team/group_report.md`, điền `TEAM.md`

### Đóng góp cụ thể

- Gắn nhãn 20 ca lỗi (bộ 2), đã so với bộ 1 của Ánh: khớp 20/20; bộ 2 có Claude hỗ trợ, Hà đã tự rà và xác nhận; Ánh đã review và xác nhận bộ 1 ngày 21/11
- Bảng khắc phục 5 ca (9, 7, 18, 4, 17) đủ 5 loại, có cách phát hiện đo được và vai trò phụ trách
- Hồ sơ launch v0 bảy mục, đề xuất Go có điều kiện, số simulated có nhãn

### Bằng chứng

- `report/team/bang_loi.md`, `report/team/ho_so_launch_v0.md`, `report/team/group_report.md`, `report/team/23001603_NguyenThiThuHa.md`
