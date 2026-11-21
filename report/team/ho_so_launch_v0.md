# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: Soopi · Lớp: L3A

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 3.414 đ (4.599 đ gồm cố định) [simulated] trong phạm vi `noi_dia + hang_nang` | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | 1. Làm lại (+51,8%) · 2. Xem lại (+40,7%) · 3. Lương NV (+23,1%) [simulated] | Giả lập | Người kiểm số |
| 3 · So với nhân viên tự làm | 0,28× (hoặc 0,38× gồm cố định) [simulated]; loại `quoc_te` (1,88×) và `doi_tac` (0,85×) | Giả lập | PM trợ lý hoàn phí |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chính: 82,83% (994/1.200) · Dùng: 27,12% (48/177) · An toàn: 4,25% (51/1.200) | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 5 · Bảng lỗi và cách khắc phục | Đồng thuận 100% (20/20 ca); 5 ca khắc phục đủ 5 loại có cách phát hiện đo được | Xong, có bằng chứng | Người gắn nhãn 1 |
| 6 · Pilot plan | 20 nhân viên/nhóm, m ≥ 299 yc/người (DE = 6,96, phát hiện chênh 6 điểm, power 0,64); 3 luật dừng | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 7 · Rủi ro kinh tế | Làm lại ×2: +51,8% (6.787 đ); Xem lại 100%: 0,98×–1,03× (11.743 đ–12.414 đ); Khối lượng giảm 50%: định phí 2.370 đ [simulated] | Giả lập | PM trợ lý hoàn phí |

**Đề xuất:** Go có điều kiện (cho kế hoạch pilot phạm vi `noi_dia` + `hang_nang`).

- **Điều kiện 1:** Sửa lỗi khoá chống trùng (idempotency key) và cơ chế đối soát sổ cái hai chiều (ca 7, ca 20) trước ngày khởi chạy pilot. Phụ trách: *Kỹ sư trưởng agent*, kiểm tra hoàn tất trước ngày T-1.
- **Điều kiện 2:** Giám đốc vận hành (COO) ký văn bản phê duyệt chấp nhận mức chênh thiết kế 6 điểm (chấp nhận rủi ro power chỉ đạt 0,64 nếu mức chênh thực tế là 5 điểm do giới hạn 40 nhân viên). Phụ trách: *PM trợ lý hoàn phí*, kiểm tra trước ngày T-3.
- **Điều kiện 3:** Kích hoạt đầy đủ 10 event có `trace_id` trong hệ thống; thay thế hoàn toàn số phút giả lập (`phut_xem_lai`, `phut_lam_lai`) bằng số đo thực tế từ nhân viên sau tuần pilot đầu tiên. Phụ trách: *Kỹ sư trưởng agent*, rà soát ngày T+7.
- **Điều kiện 4:** Ban hành quy trình giảm xem lại theo bậc (staged sampling: 100% → 50% → 20%), không duy trì xem lại 100% kéo dài vì trợ lý sẽ mất hoàn toàn lợi thế kinh tế (0,98×–1,03×). Phụ trách: *Trưởng nhóm CSKH*, hoàn thành trước ngày T-2.
