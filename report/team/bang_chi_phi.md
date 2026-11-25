# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py` (hàm `mo_hinh`), người kiểm số tính lại độc lập và cho cùng kết quả. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

Giá dùng chung (giả định của lab): token vào 26 đ, token ra 130 đ cho 1.000 token; tool 15 đ/lần; nhân viên 2.000 đ/phút; nhân viên tự làm 12.000 đ/yêu cầu.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 (= 1/p: số lần chạy 1,24 chia tỉ lệ thành công 99,2%) |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv`, cả 1.624 lần chạy | đo từ trace |
| Tool | 84.000 | `logix_runs.csv`, 5.600 lần gọi × 15 đ | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated`, 890 phút × 2.000 đ | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated`, 1.132 phút × 2.000 đ | simulated |
| Tổng chi phí | 4.373.585 | | có phần simulated |
| Số việc thành công | 978 / 1.200 | `ket_qua == 'thanh_cong'` | |
| Chi phí mỗi việc thành công | 4.472 | 4.373.585 ÷ 978 | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | (245.585 + 84.000) ÷ 1.200 | đo từ trace |

- Chi phí mỗi việc thành công gấp **16,3 lần** hoá đơn chia số yêu cầu (4.472 so với 274,7 đ) [simulated].
- Khoản lớn nhất là **làm lại, 51,8%** tổng chi phí, tiếp theo là xem lại 40,7% [simulated]. Giờ nhân viên chiếm 92,5%, token và tool chỉ 7,5%.
- Tử số cộng mọi lần chạy, kể cả lần lỗi, vì lần lỗi vẫn tốn token và tool. Mẫu số chỉ đếm 978 việc thành công, nên chi phí của các lần hỏng dồn vào những việc làm xong.
- So với nhân viên tự làm phải tính cả 222 ca không thành công do nhân viên làm thay: (4.373.585 + 222 × 12.000) ÷ 1.200 = **5.865 đ/yêu cầu, bằng 0,49 lần 12.000 đ** [simulated].

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công [simulated] | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ | 0,22× |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ | 0,69× |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ | 1,88× |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ | 0,85× |

Tỉ lệ lần chạy đạt `ok` theo lần thử (đo từ trace):

| Loại | Lần 1 | Lần 2 | Lần 3 |
| --- | ---: | ---: | ---: |
| noi_dia | 91,0% | 75,7% | 38,9% |
| hang_nang | 70,9% | 39,1% | 17,9% |
| quoc_te | 30,0% | 11,4% | 2,2% |
| doi_tac | 51,5% | 18,2% | 14,8% |

- **quoc_te không đáng để trợ lý xử lý**: 22.515 đ, bằng 1,88 lần 12.000 đ, chỉ 27,3% thành công [simulated].
- Chạy lại tới 3 lần không giúp loại này. Lần 2 chỉ đúng 11,4%, lần 3 chỉ 2,2%: lỗi lặp lại trên cùng yêu cầu, nên các lần chạy độc lập p = 0,8 trong A1 không còn đúng.
- doi_tac sát ngưỡng (0,85×) [simulated] và có điều khoản riêng, nên cũng để ngoài phạm vi pilot.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

Trong phạm vi có 982 yêu cầu, 900 việc thành công, tổng 3.072.513 đ, tức 3.414 đ mỗi việc thành công [simulated]. Ở quy mô đầy đủ, số việc thành công mỗi tháng là 45.000 × 900 ÷ 1.200 = 33.750.

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ [simulated] | 0,38× |
| Một nửa khối lượng | 16.875 | 2.370 đ | 5.784 đ [simulated] | 0,48× |

- Ở 45.000 yêu cầu/tháng, chi phí cố định 40 triệu đ không đổi kết luận: 4.599 đ vẫn bằng 0,38 lần 12.000 đ [simulated].
- Khi khối lượng giảm một nửa, như lúc pilot, phần cố định tăng gấp đôi lên 2.370 đ/việc. Hồ sơ phải ghi rõ con số đã cộng cố định hay chưa, và ở khối lượng nào.

## B1 · Đổi từng yếu tố

Mức gốc (A2): 4.472 đ [simulated]. Mỗi dòng chỉ đổi một yếu tố.

| Kịch bản | Cách tính | Chi phí mỗi việc thành công [simulated] | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 đ | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 đ (966 thành công) | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 đ (881 thành công) | −8,1% |

Tự kiểm tra: mỗi kịch bản "giảm một nửa" giảm đúng bằng nửa mức tăng của "gấp đôi" (5,6 → 2,8; 40,7 → 20,3; 51,8 → 25,9), vì mô hình cộng tuyến tính.

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: **6.543 đ (+46,3%)** [simulated], đúng bằng tổng hai tác động riêng (+5,6% và +40,7%) vì mô hình cộng tuyến tính.
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. **số ca làm lại** (+51,8% / −25,9%) · 2. **tỉ lệ xem lại** (+40,7% / −20,3%) · 3. **lương nhân viên** (+23,1% khi tăng 25%). Giá token xếp cuối (+5,6% / −2,8%) [simulated].

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

Chi phí cả hệ thống = tổng chi phí trợ lý + 12.000 đ × số yêu cầu không thành công, vì nhân viên phải làm thay.

| Giới hạn | Tổng chi phí trợ lý [simulated] | Số yêu cầu không thành công | Chi phí cả hệ thống [simulated] | Chi phí mỗi việc thành công [simulated] |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ | 319 | 7.449.781 đ | 4.111 đ (thấp nhất) |
| 2 lần | 4.093.220 đ | 234 | **6.901.220 đ (rẻ nhất)** | 4.237 đ |
| 3 lần | 4.373.585 đ | 222 | 7.037.585 đ | 4.472 đ |

- Giới hạn **2 lần** rẻ nhất cho công ty: 6.901.220 đ, thấp hơn 3 lần 136.365 đ [simulated].
- Không trùng với giới hạn cho chi phí mỗi việc thành công thấp nhất (1 lần, 4.111 đ) [simulated]. Giới hạn 1 lần đẩy thêm 85 yêu cầu sang nhân viên so với 2 lần (319 so với 234).

## B4 · Nếu phải xem lại tất cả

Cách tính trên noi_dia + hang_nang (982 yêu cầu): 948 yêu cầu có ít nhất một lần chạy ok × 5 phút × 2.000 đ = 9.480.000 đ; 48 ca làm lại × 9 phút × 2.000 đ = 864.000 đ; token + tool của mọi lần chạy = 224.513 đ. Tổng 10.568.513 đ ÷ 900 việc thành công.

- Xem lại 100% cho **11.743 đ mỗi việc thành công, bằng 0,98 lần 12.000 đ** [simulated], gần như không tiết kiệm được gì.
- Nếu dùng 15,3 phút làm lại mỗi ca (trung bình cột `phut_lam_lai_simulated`) thay cho 9 phút: 12.415 đ = 1,03×, đắt hơn nhân viên tự làm [simulated].
- Pilot phải tìm tỉ lệ xem lại thấp nhất mà vẫn an toàn. Để hoà vốn, mỗi lần xem lại phải ≤ 5,1 phút (làm lại 9 phút) hoặc ≤ 4,8 phút (làm lại 15,3 phút) [simulated].
