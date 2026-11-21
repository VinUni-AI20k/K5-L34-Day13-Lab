# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: PD
- Lớp: L3A
- Thành viên: xem `TEAM.md` (Bùi Anh Dũng, Phụng, Mai Văn Thanh)

## 2. Mục tiêu và cách tiếp cận

Trả lời bốn câu cho trợ lý hoàn phí LogiX-VN trước Gate 2a: có đáng chạy không, nhân viên có dùng không, khi hỏng thì sao, pilot phải thiết kế thế nào. Nhóm tính chi phí thật từ trace (tử số gồm mọi lần chạy kể cả lần lỗi, mẫu số chỉ đếm việc thành công), tìm yếu tố nhạy nhất, phân loại lỗi theo năm loại của Google PAIR, rồi thiết kế pilot đủ cụm và có luật dừng viết trước. Nhóm 3 người nên một người giữ hai vai; người viết code đổi sau giờ giải lao để hai người tự tay tính được chi phí.

## 3. Giải pháp

- **A · Chi phí** (`bang_chi_phi.md`, `src/lab13.py`): ba phép thử A1 đạt; `mo_hinh` tính từ trace; tách theo loại; cộng chi phí cố định 40 triệu đ/tháng cho phạm vi noi_dia + hang_nang.
- **B · Độ nhạy** (`bang_chi_phi.md`): 9 kịch bản đổi từng yếu tố, một cặp, giới hạn 1/2/3 lần chạy, xem lại 100%. Tự kiểm: "giảm một nửa" bằng đúng nửa mức tăng của "gấp đôi".
- **C · Bảng lỗi** (`bang_loi.md`): hai người gắn nhãn 20 ca, đồng thuận 18/20 = 90% (lệch ca 8 và 13); quy tắc cho ca lệch; bảng khắc phục 5 ca đủ năm loại, mỗi dòng có event, ngưỡng, tần suất và một vai phụ trách.
- **D · Pilot** (`pilot_plan.yaml`): tính đủ năm câu D1 trước khi chọn cách chia; chọn chia theo nhân viên 20 + 20; bốn luật dừng (an toàn, hoàn trùng, chi phí, mức độ sử dụng); điều kiện đủ 40 nhân viên và lịch thu mẫu + 7 ngày theo dõi.
- **E · Chỉ số, rủi ro, hồ sơ** (`chi_so.md`, `ho_so_launch_v0.md`): ba chỉ số tính thử, 8 event có `trace_id`, 3 dòng rủi ro kinh tế lấy số từ bảng độ nhạy; hồ sơ một trang bảy mục.

## 4. Kết quả

- Chi phí mỗi việc thành công **4.472 đ** [simulated], gấp **16,3 lần** hoá đơn token + tool chia số yêu cầu; giờ nhân viên chiếm 92,5%. Cả hệ thống 5.865 đ/yêu cầu = **0,49×** của 12.000 đ [simulated].
- Theo loại: noi_dia 0,22×, hang_nang 0,69×, quoc_te 1,88×, doi_tac 0,85× [simulated] → phạm vi pilot chỉ noi_dia + hang_nang (cộng cố định: 4.599 đ = 0,38×) [simulated].
- Ba yếu tố nhạy nhất: số ca làm lại (+51,8%), tỉ lệ xem lại (+40,7%), lương (+23,1%) [simulated]. Xem lại 100% thì 0,98×–1,03×, gần như không tiết kiệm [simulated].
- Chỉ số trong đợt chạy thử: chính 82,83%, bỏ qua gợi ý 27,12%, mở lại 7 ngày 4,25%.
- Pilot: chia theo nhân viên 20 + 20, MDE 6 điểm (859/nhóm, DE 6,96). Con số bất lợi: power chỉ 0,64 nếu tác động thật là 5 điểm.
- Đề xuất: **Go có điều kiện** cho pilot noi_dia + hang_nang.
- Kết quả duyệt chéo từ hội đồng: ... / 30, quyết định ..., câu hỏi: ...

## 5. Khó khăn và cách xử lý

- Với 40 nhân viên, không cách chia theo cụm nào đủ mẫu cho mức chênh 5 điểm (20 người/nhóm tối đa 1.000 < 1.251). Nhóm chấp nhận mức chênh 6 điểm và ghi rõ power 0,64 trong hồ sơ thay vì giấu đi.
- Tỉ lệ mở lại hiện tại 4,25% (3,97% trong phạm vi) nên ngưỡng tuyệt đối 3% sẽ dừng pilot ngay tuần đầu; nhóm đổi sang so với đối chứng (+2 điểm) kèm trần 6%.
- Cột nhãn người 1 có đối chiếu với bảng tham khảo trong hướng dẫn, nên tỉ lệ đồng thuận 90% chỉ phản ánh độ khớp của người 2 với bộ nhãn đó; nhóm ghi rõ điều này trong `bang_loi.md`. Hai ca lệch (8, 13) đều do lẫn giữa nơi cần sửa và nguyên nhân gốc.
- Hai người cùng sửa `bang_chi_phi.md` gây xung đột khi gộp; số hai bên trùng khớp nên giữ bản chạy ra từ code. Sau đó mỗi người làm trên nhánh riêng và mở PR.
- ...

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

- Chi phí xem lại và làm lại dựa trên cột `_simulated`; phải thay bằng phút đo thật (event `staff_review_decision`, `staff_rework_completed`) sau tuần 1 của pilot.
- Đợt chạy thử không có nhóm đối chứng nên chỉ viết được "chỉ số trong đợt chạy thử là…", chưa kết luận được tác động của trợ lý.
- Mẫu 1.200 yêu cầu chỉ có 20 nhân viên và 6 depot; kết quả theo loại hang_nang (158 yêu cầu) và doi_tac (68) còn ít dữ liệu.
- ...

## 8. Tài liệu tham khảo

- Đề bài và hướng dẫn: `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`, `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`, `docs/du_lieu_va_cong_thuc.md`
- Google PAIR, *People + AI Guidebook*, chương Errors + Graceful Failure.
- Dữ liệu giả lập: `src/logix_runs.csv`, `src/logix_requests.csv`.
