# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): Stech (L3A)
- Nhóm được chấm: Teamday14 (L3A) · repo `VUDUCTHANG130604/K5-L3A-DAY13-Teamday14-LaunchEconomics`, commit `ccfa5d9`

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | No-go khớp với số của nhóm và nêu đủ con số bất lợi: xem lại 100% lên 12.415 đ = 1,03× [simulated], power chỉ 0,64 nếu tác động thật +5 điểm, ca 20 hoàn trùng, ca 7 báo xong khi sổ cái lỗi. Mỗi con số có điều kiện xử lý để trình lại. |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 10 | Mọi số tính từ cột `_simulated` có nhãn (4.472 đ, 5.865 đ/yêu cầu, B1–B4). Phạm vi thu hẹp về `noi_dia` + `hang_nang` vì `quoc_te` 22.515 đ = 1,88× và `doi_tac` chỉ 54,4% thành công. |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 | Đối chứng đồng thời 20 + 20 nhân viên, chia ngẫu nhiên theo tầng depot; 20 cụm × 299 yêu cầu, DE 6,96, n hiệu dụng 859 đủ phát hiện chênh 6 điểm. 4 luật dừng NẾU – TRONG – THÌ – KHÔNG THÌ có ngưỡng (hoàn trùng ≥ 1 đơn, mở lại > 6% hoặc +2 điểm trong 3 ngày, chi phí > 12.000 đ trong 2 tuần), thời hạn 30 phút và người dừng là Giám đốc vận hành. |
| **Tổng** | | | | **30 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Chi phí trong phạm vi chỉ 4.599 đ = 0,38× [simulated] (đã cộng cố định), kế hoạch pilot đủ 20 cụm mỗi nhánh và chấp nhận rõ mức chênh 6 điểm. Các lý do No-go của nhóm (khoá chống trùng ca 20, đối soát ca 7, log chi phí) đều làm được trước ngày mở quyền, nên đặt thành điều kiện bắt buộc trước 30/11/2026 thay vì dừng cả vòng. Điểm cần nhóm bổ sung: CP3 chưa có bằng chứng hai bộ nhãn độc lập (nhóm tự ghi trạng thái "Chưa"), nên tỉ lệ đồng thuận 85% chưa đủ tin cậy.

**Một câu hỏi cho đội trình:** Chi phí phạm vi chỉ 0,38× và pilot đã đủ 20 cụm mỗi nhánh; vì sao nhóm chọn No-go thay vì Go có điều kiện, với ca 20 và ca 7 là điều kiện phải xong trước ngày mở quyền?

**Câu trả lời của đội trình (ghi lại tại buổi):** ...
