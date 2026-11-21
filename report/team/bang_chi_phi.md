# Bảng chi phí · Nhiệm vụ A và B

Nguồn: kết quả `src/lab13.py`, kiểm tra độc lập trong `kiem_so.md`. Dữ liệu và giá đều là giả định của lab; **simulated** đánh dấu kết quả sử dụng hoặc phụ thuộc vào phút nhân viên giả lập. Giá trị tiền đã làm tròn đến đồng, trừ khi ghi khác.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | ---: |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 — ĐẠT |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 — ĐẠT |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 — ĐẠT |

## A2 · Mô hình chi phí từ trace

| Khoản | Giá trị | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 đ | Mọi lượt trong `logix_runs.csv` | trace |
| Tool | 84.000 đ | 5.600 lượt gọi × 15 đ | trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 đ | Token và tool với `attempt` > 1; đã nằm trong hai dòng trên | trace |
| Xem lại | 1.780.000 đ | 890 phút × 2.000 đ | simulated |
| Làm lại | 2.264.000 đ | 1.132 phút × 2.000 đ | simulated |
| Tổng chi phí | 4.373.585 đ | Token + tool + xem lại + làm lại | simulated |
| Số việc thành công | 978 | `ket_qua == thanh_cong` | dữ liệu lab |
| Chi phí mỗi việc thành công | 4.472 đ | Tổng chi phí / 978 | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,65 đ | (Token + tool) / 1.200 | trace |

- Chi phí mỗi việc thành công gấp **16,28 lần [simulated]** hoá đơn token và tool mỗi yêu cầu; hai tỷ số dùng mẫu số khác nhau.
- Làm lại là khoản lớn nhất: **51,77% [simulated]** tổng chi phí.
- Theo quy ước B3 của lab, chi phí cả hệ thống là (4.373.585 + 222 × 12.000)/1.200 = **5.865 đ/yêu cầu [simulated]**, chưa cộng chi phí cố định.

## A3 · Tách theo loại yêu cầu

Chi phí mỗi việc thành công và tỉ số trong hai cột cuối đều **simulated**; so sánh với 12.000 đ chỉ nhằm đối chiếu theo đề, chưa bao gồm chi phí làm thay tất cả ca không thành công.

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ | 0,22 lần |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ | 0,69 lần |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ | 1,88 lần |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ | 0,85 lần |

- `quoc_te` có CPS 22.515 đ [simulated] và chỉ 27,3% thành công; tỉ lệ `ok` ở lần chạy 1, 2, 3 lần lượt 30,0%, 11,4%, 2,2% trên các ca có lần chạy đó, cho thấy lợi ích chạy lại giảm mạnh.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

Khối lượng dưới đây là **tổng yêu cầu toàn hệ thống**, giả định cơ cấu như mẫu; số thành công trong phạm vi = khối lượng × 900/1.200. Các chi phí và tỉ số sau là **simulated**.

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ | 0,38 lần |
| Một nửa khối lượng: 22.500 yêu cầu/tháng | 16.875 | 2.370 đ | 5.784 đ | 0,48 lần |

- Với cả hai mức, CPS cộng cố định vẫn dưới 12.000 đ [simulated]; mức cố định mỗi việc tăng gấp đôi khi lượng yêu cầu giảm một nửa. Đây chưa phải so sánh chi phí cả hệ thống.

## B1 · Đổi từng yếu tố

Mốc gốc: **4.472 đ/việc [simulated]**; toàn bộ chi phí và phần trăm thay đổi trong bảng là **simulated**.

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ/1.000 token; giá tool giữ nguyên | 4.723 đ | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ/1.000 token | 4.346 đ | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ/phút | 5.506 đ | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ `attempt > 2`; yêu cầu vượt giới hạn chuyển nhân viên | 4.237 đ | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 đ | −8,1% |

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tiền xem lại gấp đôi: **6.543 đ/việc, +46,3% [simulated]**; xấp xỉ tổng tác động +5,6% và +40,7% sau làm tròn.
- Theo các mức thay đổi đã cho, thứ tự ảnh hưởng: **1. làm lại +51,8%; 2. xem lại +40,7%; 3. lương +23,1% [simulated]**.

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

Theo quy ước bài mẫu: chi phí cả hệ thống = chi phí trợ lý + 12.000 đ × số yêu cầu không thành công. Các cột chi phí dưới đây đều **simulated**.

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ | 319 | 7.449.781 đ | 4.111 đ |
| 2 lần | 4.093.220 đ | 234 | 6.901.220 đ | 4.237 đ |
| 3 lần | 4.373.585 đ | 222 | 7.037.585 đ | 4.472 đ |

- Giới hạn **2 lần** rẻ nhất theo quy ước cả hệ thống: 6.901.220 đ; CPS thấp nhất lại là **1 lần**, 4.111 đ [simulated].
- Lưu ý: chi phí trợ lý đã gồm phút làm lại, nhưng quy ước còn cộng 12.000 đ cho mọi ca không thành công. Khi dự toán thực tế cần kiểm tra khoản làm lại có bị tính trùng không.

## B4 · Nếu phải xem lại tất cả

- Với 948 yêu cầu có ít nhất một lần `ok`, 5 phút xem lại/ca và 48 ca làm lại × 9 phút, CPS = **11.743 đ = 0,98 lần 12.000 đ [simulated]**. Nếu dùng 15,3 phút làm lại/ca, CPS = **12.415 đ = 1,03 lần [simulated]**.
- Pilot cần đo thời gian và tỉ lệ xem lại thực tế, đồng thời tìm mức giảm xem lại an toàn: ở giả định 15,3 phút, CPS vượt mốc 12.000 đ [simulated]. Hai đại lượng này có mẫu số khác nhau nên chưa kết luận tiết kiệm toàn hệ thống.
