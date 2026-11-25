# Báo cáo cá nhân — NguyenAnhQuan-2A202603892

## 1. Thông tin thành viên

- Họ tên: Nguyễn Anh Quân
- MSSV: 2A202603892
- Email: 2A202603892@vinuni.edu.vn
- Vai trong nhóm: Người giữ hồ sơ kiêm Phụ trách Thiết kế Kế hoạch Pilot (Nhiệm vụ D) & Đóng gói Hồ sơ Launch v0 (Nhiệm vụ E)

## 2. Phần việc phụ trách

- **Nhiệm vụ D (CP4 · Kế hoạch Pilot):**
  - Tính toán và giải 5 bài toán cỡ mẫu D1 (a, b, c, d, e), xác định hệ số thiết kế (DE) và trần cỡ mẫu hiệu dụng khi phân cụm theo nhân viên và bưu cục.
  - Phân tích và chỉ rõ đánh đổi thống kê khi số nhân viên bị giới hạn (40 người), đề xuất giải pháp khả thi nâng MDE lên 6% ($m \ge 299$).
  - Trả lời 5 câu hỏi cốt lõi về tính nhận diện tác động can thiệp (D2).
  - Soạn thảo và hoàn thiện toàn bộ file `report/team/pilot_plan.yaml` sạch 100% dấu `?`, xây dựng 3 luật dừng chuẩn cú pháp `NẾU – TRONG – THÌ – KHÔNG THÌ`.
- **Nhiệm vụ E (CP5 · Chỉ số, Rủi ro, Hồ sơ Launch v0 & Hội đồng Gate 2a):**
  - Tính toán và đặc tả 3 chỉ số từ tập dữ liệu 1.200 requests (Chính: 82,83%, Dùng: 27,12%, An toàn: 4,25%), đề xuất 2 chỉ số mở rộng (Dùng và An toàn).
  - Thiết kế danh sách 10 nghiệp vụ trace events chuẩn hoá có gắn `trace_id` trong `report/team/chi_so.md`.
  - Phân tích 3 rủi ro kinh tế trọng yếu (làm lại x2, xem lại 100%, sụt giảm khối lượng) lấy số liệu từ Bảng độ nhạy.
  - Tổng hợp toàn bộ kết quả của nhóm thành bản Hồ sơ Launch v0 đúng 1 trang tại `report/team/ho_so_launch_v0.md` với đề xuất chiến lược "Go có điều kiện" và 5 điều kiện tiên quyết.

## 3. Đóng góp cụ thể

- Tính toán chính xác trần cỡ mẫu hiệu dụng $n_{\text{eff}} < c / \text{ICC} = 20 / 0.02 = 1.000$, chứng minh về mặt toán học không thể đạt mức chênh 5 điểm với 40 nhân viên hiện có, qua đó thuyết phục nhóm chọn mức chênh 6% ($m \ge 299$) và minh bạch rủi ro Power = 0,64 nếu hiệu quả thực tế chỉ là 5%.
- Xây dựng 3 luật dừng thực tế bảo vệ an toàn cho hệ thống và uy tín khách hàng (dừng khi tỉ lệ mở lại > 6% hoặc chênh >= 2 điểm so với đối chứng), khống chế trần chi phí mỗi việc thành công không quá 8.000 đ.
- Đề xuất điều kiện thứ 5 mang tính đột phá về "Đào tạo & Quản trị thay đổi" (Change Management) cho 100% nhân viên can thiệp trước ngày kích hoạt bot.
- Chuẩn bị đầy đủ cơ sở lý lẽ phản biện và câu hỏi chất vấn để bảo vệ hồ sơ trước Hội đồng Gate 2a.

## 4. Bằng chứng

- File kế hoạch pilot: [report/team/pilot_plan.yaml](pilot_plan.yaml) (hợp lệ YAML, không còn dấu `?`).
- File đặc tả chỉ số & rủi ro: [report/team/chi_so.md](chi_so.md).
- File hồ sơ launch: [report/team/ho_so_launch_v0.md](ho_so_launch_v0.md).
- Mã nguồn tính cỡ mẫu và các commit trên nhánh `AnhQuanHANU`.

## 5. Công cụ AI đã dùng

- Công cụ: Antigravity Assistant.
- Mục đích sử dụng: Tra cứu công thức toán thống kê (cỡ mẫu so sánh hai tỉ lệ, DE, ICC), format markdown bảng biểu và kiểm tra tính hợp lệ cú pháp YAML.
- Tự kiểm tra: Tự tính toán lại toàn bộ các phương trình cỡ mẫu, kiểm tra logic các vế luật dừng và rà soát kỹ lưỡng không vi phạm bất kỳ quy tắc nào của bài lab (tuân thủ quy tắc chỉ duyệt kế hoạch pilot, gắn nhãn `simulated` đầy đủ).

## 6. Tự đánh giá

- Hoàn thành xuất sắc toàn bộ khối lượng công việc được giao của Phần D và Phần E.
- Đảm bảo tính nhất quán số liệu giữa các tài liệu, hồ sơ chặt chẽ, khoa học, sẵn sàng bảo vệ thành công trước Hội đồng Gate 2a.
