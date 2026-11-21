# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

Đã đối chiếu với bảng đáp án trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`: mọi số A2, A3, A4, B1–B4 lệch 0% (ngưỡng cho phép 2%).

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 (ĐẠT) |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 (ĐẠT) |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 (ĐẠT) |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 (5.600 lần gọi) | `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 (890 phút) | `phut_xem_lai_simulated` | simulated |
| Làm lại | 2.264.000 (1.132 phút) | `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | 4.373.585 | | simulated |
| Số việc thành công | 978 | `ket_qua` | |
| Chi phí mỗi việc thành công | 4.472 | | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | | đo từ trace |

- Chi phí mỗi việc thành công (4.472 đ) gấp **16,3 lần** hoá đơn chia số yêu cầu (274,7 đ) [simulated].
- Khoản lớn nhất là **làm lại, 51,8%** tổng chi phí, kế đến là xem lại 40,7%. Giờ nhân viên chiếm 92,5% [simulated].
- So công bằng với 12.000 đ (cộng 222 ca không thành công × 12.000 đ): 5.865 đ/yêu cầu, bằng **0,49×** [simulated].

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công [simulated] | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ | 0,22× |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ | 0,69× |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ | 1,88× |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ | 0,85× |

- **quoc_te** không đáng để trợ lý xử lý: 22.515 đ = 1,88× của 12.000 đ [simulated], chỉ 27,3% thành công.
- Chạy lại tới 3 lần không giúp: tỉ lệ ok của quoc_te giảm từ 30,0% (lần 1) xuống 11,4% (lần 2) và 2,2% (lần 3). Lỗi lặp lại trên cùng yêu cầu.
- doi_tac sát ngưỡng (0,85×) và có điều khoản riêng, nên cũng để ngoài phạm vi pilot.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

Trong phạm vi có 900 việc thành công trên 1.200 yêu cầu của mẫu (75%). Tổng chi phí là 3.072.513 đ, tức chi phí biến đổi 3.414 đ cho mỗi việc thành công [simulated].

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định [simulated] | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ | 0,38× |
| Một nửa khối lượng (22.500) | 16.875 | 2.370 đ | 5.784 đ | 0,48× |

- Ở 45.000 yêu cầu/tháng, chi phí cố định không đổi kết luận (0,38×). Khi khối lượng giảm một nửa, như giai đoạn pilot, phần cố định tăng gấp đôi lên 2.370 đ/việc (0,48×) [simulated]. Hồ sơ phải ghi rõ con số đã cộng cố định hay chưa, và ở khối lượng nào.

## B1 · Đổi từng yếu tố

Gốc (A2): 4.472 đ [simulated].

| Kịch bản | Cách tính | Chi phí mỗi việc thành công [simulated] | Thay đổi (%) |
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

Tự kiểm tính tuyến tính: mỗi kịch bản "giảm một nửa" giảm đúng bằng nửa mức tăng của kịch bản "gấp đôi" (token 5,6 → 2,8; xem lại 40,7 → 20,3; làm lại 51,8 → 25,9). Đúng.

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: **6.543 đ (+46,3%)** [simulated]. Con số này đúng bằng tổng hai tác động riêng (+5,6% và +40,7%), chênh 0 đ, vì mô hình cộng tuyến tính.
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. **Số ca làm lại** (+51,8%) · 2. **Tỉ lệ xem lại** (+40,7%) · 3. **Lương nhân viên** (+23,1%) [simulated]. Giá token gấp đôi chỉ làm tăng 5,6%.

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

Chi phí cả hệ thống = tổng chi phí trợ lý + 12.000 đ × số yêu cầu không thành công, vì nhân viên phải làm thay.

| Giới hạn | Tổng chi phí trợ lý [simulated] | Số yêu cầu không thành công | Chi phí cả hệ thống [simulated] | Chi phí mỗi việc thành công [simulated] |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ | 319 | 7.449.781 đ | 4.111 đ (thấp nhất) |
| 2 lần | 4.093.220 đ | 234 | **6.901.220 đ (rẻ nhất)** | 4.237 đ |
| 3 lần | 4.373.585 đ | 222 | 7.037.585 đ | 4.472 đ |

- Giới hạn **2 lần** rẻ nhất cho công ty: 6.901.220 đ, rẻ hơn 136.365 đ so với 3 lần [simulated]. Giới hạn này **không trùng** với giới hạn cho chi phí mỗi việc thành công thấp nhất (1 lần, 4.111 đ).
- Chọn 1 lần để tối ưu chi phí mỗi việc thành công sẽ đẩy thêm 85 việc sang nhân viên (319 so với 234), làm chi phí cả hệ thống tăng 548.561 đ so với 2 lần [simulated].

## B4 · Nếu phải xem lại tất cả

Phạm vi `noi_dia` + `hang_nang` gồm 982 yêu cầu. Có 948 yêu cầu có ít nhất một lần chạy ok, xem lại 5 phút mỗi yêu cầu (9.480.000 đ) [simulated]. Có 48 ca làm lại. Token và tool là 224.513 đ (đo từ trace). Có 900 việc thành công.

- Xem lại 100%, giả định đề 9 phút/ca làm lại: tổng 10.568.513 đ, tức **11.743 đ mỗi việc thành công = 0,98× của 12.000 đ** [simulated]. Nếu dùng phút làm lại thực tế trong dữ liệu (trung bình 15,3 phút/ca) thì ra 12.415 đ = **1,03×**, đắt hơn nhân viên tự làm [simulated].
- Xem lại 100% thì trợ lý gần như không tiết kiệm được gì, vì tiền xem lại chiếm khoảng 90% chi phí. Mức hoà vốn là mỗi lần xem lại ≤ 5,1 phút (≤ 4,8 phút nếu tính 15,3 phút làm lại) [simulated].
- Pilot cần học được hai điều: tỉ lệ xem lại có thể giảm an toàn từ 100% xuống mức nào, và mỗi lần xem lại có rút từ 5 phút xuống dưới mức hoà vốn 5,1 phút được không [simulated].
