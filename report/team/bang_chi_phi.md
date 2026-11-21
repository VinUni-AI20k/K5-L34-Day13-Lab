# Bảng chi phí · Nhiệm vụ A và B

Người 2 kiểm độc lập bằng Python trên hai CSV trong `src/`, theo công thức của lab. Bảng chờ đối chiếu với `src/lab13.py` sau bàn giao CP1–CP2. Các chi phí làm tròn đến đồng, phần trăm tính từ số chưa làm tròn.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1 + 0,2 = **1,20** |
| Số lần chạy trung bình, chạy đến khi đúng | 1 / 0,8 = **1,25** |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | (1 + 0,2 + 0,04) / (1 − 0,2³) = **1,25** |

## A2 · Mô hình chi phí từ trace

| Khoản | Giá trị | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 đ | (5.771.712 × 26 + 734.774 × 130) / 1.000 | đo từ trace |
| Tool | 84.000 đ | 5.600 × 15 | đo từ trace |
| Trong đó, phần token và tool của lần chạy thứ 2 và 3 | 93.804 đ | `attempt` > 1 | đo từ trace |
| Xem lại | 1.780.000 đ | 890 phút × 2.000 từ `phut_xem_lai_simulated` | simulated |
| Làm lại | 2.264.000 đ | 1.132 phút × 2.000 từ `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | 4.373.585 đ | Token + tool + xem lại + làm lại | simulated |
| Số việc thành công | 978 yêu cầu | `ket_qua == 'thanh_cong'` | đếm từ dữ liệu |
| Chi phí mỗi việc thành công | 4.472 đ/việc | 4.373.585 / 978 | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 đ/yêu cầu | (245.585 + 84.000) / 1.200 | đo từ trace |

- Chi phí mỗi việc thành công gấp **16,3 lần** hóa đơn chia số yêu cầu (simulated).
- Làm lại chiếm lớn nhất, **51,8%** (simulated). Xem lại và làm lại cộng lại chiếm **92,5%** (simulated).
- Kiểm tra bằng phép tính trực tiếp: `(4.373.585 + 222 × 12.000) / 1.200 ≈ 5.865 đ/yêu cầu` (simulated), bằng **0,49×** chi phí nhân viên tự làm theo quy ước B3. Mọi lần chạy đều phát sinh phí, còn mẫu số của chi phí mỗi việc thành công chỉ gồm 978 việc xử lý thành công.

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công (simulated) | So với 12.000 đ (simulated) |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% (783/824) | 1,11 (916/824) | 2.696 đ | 0,22× |
| hang_nang | 158 | 74,1% (117/158) | 1,47 (232/158) | 8.221 đ | 0,69× |
| quoc_te | 150 | 27,3% (41/150) | 2,32 (348/150) | 22.515 đ | 1,88× |
| doi_tac | 68 | 54,4% (37/68) | 1,88 (128/68) | 10.215 đ | 0,85× |

- `quoc_te` có chi phí **1,88×** (simulated). Tỉ lệ `ok` lần 1–3 giảm từ **30,0%** còn **11,4%** và **2,2%**. Lần 3 chỉ thêm 2 lượt `ok` trên 93 lần chạy, nên lợi ích biên thấp.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng toàn hệ thống | Việc thành công trong phạm vi mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định (simulated) | So với 12.000 đ (simulated) |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ | 0,38× |
| 22.500 yêu cầu/tháng | 16.875 | 2.370 đ | 5.784 đ | 0,48× |

- Dùng 900/1.200 để dự phóng việc thành công trong phạm vi theo khối lượng toàn hệ thống. Chia 40 triệu đ cho số việc này rồi cộng chi phí biến đổi **3.414 đ/việc** (simulated).
- Cả hai kịch bản vẫn dưới 12.000 đ theo phép so trên mỗi việc trợ lý làm xong. Ở nửa khối lượng, phần cố định tăng từ **1.185** lên **2.370 đ/việc**.

## B1 · Đổi từng yếu tố

Mốc so sánh là **4.472 đ/việc** (simulated) của A2 trên toàn bộ **1.200 yêu cầu**. Với giá token, xem lại và làm lại, mức giảm của kịch bản chia đôi bằng một nửa mức tăng của kịch bản gấp đôi khi tính trước khi làm tròn.

| Kịch bản | Cách tính | Chi phí mỗi việc thành công (simulated) | Thay đổi so với A2 (simulated) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token, giữ nguyên giá tool | 4.723 đ | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ cho 1.000 token | 4.346 đ | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lượt có `attempt > 2`. Chuyển yêu cầu có `so_lan_chay > 2` cho nhân viên và đặt phút xem lại, làm lại của trợ lý bằng 0 | 4.237 đ | −5,2% |
| Chỉ cho chạy 1 lần | Cùng cách tính với giới hạn 1 | 4.111 đ | −8,1% |

## B2 · Đổi một cặp và xếp hạng

- Gấp đôi giá token và tỉ lệ xem lại cho **6.543 đ/việc (+46,3%)** (simulated). Mức tăng bằng tổng hai tác động riêng vì hai khoản cộng tuyến tính và mẫu số giữ nguyên.
- Ba yếu tố ảnh hưởng mạnh nhất theo mức tăng (simulated) là **số ca làm lại (+51,8%)**, **tỉ lệ xem lại (+40,7%)** và **lương nhân viên (+23,1%)**.

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý (simulated) | Số yêu cầu không thành công | Chi phí cả hệ thống (simulated) | Chi phí mỗi việc thành công (simulated) |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ | 319 | 7.449.781 đ | **4.111 đ** |
| 2 lần | 4.093.220 đ | 234 | **6.901.220 đ** | 4.237 đ |
| 3 lần | 4.373.585 đ | 222 | 7.037.585 đ | 4.472 đ |

- Tổng hệ thống = chi phí trợ lý + 12.000 đ cho mỗi yêu cầu không thành công. **2 lần** rẻ nhất cho công ty. **1 lần** rẻ nhất trên mỗi việc trợ lý làm xong nhưng chuyển thêm **85** việc cho nhân viên so với 2 lần.

## B4 · Nếu phải xem lại tất cả

Các mức dưới đây tính chi phí biến đổi trên mỗi việc trợ lý làm xong. Để so tổng ngân sách với luồng thủ công, cần dùng chi phí cả hệ thống trên mỗi yêu cầu theo cách tính B3 và cộng phần cố định A4 ở cùng khối lượng.

- Xem lại 100% kết quả `ok` trong `noi_dia` + `hang_nang`: `(224.513 + 948 × 5 × 2.000 + 48 × 9 × 2.000) / 900` ≈ **11.743 đ/việc**, bằng **0,98×** (simulated). Dùng thời gian làm lại trung bình **15,3 phút/ca** từ cột `_simulated` cho **12.415 đ/việc**, bằng **1,03×** (simulated).
- Pilot cần đo thời gian xem lại thực tế và xác định tỉ lệ xem lại có thể giảm an toàn. Ngưỡng hòa vốn theo cùng mẫu số là **5,1 phút** nếu làm lại 9 phút/ca hoặc **4,8 phút** nếu làm lại 15,3 phút/ca (simulated).
