# Báo cáo cá nhân — DoanXuanDuyBao-2A202603858

## 1. Thông tin thành viên

- Họ tên: Đoàn Xuân Duy Bảo
- MSSV: 2A202603858
- Email: doanxuanduybao96@gmail.com
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): Người gắn nhãn 1 (phụ trách bảng lỗi, kế hoạch pilot, đặc tả chỉ số/event và tổng hợp rủi ro kinh tế)

## 2. Phần việc phụ trách

- **Nhiệm vụ C (`report/team/bang_loi.md`):** Gắn nhãn độc lập 20 ca lỗi; phối hợp Hùng so nhãn, tính đồng thuận và viết quy tắc phân biệt; hoàn thiện bảng khắc phục 5 ca (đủ 5 loại Google PAIR).
- **Nhiệm vụ D (`report/team/pilot_plan.yaml`):** Chủ trì D2 (5 câu tách được tác động), hoàn thiện kế hoạch pilot, rollout, luật dừng và rollback từ số liệu D1 của Hải.
- **Nhiệm vụ E (`report/team/chi_so.md`):** Đặc tả chỉ số (kết hợp số liệu Hải bàn giao), danh sách event có `trace_id`, kiểm tra chéo event–chỉ số và tổng hợp rủi ro kinh tế từ bảng độ nhạy.
- **Gate 2a & hoàn tất:** Trả lời phản biện về lỗi, pilot, luật dừng; cùng nhóm chấm chéo; soát checklist nộp bài và hoàn thiện báo cáo cá nhân.

## 3. Đóng góp cụ thể

- **Đã triển khai (đến hiện tại):**
  - Hoàn thành gắn nhãn độc lập 20 ca lỗi (`Nhãn người 1`) và bản nháp bảng khắc phục 5 ca trong `report/team/bang_loi.md` (khớp phạm vi loại `quoc_te` từ A3).
  - Sau khi pull kết quả A–B của Minh và Hải (`bang_chi_phi.md`), đã điền `scope` và luật dừng chi phí vào `report/team/pilot_plan.yaml` (cùng 5 câu D2, `owner`, `assignment`, `rollout`, `identifiability`, `rollback`, `decision_date`).
  - Hoàn thiện bảng **E2 · Rủi ro kinh tế** (3 dòng lấy số từ `bang_chi_phi.md`), 2 chỉ số tự đề xuất, 10 event có `trace_id` và phần kiểm tra chéo event–chỉ số trong `report/team/chi_so.md`.
- **Đang chờ output đồng đội để hoàn tất:**
  - Chờ Hùng gắn nhãn độc lập 20 ca để so nhãn, tính đồng thuận và chốt `bang_loi.md` (Lượt 5).
  - Chờ Hải hoàn thiện code D1 + `mo_lai_trong_7_ngay` (Lượt 6) và 3 chỉ số E1 (Lượt 8) để điền các số liệu còn lại vào `pilot_plan.yaml` và `chi_so.md`.

## 4. Bằng chứng

- Nhánh cá nhân `baodxd` với các file đã cập nhật: `report/team/bang_loi.md`, `report/team/pilot_plan.yaml`, `report/team/chi_so.md`, `report/team/2A202603858_DoanXuanDuyBao.md`.
- *(Sẽ bổ sung commit hash cuối cùng và ghi nhận duyệt chéo Gate 2a sau khi hoàn tất cả buổi)*

## 5. Công cụ AI đã dùng

- Sử dụng trợ lý AI để đọc tài liệu đề bài/hướng dẫn, trích xuất 20 ca lỗi từ file `.docx`, kiểm tra cấu trúc YAML và đối chiếu checklist của rubric.
- Tự kiểm tra bằng cách đối chiếu từng dòng với `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`, `CHECKPOINTS.md`, `RUBRIC.md` và `SUBMISSION.md`.

## 6. Tự đánh giá

- *(Cập nhật sau khi hoàn thành toàn bộ các phase và duyệt chéo Gate 2a)*
