# Báo cáo cá nhân — VoThiPhuongNhung-2A202603918

## 1. Thông tin thành viên

- Họ tên: Võ Thị Phương Nhung
- MSSV: 2A202603918
- Email:
- Vai trong nhóm: Thành viên 1 (Hoàn thiện A1/A2 và kịch bản B1–B4, gắn nhãn độc lập 20 ca CP3, tính D1(a) và kiểm tra chỉ số chính).

## 2. Phần việc phụ trách

- **CP1 · A1, A2:** viết ba hàm kinh tế chạy lại và `mo_hinh(...)` trong `src/lab13.py`.
- **CP2 · B:** bổ sung hàm gọi lại mô hình với giá, hệ số và giới hạn chạy thay đổi; in kết quả B1–B4.
- **CP3:** gắn nhãn độc lập 20 ca lỗi theo năm loại; lưu Bộ nhãn độc lập số 1.
- **CP4 · D1(a):** tính cỡ mẫu theo yêu cầu cho baseline 0,70 và mục tiêu tăng 5 điểm phần trăm.
- **CP5:** tính thử chỉ số chính và diễn đạt kết quả quan sát, không khẳng định quan hệ nhân quả.

## 3. Đóng góp cụ thể

- **A1:** cài đặt các hàm số lần chạy kỳ vọng, tỉ lệ thành công và hệ số chi phí mỗi việc thành công; ba kiểm tra đạt lần lượt **1,20 · 1,25 · 1,25**.
- **A2:** `mo_hinh` cộng token/tool ở mọi lần chạy và chi phí nhân viên từ phút `simulated`; kết quả gồm token **245.585 đ**, tool **84.000 đ**, xem lại **1.780.000 đ [simulated]**, làm lại **2.264.000 đ [simulated]**, **978** việc thành công và **4.472 đ/việc thành công [simulated]**.
- **B1:** in đủ 9 kịch bản độ nhạy. Chi phí/việc thành công chạy từ **3.315 đ** (làm lại giảm một nửa) đến **6.787 đ** (làm lại gấp đôi); ba yếu tố ảnh hưởng mạnh nhất là làm lại, xem lại và lương nhân viên.
- **B2:** token gấp đôi cùng xem lại gấp đôi cho **6.543 đ/việc (+46,3%)**.
- **B3:** chi phí hệ thống thấp nhất khi giới hạn 2 lần chạy: **6.901.220 đ**; giới hạn 1 lần có CPS thấp nhất (**4.111 đ**) nhưng nhiều yêu cầu chuyển cho nhân viên hơn.
- **B4:** trong phạm vi `noi_dia` + `hang_nang`, xem lại 100% cho CPS **11.743 đ** với giả định 9 phút làm lại; dùng 15,3 phút làm lại trung bình `simulated` cho **12.415 đ**.
- **CP3:** Bộ nhãn độc lập số 1 được lưu tại `report/team/tv1_cp3_nhan_da_dien.md`; xem bằng chứng commit `45ce63c`.
- **D1(a):** cỡ mẫu **1.251 yêu cầu mỗi nhóm** (giá trị thô 1.250,716733, làm tròn lên), theo công thức hai tỉ lệ với α = 0,05 và power = 0,80.
- **Chỉ số chính:** **994/1.200 = 82,83%** yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày. Đây là kết quả quan sát của đợt chạy thử, không chứng minh trợ lý làm chỉ số tăng từ baseline 0,70.

## 4. Bằng chứng

- `d601b14` — cập nhật `src/lab13.py`: ba hàm A1 và `mo_hinh(...)`.
- `bddce53` — cập nhật `src/lab13.py`: tính và in các kịch bản B1–B4.
- `5d0f643` — thêm phiếu nhãn CP3 ban đầu; `45ce63c` — lưu Bộ nhãn độc lập số 1 tại `report/team/tv1_cp3_nhan_da_dien.md`.
- Số A1/A2/B1–B4 được kiểm tra bằng `python lab13.py`; D1(a) được tính bằng Python và đối chiếu hướng dẫn. Chỉ số chính được tính trực tiếp từ `src/logix_requests.csv`.
- Các commit nêu trên thuộc nhánh `nhungvo`.

## 5. Công cụ AI đã dùng

- Copilot SDK trong VS Code hỗ trợ hoàn thiện code A1/A2 và B1–B4, tính/kiểm tra D1(a) và chỉ số chính, đồng thời cập nhật khung báo cáo.
- Cách tự kiểm tra: chạy `python lab13.py`, đối chiếu kết quả A1/A2/B với số tham chiếu trong hướng dẫn, kiểm tra công thức D1(a), và tự chạy phép tính 994/1.200 từ dữ liệu.
- Nội dung nhãn CP3 được ghi nhận theo file và commit nêu ở mục 4; cần bảo đảm việc gắn nhãn được thực hiện độc lập theo quy định nhóm.

## 6. Tự đánh giá

- Đã có bằng chứng cho phần code A1/A2, kịch bản B, kết quả D1(a), chỉ số chính và file bàn giao CP3.
- Trước khi nộp, xác nhận email, vai trò thực tế, quy trình gắn nhãn CP3 và các kết quả đã tự giải thích được; đặc biệt phân biệt kết quả pilot quan sát với tác động nhân quả.
