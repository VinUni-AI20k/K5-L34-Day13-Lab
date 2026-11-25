# Biên bản kiểm tra phần Nguyễn Hoàng Gia An

Ngày làm việc: 2026-11-25 (Asia/Bangkok). Mốc giờ GĐ1–GĐ4 trong báo cáo cá nhân là lịch phân công. Toàn bộ số trong CSV do đề bài giả lập.

| Kiểm tra | Cách chạy / tiêu chí | Kết quả |
| --- | --- | --- |
| Môi trường | `cd src && .venv/bin/python -m pip check` | No broken requirements found |
| Chạy trọn bài | `cd src && .venv/bin/python lab13.py` | Thoát 0; A/B/D1/E1, output tại lab13-output.txt |
| A1 | Ba assert bắt buộc | ĐẠT: 1.20, 1.25, 1.25 |
| A2 | Tổng bốn khoản / 978 thành công | Tổng 4.373.585,13 đ; CPS 4.471,97 đ (simulated) |
| A1 mở rộng | So tổng cấp số nhân ở p=0,01/0,2/0,8/1; k=1/2/3/10; đầu vào sai | ĐẠT; xác suất sai/giới hạn không hợp lệ báo ValueError |
| B1 | Tăng gấp đôi so với giảm một nửa | Thay đổi giảm bằng nửa thay đổi tăng |
| B3 | So tổng hệ thống với CPS | Giới hạn 2 lần thấp nhất tổng, 1 lần thấp nhất CPS (simulated) |
| Dữ liệu đầu vào | So DataFrame trước/sau hàm, diff hai CSV và starter với commit gốc 4f3f1a6 | Không sửa đầu vào; hai CSV và starter giữ nguyên |
| B4 | Hai kịch bản ở hai phía baseline 12.000 đ | 11.742,79 < 12.000 < 12.414,79 (simulated) |
| D1 | Công thức hai tỉ lệ và hiệu ứng cụm | 1.251 ở 5 điểm; 859 ở 6 điểm; 5.980/6,96 =859,1954 hiệu dụng/nhánh |
| YAML | `yaml.safe_load` đọc pilot_plan.yaml; kiểm trường và bốn vế luật dừng | Đọc thành công; 5 luật có NẾU/TRONG/THÌ/KHÔNG THÌ |
| Dấu hỏi | `rg -n '\?' report/team/pilot_plan.yaml` | Không có kết quả (exit 1 là không khớp) |
| Từ cấm | `rg -n -i 'production\|cả đội' report/team/` (dùng biểu thức xen kẽ của rg) | Không có kết quả; cũng xác nhận bằng Python trên mọi file trong report/team |
| Bản vá | `git diff --check` | Không có lỗi khoảng trắng |
| Thư mục ảo | `.gitignore` có `.venv/`; kiểm bằng `git check-ignore src/.venv/pyvenv.cfg` | Không đưa thư viện hay môi trường vào commit |
| Bàn giao | Bình luận commit B1–B4 nhắc minh240804 | Đã gửi; URL lưu tại ban_giao-url.txt |

Lệnh quét từ cấm thực tế: `rg -n -i 'production|cả đội' report/team/`.

Phần chưa xác minh: thành viên #2 chạy trên máy khác; hai bộ nhãn C độc lập; kết quả duyệt chéo; thông tin thành viên 3/4 và danh tính đầy đủ thành viên #2. Các file bang_loi.md và phieu_cham.md giữ các ô mẫu để người phụ trách ghi bằng chứng thật; không tính đây là hồ sơ nhóm đã hoàn chỉnh.

pilot_plan.yaml là bản đề xuất chờ ký duyệt, có lịch minh họa cụ thể và điều kiện dịch lịch nếu trễ; không khẳng định pilot đã được phê duyệt hoặc đã chạy. LMS do Nguyễn Hoàng Gia An tự nộp theo yêu cầu cập nhật.
