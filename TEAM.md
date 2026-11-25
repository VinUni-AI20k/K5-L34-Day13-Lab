# Team

## Thông tin nhóm

- Tên nhóm: 4thangtay
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-4thangtay-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: `https://github.com/Basrot/K5-L3B-DAY13-4thangtay-LaunchEconomics` · nhánh `main` *(cập nhật commit chốt sau duyệt chéo Gate 2a)*

## Thành viên

| STT | Họ tên             | MSSV        | Email                     | GitHub     | Vai trò                          |
| --: | ------------------ | ----------- | ------------------------- | ---------- | -------------------------------- |
|   1 | Thiều Thế Ngọc     | 2A202603788 | thengoc041012@gmail.com   | BFNGOC2    | Người viết code                  |
|   2 | Nguyễn Gia Nam     | 2A202603761 | mrbasrot@gmail.com        | Basrot     | Người kiểm số                    |
|   3 | Đào Ngọc Hân       | 2A202603779 | daongochan1505@gmail.com  | daongochan | Người gắn nhãn 1                 |
|   4 | Trần Trọng Đức Tài | 2A202603732 | ductai202603732@gmail.com | DucTai2804 | Người gắn nhãn 2, kiêm giữ hồ sơ |

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

## TranTrongDucTai-2A202603732

### Phần việc phụ trách

- Chủ trì thiết kế kế hoạch pilot D3 (`report/team/pilot_plan.yaml`).
- Chủ trì tổng hợp và hoàn thiện hồ sơ launch v0 một trang (`report/team/ho_so_launch_v0.md`).
- Gắn nhãn độc lập 20 ca lỗi ở Nhiệm vụ C (cột Nhãn người 2 trong `report/team/bang_loi.md`).
- Điều phối duyệt chéo, ghi phiếu chấm (`report/team/phieu_cham.md`) và tổng hợp `group_report.md`.

### Đóng góp cụ thể

- Thiết lập cấu hình pilot và 3 luật dừng an toàn/chi phí/sử dụng đúng mẫu chuẩn.
- Độc lập gắn nhãn 20 ca lỗi theo 5 loại của Google PAIR.
- Quản lý và liên kết số liệu giữa các phần A, B, C, D vào hồ sơ launch v0.

### Bằng chứng

- Commit trên nhánh `2A202603732_TranTrongDucTai`.
- File `report/team/pilot_plan.yaml`, `report/team/ho_so_launch_v0.md`, `report/team/2A202603732_TranTrongDucTai.md`.

## ThieuTheNgoc-2A202603788

### Phần việc phụ trách

- Chủ trì chuẩn bị môi trường Python và thực hiện A1–A4 trong `src/lab13.py`.
- Bàn giao mô hình và số liệu A cho Người 2; theo phân công, phối hợp kiểm tra B3, B4, D1 và chạy bản cuối trên máy khác.

### Đóng góp cụ thể

- Viết ba hàm A1 và mô hình A2; tính chi phí từ trace, tách A3 theo bốn loại yêu cầu và tính A4 với chi phí cố định 40 triệu đồng/tháng.
- Điền kết quả A1–A4 vào `report/team/bang_chi_phi.md`; ghi nhãn `simulated` cho các kết quả phụ thuộc phút xem lại/làm lại.
- Kết quả chính: A1 đạt 1,20 · 1,25 · 1,25; A2 là 4.472đ/việc thành công [simulated]; A4 là 4.599đ ở đủ khối lượng và 5.784đ ở nửa khối lượng [simulated].

### Bằng chứng

- File: `src/lab13.py`, `report/team/bang_chi_phi.md`, `report/team/2A202603788_ThieuTheNgoc.md`.
- Các commit A1–A4 và cập nhật theo review: `8ac8446`, `942f8b9`; PR được merge vào `main` tại `39194b6`.

## NguyenGiaNam-2A202603761

### Phần việc phụ trách

- Kiểm tra mô hình chi phí A và nhận vai viết code sau giờ giải lao (`src/lab13.py`).
- Chủ trì phân tích độ nhạy B1–B4 trong `report/team/bang_chi_phi.md`, tính cỡ mẫu D1 và bàn giao 3 chỉ số E1 cùng tỉ lệ mở lại 7 ngày.

### Đóng góp cụ thể

- Bổ sung các hàm B1–B4, D1 và tính E1 vào `src/lab13.py`; hoàn thiện bảng độ nhạy, chi phí toàn hệ thống và xem lại 100% trong `report/team/bang_chi_phi.md`.
- Lập bản phân chia công việc nhóm (`docs/phan_chia_cong_viec.md`) và phối hợp hoàn thiện `report/team/ho_so_launch_v0.md`.

### Bằng chứng

- File: `src/lab13.py`, `report/team/bang_chi_phi.md`, `report/team/2A202603761_NguyenGiaNam.md`, `docs/phan_chia_cong_viec.md`.
- PR #1 (`fbbc842`), PR #4 (`20a5efb`) và PR #7 (`1c839a2`) đã merge vào `main`.

## DaoNgocHan-2A202603779

### Phần việc phụ trách

- Theo dõi điều kiện hoàn thành checkpoint, chủ trì Nhiệm vụ C (`report/team/bang_loi.md`) và Nhiệm vụ E1–E2 (`report/team/chi_so.md`).
- Kiểm tra phần D2 và 3 luật dừng trong `report/team/pilot_plan.yaml`; rà soát chất lượng (nhãn `simulated`, từ cấm, tính nhất quán) toàn bộ hồ sơ nhóm trước Gate 2a.

### Đóng góp cụ thể

- Hoàn thiện bộ nhãn 20 ca lỗi Google PAIR (đồng thuận 20/20 = 100% với Người 4), 5 quy tắc phân biệt ranh giới và chuẩn hóa bảng khắc phục 5 ca có event/ngưỡng/tần suất trong `report/team/bang_loi.md`.
- Hoàn thiện 5 chỉ số E1 khớp đầu ra `src/lab13.py`, thiết kế 11 event có `trace_id` (kiểm tra chéo 5/5 chỉ số đo được) và 3 dòng rủi ro kinh tế E2 gắn nhãn `simulated` trong `report/team/chi_so.md`.
- Rà soát QA toàn bộ hồ sơ trước Gate 2a: chuẩn hóa công thức, nhãn `simulated` và điều kiện cụ thể trên `bang_chi_phi.md`, `group_report.md`, `ho_so_launch_v0.md` và `TEAM.md`.

### Bằng chứng

- File: `report/team/bang_loi.md`, `report/team/chi_so.md`, `report/team/2A202603779_DaoNgocHan.md`.
- Nhánh `2A202603779_DaoNgocHan`: commit `02476eb`, PR #5 đã merge vào `main` tại `a3d3e7d`.
