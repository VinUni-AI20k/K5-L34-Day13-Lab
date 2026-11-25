# Bảng chi phí · Nhiệm vụ A và B

Số B tính bằng `src/lab13.py` ở nhánh `origin/p1-b1-b4` (commit `9374bca`). Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- || Số lầ| Số lần chạy trung bình, tối đa 2 lần | ... |
| Số lần chạy trung bình, chạy đến khi đúng | ... |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | ... |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | ... | `logix_runs.csv` | đo từ trace |
| Tool | ... | `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | ... | attempt lớn hơn 1 | đo từ trace |
| Xem lại | ... | `phut_xem_lai_simulated` | simulated |
| Làm lại | ... | `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | ... | | |
| Số việc thành công | ... | `ket_qua` | |
| Chi phí mỗi việc thành công | ... | | |
| Hoá đơn token và tool chia cho số yêu cầu | ... | | |

- Chi phí mỗi việc thành công gấp bao nhiêu lần "hoá đơn chia số yêu cầu"? ...
- Khoản nào chiếm tỉ trọng lớn nhất trong tổng chi phí, bao nhiêu phần trăm? ...

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | ... | ... | ... | ... | ... |
| hang_nang | ... | ... | ... | ... | ... |
| quoc_te | ... | ... | ... | ... | ... |
| doi_tac | ... | ... | ... | ... | ... |

- Loại nào không đáng để trợ lý xử lý? Với loại đó, cho chạy lại tới 3 lần có giúp không? ...

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | ... | ... | ... | ... |
| Một nửa khối lượng | ... | ... | ... | ... |

- Chi phí cố định có đổi kết luận không? Ở khối lượng nào? ...

## B1 · Đổi từng yếu tố

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 đ simulated | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ simulated | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ simulated | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ simulated | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ simulated | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ simulated | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ simulated | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 đ simulated | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 đ simulated | −8,1% |

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: 6.543 đ simulated, tăng 46,3% so với 4.472 đ simulated.
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. số ca làm lại · 2. tỉ lệ xem lại · 3. lương nhân viên.

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ simulated | 319 | 7.449.781 đ simulated | 4.111 đ simulated |
| 2 lần | 4.093.220 đ simulated | 234 | 6.901.220 đ simulated | 4.237 đ simulated |
| 3 lần | 4.373.585 đ simulated | 222 | 7.037.585 đ simulated | 4.472 đ simulated |

- Hai lần rẻ nhất cho công ty (6.901.220 đ simulated); một lần cho chi phí mỗi việc thành công thấp nhất (4.111 đ simulated), nhưng thêm 85 yêu cầu không thành công.

## B4 · Nếu phải xem lại tất cả

- Xem lại 100% (`noi_dia` + `hang_nang`): 11.743 đ/việc simulated, bằng 0,98 lần 12.000 đ, giả định 5 phút xem lại và 9 phút làm lại. Nếu làm lại 15,3 phút: 12.415 đ simulated, bằng 1,03 lần.
- Pilot cần đo thời gian thực và xác định có thể giảm tỉ lệ xem lại an toàn đến mức nào; ở giả định 9 phút làm lại, xem lại phải không quá khoảng 5,1 phút để hòa vốn.
