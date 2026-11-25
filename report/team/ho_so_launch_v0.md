# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: 25112026 · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ/việc thành công, gấp 16,3× hoá đơn token + tool chia số yêu cầu (274,7 đ) [simulated]. Khoản lớn nhất: làm lại 51,8%, xem lại 40,7% [simulated]. Số này chưa cộng chi phí cố định; cộng 40 triệu đ/tháng trong phạm vi noi_dia + hang_nang: 4.599 đ ở 45.000 yêu cầu/tháng, 5.784 đ nếu khối lượng còn một nửa [simulated] | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | 1. Số ca làm lại (±51,8%) · 2. Tỉ lệ xem lại (±40,7%) · 3. Lương nhân viên (+23,1% khi tăng 25%) [simulated]. Giá token chỉ +5,6% khi gấp đôi | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Chi phí cả hệ thống, đã cộng 222 ca không thành công × 12.000 đ: 5.865 đ/yêu cầu = 0,49× của 12.000 đ [simulated]. Theo loại: noi_dia 0,22×, hang_nang 0,69×, doi_tac 0,85×, quoc_te 1,88× [simulated]. Phạm vi pilot thu hẹp về noi_dia + hang_nang (4.599 đ = 0,38× đã cộng cố định [simulated]); loại quoc_te (thành công 27,3%, chạy lại không giúp: ok 30,0% → 11,4% → 2,2%) và doi_tac (sát ngưỡng, điều khoản riêng). Bất lợi: xem lại 100% thì 11.743 đ = 0,98× (12.415 đ = 1,03× nếu làm lại 15,3 phút/ca) [simulated] | Giả lập | Giám đốc vận hành |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chỉ số trong đợt chạy thử là: chính 82,83% (994/1.200) · bỏ qua gợi ý 27,12% (48/177) · lỗi lọt đến khách 4,25% (51/1.200). Không kết luận "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng. Mỗi chỉ số có event có `trace_id` để tính (`chi_so.md`) | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | Hai bộ nhãn độc lập, đồng thuận 20/20 = 100%. Phân bố: Do người dùng 4 · Hệ thống 5 · Ngữ cảnh 4 · Giới hạn hệ thống 4 · Ngầm 3. 5 cách khắc phục (ca 9, 7, 18, 4, 17), mỗi cách có event, ngưỡng, tần suất và một vai trò phụ trách (`bang_loi.md`) | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | Chia ngẫu nhiên theo nhân viên, 20 cụm mỗi nhóm, n = 859 mỗi nhóm (DE 6,96, ≥ 299 yêu cầu mỗi nhân viên), mde 0,06. Chia theo yêu cầu cần 1.251 nhưng tràn tác động; theo depot tối đa 300. Bất lợi: nếu tác động thật chỉ 5 điểm thì power còn khoảng 0,64. 3 luật dừng (an toàn, chi phí, mức dùng); ngưỡng an toàn so với đối chứng (+2 điểm) kèm trần 6%, vì tỉ lệ mở lại hiện tại đã 4,25%. Ngày quyết định 2027-01-05 | Xong, có bằng chứng | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | 3 dòng trong `chi_so.md`: làm lại gấp đôi lên 6.787 đ (+51,8%); xem lại gấp đôi lên 6.292 đ (+40,7%), xem lại 100% lên 11.743 đ = 0,98×; khối lượng còn một nửa thì cố định 2.370 đ/việc [simulated] | Giả lập | PM trợ lý hoàn phí |

**Đề xuất: Go có điều kiện** cho pilot chỉ gồm `noi_dia` + `hang_nang` (4.599 đ = 0,38× của 12.000 đ, đã cộng chi phí cố định [simulated]); `quoc_te` và `doi_tac` vẫn do nhân viên xử lý.

Ba con số bất lợi nhóm không bỏ qua: xem lại 100% thì 11.743 đ = 0,98× (12.415 đ = 1,03× nếu làm lại 15,3 phút/ca) [simulated], tức gần như không tiết kiệm; chia theo nhân viên chỉ thấy được mức chênh 6 điểm, nếu tác động thật là 5 điểm thì power còn khoảng 0,64; tỉ lệ mở lại hiện tại đã 4,25%, nên luật an toàn so với đối chứng thay vì đặt ngưỡng tuyệt đối thấp. Các điều kiện dưới đây xử lý từng điểm.

| Điều kiện | Người phụ trách | Ngày kiểm tra |
| --- | --- | --- |
| Khoá chống trùng (`idempotency_key`) khi ghi sổ cái và đối soát mỗi giờ "đã báo hoàn" với bản ghi sổ cái `ok` cùng `trace_id`; ngưỡng 0 ca lệch trong 3 ngày chạy thử nội bộ | Kỹ sư trưởng agent | 2026-12-04 |
| Ký chấp nhận mde 0,06 và power khoảng 0,64 nếu tác động thật chỉ 5 điểm, trước khi bốc thăm 20 + 20 nhân viên | Giám đốc vận hành | 2026-12-04 |
| Chỉ mở cho `noi_dia` + `hang_nang`; yêu cầu `quoc_te`, `doi_tac` tự chuyển nhân viên kèm tóm tắt (event `handoff_to_staff`) | PM trợ lý hoàn phí | 2026-12-08 |
| Bật đủ 11 event có `trace_id` trong `chi_so.md`; sau tuần 1 thay phút `_simulated` bằng phút đo thật từ `staff_review_decision`, `staff_rework_completed` và tính lại chi phí mỗi việc thành công | Kỹ sư trưởng agent | 2026-12-15 |
| Giảm xem lại theo bậc: 100% ở bước 0,10; chỉ giảm khi tỉ lệ sửa + bỏ dưới 15% (đợt chạy thử 27,12%) và phút xem lại đo thật dưới 5,1 phút; không đạt ở cuối bước 0,25 thì không sang bước 0,50 | Trưởng nhóm CSKH | 2026-12-22 |
