# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: Hihihuhu
- Lớp: L3B
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Lab 13 yêu cầu dựng hồ sơ launch v0 cho trợ lý hoàn phí của LogiX-VN (dữ liệu giả lập: 1.200 yêu cầu, 1.624 lần chạy của agent) và bảo vệ trước hội đồng Gate 2a. Nhóm trả lời bốn câu: có đáng chạy không (chi phí mỗi việc thành công), nhân viên có dùng không (chỉ số sử dụng), khi hỏng thì sao (bảng lỗi), và pilot thiết kế thế nào để ra được quyết định (đối chứng, cỡ mẫu, luật dừng).

Cách làm: ... (cách nhóm chia việc và phối hợp qua Git: ai viết code, ai kiểm số, ai gắn nhãn; một người sửa `src/lab13.py` tại một thời điểm)

## 3. Giải pháp

| Nhiệm vụ | Cách nhóm làm | File |
| --- | --- | --- |
| A · Chi phí mỗi việc thành công | ... | `src/lab13.py`, `report/team/bang_chi_phi.md` |
| B · Bảng độ nhạy | ... | `report/team/bang_chi_phi.md` |
| C · Bảng lỗi và cách khắc phục | ... | `report/team/bang_loi.md` |
| D · Kế hoạch pilot | ... | `report/team/pilot_plan.yaml` |
| E · Chỉ số, rủi ro, hồ sơ launch | ... | `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md` |

## 4. Kết quả

Con số chính (ghi nhãn `simulated` khi cần) và đề xuất cuối của `ho_so_launch_v0.md`. Kết quả duyệt chéo nhóm nhận được từ hội đồng.

- Chi phí mỗi việc thành công: ... đ [simulated]
- Ba yếu tố nhạy nhất: ... [simulated]
- Đề xuất cuối: Go · Go có điều kiện · No-go — lý do bằng số: ...
- Kết quả hội đồng chấm nhóm mình: ... / 30; nhận xét chính: ...

## 5. Khó khăn và cách xử lý

...

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

...

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, https://arxiv.org/abs/2504.13359
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure", https://pair.withgoogle.com
- Tài liệu statsmodels, lớp `NormalIndPower` (mục `stats.power`)
