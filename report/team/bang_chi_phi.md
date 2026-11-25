# Bảng chi phí · Nhiệm vụ A và B

Số tính từ CSV bằng `src/lab13.py`. Các chi phí dựa trên phút `_simulated` được ghi nhãn `simulated`.

## A1 · Ba phép thử

| Phép thử (p = 0,8) | Kết quả |
| --- | ---: |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 | `logix_runs.csv` | đo từ trace |
| Trong đó, lần chạy thứ 2 và 3 | 93.804 | attempt > 1 | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated` | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | 4.373.585 | trace + phút giả lập | simulated |
| Số việc thành công | 978 | `ket_qua` | |
| Chi phí mỗi việc thành công | 4.472 | tổng / 978 | simulated |
| Token + tool / 1.200 yêu cầu | 274,7 | trace | đo từ trace |

CPS gấp **16,3 lần** hóa đơn token + tool chia số yêu cầu. Làm lại là khoản lớn nhất (**51,8%**), kế đến xem lại (**40,7%**) (`simulated`). Tính cả 222 yêu cầu không thành công (148 `chuyen_nhan_vien` + 74 `lam_lai` nhân viên phải xử lý thay, đồng nhất với bảng B3): (4.373.585 + 222 × 12.000) / 1.200 = **5.865 đ/yêu cầu = 0,49×** baseline (`simulated`).

## A3 · Theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Lần chạy/yêu cầu | CPS `[simulated]` | So với 12.000 đ `[simulated]` |
| --- | ---: | ---: | ---: | ---: | ---: |
| `noi_dia` | 824 | 95,0% | 1,11 | 2.696 đ `[simulated]` | 0,22× `[simulated]` |
| `hang_nang` | 158 | 74,1% | 1,47 | 8.221 đ `[simulated]` | 0,69× `[simulated]` |
| `quoc_te` | 150 | 27,3% | 2,32 | 22.515 đ `[simulated]` | 1,88× `[simulated]` |
| `doi_tac` | 68 | 54,4% | 1,88 | 10.215 đ `[simulated]` | 0,85× `[simulated]` |

`quoc_te` không đáng xử lý: CPS **22.515 đ (1,88×)** và chỉ thành công 27,3% `[simulated]`. Tỉ lệ lần chạy `ok` ở attempt 1/2/3 giảm mạnh (30,0% → 11,4% → 2,2%); trần 1→2 lần chỉ nâng số thành công 32→41/150 (CPS 20.403→20.605 đ), còn lần 3 không thêm ca thành công mà đẩy CPS lên 22.515 đ `[simulated]`.

## A4 · Chi phí cố định (phạm vi `noi_dia` + `hang_nang`)

Theo cách tính trong bài mẫu, sản lượng thành công quy đổi trong phạm vi là 45.000 × 900/1.200 = 33.750 việc/tháng. CPS biến đổi của phạm vi là 3.414 đ `[simulated]`, cộng thêm chi phí cố định 40 triệu đ/tháng theo output A4 trong code.

| Khối lượng | Việc thành công/tháng | Cố định/việc | CPS gồm cố định `[simulated]` | So với baseline `[simulated]` |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ `[simulated]` | 0,38× `[simulated]` |
| Nửa khối lượng | 16.875 | 2.370 đ | 5.784 đ `[simulated]` | 0,48× `[simulated]` |

Chi phí cố định không đổi kết luận ở hai mức này; cả hai đều dưới baseline 12.000 đ (`simulated`).

## B1 · Độ nhạy

| Kịch bản | CPS | Thay đổi |
| --- | ---: | ---: |
| Gốc A2 | 4.472 đ `simulated` | — |
| Giá token gấp đôi | 4.723 đ `simulated` | +5,6% |
| Giá token giảm một nửa | 4.346 đ `simulated` | −2,8% |
| Tỉ lệ xem lại gấp đôi | 6.292 đ `simulated` | +40,7% |
| Tỉ lệ xem lại giảm một nửa | 3.562 đ `simulated` | −20,3% |
| Số ca làm lại gấp đôi | 6.787 đ `simulated` | +51,8% |
| Số ca làm lại giảm một nửa | 3.315 đ `simulated` | −25,9% |
| Lương nhân viên tăng 25% | 5.506 đ `simulated` | +23,1% |
| Chạy tối đa 2 lần | 4.237 đ `simulated` | −5,2% |
| Chạy 1 lần | 4.111 đ `simulated` | −8,1% |

## B2 · Đổi một cặp và xếp hạng

Token gấp đôi cùng xem lại gấp đôi: **6.543 đ (+46,3%)**. Ba yếu tố nhạy nhất: **1. làm lại (+51,8%) · 2. xem lại (+40,7%) · 3. lương (+23,1%)**; tác động từ phút lao động là `simulated`.

## B3 · Giới hạn chạy lại và chi phí cả hệ thống

Chi phí cả hệ thống = chi phí trợ lý + 12.000 đ cho mỗi yêu cầu không thành công.

| Giới hạn | Chi phí trợ lý | Không thành công | Chi phí cả hệ thống | CPS |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ `simulated` | 319 | 7.449.781 đ `simulated` | 4.111 đ `simulated` |
| 2 lần | 4.093.220 đ `simulated` | 234 | 6.901.220 đ `simulated` | 4.237 đ `simulated` |
| 3 lần | 4.373.585 đ `simulated` | 222 | 7.037.585 đ `simulated` | 4.472 đ `simulated` |

Giới hạn **2 lần** rẻ nhất cho công ty. CPS thấp nhất là giới hạn **1 lần**, nhưng chuyển thêm 85 yêu cầu sang nhân viên. Chi phí có phút giả lập.

## B4 · Xem lại 100%

Trong phạm vi có 982 yêu cầu, 948 có ít nhất một lượt `ok`, 48 ca làm lại và 900 thành công.

- Xem lại mọi kết quả 5 phút, làm lại 9 phút/ca: **11.743 đ = 0,98×** baseline (`simulated`).
- Nếu dùng thời gian làm lại trung bình 15,3 phút trong CSV: **12.415 đ = 1,03×** baseline (`simulated`).
- Các mức hòa vốn khoảng 5,1 phút (làm lại 9 phút) và 4,8 phút (làm lại 15,3 phút) chỉ xét chi phí agent trên mỗi việc thành công, chưa cộng nhân viên xử lý thay và chi phí cố định (`simulated`). Để trả lời theo chi phí toàn hệ thống, dùng cùng quy ước B3: cộng 12.000 đ cho mỗi yêu cầu agent không hoàn thành để nhân viên xử lý thay; phân bổ chi phí cố định theo A4.

| Thời gian làm lại/ca | Agent + xem lại + làm lại | Nhân viên xử lý thay (82 × 12.000 đ) | Cố định (900 × 1.185,185 đ) | Tổng hệ thống | Tổng / 982 yêu cầu |
| --- | ---: | ---: | ---: | ---: | ---: |
| 9 phút | 10.568.513 đ `[simulated]` | 984.000 đ | 1.066.667 đ | 12.619.180 đ `[simulated]` | **12.850 đ/yêu cầu** `[simulated]` |
| 15,3 phút | 11.173.313 đ `[simulated]` | 984.000 đ | 1.066.667 đ | 13.223.980 đ `[simulated]` | **13.466 đ/yêu cầu** `[simulated]` |

**Cách phân bổ và ngưỡng quyết định:** phạm vi có 982 yêu cầu, 900 thành công và 82 không thành công; phần nhân viên xử lý thay tính theo 82 × 12.000 đ như B3. A4 quy đổi 45.000 yêu cầu/tháng thành 33.750 việc thành công/tháng (tỉ lệ 900/1.200), nên cố định là 40.000.000 / 33.750 = 1.185,185 đ/việc thành công; phân bổ cho 900 việc là 1.066.667 đ. Đây là các con số `[simulated]` theo giả định của bài.

Với thời gian làm lại 15,3 phút/ca, để tổng hệ thống không vượt 12.000 đ × 982 yêu cầu, thời gian xem lại tối đa là **4,24 phút/ca được xem lại** `[simulated]`:

`(982 × 12.000 − 224.513 token/tool − 48 × 15,3 × 2.000 làm lại − 82 × 12.000 xử lý thay − 900 × 1.185,185 cố định) / (948 ca được xem lại × 2.000 đ/phút) = 4,24 phút/ca`.

Ở giả định làm lại 9 phút/ca, giới hạn tương ứng là 4,56 phút/ca `[simulated]`. Vì vậy, pilot cần đo thời gian thực; chỉ giảm tỷ lệ xem lại khi đồng thời đạt ngưỡng sửa + bỏ dưới 15% trong một tuần, không vi phạm luật an toàn và dự báo chi phí toàn hệ thống vẫn ≤ 12.000 đ/yêu cầu. Nếu không đạt, giữ nguyên bước hoặc dừng mở rộng.

## D1 · Cỡ mẫu

| Câu | Kết quả |
| --- | --- |
| a · Chia theo yêu cầu | 1.251 mỗi nhánh để phát hiện chênh 5 điểm |
| b · Theo nhân viên, m = 75 | Design effect 2,48; 3.103 mỗi nhánh; cần 42 nhân viên/nhánh, tổng 84 nên không đủ 40 |
| c · 20 nhân viên mỗi nhánh | Trần hiệu dụng 1.000, dưới 1.251 |
| d · 6 depot mỗi nhánh | Trần hiệu dụng 300 |
| e · Chênh 6 điểm, 20 nhân viên mỗi nhánh | 859 mỗi nhánh; cần 299 yêu cầu/nhân viên; design effect 6,96 |

**Bàn giao E1:** chỉ số chính 994/1.200 = **82,83%**; bỏ qua gợi ý 48/177 = **27,12%**; mở lại 7 ngày 51/1.200 = **4,25%**. Tỉ lệ mở lại trong phạm vi nội địa + hàng nặng là 39/982 = **3,97%**.
