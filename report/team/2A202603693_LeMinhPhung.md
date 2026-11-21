# Báo cáo cá nhân — LeMinhPhung-2A202603693

## 1. Thông tin thành viên

- Họ tên: Lê Minh Phụng
- MSSV: 2A202603693
- Email: phung8282003@gmail.com
- GitHub: okuminhphen
- Vai trong nhóm: Người gắn nhãn 1 và người kiểm số trước giải lao, người viết code D1 sau giải lao.

## 2. Phần việc phụ trách

- **CP1:** Tính tay A1 và đối chiếu phí token, phí gọi tool ở A2.
- **CP3:** Phụ trách cột nhãn người 1 và đối chiếu bảng lỗi.
- **CP4:** Viết code cho năm câu D1 và tính tỉ lệ mở lại trong 7 ngày để nhóm chọn ngưỡng an toàn.
- **CP5:** Soát chỉ số, kiểm tra các event có `trace_id` và góp ý cho kế hoạch pilot.

## 3. Đóng góp cụ thể

- **CP1:** Đối chiếu ba kết quả A1 là 1,20 · 1,25 · 1,25. Từ `logix_runs.csv`, phí token là `(5.771.712 × 26 + 734.774 × 130) / 1.000 = 245.585,132 đ` và phí gọi tool là `5.600 × 15 = 84.000 đ`.
- **CP3:** Chuẩn bị 20 nhãn tham khảo có hỗ trợ AI, đối chiếu với hướng dẫn Lab 13. Bảng lỗi trên `main` ghi hai cột trùng 18/20 ca (90%). Hai ca lệch là ca 8 (Hệ thống) và ca 13 (Giới hạn hệ thống).
- **CP4:** Bổ sung `co_mau_hai_ti_le` và `in_d1` vào `lab13.py`. Để phát hiện chênh 5 điểm phần trăm, cần 1.251 yêu cầu mỗi nhóm nếu chia theo yêu cầu. Nếu chia theo nhân viên với 75 yêu cầu mỗi người, DE = 2,48 và cần 3.103 yêu cầu, tương đương 42 người mỗi nhóm. Với 20 nhân viên hoặc 6 depot mỗi nhóm, trần cỡ mẫu hiệu dụng lần lượt là 1.000 và 300. Với mức chênh 6 điểm, mỗi nhóm 20 người cần 859 yêu cầu hiệu dụng, tức tối thiểu 299 yêu cầu mỗi người (DE = 6,96). Nếu tác động thật là 5 điểm, power còn khoảng 0,64.
- **CP4 · An toàn:** Đối chiếu tỉ lệ mở lại trong 7 ngày là 4,25% (51/1.200) toàn mẫu và 3,97% (39/982) trong phạm vi `noi_dia` và `hang_nang`.
- **CP5:** Soát các chỉ số và cách nối event qua `trace_id`. Góp ý xác nhận đủ 40 nhân viên để chia 20 + 20 vì CSV chạy thử chỉ ghi nhận 20 người. Bản pilot trên `main` đã bổ sung mục tiêu 5.980 yêu cầu thực tế mỗi nhóm, thời gian theo dõi mở lại 7 ngày và điều kiện dừng ngay khi phát hiện hoàn tiền trùng.

## 4. Bằng chứng

- **Commit:** `d9b5aaf` (code D1, chỉ số và bảng nhãn tham khảo), `2d4f9ac` (tên cột bảng lỗi). Phần việc đã vào `main` qua PR #2.
- **File:** `src/lab13.py`, `report/team/bang_loi.md`, `report/team/chi_so.md` và `report/team/pilot_plan.yaml`.
- **Kiểm tra cuối trên `main`:** Ba phép thử A1 đều đạt, script in đủ năm câu D1, 10/10 event có `trace_id` và YAML đọc được với 5 luật dừng.

## 5. Công cụ AI đã dùng

- **Trợ lý AI của OpenAI:** Hỗ trợ viết code D1, gợi ý nhãn tham khảo cho 20 ca, đối chiếu kết quả và soạn nháp báo cáo.
- **Cách kiểm tra kết quả:** Chạy `python lab13.py` trong `src/`, đối chiếu các số A1 và D1 với hướng dẫn Lab 13, đếm số ca mở lại từ CSV và dùng `yaml.safe_load` để kiểm tra kế hoạch pilot. Với D1(e), 298 yêu cầu/người cho 858,79 yêu cầu hiệu dụng mỗi nhóm, còn 299 cho 859,20 và đạt mức 859.

## 6. Tự đánh giá

- **Làm được:** Tính và giải thích được cỡ mẫu theo yêu cầu, nhân viên và depot. Khi chia theo cụm, tăng số yêu cầu mỗi cụm chỉ đưa cỡ mẫu hiệu dụng tới gần trần số cụm chia ICC. Vì vậy việc xác nhận đủ nhân viên ảnh hưởng trực tiếp đến khả năng đo tác động của pilot.
- **Điểm cần cải thiện:**
  - Lần sau, tôi sẽ tự gắn nhãn cả 20 ca trước khi xem bảng tham khảo và ghi lý do cho các ca dễ nhầm, nhất là khi cần phân biệt lỗi đã lộ với lỗi ngầm hoặc lỗi ngoài phạm vi.
  - Khi soát pilot, tôi sẽ đối chiếu ngay từ đầu số nhân viên đủ điều kiện, lượng yêu cầu cần thu, thời gian theo dõi 7 ngày và luật dừng cho từng bước rollout.
