# Bảng chi phí · Nhiệm vụ A và B

Nguồn số: chạy `src/lab13.py` trên hai CSV được phát; toàn bộ dữ liệu lab là giả lập. Mọi tổng, tỉ lệ hoặc kết luận có sử dụng phút `_simulated` được ghi nhãn **simulated**. Các bảng A2–B3 chưa cộng chi phí cố định, trừ A4.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 |

Giả định mỗi lần chạy đúng độc lập với xác suất p: E = (1 − (1 − p)^k)/p; P(thành công) = 1 − (1 − p)^k; E/P = 1/p = 1,25 với p = 0,8. Khi chạy đến khi đúng, E = 1/p và P = 1.

## A2 · Mô hình chi phí từ trace

| Khoản | Giá trị (đ, trừ số việc) | Cách tính | Nhãn |
| --- | --- | --- | --- |
| Token | 245.585 | tokens_in / 1.000 × 26 + tokens_out / 1.000 × 130 | đo từ trace |
| Tool | 84.000 | tool_calls × 15 | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | token + tool của attempt > 1; đã nằm trong hai dòng trên | đo từ trace |
| Xem lại | 1.780.000 | phut_xem_lai_simulated × 2.000 | simulated |
| Làm lại | 2.264.000 | phut_lam_lai_simulated × 2.000 | simulated |
| Tổng chi phí | 4.373.585 | token + tool + xem lại + làm lại | simulated |
| Số việc thành công (việc) | 978 | ket_qua == 'thanh_cong' | đếm từ dữ liệu |
| Chi phí mỗi việc thành công | 4.472 | tổng / số việc thành công | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | hoá đơn / số yêu cầu | đo từ trace |

- Tử số tính mọi lần chạy kể cả lỗi vì vẫn phát sinh tiền; mẫu số chỉ đếm 978 việc thành công. Chi phí mỗi việc thành công gấp **16,3 lần** hoá đơn chia số yêu cầu [simulated].
- Khoản lớn nhất là làm lại: **51,8%**; tổng tiền nhân viên chiếm **92,5%** [simulated].

So sánh cùng khối lượng: (4.373.585 + 222 × 12.000) / 1200 = **5.865 đ/yêu cầu**, bằng 0,49× nhân viên tự làm [simulated]; áp dụng quy ước B3 cho mọi yêu cầu không thành công.

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công [simulated] | So với 12.000 đ [simulated] |
| --- | --- | --- | --- | --- | --- |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 | 0,22× |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 | 0,69× |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 | 1,88× |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 | 0,85× |

- Quốc tế không đáng đưa vào pilot: 22.515 đ/việc thành công = 1,88× mốc 12.000 đ [simulated].
- Tỉ lệ run `ok` ở lần 1/2/3 của quốc tế là 30,0% / 11,4% / 2,2%; chạy lại không khắc phục tốt lỗi lặp. Đây là tỉ lệ theo run, khác thành công cuối của yêu cầu.
- Đề xuất phạm vi noi_dia + hang_nang; doi_tac cần đánh giá riêng điều khoản, dù chi phí mỗi việc thành công còn dưới 12.000 đ [simulated].

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng toàn công ty | Việc thành công trong phạm vi/tháng | Cố định mỗi việc (đ) | Chi phí mỗi việc thành công + cố định (đ) [simulated] | So với 12.000 đ [simulated] |
| --- | --- | --- | --- | --- |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 | 4.599 | 0,38× |
| 22.500 yêu cầu/tháng | 16.875 | 2.370 | 5.784 | 0,48× |

- Giữ cơ cấu mẫu: việc thành công trong phạm vi/tháng = khối lượng toàn công ty × 900/1200; chi phí biến đổi = 3.072.513 / 900 = 3.414 đ [simulated].
- Cố định 40.000.000 đ/tháng chưa đảo kết luận ở 45.000 hoặc 22.500 yêu cầu/tháng; điểm hoà vốn theo chi phí/việc thành công khoảng 6.212 yêu cầu toàn công ty/tháng [simulated].
- Cột so với 12.000 đ chỉ so chi phí/việc thành công; khi đánh giá tiết kiệm toàn công ty phải cộng phần nhân viên xử lý như B3.

## B1 · Đổi từng yếu tố

| Kịch bản | Cách tính | Chi phí mỗi việc thành công (đ) [simulated] | Thay đổi [simulated] |
| --- | --- | --- | --- |
| Giá token gấp đôi | 52 đ vào; 260 đ ra / 1.000 token; tool giữ nguyên | 4.723 | +5,6% |
| Giá token giảm một nửa | 13 đ vào; 65 đ ra / 1.000 token | 4.346 | -2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 | -20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 | -25,9% |
| Lương nhân viên tăng 25% | 2.500 đ/phút | 5.506 | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ attempt > 2; yêu cầu vượt giới hạn chuyển nhân viên, phút simulated = 0 | 4.237 | -5,2% |
| Chỉ cho chạy 1 lần | Bỏ attempt > 1; yêu cầu vượt giới hạn chuyển nhân viên, phút simulated = 0 | 4.111 | -8,1% |

## B2 · Đổi một cặp và xếp hạng

- Token và xem lại cùng gấp đôi: **6.543 đ**, tăng **46,3%** [simulated]; bằng tổng hai tác động riêng vì số việc thành công giữ nguyên và mô hình cộng tuyến tính.
- Theo các mức biến động B1: **1. Làm lại (+51,8%) · 2. Xem lại (+40,7%) · 3. Lương (+23,1%)** [simulated].

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý (đ) [simulated] | Số yêu cầu không thành công | Chi phí cả hệ thống (đ) [simulated] | Chi phí mỗi việc thành công (đ) [simulated] |
| --- | --- | --- | --- | --- |
| 1 lần | 3.621.781 | 319 | 7.449.781 | 4.111 |
| 2 lần | 4.093.220 | 234 | 6.901.220 | 4.237 |
| 3 lần | 4.373.585 | 222 | 7.037.585 | 4.472 |

- Cả hệ thống = tổng trợ lý + (số yêu cầu − số thành công) × 12.000 đ, theo quy ước B3.
- **2 lần** rẻ nhất cho công ty (6.901.220 đ); **1 lần** có chi phí/việc thành công thấp nhất nhưng đẩy thêm 85 yêu cầu sang nhân viên [simulated].

## B4 · Nếu phải xem lại tất cả (noi_dia + hang_nang)

| Kịch bản | Phút làm lại/ca [simulated] | Tổng chi phí (đ) [simulated] | Chi phí/việc thành công (đ) [simulated] | So với 12.000 đ [simulated] | Phút xem lại tối đa để hoà vốn [simulated] |
| --- | --- | --- | --- | --- | --- |
| Giả định đề bài: 9 phút/ca | 9,0000 | 10.568.513 | 11.743 | 0,98× | 5,12 |
| Theo trung bình CSV chính xác | 15,2973 | 11.173.054 | 12.415 | 1,03× | 4,80 |
| Trung bình làm tròn 1 chữ số (đối chiếu hướng dẫn) | 15,3000 | 11.173.313 | 12.415 | 1,03× | 4,80 |

- Phạm vi 982 yêu cầu, 900 thành công; 948 yêu cầu có ≥1 run `ok`, mỗi yêu cầu xem lại 5 phút; 48 ca làm lại; token + tool = 224.513 đ.
- Công thức: (token + tool + 948 × 5 × 2.000 + 48 × phút làm lại × 2.000) / 900; phút trung bình/trung vị của toàn bộ ca làm lại = 15,2973/14,5 [simulated].
- Xem lại 100% gần hoặc vượt mốc 12.000 đ/việc thành công [simulated]; pilot cần đo thời gian thực và mức xem lại có thể giảm an toàn. B4 chưa cộng cố định và phần nhân viên làm thay.

## Nguồn phương pháp và bàn giao

- Công thức, quy tắc cắt lần chạy và giả định B4: `docs/du_lieu_va_cong_thuc.md`, `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (A–B).
- Người phụ trách chỉ số và hồ sơ cuối lấy kết quả từ các bảng trên, giữ nguyên nhãn simulated và phạm vi.
- Phần tính cỡ mẫu D1 do người phụ trách D bổ sung vào `src/lab13.py`.
