# Phân công Lab 13: 4 người làm song song

Tài liệu cho 4 thành viên nhóm LuckyTeam. Mục tiêu: mỗi người làm phần của mình từ đầu buổi, không ai phải ngồi chờ người khác.

## Ý chính để không ai phải đợi ai

1. **Mỗi người làm trên nhánh riêng và tự giữ file của mình.** Không có hai người cùng sửa một file, nên khi merge không bị xung đột.
2. **Code B, D, E viết ở module riêng**, không viết thẳng vào `src/lab13.py`. Hàm nhận `mo_hinh` làm tham số, ví dụ `chay_do_nhay(mo_hinh, runs, reqs)`. Cuối buổi Người 1 thêm vài dòng import vào `__main__`, để `python lab13.py` vẫn chạy hết từ đầu đến cuối như yêu cầu.
3. **Không cần đợi `mo_hinh` của Người 1.** Tên hàm và tham số đã có sẵn trong `src/lab13.py`, còn [hướng dẫn chi tiết, mục A2](docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md) có code mẫu. Người 2 chép tạm code đó vào file của mình làm bản thay thế, khi Người 1 merge thì chuyển sang `from lab13 import mo_hinh`.
4. **Chỉ có một lần ngồi chung bắt buộc:** hai người gắn nhãn so nhãn ở bài C, khoảng 10 phút. Đề yêu cầu gắn nhãn độc lập rồi mới so, nên không bỏ được bước này.

## Bảng phân công

| | Người 1: viết code A | Người 2: kiểm số và độ nhạy B | Người 3: gắn nhãn 1 và pilot D | Người 4: gắn nhãn 2 và giữ hồ sơ, chỉ số E |
|---|---|---|---|---|
| **Vai trong TEAM.md** | Người viết code (trước giải lao) | Người kiểm số | Người gắn nhãn 1, viết code sau giải lao | Người gắn nhãn 2 kiêm giữ hồ sơ |
| **File tự giữ** | `src/lab13.py`, `report/team/bang_chi_phi.md` (phần A1–A4) | `src/cp2_do_nhay.py`, `report/team/bang_chi_phi.md` (phần B1–B4), phần E2 trong `report/team/chi_so.md` | `src/cp4_co_mau.py`, `report/team/pilot_plan.yaml`, `report/team/bang_loi.md` | `src/cp5_chi_so.py`, `report/team/chi_so.md` (E1 và event), `report/team/ho_so_launch_v0.md`, `TEAM.md`, `report/team/group_report.md` |
| **Việc 1** | A1: ba hàm, qua ba phép thử 1,20 · 1,25 · 1,25 | Tính tay A1 và A2 bằng pandas, độc lập với Người 1, để đối chiếu | **Gắn nhãn 20 ca một mình trong 8 phút** (lấy từ file docx đề bài, mục "Hai mươi ca lỗi"), không trao đổi | **Gắn nhãn 20 ca một mình trong 8 phút**, không trao đổi |
| **Việc 2** | A2: `mo_hinh`, gồm cả nhánh `max_lan_chay`, và trả thêm `chay_lai`, `hoa_don_moi_yc` | B1: 9 kịch bản, kiểm tra kịch bản "giảm một nửa" bằng đúng nửa mức tăng của "gấp đôi" | D1: năm câu cỡ mẫu a–e | E1: tính ba chỉ số (chính, dùng, an toàn) và đề xuất thêm một chỉ số dùng, một chỉ số an toàn |
| **Việc 3** | A3: tách theo 4 loại, thêm tỉ lệ đúng theo từng lần chạy (`attempt`) | B2 (đổi một cặp, xếp hạng), B3 (giới hạn 1/2/3 lần, chi phí cả hệ thống) | D2: năm câu "tách được tác động"; tính tỉ lệ `mo_lai_trong_7_ngay` trước khi đặt luật an toàn | Ít nhất 6 event có `trace_id`, kèm phần kiểm tra chéo chỉ số với event |
| **Việc 4** | A4: cộng chi phí cố định 40 triệu, ở khối lượng 45.000 và một nửa | B4: xem lại 100% (`noi_dia` + `hang_nang`) | Điền hết dấu `?` trong `pilot_plan.yaml`, ít nhất 3 luật dừng theo mẫu NẾU – TRONG – THÌ – KHÔNG THÌ | Dựng khung hồ sơ 7 mục ngay từ đầu: vai phụ trách, trạng thái, đề xuất nháp |
| **Việc 5** | Nối các module vào `lab13.py`, chạy lại toàn bộ | E2: ít nhất 2 dòng rủi ro kinh tế, lấy số từ B do chính mình tính | Sau khi thống nhất nhãn: viết quy tắc cho các ca không trùng và bảng khắc phục 5 ca (đủ 5 loại) | Điền số vào hồ sơ khi các nhánh đã merge |
| **Tự kiểm tra** | `python lab13.py` in ĐẠT; A2 khớp số của Người 2 | Số trong `cp2_do_nhay.py` khớp số chạy qua `lab13.py` | `yaml.safe_load` chạy không lỗi; `grep` không còn `?` ngoài dòng chú thích | `grep -rni production report/team` không in gì |

## Vì sao không phải chờ nhau

- **A và B:** Người 2 dùng tạm bản `mo_hinh` mẫu nên chạy được B ngay. Việc kiểm số cũng không cần đợi Người 1 vì là tính độc lập.
- **C và các việc khác:** gắn nhãn chỉ cần file đề bài. Lúc so nhãn, Người 4 gửi nhãn của mình cho Người 3, và Người 3 là người duy nhất ghi vào `bang_loi.md`.
- **D:** cỡ mẫu chỉ dùng số đề cho sẵn (0,70; +5 điểm; alpha 0,05; power 0,8; ICC 0,02). Phạm vi `noi_dia` + `hang_nang` thì đề bài A4 đã nói trước, không cần đợi kết quả A3.
- **E1:** tính thẳng từ `src/logix_requests.csv`, không phụ thuộc mô hình chi phí.
- **Rủi ro E2** cần số của bài B, nên giao luôn cho Người 2, người đang có các số đó.
- **Hồ sơ:** Người 4 dựng khung và chữ trước, cuối buổi mới điền số. Đây là bước tổng hợp, không phải chờ giữa chừng.

## Thứ tự trong buổi

1. **Bắt đầu (10 phút, cả nhóm):** cài `.venv`, mỗi người tạo nhánh `p1-A`, `p2-B`, `p3-CD`, `p4-E`. Chốt tên các vai phụ trách dùng chung trong mọi file (ví dụ "Giám đốc vận hành", "PM trợ lý hoàn phí", "Trưởng nhóm CSKH") để các file khớp nhau.
2. **Làm song song (khoảng 60–75 phút):** mỗi người làm cột của mình. Lúc nào cả hai người gắn nhãn xong thì ngồi so nhãn 10 phút, cần đồng thuận từ 16/20 ca.
3. **Merge:** Người 1 merge theo thứ tự `p1` → `p2` → `p3` → `p4`, nối module vào `lab13.py` và chạy lại. Người 2 so số lần cuối.
4. **Trước 17:00:** Người 4 điền số và chốt đề xuất (Go / Go có điều kiện / No-go). Cả nhóm đọc lại 5 phút.
5. **Duyệt chéo Gate 2a:** Người 1 và 2 chấm hồ sơ nhóm bạn vào `report/team/phieu_cham.md`. Người 3 và 4 bảo vệ hồ sơ của mình.
6. **Cuối buổi:** mỗi người tự copy `report/team/MSSV_HoTen.md` thành báo cáo cá nhân (làm lúc nào cũng được). Mỗi người tự nộp link repo trên LMS.

## Hai lưu ý cho cả nhóm

- Mọi con số tính từ cột `_simulated` phải có nhãn `simulated`.
- Người phụ trách phải là một vai trò cụ thể, không ghi "cả đội".
