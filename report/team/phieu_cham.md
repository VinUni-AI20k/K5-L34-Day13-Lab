# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): PD (L3A)
- Nhóm được chấm: DLB (L3A) · [hồ sơ](https://github.com/NguyenQuangDao/K5-L3A-DAY13-DLB-LaunchEconomics/blob/main/report/team/ho_so_launch_v0.md)
- Đã soát kèm: `pilot_plan.yaml` (đọc được bằng `yaml.safe_load`, ngoài chú thích không còn `?`), `bang_loi.md`, `chi_so.md`, `bang_chi_phi.md`. Hội đồng tự tính lại từ hai CSV và khớp các số chính: 4.472 đ, 16,3×, 5.865 đ = 0,49×, 82,83% / 27,12% / 4,25%, 3,97% và 3,46% (34/982) trong phạm vi.

| Tiêu chí                 | 0 điểm                            | 5 điểm                               | 10 điểm                                                                        |        Điểm | Lý do (có số)                                                                                                                                                                                                                                                                                                                                    |
| ------------------------ | --------------------------------- | ------------------------------------ | ------------------------------------------------------------------------------ | ----------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Đề xuất khớp bằng chứng  | Mâu thuẫn với số của chính nhóm   | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý                                      |          10 | Go có điều kiện khớp số; nêu đủ ba con số bất lợi ngay ở đề xuất: power 0,64 nếu tác động thật 5 điểm, xem lại 100% tốn 0,98×–1,03× [simulated], mở lại hiện tại 4,25%. Mỗi điều kiện có vai và ngày kiểm tra (khoá chống trùng 2027-01-05; giảm xem lại theo bậc khi sửa + bỏ < 15%, hoà vốn ≤ 5,1 / 4,8 phút)                                  |
| Số giả lập và phạm vi    | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi      | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số                        |          10 | Mọi số từ cột `_simulated` có nhãn; mục 1, 2, 3, 7 ghi trạng thái Giả lập. Thu hẹp về noi_dia (0,22×) + hang_nang (0,69×), loại quoc_te (1,88×, ok theo lần chạy 30,0% → 11,4% → 2,2%) và doi_tac (0,85×, điều khoản riêng)                                                                                                                      |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung     | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng |          10 | Chia theo nhân viên 20 + 20, ngẫu nhiên có seed, phân tầng theo depot, đối chứng đồng thời; MDE 6 điểm (859/nhóm, m ≥ 299, DE 6,96) là đánh đổi đã ghi rõ. 5 luật dừng có ngưỡng, thời hạn và Giám đốc vận hành có quyền tắt; ngày đọc kết quả 2027-02-11 chờ đủ cửa sổ mở lại 7 ngày. Hai điểm yếu chưa đủ để hạ bậc (ghi ở điều kiện bên dưới) |
| **Tổng**                 |                                   |                                      |                                                                                | **30 / 30** |                                                                                                                                                                                                                                                                                                                                                  |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Số liệu khớp dữ liệu, con số bất lợi được nêu và có cách xử lý, pilot tách được tác động với đánh đổi MDE 6 điểm đã ký trước. Hội đồng thêm hai điều kiện:

- Xác nhận đủ 40 nhân viên đủ điều kiện để chia 20 + 20: dữ liệu chạy thử chỉ có 20 `staff_id` ở 6 depot; nếu chỉ 20 người (10 + 10 cụm) thì cỡ mẫu hiệu dụng tối đa < 10 / 0,02 = 500 < 859, mức chênh 6 điểm không còn đạt · Giám đốc vận hành · trước 2027-01-05.
- Luật an toàn "cao hơn đối chứng ≥ 2 điểm" đang áp dụng cả ở bước 0.10 (4 nhân viên mỗi nhóm): với 4 cụm, lệch 2 điểm dễ là nhiễu và dễ dừng nhầm. Ở bước 0.10 chỉ nên dùng luật tuyệt đối (trần 6%, hoàn trùng, báo "đã hoàn" mà sổ cái không ghi), luật so với đối chứng áp dụng từ bước 0.25 · PM trợ lý hoàn phí · sửa `pilot_plan.yaml` trước 2027-01-05.

Ghi chú nhỏ, không trừ điểm: trang hồ sơ dài khoảng 1.000 chữ, vượt yêu cầu "một trang"; mục 6 nên rút gọn và để chi tiết trong `pilot_plan.yaml`.

**Một câu hỏi cho đội trình:** Dữ liệu chạy thử chỉ có 20 nhân viên ở 6 depot. Nếu thực tế chỉ có 20 người đủ điều kiện thì nhóm chia thế nào, mức chênh phát hiện được là bao nhiêu điểm, và có còn đề xuất Go có điều kiện không?

**Câu trả lời của đội trình (ghi lại tại buổi):** Nếu chỉ có 20 người, nhóm tôi sẽ bốc thăm chia 10 người dùng trợ lý, 10 người làm đối chứng. Nếu đủ người ở từng depot, nhóm tôi sẽ bốc thăm trong từng depot để hai bên cân bằng hơn.

Mỗi bên có trần 500 yêu cầu hiệu dụng, trong khi để phát hiện chênh lệch 6 điểm phần trăm cần 859. Trong các mức tính theo điểm tròn, 8 điểm phần trăm là mức nhỏ nhất đạt power 80%, với ít nhất 796 yêu cầu mỗi người. Ngay cả với cỡ mẫu đó, nếu tác động thật chỉ là 5 điểm phần trăm thì power chỉ khoảng 41%.

Vì vậy, nếu chỉ có 20 người, nhóm tôi chọn No-go cho pilot đo tác động. Giám đốc vận hành sẽ xác nhận số người đủ điều kiện trước 05/01/2027. Khi đủ 40 người, nhóm tôi sẽ quay lại Gate 2a. Trong lúc chờ, nếu được duyệt riêng, nhóm tôi có thể chạy thử để đo thời gian xem lại, chi phí và an toàn, phục vụ việc chuẩn bị pilot sau.
