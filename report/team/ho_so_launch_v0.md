# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: HAHAHA · Lớp: L3A

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ [simulated] (gấp 16,3 lần hóa đơn token + tool 274,7 đ) ([A2](bang_chi_phi.md#a2--mô-hình-từ-trace)) | Giả lập | Kỹ sư trưởng agent |
| 2 · Ba yếu tố nhạy nhất | 1. Làm lại (+51,8%) · 2. Xem lại (+40,7%) · 3. Lương NV (+23,1%) ([B2](bang_chi_phi.md#b2--đổi-một-cặp-và-xếp-hạng)) | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Cả hệ thống: 5.865 đ (0,49×) [simulated]; Pilot gồm cố định: 4.599 đ (0,38×) [simulated] ([A3](bang_chi_phi.md#a3--tách-theo-loại-yêu-cầu), [A4](bang_chi_phi.md#a4--chi-phí-cố-định)) | Giả lập | Giám đốc tài chính |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Trong đợt chạy thử: đóng 24h & không mở lại 7 ngày **82,83%** (994/1.200), sửa hoặc bỏ **27,12%** (48/177), mở lại 7 ngày **4,25%** (51/1.200) ([E1](chi_so.md#e1--đặc-tả-chỉ-số)) | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | Hai lượt gắn nhãn độc lập trùng **17/20 (85%)**. Nhãn thống nhất khớp tham khảo **20/20**, có **5** biện pháp cho 5 loại lỗi ([CP3](bang_loi.md)) | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | Chia theo nhân viên (20 đối chứng + 20 can thiệp); MDE 6 điểm (m ≥ 299 yc/NV); dừng khi mở lại > 6% ([D](pilot_plan.yaml)) | Xong, có bằng chứng | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | Chi phí gốc **4.472 đ/việc thành công**. Làm lại x2: **6.787 đ (+51,8%)**. Xem lại x2: **6.292 đ (+40,7%)**. Cả ba số là `simulated` ([E2](chi_so.md#e2--rủi-ro-kinh-tế)) | Giả lập | PM trợ lý hoàn phí |

**Đề xuất:** Go có điều kiện (cho kế hoạch pilot phạm vi `noi_dia` và `hang_nang`):

1. **Sửa khoá chống trùng và đối soát sổ cái (ca 7, 20)** trước ngày bắt đầu pilot — Kỹ sư trưởng agent phụ trách, kiểm tra ngày 2026-12-01.
2. **Ký phê duyệt chấp nhận mức chênh 6 điểm (MDE = 0,06)** với power 0,64 nếu chênh thật là 5 điểm — Giám đốc vận hành phụ trách, kiểm tra ngày 2026-12-01.
3. **Bật đủ 10 event có trace_id** và thay số phút simulated bằng số phút đo thật sau tuần 1 của pilot — PM trợ lý hoàn phí phụ trách, kiểm tra ngày 2026-12-08.
4. **Kế hoạch giảm xem lại theo bậc** khi tỉ lệ sửa/bỏ < 15%, tránh rủi ro xem lại 100% chi phí lên 12.414 đ (1,03× so với 12.000 đ) — Trưởng nhóm CSKH phụ trách, kiểm tra ngày 2026-12-15.
