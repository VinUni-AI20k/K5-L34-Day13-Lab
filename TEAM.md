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
|   3 | Ngô Chí Vĩnh    | 2A202603724 | 26ai.vinhnc2@vinuni.edu.vn | NgChiVinh | Người kiểm số; phụ trách Nhiệm vụ D |
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
- Kiểm số Nhiệm vụ A: tính tay từ tổng các cột CSV. Token 245.585 đ; tool 84.000 đ; phần lần chạy 2–3 là 93.804 đ; tổng 4.373.585 đ (simulated); chi phí mỗi việc thành công 4.373.585 ÷ 978 = 4.472 đ (simulated); hoá đơn chia số yêu cầu 274,7 đ. Cả sáu số khớp code của Lâm.
- Đối chiếu số A3, A4 trong `pilot_plan.yaml` với output code A của Lâm: khớp.
- Kiểm tra chéo luật dừng với nhãn ca 7, 20 trong `bang_loi.md` và danh sách event trong `chi_so.md`.

### Bằng chứng

- Commit `615f021` trên nhánh `nhiem-vu-D-Vinh`; PR #4.
- `python lab13.py` chạy từ đầu đến cuối, in phần D1 ở cuối.
- `pilot_plan.yaml` đọc được bằng `yaml.safe_load`, không còn `?` ngoài dòng chú thích.
- Báo cáo cá nhân: `report/team/2A202603724_NgoChiVinh.md`.
