# Phân chia công việc Lab 13 cho nhóm 4 người

Bản phân công này bao phủ nhiệm vụ A–E, duyệt chéo Gate 2a và toàn bộ hồ sơ nộp của nhóm 4thangtay, lớp L3B. Mỗi phần có người chủ trì, người kiểm tra và đầu ra cụ thể.

Chưa có danh sách đầy đủ họ tên và MSSV nên dùng Người 1–4. Nhóm tự gán tên vào các vai và cập nhật [TEAM.md](../TEAM.md) trước khi bắt đầu; thứ tự dưới đây không mặc định tương ứng thứ tự thành viên.

## 1. Tổng quan trách nhiệm

| Thành viên | Vai đầu buổi | Phần chủ trì | Phần phối hợp |
| --- | --- | --- | --- |
| Người 1 | Người viết code | A1–A4, mô hình chi phí | Kiểm B, D1 và số kinh tế; chạy lại trên máy khác |
| Người 2 | Người kiểm số | B1–B4, code D1 và tính ba chỉ số E1 | Kiểm A; nhận vai viết code sau giải lao |
| Người 3 | Người gắn nhãn 1 | C, D2, E1–E2 | Soát điều kiện hoàn thành, chỉ số và event |
| Người 4 | Người gắn nhãn 2 kiêm giữ hồ sơ | D3, E3, tổng hợp và nộp bài | C, điều phối duyệt chéo, ghi phiếu chấm |

**Bắt buộc đổi người viết code sau giải lao:** Người 1 bàn giao cho Người 2. Cả hai phải tự tay tính và giải thích được chi phí. Người 3 và Người 4 gắn nhãn độc lập cả 20 ca, không chia mỗi người 10 ca.

## 2. Công việc cụ thể của từng người

### Người 1 — Mô hình chi phí và kiểm tra kỹ thuật

- Chuẩn bị môi trường Python 3.10 trở lên; nhóm có ít nhất hai máy chạy được bài.
- Viết A1 trong [src/lab13.py](../src/lab13.py): ba hàm và ba phép thử phải đạt 1,20 · 1,25 · 1,25 trước khi làm tiếp.
- Viết hàm mô hình A2 có tham số để tái sử dụng cho B. Cộng token và tool của mọi lần chạy, kể cả lần lỗi; mẫu số chỉ đếm yêu cầu thành công. Phần chạy lại là khoản “trong đó”, không cộng lần thứ hai vào tổng.
- Làm A3 cho đủ bốn loại yêu cầu: số yêu cầu, tỉ lệ thành công, số lần chạy, chi phí và so sánh baseline 12.000 đồng. Kiểm tỉ lệ thành công theo lần thử để giải thích việc chạy lại.
- Làm A4: cộng chi phí cố định 40 triệu đồng/tháng trong phạm vi nội địa và hàng nặng, xét khối lượng đầy đủ và một nửa.
- Gửi output và cách tính cho Người 2 điền bảng; gửi kết luận phạm vi cho Người 4 cập nhật hồ sơ.
- Sau giải lao chuyển quyền sửa code cho Người 2; kiểm B3, B4 và D1, tránh hai người sửa cùng file đồng thời.
- Cuối buổi chạy bản chốt trên máy khác với máy phát triển chính; bảo vệ phần mô hình chi phí.

**Bàn giao:** code A1–A4; số liệu và giải thích cho phần A trong bảng chi phí. Người 2 kiểm tra độc lập.

### Người 2 — Kiểm số, độ nhạy và cỡ mẫu

- Trong A, tính tay ít nhất một con số để đối chiếu code; ghi cách tính và kiểm các bảng A.
- Chủ trì B1: đủ chín kịch bản, mỗi dòng chỉ đổi một yếu tố, có chi phí và phần trăm thay đổi.
- Làm B2: đổi đồng thời một cặp yếu tố và xếp hạng ba yếu tố ảnh hưởng mạnh nhất.
- Làm B3: so giới hạn 1, 2, 3 lần chạy; tính chi phí cả hệ thống bằng chi phí trợ lý cộng 12.000 đồng cho mỗi yêu cầu không thành công.
- Làm B4: xem lại 100% cho nội địa và hàng nặng, 5 phút/yêu cầu có lần chạy ok, 9 phút làm lại/ca sai. Theo hướng dẫn chi tiết, tính thêm kịch bản dùng thời gian làm lại trung bình từ dữ liệu và nêu tác động tới kết luận.
- Nhận vai viết code sau giải lao, hoàn thiện B và tính đủ năm câu D1: theo yêu cầu; theo nhân viên với m = 75; trần hiệu dụng với 20 nhân viên mỗi nhóm; trần với 6 depot mỗi nhóm; số yêu cầu/nhân viên khi chấp nhận mức chênh 6 điểm.
- Ngay trong D, tính tỉ lệ mở lại hiện tại trên toàn mẫu và trong phạm vi được chọn; bàn giao cho Người 4 trước khi chốt ngưỡng an toàn D3. Sang E, tính đủ ba chỉ số E1 và tái sử dụng kết quả an toàn đã kiểm.
- Chốt [bang_chi_phi.md](../report/team/bang_chi_phi.md); gửi D1 cho Người 4 và chỉ số cho Người 3. Các câu trả lời ngắn không quá ba dòng, có số.
- Khi bảo vệ, giải thích độ nhạy, chi phí cả hệ thống và cỡ mẫu hiệu dụng.

**Bàn giao:** code B, D1 và tính chỉ số; bảng chi phí A–B hoàn chỉnh; kết quả D1 và E1. Người 1 kiểm tra.

### Người 3 — Bảng lỗi, thiết kế đo lường và kiểm soát yêu cầu

- Theo dõi điều kiện “Xong khi” của từng checkpoint.
- Ở C, tự gắn nhãn cả 20 ca trong đề DOCX trong 8 phút, không trao đổi với Người 4 và không xem nhãn tham khảo trước khi gắn xong.
- Sau khi cả hai hoàn thành, tổng hợp hai bộ nhãn; tính đồng thuận = số ca trùng / 20, mục tiêu từ 80%. Nếu thấp hơn, viết lại định nghĩa trước khi đi tiếp và báo cáo trung thực kết quả ban đầu.
- Giữ nguyên hai bộ nhãn độc lập sau khi so; ghi nhãn thống nhất ở cột riêng, mỗi ca bất đồng có một câu quy tắc phân biệt.
- Cùng Người 4 chọn năm ca đủ năm loại lỗi, mỗi ca có cách phát hiện đo được bằng event, ngưỡng, tần suất; cách khắc phục; một vai trò chịu trách nhiệm.
- Chủ trì D2: trả lời đủ năm câu về đối chứng cùng thời gian, chia ngẫu nhiên, ảnh hưởng gián tiếp, cam kết chỉ số/ngưỡng/ngày quyết định trước khi chạy và điều kiện số cụm.
- Chủ trì E1: đặc tả ba chỉ số cho sẵn và thêm một chỉ số dùng, một chỉ số an toàn; nhận số tính thử ba chỉ số đầu từ Người 2.
- Liệt kê ít nhất sáu event có tên, bên tạo, thuộc tính, thời điểm và trace_id; chỉ rõ event tính từng chỉ số, bổ sung event nếu chưa đo được chỉ số.
- Làm E2: ít nhất hai dòng rủi ro kinh tế lấy số từ bảng B đã kiểm; có tác động, dấu hiệu theo dõi, hành động và vai trò phụ trách.
- Soát nhãn simulated và tính nhất quán giữa các tài liệu trước khi nộp.

**Bàn giao:** [bang_loi.md](../report/team/bang_loi.md), [chi_so.md](../report/team/chi_so.md), nội dung D2. Người 4 kiểm hồ sơ lỗi; Người 2 kiểm số chỉ số và rủi ro.

### Người 4 — Pilot, hồ sơ launch và điều phối nộp bài

- Mở và cập nhật [ho_so_launch_v0.md](../report/team/ho_so_launch_v0.md) từ đầu buổi, nhận số đã kiểm từ Người 1–3.
- Ở C, tự gắn nhãn độc lập cả 20 ca trong 8 phút, không trao đổi với Người 3; sau đó cùng hoàn thiện bảng lỗi.
- Chủ trì D3 trong [pilot_plan.yaml](../report/team/pilot_plan.yaml): nhận D1 từ Người 2, D2 từ Người 3, ghi kết quả vào chú thích đầu file và điền đủ mọi trường.
- Chốt phạm vi dựa vào A3; ghi cách chia, đối chứng, cỡ mẫu, hệ số thiết kế, số cụm và đánh đổi nếu thiết kế chưa đủ điều kiện. Không mặc định tăng thời gian là khắc phục được thiếu số cụm.
- Dựa vào tỉ lệ mở lại đã tính để đặt ngưỡng an toàn; có ít nhất ba luật dừng về an toàn, chi phí, mức sử dụng, đủ NẾU – TRONG – THÌ – KHÔNG THÌ.
- Ghi vai trò có quyền dừng, thời hạn hành động, rollback, ngày quyết định và danh sách đầu vào giả lập; kiểm YAML đọc được, không còn dấu hỏi.
- Chốt hồ sơ launch một trang, đủ bảy mục: chi phí; ba yếu tố nhạy; so với nhân viên; chỉ số; lỗi; pilot; rủi ro kinh tế. Mỗi mục có số, trạng thái hợp lệ và vai trò phụ trách.
- Đặt đề xuất Go / Go có điều kiện / No-go ở dòng cuối. Nếu có điều kiện, ghi người phụ trách và ngày kiểm tra; nếu No-go, ghi việc phải làm để quay lại cổng.
- Tổng hợp [TEAM.md](../TEAM.md), [group_report.md](../report/team/group_report.md) tối đa hai trang và [phieu_cham.md](../report/team/phieu_cham.md) từ thông tin thực tế của các thành viên và buổi duyệt chéo.
- Điều phối gửi hồ sơ, trình bày, commit, push và nhắc từng người tự nộp LMS.

**Bàn giao:** YAML, hồ sơ launch, phiếu chấm, báo cáo nhóm và TEAM.md. Người 3 kiểm đủ yêu cầu; Người 2 kiểm cỡ mẫu và các ngưỡng có cơ sở bằng số.

## 3. Lịch phối hợp theo checkpoint

Các giờ dưới đây là lịch mẫu tại lớp; nếu coach đổi lịch thì giữ thứ tự và thời lượng tương ứng.

| Thời gian | Người 1 | Người 2 | Người 3 | Người 4 |
| --- | --- | --- | --- | --- |
| 14:00–14:10 | Cài môi trường, chạy khung | Chuẩn bị máy thứ hai | Đọc checklist | Điền thông tin nhóm, mở hồ sơ |
| 14:10–14:53 · A | Code A1–A4 | Tính tay, ghi và kiểm bảng A | Theo dõi điều kiện hoàn thành | Cập nhật hồ sơ từ kết quả A |
| 14:53–15:20 · B | Code các kịch bản cùng Người 2 | Chủ trì phân tích B | Chuẩn bị khung chỉ số/event | Chuẩn bị khung YAML |
| 15:20–15:35 | Giải lao; bàn giao code | Giải lao; nhận vai viết code | Giải lao | Giải lao |
| 15:35–16:08 · C | Kiểm, hoàn thiện B cùng Người 2 | Sửa code và chốt B | Gắn độc lập 20 ca, sau đó so nhãn | Gắn độc lập 20 ca, sau đó so nhãn |
| 16:08–16:36 · D | Kiểm D1 | Tính D1 và tỉ lệ mở lại, gửi trước khi chốt D3 | Chốt D2 | Nhận baseline an toàn, điền và kiểm YAML D3 |
| 16:36–17:00 · E | Kiểm số kinh tế | Tính ba chỉ số, kiểm số | Chốt chỉ số, event, rủi ro | Chốt hồ sơ một trang, bảy mục |
| 17:00–17:45 | Bảo vệ chi phí, kiểm bằng chứng nhóm khác | Bảo vệ cỡ mẫu, kiểm số nhóm khác | Phản biện lỗi và chỉ số | Trình hồ sơ, ghi phiếu chấm |
| 17:45–18:00 | Chạy lại trên máy khác | Kiểm code và bảng | Soát đủ file, nhãn, liên kết | Tổng hợp, commit và push |

Trong tám phút gắn nhãn, Người 3 và Người 4 chỉ làm nhãn độc lập; sau đó dành thời gian so nhãn, giải thích bất đồng và hoàn thiện năm ca khắc phục. Hồ sơ đủ bảy mục phải sẵn sàng lúc 17:00 để gửi hội đồng.

## 4. Bàn giao và phối hợp trên Git

1. Người 1 bàn giao hàm mô hình ổn định và output A cho Người 2; Người 2 kiểm rồi chuyển số chốt cho Người 4.
2. Người 2 bàn giao B cho Người 3 viết rủi ro kinh tế, D1 cho Người 4 điền pilot và E1 cho Người 3 viết chỉ số.
3. Người 3 bàn giao bảng lỗi, D2 và chỉ số/event cho Người 4 ghép hồ sơ.
4. Người 4 tổng hợp; mọi thay đổi số liệu phải báo người đang dùng số đó để cập nhật đồng bộ.

Mỗi file có một người chốt để tránh ghi đè. Riêng src/lab13.py do Người 1 giữ trước giải lao, Người 2 giữ sau giải lao; người còn lại kiểm output hoặc đề xuất thay đổi. Hai người gắn nhãn giữ bản độc lập riêng trước khi tổng hợp bảng chung.

Khi duyệt chéo, cả bốn cùng chấm theo bằng chứng; Người 4 ghi phiếu. Nhóm n chấm nhóm n + 1, nhóm cuối chấm nhóm 1. Phiếu cần đủ ba tiêu chí, điểm, lý do có số, quyết định, một câu hỏi và câu trả lời thực tế của đội trình.

## 5. Danh sách đầu ra và người chốt

| File | Người chốt | Người kiểm |
| --- | --- | --- |
| src/lab13.py | Người 2 sau bàn giao từ Người 1 | Người 1 |
| report/team/bang_chi_phi.md | Người 2 | Người 1 |
| report/team/bang_loi.md | Người 3 | Người 4 |
| report/team/pilot_plan.yaml | Người 4 | Người 2 kiểm D1; Người 3 kiểm D2 và luật dừng |
| report/team/chi_so.md | Người 3 | Người 2 |
| report/team/ho_so_launch_v0.md | Người 4 | Người 1–3 kiểm phần mình |
| report/team/phieu_cham.md | Người 4 ghi từ buổi hội đồng | Người 1–3 |
| report/team/group_report.md | Người 4 tổng hợp | Người 3 |
| TEAM.md | Người 4 tổng hợp thông tin | Từng thành viên kiểm phần mình |
| Bốn file report/team/MSSV_HoTen.md | Mỗi người tự viết một file riêng | Người 3 kiểm đủ bốn file |

Mỗi người sao chép mẫu báo cáo cá nhân, đổi tên theo MSSV và họ tên không dấu, giữ nguyên file mẫu. Ghi phần việc, đóng góp, bằng chứng/commit, công cụ AI đã dùng và cách tự kiểm tra. Mỗi người cung cấp thông tin để cập nhật đóng góp thực tế trong TEAM.md.

## 6. Checklist hoàn thành và nộp bài

### Tính đúng và đủ bằng chứng

- [ ] A1 đạt cả ba phép thử; A2 đủ chín dòng; A3 đủ bốn loại; A4 có hai mức khối lượng.
- [ ] B1 đủ chín kịch bản; B2 có một cặp và xếp hạng; B3 đủ ba giới hạn; B4 có số và giải thích.
- [ ] Số tính do code nhóm chạy ra hoặc tính tay có cách tính; lệch đáp án không quá 2%.
- [ ] C có hai bộ nhãn độc lập, tỉ lệ đồng thuận, quy tắc cho ca bất đồng, năm ca khắc phục đủ năm loại. Mục tiêu đồng thuận từ 80% và khớp đáp án từ 16/20 ca.
- [ ] D có đủ năm câu D1, năm câu D2, mọi trường YAML và ít nhất ba luật dừng đúng mẫu; cách chia đủ mẫu và tách được tác động, hoặc ghi rõ đánh đổi.
- [ ] E có ba chỉ số tính thử, hai chỉ số tự đề xuất, ít nhất sáu event có trace_id, ánh xạ event với chỉ số và ít nhất hai rủi ro kinh tế.
- [ ] Hồ sơ một trang đủ bảy mục; trạng thái là “Xong, có bằng chứng”, “Chưa” hoặc “Giả lập”; mục dựa trên cột simulated ghi “Giả lập”.
- [ ] Đề xuất khớp bằng chứng, nêu cả số bất lợi và cách xử lý; dòng cuối là một trong ba quyết định hợp lệ.
- [ ] Phiếu chấm ghi kết quả duyệt chéo thật; không tự tạo điểm hoặc câu trả lời của nhóm khác.

### Quy định dữ liệu và hồ sơ

- [ ] Mọi số phụ thuộc cột _simulated, gồm tổng, chi phí và tỉ lệ suy ra, có nhãn simulated.
- [ ] Không kết luận trợ lý “đã nâng” chỉ số từ đợt chạy thử không có đối chứng.
- [ ] Người chịu trách nhiệm trong hồ sơ là vai trò có quyền quyết định, không ghi “cả đội”.
- [ ] Hồ sơ không chứa từ “production”.
- [ ] Không sửa hai CSV và lab13_starter.py; đọc logix_requests.csv với keep_default_na=False.
- [ ] Không gọi model thật; không dùng API key; không commit secret, .env hoặc .venv.
- [ ] Đủ sáu file hồ sơ đúng tên trong report/team/, báo cáo nhóm, TEAM.md và bốn báo cáo cá nhân.

### Kiểm tra và nộp

Chạy trong thư mục src/:

~~~powershell
python lab13.py
python -c "from pathlib import Path; import yaml; p=Path('../report/team/pilot_plan.yaml'); t=p.read_text(encoding='utf-8'); yaml.safe_load(t); assert '?' not in t; print('YAML hop le, khong con dau hoi')"
~~~

- [ ] Code chạy hết trên máy khác trong nhóm, ba phép thử A1 in ĐẠT.
- [ ] Repo đúng tên lớp L3B, public hoặc đã mời giảng viên; người chấm mở được.
- [ ] Đã commit và push bản chốt; thay đổi sau deadline dùng commit mới, không force-push hoặc sửa lịch sử.
- [ ] Cả bốn thành viên tự nộp cùng link repo trên LMS trước 23:59 GMT+7 ngày lab; ai chưa nộp link thì chưa hoàn tất nghĩa vụ cá nhân.

**Lưu ý hạn nộp:** 17:00 là mốc gửi hồ sơ cho hội đồng; 17:45–18:00 là mốc đóng gói tại lớp. Deadline hiện hành theo SUBMISSION.md là 23:59 GMT+7 ngày lab, trừ thông báo gia hạn của coach. Không dùng mốc 18:00 trong tài liệu gốc thay cho quy định nộp repo hiện hành.

Phần nâng cao không tính điểm. Chỉ làm sau khi toàn bộ yêu cầu bắt buộc đã được kiểm tra.

## 7. Tài liệu đối chiếu

- [README.md](../README.md): mục tiêu, lịch và năm quy tắc.
- [TEAM.md](../TEAM.md): bốn vai và yêu cầu đổi người viết code.
- [CHECKPOINTS.md](../CHECKPOINTS.md): điều kiện hoàn thành CP1–CP5.
- [RUBRIC.md](../RUBRIC.md): 70 điểm đối chiếu và 30 điểm hội đồng.
- [RULES.md](../RULES.md): liêm chính, dữ liệu và công cụ AI.
- [SUBMISSION.md](../SUBMISSION.md): cấu trúc, checklist và deadline.
- [Hướng dẫn chi tiết buổi chiều](Lab13_Huong_dan_chi_tiet_buoi_chieu.md): A4, B4 và các bước thực hiện.
- [Đề bài học viên](Ngay13_Lab13_De_bai_hoc_vien.docx): 20 ca lỗi và yêu cầu A–E.
- [Hướng dẫn học viên](Ngay13_Huong_dan_hoc_vien.docx): tổ chức nhóm.
- [Dữ liệu và công thức](du_lieu_va_cong_thuc.md).
