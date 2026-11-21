# Hồ sơ launch v0 · LogiX-VN · Gate 2a

Trần Việt Tiến — 2A202603394 · Nhóm VOI · L3A. Dữ liệu giả lập; bản đối chiếu main `fa4ffa2` ngày 21/11/2026.

| Mục | Kết quả chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | Toàn mẫu **4.472 đ**; nội địa + hàng nặng **3.414 đ**. Cộng cố định thành **4.599 đ** ở 45.000 yêu cầu toàn công ty/tháng, **5.784 đ** khi giảm nửa khối lượng; đều **simulated**. | Giả lập | Người kiểm số |
| 2 · Ba yếu tố nhạy nhất | Làm lại ×2 tăng **51,8%**; xem lại ×2 tăng **40,7%**; lương +25% tăng **23,1%**, đều **simulated**. | Giả lập | Người kiểm số |
| 3 · So với nhân viên tự làm | Chọn **noi_dia + hang_nang**, 982 yêu cầu. Chi phí hệ thống gồm nhân viên xử lý 82 ca thất bại là **4.131 đ/yêu cầu, simulated**, trước cố định, so với 12.000 đ tự làm. Quốc tế thành công **27,3%**, chi phí **22.515 đ/việc, simulated**; đối tác có điều khoản riêng. | Giả lập | PM trợ lý hoàn phí |
| 4 · Chỉ số và event | Chính **994/1.200 = 82,83%**; sửa/bỏ gợi ý **48/177 = 27,12%**; mở lại **51/1.200 = 4,25%**. Đề xuất thêm 2 chỉ số và **12 event** có trace_id. | Xong, có bằng chứng | Người giữ hồ sơ Gate 2a |
| 5 · Lỗi và khắc phục | Có **20 nhãn Người 3**, khắc phục **5 loại**. Người 4 báo đã xong nhãn nhưng bảng chung còn chờ cập nhật; mục tiêu đồng thuận **≥16/20**. | Chưa | Người phụ trách phân loại lỗi |
| 6 · Pilot plan | Phạm vi 12 depot, chia theo nhân viên **20 cụm/nhánh**, đối chứng đồng thời, MDE **6 điểm**, **299 yêu cầu/người**, DE **6,96**, n hiệu dụng **859,2/nhánh**. Power nếu tác động chỉ +5 điểm còn **0,64**. Quyết định **05/01/2027**. | Xong, có bằng chứng | Người thiết kế pilot |
| 7 · Rủi ro kinh tế | Làm lại ×2 lên **6.787 đ/việc**; xem lại 100% lên **11.743–12.415 đ/việc** theo hai giả định B4, đều **simulated**, trước cố định. | Giả lập | Giám đốc vận hành |

Điều kiện cần kiểm tra vào **23/11/2026**, mốc đề xuất trước khi bật pilot.

- **Người thiết kế pilot và người phụ trách lỗi** đưa bộ nhãn thứ hai vào bảng, tính đồng thuận; **Kỹ sư trưởng agent** kiểm thử chống hoàn trùng và đối soát sổ cái.
- **Người thiết kế pilot** chốt seed, ngày bắt đầu, lịch thu đủ mẫu và theo dõi 7 ngày, tiêu chí kết luận; **Giám đốc vận hành** ký đánh đổi MDE 6 điểm và ba luật dừng trong D, rollback trong 30 phút.
- **Trưởng nhóm CSKH** bật event, đo phút thực tuần 1, đề xuất giảm xem lại có kiểm tra an toàn; **Người giữ hồ sơ** nhận xác nhận chạy trên máy thứ hai và cập nhật duyệt chéo.

Nguồn gồm [A/B](bang_chi_phi.md), [C](bang_loi.md), [D](pilot_plan.yaml) và [E](chi_so.md). Mục 6 ghi nhận kế hoạch đã được viết. Đề xuất và lịch kiểm tra cần nhóm thông qua; kết quả duyệt chéo chờ thực hiện.

**Đề xuất — Go có điều kiện cho pilot noi_dia + hang_nang sau khi hoàn tất các điều kiện trên.**
