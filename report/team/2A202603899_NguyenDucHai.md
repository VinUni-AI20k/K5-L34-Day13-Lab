# Báo cáo cá nhân — NguyenDucHai-2A202603899

## 1. Thông tin thành viên

- Họ tên: Nguyễn Đức Hải
- MSSV: 2A202603899
- Email: 26ai.haind4@vinuni.edu.vn
- Vai trong nhóm: người giữ hồ sơ (Thành viên 4 theo bảng phân công của nhóm). Giữ `pilot_plan.yaml`, `chi_so.md`, `ho_so_launch_v0.md`; tổng hợp `phieu_cham.md`, `group_report.md`, `TEAM.md`.

## 2. Phần việc phụ trách

- **CP1 · A4:** cộng chi phí cố định 40 triệu đ/tháng cho phạm vi noi_dia + hang_nang, ở 45.000 yêu cầu/tháng và ở một nửa khối lượng.
- **CP2 · B2, B4:** đổi một cặp (giá token và xem lại cùng gấp đôi); xem lại 100% trong phạm vi; chuyển số rủi ro kinh tế sang CP5.
- **CP3:** soạn bảng khắc phục 5 ca, mỗi loại một ca, kèm 5 ca dự phòng; đặt ngưỡng phát hiện từ dữ liệu chạy thử.
- **CP4:** giữ `pilot_plan.yaml`; tính tỉ lệ mở lại hiện tại; soạn phạm vi, cách chia, lịch, luật dừng, rollback, ngày quyết định.
- **CP5:** giữ `chi_so.md` và `ho_so_launch_v0.md`; ghép phần chỉ số và rủi ro; viết đề xuất cuối.

## 3. Đóng góp cụ thể

- **A4** [simulated]:
  - chi phí mỗi việc thành công trong phạm vi 3.414 đ; cộng cố định thành 4.599 đ = 0,38× ở 45.000 yêu cầu/tháng, 5.784 đ = 0,48× ở một nửa
  - hoà vốn ở khoảng 6.212 yêu cầu/tháng (14% kế hoạch)
  - con số bất lợi: cộng 82 ca nhân viên làm thay thì là 0,43×, không phải 0,38×
- **B2** [simulated]: 6.543 đ (+46,3%), đúng bằng 5,6% + 40,7% vì mô hình cộng tuyến tính.
- **B4** [simulated]: xem lại 100% cho 11.743 đ = 0,98×; nếu làm lại 15,3 phút như dữ liệu thì 12.415 đ = 1,03×. Hoà vốn khi mỗi lần xem lại ≤ 5,1 phút (4,8 phút).
- **CP3:**
  - 5 ca chính: 1 (Do người dùng), 20 (Hệ thống), 18 (Ngữ cảnh), 4 (Giới hạn hệ thống), 17 (Ngầm)
  - 5 ca dự phòng: 9, 7, 3, 19, 12
  - ngưỡng lấy từ dữ liệu: chuyển nhân viên 3,5% trong phạm vi; mở lại 3,97%; token + tool theo depot cao nhất 1,05× trung vị
  - cả 5 ca chính khớp nhãn thống nhất nên TV3 dùng nguyên trong `bang_loi.md`
- **CP4 ·** `pilot_plan.yaml`**:**
  - chia theo nhân viên 20 + 20, phân tầng theo 12 depot
  - MDE 6 điểm, 859 yêu cầu mỗi nhóm, DE 6,96, m ≥ 299; nêu con số bất lợi power 0,64 nếu tác động thật chỉ 5 điểm
  - với 30,7 yêu cầu/nhân viên/ngày trong phạm vi, bước 0.50 cần khoảng 10 ngày, nên kéo dài 3 tuần; ngày quyết định 2027-01-18, sau 7 ngày theo dõi mở lại
  - mở lại hiện tại 4,25% (3,97% trong phạm vi, hang_nang 8,23%), nên không đặt ngưỡng tuyệt đối 3% mà so với đối chứng (+2 điểm) kèm trần 6%
  - 4 luật dừng đủ NẾU – TRONG – THÌ – KHÔNG THÌ: mở lại, hoàn trùng, chi phí > 8.000 đ, bỏ qua gợi ý > 40%
  - D1(a–d) do mình tính trước để đối chiếu; sau đó TV1 gửi D1(a) = 1.251 và TV2 gửi D1(b–d), cả hai khớp số trong file
- **CP5:**
  - ba chỉ số tính thử: chính 82,83% (994/1.200), bỏ qua gợi ý 27,12% (48/177), mở lại 4,25% (51/1.200)
  - đề xuất chỉ số dùng: % yêu cầu nhóm trợ lý có gợi ý được mở, đo cả ở nhóm đối chứng để phát hiện tràn tác động
  - danh sách 11 event có `trace_id`, đồng bộ tên với `bang_loi.md`; kiểm tra chéo cả 5 chỉ số đều đo được
  - hồ sơ 7 mục; đề xuất **Go có điều kiện** cho noi_dia + hang_nang, 5 điều kiện có người phụ trách và ngày kiểm tra

## 4. Bằng chứng

- Script: `src/tv4_tinh_so.py`, mỗi checkpoint một hàm (`cp1_a4`, `cp2_b2`, `cp2_b4`, `cp2_rui_ro`, `cp3_nguong`, `cp4_pilot`, `cp5_chi_so`). Chạy trong `src/` bằng lệnh `python tv4_tinh_so.py`; gọi lại `mo_hinh` trong `src/lab13.py` của TV1.
- File bàn giao: `report/team/tv4_ban_giao.md` (A4, B2, B4 gửi TV2; bảng khắc phục gửi TV3).
- File giữ: `report/team/pilot_plan.yaml`, `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md`.
- Commit:
  - `b1bef74` CP1 (A4), merge qua PR #2
  - `16b5e4e` CP2 (B2, B4), merge qua PR #8
  - `290f265` CP3 (bảng khắc phục), merge qua PR #12
  - `66f8577` CP4 và `1b30ea5` CP5, merge qua PR #20

## 5. Công cụ AI đã dùng

- **Claude Code** (trợ lý lập trình trong terminal) dùng để:
  - đọc đề, tóm tắt bảng phân công và xác định việc nào làm ngay được, việc nào phải chờ người khác
  - viết `src/tv4_tinh_so.py` và chạy để ra số
  - soạn nháp file bàn giao, `pilot_plan.yaml`, `chi_so.md`, `ho_so_launch_v0.md`

- **Cách tự kiểm tra:**
  - so mọi số với số tham chiếu trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`, lệch 0% (riêng 12.415 đ so với 12.414 đ do làm tròn 12.414,79)
  - so `mo_hinh` của TV1 với một bản tính độc lập viết ở CP1: A2, A3, B1 khớp từng đồng
  - `yaml.safe_load` đọc được `pilot_plan.yaml`; ngoài chú thích không còn dấu `?`
  - chạy lệnh grep tìm từ cấm và người phụ trách "cả đội" theo checklist CP5, kết quả rỗng

## 6. Tự đánh giá

- **Đã xong:** A4, B2, B4, bảng khắc phục, `pilot_plan.yaml`, `chi_so.md`, `ho_so_launch_v0.md`. Mọi số có nhãn `simulated` khi tính từ cột giả lập.
- **Điểm cần học thêm:** phần lớn code và bản nháp do AI viết. Mình cần tự giải thích được trước hội đồng:
  - vì sao chia 20 nhân viên mỗi nhóm có trần cỡ mẫu c / ICC = 1.000, nên phải chấp nhận MDE 6 điểm
  - vì sao chọn Go có điều kiện thay vì Go, dù chi phí trong phạm vi chỉ 0,38×
