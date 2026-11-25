# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 · ĐẠT |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 · ĐẠT |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 · ĐẠT |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 | 5.600 lần gọi tool | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | token + tool khi `attempt > 1` | đo từ trace |
| Xem lại | 1.780.000 | 890 phút từ `phut_xem_lai_simulated` | simulated |
| Làm lại | 2.264.000 | 1.132 phút từ `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | 4.373.585 | token + tool + xem lại + làm lại | simulated |
| Số việc thành công | 978 việc | `ket_qua == 'thanh_cong'` | đo từ trace |
| Chi phí mỗi việc thành công | 4.472 | tổng chi phí / 978 | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | (token + tool) / 1.200 | đo từ trace |

- Chi phí mỗi việc thành công gấp **16,3 lần** (simulated) hoá đơn token và tool trên mỗi yêu cầu.
- Làm lại là khoản lớn nhất, chiếm **51,8%** tổng chi phí (simulated).
- Chi phí cả hệ thống là **5.865 đ/yêu cầu** (simulated, **0,49×** mức nhân viên tự làm), tính bằng (4.373.585 + 222 × 12.000) / 1.200.

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công (simulated) | So với 12.000 đ (simulated) |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ | 0,22× |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ | 0,69× |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ | 1,88× |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ | 0,85× |

- `quoc_te` tốn **1,88×** mức nhân viên tự làm (simulated). Chạy lại ít hiệu quả vì chỉ **11,4%** lượt 2 và **2,2%** lượt 3 có trạng thái `ok`.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định (simulated) | So với 12.000 đ (simulated) |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ | 0,38× |
| 22.500 yêu cầu/tháng | 16.875 | 2.370 đ | 5.784 đ | 0,48× |

- Lấy **900/1.200** nhân khối lượng tháng để ước tính số việc thành công trong phạm vi, rồi chia **40 triệu đ** cho số việc đó. Cả hai mức chi phí sau phân bổ đều dưới **12.000 đ/việc** (simulated).

## B1 · Đổi từng yếu tố

| Kịch bản | Cách tính | Chi phí mỗi việc thành công (simulated) | Thay đổi so với A2 (simulated) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token, giá tool giữ nguyên | 4.723 đ | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ cho 1.000 token | 4.346 đ | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lượt có `attempt > 2`. Ca vượt giới hạn chuyển cho nhân viên và tính 0 phút xem lại, làm lại. | 4.237 đ | −5,2% |
| Chỉ cho chạy 1 lần | Áp dụng quy tắc trên với giới hạn 1 lượt | 4.111 đ | −8,1% |

## B2 · Đổi một cặp và xếp hạng

- Gấp đôi giá token và tỉ lệ xem lại cho **6.543 đ/việc thành công**, tăng **46,3% = 5,6% + 40,7%** (simulated).
- Ba yếu tố nhạy nhất trong các kịch bản đã thử (simulated) là **số ca làm lại (+51,8%)**, **tỉ lệ xem lại (+40,7%)** và **lương nhân viên (+23,1%)**.

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý (simulated) | Số yêu cầu không thành công | Chi phí cả hệ thống (simulated) | Chi phí mỗi việc thành công (simulated) |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ | 319 | 7.449.781 đ | 4.111 đ |
| 2 lần | 4.093.220 đ | 234 | 6.901.220 đ | 4.237 đ |
| 3 lần | 4.373.585 đ | 222 | 7.037.585 đ | 4.472 đ |

- **2 lượt** rẻ nhất cho hệ thống (**6.901.220 đ**), tính cả **12.000 đ** mỗi ca nhân viên làm thay. **1 lượt** rẻ nhất theo chi phí trợ lý trên mỗi việc thành công (**4.111 đ**) và tăng **85** ca làm thay (chi phí simulated).

## B4 · Nếu phải xem lại tất cả

- Với `noi_dia` + `hang_nang`, cộng token và tool của **982** yêu cầu, **948** lượt xem lại (5 phút/lượt) và **48** ca làm lại, rồi chia cho **900** việc thành công.
- Chi phí mỗi việc thành công là **11.743 đ** ở **9 phút** làm lại/ca và **12.415 đ** ở **15,30 phút**/ca (simulated), bằng **0,98×** và **1,03×** mức 12.000 đ.
- Pilot cần đo tỉ lệ xem lại có thể giảm an toàn và số phút mỗi lượt. Nếu vẫn xem lại 100%, hòa vốn ở **5,12** hoặc **4,80 phút/lượt** theo hai kịch bản (simulated).
