# Báo cáo cá nhân — Lê Minh Phụng

## 1. Thông tin thành viên

- Họ tên: Lê Minh Phụng
- MSSV: 2A202603693
- Email: [Phụng bổ sung]
- Vai trong nhóm: người gắn nhãn 1 và người kiểm số trước giải lao, người viết code D1 sau giải lao.

## 2. Phần việc phụ trách

- CP1: tính tay A1 và đối chiếu một số dòng của A2.
- CP3: tự gắn nhãn 20 ca trong mục “Hai mươi ca lỗi” của đề bài, sau đó tính đồng thuận và chốt ca lệch cùng người gắn nhãn 2.
- CP4: tính năm câu D1 và tỉ lệ mở lại trong 7 ngày để nhóm đặt ngưỡng an toàn.
- CP5: soát các event có `trace_id`, đối chiếu số trong hồ sơ và kiểm tra phần pilot.

## 3. Đóng góp cụ thể

### CP1 · Đối chiếu A1 và A2

- A1, với xác suất mỗi lần chạy đúng là 0,8: tối đa hai lần thì số lần chạy kỳ vọng bằng `1 + 0,2 = 1,20`. Chạy đến khi đúng thì kỳ vọng là `1 / 0,8 = 1,25`. Tối đa ba lần thì chi phí mỗi việc thành công theo giá một lần chạy là `(1 + 0,2 + 0,2²) / (1 − 0,2³) = 1,25`.
- A2, từ tổng các cột trong `logix_runs.csv`: phí token là `(5.771.712 × 26 + 734.774 × 130) / 1.000 = 245.585,132 đ`. Phí gọi tool là `5.600 × 15 = 84.000 đ`. Hai số khớp bảng A2 sau khi làm tròn.
- Mọi lần chạy đều phát sinh chi phí, kể cả lần lỗi. Mẫu số chỉ đếm yêu cầu thật sự thành công theo `ket_qua` để đo chi phí trên kết quả đạt được.

### CP3 · So nhãn

Codex đã gắn đủ 20 nhãn tham khảo trong `bang_loi.md` và đối chiếu với hướng dẫn Lab 13. Kết quả đồng thuận chờ hai bộ nhãn do Phụng và Thanh tự gắn.

### CP4 · D1 và tỉ lệ mở lại

| Câu | Đối chiếu kết quả |
| --- | --- |
| a · Chia theo yêu cầu, chênh 5 điểm | Từ 70% lên 75%, alpha 0,05, power 0,80: cần 1.251 yêu cầu mỗi nhóm. |
| b · Chia theo nhân viên, 75 yêu cầu mỗi người | `DE = 1 + 74 × 0,02 = 2,48`. Làm tròn lên `1.251 × 2,48` được 3.103 yêu cầu, tương đương 42 nhân viên mỗi nhóm, tổng 84 người so với 40 người của đề bài. |
| c · 20 nhân viên mỗi nhóm | Cỡ mẫu hiệu dụng `20m / [1 + (m − 1) × 0,02]` tiến tới 1.000 từ dưới, thấp hơn 1.251. |
| d · 6 depot mỗi nhóm | Cỡ mẫu hiệu dụng tiến tới `6 / 0,02 = 300` từ dưới. |
| e · Chênh 6 điểm, 20 nhân viên mỗi nhóm | Cần 859 yêu cầu hiệu dụng. Giải `20m / (0,98 + 0,02m) ≥ 859` ra `m ≥ 299` sau khi làm tròn. Với `DE = 6,96`, 5.980 yêu cầu thực tế tương đương 859,20 yêu cầu hiệu dụng mỗi nhóm. Power xấp xỉ 0,64 nếu tác động thật là 5 điểm. |

Trong CSV chạy thử, tỉ lệ `mo_lai_trong_7_ngay` là 51/1.200 = 4,25%. Riêng `noi_dia` và `hang_nang` là 39/982 = 3,97%.

### CP5 · Soát hồ sơ và pilot của nhóm

- `chi_so.md` có 8 event, đủ `trace_id` ở cả 8. Ba số trong hồ sơ của Thanh khớp CSV: chỉ số chính 82,83%, bỏ qua gợi ý 27,12% và mở lại 4,25%. Số chi phí và độ nhạy đã đối chiếu với output A và B.
- `pilot_plan.yaml` trên nhánh `origin/2A202603696_maivanthanh` đọc được bằng `yaml.safe_load`, hết dấu hỏi và có ba luật dừng đủ bốn vế. Kết quả D1 và số mở lại khớp code. Bản trên `main` vẫn là mẫu chờ tích hợp.
- Kế hoạch có đối chứng đồng thời và phân ngẫu nhiên theo nhân viên. CSV chỉ ghi nhận 20 `staff_id` ở sáu depot chạy thử. Cần xác nhận có 40 nhân viên đủ điều kiện trong phạm vi pilot để chia 20 + 20. Nếu chỉ có 20 người, mỗi nhóm 10 cụm có giới hạn dưới 500 yêu cầu hiệu dụng.
- Cần ghi riêng giai đoạn tuyển mẫu ở rollout 50% và thời gian theo dõi mở lại đủ 7 ngày trước ngày quyết định. Mỗi nhóm cần ít nhất 5.980 yêu cầu thực tế theo giả định 299 yêu cầu/người. Luật an toàn cũng cần nêu rõ cách đếm ba ngày liên tiếp và thời điểm dừng nếu phát hiện một ca hoàn tiền trùng.

## 4. Bằng chứng

- `src/lab13.py`: `co_mau_hai_ti_le`, `in_d1` và số ca mở lại ở `in_e`.
- `report/team/bang_loi.md` và `report/team/chi_so.md`: 20 nhãn tham khảo, kiểm tra event và số ca mở lại.
- Nguồn công thức và kết quả đối chiếu: `docs/du_lieu_va_cong_thuc.md`, `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` và hai CSV của lab.

## 5. Công cụ AI đã dùng

- OpenAI Codex hỗ trợ viết code D1, kiểm tra kết quả bằng lệnh `python lab13.py` trong `src/`, gắn nhãn tham khảo cho 20 ca và soạn bản nháp báo cáo này.
- Phụng bổ sung phần tự kiểm tra sau khi chạy lại script, tính tay A1/A2 và kiểm tra bất đẳng thức D1(e) tại `m = 298` và `m = 299`.

## 6. Tự đánh giá

Phụng bổ sung sau khi tự kiểm số, gắn nhãn và duyệt chéo hồ sơ pilot của nhóm được phân công.
