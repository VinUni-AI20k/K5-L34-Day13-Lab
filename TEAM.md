# Team

## Thông tin nhóm

- Tên nhóm: TSNQ
- Lớp: L3A
- Repo nhóm: `K5-L3A-DAY13-TSNQ-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/NamPham1012/K5-L3A-DAY13-TSNQ-LaunchEconomics · nhánh `main` · commit chốt: điền sau khi push (hiện `a4e052f` là commit cuối đã push, chưa gồm bản sửa mới)

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Phạm Văn Nam | 2A202603681 | namphamit04@gmail.com | NamPham1012 | Người viết code; tham gia kiểm số |
|   2 | Vũ Thành Toàn | 2A202603654 | thanhtoana7hha@gmail.com | kyo708       | Người gắn nhãn 1; theo dõi điều kiện hoàn thành |
|   3 | Lê Nguyễn Hoàng Sơn | 2A202603686 | hoangson199205@gmail.com | SonLNH19      | Người gắn nhãn 2 kiêm giữ hồ sơ |

Nhóm có 3 thành viên nên một người kiêm hai vai. Bốn vai của lab:

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

## Phạm Văn Nam — 2A202603681

### Phần việc phụ trách

- Người viết code; tham gia kiểm số cho các nhiệm vụ A, B và D1.

### Đóng góp cụ thể

- Dùng Codex hỗ trợ triển khai và chạy `src/lab13.py`, cài môi trường và kiểm tra ba phép thử A1.
- Dùng kết quả kiểm số độc lập do AI hỗ trợ để đối chiếu chi phí, độ nhạy và cỡ mẫu; điền `report/team/bang_chi_phi.md` từ kết quả chạy.

### Bằng chứng

- `src/lab13.py` — commit `b819e8e`; `report/team/kiem_so.md` — commit `eb1ce5a`.
- `report/team/bang_chi_phi.md` và báo cáo cá nhân `report/team/2A202603681_PhamVanNam.md`.

## Lê Nguyễn Hoàng Sơn — 2A202603686

### Phần việc phụ trách

- Phụ trách nhãn lỗi người 2 và hồ sơ launch v0; thực hiện phân loại, đề xuất khắc phục, tổng hợp bằng chứng và chạy kiểm tra số liệu.

### Đóng góp cụ thể

- Gắn nhãn người 2 cho 20 ca trong buổi chiều ngày lab (khai báo của Sơn, chưa có phiếu gốc ghi giờ). Lý do từng ca và 5 ca khắc phục trong `report/team/bang_loi.md` có Codex hỗ trợ biên soạn.
- Tổng hợp hồ sơ launch 7 mục từ đầu ra đã lưu của nhóm, phân biệt số simulated, nêu số bất lợi và các điều kiện còn thiếu; đề xuất No-go ở trạng thái hiện tại để nhóm thảo luận.
- Đã chạy lại `src/lab13.py` trên máy cá nhân và cung cấp output A1–E1; ba phép thử A1 ĐẠT, toàn bộ output được đối chiếu khớp `src/ket_qua_lab13.txt` khi bỏ qua khoảng trắng.
- Kết quả so nhãn với Toàn: 20/20 theo xác nhận của nhóm; chưa xác minh được tính độc lập và chưa có phiếu gốc nên không dùng làm bằng chứng độc lập. Còn chờ xác nhận công thức của người kiểm số và quyết định chung của nhóm.

### Bằng chứng

- `report/team/bang_loi.md`: cột nhãn người 2, lý do cho 20 ca, quy tắc phân biệt và bảng khắc phục 5 loại.
- `report/team/ho_so_launch_v0.md`: bảy mục có số, trạng thái, vai trò phụ trách, nguồn số và việc cần làm để quay lại Gate 2a.

## Vũ Thành Toàn — 2A202603654

### Phần việc phụ trách

- Người gắn nhãn 1 tại CP3: đọc đề, theo dõi điều kiện hoàn thành và tự gắn nhãn 20 ca trước khi so với người 2.

### Đóng góp cụ thể

- Làm 20 nhãn; kết quả so với cột người 2 là 20/20. Theo khai báo của Toàn và Sơn, hai người gắn nhãn trong buổi chiều ngày lab; chưa có phiếu gốc ghi giờ nên tính độc lập chưa được xác minh.
- Có công cụ đối chiếu hai phiếu; kết quả 20/20, không dựa trên output công cụ.
- Theo xác nhận của người dùng, bộ nhãn người 2 trong bảng chung là tự làm; cần giữ bản gốc của từng người trước khi so nhãn.

### Bằng chứng

- `report/team/bang_loi.md`: bảng tổng hợp nhãn và kết quả đối chiếu theo xác nhận.
- `scripts/doi_chieu_nhan.py`: công cụ đọc hai phiếu, kiểm tra nhãn và in tỉ lệ trùng, không sửa dữ liệu đầu vào.
- `report/team/2A202603654_VuThanhToan.md`: thông tin cá nhân, phạm vi việc, kiểm điều kiện và khai báo AI.
