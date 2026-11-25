# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: Neon
- Lớp: L3A
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Nhóm trả lời câu hỏi của Gate 2a: có nên chạy pilot trợ lý hoàn phí của LogiX-VN không, và pilot phải thiết kế thế nào để ra được quyết định. Cách làm có ba điểm chính:
- Mọi con số do `src/lab13.py` tính. Người kiểm số tính lại độc lập bằng script riêng để đối chiếu.
- Mỗi file hồ sơ có một chủ file, người khác gửi nội dung để chủ file ghép vào.
- Mỗi thành viên làm trên nhánh riêng, ghép vào `main` qua pull request.

Phân công chi tiết theo từng checkpoint nằm trong `TEAM.md` và `PHAN_CONG_CHI_TIET.md`.

## 3. Giải pháp

| Nhiệm vụ | Cách làm | File |
| --- | --- | --- |
| A · Chi phí | Hàm `mo_hinh` cộng token và tool trên mọi lần chạy, kể cả lần lỗi, cộng thêm phút xem lại và làm lại; chia cho số yêu cầu `thanh_cong`. Tách theo `loai`, cộng chi phí cố định cho phạm vi `noi_dia` + `hang_nang` | [bang_chi_phi.md](bang_chi_phi.md) |
| B · Độ nhạy | 9 kịch bản, mỗi kịch bản đổi một tham số; một kịch bản đổi cặp; giới hạn 1/2/3 lần chạy tính chi phí cả hệ thống; xem lại 100% | [bang_chi_phi.md](bang_chi_phi.md) |
| C · Bảng lỗi | Hai người gắn nhãn độc lập 20 ca theo 5 loại Google PAIR, so nhãn, thống nhất ca lệch bằng quy tắc nguyên nhân gốc, điền bảng khắc phục 5 ca | [bang_loi.md](bang_loi.md) |
| D · Pilot | Tính đủ 5 câu D1 trước khi chọn cách chia; tính tỉ lệ mở lại hiện tại trước khi đặt luật an toàn | [pilot_plan.yaml](pilot_plan.yaml) |
| E · Hồ sơ | Tính thử 3 chỉ số, liệt kê 11 event có `trace_id`, 3 dòng rủi ro kinh tế; ghép A–D thành hồ sơ 7 mục | [chi_so.md](chi_so.md), [ho_so_launch_v0.md](ho_so_launch_v0.md) |

## 4. Kết quả

- **Chi phí mỗi việc thành công:** **4.472 đ** (`simulated`), gấp **16,3 lần** hoá đơn token + tool chia số yêu cầu (274,7 đ). Giờ nhân viên chiếm 92,5% tổng chi phí.
- **Phạm vi:** `quoc_te` không đáng chạy (1,88× so với 12.000 đ, thành công 27,3%, chạy lại không giúp). Pilot chỉ gồm `noi_dia` + `hang_nang`: cộng chi phí cố định là 4.599 đ = 0,38× (`simulated`).
- **Yếu tố nhạy nhất:**
  - Số ca làm lại: +51,8%
  - Tỉ lệ xem lại: +40,7%
  - Lương nhân viên: +23,1%

  Giá token gấp đôi chỉ làm tăng 5,6%. Giới hạn 2 lần chạy rẻ nhất cho công ty (6.901.220 đ, `simulated`).
- **Bảng lỗi:** đồng thuận 18/20 = 90%.
- **Pilot:** chia theo nhân viên 20 + 20, mức chênh 6 điểm, m ≥ 299, DE 6,96. Con số bất lợi: power chỉ 0,64 nếu tác động thật là 5 điểm.
- **Chỉ số trong đợt chạy thử:**
  - Chính: 82,83%
  - Bỏ qua gợi ý: 27,12%
  - Mở lại trong 7 ngày: 4,25%
- **Đề xuất cuối:** **Go có điều kiện**, với 4 điều kiện. Mỗi điều kiện có người phụ trách và ngày kiểm tra trong `ho_so_launch_v0.md`.
- **Kết quả duyệt chéo nhóm nhận được từ hội đồng:** *(điền sau buổi duyệt chéo: quyết định, điểm C6–C8, câu hỏi và câu trả lời của nhóm)*

## 5. Khó khăn và cách xử lý

- Trên Windows, lệnh kiểm tra `yaml.safe_load(open('../report/team/pilot_plan.yaml'))` báo `UnicodeDecodeError`. Lý do: Python đọc file bằng bảng mã mặc định cp1252, mà file có tiếng Việt. Bản mẫu gốc của đề cũng lỗi như vậy. Cách xử lý: chạy với `PYTHONUTF8=1` (PowerShell: `$env:PYTHONUTF8=1`); khi đó file đọc được, đủ 11 trường, 3 luật dừng.
- Nhiều người cùng sửa một file dễ xung đột git. Nhóm áp dụng quy tắc chỉ chủ file gõ vào file, và mỗi người làm trên nhánh riêng rồi mở pull request.
- *(Thành viên bổ sung khó khăn khác gặp trong buổi, nếu có.)*

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

- Phút xem lại và làm lại là số giả lập, mà giờ nhân viên chiếm 92,5% chi phí. Kết luận về chi phí còn phụ thuộc vào việc đo phút thật sau tuần 1 của pilot.
- Đợt chạy thử không có nhóm đối chứng, nên chưa biết tác động thật của trợ lý lên chỉ số chính.
- Với 40 nhân viên, pilot chỉ đủ mẫu để thấy mức chênh 6 điểm. Nếu tác động thật là 5 điểm, có 36% khả năng pilot không phát hiện được.
- Phút làm lại trong dữ liệu trung bình 15,3 phút/ca, cao hơn giả định 9 phút của đề. Ở mức này, xem lại 100% đắt hơn nhân viên tự làm (1,03×).

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, arXiv:2504.13359.
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure".
- Tài liệu statsmodels, `statsmodels.stats.power.NormalIndPower` và `statsmodels.stats.proportion.proportion_effectsize`.
- `docs/du_lieu_va_cong_thuc.md`, `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` của đề bài.
