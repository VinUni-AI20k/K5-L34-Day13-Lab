# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py` (chạy `cd src && python lab13.py`). Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

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
| Tool (5.600 lần gọi) | 84.000 | `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | đo từ trace |
| Xem lại (890 phút) | 1.780.000 | `phut_xem_lai_simulated` | simulated |
| Làm lại (1.132 phút) | 2.264.000 | `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | 4.373.585 | | có phần simulated |
| Số việc thành công | 978 | `ket_qua` | |
| Chi phí mỗi việc thành công | 4.472 | | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | | đo từ trace |

- Chi phí mỗi việc thành công gấp bao nhiêu lần "hoá đơn chia số yêu cầu"? 4.472 / 274,7 = **16,3 lần** [simulated]. Tử số tính mọi lần chạy (kể cả lần lỗi, vì lần lỗi vẫn tốn token và giờ làm lại), mẫu số chỉ đếm 978 yêu cầu thành công.
- Khoản nào chiếm tỉ trọng lớn nhất? **Làm lại 51,8%** [simulated], rồi xem lại 40,7% [simulated]; giờ nhân viên cộng lại 92,5%, token + tool chỉ 7,5%.
- So với nhân viên tự làm: 4.472 đ chưa tính 148 ca `chuyen_nhan_vien` mà nhân viên làm thay. Chi phí cả hệ thống = (4.373.585 + 222 × 12.000) / 1.200 = **5.865 đ/yêu cầu = 0,49×** của 12.000 đ [simulated].

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công [simulated] | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 | 0,22× |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 | 0,69× |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 | 1,88× |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 | 0,85× |

- Loại nào không đáng để trợ lý xử lý? **quoc_te**: 1,88× (đắt hơn nhân viên) và chỉ thành công 27,3% [simulated]. Chạy lại không giúp: tỉ lệ `ok` theo lần thử là 30,0% → 11,4% → 2,2% (đo từ trace), lỗi lặp lại trên cùng yêu cầu nên chỉ tốn thêm tiền.
- `doi_tac` sát ngưỡng (0,85×, thành công 54,4%) và có điều khoản riêng, cũng nên loại khỏi phạm vi pilot.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc (đ) | Chi phí mỗi việc thành công + cố định (đ) | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 | 4.599 | 0,38× |
| Một nửa khối lượng | 16.875 | 2.370 | 5.784 | 0,48× |

- Chi phí cố định có đổi kết luận không? Không: ở cả hai khối lượng vẫn dưới 0,5× [simulated]. Nhưng nó tăng gấp đôi khi khối lượng giảm một nửa (1.185 → 2.370 đ/việc), nên hồ sơ phải nói rõ con số đã cộng cố định ở khối lượng nào. Chi phí mỗi việc phạm vi (chưa cố định): 3.414 đ = 3.072.513 / 900.

## B1 · Đổi từng yếu tố

| Kịch bản | Cách tính | Chi phí mỗi việc thành công [simulated] | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 | −8,1% |

Gốc (A2): 4.472 đ. Tự kiểm tra: mỗi kịch bản "giảm một nửa" bằng đúng nửa mức tăng của "gấp đôi" (5,6 → 2,8; 40,7 → 20,3; 51,8 → 25,9) vì mô hình cộng tuyến tính.

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: **6.543 đ (+46,3%)** [simulated] = 5,6% + 40,7%, đúng bằng tổng hai tác động riêng.
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. số ca làm lại (±51,8%) · 2. tỉ lệ xem lại (±40,7%) · 3. lương nhân viên (+23,1%). Giá token chỉ +5,6%.

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

Chi phí cả hệ thống = tổng chi phí trợ lý + 12.000 đ × số yêu cầu không thành công (nhân viên làm thay).

| Giới hạn | Tổng chi phí trợ lý [simulated] | Số yêu cầu không thành công | Chi phí cả hệ thống [simulated] | Chi phí mỗi việc thành công [simulated] |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 | 319 | 7.449.781 | 4.111 (thấp nhất) |
| 2 lần | 4.093.220 | 234 | **6.901.220 (rẻ nhất)** | 4.237 |
| 3 lần | 4.373.585 | 222 | 7.037.585 | 4.472 |

- Giới hạn **2 lần** rẻ nhất cho công ty (6.901.220 đ). Không trùng với giới hạn cho chi phí mỗi việc thành công thấp nhất (1 lần, 4.111 đ): tối ưu riêng chỉ số này đẩy thêm 85 việc (319 − 234) sang nhân viên.

## B4 · Nếu phải xem lại tất cả (noi_dia + hang_nang, 982 yêu cầu)

- Xem lại 100%: 948 yêu cầu có ít nhất một lần `ok` × 5 phút + 48 ca làm lại × 9 phút (đề bài) + token/tool 224.513 đ = 10.568.513 đ; chia 900 việc thành công = **11.743 đ = 0,98×** của 12.000 đ [simulated].
- Độ nhạy theo phút làm lại: dữ liệu cho trung bình 16,2 phút/ca làm lại trong phạm vi này (thay cho 9) → **12.516 đ = 1,04×** [simulated], tức đắt hơn nhân viên tự làm. Hoà vốn: mỗi lần xem lại phải ≤ 5,1 phút (9 phút làm lại) hoặc ≤ 4,8 phút (16,2 phút).
- Pilot cần học được: tỉ lệ xem lại có thể giảm an toàn xuống mức nào (hiện 14,8% yêu cầu được xem lại, 13,0% trong phạm vi) và mỗi lần xem lại có xuống dưới 5 phút được không, vì tiền xem lại chiếm ~90% chi phí khi xem 100%.
