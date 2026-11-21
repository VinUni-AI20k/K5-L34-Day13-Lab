# Báo cáo nhóm · Bản tổng hợp trên main

## 1. Thông tin và phạm vi

- Repo: `K5-L3A-DAY13-Random23-LaunchEconomics`; lớp L3A.
- Tên nhóm và danh sách thành viên chính thức: chờ điền trong `TEAM.md`.
- Mục tiêu: hồ sơ Gate 2a cho pilot trợ lý hoàn phí LogiX-VN trên dữ liệu giả lập của lab; chưa phải kết quả pilot có đối chứng.

## 2. Tổng hợp nguồn đóng góp

| Nhánh | Phần được tổng hợp |
| --- | --- |
| thanhthuy | Code A1–A4, B1–B4; báo cáo chi phí, rủi ro và bản nháp báo cáo nhóm/hồ sơ; báo cáo cá nhân được giữ trong file theo MSSV |
| manh | Tính tay kiểm chứng A1; báo cáo CP1–CP2; code D1 và baseline mở lại tại commit c28ae2c |
| truong | Bản code A/B ở commit 3e43cfa, đã có trong lịch sử main |
| duongnguyen | Hai bộ nhãn do người dùng cung cấp, xác nhận TV4 theo thông tin người dùng, bảng khắc phục năm loại; thiết kế pilot và đối chiếu kinh tế |

Không suy ra thời điểm gắn nhãn hoặc danh tính đầy đủ chỉ từ tên nhánh. Đóng góp chi tiết cần các thành viên xác nhận trong `TEAM.md`.

## 3. Kết quả chính

A1 đạt ba phép thử 1,20 · 1,25 · 1,25. A2 cộng chi phí mọi lần chạy, kể cả lỗi, rồi chia 978 việc thành công: **4.472 đ/việc [simulated]**. Trong phạm vi nội địa + hàng nặng, cộng cố định ở giả định 45.000 yêu cầu/tháng: **4.599 đ/việc**, giảm nửa khối lượng: **5.784 đ/việc [simulated]**. Chi tiết: [bảng chi phí](bang_chi_phi.md).

B1: làm lại ×2 tăng CPS 51,8%; xem lại ×2 tăng 40,7%; lương tăng 25% làm CPS tăng 23,1% [simulated]. B3 toàn mẫu: giới hạn hai lần có tổng chi phí hệ thống thấp nhất **6.901.220 đ [simulated]**. B4 xem lại mọi gợi ý trong phạm vi pilot: **11.743–12.415 đ/việc [simulated]**, chưa gồm cố định; không bảo đảm tiết kiệm so với baseline 12.000 đ.

C: hai bộ nhãn trùng **20/20 = 100%**. Khác biệt mô tả bộ 2 đã được đối chiếu với đề; người dùng xác nhận TV4 đã xác nhận. Giữ nguyên hai bộ ban đầu, chốt nhãn thống nhất và bảng khắc phục ca **9, 7, 18, 4, 17**, đủ năm loại. Chi tiết: [bảng lỗi](bang_loi.md).

D1: cần **1.251 yêu cầu/nhóm** cho +5 điểm. Với 40 nhân viên, chia theo nhân viên không đủ cỡ mẫu hiệu dụng để nhắm +5 điểm; phương án đề xuất chấp nhận +6 điểm, **20 nhân viên/nhóm × 299 yêu cầu/người**, DE=6,96, cỡ mẫu hiệu dụng khoảng 859/nhóm. Power chỉ khoảng 0,64 nếu tác động thật là +5 điểm. Chưa thể kết luận tác động thực của trợ lý từ dữ liệu chạy thử không đối chứng.

## 4. Tiến độ checkpoint và phần còn lại

| Checkpoint | Trạng thái của bản tổng hợp |
| --- | --- |
| CP1 | Hoàn thành code A và bảng A; mọi chi phí suy ra từ thời gian giả lập phải giữ nhãn simulated |
| CP2 | Hoàn thành code B và bảng B; đã làm rõ chi phí toàn hệ thống và giả định B4 |
| CP3 | Hoàn thành hai bộ nhãn, đồng thuận và năm dòng khắc phục; còn bổ sung họ tên/thời điểm chốt và liên kết event với E |
| CP4 | Đã có D1 trong lab13.py; YAML có thiết kế, luật dừng, rollback nhưng còn chờ ngày quyết định, xác nhận nguồn lực và duyệt các ngưỡng/phạm vi |
| CP5 | Mới có hai dòng rủi ro kinh tế và hồ sơ tổng hợp đang cập nhật; bảng chỉ số, event, kết luận cuối chưa hoàn tất |
| Đóng gói | Chưa có kết quả duyệt chéo; thiếu TEAM.md hoàn chỉnh và báo cáo riêng của các thành viên còn lại |

## 5. Hạn chế và bước tiếp theo

TV4 hoàn thiện ba chỉ số tính thử, hai chỉ số tự đề xuất, ít nhất sáu event có trace_id và cách tính từ event trong [chi_so.md](chi_so.md). Nhóm chốt phạm vi, trần chi phí, ngày bắt đầu/ngày quyết định và khả năng đủ mẫu trong [pilot_plan.yaml](pilot_plan.yaml). Sau đó hoàn thiện [hồ sơ launch](ho_so_launch_v0.md), chọn Go / Go có điều kiện / No-go và ghi điều kiện theo vai trò, thời hạn. Duyệt chéo được ghi từ hoạt động thực tế trong [phieu_cham.md](phieu_cham.md); chưa có thì không điền điểm hoặc quyết định giả định.

## 6. Nguồn và bằng chứng

Code nộp: `src/lab13.py`; dữ liệu: hai CSV gốc không sửa. Bằng chứng nhãn và xác nhận được lưu tại `bang_loi.md`; D1 có script đối chiếu độc lập `src/tv3_pilot_checks.py`. Nguồn yêu cầu: README.md, CHECKPOINTS.md, RUBRIC.md, SUBMISSION.md và đề bài trong docs/.
