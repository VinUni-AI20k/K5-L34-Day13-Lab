# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | ... |
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

Giá trị gốc (A2): **4.472 đ** (`simulated`). Các số trong bảng B1–B4 tính bằng `src/cp2_do_nhay.py` (nhận `mo_hinh` làm tham số, tự kiểm tra kịch bản "giảm một nửa" = đúng 1/2 mức tăng "gấp đôi": ĐẠT).

| Kịch bản | Cách tính | Chi phí mỗi việc thành công (`simulated`) | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 đ (`simulated`) | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ (`simulated`) | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ (`simulated`) | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ (`simulated`) | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ (`simulated`) | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ (`simulated`) | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ (`simulated`) | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 đ (`simulated`) | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 đ (`simulated`) | −8,1% |

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: **6.543 đ (`simulated`, +46,3%)**, đúng bằng tổng hai tác động riêng (+5,6% và +40,7%) vì mô hình cộng tuyến tính.
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: **1. Số ca làm lại (+51,8%) · 2. Tỉ lệ xem lại (+40,7%) · 3. Lương nhân viên (+23,1%)** (`simulated`).

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

Chi phí cả hệ thống = tổng chi phí trợ lý + 12.000 đ × số yêu cầu không thành công (nhân viên làm thay).

| Giới hạn | Tổng chi phí trợ lý (`simulated`) | Số yêu cầu không thành công | Chi phí cả hệ thống (`simulated`) | Chi phí mỗi việc thành công (`simulated`) |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ | 319 | 7.449.781 đ | 4.111 đ (thấp nhất) |
| 2 lần | 4.093.220 đ | 234 | **6.901.220 đ (rẻ nhất)** | 4.237 đ |
| 3 lần | 4.373.585 đ | 222 | 7.037.585 đ | 4.472 đ |

- Giới hạn nào rẻ nhất cho công ty? Có trùng với giới hạn cho chi phí mỗi việc thành công thấp nhất không? **Tối đa 2 lần** rẻ nhất cho công ty (**6.901.220 đ**, `simulated`), không trùng với mức có chi phí mỗi việc thành công thấp nhất (**1 lần**, **4.111 đ**, `simulated`) vì giới hạn 1 lần đẩy thêm **85 ca** (319 vs 234) sang nhân viên làm tay.

## B4 · Nếu phải xem lại tất cả

- Chi phí mỗi việc thành công khi xem lại 100% (`noi_dia` + `hang_nang`, 948 ca có `ok` × 5 phút, 48 ca làm lại, 900 việc thành công, 224.513 đ token+tool), so với 12.000 đ: với giả định 9 phút/ca làm lại là **11.743 đ = 0,98×** (`simulated`, hoà vốn ≤ **5,1 phút**/lần xem lại); nếu dùng trung bình thực tế `15,3 phút`/ca từ `phut_lam_lai_simulated` (trung vị 14,5 phút) là **12.415 đ = 1,03×** (`simulated`, đắt hơn nhân viên tự làm, hoà vốn ≤ **4,8 phút**/lần xem lại).
- Kết quả này nói gì về thứ pilot cần học được? Xem lại 100% khiến tiền xem lại chiếm **89,7%** chi phí (**9.480.000 đ**, `simulated`) nên hầu như không tiết kiệm; pilot phải xác định mức giảm tỉ lệ xem lại an toàn và rút thời gian xem lại xuống dưới **4,8–5,1 phút/ca**.
