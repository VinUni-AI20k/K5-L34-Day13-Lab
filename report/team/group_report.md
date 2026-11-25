# Báo cáo nhóm · Lab 13 Launch Economics

Báo cáo ngắn gọn (tối đa 2 trang). Số liệu chi tiết nằm trong các file hồ sơ; ở đây tổng hợp các phát hiện chính và căn cứ ra quyết định Gate 2a.

## 1. Thông tin nhóm

- Tên nhóm: 4thangtay
- Lớp: L3B
- Thành viên: xem [TEAM.md](../../TEAM.md)

## 2. Mục tiêu và cách tiếp cận

- **Mục tiêu:** Đánh giá tính khả thi kinh tế (Launch Economics) của trợ lý AI hoàn phí LogiX-VN, xác định mô hình chi phí thực tế từ trace vận hành, nhận diện các lỗi điển hình theo chuẩn Google PAIR, và thiết kế kế hoạch thử nghiệm pilot (Gate 2a) có kiểm soát và đo lường chặt chẽ trước khi quyết định mở rộng.
- **Cách tiếp cận:**
  - Không dựa vào hóa đơn API token đơn thuần mà tính toán toàn diện chi phí mỗi việc thành công (gồm chi phí token, tool, thời gian nhân viên xem lại và làm lại).
  - Phân tầng theo 4 loại yêu cầu để tìm phạm vi có hiệu quả kinh tế rõ rệt.
  - Phân tích cỡ mẫu cụm có tính đến hệ số thiết kế ($DE = 1 + (m-1)\text{ICC}$) để tránh bẫy thiếu mẫu.
  - Thiết lập cơ chế kiểm soát rủi ro bằng 3 luật dừng định lượng theo mẫu NẾU – TRONG – THÌ – KHÔNG THÌ.

## 3. Giải pháp và các hồ sơ bàn giao

- **Nhiệm vụ A (Mô hình chi phí):** [bang_chi_phi.md](bang_chi_phi.md) & [src/lab13.py](../../src/lab13.py). Xây dựng hàm mô hình tính đúng chi phí thực tế cho mỗi yêu cầu thành công, kiểm chứng qua 3 phép thử đáp án biết trước đạt chuẩn.
- **Nhiệm vụ B (Phân tích độ nhạy):** [bang_chi_phi.md](bang_chi_phi.md). Phân tích 9 kịch bản biến động đơn yếu tố và đa yếu tố, xác định ngưỡng chi phí cả hệ thống và tác động của cơ chế xem lại 100%.
- **Nhiệm vụ C (Bảng lỗi Google PAIR):** [bang_loi.md](bang_loi.md). Gắn nhãn độc lập 20 ca lỗi, tính tỉ lệ đồng thuận, thống nhất quy tắc phân biệt và đề xuất giải pháp phát hiện/khắc phục bằng event cho 5 ca tiêu biểu.
- **Nhiệm vụ D (Kế hoạch pilot):** [pilot_plan.yaml](pilot_plan.yaml). Thiết kế thử nghiệm A/B dạng cụm trên 40 nhân viên (20 cụm mỗi nhóm), xử lý trade-off cỡ mẫu và tích hợp 3 luật dừng an toàn/chi phí/sử dụng.
- **Nhiệm vụ E (Hồ sơ launch v0):** [ho_so_launch_v0.md](ho_so_launch_v0.md) & [chi_so.md](chi_so.md). Tổng hợp hồ sơ 1 trang đủ 7 tiêu chí phục vụ hội đồng Gate 2a.

## 4. Kết quả chính

- Chi phí mỗi việc thành công toàn mẫu: **4.472 đ [simulated]**, gấp **16,3 lần** hóa đơn token + tool (274,7 đ). Làm lại chiếm 51,8%, xem lại chiếm 40,7%.
- Phạm vi tối ưu: Chỉ áp dụng cho `noi_dia` (2.696 đ, 0,22× baseline `[simulated]`) và `hang_nang` (8.221 đ, 0,69× baseline `[simulated]`). Loại bỏ `quoc_te` (22.515 đ, 1,88× baseline `[simulated]`) và `doi_tac` (10.215 đ, 0,85× baseline `[simulated]`).
- Đã tính chi phí cố định 40 triệu đ/tháng: Đạt **4.599 đ/việc (0,38×)** ở mức 45.000 yc/tháng và **5.784 đ/việc (0,48×)** ở nửa khối lượng [simulated].
- Đề xuất Gate 2a: **Go có điều kiện** (chỉ mở pilot cho nội địa + hàng nặng, kiểm soát ngưỡng mở lại trong 7 ngày không vượt trần 6%).

## 5. Khó khăn và cách xử lý

- *Khó khăn về cỡ mẫu cụm:* Với 40 nhân viên (20 người/nhóm), cỡ mẫu hiệu dụng tối đa chỉ đạt 1.000, không đủ phát hiện mức chênh 5 điểm ($n=1.251$).
- *Cách xử lý:* Nhóm chấp nhận đánh đổi (trade-off) nâng MDE lên 6 điểm ($n=859$), yêu cầu mỗi nhân viên xử lý $m \ge 299$ yêu cầu để duy trì thiết kế ngẫu nhiên cấp nhân viên, tránh rủi ro tràn tác động (spillover) khi chia theo từng yêu cầu. Ở bước 20 nhân viên can thiệp, cần khoảng 8 ngày để mỗi người đạt 299 yêu cầu; sau đó chờ đủ cửa sổ mở lại 7 ngày của yêu cầu cuối trước khi chốt chỉ số chính.

## 6. Tổng hợp đóng góp

Chi tiết phân vai và đóng góp cụ thể của từng thành viên được ghi nhận tại [TEAM.md](../../TEAM.md) và 4 báo cáo cá nhân trong `report/team/`.

## 7. Hạn chế và hướng cải thiện

- Dữ liệu thời gian xem lại và làm lại hiện tại là giả lập (`_simulated`), cần thu thập dữ liệu đo thực từ các event của nhân viên trong giai đoạn pilot.
- Cần hoàn thiện hệ thống event tracking (đặc biệt là `refund_ledger_write` và `input_validation_failed`) trước khi nâng tỉ lệ rollout lên 50%.

## 8. Tài liệu tham khảo

- Google PAIR Guidebook: Hướng dẫn phân loại lỗi và phản hồi AI.
- Tài liệu hướng dẫn Lab 13 Launch Economics và dữ liệu LogiX-VN.
