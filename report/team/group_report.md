# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: CATH
- Lớp: L3A
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Nhóm dựng bộ hồ sơ launch v0 cho trợ lý hoàn phí của LogiX-VN nhằm trả lời bốn câu hỏi: (1) có đáng chạy không, (2) nhân viên có dùng không, (3) khi hỏng thì sao, (4) pilot thiết kế thế nào. Cách tiếp cận: chia bốn vai (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ), hoàn thành tuần tự 5 nhiệm vụ A–E, đối chiếu số sau mỗi checkpoint.

## 3. Giải pháp

- **Nhiệm vụ A** (Mô hình chi phí): viết 3 hàm kinh tế chạy lại (A1), hàm `mo_hinh` tính chi phí mỗi việc thành công từ trace (A2), tách theo loại (A3), cộng chi phí cố định (A4). Kết quả: 4.472 đ/việc [simulated], gấp 16,3 lần hoá đơn. → [`bang_chi_phi.md`](bang_chi_phi.md)
- **Nhiệm vụ B** (Bảng độ nhạy): 9 kịch bản B1, xếp hạng 3 yếu tố, B3 giới hạn chạy lại, B4 xem lại 100%. → [`bang_chi_phi.md`](bang_chi_phi.md)
- **Nhiệm vụ C** (Bảng lỗi): gắn nhãn 20 ca lỗi theo 5 loại Google PAIR, hai bộ nhãn khớp 20/20, cả hai bộ có AI hỗ trợ; Hà đã tự rà và xác nhận, Ánh đã review và xác nhận bộ của mình ngày 21/11. Bảng khắc phục 5 ca đủ 5 loại. → [`bang_loi.md`](bang_loi.md)
- **Nhiệm vụ D** (Pilot plan): tính cỡ mẫu, chọn chia theo nhân viên 20+20, mức chênh 6 điểm, 3 luật dừng. → [`pilot_plan.yaml`](pilot_plan.yaml)
- **Nhiệm vụ E** (Chỉ số, rủi ro, hồ sơ): 3 chỉ số + 2 chỉ số đề xuất, 8 event có `trace_id`, 2 dòng rủi ro kinh tế + cảnh báo B4, ghép hồ sơ 7 mục. → [`chi_so.md`](chi_so.md), [`ho_so_launch_v0.md`](ho_so_launch_v0.md)

## 4. Kết quả

- **Chi phí mỗi việc thành công:** 4.472 đ [simulated], giờ nhân viên chiếm 92,5%.
- **Chi phí cả hệ thống:** 5.865 đ/yêu cầu = 0,49× so với 12.000 đ [simulated].
- **Phạm vi pilot:** chỉ noi_dia (0,22×) + hang_nang (0,69×); loại quoc_te (1,88×) và doi_tac (0,85×).
- **Ba yếu tố nhạy nhất:** 1. Số ca làm lại (+51,8%) · 2. Tỉ lệ xem lại (+40,7%) · 3. Lương nhân viên (+23,1%).
- **Chỉ số chính trong đợt chạy thử:** 82,83% (994/1.200).
- **Đề xuất:** Go có điều kiện (sửa lỗi trùng sổ cái, ký chấp nhận 6 điểm, bật event, kế hoạch giảm xem lại).
- **Kết quả duyệt chéo:** (ghi lại tại buổi duyệt).

## 5. Khó khăn và cách xử lý

- Đọc CSV thiếu `keep_default_na=False` gây sai cột `quyet_dinh_xem_lai` → đã sửa theo hướng dẫn `src/README.md`.
- Ban đầu chia pilot theo depot vì dễ triển khai → tính lại thấy chỉ tối đa 300 mẫu hiệu dụng, không đủ → chuyển sang chia theo nhân viên.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

- Mọi con số về giờ nhân viên (xem lại, làm lại) đều là **simulated** từ cột `_simulated`, chưa phải đo thật. Pilot cần thay bằng phút đo thật sau tuần 1.
- Power chỉ 0,64 nếu tác động thật chỉ 5 điểm (thay vì 6 điểm đã chọn). Nếu có thêm nhân viên hoặc kéo dài pilot, có thể cải thiện power.
- Xem lại 100% gần hoà vốn (0,98×); pilot cần học tỉ lệ xem lại có thể giảm an toàn xuống mức nào.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, [arxiv.org/abs/2504.13359](https://arxiv.org/abs/2504.13359)
- Google PAIR, *People + AI Guidebook*, chương "Errors & Graceful Failure", [pair.withgoogle.com](https://pair.withgoogle.com)
- Tài liệu statsmodels, lớp `NormalIndPower` (mục `stats.power`)
