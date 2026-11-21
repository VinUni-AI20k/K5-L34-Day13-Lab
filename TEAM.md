# Team

## Thông tin nhóm

- Tên nhóm: HAHAHA
- Lớp: L3A
- Repo nhóm: `K5-L3A-DAY13-HAHAHA-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/Ein05/K5-L3A-DAY13-HAHAHA-LaunchEconomics, nhánh `main`

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Do Nhat Anh | 2A202603701 | 26ai.anhdn6@vinuni.edu.vn | anhnhatdo175 | Người viết code |
|   2 | Vũ Đức Anh | 2A202603714 | 26ai.anhvd4@vinuni.edu.vn | Ein05 | Người gắn nhãn 2 và giữ hồ sơ |
|   3 | Nguyễn Thế Hoàng | 2A202603718 | 26ai.hoangnt3@vinuni.edu.vn | rollingthunder02 | Người gắn nhãn 1 và phụ trách chỉ số |
|   4 | Lê Hải Bắc | 2A202603710 | 26ai.baclh@vinuni.edu.vn | Lehaibac05 | Người kiểm số và viết code |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/team/` theo dạng `report/team/MSSV_HoTen.md`.

## DoNhatAnh-2A202603701

### Phần việc phụ trách

- Người 1: triển khai mô hình chi phí A1–A4 và phân tích độ nhạy B1–B4 trong `src/lab13.py`.
- Phụ trách thiết kế pilot D2–D3 và hoàn thiện `report/team/pilot_plan.yaml`.

### Đóng góp cụ thể

- Viết hàm số lần chạy kỳ vọng, xác suất thành công, hệ số chi phí và mô hình tính chi phí từ log runs/requests.
- Thêm tính chi phí theo loại, chi phí cố định, kịch bản độ nhạy, giới hạn số lần chạy, xem lại 100% và cỡ mẫu D1.
- Ghi cách chia pilot, rủi ro ảnh hưởng gián tiếp, luật dừng, rollback và đầu vào giả lập.

### Bằng chứng

- Tệp: `src/lab13.py`, `report/team/pilot_plan.yaml`, `report/team/2A202603701_DoNhatAnh.md`.

## VuDucAnh-2A202603714

### Phần việc phụ trách

- Người 4: Người gắn nhãn 2 kiêm giữ hồ sơ Gate 2a và điều phối chốt nộp.
- Khởi tạo và điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn độc lập 20 ca lỗi CP3.
- Chuẩn bị phiếu chấm Gate 2a, cập nhật `TEAM.md`, `group_report.md` và chốt bản nộp lên main.

### Đóng góp cụ thể

- Gắn nhãn độc lập 20 ca lỗi đạt tỉ lệ đồng thuận 17/20 (85%) với Người 3, thống nhất bộ nhãn đạt 20/20 nhãn chuẩn.
- Hoàn thiện hồ sơ launch v0 với đầy đủ nhãn simulated và 4 điều kiện cho đề xuất Go có điều kiện.
- Soạn thảo phiếu chấm hội đồng với 3 câu hỏi sắc bén; chủ trì rà soát checklist và đồng bộ code nhóm.

### Bằng chứng

- Tệp: `report/team/ho_so_launch_v0.md`, `report/team/bang_loi.md`, `report/team/phieu_cham.md`, `report/team/group_report.md`, `report/team/2A202603714_VuDucAnh.md`.

## NguyenTheHoang-2A202603718

### Phần việc phụ trách

- Người 3: Người gắn nhãn 1 và phụ trách phần chỉ số, event, rủi ro kinh tế.

### Đóng góp cụ thể

- Cung cấp bộ nhãn độc lập 20 ca CP3, cùng Vũ Đức Anh chốt 20/20 ca.
- Hoàn thiện đặc tả chỉ số, danh sách 10 event có `trace_id` và 3 dòng rủi ro kinh tế trong `report/team/chi_so.md`.

### Bằng chứng

- Tệp: `report/team/bang_loi.md`, `report/team/chi_so.md`, `report/team/2A202603718_NguyenTheHoang.md`.

## LeHaiBac-2A202603710

### Phần việc phụ trách

- Người 2: Người kiểm số, tính tay đối chiếu và hoàn thiện `report/team/bang_chi_phi.md`.

### Đóng góp cụ thể

- Tính tay đối chiếu các bảng chi phí A2, A3, độ nhạy B1-B4 và trả lời các câu hỏi kinh tế.

### Bằng chứng

- Tệp: `report/team/bang_chi_phi.md`, `report/team/2A202603710_LeHaiBac.md`.
