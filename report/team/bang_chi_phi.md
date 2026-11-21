# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 (ĐẠT) |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 (ĐẠT) |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 (ĐẠT) |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 | `logix_runs.csv` (5.600 lần gọi) | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated` (890 phút) | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated` (1.132 phút) | simulated |
| Tổng chi phí | 4.373.585 | Tổng 4 khoản trên | có phần simulated |
| Số việc thành công | 978 | `ket_qua == 'thanh_cong'` | đo từ trace |
| Chi phí mỗi việc thành công | 4.472 | 4.373.585 ÷ 978 | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | 329.585 ÷ 1.200 | đo từ trace |

- Chi phí mỗi việc thành công gấp bao nhiêu lần "hoá đơn chia số yêu cầu"? Chi phí mỗi việc thành công (4.472 đ [simulated]) gấp **16,3 lần** hoá đơn token + tool chia số yêu cầu (274,7 đ). Khi so công bằng với 12.000 đ nhân viên tự làm (cộng thêm 222 ca không thành công × 12.000 đ), chi phí cả hệ thống là **5.865 đ/yêu cầu = 0,49×** [simulated].
- Khoản nào chiếm tỉ trọng lớn nhất trong tổng chi phí, bao nhiêu phần trăm? Khoản lớn nhất là **làm lại, chiếm 51,8%** (2.264.000 đ [simulated]), tiếp theo là xem lại 40,7% (1.780.000 đ [simulated]). Tổng thời gian nhân viên chiếm **92,5%** tổng chi phí, còn token + tool chỉ chiếm 7,5%.

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công [simulated] | So với 12.000 đ [simulated] |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ | 0,22× |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ | 0,69× |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ | 1,88× |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ | 0,85× |

- Loại nào không đáng để trợ lý xử lý? Với loại đó, cho chạy lại tới 3 lần có giúp không? **`quoc_te`** không đáng để trợ lý xử lý vì chi phí lên tới **22.515 đ = 1,88×** nhân viên tự làm [simulated] và tỉ lệ thành công chỉ 27,3%. Cho chạy lại tới 3 lần không giúp: tỉ lệ `ok` của `quoc_te` giảm mạnh từ 30,0% (lần 1) xuống 11,4% (lần 2) và 2,2% (lần 3), chạy lại chỉ tốn thêm tiền; `doi_tac` cũng sát ngưỡng (0,85× [simulated]) và có điều khoản riêng nên loại khỏi pilot.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

*(Chi phí biến đổi trong phạm vi `noi_dia` + `hang_nang`: 3.072.513 đ cho 900 việc thành công = 3.414 đ/việc [simulated]; chi phí cố định 40.000.000 đ/tháng.)*

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định [simulated] | So với 12.000 đ [simulated] |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ | 0,38× |
| Một nửa khối lượng (22.500/tháng) | 16.875 | 2.370 đ | 5.784 đ | 0,48× |

- Chi phí cố định có đổi kết luận không? Ở khối lượng nào? Chi phí cố định 40 triệu đ/tháng **không đổi kết luận** ở quy mô đầy đủ 45.000 yêu cầu/tháng (4.599 đ = **0,38×** [simulated]) lẫn khi giảm một nửa (5.784 đ = **0,48×** [simulated]). Tuy nhiên định phí mỗi việc tăng gấp đôi khi khối lượng giảm một nửa (1.185 đ → 2.370 đ/việc), nên nếu khối lượng pilot quá nhỏ (dưới ~4.660 việc thành công/tháng) sẽ vượt ngưỡng 12.000 đ.

## B1 · Đổi từng yếu tố

*(Mức gốc A2: 4.472 đ/việc thành công [simulated].)*

| Kịch bản | Cách tính | Chi phí mỗi việc thành công [simulated] | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 đ | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 đ | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 đ | −8,1% |

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: **6.543 đ (+46,3%)** [simulated], đúng bằng tổng hai tác động riêng (+5,6% + 40,7% = +46,3%) vì mô hình chi phí là hàm cộng tuyến tính theo các khoản chi phí.
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: **1. Số ca làm lại** (+51,8% / −25,9%) · **2. Tỉ lệ xem lại** (+40,7% / −20,3%) · **3. Lương nhân viên** (+23,1% khi tăng 25%).

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý [simulated] | Số yêu cầu không thành công | Chi phí cả hệ thống [simulated] | Chi phí mỗi việc thành công [simulated] |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ | 319 | 7.449.781 đ | 4.111 đ |
| 2 lần | 4.093.220 đ | 234 | **6.901.220 đ** | 4.237 đ |
| 3 lần | 4.373.585 đ | 222 | 7.037.585 đ | 4.472 đ |

- Giới hạn nào rẻ nhất cho công ty? Có trùng với giới hạn cho chi phí mỗi việc thành công thấp nhất không? **Giới hạn 2 lần** rẻ nhất cho công ty với chi phí cả hệ thống **6.901.220 đ** [simulated], **không trùng** với giới hạn có chi phí mỗi việc thành công thấp nhất là 1 lần (4.111 đ [simulated]). Tối ưu riêng chi phí mỗi việc thành công ở mức 1 lần sẽ đẩy thêm 85 yêu cầu (319 so với 234) sang nhân viên tự làm, làm tổng chi phí cả hệ thống tăng thêm 548.561 đ.

## B4 · Nếu phải xem lại tất cả

- Chi phí mỗi việc thành công khi xem lại 100% (`noi_dia` + `hang_nang`), so với 12.000 đ: Với 948 yêu cầu xem lại 5 phút (9.480.000 đ), 48 ca làm lại 9 phút (864.000 đ) và 224.513 đ token + tool cho 900 việc thành công, chi phí là **11.743 đ = 0,98×** của 12.000 đ [simulated] (hoà vốn khi xem lại ≤ 5,1 phút). Nếu dùng trung bình thực tế từ dữ liệu là 15,3 phút/ca làm lại (trung vị 14,5 phút), chi phí lên tới **12.414 đ = 1,03×** [simulated] (hoà vốn ≤ 4,8 phút), đắt hơn nhân viên tự làm.
- Kết quả này nói gì về thứ pilot cần học được? Xem lại 100% khiến tiền xem lại chiếm tới ~90% tổng chi phí nên trợ lý gần như không tiết kiệm (hoặc lỗ nhẹ). Pilot bắt buộc phải đo được **tỉ lệ xem lại có thể giảm an toàn xuống mức nào** và **thời gian xem lại thực tế có rút ngắn dưới 5 phút** được không.
