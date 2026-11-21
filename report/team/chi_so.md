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
| Số ca làm lại tăng gấp đôi | Chi phí mỗi việc thành công tăng **+51,8%**, từ 4.472 đ lên **6.787 đ** (`simulated`) | Tỉ lệ làm lại theo tuần > 7% (trong đợt chạy thử: 4,9% ở phạm vi `noi_dia` + `hang_nang`) | Thu hẹp phạm vi pilot về `noi_dia`, rà soát 20 trace làm lại gần nhất | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | Chi phí trong phạm vi `noi_dia` + `hang_nang` lên **11.743 đ = 0,98×** của 12.000 đ (hoặc **12.415 đ = 1,03×** nếu làm lại 15,3 phút/ca như dữ liệu, `simulated`); không còn tiết kiệm | Tỉ lệ yêu cầu được xem lại vẫn > 50% ở cuối bước rollout 0,25 hoặc thời gian xem lại trung bình > 4,8 phút | Giảm tỉ lệ xem lại theo bậc khi tỉ lệ `sua` + `bo` < 15%; tối ưu giao diện đối chiếu nhanh | Trưởng nhóm CSKH |
| Khối lượng yêu cầu thấp hơn dự kiến | Chi phí cố định 40 triệu đ/tháng làm cộng thêm **+1.185 đ/việc** ở 45.000 yc/tháng (lên 4.599 đ = 0,38×, `simulated`), và tăng gấp đôi lên **+2.370 đ/việc** nếu khối lượng chỉ còn một nửa (lên 5.784 đ = 0,48×, `simulated`) | Số việc thành công theo tuần đạt < 50% kế hoạch (< 4.200 việc/tuần) | Tạm dừng mở rộng bước rollout, đàm phán lại gói hạ tầng chi phí cố định theo mức dùng | PM trợ lý hoàn phí |
