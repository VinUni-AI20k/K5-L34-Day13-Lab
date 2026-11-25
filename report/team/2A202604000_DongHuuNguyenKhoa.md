# Báo cáo cá nhân — DongHuuNguyenKhoa-2A202604000

## 1. Thông tin thành viên

- Họ tên: Dong Huu Nguyen Khoa
- MSSV: 2A202604000
- Email:
- Vai trong nhóm: người gắn nhãn 2, kiêm giữ hồ sơ

## 2. Phần việc phụ trách

- CP3: gắn nhãn độc lập 20 ca lỗi, so nhãn, bảng khắc phục 5 ca (`bang_loi.md`).
- CP5: hồ sơ launch v0 (`ho_so_launch_v0.md`), danh sách event và kiểm tra chéo chỉ số (`chi_so.md`).

## 3. Đóng góp cụ thể

...

## 4. Bằng chứng

Commit, file, bảng hoặc con số do bạn làm.

...

## 5. Công cụ AI đã dùng

Công cụ nào, dùng vào việc gì, bạn tự kiểm tra kết quả ra sao.

**Công cụ:** Claude Code (CLI, model Claude Opus 5.5), chạy trong repo nhóm.

| Việc | AI làm gì | Tôi kiểm tra thế nào |
| --- | --- | --- |
| Đọc đề, chia việc (14:00) | Tóm tắt README, CHECKPOINTS, RUBRIC; đề xuất chia 4 vai làm song song | Đối chiếu với bốn vai trong `TEAM.md` và lịch trong `CHECKPOINTS.md` |
| Khung hồ sơ launch v0 (CP5) | Dựng bảng bảy mục, gán người phụ trách là vai trò | Mỗi dòng có một vai trò, không có "cả đội"; trạng thái chỉ dùng ba giá trị cho phép |
| Danh sách event (CP5) | Đề xuất 10 event có `trace_id` và bảng kiểm tra chéo chỉ số ↔ event | Với từng chỉ số E1, kiểm tra tính được từ các event trong danh sách |
| Gắn nhãn 20 ca lỗi (CP3) | Gắn nhãn kèm một câu lý do cho mỗi ca; được giảng viên cho phép lúc 14:50 vì lớp bắt đầu muộn | Đọc lại từng ca theo định nghĩa năm loại; commit và push bộ nhãn trước khi xem nhãn người gắn nhãn 1 để giữ tính độc lập |
| Git | Tạo nhánh theo nhiệm vụ, commit nhỏ có tên checkpoint, push | Xem `git log` từng nhánh trước khi mở PR |

**Giới hạn đã biết:** trước khi gắn nhãn, AI đã đọc phần "Quy tắc cho các ca dễ lẫn" trong hướng dẫn chi tiết, nên bộ nhãn người 2 không hoàn toàn mù với đáp án; tỉ lệ khớp đáp án cần đọc với lưu ý này. AI không tạo con số nào trong hồ sơ: số chi phí, độ nhạy, cỡ mẫu lấy từ `src/lab13.py` và bảng của nhóm.

## 6. Tự đánh giá

...
