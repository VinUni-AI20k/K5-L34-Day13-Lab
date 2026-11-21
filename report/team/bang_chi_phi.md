# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 |

**Tính tay kiểm chứng ($p = 0{,}8$, tỉ lệ lỗi $1 - p = 0{,}2$):**
- Phép thử 1 ($k = 2$): $E[\text{số lần chạy}] = \frac{1 - (1 - p)^k}{p} = \frac{1 - (1 - 0{,}8)^2}{0{,}8} = \frac{1 - 0{,}04}{0{,}8} = \frac{0{,}96}{0{,}8} = \mathbf{1{,}20}$.
- Phép thử 2 ($k \to \infty$, chạy đến khi đúng): $E[\text{số lần chạy}] = \frac{1}{p} = \frac{1}{0{,}8} = \mathbf{1{,}25}$.
- Phép thử 3 ($k = 3$): $P(\text{thành công}) = 1 - (1 - p)^3 = 1 - 0{,}2^3 = 0{,}992$; $E[\text{số lần chạy}] = \frac{1 - 0{,}2^3}{0{,}8} = 1{,}24 \Rightarrow \text{Hệ số chi phí} = \frac{E[\text{số lần chạy}]}{P(\text{thành công})} = \frac{1{,}24}{0{,}992} = \frac{1}{0{,}8} = \mathbf{1{,}25}$ (thừa số $1 - (1 - p)^k$ triệt tiêu).

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 | `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated` | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | 4.373.585 | | có phần simulated |
| Số việc thành công | 978 | `ket_qua` | đo từ dữ liệu yêu cầu |
| Chi phí mỗi việc thành công | 4.472 | tổng chi phí / thành công | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | (token + tool) / 1.200 | đo từ trace |

- Chi phí mỗi việc thành công khoảng **16,3 lần** hoá đơn token và tool chia cho số yêu cầu (4.472 / 274,7 đồng, simulated).
- **Làm lại** chiếm phần lớn nhất: 2.264.000 đồng, tương đương **51,8%** tổng chi phí [simulated]. Xem lại chiếm 40,7% [simulated] (chi phí nhân viên chiếm 92,5% tổng chi phí).

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ [simulated] | 0,22× |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ [simulated] | 0,69× |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ [simulated] | 1,88× |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ [simulated] | 0,85× |

- `quoc_te` không đáng để trợ lý xử lý: chi phí **22.515 đ/việc** [simulated] (`1,88×` so với `12.000 đ`) và tỉ lệ thành công chỉ **27,3%**. Chạy lại tới 3 lần không giúp vì trung bình đã chạy **2,32 lần/yêu cầu** nhưng phần lớn vẫn thất bại.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ [simulated] | 0,38× |
| Một nửa khối lượng | 16.875 | 2.370 đ | 5.784 đ [simulated] | 0,48× |

- Không đổi kết luận ở quy mô 45.000 yêu cầu/tháng (4.599 đ/việc, bằng 0,38× của 12.000 đ); ở một nửa sản lượng chi phí tăng lên 5.784 đ/việc (0,48×) nhưng vẫn thấp hơn baseline. Các ước tính này dùng thời gian nhân viên simulated.

## B1 · Đổi từng yếu tố

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 đ [simulated] | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ [simulated] | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ [simulated] | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ [simulated] | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ [simulated] | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ [simulated] | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ [simulated] | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 đ [simulated] | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 đ [simulated] | −8,1% |

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: **6.543 đ (+46,3%, simulated)** — đúng bằng tổng hai tác động riêng (`+5,6% + 40,7%`) vì mô hình cộng tuyến tính.
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: **1. Số ca làm lại** · **2. Tỉ lệ xem lại** · **3. Lương nhân viên**.

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ [simulated] | 319 | 7.449.781 đ [simulated] | 4.111 đ [simulated] |
| 2 lần | 4.093.220 đ [simulated] | 234 | 6.901.220 đ [simulated] | 4.237 đ [simulated] |
| 3 lần | 4.373.585 đ [simulated] | 222 | 7.037.585 đ [simulated] | 4.472 đ [simulated] |

- Giới hạn **2 lần** rẻ nhất cho công ty (**6.901.220 đ**, simulated), không trùng với giới hạn **1 lần** có chi phí mỗi việc thành công thấp nhất (**4.111 đ**), vì giới hạn 1 lần đẩy thêm **85** việc sang nhân viên (`12.000 đ`/việc).

## B4 · Nếu phải xem lại tất cả

- Chi phí mỗi việc thành công khi xem lại 100% (`noi_dia` + `hang_nang`), so với 12.000 đ: Với 9 phút/ca làm lại là **11.743 đ = 0,98×** [simulated]; với thời gian làm lại trung bình từ dữ liệu `simulated` là `15,3 phút/ca` là **12.415 đ = 1,03×** [simulated] (đắt hơn nhân viên tự làm). Mức hoà vốn xem lại là `≤ 5,1 phút` (hoặc `≤ 4,8 phút` với 15,3 phút làm lại).
- Pilot phải đo được **tỉ lệ xem lại có thể giảm an toàn xuống mức nào** và **mỗi lần xem lại có rút ngắn dưới 5 phút được không**, vì tiền xem lại chiếm **89,7%** tổng chi phí ở kịch bản làm lại 9 phút/ca (`9.480.000 / 10.568.513 đ`, simulated).
