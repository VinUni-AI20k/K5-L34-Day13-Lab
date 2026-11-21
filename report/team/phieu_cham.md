# Phiếu chấm hội đồng Gate 2a

Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): NguyenTuanBach
- Hồ sơ được chấm: `report/team/ho_so_launch_v0.md` (Go có điều kiện), đối chiếu với `bang_chi_phi.md` và `pilot_plan.yaml`

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | Go có điều kiện khớp số: chi phí cả hệ thống 0,49× của 12.000 đ [simulated]; nêu cả số bất lợi (xem lại 100% làm chi phí lên 11.743 đ, power chỉ 0,64 nếu tác động thật 5 điểm) kèm điều kiện xử lý |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 10 | Mọi số từ cột `_simulated` có nhãn; phạm vi thu hẹp về noi_dia (0,22×) và hang_nang (0,69×), loại quoc_te (1,88×, thành công 27,3%) |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 5 | Có đối chứng và ba luật dừng có ngưỡng, nhưng 20 + 20 nhân viên chỉ đủ cho mức chênh 6 điểm (cần 42 người/nhóm cho 70% baseline), chưa đủ cho 5 điểm |
| **Tổng** | | | | **25 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện, chỉ duyệt kế hoạch pilot.

**Lý do:** số bất lợi được nêu rõ và có điều kiện xử lý; điểm trừ ở cỡ mẫu pilot (power 0,64 nếu tác động thật 5 điểm).

**Một câu hỏi cho đội trình:** nếu mức chênh thật chỉ 5 điểm, pilot 20 + 20 nhân viên có kết luận được không, và nhóm sẽ làm gì với kết quả không đủ power?

**Câu trả lời của đội trình (ghi lại tại buổi):** Không kết luận được ở mức 5 điểm (power 0,64). Nhóm chấp nhận mức chênh 6 điểm đã ghi trong hồ sơ, và nếu kết quả không đạt ngưỡng thì mở rộng thêm nhân viên hoặc depot trước khi quyết định rollout.
