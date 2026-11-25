# Checklist công việc Lab 13 (nhóm 3 người)

Vai: **TV1** = viết code + kiểm số · **TV2** = gắn nhãn 1 + pilot_plan · **TV3** = gắn nhãn 2 + giữ hồ sơ.

## 0. Chuẩn bị (14:00–14:10)
- [ ] **TV3:** Tạo repo nhóm tên `K5-L3B-DAY13-TenNhom-LaunchEconomics` (fork hoặc đổi `origin`), mời các thành viên và giảng viên.
- [ ] **Cả 3:** Clone repo nhóm (không dùng repo đề).
- [ ] **Cả 3:** Cài môi trường trong `src/` (`venv`, `pip install -r requirements.txt`). Chạy thử `python lab13.py`.
- [ ] **Cả 3:** Đọc `docs/du_lieu_va_cong_thuc.md`.
- [ ] **TV3:** Điền vai trong `TEAM.md`, xoá dòng thành viên thứ 4 và ghi rõ vai kiêm nhiệm.
- [ ] **TV3:** Mở sẵn `ho_so_launch_v0.md` để điền dần từ đầu buổi.

## CP1 · A: Mô hình chi phí (14:10–14:53)
- [ ] **TV1:** Viết 3 hàm A1 ở dòng `TODO CP1`. Ba phép thử phải ĐẠT (1,20 · 1,25 · 1,25) rồi mới làm tiếp.
- [ ] **TV1:** Viết `mo_hinh(runs, reqs, …)` (A2).
- [ ] **TV1:** Chạy lại theo từng giá trị cột `loai` (A3).
- [ ] **TV1:** Cộng chi phí cố định 40 triệu/tháng cho `noi_dia` + `hang_nang` (A4).
- [ ] **TV2, TV3:** Tính tay một con số để đối chiếu với TV1.
- [ ] **TV1:** Điền bảng A2 (đủ 9 dòng, 2 dòng giả lập có nhãn `simulated`) và A3 (đủ 4 dòng) vào `bang_chi_phi.md`.
- [ ] **Cả 3:** Đối chiếu số với slide đáp án (lệch không quá 2%).
- [ ] **Cả 3:** Hiểu được vì sao tử số tính mọi lần chạy còn mẫu số chỉ đếm `thanh_cong`.

## CP2 · B: Bảng độ nhạy (14:53–15:20)
- [ ] **TV1:** Chạy 9 kịch bản đổi từng yếu tố (B1).
- [ ] **TV1:** Chạy 1 kịch bản đổi một cặp (B2).
- [ ] **TV1:** Chạy giới hạn 1/2/3 lần và tính chi phí cả hệ thống (B3).
- [ ] **TV1:** Chạy kịch bản xem lại 100% cho `noi_dia` + `hang_nang` (B4).
- [ ] **TV1:** Điền B1–B4 vào `bang_chi_phi.md` và xếp hạng 3 yếu tố mạnh nhất.
- [ ] **TV1:** Tự kiểm tra: "giảm một nửa" phải bằng nửa mức tăng của "gấp đôi".
- [ ] **TV1, TV3:** Mỗi câu trả lời không quá 3 dòng và có số.
- [ ] **TV1:** Bàn giao `mo_hinh()` cho người viết code mới (giờ giải lao 15:20–15:35).
- [ ] **Người nhận:** Chạy lại `lab13.py` trên máy mình, ba phép thử ĐẠT.

## CP3 · C: Bảng lỗi (15:35–16:08)
- [ ] **TV2, TV3:** Ngồi tách nhau, gắn nhãn độc lập 20 ca trong 8 phút (không trao đổi).
- [ ] **TV2, TV3:** So nhãn và tính tỉ lệ đồng thuận (cần từ 16/20). Không sửa bộ nhãn độc lập sau khi so.
- [ ] **TV2:** Với ca không trùng, thống nhất nhãn và ghi một câu quy tắc phân biệt.
- [ ] **TV2:** Chọn 5 ca, mỗi loại một ca. Điền bảng khắc phục trong `bang_loi.md`, mỗi dòng có cách phát hiện đo được (event, ngưỡng, tần suất) và một vai trò phụ trách.
- [ ] **TV1:** Hoàn thiện CP2 và viết sẵn khung D1 trong lúc hai người gắn nhãn.

## CP4 · D: pilot_plan.yaml (16:08–16:36)
- [ ] **Người viết code mới:** Tính 5 câu D1: cỡ mẫu theo yêu cầu, theo nhân viên, theo depot, mức chênh 6 điểm.
- [ ] **TV2:** Trả lời 5 câu D2 "tách được tác động".
- [ ] **TV2:** Tính tỉ lệ `mo_lai_trong_7_ngay` hiện tại trước khi đặt luật an toàn.
- [ ] **TV2:** Điền mọi dấu `?` trong `pilot_plan.yaml`. Ghi kết quả D1 và D2 vào chú thích đầu file.
- [ ] **TV2:** Viết ≥ 3 luật dừng (an toàn, chi phí, mức độ sử dụng) theo mẫu NẾU–TRONG–THÌ–KHÔNG THÌ, mỗi luật có ngưỡng, thời hạn và người có quyền dừng.
- [ ] **TV2:** Cách chia có ít nhất 20 cụm mỗi nhóm hoặc ghi rõ đánh đổi.
- [ ] **TV2:** Kiểm tra `yaml.safe_load` chạy không lỗi, và `grep -v '^ *#' … | grep -n '?'` không in gì.

## CP5 · E: Chỉ số, rủi ro, hồ sơ (16:36–17:00)
- [ ] **TV3:** Tính thử 3 chỉ số (chính, dùng, an toàn) và đề xuất thêm 1 chỉ số dùng, 1 chỉ số an toàn.
- [ ] **TV3:** Liệt kê ≥ 6 event có `trace_id` trong `chi_so.md`.
- [ ] **TV1:** Cấp số cho ≥ 2 dòng rủi ro kinh tế lấy từ bảng độ nhạy.
- [ ] **TV3:** Chốt `ho_so_launch_v0.md`: 1 trang, đủ 7 mục. Mỗi mục có con số chính, trạng thái (Xong, có bằng chứng · Chưa · Giả lập) và người phụ trách là một vai trò. Dòng cuối là đề xuất Go, Go có điều kiện hoặc No-go.
- [ ] **TV2:** Rà soát: `grep -rni production report/team` không in gì, mọi số giả lập có nhãn `simulated`, phạm vi đã thu hẹp có lý do bằng số.
- [ ] **Cả 3:** Gửi hồ sơ cho nhóm hội đồng lúc 17:00.

## Duyệt chéo Gate 2a (17:00–17:45)
- [ ] **TV3:** Điền `phieu_cham.md` khi chấm nhóm n+1 (nhóm cuối chấm nhóm 1).
- [ ] **TV1:** Trả lời câu hỏi về chi phí và độ nhạy.
- [ ] **TV2:** Trả lời câu hỏi về lỗi và pilot.
- [ ] **Cả 3:** Bảo vệ được lý do của đề xuất cuối, kể cả số bất lợi.

## Đóng gói và nộp (17:45–18:00, hạn 23h59 GMT+7)
- [ ] **Mỗi người:** Copy `report/team/MSSV_HoTen.md` thành file riêng (tên không dấu). Điền phần việc, đóng góp, bằng chứng, công cụ AI đã dùng và cách tự kiểm tra.
- [ ] **TV3:** Điền `report/team/group_report.md`.
- [ ] **TV3:** Hoàn thiện `TEAM.md` (URL repo, nhánh nộp, commit chốt).
- [ ] **Một người:** `cd src && python3 lab13.py` chạy hết trên máy khác, rồi commit và push. Không commit `.venv/` hay `.env`.
- [ ] **Cả 3:** Đủ 6 file hồ sơ trong `report/team/` đúng tên, không có từ "production", repo mở được cho người chấm.
- [ ] **Mỗi người, tự nộp:** Nộp cùng link repo trên LMS bằng tài khoản cá nhân. Ai không nộp thì không có điểm.
