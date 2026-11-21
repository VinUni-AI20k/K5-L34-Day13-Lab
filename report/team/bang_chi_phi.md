# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 | `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated` | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | 4.373.585 | | có phần simulated |
| Số việc thành công | 978 | `ket_qua` | |
| Chi phí mỗi việc thành công | 4.472 | | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | | đo từ trace |

- Chi phí mỗi việc thành công gấp bao nhiêu lần "hoá đơn chia số yêu cầu"? Gấp 16,3 lần (4.472 ÷ 274,7) [simulated].
- Khoản nào chiếm tỉ trọng lớn nhất? Làm lại, 51,8% tổng chi phí [simulated]; tiếp theo là xem lại 40,7%. Giờ nhân viên chiếm 92,5%.
- So với nhân viên tự làm: 4.472 đ chưa tính 222 yêu cầu chuyển nhân viên. Chi phí cả hệ thống = (4.373.585 + 222 × 12.000) ÷ 1.200 = 5.865 đ mỗi yêu cầu = 0,49× của 12.000 đ [simulated].

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ | 0,22× |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ | 0,69× |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ | 1,88× |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ | 0,85× |

(Chi phí cột 5 và 6 là simulated.)

- Loại nào không đáng để trợ lý xử lý? `quoc_te`: 22.515 đ = 1,88× của 12.000 đ, thành công chỉ 27,3%. Chạy lại tới 3 lần không giúp: tỉ lệ ok theo lần thử là 30,0% → 11,4% → 2,2%, lỗi lặp lại trên cùng yêu cầu nên chỉ tốn thêm tiền. `doi_tac` (0,85×, 54,4%) sát ngưỡng và cũng loại khỏi phạm vi pilot.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ | 0,38× |
| Một nửa khối lượng | 16.875 | 2.370 đ | 5.784 đ | 0,48× |

(Chi phí mỗi việc thành công trong phạm vi chưa cố định: 3.414 đ, simulated.)

- Chi phí cố định có đổi kết luận không? Không ở cả hai khối lượng (0,38× và 0,48× đều dưới 1×), nhưng cố định mỗi việc tăng gấp đôi (1.185 → 2.370 đ) khi khối lượng giảm một nửa. Hồ sơ phải nói rõ con số đã cộng cố định hay chưa và ở khối lượng nào.

## B1 · Đổi từng yếu tố

| Kịch bản | Cách tính | Chi phí mỗi việc thành công (simulated) | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 | +5,6 |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 | −2,8 |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 | +40,7 |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 | −20,3 |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 | +51,8 |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 | −25,9 |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 | +23,1 |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 | −5,2 |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 | −8,1 |

Gốc: 4.472 đ. Kiểm tra: mỗi kịch bản "giảm một nửa" giảm đúng bằng nửa mức tăng của "gấp đôi" (5,6 → 2,8; 40,7 → 20,3; 51,8 → 25,9).

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: 6.543 đ (+46,3%) [simulated], đúng bằng tổng hai tác động riêng (5,6 + 40,7) vì mô hình cộng tuyến tính.
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. số ca làm lại (±51,8%) · 2. tỉ lệ xem lại (±40,7%) · 3. lương nhân viên (+23,1%).

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 | 319 | 7.449.781 | 4.111 |
| 2 lần | 4.093.220 | 234 | 6.901.220 | 4.237 |
| 3 lần | 4.373.585 | 222 | 7.037.585 | 4.472 |

(Chi phí cả hệ thống = tổng trợ lý + 12.000 đ × số yêu cầu không thành công; mọi số là simulated.)

- Giới hạn rẻ nhất cho công ty là 2 lần (6.901.220 đ). Không trùng với giới hạn cho chi phí mỗi việc thành công thấp nhất (1 lần, 4.111 đ): tối ưu riêng chỉ số đó đẩy thêm 85 việc (319 − 234) sang nhân viên.

## B4 · Nếu phải xem lại tất cả

- Xem lại 100% (`noi_dia` + `hang_nang`: 948 yêu cầu có lần chạy ok × 5 phút, 48 ca làm lại × 9 phút): tổng 10.568.513 đ ÷ 900 việc thành công = 11.743 đ = 0,98× của 12.000 đ [simulated]. Nếu dùng phút làm lại trung bình của dữ liệu trong phạm vi này (16,2 phút/ca thay vì 9): 12.516 đ = 1,04× [simulated]. Hoà vốn khi mỗi lần xem lại ≤ 5,1 phút (9 phút làm lại) hoặc ≤ 4,8 phút (16,2 phút làm lại).
- Pilot cần học được tỉ lệ xem lại có thể giảm an toàn xuống mức nào và mỗi lần xem lại có ngắn hơn 5 phút được không, vì tiền xem lại chiếm khoảng 90% chi phí khi xem 100%.
