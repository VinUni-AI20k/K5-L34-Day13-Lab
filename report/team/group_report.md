# Báo cáo nhóm · Lab 13: Định giá agent và lập kế hoạch pilot (LogiX-VN, Gate 2a)

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: dimuon
- Lớp: L3A
- Repo: `K5-L3A-DAY13-dimuon-LaunchEconomics`
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Xây dựng bộ hồ sơ thẩm định Gate 2a cho trợ lý hoàn phí tự động tại công ty LogiX-VN dựa trên mẫu dữ liệu 1.200 yêu cầu (1.624 lượt chạy). Cách tiếp cận tập trung vào 4 khía cạnh:
1. **Kinh tế học vận hành (Cost of Pass):** Tính toán chi phí thực tế cho mỗi yêu cầu thành công, bao gồm cả chi phí cơ hội thời gian nhân viên xem lại và làm lại.
2. **Độ nhạy chi phí:** Xác định các đòn bẩy chi phí trọng yếu để thiết lập giới hạn chạy lại và ngưỡng can thiệp tối ưu.
3. **Quản trị rủi ro lỗi (Google PAIR):** Gắn nhãn 20 ca lỗi độc lập, xây dựng cơ chế phát hiện định lượng và phân định vai trò khắc phục.
4. **Thiết kế thử nghiệm có đối chứng (RCT):** Thiết kế kế hoạch pilot phân cụm ngẫu nhiên theo nhân viên, tính toán hiệu ứng thiết kế (DE) và thiết lập các luật dừng an toàn.

## 3. Giải pháp

- **Nhiệm vụ A & B (`bang_chi_phi.md`):** Phát triển hàm mô hình hóa chi phí trong `src/lab13.py`. Vượt qua 3 phép thử A1 (1,20 · 1,25 · 1,25). Phân tách chi phí theo 4 loại yêu cầu và đánh giá 9 kịch bản độ nhạy.
- **Nhiệm vụ C (`bang_loi.md`):** Hai thành viên độc lập gắn nhãn 20 ca lỗi theo 5 phân loại Google PAIR, đạt mức đồng thuận 85,0% (17/20). Xây dựng phương án khắc phục cho 5 ca tiêu biểu với sự gắn kết vai trò trách nhiệm rõ ràng.
- **Nhiệm vụ D (`pilot_plan.yaml`):** Tính toán cỡ mẫu theo thiết kế cụm phân tầng. Chấp nhận mức chênh tối thiểu phát hiện được (MDE) là 6 điểm ($n = 859$ yêu cầu/nhóm, 20 nhân viên/nhóm) và xây dựng 3 luật dừng định lượng theo mẫu NẾU – TRONG – THÌ – KHÔNG THÌ.
- **Nhiệm vụ E (`chi_so.md`, `ho_so_launch_v0.md`):** Đặc tả 3 chỉ số đo lường hiện hữu, 2 chỉ số tự đề xuất, thiết lập cấu trúc 10 event có `trace_id` và tổng hợp hồ sơ Gate 2a một trang.

## 4. Kết quả

- **Chi phí mỗi việc thành công (CPS):** 4.472 đ toàn mẫu [simulated]. Trong phạm vi đề xuất (`noi_dia` + `hang_nang`): đạt 3.414 đ (chưa cố định) và 4.599 đ (cộng chi phí cố định ở quy mô 45.000 yc/tháng, bằng 0,38× so với 12.000 đ nhân viên tự làm) [simulated].
- **Phạm vi pilot tối ưu:** Đưa `quoc_te` (22.515 đ = 1,88×, thành công chỉ 27,3%) và `doi_tac` (10.215 đ = 0,85×) ra khỏi phạm vi pilot.
- **Giới hạn số lần chạy:** Đặt tối đa 2 lần chạy cho mỗi yêu cầu (giúp giảm tổng chi phí hệ thống xuống 6.901.220 đ [simulated]).
- **Đề xuất tại Gate 2a:** **Go có điều kiện** (kèm 4 cam kết về sửa lỗi sổ cái, ký duyệt rủi ro cỡ mẫu, bật đầy đủ log event và lộ trình giảm tỷ lệ xem lại).

## 5. Khó khăn và cách xử lý

- *Khó khăn:* Với quy mô 40 nhân viên, không có cách chia cụm nào đạt đủ cỡ mẫu cho mức chênh 5 điểm với power 0,8 (cần tới 84 nhân viên).
- *Cách xử lý:* Nâng mức MDE lên 6 điểm để giữ nguyên thiết kế RCT phân cụm theo 20 nhân viên mỗi nhóm, đồng thời ghi rõ trong hồ sơ mức suy giảm power (còn 0,64 nếu chênh lệch thực tế là 5 điểm) để cấp quản lý phê duyệt có hiểu biết.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp và minh chứng công việc của từng thành viên được khai báo chi tiết tại [`TEAM.md`](file:///F:/vinai/K5-L3A-DAY13-dimuon-LaunchEconomics/TEAM.md).

## 7. Hạn chế và hướng cải thiện

- Số phút xem lại và làm lại hiện tại hoàn toàn dựa trên dữ liệu giả lập (`_simulated`). Cần kích hoạt hệ thống đo thời gian thực qua `trace_id` trong tuần pilot đầu tiên để hiệu chỉnh lại mô hình kinh tế.
- Tỷ lệ xem lại 100% làm mất tính kinh tế của agent (CPS tăng lên xấp xỉ mức hòa vốn 12.000 đ). Cần triển khai thuật toán đánh giá độ tin cậy để chuyển dần sang kiểm tra xác suất.

## 8. Tài liệu tham khảo

- Erol et al., *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, arXiv:2504.13359.
- Google PAIR, *People + AI Guidebook* (Errors + Graceful Failure).
- Thư viện `statsmodels.stats.power` (`NormalIndPower`).
