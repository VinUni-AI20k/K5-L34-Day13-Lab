# Báo cáo cá nhân — HoVaTen-MSSV

## 1. Thông tin thành viên

- Họ tên: Hoàng Ngọc Minh Trí
- MSSV: 2A202603379
- Email: 26ai.trihnm@vinuni.edu.vn
- Vai trong nhóm: Người phụ trách Nhiệm vụ D, viết cấu hình và mã phần pilot.

## 2. Phần việc phụ trách

- Thực hiện D1: xác định cỡ mẫu theo yêu cầu và theo cụm nhân viên.
- Thực hiện D2: ghi các điều kiện tách được tác động (identifiability).
- Thiết lập tỉ lệ mở lại, ngưỡng an toàn và các luật dừng của pilot.
- Phụ trách `report/team/pilot_plan.yaml` và phần D trong `src/lab13.py`.
- Hoàn thiện A3 sau khi kéo mã của thành viên khác: phạm vi pilot và ngưỡng chi phí.

## 3. Đóng góp cụ thể

- Tính và cấu hình D1: chia theo yêu cầu cần 1.251 yêu cầu mỗi nhánh cho MDE 5 điểm; thiết kế được chấp nhận theo 20 cụm nhân viên mỗi nhánh dùng MDE 6 điểm, 859 yêu cầu mỗi nhánh và DE 6,96.
- Viết năm điều kiện D2 về nhóm đối chứng đồng thời, phân bổ ngẫu nhiên phân tầng depot, giảm spillover, chốt trước chỉ số/ngưỡng và đủ 20 cụm mỗi nhánh.
- Khai báo tỉ lệ mở lại baseline toàn bộ 4,25%, baseline trong phạm vi pilot khoảng 3,97%, ngưỡng chênh với đối chứng 2 điểm phần trăm và trần tuyệt đối 6%.
- Viết ba luật dừng đủ bốn vế NẾU – TRONG – THÌ – KHÔNG THÌ cho an toàn/reopen, chi phí và mức độ sử dụng.
- Hoàn thiện A3: pilot gồm `noi_dia` và `hang_nang` tại D01–D12; loại `quoc_te` và `doi_tac`; Ngưỡng chi phí pilot là 8.000 đồng cho mỗi việc thành công, chưa cộng chi phí cố định (0,67× mức 12.000 đ và khoảng 2,3 lần 3.414 đ A4 [simulated]).
- Cập nhật `lab13.py` để phạm vi được đọc từ YAML thay vì hard-code, đồng thời duy trì kiểm tra D1/D2, reopen rate và luật dừng.

## 4. Bằng chứng

- `report/team/pilot_plan.yaml`: cấu hình pilot cuối cùng, gồm phạm vi A3, ngưỡng chi phí, D1, D2, reopen rate và luật dừng.
- `src/lab13.py`: các hàm `tai_cau_hinh_pilot()` và `danh_gia_reopen_rate()` nạp, kiểm tra và dùng cấu hình này.
- Đã kiểm tra cỡ mẫu tính lại là 1.251 và 859; `baseline_scope` từ dữ liệu là khoảng 0,0397; YAML đọc được và không còn placeholder cho phần cấu hình pilot.

## 5. Công cụ AI đã dùng

- Dùng Codex để soạn cấu hình, đề xuất cách diễn đạt luật dừng và đối chiếu tính nhất quán giữa YAML với `lab13.py`.
- Tự kiểm tra bằng cách chạy `tai_cau_hinh_pilot()`, tính lại cỡ mẫu và đối chiếu `baseline_scope` với dữ liệu yêu cầu.

## 6. Tự đánh giá

Phần việc phụ trách đã được cấu hình thành các khóa có thể kiểm tra và được mã nguồn sử dụng trực tiếp. Phần A3 được hoàn thiện trên nền mã đã kéo từ thành viên khác, nên tôi tập trung vào việc thay thế phạm vi hard-code bằng cấu hình YAML và kiểm tra lại số liệu. Rủi ro còn lại là toàn bộ chương trình còn phụ thuộc vào các phần A/B do các thành viên khác hoàn thiện; phần pilot cần được kiểm tra lại khi các số liệu chi phí A3 cuối cùng thay đổi.
