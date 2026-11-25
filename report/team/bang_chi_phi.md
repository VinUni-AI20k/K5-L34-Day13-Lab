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
| Hoá đơn token và tool chia cho số yêu cầu | 274,65 | | đo từ trace |

- Chi phí mỗi việc thành công gấp bao nhiêu lần "hoá đơn chia số yêu cầu"? Gấp **16,28 lần** (4.472 đ [simulated] so với 274,65 đ).
- Khoản nào chiếm tỉ trọng lớn nhất trong tổng chi phí, bao nhiêu phần trăm? **Làm lại** chiếm tỉ trọng lớn nhất với **51,77%** (2.264.000 đ / 4.373.585 đ, simulated); tiếp theo là xem lại **40,70%** (simulated).

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ (simulated) | 0,22× (simulated) |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ (simulated) | 0,69× (simulated) |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ (simulated) | 1,88× (simulated) |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ (simulated) | 0,85× (simulated) |

- Loại nào không đáng để trợ lý xử lý? Với loại đó, cho chạy lại tới 3 lần có giúp không? **`quoc_te`** không đáng để trợ lý xử lý (22.515 đ = 1,88× so với 12.000 đ, simulated; thành công chỉ 27,3%). Chạy lại tới 3 lần không giúp vì tỉ lệ `status=ok` giảm mạnh qua từng lần: lần 1 **30,0%**, lần 2 **11,4%**, lần 3 **2,2%**.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ (simulated) | 0,38× (simulated) |
| Một nửa khối lượng | 16.875 | 2.370 đ | 5.784 đ (simulated) | 0,48× (simulated) |

- Chi phí cố định có đổi kết luận không? Ở khối lượng nào? **Không đổi kết luận** ở cả 45.000 yêu cầu/tháng (4.599 đ = 0,38×, simulated) và một nửa khối lượng (5.784 đ = 0,48×, simulated), dù phần cố định tăng gấp đôi từ 1.185 đ lên 2.370 đ/việc. Lưu ý cần tính thêm phần nhân viên làm thay (chi phí cả hệ thống 5.865 đ/yêu cầu = 0,49× trên toàn mẫu, simulated) khi so với 12.000 đ.

## B1 · Đổi từng yếu tố

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 đ (simulated) | +5,62% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ (simulated) | -2,81% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ (simulated) | +40,70% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ (simulated) | -20,35% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ (simulated) | +51,77% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ (simulated) | -25,88% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ (simulated) | +23,12% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 đ (simulated) | -5,25% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 đ (simulated) | -8,07% |

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: **6.543 đ** (+46,31%, simulated) — đúng bằng tổng hai tác động riêng (+5,62% và +40,70%) vì mô hình cộng tuyến tính.
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. **Số ca làm lại** (+51,77%, simulated) · 2. **Tỉ lệ xem lại** (+40,70%, simulated) · 3. **Lương nhân viên** (+23,12%, simulated).

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ (simulated) | 319 | 7.449.781 đ (simulated) | 4.111 đ (simulated) |
| 2 lần | 4.093.220 đ (simulated) | 234 | 6.901.220 đ (simulated) | 4.237 đ (simulated) |
| 3 lần | 4.373.585 đ (simulated) | 222 | 7.037.585 đ (simulated) | 4.472 đ (simulated) |

- Giới hạn nào rẻ nhất cho công ty? Có trùng với giới hạn cho chi phí mỗi việc thành công thấp nhất không? Giới hạn **2 lần** rẻ nhất cho cả hệ thống (**6.901.220 đ**, simulated), **không trùng** với giới hạn cho CPS thấp nhất là **1 lần** (**4.111 đ**, simulated) vì giới hạn 1 lần đẩy thêm **85 yêu cầu** sang nhân viên tự làm (319 so với 234).

## B4 · Nếu phải xem lại tất cả

- Chi phí mỗi việc thành công khi xem lại 100% (`noi_dia` + `hang_nang`), so với 12.000 đ: Với 9 phút làm lại/ca, CPS là **11.743 đ = 0,98×** của 12.000 đ (simulated; hoà vốn khi xem lại ≤ 5,12 phút/ca). Với mức trung bình dữ liệu **15,3 phút/ca**, CPS lên **12.415 đ = 1,03×** (simulated; đắt hơn nhân viên tự làm, hoà vốn khi xem lại ≤ 4,80 phút/ca).
- Kết quả này nói gì về thứ pilot cần học được? Xem lại 100% gần như không tiết kiệm (tiền xem lại chiếm ~90% tổng chi phí), nên pilot phải đo thời gian xem lại/làm lại thật và tìm mức giảm tỉ lệ xem lại an toàn mà không làm tăng ca làm lại.
