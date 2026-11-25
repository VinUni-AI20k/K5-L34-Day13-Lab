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

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`, tính bằng `src/cp2_do_nhay.py`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | +51,8%, lên **6.787 đ**/việc thành công (`simulated`) | Tỉ lệ làm lại theo tuần > 7% (đợt chạy thử trong phạm vi `noi_dia` + `hang_nang`: 4,9%) | Thu hẹp phạm vi về `noi_dia`, rà soát 20 trace làm lại gần nhất | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | **11.743 đ** = 0,98× (9 phút/ca làm lại) hoặc **12.415 đ** = 1,03× (15,3 phút/ca thực tế, `simulated`) | % yêu cầu được xem lại > 50% vào cuối bước rollout 0,25 hoặc thời gian xem lại > 5,0 phút/ca | Giảm tỉ lệ xem lại theo bậc khi tỉ lệ sửa + bỏ < 15% và tối ưu giao diện đưa thời gian xem lại ≤ 4,8 phút/ca | Trưởng nhóm CSKH |
| Khối lượng yêu cầu thấp hơn dự kiến | Chi phí cố định 40 triệu đ/tháng tăng từ **+1.185 đ**/việc (45.000 yc/tháng, tổng 4.599 đ) lên **+2.370 đ**/việc ở một nửa khối lượng (tổng 5.784 đ, `simulated`) | Số việc thành công theo tuần < 50% kế hoạch | Dừng mở rộng phạm vi pilot, rà soát lại định mức và hợp đồng chi phí cố định | Giám đốc vận hành |
