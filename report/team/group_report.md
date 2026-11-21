# Báo cáo nhóm — HAHAHA (Lớp L3A)

## 1. Thông tin nhóm

- Tên nhóm: HAHAHA
- Lớp: L3A
- Thành viên: xem [TEAM.md](../../TEAM.md) (Do Nhat Anh, Vũ Đức Anh, Nguyễn Thế Hoàng, Lê Hải Bắc).

## 2. Mục tiêu và cách tiếp cận

Đánh giá tính khả thi kinh tế của Trợ lý hoàn phí LogiX-VN dựa trên tập dữ liệu 1.200 yêu cầu và 1.624 lượt chạy, nhằm chuẩn bị hồ sơ bảo vệ tại cổng Gate 2a. Tiếp cận bài toán qua 5 khía cạnh:
1. **Mô hình chi phí thật:** Tính đầy đủ chi phí token, tool và giờ nhân viên (xem lại, làm lại) trên mỗi việc thành công.
2. **Phân tích độ nhạy:** Xác định yếu tố rủi ro chi phí lớn nhất và đánh giá giới hạn số lần chạy.
3. **Phân loại lỗi theo Google PAIR:** Gắn nhãn độc lập 20 ca lỗi theo nguyên nhân gốc và đề xuất giải pháp có thể đo lường.
4. **Thiết kế Pilot ngẫu nhiên có đối chứng (RCT):** Tính cỡ mẫu, hiệu ứng thiết kế cụm và xây dựng luật dừng rõ ràng.
5. **Đặc tả chỉ số & Hồ sơ Gate 2a:** Xây dựng danh sách event, quản trị rủi ro kinh tế và đưa ra đề xuất có điều kiện.

## 3. Giải pháp

- **Nhiệm vụ A (Mô hình chi phí):** Triển khai hàm `mo_hinh()` trong [lab13.py](../../src/lab13.py). Chi phí mỗi việc thành công lấy tổng chi phí chia cho số việc thành công (978 việc). Chi tiết tại [bang_chi_phi.md](bang_chi_phi.md).
- **Nhiệm vụ B (Bảng độ nhạy):** Chạy 9 kịch bản biến thiên tham số. Đánh giá kịch bản xem lại 100% cho thấy trợ lý không tiết kiệm chi phí nếu không giảm được tỉ lệ xem lại.
- **Nhiệm vụ C (Bảng lỗi & khắc phục):** Hai người gắn nhãn độc lập 20 ca theo 5 loại Google PAIR. Đạt tỉ lệ đồng thuận 17/20 (85%) và thống nhất 20/20 ca. Lập bảng khắc phục 5 ca đại diện tại [bang_loi.md](bang_loi.md).
- **Nhiệm vụ D (Kế hoạch pilot):** Thiết kế chia theo nhân viên (20 đối chứng + 20 can thiệp). Chấp nhận mức chênh MDE 6 điểm để đảm bảo đủ mẫu. Xây dựng 3 luật dừng NẾU – TRONG – THÌ – KHÔNG THÌ trong [pilot_plan.yaml](pilot_plan.yaml).
- **Nhiệm vụ E (Hồ sơ launch v0):** Tổng hợp 7 mục vào [ho_so_launch_v0.md](ho_so_launch_v0.md), đặc tả 10 event có `trace_id` trong [chi_so.md](chi_so.md).

## 4. Kết quả

- **Chi phí mỗi việc thành công:** **4.472 đ [simulated]**, gấp **16,3 lần** hóa đơn token + tool (274,7 đ). Giờ nhân viên chiếm 92,5% tổng chi phí.
- **Chi phí toàn hệ thống:** **5.865 đ/yêu cầu [simulated]** = **0,49×** so với nhân viên tự làm (12.000 đ).
- **Phạm vi pilot:** Giới hạn ở `noi_dia` (0,22×) và `hang_nang` (0,69×), loại bỏ `quoc_te` (1,88×) và `doi_tac` (0,85×).
- **Yếu tố nhạy nhất:** 1. Số ca làm lại (+51,8%) · 2. Tỉ lệ xem lại (+40,7%) · 3. Lương nhân viên (+23,1%).
- **Đề xuất cuối cùng:** **Go có điều kiện** (chỉ triển khai pilot sau khi sửa khóa chống trùng ca 7, 20; Giám đốc vận hành phê duyệt MDE 6 điểm; log đủ event đo thời gian thật và có lộ trình giảm xem lại).
- **Kết quả duyệt chéo tại Gate 2a:** Nhóm trình bày hồ sơ minh bạch, nêu rõ cả các con số bất lợi và được hội đồng đánh giá cao.

## 5. Khó khăn và cách xử lý

- *Khó khăn:* Cỡ mẫu 40 nhân viên không đủ phát hiện mức chênh 5 điểm với ICC = 0,02 (giới hạn hiệu dụng chỉ 1.000 < 1.251 yêu cầu).
- *Cách xử lý:* Nhóm tính toán và chấp nhận đánh đổi mức chênh MDE 6 điểm (cần $m \ge 299$ yêu cầu/nhân viên), đồng thời ghi nhận trung thực sự sụt giảm power (còn 0,64 nếu chênh thật là 5 điểm) để Giám đốc vận hành phê duyệt.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của 4 thành viên được ghi nhận đầy đủ tại [TEAM.md](../../TEAM.md) và các file báo cáo cá nhân tương ứng trong thư mục `report/team/`.

## 7. Hạn chế và hướng cải thiện

- Dữ liệu thời gian xem lại và làm lại hiện tại là giả định (`_simulated`). Cần thay bằng đo lường thời gian thực tế qua telemetry event ngay trong tuần đầu tiên của pilot.
- Cần tối ưu thuật toán để giảm tỉ lệ xem lại xuống dưới 15% nhằm phát huy hiệu quả cắt giảm chi phí.

## 8. Tài liệu tham khảo

- Google PAIR Guidebook (Patterns for AI Products).
- Hướng dẫn chi tiết buổi chiều Lab 13 — Launch Economics.
