# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Phạm vi đề xuất khi quay lại Gate 2a: `noi_dia` + `hang_nang`, 982/1.200 yêu cầu; loại `quoc_te` (CPS 22.515 đ, 27,3% thành công) và `doi_tac` (CPS 10.215 đ, điều khoản riêng), các CPS đều **simulated**.

Nhóm: TSNQ · Lớp: L3A. Đây là đề xuất của người giữ hồ sơ để nhóm thống nhất, chưa phải quyết định hội đồng.

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | Toàn mẫu 4.472 đ/việc; phạm vi 4.599 đ/việc đã cộng cố định 40 triệu/tháng, giả định tổng lượng 45.000 yêu cầu/tháng và giữ cơ cấu mẫu; **simulated**. | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | Làm lại gấp đôi: +51,8%, lên 6.787 đ; xem lại gấp đôi: +40,7%, lên 6.292 đ; lương +25%: CPS +23,1%, lên 5.506 đ; toàn mẫu, **simulated**. | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Theo quy ước B3: 5.865 đ/yêu cầu so với 12.000 đ, toàn mẫu, chưa cố định; 2 lần chạy rẻ nhất: 6.901.220 đ/1.200 yêu cầu; **simulated**. Chưa kết luận tiết kiệm thực tế: cần loại phần làm lại có thể tính trùng. | Giả lập | Giám đốc tài chính |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Đợt chạy thử: 994/1.200 = 82,83% đóng 24h, không mở lại 7 ngày; sửa/bỏ 48/177 = 27,12%; mở lại 51/1.200 = 4,25% (phạm vi 39/982 = 3,97%). Không có đối chứng; đặc tả 10 event trong [chi_so.md](chi_so.md). | Chưa | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | Có 20 nhãn người 2 (Sơn và Toàn khai gắn trong buổi chiều ngày lab, chưa có phiếu gốc ghi giờ) và 5 ca khắc phục đủ 5 loại; Toàn xác nhận nhãn trùng 20/20; tính độc lập chưa được xác minh. Mốc cần đạt ≥16/20 = 80%; giữ bản gốc trước khi so, xem [bảng lỗi](bang_loi.md). | Chưa | Người gắn nhãn 2 kiêm giữ hồ sơ |
| 6 · Pilot plan | Plan đã điền: chia theo nhân viên 20 + 20, mức chênh 6 điểm, 3 luật dừng, rollback 30 phút, ngày quyết định 2027-01-05 (đề xuất). D1: cần 1.251 quan sát độc lập/nhóm cho +5 điểm; 20 nhân viên/nhóm có hiệu dụng <1.000. Phương án +6 điểm cần 859 hiệu dụng/nhóm, 299 yêu cầu/người, DE 6,96; đánh đổi chờ Giám đốc vận hành ký. | Chưa | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Xem lại 100%: 11.743 đ/việc ở 9 phút làm lại; 12.415 đ ở 15,3 phút, vượt 12.000 đ. Nửa lượng toàn hệ thống 22.500 yêu cầu/tháng làm CPS phạm vi cộng cố định lên 5.784 đ; **simulated**. | Giả lập | PM trợ lý hoàn phí |

Nguồn số: [đầu ra đã lưu](../../src/ket_qua_lab13.txt), [bảng chi phí](bang_chi_phi.md), [kiểm số](kiem_so.md). Người giữ hồ sơ đã cung cấp output chạy lại A1–E1 trên máy cá nhân: A1 ĐẠT, toàn bộ output khớp bản đã lưu khi bỏ qua khoảng trắng. CPS/việc thành công khác mẫu số với chi phí/yêu cầu, không suy ra mức tiết kiệm bằng cách chia trực tiếp CPS cho 12.000 đ.

Để quay lại cổng: người kiểm số xác nhận công thức và giả định từ kết quả A1–E1 đã chạy lại; hai người gắn nhãn cung cấp bản độc lập thực tế, ghi bất đồng riêng; kỹ sư trưởng kiểm thử ghi sổ, chống hoàn trùng ca 7/20; đo phút thực sau tuần 1. Giám đốc vận hành duyệt đánh đổi nếu chọn +6 điểm (hướng dẫn ước tính power chỉ khoảng 0,64 khi tác động thật +5 điểm); PM chốt phương án giảm xem lại an toàn. Hoàn tất trước lần duyệt lại Gate 2a, ngày do nhóm thống nhất.

**Đề xuất: No-go** cho việc bắt đầu pilot ở trạng thái hồ sơ hiện tại; quay lại Gate 2a sau khi có bằng chứng hoàn tất các việc trên.
