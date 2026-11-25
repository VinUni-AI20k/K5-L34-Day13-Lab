# Báo cáo cá nhân — Nguyễn Hoàng Gia An — 2A202603799

## 1. Thông tin thành viên

- Họ tên: Nguyễn Hoàng Gia An.
- MSSV: 2A202603799.
- Email: chưa xác nhận trong phiên làm việc.
- GitHub: AnK17-UIT.
- Vai trò: Trưởng nhóm; người viết code A/B; phụ trách đặc tả chỉ số/event và kiểm tra tích hợp.

## 2. Phần việc phụ trách

| Giai đoạn theo phân công | Công việc | Sản phẩm / bằng chứng |
| --- | --- | --- |
| GĐ1 · 14:00–14:53 | Tạo src/.venv, cài requirements, A1–A4, đọc CSV giữ ô trống | lab13.py, bang_chi_phi.md; commit de4d995 đã push |
| GĐ2 · 14:53–15:35 | B1–B4, xem lại 100% với cả 9 và 15,3 phút làm lại; bàn giao minh240804 | Commit 18c079a đã push; nội dung và URL bàn giao ở report/evidence/ |
| GĐ3 · 15:35–16:36 | 5 chỉ số, đề xuất 1 chỉ số dùng và 1 chỉ số an toàn, 11 event có trace_id, bảng kiểm tra chéo, rủi ro kinh tế | chi_so.md; số E1 tính bằng lab13.py |
| GĐ4 · 16:36–18:00 | Bổ sung D1, kiểm tra YAML/từ cấm, báo cáo cá nhân, tích hợp Git | pilot_plan.yaml, bằng chứng kiểm tra trong report/evidence/ |

Mốc giờ ở bảng là lịch phân công, không phải tuyên bố thời gian thực tế đã làm từng thao tác. Theo yêu cầu cập nhật của tôi trong phiên, LMS do tôi tự nộp, không nhờ công cụ nộp hộ.

## 3. Đóng góp cụ thể

- A1 in ĐẠT: 1.20, 1.25, 1.25; tử số cộng mọi lần chạy kể cả lỗi, mẫu số chỉ 978 việc thành công. A2 cho 4.471,97 đ/việc (simulated), gấp 16,28 lần hóa đơn/1.200 yêu cầu.
- A3 tách 4 loại, quoc_te đạt 27,33% thành công và CPS 22.515,17 đ (simulated), không chọn vào pilot. A4 tính phần cố định từ 900/1.200 thành công thuộc phạm vi trên tổng mẫu.
- B1 đủ 9 kịch bản; làm lại là yếu tố mạnh nhất (+51,77%, simulated). B3: 2 lần rẻ nhất cho công ty với 6.901.220,23 đ, trong khi 1 lần có CPS thấp nhất (simulated).
- B4: 948 yêu cầu có kết quả ok được xem lại 5 phút, 48 ca làm lại, 900 việc thành công; CPS 11.742,79 đ ở 9 phút và 12.414,79 đ ở 15,3 phút làm lại (simulated). Không cộng chồng chi phí xem lại cũ.
- E1: chính 994/1.200=82,83%; bỏ qua 48/177=27,12%; mở lại 51/1.200=4,25%. Chỉ số mới: tiếp nhận trợ lý và sai tiền kiểm toán, chưa có dữ liệu để tính.
- D1: 1.251/nhánh cho MDE 5 điểm; chia staff m=75 cần 84 người; đề xuất MDE 6 điểm với 20+20 staff, m=299, DE=6,96. Power nếu thật chỉ tăng 5 điểm là 0,6417.

## 4. Bằng chứng

- Code: [lab13.py](../../src/lab13.py), dữ liệu đầu vào giữ nguyên; starter giữ nguyên.
- Bảng tính: [bang_chi_phi.md](bang_chi_phi.md); đặc tả: [chi_so.md](chi_so.md); kế hoạch: [pilot_plan.yaml](pilot_plan.yaml).
- A1–A4: commit `de4d995`; B1–B4: commit `18c079a`; các commit tích hợp sau tra bằng `git log --oneline`.
- [Output chạy thật của script](../evidence/lab13-output.txt), [biên bản kiểm tra](../evidence/kiem_tra.md), [bàn giao](../evidence/ban_giao.md), [URL bàn giao](../evidence/ban_giao-url.txt).

## 5. Công cụ AI đã dùng

Dùng OpenAI Codex để đọc yêu cầu, hỗ trợ viết code Python, soạn đặc tả event, đề xuất YAML và chạy kiểm tra. Không gọi model thật hay dùng API key trong bài lab.

Kiểm tra tự động đã thực hiện: ba assert A1; đối chiếu output A/B với hướng dẫn trong repo; bất biến độ nhạy gấp đôi/giảm nửa; xác nhận hàm không sửa DataFrame đầu vào; kiểm tra trường hợp không có thành công; so hai kịch bản B4 qua mức 12.000 đ; yaml.safe_load; quét từ cấm và dấu hỏi. Đây là kiểm tra chạy bởi công cụ trong phiên; tôi cần tự đọc, chạy lại và giải thích công thức trước khi nộp.

Không tạo bộ nhãn giả cho hai người, không tự ghi điểm hội đồng, không khẳng định thành viên #2 đã chạy lại trên máy thứ hai khi chưa có xác nhận.

## 6. Tự đánh giá

Phần A/B và đặc tả E đã có code và bằng chứng đối chiếu; số có thời gian nhân viên mang nhãn simulated. Kế hoạch D là đề xuất cần người có thẩm quyền ký duyệt. Cần bổ sung bộ nhãn độc lập, phiếu chấm chéo và xác nhận chạy trên máy thành viên #2 trước khi xem hồ sơ nhóm hoàn tất. Tôi tự nộp link repo lên LMS.
