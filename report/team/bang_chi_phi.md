# Bảng chi phí · Nhiệm vụ A và B

Phần A theo mô hình của Người 1 ở commit `0305c30`. Phần A và B được đối chiếu trực tiếp từ hai CSV theo [hướng dẫn lab](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md). Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`.

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
| Trong đó, phần token và tool của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated` | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | 4.373.585 | Token + tool + xem lại + làm lại | simulated |
| Số việc thành công | 978 trên 1.200 yêu cầu | `ket_qua` | |
| Chi phí mỗi việc thành công | 4.472 | Tổng chi phí ÷ 978 | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | (Token + tool) ÷ 1.200 | đo từ trace |

- Chi phí mỗi việc thành công gấp **16,3 lần** hóa đơn token và tool trên mỗi yêu cầu (simulated).
- Làm lại là khoản lớn nhất, chiếm **51,8%** tổng chi phí (simulated).

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công (simulated) | So với 12.000 đ (simulated) |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ | 0,22 lần |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ | 0,69 lần |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ | 1,88 lần |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ | 0,85 lần |

- `quoc_te` tốn **22.515 đ/việc thành công (simulated)**, vượt mốc tự làm. Lượt 2 và 3 có thêm 12 và 2 lượt `ok`, với tỉ lệ `ok` chỉ **11,4%** và **2,2%** trên các lượt tương ứng. Chạy lại có thêm kết quả `ok` nhưng chi phí ở giới hạn 3 vẫn vượt mốc.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định (simulated) | So với 12.000 đ (simulated) |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ | 0,38 lần |
| 22.500 yêu cầu/tháng | 16.875 | 2.370 đ | 5.784 đ | 0,48 lần |

- Cả hai mức khối lượng vẫn dưới 12.000 đ/việc (simulated). Số việc thành công mỗi tháng được ngoại suy bằng khối lượng toàn hệ thống nhân **900/1.200**.

## B1 · Đổi từng yếu tố

Mốc A2 để so sánh là **4.472 đ/việc thành công (simulated)**. Khi cắt lượt chạy, các yêu cầu vượt giới hạn chuyển sang nhân viên và có 0 phút xem lại, làm lại trong chi phí trợ lý.

| Kịch bản | Cách tính | Chi phí mỗi việc thành công (simulated) | Thay đổi (%) |
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

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: **6.543 đ/việc thành công (+46,3%, simulated)**. Hai khoản chi phí tăng cộng dồn và số việc thành công giữ ở 978.
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. Số ca làm lại (+51,8%) · 2. Tỉ lệ xem lại (+40,7%) · 3. Lương nhân viên (+23,1%). Thứ hạng dựa trên mức tăng trong các kịch bản B1 (simulated).

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý (simulated) | Số yêu cầu không thành công | Chi phí cả hệ thống (simulated) | Chi phí mỗi việc thành công (simulated) |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ | 319 | 7.449.781 đ | 4.111 đ |
| 2 lần | 4.093.220 đ | 234 | 6.901.220 đ | 4.237 đ |
| 3 lần | 4.373.585 đ | 222 | 7.037.585 đ | 4.472 đ |

Chi phí cả hệ thống bằng chi phí trợ lý cộng 12.000 đ cho mỗi yêu cầu cần nhân viên làm thay.

- Giới hạn **2 lần** có chi phí hệ thống thấp nhất (6.901.220 đ). Giới hạn **1 lần** có chi phí mỗi việc thành công thấp nhất (4.111 đ) và thêm 85 yêu cầu cần nhân viên xử lý so với 2 lần (simulated).

## B4 · Nếu phải xem lại tất cả

- Trong 982 yêu cầu `noi_dia` và `hang_nang`, xem lại cả 948 yêu cầu có lượt chạy `ok` với 5 phút/yêu cầu. Cộng 224.513 đ token và tool cùng chi phí 48 ca làm lại rồi chia cho 900 việc thành công.
- Với 9 phút làm lại/ca, chi phí là **11.743 đ/việc** (0,98 lần mức 12.000 đ). Với thời gian giả lập trung bình toàn mẫu 15,3 phút/ca, chi phí là **12.415 đ/việc** (1,03 lần), làm tròn đến đồng (simulated).
- Pilot cần đo thời gian xem lại thực tế và xác định mức giảm tỉ lệ xem lại an toàn. Nếu vẫn xem lại 100%, ngưỡng hòa vốn là **5,12 phút/lần** với kịch bản 9 phút và **4,80 phút/lần** với kịch bản 15,3 phút (simulated).
