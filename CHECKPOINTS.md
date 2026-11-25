# Checkpoints

Năm checkpoint bám theo năm nhiệm vụ A–E của buổi lab 14:00–18:00 (giải lao 15:20–15:35). Giờ ghi kèm là mốc tại lớp, không phải deadline nộp bài; lớp học giờ khác đi cùng thứ tự và thời lượng, giờ cụ thể theo coach thông báo. Sau mỗi nhiệm vụ, giảng viên chiếu slide đáp án; số của nhóm được nhận nếu lệch không quá 2%. Mọi lệnh chạy trong thư mục `src/`.

Cách làm từng bước, code mẫu và số để tự đối chiếu: [docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md](docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md).

## CP1 — Mô hình chi phí mỗi việc thành công (14:00 → 14:53, nhiệm vụ A)

- **Mục tiêu:** tính được chi phí thật cho mỗi yêu cầu được giải quyết từ trace, và chỉ ra nó gấp bao nhiêu lần hoá đơn token.
- **Cần làm:** 14:00 chia vai trong `TEAM.md` (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ), cài môi trường theo [src/README.md](src/README.md). Viết vào `src/lab13.py` (tài liệu trong `docs/` gọi là `lab13_starter.py`; bản gốc giữ nguyên để đối chiếu): viết ba hàm A1 ở dòng `TODO CP1`; viết `mo_hinh(runs, reqs, …)` (đã có sẵn tham số giá và hệ số, A2); gọi lại cho từng giá trị cột `loai` (A3); cộng chi phí cố định 40 triệu đ/tháng cho phạm vi `noi_dia` + `hang_nang` (A4). Điền bảng A2, A3, A4 và các câu trả lời vào `report/team/bang_chi_phi.md`.
- **Sản phẩm:** `src/lab13.py` in ba phép thử ĐẠT và bảng A2; `report/team/bang_chi_phi.md` có bảng A2 đủ 9 dòng (hai dòng giả lập có nhãn `simulated`) và bảng A3 đủ 4 dòng.
- **Cần hiểu:** vì sao tử số tính mọi lần chạy kể cả lần lỗi, còn mẫu số chỉ đếm `ket_qua == 'thanh_cong'`; loại yêu cầu nào không đáng để trợ lý xử lý và vì sao chạy lại tới 3 lần không giúp loại đó.
- **Tự kiểm tra:** `python lab13.py` in `Ba phép thử đáp án biết trước: ĐẠT` (1,20 · 1,25 · 1,25). Chi phí mỗi việc thành công phải lớn hơn nhiều lần hoá đơn token chia số yêu cầu; nếu chỉ gấp 1–2 lần là đã quên giờ của nhân viên.

## CP2 — Bảng độ nhạy (14:53 → 15:20, nhiệm vụ B)

- **Mục tiêu:** tìm yếu tố làm chi phí mỗi việc thành công thay đổi nhiều nhất, để biết pilot phải theo dõi gì.
- **Cần làm:** ở dòng `TODO CP2` trong `src/lab13.py`, gọi lại `mo_hinh` cho 9 kịch bản đổi từng yếu tố (B1), một kịch bản đổi một cặp (B2), giới hạn 1, 2, 3 lần chạy và tính chi phí cả hệ thống (B3), kịch bản xem lại 100% cho `noi_dia` + `hang_nang` (B4). Điền vào `report/team/bang_chi_phi.md`.
- **Sản phẩm:** bảng B1 đủ 9 dòng; xếp hạng ba yếu tố ảnh hưởng mạnh nhất; câu trả lời B3 và B4, mỗi câu không quá ba dòng và có số.
- **Cần hiểu:** vì sao mô hình cộng tuyến tính nên tác động của một cặp bằng tổng hai tác động riêng; vì sao giới hạn rẻ nhất cho công ty có thể khác giới hạn cho chi phí mỗi việc thành công thấp nhất.
- **Tự kiểm tra:** mỗi kịch bản "giảm một nửa" làm chi phí giảm đúng bằng nửa mức tăng của kịch bản "gấp đôi" tương ứng.

## CP3 — Bảng lỗi và cách khắc phục (15:35 → 16:08, nhiệm vụ C)

- **Mục tiêu:** gắn nhãn 20 ca lỗi theo năm loại của Google PAIR, đạt đồng thuận từ 80%, rồi gán cách khắc phục cho từng loại.
- **Cần làm:** 20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` (mục "Hai mươi ca lỗi"). Hai người gắn nhãn ngồi tách nhau, gắn độc lập cả 20 ca trong 8 phút, không trao đổi; hai người còn lại hoàn thiện CP2. So nhãn, tính tỉ lệ đồng thuận; với ca không trùng, thống nhất nhãn và ghi một câu quy tắc phân biệt. Chọn 5 ca, mỗi loại một ca, điền bảng khắc phục trong `report/team/bang_loi.md`.
- **Sản phẩm:** `report/team/bang_loi.md` có hai bộ nhãn độc lập, tỉ lệ đồng thuận, quy tắc cho các ca không trùng, bảng khắc phục 5 ca đủ năm loại.
- **Cần hiểu:** gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa; khác nhau giữa lỗi hệ thống (đã lộ ra) và lỗi ngầm (không ai nhận ra cho tới khi kiểm tra).
- **Tự kiểm tra:** đồng thuận từ 16/20 ca, nếu thấp hơn thì đã viết lại định nghĩa trước khi đi tiếp; mỗi dòng khắc phục có cách phát hiện đo được (event, ngưỡng, tần suất) và một vai trò phụ trách, không ghi "cả đội".

## CP4 — pilot_plan.yaml (16:08 → 16:36, nhiệm vụ D)

- **Mục tiêu:** một kế hoạch pilot tách được tác động của trợ lý và đủ cỡ mẫu, có điều kiện dừng viết trước.
- **Cần làm:** ở dòng `TODO CP4` trong `src/lab13.py`, tính năm câu D1 (cỡ mẫu theo yêu cầu, theo nhân viên, theo depot, mức chênh 6 điểm) rồi mới chọn cách chia; trả lời năm câu D2 "tách được tác động"; tính tỉ lệ `mo_lai_trong_7_ngay` hiện tại trước khi đặt luật an toàn; điền mọi dấu `?` trong `report/team/pilot_plan.yaml`. Ghi kết quả D1 và D2 vào phần chú thích đầu file.
- **Sản phẩm:** `report/team/pilot_plan.yaml` không còn dấu `?`, có ít nhất ba luật dừng (an toàn, chi phí, mức độ sử dụng) theo mẫu NẾU – TRONG – THÌ – KHÔNG THÌ.
- **Cần hiểu:** hệ số thiết kế và cỡ mẫu hiệu dụng khi chia theo cụm; vì sao số cụm quyết định chứ không phải tổng số yêu cầu; đánh đổi nhóm chấp nhận nếu cách chia chưa đủ mẫu.
- **Tự kiểm tra:** `python -c "import yaml; yaml.safe_load(open('../report/team/pilot_plan.yaml'))"` chạy không lỗi; `grep -v '^ *#' ../report/team/pilot_plan.yaml | grep -n '?'` không in gì (không còn dấu `?` ngoài dòng chú thích); cách chia đã chọn có ít nhất 20 cụm mỗi nhóm hoặc ghi rõ đánh đổi.

## CP5 — Chỉ số, rủi ro, hồ sơ launch v0 và duyệt chéo Gate 2a (16:36 → 18:00, nhiệm vụ E)

- **Mục tiêu:** ghép bốn nhiệm vụ trước thành một trang để hội đồng ra quyết định, rồi bảo vệ trước nhóm khác và chấm một nhóm khác.
- **Cần làm:** tính thử ba chỉ số (chính, dùng, an toàn), đề xuất thêm một chỉ số dùng và một chỉ số an toàn, liệt kê ít nhất sáu event có `trace_id`, thêm ít nhất hai dòng rủi ro kinh tế lấy số từ bảng độ nhạy, tất cả trong `report/team/chi_so.md`. Điền `report/team/ho_so_launch_v0.md` (người giữ hồ sơ điền dần từ đầu buổi). 17:00 gửi hồ sơ cho nhóm hội đồng; nhóm n chấm nhóm n + 1 (nhóm cuối chấm nhóm 1) vào `report/team/phieu_cham.md`. 17:45 điền `report/team/group_report.md`, báo cáo cá nhân, commit và push.
- **Sản phẩm:** `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md` (một trang, bảy mục, dòng cuối là đề xuất), `report/team/phieu_cham.md`.
- **Cần hiểu:** chỉ số nào không tính được từ danh sách event thì chưa đo được; vì sao chỉ được viết "chỉ số trong đợt chạy thử là…" chứ không viết "trợ lý đã nâng chỉ số"; vì sao một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.
- **Tự kiểm tra:** mỗi mục hồ sơ có con số chính, trạng thái (Xong, có bằng chứng · Chưa · Giả lập) và người phụ trách là một vai trò; đề xuất là một trong ba: Go, Go có điều kiện, No-go; `grep -rni production ../report/team` không in gì.
