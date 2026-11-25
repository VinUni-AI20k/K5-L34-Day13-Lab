# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: MoiNgayMotNhom · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | **4.472 đ** mỗi việc thành công (978/1.200 yêu cầu), gấp **16,3 lần** hoá đơn token + tool chia số yêu cầu (274,7 đ). Giờ nhân viên chiếm 92,5% tổng chi phí, trong đó làm lại 51,8%. Trong phạm vi pilot noi_dia + hang_nang: 3.414 đ [simulated] | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | 1. Số ca làm lại: +51,8% khi gấp đôi / −25,9% khi giảm một nửa · 2. Tỉ lệ xem lại: +40,7% / −20,3% · 3. Lương nhân viên: +23,1% khi tăng 25%. Giá token gấp đôi chỉ +5,6% [simulated] | Giả lập | Trưởng nhóm CSKH |
| 3 · So với nhân viên tự làm (12.000 đ) | Phạm vi pilot, đã cộng cố định 40 triệu đ/tháng: **4.599 đ = 0,38×** ở 45.000 yêu cầu/tháng; 5.784 đ = 0,48× ở nửa khối lượng. Cả hệ thống, mọi loại, kể cả 222 ca nhân viên làm thay: 5.865 đ/yêu cầu = 0,49×. Bất lợi: quoc_te 22.515 đ = **1,88×**, nên loại khỏi pilot; doi_tac 0,85× sát ngưỡng, cũng loại khỏi pilot; xem lại 100% thì **0,98–1,03×** [simulated] | Giả lập | Giám đốc vận hành |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Trong đợt chạy thử, không có nhóm đối chứng: chính (đóng trong 24 giờ, không mở lại trong 7 ngày) 82,83% (994/1.200) · dùng (bỏ qua gợi ý = sửa + bỏ) 27,12% (48/177) · an toàn (mở lại trong 7 ngày) 4,25% (51/1.200), trong phạm vi pilot 3,97% (39/982). Chờ `chi_so.md` | Chưa | PM trợ lý hoàn phí |
| 5 · Bảng lỗi và cách khắc phục | Chờ CP3 (`bang_loi.md`): tỉ lệ đồng thuận …/20, phân bố năm loại lỗi, bảng khắc phục 5 ca | Chưa | Kỹ sư trưởng agent |
| 6 · Pilot plan | Chờ CP4 (`pilot_plan.yaml`). Số D1 đã tính: chia theo yêu cầu cần 1.251 yêu cầu/nhóm (+5 điểm từ 0,70); chia theo nhân viên cần 42 nhân viên/nhóm, nhưng LogiX-VN chỉ có 40; 20 nhân viên/nhóm cho cỡ mẫu hiệu dụng tối đa 1.000; 6 depot/nhóm tối đa 300; mức chênh 6 điểm với 20 nhân viên/nhóm cần 859 yêu cầu/nhóm (power ở mức 5 điểm chỉ 0,64) | Chưa | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | Chờ `chi_so.md` phần E2. Số đã có từ bảng độ nhạy: làm lại gấp đôi → 6.787 đ (+51,8%); xem lại 100% → 11.743 đ = 0,98×; khối lượng còn một nửa → chi phí cố định 2.370 đ/việc [simulated] | Chưa | PM trợ lý hoàn phí |

**Đề xuất:** (chốt sau CP5) Go · Go có điều kiện · No-go (giữ một). Go có điều kiện: ghi từng điều kiện, người phụ trách, ngày kiểm tra. No-go: ghi việc phải làm để quay lại cổng.

- Con số bất lợi đề xuất phải xử lý (từ CP1–CP2):
  - xem lại 100% thì không tiết kiệm (0,98–1,03×) [simulated];
  - quoc_te 1,88× [simulated];
  - phút xem lại và làm lại đang là số giả lập, chiếm 92,5% chi phí.
- Từ CP4 (còn chờ chốt): chia theo nhân viên thì thiếu cỡ mẫu.
