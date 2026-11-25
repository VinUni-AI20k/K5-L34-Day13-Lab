# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`). Tuyệt đối không dùng thuật ngữ chạy chính thức ngoài đời thực.

Nhóm: 4thangtay · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ `[simulated]` (toàn mẫu); 2.696 đ `[simulated]` (nội địa); 8.221 đ `[simulated]` (hàng nặng); gồm cố định trong phạm vi nội địa + hàng nặng: 4.599 đ `[simulated]` (0,38×) | Giả lập | Kỹ sư trưởng agent |
| 2 · Ba yếu tố nhạy nhất | 1. Làm lại (+51,8%, lên 6.787 đ); 2. Xem lại (+40,7%, lên 6.292 đ); 3. Lương (+23,1%, lên 5.506 đ) `[simulated]` | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | 0,38× ở 45.000 yc/tháng và 0,48× ở nửa khối lượng (phạm vi `noi_dia + hang_nang`); cả hệ thống toàn mẫu 5.865 đ/yc = 0,49× mốc 12.000 đ `[simulated]` | Giả lập | PM trợ lý hoàn phí |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Mẫu dữ liệu giả lập của bài tập (chưa có nhóm đối chứng): Chính 82,83% (994/1.200); Dùng 27,12% (48/177); An toàn 4,25% toàn mẫu (3,97% trong phạm vi); đủ 11 event có `trace_id` | Xong, có bằng chứng | PM trợ lý hoàn phí |
| 5 · Bảng lỗi và cách khắc phục | 20 ca gắn nhãn (đồng thuận 100%, 20/20), 5 ca khắc phục đo bằng event, ngưỡng và tần suất | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 6 · Pilot plan | Rollout 4→10→20 nhân viên can thiệp; ở bước 20: 20 nhân viên/nhóm (40 cụm), MDE 6 điểm (859 yêu cầu hiệu dụng/nhóm; m ≥ 299 yêu cầu/người; khoảng 8 ngày lấy mẫu + cửa sổ mở lại 7 ngày), 3 nhóm luật dừng NẾU–TRONG–THÌ–KHÔNG THÌ | Xong, có bằng chứng | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Làm lại gấp đôi (+51,8%, lên 6.787 đ); Xem lại 100% kéo dài (11.743 đ = 0,98× đến 12.415 đ = 1,03× mốc 12.000 đ); Khối lượng giảm 50% (+2.370 đ/việc) `[simulated]` | Giả lập | PM trợ lý hoàn phí |

**Đề xuất:** Go có điều kiện

**Điều kiện cụ thể:**
- **Thu hẹp phạm vi & giới hạn chạy lại:** Chỉ mở pilot cho `noi_dia` và `hang_nang`, tạm loại `quoc_te` (1,88× `[simulated]`) và `doi_tac` (0,85× `[simulated]`); giới hạn tối đa 2 lần chạy (phương án rẻ nhất toàn hệ thống 6.901.220 đ `[simulated]`). Dù CPS `doi_tac` là 10.215 đ `[simulated]` (thấp hơn mốc 12.000 đ), tỉ lệ thành công chỉ 54,4% `[simulated]` và trung bình cần 1,88 lần chạy/yêu cầu `[simulated]`; tạm hoãn phân khúc này để ưu tiên hai phân khúc có tỉ lệ thành công cao hơn, rồi đánh giá lại bằng dữ liệu pilot thực ([bảng A3](bang_chi_phi.md#a3--theo-loai-yeu-cau)). *(Phụ trách: PM trợ lý hoàn phí · kiểm tra trước ngày khởi chạy.)*
- **Sửa lỗi hệ thống & thay số giả lập:** Sửa khóa chống trùng (`idempotency_key`) và đối soát sổ cái (Ca 7, Ca 20) trước khi chạy; bật đủ 11 event có `trace_id` và thay phút `simulated` bằng thời gian đo thật sau tuần 1. *(Phụ trách: Kỹ sư trưởng agent · kiểm tra cuối tuần 1.)*
- **Chấp nhận đánh đổi cỡ mẫu bất lợi:** Ký xác nhận chấp nhận **MDE 6 điểm** (power giảm còn ~0,64 nếu tác động thật chỉ 5 điểm) để giữ thiết kế 20 cụm nhân viên/nhóm, tránh tràn tác động. *(Phụ trách: Giám đốc vận hành LogiX-VN · kiểm tra trước ngày khởi chạy.)*
- **Kích hoạt luật dừng & lộ trình giảm xem lại:** Ở mọi bước, ngắt trong 30 phút nếu mở lại vượt 6%, có hoàn trùng cùng yêu cầu hoặc báo đã hoàn nhưng sổ cái chưa ghi; chỉ áp dụng ngưỡng chênh ≥ 2 điểm từ bước 10 nhân viên can thiệp; chỉ đọc chỉ số chính ở bước 20 sau khi đủ mẫu và cửa sổ mở lại 7 ngày. Ngưỡng chi phí vận hành 8.000 đ không gồm 40 triệu chi phí cố định, khoản này được xem riêng theo E2; giữ xem lại 100% ở bước 0.10 và chỉ giảm theo bậc khi tỉ lệ sửa + bỏ < 15% trong 1 tuần, đồng thời xác nhận chi phí toàn hệ thống dự báo không vượt 12.000 đ/yêu cầu. Ở kịch bản xem lại 100%, tổng hệ thống là 12.850–13.466 đ/yêu cầu `[simulated]` sau khi cộng 82 yêu cầu nhân viên xử lý thay và phân bổ 40 triệu/tháng theo 33.750 việc thành công; nếu làm lại 15,3 phút/ca, thời gian xem lại bình quân phải ≤ 4,24 phút/ca để giữ trần 12.000 đ. *(Phụ trách: Giám đốc vận hành LogiX-VN & Trưởng nhóm CSKH · mốc quyết định tổng thể: 2027-01-05; cách tính ở [B4](bang_chi_phi.md#b4--xem-lai-100)).*
