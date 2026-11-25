# Lab 13 · Phân công việc và checkpoint theo người

Nhóm 4 người, mỗi người một vai theo [TEAM.md](TEAM.md). Các checkpoint CP1 → CP5 đi theo thứ tự (sau mỗi CP giảng viên chiếu đáp án, CP sau dùng lại số của CP trước), nhưng **trong mỗi checkpoint cả 4 người làm song song**. Mỗi checkpoint có một người **chịu trách nhiệm chính**: người đó đảm bảo đạt điều kiện "Xong khi" trong [CHECKPOINTS.md](CHECKPOINTS.md).

| Người | Vai | Họ tên |
| --- | --- | --- |
| Người 1 | Người viết code (trước giải lao) | Vinh |
| Người 2 | Người kiểm số (sau giải lao nhận viết code) | Ngô Duy Khánh (2A202603870) |
| Người 3 | Người gắn nhãn 1 | Bảo |
| Người 4 | Người gắn nhãn 2 kiêm giữ hồ sơ | Huy |

## 1. Ma trận người × checkpoint

**Chính** = chịu trách nhiệm đạt "Xong khi" · **Phụ** = làm một phần · trống = không tham gia CP đó.

| Checkpoint | Giờ | Điểm | Người 1 | Người 2 | Người 3 | Người 4 |
| --- | --- | ---: | --- | --- | --- | --- |
| Chuẩn bị (cài đặt, chạy thử) | 14:00 | | **Chính** | Phụ | | Phụ (khung hồ sơ) |
| CP1 · A · Mô hình chi phí | 14:10 | 20 | **Chính** (code) | Phụ (tính tay, điền bảng) | Phụ (theo dõi "Xong khi") | Phụ (mục 1, 3 hồ sơ) |
| CP2 · B · Bảng độ nhạy | 14:53 | 15 | **Chính** (code) | Phụ (điền bảng, tự kiểm) | | Phụ (mục 2 hồ sơ) |
| CP3 · C · Bảng lỗi 20 ca | 15:35 | 10 | Phụ (hoàn thiện B) | Phụ (hoàn thiện B) | **Chính** | Phụ (gắn nhãn 2) |
| CP4 · D · pilot_plan.yaml | 16:08 | 15 | Phụ (soát YAML) | **Chính** (code D1, YAML) | Phụ (luật dừng, rollback) | Phụ (mục 6 hồ sơ) |
| CP5 · E · Chỉ số, rủi ro, hồ sơ | 16:36 | 10 | Phụ (chạy lại toàn bộ) | Phụ (3 chỉ số E1) | Phụ (event) | **Chính** (hồ sơ, rủi ro, đề xuất) |
| Duyệt chéo Gate 2a | 17:00 | 30 | Phụ | Phụ | Phụ | **Chính** |
| Đóng gói, nộp | 17:45 | | **Chính** (TEAM.md, push) | Phụ | Phụ | Phụ (group_report) |

Tóm tắt: **Người 1** chính ở CP1, CP2 và nộp bài · **Người 2** chính ở CP4 · **Người 3** chính ở CP3 · **Người 4** chính ở CP5 và duyệt chéo.

## 2. Người 1 · Người viết code

**Chính:** CP1, CP2, đóng gói nộp · **Phụ:** CP3, CP4, CP5

- [ ] 14:00 tạo/clone repo nhóm, cài môi trường theo [src/README.md](src/README.md), chạy `python lab13.py`.
- [ ] **CP1 · A1:** viết 3 hàm trong [src/lab13.py](src/lab13.py) đến khi in `Ba phép thử đáp án biết trước: ĐẠT` (1,20 · 1,25 · 1,25).
- [ ] **CP1 · A2:** viết `mo_hinh()`: token, tool, phần lần chạy 2–3, xem lại, làm lại, tổng, số việc thành công, chi phí mỗi việc thành công, hoá đơn chia số yêu cầu.
- [ ] **CP1 · A3:** gọi `mo_hinh` cho từng `loai`, tính thêm tỉ lệ ok theo từng lần thử (để trả lời "chạy lại có giúp không").
- [ ] **CP1 · A4:** cộng chi phí cố định 40 triệu đ/tháng cho phạm vi `noi_dia` + `hang_nang`, ở 45.000 yêu cầu/tháng và một nửa.
- [ ] **CP2 · B1:** 9 kịch bản (giá token ×2/÷2, xem lại ×2/÷2, làm lại ×2/÷2, lương +25%, tối đa 2 lần, 1 lần).
- [ ] **CP2 · B2, B3, B4:** đổi một cặp; chi phí cả hệ thống với giới hạn 1/2/3 lần; xem lại 100% cho `noi_dia` + `hang_nang`.
- [ ] **CP3:** trong lúc Người 3, 4 gắn nhãn: hoàn thiện B, dọn code để chạy từ đầu đến cuối.
- [ ] **Sau giải lao:** bàn giao code cho Người 2.
- [ ] **CP4:** soát `pilot_plan.yaml`: `yaml.safe_load` chạy được, không còn `?` ngoài dòng chú thích.
- [ ] **CP5:** chạy lại `lab13.py` từ đầu trên một máy khác trong nhóm.
- [ ] **17:45:** điền [TEAM.md](TEAM.md), commit, push.

## 3. Người 2 · Người kiểm số

**Chính:** CP4 · **Phụ:** CP1, CP2, CP3, CP5

- [x] **CP1:** tính tay ít nhất một con số mỗi bảng để đối chiếu (ví dụ tổng chi phí ÷ số việc thành công).
- [x] **CP1:** điền A1, A2, A3, A4 và hai câu trả lời vào [report/team/bang_chi_phi.md](report/team/bang_chi_phi.md); nhãn `simulated` ở dòng xem lại, làm lại.
- [x] **CP2:** điền B1–B4; tự kiểm "giảm một nửa = nửa mức tăng của gấp đôi"; mỗi câu ≤ 3 dòng, có số.
- [x] **CP3:** soát lại `bang_chi_phi.md` (lệch ≤ 2% so với slide chữa).
- [x] **Sau giải lao nhận viết code.**
- [x] **CP4 · D1:** tính 5 câu cỡ mẫu (theo yêu cầu, theo nhân viên m = 75, 20 nhân viên mỗi nhóm, 6 depot mỗi nhóm, mức chênh 6 điểm) trong `lab13.py`.
- [x] **CP4:** tính tỉ lệ `mo_lai_trong_7_ngay` hiện tại trước khi đặt luật an toàn.
- [x] **CP4:** chủ trì [report/team/pilot_plan.yaml](report/team/pilot_plan.yaml): chú thích D1, D2, đánh đổi, các trường số, `simulated_inputs`.
- [x] **CP5 · E1:** tính 3 chỉ số (chính, bỏ qua gợi ý, lỗi lọt đến khách), đưa vào [report/team/chi_so.md](report/team/chi_so.md).

## 4. Người 3 · Người gắn nhãn 1

**Chính:** CP3 · **Phụ:** CP1, CP4, CP5

- [ ] **Suốt buổi:** đọc đề, theo dõi "Xong khi" của từng CP, nhắc 5 quy tắc lab (nhãn `simulated`, ≤ 3 dòng có số, không dùng từ "production"…).
- [ ] **CP3:** gắn nhãn 20 ca trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` **độc lập**, 8 phút, không trao đổi.
- [ ] **CP3:** so nhãn với Người 4, tính tỉ lệ đồng thuận; viết một câu quy tắc cho mỗi ca không trùng (dưới 80% thì viết lại định nghĩa).
- [ ] **CP3:** bảng khắc phục 5 ca, mỗi loại một ca, cách phát hiện đo được (event, ngưỡng, tần suất), một vai trò phụ trách, trong [report/team/bang_loi.md](report/team/bang_loi.md).
- [ ] **CP4:** viết 3 luật dừng (an toàn, chi phí, mức dùng) đủ NẾU – TRONG – THÌ – KHÔNG THÌ; `identifiability`, `rollback`.
- [ ] **CP5:** danh sách ≥ 6 event có `trace_id` và phần kiểm tra chéo chỉ số ↔ event trong `chi_so.md`.

## 5. Người 4 · Người gắn nhãn 2, kiêm giữ hồ sơ

**Chính:** CP5, duyệt chéo · **Phụ:** CP1–CP4

- [ ] **Từ 14:10:** điền dần [report/team/ho_so_launch_v0.md](report/team/ho_so_launch_v0.md) sau mỗi CP (mục 1, 3 sau CP1; mục 2 sau CP2; mục 5 sau CP3; mục 6 sau CP4).
- [ ] **CP3:** gắn nhãn 20 ca **độc lập**, song song Người 3, không trao đổi.
- [ ] **CP5 · E1:** đề xuất thêm 1 chỉ số dùng và 1 chỉ số an toàn trong `chi_so.md`.
- [ ] **CP5 · E2:** ≥ 2 dòng rủi ro kinh tế, số lấy từ bảng độ nhạy, có người phụ trách là vai trò.
- [ ] **CP5 · E3:** hoàn thiện 7 mục hồ sơ (con số chính, trạng thái Xong/Chưa/Giả lập, vai trò phụ trách); chốt đề xuất Go / Go có điều kiện / No-go, kèm con số bất lợi và cách xử lý.
- [ ] **17:00:** gửi hồ sơ cho nhóm hội đồng; chủ trì chấm nhóm n + 1 vào [report/team/phieu_cham.md](report/team/phieu_cham.md).
- [ ] **17:45:** viết [report/team/group_report.md](report/team/group_report.md).

## 6. Việc nào phải chờ việc nào

| Việc | Phải chờ | Lý do |
| --- | --- | --- |
| B (độ nhạy) | A2 (`mo_hinh`) | B chỉ là gọi lại `mo_hinh` với tham số đã đổi |
| Phạm vi pilot trong D | A3 | Chọn loại yêu cầu dựa vào chi phí từng loại |
| Luật dừng an toàn trong D | Tỉ lệ mở lại hiện tại | Ngưỡng thấp hơn tỉ lệ hiện tại sẽ dừng pilot tuần đầu |
| Rủi ro E2 | B | Số tác động lấy từ bảng độ nhạy |
| Hồ sơ launch, đề xuất | A–E | Hồ sơ ghép kết quả của tất cả |

**Làm được ngay, không chờ ai:** gắn nhãn C, cỡ mẫu D1, 3 chỉ số E1, danh sách event. Nếu làm ở nhà (hạn 23h59), chia song song từ đầu: Người 1 code A, B · Người 2 code D1, E1 · Người 3, 4 gắn nhãn C trước rồi làm event và hồ sơ.

## 7. Checklist nộp bài (cả nhóm)

- [ ] Repo đổi tên `K5-L3A-DAY13-TenNhom-LaunchEconomics` (hoặc `L3B`), mở được cho người chấm.
- [ ] `cd src && python lab13.py` chạy hết trên máy khác; ba phép thử in ĐẠT.
- [ ] Đủ 6 file hồ sơ trong `report/team/`, đúng tên; `group_report.md` đã điền.
- [ ] Mọi số từ cột `_simulated` có nhãn `simulated`.
- [ ] `pilot_plan.yaml` đọc được bằng `yaml.safe_load`, không còn `?`, ≥ 3 luật dừng đủ bốn vế.
- [ ] Người phụ trách là một vai trò, không ghi "cả đội"; đề xuất là Go / Go có điều kiện / No-go.
- [ ] `grep -rni production report/team` không in gì.
- [ ] Mỗi người copy `report/team/MSSV_HoTen.md` thành file riêng (có mục công cụ AI đã dùng).
- [ ] **Mỗi người tự nộp link repo trên LMS** trước 23h59 GMT+7.

## Lưu ý

1. **Người 3, 4 không đọc trước** mục "Nhãn tham khảo cho 20 ca" trong [docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md](docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md) và trang 71 của slide cho tới khi gắn xong; không sửa bộ nhãn độc lập sau khi đã so.
2. Số trong hồ sơ phải do `lab13.py` của nhóm tính ra; file hướng dẫn chi tiết chỉ dùng để tự đối chiếu (lệch ≤ 2%).
3. Đọc CSV phải có `keep_default_na=False`. Không sửa 2 file CSV và `lab13_starter.py`.
