# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | ... |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | ... |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | ... |
| Dùng | Nhóm tự đề xuất: ... | ... | Không cần tính |
| An toàn | Nhóm tự đề xuất: ... | ... | Không cần tính |

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| ... | ... | ..., trace_id | ... |
| ... | ... | ..., trace_id | ... |
| ... | ... | ..., trace_id | ... |
| ... | ... | ..., trace_id | ... |
| ... | ... | ..., trace_id | ... |
| ... | ... | ..., trace_id | ... |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- ...

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | CPS tăng 51,8%, từ 4.472 lên 6.787 đ/việc [simulated] | Ngưỡng đề xuất: làm lại theo tuần > 7%; 4,9% là baseline trong phạm vi, còn tác động +51,8% là B1 toàn mẫu | Giữ giới hạn phạm vi `noi_dia` + `hang_nang`; nếu vẫn tăng lỗi thì tạm thu hẹp về `noi_dia` và rà 20 trace làm lại | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | 11.743 đ/việc (0,98× baseline) nếu làm lại 9 phút; 12.415 đ (1,03×) nếu dùng 15,3 phút trung bình [simulated] | Tỉ lệ xem lại còn > 50% cuối bước rollout 0,25 hoặc thời gian xem lại trung bình > 4,8 phút | Giảm xem lại theo bậc khi tỉ lệ sửa + bỏ dưới 15%; đo thời gian thật sau tuần 1 | Trưởng nhóm CSKH |
