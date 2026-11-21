# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: Stech
- Lớp: L3A
- Thành viên: xem `TEAM.md` (Lưu Thanh Mỹ, Nguyễn Thị Hồng Hạnh, Phạm Đức Hồng Đức, Bùi Lê Công Tuấn)

## 2. Mục tiêu và cách tiếp cận

- Đánh giá tính kinh tế thật và lập kế hoạch pilot **Gate 2a** cho trợ lý hoàn phí của **LogiX-VN** trên dữ liệu giả lập (1.200 yêu cầu, 1.624 lần chạy).
- Chia nhóm theo cặp: Mỹ + Hạnh phụ trách phần chính (CP1–CP2: mô hình chi phí và độ nhạy), Đức + Tuấn phụ trách phần phụ (CP3–CP4: gắn nhãn lỗi và thiết kế pilot), Tuấn tổng hợp hồ sơ CP5 và review toàn bộ trước khi nộp.

## 3. Giải pháp

- **Nhiệm vụ A & B ([bang_chi_phi.md](bang_chi_phi.md), [src/lab13.py](../../src/lab13.py)):** Hoàn thành 3 phép thử A1 (`1,20 · 1,25 · 1,25`), xây dựng `mo_hinh()`, tách theo 4 loại yêu cầu (A3), cộng chi phí cố định 40 triệu đ/tháng (A4), phân tích độ nhạy 9 kịch bản (B1–B2), chi phí cả hệ thống theo giới hạn chạy lại (B3) và kịch bản xem lại 100% (B4).
- **Nhiệm vụ C ([bang_loi.md](bang_loi.md)):** Hai thành viên gắn nhãn độc lập 20 ca lỗi theo 5 loại Google PAIR đạt đồng thuận **20/20 (100%)**, lập bảng khắc phục 5 ca có event, ngưỡng, tần suất đo được và vai trò phụ trách.
- **Nhiệm vụ D ([pilot_plan.yaml](pilot_plan.yaml), [src/lab13.py](../../src/lab13.py)):** Tính 5 câu cỡ mẫu D1, chọn chia cụm theo nhân viên `20 + 20`, chấp nhận đánh đổi MDE 6 điểm (`n = 859`, `m >= 299`, `DE = 6,96`), thiết kế 3 luật dừng 4 vế `NẾU – TRONG – THÌ – KHÔNG THÌ`.
- **Nhiệm vụ E ([chi_so.md](chi_so.md), [ho_so_launch_v0.md](ho_so_launch_v0.md)):** Đặc tả 5 chỉ số, 10 event có `trace_id`, 3 dòng rủi ro kinh tế và tổng hợp hồ sơ 1 trang (7 mục) cho Gate 2a.

## 4. Kết quả

- **Chi phí mỗi việc thành công:** **4.472 đ** [simulated] trên toàn mẫu (gấp **16,3×** hoá đơn token+tool 274,7 đ); phạm vi `noi_dia` + `hang_nang` cộng cố định là **4.599 đ** (`0,38×` so với 12.000 đ) ở 45.000 yc/tháng và **5.784 đ** (`0,48×`) ở nửa khối lượng [simulated].
- **Độ nhạy & vận hành:** 3 yếu tố mạnh nhất là số ca làm lại (`+51,8%`), tỉ lệ xem lại (`+40,7%`), lương nhân viên (`+23,1%`) [simulated]; giới hạn **2 lần chạy** rẻ nhất cho cả hệ thống (**6.901.220 đ** [simulated]).
- **Chỉ số đợt chạy thử:** Chính **82,83%** (994/1.200), bỏ qua gợi ý **27,12%** (48/177), mở lại 7 ngày **4,25%** (51/1.200).
- **Đề xuất cuối (`ho_so_launch_v0.md`):** **`Go có điều kiện`** (chỉ pilot `noi_dia` + `hang_nang`, giới hạn 2 lần chạy, triển khai 5 cơ chế kiểm soát lỗi, theo dõi thời gian xem lại dưới 4,8–5,1 phút [simulated]).
- **Kết quả duyệt chéo Gate 2a từ hội đồng:** *(cập nhật sau phiên duyệt chéo lúc 17:00)*.

## 5. Khó khăn và cách xử lý

- **Tách dữ liệu & kiểm soát nhãn:** Đọc CSV thiếu `keep_default_na=False` dễ làm sai cột `quyet_dinh_xem_lai`; nhóm đã chuẩn hoá trong `src/lab13.py`. Hai người gắn nhãn giữ độc lập trước khi đối chiếu, sau đó ghi rõ phạm vi giải thích cho từng ca dễ nhầm.
- **Khác biệt nhỏ ở B4 (`948` vs `982`):** Trong quá trình review PR #12 và PR #9, nhóm phát hiện code B4 dùng `982` yêu cầu thay vì `948` yêu cầu có `status == 'ok'` (chênh 0,55%: `11.679 đ` vs `11.743 đ` [simulated]) và đã ghi nhận đối chiếu rõ trong `bang_chi_phi.md`.
- **Chính sách Application Control trên Windows:** Trên một máy thành viên, chính sách bảo mật Windows chặn nạp DLL mở rộng (`.pyd`) của `pandas` trong `.venv` (`ImportError: DLL load failed ...: An Application Control policy has blocked this file`). Nhóm khắc phục bằng cách kiểm tra `yaml.safe_load` / logic CP4 trực tiếp bằng Python chuẩn và đối chiếu chạy `src/lab13.py` trên máy khác trong nhóm.

## 6. Tổng hợp đóng góp

Phân công của nhóm nằm trong `TEAM.md`; đóng góp chi tiết nằm trong bốn báo cáo cá nhân: `2A202603532_LuuThanhMy.md`, `2A202603537_NguyenThiHongHanh.md`, `2A202603558_PhamDucHongDuc.md`, `2A202603610_BuiLeCongTuan.md`.

## 7. Hạn chế và hướng cải thiện

- **Cỡ mẫu pilot:** Với 40 nhân viên, không đủ mẫu cho MDE 5 điểm (tối đa 1.000 hiệu dụng < 1.251); nhóm chấp nhận MDE 6 điểm (`power` giảm còn ~0,64 nếu tác động thật chỉ 5 điểm) và cần kéo dài thời gian thu thập đủ `m >= 299` yêu cầu/người.
- **Số liệu giả lập:** Chi phí giờ nhân viên dựa trên cột `_simulated`; cần đo thời gian xem lại và làm lại thực tế qua event `staff_review_decision` và `staff_rework_completed` trong pilot để hiệu chỉnh mô hình.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, arxiv.org/abs/2504.13359.
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure".
- Tài liệu `statsmodels` (`NormalIndPower`, `proportion_effectsize`) và tài liệu Lab 13 (`docs/du_lieu_va_cong_thuc.md`, `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`).
