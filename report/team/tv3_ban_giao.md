# Bàn giao của Thành viên 3: A3, B3, D1(e), D2, chỉ số an toàn

Mọi số do `src/tv3_tinh_so.py` in ra (chạy trong `src/`: `python tv3_tinh_so.py`), dùng `mo_hinh` của `src/lab13.py`. Số tính từ cột `_simulated` có nhãn **simulated**.

| Phần | Gửi cho | File đích |
| --- | --- | --- |
| A3, B3 | Thành viên 2 (người giữ) | `report/team/bang_chi_phi.md` |
| D1(e), D2 | Thành viên 4 (người giữ) | `report/team/pilot_plan.yaml` (chú thích đầu file) |
| Chỉ số an toàn | Thành viên 4 (người giữ) | `report/team/chi_so.md` |

## CP1 · A3: Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Lần chạy / yêu cầu | Chi phí mỗi việc thành công [simulated] | So với 12.000 đ [simulated] |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ | 0,22× |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ | 0,69× |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ | 1,88× |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ | 0,85× |

Tỉ lệ lần chạy `ok` theo từng lần thử (đo từ trace):

| Loại | Lần 1 | Lần 2 | Lần 3 |
| --- | ---: | ---: | ---: |
| noi_dia | 91,0% | 75,7% | 38,9% |
| hang_nang | 70,9% | 39,1% | 17,9% |
| quoc_te | 30,0% | 11,4% | 2,2% |
| doi_tac | 51,5% | 18,2% | 14,8% |

- **Loại không đáng giao:** quoc_te tốn 22.515 đ mỗi việc thành công, bằng 1,88× nhân viên tự làm [simulated], và chỉ 27,3% thành công. doi_tac (0,85× [simulated]) sát ngưỡng, lại có điều khoản riêng, nên cũng để ngoài phạm vi pilot.
- **Vì sao chạy lại không giúp:** với quoc_te, lần 1 đúng 30,0%, lần 2 còn 11,4%, lần 3 chỉ 2,2%. Lỗi lặp lại trên cùng một yêu cầu, nên chạy lại chủ yếu tốn thêm token và tool.
- **Phạm vi đề xuất:** noi_dia + hang_nang (982/1.200 yêu cầu).

## CP2 · B3: Giới hạn chạy lại và chi phí cả hệ thống

Chi phí cả hệ thống = tổng chi phí trợ lý + 12.000 đ × số yêu cầu không thành công (nhân viên làm thay).

| Giới hạn | Tổng trợ lý [simulated] | Không thành công | Nhân viên làm thay | Cả hệ thống [simulated] | Chi phí mỗi việc thành công [simulated] |
| --- | ---: | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ | 319 | 3.828.000 đ | 7.449.781 đ | 4.111 đ (thấp nhất) |
| 2 lần | 4.093.220 đ | 234 | 2.808.000 đ | **6.901.220 đ (rẻ nhất)** | 4.237 đ |
| 3 lần | 4.373.585 đ | 222 | 2.664.000 đ | 7.037.585 đ | 4.472 đ |

**Trả lời B3:**
- Với công ty, giới hạn 2 lần rẻ nhất: 6.901.220 đ [simulated], ít hơn giới hạn 3 lần 136.365 đ.
- Chi phí mỗi việc thành công thấp nhất lại rơi vào giới hạn 1 lần (4.111 đ [simulated]), nhưng mức đó đẩy thêm 85 việc sang nhân viên.
- Vì vậy không nên tối ưu riêng chi phí mỗi việc thành công.

## CP4 · D1(e) và D2

**D1(e), mức chênh 6 điểm (0,70 → 0,76), 20 nhân viên mỗi nhóm:**
- Cần **859** yêu cầu mỗi nhóm theo công thức tay; statsmodels `NormalIndPower` với Cohen h cho 858.
- Muốn đạt mức đó, mỗi nhân viên cần m ≥ **299** yêu cầu, DE = 6,96, n hiệu dụng = 859, dưới trần c/ICC = 1.000.
- Giải tay: 20m ≥ 859 × (0,98 + 0,02m) → 2,82m ≥ 841,82 → m ≥ 298,5 → 299.
- **Con số bất lợi:** nếu tác động thật chỉ 5 điểm thì với 859 yêu cầu mỗi nhóm, power chỉ còn khoảng **0,64**.

**D2, năm câu kiểm tra "tách được tác động"** (với cách chia theo nhân viên, 20 + 20):
1. Đối chứng chạy cùng thời gian: có. 20 nhân viên đối chứng làm cùng tuần, cùng depot với 20 nhân viên dùng trợ lý.
2. Ngẫu nhiên: bốc thăm bằng code với seed ghi trước, phân tầng theo 6 depot, không để trưởng nhóm tự chọn.
3. Ảnh hưởng gián tiếp: có rủi ro nhân viên trong cùng depot chia sẻ câu trả lời. Giảm bằng cách cấp quyền theo tài khoản và log lượt mở trợ lý theo `staff_id`.
4. Viết trước: chỉ số chính, MDE 6 điểm, 3 luật dừng và ngày quyết định đều chốt trước ngày bắt đầu.
5. Ít nhất 20 cụm mỗi nhóm: có, đúng 20 nhân viên mỗi nhóm.

## CP5 · Chỉ số an toàn

**Chỉ số an toàn chính: tỉ lệ mở lại trong 7 ngày (đo từ dữ liệu chạy thử)**

| Nhóm | Tỉ lệ hiện tại |
| --- | ---: |
| Toàn mẫu | 4,25% (51/1.200) |
| Phạm vi noi_dia + hang_nang | 3,97% (39/982) |
| noi_dia | 3,16% (26/824) |
| hang_nang | 8,23% (13/158) |
| quoc_te | 6,00% (9/150) |
| doi_tac | 4,41% (3/68) |

- **Gợi ý ngưỡng:** nếu đặt ngưỡng tuyệt đối 3%, pilot sẽ dừng ngay tuần đầu (hiện tại trong phạm vi đã là 3,97%). Nên so với nhóm đối chứng (chênh từ 2 điểm) kèm trần tuyệt đối 6%.
- **Cần theo dõi riêng hang_nang:** loại này có tỉ lệ mở lại 8,23%, đã vượt trần 6% ngay từ dữ liệu chạy thử.

**Chỉ số an toàn đề xuất thêm: mở lại 7 ngày ở ca không được xem lại**
- Hiện tại: 4,99% (51/1.023) ở ca không được xem lại, so với 0,00% (0/129) ở ca đã xem lại và nhân viên giữ nguyên. Cả 51 ca mở lại đều có `ket_qua = lam_lai`.
- Lý do cần chỉ số này: giảm tỉ lệ xem lại là đòn bẩy chi phí lớn thứ hai ở B1. Chỉ số này cho biết giảm xem lại có làm lỗi lọt đến khách tăng không.
- Cách đo: nối event `review_completed` với `case_reopened` qua `trace_id`.
