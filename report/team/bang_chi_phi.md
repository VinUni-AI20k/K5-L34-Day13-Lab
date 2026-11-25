# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 đ | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 đ | 5.600 lượt gọi × 15 đ/lượt | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 đ | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 đ | 890 phút xem lại × 2.000 đ/phút | simulated |
| Làm lại | 2.264.000 đ | 1.132 phút làm lại × 2.000 đ/phút | simulated |
| Tổng chi phí | 4.373.585 đ | | có phần simulated |
| Số việc thành công | 978 | `ket_qua` | |
| Chi phí mỗi việc thành công | 4.472 đ | 4.373.585,132 đ ÷ 978 việc thành công | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 đ | (245.585,132 + 84.000) đ ÷ 1.200 yêu cầu | đo từ trace |

**Đối chiếu CP1.** Cả ba phép thử A1 đều đạt khi chạy `lab13.py`. Cả 9 dòng A2 khớp với phép tính độc lập từ CSV sau khi làm tròn. Chi phí token và tool tính trên cả 1.624 lần chạy, kể cả lần lỗi. Khoản 93.804 đ của lần chạy lại đã nằm trong hai khoản này.

- Chi phí mỗi việc thành công khoảng **16,3 lần** hoá đơn token và tool chia cho số yêu cầu (4.472 ÷ 274,7). Số CPS có phần chi phí `simulated`.
- **Làm lại** chiếm phần lớn nhất: khoảng **51,8%** tổng chi phí (2.264.000 ÷ 4.373.585); số phút làm lại là `simulated`.

## A3 · Tách theo loại yêu cầu

Đối chiếu với [bảng A3 của Thành viên 3](tv3_ban_giao.md). Bốn loại cộng lại đủ 1.200 yêu cầu và 978 việc thành công, khớp mẫu số tính chi phí mỗi việc thành công ở A2.

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công (`simulated`) | So với 12.000 đ (`simulated`) |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 783/824 = 95,0% | 1,11 | 2.696 đ | 0,22× |
| hang_nang | 158 | 117/158 = 74,1% | 1,47 | 8.221 đ | 0,69× |
| quoc_te | 150 | 41/150 = 27,3% | 2,32 | 22.515 đ | 1,88× |
| doi_tac | 68 | 37/68 = 54,4% | 1,88 | 10.215 đ | 0,85× |

- Nên giao yêu cầu quốc tế cho nhân viên vì mỗi việc thành công tốn 22.515 đ (`simulated`), cao hơn mức 12.000 đ. Chạy lại giúp được ít ca. Tỉ lệ lần chạy có trạng thái `ok` giảm từ 45/150 (30,0%) ở lần đầu xuống 12/105 (11,4%) ở lần hai và 2/93 (2,2%) ở lần ba.
- Chọn `noi_dia` và `hang_nang` cho pilot (982/1.200 yêu cầu). Đề xuất để `doi_tac` ngoài đợt đầu vì nhóm này có điều khoản riêng, chỉ 37/68 yêu cầu thành công và chi phí đã bằng 0,85 lần mức nhân viên tự làm (`simulated`).

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

Hai kịch bản dưới đây đã được đối chiếu với [phép tính A4 của Thành viên 4](../../src/tv4_tinh_so.py).

Trong 1.200 yêu cầu, có 900 việc thành công thuộc hai loại này. Giữ nguyên cơ cấu yêu cầu và tỉ lệ thành công, số việc thành công trong phạm vi mỗi tháng bằng tổng lượng yêu cầu × 900/1.200. Phân bổ 40 triệu đ/tháng cho các việc này rồi cộng với chi phí biến đổi 3.414 đ/việc (`simulated`).

| Tổng yêu cầu/tháng | Việc thành công trong phạm vi/tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công gồm cố định (`simulated`) | So với 12.000 đ (`simulated`) |
| --- | ---: | ---: | ---: | ---: |
| 45.000 | 33.750 | 1.185 đ | 4.599 đ | 0,38× |
| 22.500 | 16.875 | 2.370 đ | 5.784 đ | 0,48× |

- Ở cả hai khối lượng, chi phí mỗi việc thành công vẫn dưới 12.000 đ. Với cùng cơ cấu yêu cầu, điểm hòa vốn là khoảng 6.212 yêu cầu/tháng (`simulated`), theo phép tính 40.000.000 ÷ [(12.000 − 3.413,90) × 900/1.200]. Dưới ngưỡng này, nhân viên tự làm rẻ hơn.

## B1 · Đổi từng yếu tố

Mốc so sánh là 4.471,9684 đ/việc thành công ở A2 (`simulated`). Phần trăm thay đổi được tính trước khi làm tròn số tiền.

| Kịch bản | Tham số thay đổi | Chi phí mỗi việc thành công (`simulated`) | Thay đổi so với A2 (`simulated`) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ đầu vào và 260 đ đầu ra cho 1.000 token | 4.723 đ | +5,6% |
| Giá token giảm một nửa | 13 đ đầu vào và 65 đ đầu ra cho 1.000 token | 4.346 đ | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ/phút | 5.506 đ | +23,1% |
| Tối đa 2 lần chạy | Chuyển yêu cầu cần lần thứ 3 cho nhân viên | 4.237 đ | −5,2% |
| Tối đa 1 lần chạy | Chuyển yêu cầu cần lần thứ 2 cho nhân viên | 4.111 đ | −8,1% |

## B2 · Đổi một cặp và xếp hạng

- Khi giá token và tỉ lệ xem lại cùng gấp đôi, chi phí là **6.543 đ/việc** (+46,3%, `simulated`). Hai khoản tăng độc lập và cùng chia cho 978 việc thành công, nên mức tăng bằng 5,6% + 40,7%.
- Theo mức tăng chi phí trong các kịch bản B1 (`simulated`), số ca làm lại gấp đôi đứng đầu (+51,8%), tiếp theo là tỉ lệ xem lại gấp đôi (+40,7%) và lương nhân viên tăng 25% (+23,1%).

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

Chi phí cả hệ thống bằng tổng chi phí trợ lý cộng 12.000 đ cho mỗi yêu cầu nhân viên phải xử lý tiếp. Kết quả khớp với [bảng B3 của Thành viên 3](tv3_ban_giao.md).

| Giới hạn | Tổng chi phí trợ lý (`simulated`) | Số yêu cầu không thành công | Chi phí cả hệ thống (`simulated`) | Chi phí mỗi việc thành công (`simulated`) |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ | 319 | 7.449.781 đ | 4.111 đ |
| 2 lần | 4.093.220 đ | 234 | 6.901.220 đ | 4.237 đ |
| 3 lần | 4.373.585 đ | 222 | 7.037.585 đ | 4.472 đ |

- **2 lần chạy** cho tổng chi phí thấp nhất, 6.901.220 đ (`simulated`). Giới hạn 1 lần cho chi phí mỗi việc thành công thấp nhất, 4.111 đ (`simulated`), nhưng chuyển thêm 85 yêu cầu cho nhân viên so với giới hạn 2 lần.

## B4 · Nếu phải xem lại tất cả

Trong 982 yêu cầu nội địa và hàng nặng, 948 yêu cầu có ít nhất một lần chạy `ok` để xem lại, 48 ca phải làm lại và 900 việc thành công. Hóa đơn token và tool là 224.513 đ. Mỗi kịch bản tính 5 phút xem lại cho cả 948 yêu cầu, với đơn giá 2.000 đ/phút.

| Thời gian làm lại mỗi ca | Chi phí mỗi việc thành công, chưa cộng cố định (`simulated`) | So với 12.000 đ (`simulated`) |
| --- | ---: | ---: |
| 9 phút theo giả định của đề | 11.743 đ | 0,98× |
| 15,3 phút theo trung bình toàn mẫu, làm tròn một chữ số (`simulated`) | 12.415 đ | 1,03× |

- Pilot cần đo thời gian xem lại thực tế và tỉ lệ mở lại sau 7 ngày khi giảm dần số ca phải xem. Nếu vẫn xem lại 100%, thời gian hòa vốn mỗi lượt là khoảng 5,1 phút khi làm lại mất 9 phút/ca, hoặc 4,8 phút khi làm lại mất 15,3 phút/ca (`simulated`).
