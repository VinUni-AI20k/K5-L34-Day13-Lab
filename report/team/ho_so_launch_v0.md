# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: 3boy · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ [simulated] (gấp 16,3 lần hóa đơn token và tool chia số yêu cầu là 274,7 đ; giờ nhân viên chiếm 92,5% tổng chi phí) | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | 1. Số ca làm lại (+51,8%), 2. Tỉ lệ xem lại (+40,7%), 3. Lương nhân viên (+23,1%); Giá token tăng gấp đôi chỉ làm tăng +5,6% | Giả lập | Kỹ sư trưởng agent |
| 3 · So với nhân viên tự làm | Cả hệ thống: 5.865 đ = 0,49× [simulated] của 12.000 đ. Trong phạm vi pilot: noi_dia 2.696 đ (0,22×), hang_nang 8.221 đ (0,69×); Loại quoc_te (1,88×) | Giả lập | PM trợ lý hoàn phí |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chính: 82,83% (đóng trong 24h & không mở lại 7 ngày), Dùng: 27,12% (bỏ qua gợi ý), An toàn: 4,25% (lỗi lọt đến khách); 10 event có trace_id | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | 20 ca lỗi phân loại đủ 5 loại Google PAIR; 5 ca khắc phục mẫu đủ event phát hiện đo được và một vai trò chịu trách nhiệm | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | Phạm vi noi_dia + hang_nang; Chia theo 20 đối chứng + 20 can thiệp (MDE 6%, m ≥ 299 đơn/người); 3 luật dừng chuẩn NẾU – TRONG – THÌ – KHÔNG THÌ | Xong, có bằng chứng | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Làm lại x2 (+51,8% lên 6.787 đ); Xem lại 100% vọt lên 11.743 đ – 12.414 đ (0,98× – 1,03×); Cố định 40tr/tháng (+2.370 đ/việc nếu khối lượng giảm nửa) [simulated] | Giả lập | PM trợ lý hoàn phí |

**Đề xuất:** Go có điều kiện (cho kế hoạch pilot phạm vi `noi_dia` và `hang_nang`).

Các điều kiện tiên quyết để được bấm chạy pilot:
1. **Kỹ thuật (Idempotency & Ledger):** Kỹ sư trưởng agent bổ sung cơ chế khóa giao dịch `idempotency_key` và quy trình đối soát tự động mỗi giờ với sổ cái kế toán để loại bỏ triệt để lỗi ghi hoàn tiền trùng (ca 7, ca 20). *Người phụ trách: Kỹ sư trưởng agent · Ngày kiểm tra: 2026-12-01.*
2. **Nghiệp vụ & Thống kê (Phê duyệt đánh đổi Power):** Giám đốc vận hành ký phê duyệt chấp nhận đánh đổi cỡ mẫu ở mức chênh 6 điểm phần trăm (MDE = 0,06) với Power kiểm định đạt 0,64 trong trường hợp mức chênh thực tế chỉ là 5 điểm. *Người phụ trách: Giám đốc vận hành LogiX-VN · Ngày kiểm tra: 2026-12-05.*
3. **Giám sát & Dữ liệu đo thật (Trace & Instrumentation):** Kích hoạt đầy đủ 10 event nghiệp vụ có gắn `trace_id` trong hệ thống; thay thế hoàn toàn số phút giả lập (`_simulated`) bằng số phút đo thực tế từ đồng hồ bấm giờ trên giao diện CSKH sau tuần đầu tiên của bước rollout 0.10. *Người phụ trách: Kỹ sư trưởng agent · Ngày kiểm tra: 2026-12-12.*
4. **Kinh tế & Kiểm soát chi phí (Lộ trình giảm xem lại):** Trưởng nhóm CSKH ban hành quy trình giảm tỉ lệ xem lại theo bậc (từ 100% xuống 50% rồi 20%) khi tỉ lệ nhân viên sửa hoặc bỏ qua gợi ý duy trì dưới 15%, nhằm tránh rủi ro chi phí trợ lý đắt hơn người tự làm (11.743 đ – 12.414 đ) ở kịch bản xem lại 100%. *Người phụ trách: Trưởng nhóm CSKH · Ngày kiểm tra: 2026-12-08.*
5. **Đào tạo & Quản trị thay đổi (Change Management & Training):** 100% nhân viên CSKH thuộc nhóm can thiệp (20 nhân viên) hoàn thành khóa đào tạo 2 giờ về quy trình phối hợp người-máy (Human-in-the-loop), nắm vững thao tác thẩm định đơn, phản hồi sửa/bỏ và đạt tối thiểu 80% điểm bài kiểm tra tình huống nghiệp vụ trước khi cấp quyền sử dụng trợ lý ở bước rollout 0.10. *Người phụ trách: Trưởng nhóm CSKH · Ngày kiểm tra: 2026-12-07.*
