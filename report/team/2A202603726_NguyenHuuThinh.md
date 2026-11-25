# Báo cáo cá nhân — Nguyễn Hữu Thịnh — 2A202603726

## 1. Thông tin thành viên

- Họ tên: Nguyễn Hữu Thịnh
- MSSV: 2A202603726
- Email: 26ai.thinhnh2@vinuni.edu.vn
- Vai trong nhóm: P4 — người gắn nhãn 2 kiêm giữ hồ sơ

## 2. Phần việc phụ trách

Tôi phụ trách tổng hợp số liệu P1 và P2 bàn giao vào bảng chi phí, chuẩn bị phần gắn nhãn 2 và bảng khắc phục lỗi, viết phần đo lường và rủi ro kinh tế, rồi tóm tắt bằng chứng vào hồ sơ launch v0 và báo cáo nhóm.

## 3. Đóng góp cụ thể

- **Nhiệm vụ A và B.** Điền bảng A1–A4 và B1–B4 từ kết quả bàn giao. Ghi riêng chi phí trợ lý trên mỗi việc thành công, chi phí biến đổi cả hệ thống trên mỗi yêu cầu và chi phí sau khi cộng cố định ở hai mức khối lượng. [Bảng chi phí](bang_chi_phi.md)
- **Nhiệm vụ C.** Chuẩn bị phiếu gắn nhãn 20 ca, đưa bộ nhãn P3 từ PR #3 vào bảng và đối chiếu với bộ nhãn tham khảo. Kết quả **20/20** là độ khớp với bảng tham khảo. Tôi soạn biện pháp cho **5 ca thuộc 5 loại lỗi**, gồm tín hiệu phát hiện, ngưỡng, tần suất, hành động và vai trò phụ trách đề xuất. [Bảng lỗi và cách khắc phục](bang_loi.md)
- **Nhiệm vụ E.** Điền ba chỉ số tính thử từ P2, đề xuất hai chỉ số bổ sung và đặc tả **11 event** có `trace_id`. Đối chiếu các event với công thức chỉ số, bảng khắc phục và luật dừng của pilot. Soạn hành động cho rủi ro làm lại tăng và xem lại 100% kéo dài. [Đặc tả chỉ số và rủi ro](chi_so.md)
- **Hồ sơ nhóm.** Tổng hợp số liệu, bằng chứng bảng lỗi và kế hoạch pilot từ PR của P3 vào hồ sơ launch v0. Soạn phần tổng hợp kết quả, khó khăn và giới hạn trong báo cáo nhóm. [Hồ sơ launch](ho_so_launch_v0.md) · [Báo cáo nhóm](group_report.md)

## 4. Bằng chứng

- **4.472 đ/việc thành công `simulated`** trên toàn mẫu và **5.865 đ/yêu cầu `simulated`** cho chi phí biến đổi cả hệ thống. Hai số sử dụng mẫu số khác nhau và được ghi đúng đơn vị. [Bảng chi phí](bang_chi_phi.md) · [Mục 1 và 3 hồ sơ launch](ho_so_launch_v0.md)
- **Ca 20** có đề xuất dùng khóa chống trùng theo quyền hoàn phí và cảnh báo khi có từ hai giao dịch thành công khác mã cho cùng quyền hoàn phí. [Bảng khắc phục](bang_loi.md#bảng-khắc-phục-cho-5-ca-mỗi-loại-một-ca)
- Bảng E1 ghi **82,83% (994/1.200)** cho chỉ số chính, **27,12% (48/177)** cho tỷ lệ sửa hoặc bỏ gợi ý trong nhóm đã xem lại, và **4,25% (51/1.200)** cho tỷ lệ mở lại trong bảy ngày. [Bảng chỉ số](chi_so.md#e1--đặc-tả-chỉ-số)

## 5. Công cụ AI đã dùng

Tôi dùng ChatGPT/Codex để hỗ trợ đọc đề, rà nội dung bàn giao của P1 và P2, chuẩn bị bản nháp, điền báo cáo Markdown và kiểm tra tính nhất quán giữa các file. Khi kiểm tra số, tôi dùng kết quả của P1 và P2 làm nguồn đối chiếu và dùng Codex kiểm lại từ CSV. Ví dụ, tỷ lệ sửa hoặc bỏ gợi ý dùng **48/177** vì mẫu số chỉ gồm yêu cầu đã được xem lại. Với phần C, Codex so từng nhãn của P3 trong PR #3 với bảng tham khảo của lab. Báo cáo ghi rõ nguồn khi trình bày tỷ lệ **20/20**. [Mô tả dữ liệu và công thức](../../docs/du_lieu_va_cong_thuc.md) · [PR #3 của P3](https://github.com/ddkhoa2605/K5-L3B-DAY13-MKTT-LaunchEconomics/pull/3/files)

## 6. Tự đánh giá

Phần đóng góp chính của tôi là đưa số liệu đã kiểm vào đúng mục và ghi rõ phạm vi, mẫu số, đơn vị của từng con số. Ví dụ, kịch bản xem lại 100% có thể lên **12.415 đ/việc thành công `simulated`**, vượt mốc **12.000 đ**, nên đề xuất pilot gắn việc giảm xem lại với thời gian theo dõi mở lại. Các bước nhóm cần xác nhận là bộ nhãn gốc của hai người, phân công E2 và các điều kiện trước khi mở pilot. [Bảng chi phí](bang_chi_phi.md#b4--nếu-phải-xem-lại-tất-cả) · [Hồ sơ launch](ho_so_launch_v0.md)
