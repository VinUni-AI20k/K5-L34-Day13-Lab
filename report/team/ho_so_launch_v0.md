# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: Stech · Lớp: L3A

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | **4.472 đ** toàn mẫu (gấp **16,3×** hoá đơn token+tool 274,7 đ); phạm vi `noi_dia` + `hang_nang` cộng cố định: **4.599 đ** ở 45.000 yc/tháng (**5.784 đ** ở nửa khối lượng) [simulated] | Giả lập | Người kiểm số |
| 2 · Ba yếu tố nhạy nhất | 1. Số ca làm lại (**+51,8%** khi ×2) · 2. Tỉ lệ xem lại (**+40,7%** khi ×2) · 3. Lương nhân viên (**+23,1%** khi +25%) [simulated] | Giả lập | Người viết code |
| 3 · So với nhân viên tự làm | Toàn hệ thống trong mẫu: **5.865 đ/yc = 0,49×** của 12.000 đ; giới hạn **2 lần chạy** rẻ nhất (**6.901.220 đ**); xem lại 100% lên **11.743–12.415 đ (0,98×–1,03×)** [simulated] | Giả lập | Người kiểm số |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Đợt chạy thử: chính **82,83%** (994/1.200), bỏ qua gợi ý **27,12%** (48/177), mở lại 7 ngày **4,25%** (51/1.200); đủ 10 event có `trace_id` | Xong, có bằng chứng | Người giữ hồ sơ |
| 5 · Bảng lỗi và cách khắc phục | Đồng thuận **20/20 (100%)** giữa 2 bộ nhãn độc lập; đủ bảng khắc phục 5 ca theo 5 loại Google PAIR (ngưỡng giám sát đề xuất cho pilot) | Xong, có bằng chứng | Người gắn nhãn 1 |
| 6 · Pilot plan | Chia theo nhân viên **20 + 20**, MDE **6 điểm** (`n = 859`, `m >= 299`, `DE = 6,96`; power còn ~0,64 nếu tác động thật 5 điểm); phạm vi `noi_dia` + `hang_nang` (loại `quoc_te` 1,88×, `doi_tac` 0,85×); đủ 3 luật dừng | Xong, có bằng chứng | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Làm lại ×2 đẩy chi phí lên **6.787 đ (+51,8%)**; xem lại 100% kéo dài lên **0,98×–1,03×**; khối lượng giảm nửa tăng cố định thêm **+1.185 đ/việc** [simulated] | Giả lập | PM trợ lý hoàn phí |

**Đề xuất:** **Go có điều kiện**

- **Điều kiện 1 (Triển khai kiểm soát lỗi trước khi chạy pilot):** Cài đặt đủ 5 cơ chế phát hiện/khắc phục đã đề xuất trong `bang_loi.md` (đặc biệt khoá chống trùng lệnh hoàn tiền và đối soát sổ cái mỗi giờ) — **Người phụ trách:** Kỹ sư trưởng agent · **Ngày kiểm tra:** trước ngày mở rollout `0.10`.
- **Điều kiện 2 (Giữ chặt phạm vi & giới hạn chạy lại):** Chỉ pilot trên `noi_dia` (0,22×) và `hang_nang` (0,69×) [simulated], loại `quoc_te` (1,88×) và `doi_tac` (0,85×), đặt giới hạn tối đa **2 lần chạy** (rẻ nhất cho toàn hệ thống: 6.901.220 đ [simulated]) — **Người phụ trách:** PM trợ lý hoàn phí · **Ngày kiểm tra:** trước ngày mở rollout `0.10`.
- **Điều kiện 3 (Kiểm soát tỉ lệ xem lại & cỡ mẫu):** Theo dõi thời gian xem lại dưới mức hoà vốn 4,8–5,1 phút [simulated], giữ tỉ lệ mở lại 7 ngày không vượt đối chứng ≥ 2 điểm hoặc trần 6%, và ghi nhận rõ đánh đổi MDE 6 điểm (`power` ~0,64 nếu tác động thật là 5 điểm) tới ngày quyết định — **Người phụ trách:** Giám đốc vận hành LogiX-VN · **Ngày kiểm tra:** `2027-01-05`.
