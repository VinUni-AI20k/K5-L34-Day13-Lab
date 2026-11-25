# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: Hihihuhu · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ/việc [sim], toàn mẫu, chưa cộng chi phí cố định; gấp 16,28 lần cách chỉ lấy hoá đơn token + tool chia số yêu cầu (274,65 đ). Làm lại chiếm 51,77% và xem lại 40,70% tổng chi phí [sim]. — `bang_chi_phi.md` A2 | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | 1) số ca làm lại gấp đôi +51,77% 2) tỉ lệ xem lại gấp đôi +40,70% 3) lương nhân viên +25% → +23,12% [sim]. Giá token gấp đôi chỉ +5,62%. — `bang_chi_phi.md` B1, B2 | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Phạm vi `noi_dia` + `hang_nang`, 45.000 yêu cầu/tháng, đã cộng chi phí cố định 40 triệu/tháng: 4.599 đ/việc = 0,38× so với 12.000 đ; một nửa khối lượng: 5.784 đ = 0,48× [sim]. Cả hệ thống (kể cả phần nhân viên làm thay): 5.865 đ/yêu cầu = 0,49× [sim]. `quoc_te`: 22.515 đ = 1,88×, không đáng xử lý. — `bang_chi_phi.md` A3, A4 | Giả lập | PM trợ lý hoàn phí |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Trong đợt chạy thử (không có nhóm đối chứng, nên không nói "trợ lý đã nâng chỉ số"): chính 82,83% (994/1.200) đóng ≤ 24 giờ và không mở lại 7 ngày · dùng: bỏ qua gợi ý 27,12% (48/177) · an toàn: lỗi lọt đến khách 4,25% (51/1.200). Thêm 2 chỉ số đề xuất và 10 event có `trace_id`. — `chi_so.md` | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 5 · Bảng lỗi và cách khắc phục | Đồng thuận hai người gắn nhãn 12/20 = 60% (dưới mục tiêu 80%) nên đã viết lại định nghĩa 5 loại theo nguyên nhân gốc; 8 ca không trùng đã thống nhất nhãn kèm quy tắc. 5 cách khắc phục đủ 5 loại, mỗi cách có ngưỡng đo được và một vai. Hai lỗi phải sửa trước pilot: ca 7 (báo "đã hoàn" khi sổ cái lỗi 503) và ca 20 (hoàn trùng, thiếu khoá chống trùng). — `bang_loi.md` | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | Phạm vi `noi_dia` + `hang_nang`; chia ngẫu nhiên theo nhân viên 20 + 20, rollout 10% → 25% → 50% mỗi bước 1 tuần; MDE +6 điểm, 859 yêu cầu/nhóm, DE 6,96; chỉ thấy được +5 điểm với power 0,64 (cần 1.251/nhóm nếu chia theo yêu cầu). 3 luật dừng (an toàn, chi phí > 8.000 đ, bỏ qua gợi ý > 40%), rollback 30 phút, ngày quyết định 2027-01-05. — `pilot_plan.yaml` | Giả lập | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | (1) xem lại 100%: 11.743 đ = 0,98× hoặc 12.415 đ = 1,03× nếu làm lại 15,3 phút/ca [sim] → gần như không tiết kiệm. (2) giới hạn chạy lại: 1 lần rẻ nhất mỗi việc (4.111 đ) nhưng 2 lần rẻ nhất cho cả hệ thống (6.901.220 đ so với 7.449.781 đ) vì thêm 85 yêu cầu chuyển nhân viên [sim]. (3) khối lượng giảm một nửa: cố định +1.185 đ/việc, lên 2.370 đ [sim]. — `bang_chi_phi.md` B3, B4, A4; `chi_so.md` E2 | Giả lập | PM trợ lý hoàn phí |

**Đề xuất: Go có điều kiện** — chỉ cho pilot `noi_dia` + `hang_nang` theo `pilot_plan.yaml`; không mở `quoc_te` và `doi_tac`.

Căn cứ: trong phạm vi này chi phí mỗi việc thành công cộng chi phí cố định là 4.599 đ (0,38× so với 12.000 đ) và tỉ lệ mở lại 7 ngày là 3,97% (39/982) [sim]. Con số bất lợi: xem lại 100% đẩy chi phí lên 12.415 đ (1,03×), tức đắt hơn nhân viên tự làm; pilot chia 20 + 20 nhân viên chỉ thấy được mức chênh +6 điểm, nếu tác động thật là +5 điểm thì power còn 0,64; đồng thuận gắn nhãn lỗi mới đạt 60%.

Điều kiện, mỗi điều kiện có người phụ trách và ngày kiểm tra (ngày đề xuất, nhóm chốt lại theo lịch pilot):

- Sửa khoá chống trùng và chặn thông báo "đã hoàn" khi sổ cái chưa trả `ok` (ca 7, 20) trước ngày bắt đầu — Kỹ sư trưởng agent — kiểm tra 2026-12-14.
- Giám đốc vận hành ký chấp nhận mức chênh +6 điểm (power 0,64 ở +5 điểm) trước khi chia nhóm — Giám đốc vận hành LogiX-VN — kiểm tra 2026-12-14.
- Bật đủ event có `trace_id`; thay phút xem lại/làm lại [sim] bằng phút đo thật sau tuần 1 — PM trợ lý hoàn phí — kiểm tra 2026-12-22.
- Có kế hoạch giảm xem lại theo bậc, không xem lại 100% kéo dài (B4) — Trưởng nhóm CSKH — kiểm tra 2026-12-22.
