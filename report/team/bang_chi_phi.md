# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 — ĐẠT |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 — ĐẠT |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 — ĐẠT |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585,13 | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 | `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804,49 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated` | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | 4.373.585,13 | cộng bốn khoản | simulated |
| Số việc thành công | 978 | `ket_qua` | đo từ trace |
| Chi phí mỗi việc thành công | 4.471,97 | tổng / 978 | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,65 | | đo từ trace |

- Chi phí mỗi việc thành công gấp bao nhiêu lần "hoá đơn chia số yêu cầu"? Gấp **16,28 lần** (4.471,97 đ / 274,65 đ, `simulated`). Khi cộng 222 ca không thành công (× 12.000 đ), chi phí cả hệ thống là **5.864,65 đ/yêu cầu = 0,49×** so với 12.000 đ (`simulated`).
- Khoản nào chiếm tỉ trọng lớn nhất trong tổng chi phí, bao nhiêu phần trăm? **Làm lại** lớn nhất với **51,77%** (2.264.000 / 4.373.585,13 đ, `simulated`), tiếp theo là Xem lại 40,70% (`simulated`); tổng giờ nhân viên chiếm 92,46%.

## A3 · Tách theo loại yêu cầu

Cột chi phí và tỉ số chi phí đều `simulated`; chưa gồm nhân viên làm thay.

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công (`simulated`) | So với 12.000 đ (`simulated`) |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,02% | 1,11 | 2.695,64 đ | 0,225× |
| hang_nang | 158 | 74,05% | 1,47 | 8.220,73 đ | 0,685× |
| quoc_te | 150 | 27,33% | 2,32 | 22.515,17 đ | 1,876× |
| doi_tac | 68 | 54,41% | 1,88 | 10.214,87 đ | 0,851× |

- Loại nào không đáng để trợ lý xử lý? Với loại đó, cho chạy lại tới 3 lần có giúp không? `quoc_te` không đáng để trợ lý xử lý (22.515,17 đ = 1,876× baseline `simulated`, tỉ lệ thành công 27,33%). Chạy lại tới 3 lần không giúp vì tỉ lệ `ok` giảm mạnh: lần 1/2/3 là 30,0% / 11,43% / 2,15%. `doi_tac` chỉ 54,41% thành công (0,851×) và có điều khoản riêng nên cũng loại khỏi pilot.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

Chi phí và tỉ số đều `simulated`. Khối lượng tổng 45.000 nhân tỉ lệ 900/1.200 thành công trong phạm vi; không dùng 900/982 để ngoại suy toàn công ty.

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định (`simulated`) | So với 12.000 đ (`simulated`) |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185,19 đ | 4.599,09 đ | 0,383× |
| Một nửa khối lượng (22.500 yêu cầu/tháng) | 16.875 | 2.370,37 đ | 5.784,27 đ | 0,482× |

- Chi phí cố định có đổi kết luận không? Ở khối lượng nào? Không đổi kết luận ở cả 45.000 yêu cầu/tháng (**4.599,09 đ = 0,383×**) và 22.500 yêu cầu/tháng (**5.784,27 đ = 0,482×**, `simulated`), dù chi phí cố định mỗi việc tăng gấp đôi (1.185,19 đ → 2.370,37 đ) khi khối lượng giảm một nửa.

## B1 · Đổi từng yếu tố

Toàn bộ chi phí và thay đổi chi phí B1–B4: **simulated**. Các số dưới đây dùng dấu phẩy phân cách nghìn, dấu chấm thập phân.

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4,723.08 đ | +5.62% | 
| Giá token giảm một nửa | 13 đ và 65 đ | 4,346.41 đ | -2.81% | 
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6,292.01 đ | +40.70% | 
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3,561.95 đ | -20.35% | 
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6,786.90 đ | +51.77% | 
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3,314.50 đ | -25.88% | 
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5,505.71 đ | +23.12% | 
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4,237.29 đ | -5.25% | 
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4,110.99 đ | -8.07% | 

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: 6.543,12 đ, +46,31% (`simulated`), bằng tổng hai tác động riêng do mô hình cộng tuyến tính. 
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. Số ca làm lại (+51,77%) · 2. Tỉ lệ xem lại (+40,70%) · 3. Lương nhân viên (+23,12%); `simulated`. 

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3,621,780.64 | 319 | 7,449,780.64 | 4,110.99 | 
| 2 lần | 4,093,220.23 | 234 | 6,901,220.23 | 4,237.29 | 
| 3 lần | 4,373,585.13 | 222 | 7,037,585.13 | 4,471.97 | 

- Giới hạn nào rẻ nhất cho công ty? Có trùng với giới hạn cho chi phí mỗi việc thành công thấp nhất không? 2 lần rẻ nhất cho công ty: 6.901.220,23 đ; 1 lần có CPS thấp nhất 4.110,99 đ nhưng đẩy thêm 85 yêu cầu sang nhân viên (`simulated`). 

## B4 · Nếu phải xem lại tất cả

Phạm vi 982 yêu cầu `noi_dia` + `hang_nang`; xem lại 5 phút cho 948 yêu cầu có ít nhất 1 lần `ok`, 48 ca làm lại, 900 việc thành công; token + tool mọi lần chạy = 224.513,27 đ. 

| Làm lại (phút/ca) | Xem lại (đ) | Làm lại (đ) | Tổng (đ) | CPS (đ) | /12.000 | Hòa vốn phút xem lại |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | 
| 9 | 9,480,000.00 | 864,000.00 | 10,568,513.27 | 11,742.79 | 0.979× | 5.12 | 
| 15.3 | 9,480,000.00 | 1,468,800.00 | 11,173,313.27 | 12,414.79 | 1.035× | 4.80 | 

- Mọi khoản tiền, tỉ số và phút hòa vốn B4 là **simulated**; 15,3 phút là giả định làm tròn từ trung bình CSV 15,2973 phút (trung vị 14,5 phút). 
- Xem lại 100% gần hết lợi ích: 11.742,79 đ/việc ở 9 phút, tăng thành 12.414,79 đ/việc ở 15,3 phút (`simulated`); chưa gồm cố định và làm thay ca chuyển nhân viên. 
- Pilot cần đo phút thật, học cách giảm xem lại an toàn; mức hòa vốn là 5,12 hoặc 4,80 phút/lượt (`simulated`), không suy ra đã tiết kiệm chỉ từ CPS. 

B3 dùng đúng quy ước đề: tổng trợ lý + 12.000 đ × mọi yêu cầu không thành công, gồm cả `lam_lai`; đây là kịch bản so sánh, có thể chồng chi phí làm lại. So sánh toàn mẫu: 7.037.585,13 / 1.200 = 5.864,65 đ/yêu cầu (`simulated`). 
