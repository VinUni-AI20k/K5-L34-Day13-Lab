# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

> **Kiểm số (Lý Thành Lập):** các bảng A1–A4 dưới đây được tính độc lập, không dùng `src/lab13.py`. Đọc hai CSV với `keep_default_na=False`, rồi tính theo công thức trong `docs/du_lieu_va_cong_thuc.md`. Khi `src/lab13.py` chạy xong, đối chiếu từng số, lệch tối đa 2%.
>
> - Token = Σ(`tokens_in` ÷ 1.000 × 26 + `tokens_out` ÷ 1.000 × 130), tính trên **cả 1.624 lần chạy**, kể cả 572 lần `loi`. Tổng là 5.771.712 token vào và 734.774 token ra.
> - Tool = Σ`tool_calls` × 15 = 5.600 × 15.
> - Xem lại và làm lại = tổng số phút trong cột `_simulated` × 2.000 đ.
> - Mẫu số chỉ đếm `ket_qua == 'thanh_cong'`: 978 yêu cầu. Không chia cho 1.200.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 = (1 − 0,2²) ÷ 0,8 |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 = 1 ÷ 0,8 |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 = [(1 − 0,2³) ÷ 0,8] ÷ (1 − 0,2³) |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 | `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 (890 phút) | `phut_xem_lai_simulated` | simulated |
| Làm lại | 2.264.000 (1.132 phút) | `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | 4.373.585 | | có phần simulated |
| Số việc thành công | 978 | `ket_qua` | |
| Chi phí mỗi việc thành công | 4.472 | | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | | đo từ trace |

- Chi phí mỗi việc thành công gấp bao nhiêu lần "hoá đơn chia số yêu cầu"? ...
- Khoản nào chiếm tỉ trọng lớn nhất trong tổng chi phí, bao nhiêu phần trăm? ...

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ [simulated] | 0,22× |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ [simulated] | 0,69× |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ [simulated] | 1,88× |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ [simulated] | 0,85× |

Tỉ lệ lần chạy `ok` theo lượt chạy (đo từ trace):

| Loại | Lần 1 | Lần 2 | Lần 3 |
| --- | ---: | ---: | ---: |
| noi_dia | 91,0% (824) | 75,7% (74) | 38,9% (18) |
| hang_nang | 70,9% (158) | 39,1% (46) | 17,9% (28) |
| quoc_te | 30,0% (150) | 11,4% (105) | 2,2% (93) |
| doi_tac | 51,5% (68) | 18,2% (33) | 14,8% (27) |

Số trong ngoặc là số lần chạy ở lượt đó.

- Loại nào không đáng để trợ lý xử lý? Với loại đó, cho chạy lại tới 3 lần có giúp không? ...

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ [simulated] | 0,38× |
| Một nửa khối lượng | 16.875 | 2.370 đ | 5.784 đ [simulated] | 0,48× |

Cách tính:
- Phạm vi `noi_dia` + `hang_nang` có 900 việc thành công trong mẫu 1.200 yêu cầu.
- Việc thành công mỗi tháng = 45.000 × 900 ÷ 1.200 = 33.750.
- Chi phí cố định mỗi việc = 40.000.000 ÷ 33.750 = 1.185 đ.
- Chi phí mỗi việc thành công trong phạm vi = 3.072.513 ÷ 900 = 3.414 đ [simulated].
- Cộng hai khoản: 3.414 + 1.185 = 4.599 đ [simulated].

- Chi phí cố định có đổi kết luận không? Ở khối lượng nào? ...

## B1 · Đổi từng yếu tố

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | ... | ... |
| Giá token giảm một nửa | 13 đ và 65 đ | ... | ... |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | ... | ... |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | ... | ... |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | ... | ... |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | ... | ... |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | ... | ... |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | ... | ... |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | ... | ... |

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: ...
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. ... · 2. ... · 3. ...

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | ... | ... | ... | ... |
| 2 lần | ... | ... | ... | ... |
| 3 lần | ... | ... | ... | ... |

- Giới hạn nào rẻ nhất cho công ty? Có trùng với giới hạn cho chi phí mỗi việc thành công thấp nhất không? ...

## B4 · Nếu phải xem lại tất cả

- Chi phí mỗi việc thành công khi xem lại 100% (`noi_dia` + `hang_nang`), so với 12.000 đ: ...
- Kết quả này nói gì về thứ pilot cần học được? ...
