# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 (ĐẠT) |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 (ĐẠT) |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 (ĐẠT) |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585,1 | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 | `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804,5 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated` | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | 4.373.585,1 | Token + tool + xem lại + làm lại | simulated |
| Số việc thành công | 978 việc | `ket_qua` | đếm theo yêu cầu |
| Chi phí mỗi việc thành công | 4.472 đ/việc thành công | Tổng chi phí chia cho số việc thành công | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 đ/yêu cầu | Token + tool, chia cho 1.200 yêu cầu | đo từ trace |

- Chi phí mỗi việc thành công gấp **16,3× `simulated`** hoá đơn token và tool tính trên mỗi yêu cầu.
- Chi phí làm lại chiếm tỉ trọng lớn nhất, **51,8% `simulated`** tổng chi phí.

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công (`simulated`) | So với 12.000 đ (`simulated`) |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ | 0,22× |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ | 0,69× |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ | 1,88× |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ | 0,85× |

- Nên loại `quoc_te` khỏi phạm vi pilot vì tỉ lệ thành công chỉ **27,3%** và chi phí là **22.515 đ/việc thành công**, bằng **1,88× `simulated`** mốc 12.000 đ. Tỉ lệ `ok` ở lượt 1, 2 và 3 lần lượt là **30,0%, 11,4% và 2,2%**, nên lượt thứ ba đem lại ít kết quả `ok` trong mẫu.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

Ở quy mô toàn công ty, 45.000 yêu cầu/tháng × 900/1.200 = **33.750 việc thành công/tháng** thuộc phạm vi `noi_dia` và `hang_nang`. Chi phí cố định **40 triệu đ/tháng** được chia theo số việc thành công rồi cộng vào CPS trước cố định là **3.414 đ/việc `simulated`**.

| Khối lượng toàn công ty | Việc thành công mỗi tháng trong phạm vi | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định (`simulated`) | So với 12.000 đ (`simulated`) |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ | 0,38× |
| 22.500 yêu cầu/tháng (một nửa khối lượng) | 16.875 | 2.370 đ | 5.784 đ | 0,48× |

- Chi phí mỗi việc thành công sau khi cộng cố định vẫn dưới **12.000 đ** ở cả hai mức khối lượng (`simulated`). Khi khối lượng giảm một nửa, phần cố định mỗi việc tăng gấp đôi, từ **1.185 đ** lên **2.370 đ**.

## B1 · Đổi từng yếu tố

Chi phí gốc là **4.472 đ/việc thành công `simulated`**. Hai cột kết quả trong bảng đều là `simulated`.

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 đ | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 đ | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 đ | −8,1% |

## B2 · Đổi một cặp và xếp hạng

- Khi giá token và tỉ lệ xem lại cùng gấp đôi, chi phí là **6.543 đ/việc thành công**, tăng **46,3% `simulated`**.
- Ba yếu tố có tác động mạnh nhất lần lượt là **làm lại (+51,8%)**, **xem lại (+40,7%)** và **lương (+23,1%)** theo các kịch bản tăng ở B1. Các mức thay đổi đều là `simulated`.

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý (`simulated`) | Số yêu cầu không thành công | Chi phí cả hệ thống (`simulated`) | Chi phí mỗi việc thành công (`simulated`) |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ | 319 | 7.449.781 đ | 4.111 đ |
| 2 lần | 4.093.220 đ | 234 | 6.901.220 đ | 4.237 đ |
| 3 lần | 4.373.585 đ | 222 | 7.037.585 đ | 4.472 đ |

- Giới hạn **2 lần** cho chi phí cả hệ thống thấp nhất, **6.901.220 đ `simulated`**. Giới hạn **1 lần** cho chi phí mỗi việc thành công thấp nhất, **4.111 đ `simulated`**, với **319** yêu cầu không thành công so với **234** ở giới hạn 2 lần.

## B4 · Nếu phải xem lại tất cả

- Khi xem lại 100% trong phạm vi `noi_dia` và `hang_nang`, chi phí là **11.743 đ/việc (0,98× mốc 12.000 đ)** với 9 phút làm lại mỗi ca, và **12.415 đ/việc (1,03×)** với khoảng 15,3 phút làm lại mỗi ca. Các chi phí, tỉ số và giả định 15,3 phút từ dữ liệu đều mang nhãn `simulated`.
- Pilot cần đo phút xem lại, phút làm lại và mức có thể giảm tỉ lệ xem lại mà vẫn đạt yêu cầu an toàn. Thời gian xem lại hoà vốn lần lượt khoảng **5,1 phút** và **4,8 phút/ca `simulated`** theo hai giả định làm lại.
