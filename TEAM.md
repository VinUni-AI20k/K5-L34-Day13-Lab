# Team

## Thông tin nhóm

- Tên nhóm: VOI
- Lớp: L3A
- Repo nhóm: `K5-L3A-DAY13-VOI-LaunchEconomics`
- URL repo: https://github.com/vuductam20022004/K5-L3A-DAY13-VOI-LaunchEconomics
- Nhánh làm việc của Người 1: `tam`
- Nhánh nộp, commit chốt:

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Vũ Đức Tâm | 2A202603522 | ductamyenphucnamdinh@gmail.com | vuductam20022004 | Code và mô hình chi phí A |
|   2 | Nguyễn Trung Duy | 2A202603387 | duy321111@gmail.com | duy321111 | Bảng chi phí và độ nhạy B |
|   3 | Chu Mai Hồng | 2A202603377 | | | Phân loại lỗi C và phiếu duyệt chéo |
|   4 | Phạm Việt Hưng | 2A202603370 | hungphamm1507@gmail.com | rachel157 | Thiết kế pilot D và gắn nhãn độc lập lần hai |
|   5 | [Trần Việt Tiến](report/team/2A202603394_TranVietTien.md) | 2A202603394 | | | Nhiệm vụ E, chỉ số, event và người giữ hồ sơ Gate 2a |

Người 1 phụ trách tích hợp `src/lab13.py`. Người 2 và Người 4 gửi lần lượt phần tính B và D1 cho Người 1. Người 2 kiểm số chi phí độc lập trước khi điền bảng. Người 3 và Người 4 giữ riêng hai bộ nhãn cho đến khi cả hai hoàn tất.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Thêm mục đóng góp cho từng thành viên theo phần việc đã thực hiện.

## Vũ Đức Tâm — 2A202603522

### Phần việc phụ trách

- Thiết lập môi trường Python, phụ trách `src/lab13.py` và bàn giao số liệu A1–A4 cho Người 2.

### Đóng góp cụ thể

- Hoàn thiện phần tính kinh tế chạy lại, mô hình chi phí từ trace, bảng chi phí theo loại yêu cầu và hai kịch bản phân bổ chi phí cố định. Chuẩn bị tham số độ nhạy và giới hạn lượt chạy cho phần B.
- Tích hợp phần B của Người 2 và phần D1 của Người 4 vào lệnh `python lab13.py`.

### Bằng chứng

- `src/lab13.py` chạy hết A1–A4, B1–B4 và D1 trên hai CSV gốc. A1 đạt 1,20 · 1,25 · 1,25. A2 ghi nhận 978/1.200 yêu cầu thành công và chi phí 4.472 đ/việc thành công [simulated].
- [Báo cáo cá nhân](report/team/2A202603522_VuDucTam.md).

## Nguyễn Trung Duy — 2A202603387

### Phần việc phụ trách

- Kiểm số A1–A4 từ mô hình của Người 1, phụ trách bảng chi phí và độ nhạy B1–B4, tổng hợp phần A–B trong báo cáo nhóm.

### Đóng góp cụ thể

- Tính chín kịch bản B1, kịch bản kết hợp B2, ba giới hạn lượt chạy B3 và hai giả định thời gian làm lại khi xem lại 100% ở B4.
- Chuẩn bị mã phần B để Người 1 tích hợp. Đối chiếu số liệu với hai CSV và ghi nhãn `simulated` cho các kết quả dùng thời gian giả lập.

### Bằng chứng

- Commit `2bad982`. [Bảng chi phí](report/team/bang_chi_phi.md), [mã phần B](src/lab13_b.py) và [báo cáo nhóm](report/team/group_report.md).
- [Báo cáo cá nhân](report/team/2A202603387_NguyenTrungDuy.md).

## Phạm Việt Hưng — 2A202603370

### Phần việc phụ trách

- Thiết kế kế hoạch pilot (Nhiệm vụ D), tính cỡ mẫu D1 bàn giao cho `src/lab13.py`, phụ trách `report/team/pilot_plan.yaml` và tham gia gắn nhãn lỗi lần hai ở Nhiệm vụ C.

### Đóng góp cụ thể

- Viết `src/lab13_d.py` tính năm câu D1 (`1.251`, `3.103`, `1.000`, `300`, `m >= 299` với `DE = 6,96`) và power thực tế (`0,6411`) khi nâng MDE từ `+5` lên `+6 điểm` với 20 nhân viên/nhóm.
- Tính các chỉ số nền từ `src/logix_requests.csv` (`mo_lai_trong_7_ngay`: `4,25%` toàn mẫu, `3,97%` trong phạm vi; tỉ lệ bỏ qua gợi ý: `27,12%` toàn mẫu, `21,09%` trong phạm vi) và hoàn thiện `report/team/pilot_plan.yaml` (`noi_dia + hang_nang` [simulated], chia theo `staff` 20+20, 5 câu D2, 3 luật dừng đủ bốn vế, rollback 30 phút).
- Hoàn thiện bộ nhãn 20 ca lỗi theo năm loại Google PAIR ở Nhiệm vụ C để đối chiếu cùng Người 3.

### Bằng chứng

- [Kế hoạch pilot](report/team/pilot_plan.yaml) (`yaml.safe_load` hợp lệ, không còn dấu `?`).
- [Code D1](src/lab13_d.py) tích hợp và chạy qua `src/lab13.py`.
- [Báo cáo cá nhân](report/team/2A202603370_PhamVietHung.md).

## Trần Việt Tiến — 2A202603394

### Phần việc phụ trách

- Nhiệm vụ E; phụ trách `chi_so.md`, `ho_so_launch_v0.md` và báo cáo cá nhân.

### Đóng góp cụ thể

- Tính ba chỉ số từ CSV, đề xuất thêm hai chỉ số và lập 12 event có `trace_id`.
- Tổng hợp ba rủi ro kinh tế từ B1/B4, ghi nhãn `simulated`.
- Viết hồ sơ Gate 2a bảy mục, chuẩn bị lời trình bày và rà soát bài nộp theo A–D.

### Bằng chứng

- [Chỉ số và rủi ro](report/team/chi_so.md) có kết quả 82,83%, 27,12%, 4,25%, công thức và danh sách event.
- [Hồ sơ Gate 2a](report/team/ho_so_launch_v0.md) đề xuất Go có điều kiện, nêu số bất lợi và các điều kiện cần nhóm xác nhận.
- [Báo cáo cá nhân](report/team/2A202603394_TranVietTien.md) ghi rõ đóng góp, công cụ AI và việc cần tự kiểm tra.
