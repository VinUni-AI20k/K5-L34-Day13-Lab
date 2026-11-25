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
|   2 | Phạm Lê Chuẩn                 |   2A202603784          | 26ai.chuanpl@vinuni.edu.vn                          | 22520160          | Người viết code                |
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

## PhamLeChuan-2A202603784

### Phần việc phụ trách

- Người viết code: phụ trách `src/lab13.py`; tập trung hoàn thiện tính chi phí cố định A4 và phân tích độ nhạy, giới hạn chạy lại ở nhiệm vụ B.

### Đóng góp cụ thể

- Hoàn thiện mô hình tính chi phí theo trace và các kịch bản B1–B4; phối hợp dùng ChatGPT/Codex để triển khai phép tính, rồi rà soát kết quả và các giả định trong báo cáo.
- Hoàn thiện bảng A4 cho phạm vi `noi_dia` + `hang_nang`, gồm mức 45.000 và 22.500 yêu cầu/tháng; rà soát để báo cáo không còn phần mẫu B1–B4 bị lặp.
- Đối chiếu chi phí giới hạn chạy lại 1/2/3 lần; ghi nhận giới hạn 2 lần có tổng chi phí hệ thống thấp nhất, khoảng 6,901 triệu đồng.

### Bằng chứng

- `src/lab13.py`: các phép tính A4, B1, B3, B4 và kịch bản kết hợp B2.
- `report/team/bang_chi_phi.md`: bảng A4, B1–B4 và kết luận về giới hạn 2 lần.
- Các phép tính có thành phần phút `*_simulated`; cần chạy lại `python lab13.py` với đủ thư viện và kiểm tra đầu ra trước khi nộp.
