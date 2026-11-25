# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Nhom4Nguoi · L3B · Dữ liệu chạy thử simulated; đề xuất pilot, chưa phê duyệt.

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí/việc thành công | A2 4.471,97 đ; A4 nội địa + hàng nặng: 4.599,09 đ (gồm 1.185,19 đ cố định ở 45.000 yêu cầu/tháng), simulated | Giả lập | Người kiểm số |
| 2 · Ba yếu tố nhạy nhất | Làm lại ×2 +51,77%; xem lại ×2 +40,70%; lương +25% +23,12%, simulated | Giả lập | Người viết code |
| 3 · So với nhân viên | B3 gồm làm thay 5.864,65 đ/yêu cầu (0,49×12.000 đ); B4 xem lại 100%: 11.742,79 đ/việc ở 9 phút, 12.414,79 đ ở 15,3 phút, simulated | Giả lập | Người kiểm số |
| 4 · Chỉ số, dùng, an toàn | Chính 82,83% (không có đối chứng); bỏ qua gợi ý 27,12%; mở lại 4,25%; thiết kế 11 event có trace_id | Xong, có bằng chứng | Trưởng nhóm |
| 5 · Lỗi và khắc phục | 17/20 trùng (85%); 3 bất đồng thống nhất; khắc phục đủ 5 loại | Xong, có bằng chứng | Người gắn nhãn 2, kiêm giữ hồ sơ |
| 6 · Pilot | Nội địa + hàng nặng; 20 nhân viên/nhánh, ngẫu nhiên theo depot; rollout 10/25/50%; MDE +6 điểm, n hiệu dụng 859/nhánh, DE 6,96, ≥299 yêu cầu/nhân viên; power 0,6417 ở +5 điểm; chốt 2027-01-05 | Chưa | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | Làm lại ×2: CPS 6.786,90 đ (+51,77%); xem lại 100%/15,3 phút: 12.414,79 đ (>12.000 đ); nửa khối lượng: cố định/việc 1.185,19 → 2.370,37 đ, simulated | Giả lập | PM trợ lý hoàn phí |

**Điều kiện trước pilot (hạn 27/11/2026):**

- **Kỹ sư trưởng agent:** khóa chống trùng và đối soát sổ cái; kiểm thử không trùng, 27/11/2026.
- **Giám đốc vận hành:** ký chấp nhận MDE/power tradeoff; PM khóa roster, seed, kế hoạch phân tích, 27/11/2026.
- **Trưởng nhóm CSKH:** kiểm event/trace_id ở hai nhánh, 27/11/2026; đo phút thật sau tuần đầu, 07/12/2026.
- **Người gắn nhãn 2, giữ hồ sơ:** lưu hai bộ nhãn, 3 bất đồng và bảng khắc phục; trưởng nhóm kiểm, 27/11/2026.

**Đề xuất: Go có điều kiện.**
