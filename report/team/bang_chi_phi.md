# Bảng chi phí · Nhiệm vụ A và B

Tính bằng `src/lab13.py` từ hai CSV giả lập, theo `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`. Giá tiền theo giả định của lab; không làm tròn trong phép tính.

Các chi phí, tỷ số và thay đổi phụ thuộc phút nhân viên được ghi nhãn **simulated**. Chi phí mỗi việc thành công (CPS) chưa gồm chi phí cố định hoặc xử lý thủ công bổ sung, trừ khi ghi rõ.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 |

## A2 · Mô hình chi phí từ trace

| Khoản | Giá trị (đ, trừ số việc) | Nguồn | Nhãn |
| --- | --- | --- | --- |
| Token | 245.585 | Mọi trace: tokens_in, tokens_out | đo từ trace |
| Tool | 84.000 | Mọi trace: tool_calls | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt > 1; đã nằm trong token + tool | đo từ trace |
| Xem lại | 1.780.000 | phut_xem_lai_simulated × 2.000 | simulated |
| Làm lại | 2.264.000 | phut_lam_lai_simulated × 2.000 | simulated |
| Tổng chi phí | 4.373.585 | Token + tool + xem lại + làm lại | simulated |
| Số việc thành công | 978 | ket_qua == 'thanh_cong' | đếm từ dữ liệu |
| Chi phí mỗi việc thành công | 4.472 | Tổng / số việc thành công | simulated |
| Hóa đơn token và tool chia cho số yêu cầu | 274,7 | (Token + tool) / số yêu cầu | đo từ trace |

- CPS gấp **16,3 lần** hóa đơn mỗi yêu cầu (simulated); tử số tính mọi lần chạy vì đều phát sinh tiền, mẫu số chỉ đếm 978 việc thành công.
- Làm lại chiếm nhiều nhất: **51,8%** tổng chi phí (simulated).

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Lần chạy/yêu cầu | CPS (đ, simulated) | CPS / 12.000 (simulated) |
| --- | --- | --- | --- | --- | --- |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 | 0,22× |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 | 0,69× |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 | 1,88× |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 | 0,85× |

- Quốc tế không đáng xử lý: CPS 22.515 đ (simulated); tỷ lệ trace ok ở lần 1/2/3 là 30,0% / 11,4% / 2,2%, chạy lại đến lần 3 có hiệu quả rất thấp. Phạm vi đề xuất: noi_dia + hang_nang.
- Cột so với 12.000 chỉ là tỷ số CPS, chưa chứng minh mức tiết kiệm của toàn hệ thống; B3 cộng xử lý thủ công cho các yêu cầu không thành công.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng toàn công ty | Việc thành công trong phạm vi/tháng | Cố định/việc (đ) | CPS + cố định (đ, simulated) | So với 12.000 (simulated) |
| --- | --- | --- | --- | --- |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 | 4.599 | 0,38× |
| 22.500 yêu cầu/tháng | 16.875 | 2.370 | 5.784 | 0,48× |

- Quy đổi số thành công bằng khối lượng toàn công ty × 900/1200; giả định cơ cấu yêu cầu và hiệu suất giữ nguyên.
- Cố định chưa đổi kết luận CPS dưới 12.000 đ ở cả hai mức: 4.599 và 5.784 đ/việc (simulated); chưa gồm xử lý thủ công bổ sung.

## B1 · Đổi từng yếu tố

| Kịch bản | Cách tính | CPS (đ, simulated) | Thay đổi (%, simulated) |
| --- | --- | --- | --- |
| Giá token gấp đôi | 52 và 260 đ/1.000 token; giữ giá tool | 4.723 | +5,6% |
| Giá token giảm một nửa | 13 và 65 đ/1.000 token | 4.346 | -2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 | -20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 | -25,9% |
| Lương nhân viên tăng 25% | 2.500 đ/phút | 5.506 | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Giới hạn 2 lần | 4.237 | -5,2% |
| Chỉ cho chạy 1 lần | Giới hạn 1 lần | 4.111 | -8,1% |

Giới hạn chạy: bỏ trace vượt giới hạn; yêu cầu vượt giới hạn chuyển nhân viên, phút xem lại/làm lại bằng 0.

## B2 · Đổi một cặp và xếp hạng

- Token và xem lại cùng gấp đôi: **6.543 đ/việc, +46,3%** (simulated); bằng tổng hai tác động riêng vì các khoản cộng tuyến tính, mẫu số không đổi.
- Ba yếu tố mạnh nhất theo độ lớn thay đổi trong B1 (simulated): 1. Số ca làm lại: 51,8% · 2. Tỉ lệ xem lại: 40,7% · 3. Lương nhân viên: 23,1%.

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng trợ lý (đ, simulated) | Không thành công | Cả hệ thống (đ, simulated) | CPS (đ, simulated) |
| --- | --- | --- | --- | --- |
| 1 | 3.621.781 | 319 | 7.449.781 | 4.111 |
| 2 | 4.093.220 | 234 | 6.901.220 | 4.237 |
| 3 | 4.373.585 | 222 | 7.037.585 | 4.472 |

Chi phí hệ thống = tổng trợ lý + 12.000 × số yêu cầu không thành công (gồm làm lại và chuyển nhân viên), theo quy ước B3; chưa cộng cố định.

- Giới hạn **2 lần** rẻ nhất cho công ty; CPS thấp nhất ở **1 lần** (simulated). Hai mục tiêu cho quyết định khác nhau vì chi phí xử lý thủ công nằm ngoài CPS.

## B4 · Nếu phải xem lại tất cả

Phạm vi 982 yêu cầu: 948 yêu cầu có trace ok, 48 ca làm lại, 900 việc thành công; token + tool = 224.513 đ.
Mỗi yêu cầu có trace ok được xem lại đúng một lần, 5 phút; giữ nguyên số thành công. Phút làm lại trung bình toàn mẫu = 15,30 (simulated); kịch bản bổ sung dùng 15,3 theo hướng dẫn.

| Phút làm lại/ca | Tiền xem lại (đ) | Tiền làm lại (đ) | Tổng (đ) | CPS (đ) | CPS / 12.000 | Phút xem lại hòa vốn |
| --- | --- | --- | --- | --- | --- | --- |
| 9,0 | 9.480.000 | 864.000 | 10.568.513 | 11.743 | 0,98× | 5,12 |
| 15,3 | 9.480.000 | 1.468.800 | 11.173.313 | 12.415 | 1,03× | 4,80 |

Toàn bộ giá trị tiền, tỷ số và ngưỡng hòa vốn trong bảng B4 là **simulated**; chưa cộng cố định và xử lý thủ công bổ sung.

- Xem lại 100% cho CPS **11.743 đ (0,98×)** với 9 phút làm lại; tăng lên **12.415 đ (1,03×)** với 15,3 phút (simulated), vượt 12.000 đ.
- Pilot cần đo tỷ lệ xem lại an toàn và thời gian thực tế: hòa vốn CPS ở ≤ **5,12 phút** xem lại (làm lại 9 phút), hoặc ≤ **4,80 phút** (làm lại 15,3 phút), simulated.
