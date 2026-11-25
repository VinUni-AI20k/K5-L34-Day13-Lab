# Báo cáo cá nhân — NguyenTheBao-2A202603825

## 1. Thông tin thành viên

- **Họ tên** Nguyễn Thế Bảo
- **MSSV** 2A202603825
- **Email** 26ai.baont4@vinuni.edu.vn
- **Vai trong nhóm** Người 3 · Người gắn nhãn 1

## 2. Phần việc phụ trách

- **Chính · CP3 (Nhiệm vụ C)** — Gắn nhãn độc lập 20 ca lỗi theo nguyên nhân gốc, đối chiếu với Người 4, tính tỉ lệ đồng thuận và lập bảng khắc phục cho 5 ca, mỗi loại một ca.
- **Phụ · CP1** — Theo dõi điều kiện “Xong khi”, kiểm tra nhãn `simulated` và yêu cầu câu trả lời ngắn có số liệu.
- **Phụ · CP4** — Phối hợp xây dựng ba luật dừng, điều kiện tách tác động (`identifiability`) và phương án quay về luồng thủ công (`rollback`).
- **Phụ · CP5 và duyệt chéo Gate 2a** — Đối chiếu chỉ số với danh sách event có `trace_id` và hỗ trợ rà soát bằng chứng khi duyệt chéo.

## 3. Đóng góp cụ thể

### CP3 · Bộ nhãn 20 ca lỗi

- Đã ghi đủ **20/20 nhãn** ở cột “Nhãn người 1”. Bộ nhãn gồm 4 ca Do người dùng, 5 ca Hệ thống, 4 ca Ngữ cảnh, 4 ca Giới hạn hệ thống và 3 ca Ngầm.
- Bảng nhóm đang chờ bộ nhãn của Người 4. Khi có đủ hai bộ nhãn, tỉ lệ đồng thuận bằng số ca trùng chia 20. Mốc đạt là **16/20 ca (80%)**. Mỗi ca lệch cần một câu quy tắc phân biệt. Nếu dưới mốc, cần rà lại định nghĩa và giữ nguyên hai cột nhãn ban đầu.
- Bảng khắc phục trong hồ sơ nhóm còn trống. Mỗi dòng cần chỉ rõ event phát hiện, ngưỡng, tần suất kiểm tra, cách xử lý và một vai trò phụ trách.

### CP4 · Đối chiếu luật dừng và phương án quay lui

- Mốc mở lại trong 7 ngày là **4,25%** trên toàn mẫu và **3,97%** trong phạm vi `noi_dia` + `hang_nang`. Luật an toàn dùng cửa sổ **3 ngày liên tiếp** để theo dõi tỉ lệ mở lại cao hơn đối chứng từ **2 điểm phần trăm**, vượt **6%** tuyệt đối, hoặc có ít nhất **1 ca hoàn trùng**. Khi kích hoạt luật, Giám đốc vận hành tắt trợ lý trong **30 phút** và chuyển yêu cầu về luồng thủ công.
- Hai luật còn lại theo dõi chi phí mỗi việc thành công vượt **8.000 đ [simulated]** trong **2 tuần** liên tiếp và tỉ lệ bỏ qua gợi ý vượt **40%** trong **1 tuần**. Kế hoạch dùng nhóm đối chứng chạy đồng thời và phân quyền theo `staff_id` để giảm ảnh hưởng giữa hai nhóm.

### CP5 · Đối chiếu chỉ số với event

Đặc tả nhóm có **9 event chứa `trace_id`**. Bảng dưới đây ghi các event dùng để tính từng chỉ số.

| Chỉ số | Event và cách tính |
| --- | --- |
| Đóng trong 24 giờ và không mở lại trong 7 ngày · **994/1.200 (82,83%)** | Nối `refund_request_created`, `ticket_closed` và `ticket_reopened` theo `trace_id`. Tính 24 giờ từ lúc nhận đến lúc đóng, rồi kiểm tra yêu cầu đã qua đủ 7 ngày sau khi đóng. |
| Bỏ qua gợi ý · **48/177 (27,12%)** | Lấy số yêu cầu có quyết định `sua` hoặc `bo` chia số yêu cầu được xem lại từ `staff_review_decision`. |
| Lỗi lọt đến khách · **51/1.200 (4,25%)** | Lấy số yêu cầu mở lại trong 7 ngày từ `ticket_reopened` chia tổng số yêu cầu từ `refund_request_created`. |
| Yêu cầu được mở bằng trợ lý | Đếm yêu cầu có `agent_suggestion_shown` trên tổng yêu cầu từ `refund_request_created` của nhóm can thiệp. |
| Hoàn sai số tiền qua kiểm tra mẫu | Từ `audit_sample_checked`, chia số mẫu có số tiền đã hoàn khác số tiền đúng cho tổng số mẫu đã kiểm tra. |

## 4. Bằng chứng

- Commit `86d3d06` (`gán nhãn`) bổ sung 20 dòng ở cột “Nhãn người 1”. [Bảng lỗi](bang_loi.md#hai-bộ-nhãn-độc-lập)
- Hồ sơ nhóm ghi ba luật dừng, `identifiability` và `rollback`. [Kế hoạch pilot](pilot_plan.yaml)
- Đặc tả nhóm ghi các event và phép tính chỉ số. Ba kết quả tính thử có thể đối chiếu với CSV. [Đặc tả chỉ số](chi_so.md) · [Dữ liệu yêu cầu](../../src/logix_requests.csv)

## 5. Công cụ AI đã dùng

- **ChatGPT (Codex)** hỗ trợ soạn báo cáo từ phân công, lịch sử Git và hồ sơ nhóm.
- **Cách kiểm tra bản báo cáo** — Đối chiếu commit `86d3d06` với 20 dòng nhãn trong bảng lỗi, đếm số event có `trace_id`, rồi lọc CSV để kiểm lại các tử số và mẫu số **994/1.200**, **48/177** và **51/1.200**.

## 6. Tự đánh giá

- Phần gắn nhãn cá nhân đã đủ 20 ca. Phần cần hoàn tất ở CP3 là đối chiếu với Người 4 và chốt 5 ca khắc phục có tiêu chí phát hiện đo được.
- Khi phân loại, em cần làm rõ dấu hiệu giúp phân biệt lỗi hệ thống đã lộ ra và lỗi ngầm chỉ được phát hiện khi kiểm tra. Khi kiểm tra chỉ số, em cần đối chiếu cả mốc thời gian và mẫu số với event tương ứng.
