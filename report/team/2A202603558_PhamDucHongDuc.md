# Báo cáo cá nhân — Phạm Đức Hồng Đức — 2A202603558

## 1. Thông tin thành viên

- Họ tên: Phạm Đức Hồng Đức.
- MSSV: 2A202603558.
- Email: Phamduchongduc15@gmail.com.
- GitHub: DucPham1501.
- Nhóm: Stech · Lớp: L3A.
- Vai trong nhóm: Người gắn nhãn 1, phần phụ CP3; hỗ trợ bảng khắc phục và review hồ sơ.

## 2. Phần việc phụ trách

- Đọc 20 ca lỗi và năm định nghĩa theo Google PAIR trong đề bài.
- Chuẩn bị bộ nhãn người 1 cho 20 ca, giải thích lựa chọn theo nguyên nhân gốc.
- Đối chiếu với bộ nhãn của Bùi Lê Công Tuấn, tính đồng thuận và hoàn thiện `bang_loi.md`.
- Hỗ trợ rà soát bảng khắc phục năm loại lỗi, mỗi dòng có cách phát hiện đo được và một vai trò chịu trách nhiệm.
- Hỗ trợ kiểm tra sự nhất quán của số liệu trong hồ sơ khi nhóm yêu cầu.

## 3. Đóng góp cụ thể

- **Chuẩn bị CP3:** tạo tài liệu [tóm tắt chuẩn bị gắn nhãn](../../docs/tom_tat_chuan_bi_gan_nhan_CP3.md), gồm định nghĩa năm loại lỗi, điểm dễ nhầm và tóm tắt đủ 20 tình huống; giữ nguyên số ca để đối chiếu với đề.
- **Nhãn người 1:** tự gắn nhãn độc lập đủ 20 ca, không trao đổi và không xem bộ nhãn của Tuấn trước khi chốt kết quả. Phân bố: Do người dùng 4 ca, Hệ thống 5 ca, Ngữ cảnh 4 ca, Giới hạn hệ thống 4 ca, Ngầm 3 ca.
- **Đối chiếu:** giữ nguyên bộ nhãn của Tuấn ở cột người 2; so sánh được 20/20 ca trùng, tương ứng 100%, và điền nhãn chung vào cột thống nhất. Không có ca bất đồng. Con số này chỉ đo độ trùng hai bộ nhãn, chưa phải độ đúng so với đáp án giảng viên.
- **Bảng khắc phục:** rà soát và bổ sung cách đo cho các ca 9, 7, 18, 4, 17, đủ năm loại lỗi. Làm rõ event, ngưỡng, tần suất, mẫu số và vai trò phụ trách; ghi rõ các ngưỡng là đề xuất cho pilot. Bảng ban đầu do Tuấn chuẩn bị, phần đóng góp của tôi là hoàn thiện và làm rõ cách giám sát.
- **Hỗ trợ kiểm số B4:** dùng trợ lý đọc hai CSV để phân biệt 982 yêu cầu `noi_dia + hang_nang`, 948 yêu cầu có ít nhất một lần chạy `ok`, 34 yêu cầu không có lần `ok` và 900 yêu cầu có kết quả cuối `thanh_cong`. Tiền xem lại B4 dùng 948 × 5 × 2.000 = 9.480.000 đ [simulated]; token/tool tính trên mọi lần chạy của 982 yêu cầu.

## 4. Bằng chứng

- Nhánh công việc: `feat/cp3-error-labeling`.
- [Bảng lỗi và khắc phục](bang_loi.md): 20 nhãn người 1, hai cột đối chiếu, tỉ lệ đồng thuận và năm dòng khắc phục.
- [Tài liệu chuẩn bị](../../docs/tom_tat_chuan_bi_gan_nhan_CP3.md): năm định nghĩa và 20 tình huống tóm tắt từ đề gốc.
- Dữ liệu kiểm số: `src/logix_requests.csv` và `src/logix_runs.csv`; tài liệu đối chiếu B4: `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`.
- Kiểm tra bằng công cụ: đủ 20 hàng nhãn, hai nhãn và nhãn thống nhất khớp nhau, `bang_loi.md` không còn placeholder; `git diff --check` không báo lỗi khoảng trắng.

## 5. Công cụ AI đã dùng

- Sử dụng **ChatGPT/Codex** để đọc nội dung Word, tóm tắt các tình huống; hỗ trợ sửa Markdown và kiểm số từ CSV. Bộ nhãn người 1 được tự chốt trước khi xem bộ nhãn người 2.
- Kiểm số với AI hỗ trợ: đếm yêu cầu duy nhất theo `request_id`, phân biệt `status = ok` ở mức lần chạy với `ket_qua = thanh_cong` ở mức yêu cầu.

## 6. Tự đánh giá

- Hoàn thiện hồ sơ CP3 về nội dung: đủ 20 ca, có kết quả đối chiếu và bảng khắc phục đủ năm loại lỗi. Hiểu rõ việc gắn nhãn phải dựa trên nguyên nhân gốc và cách nhận biết sai sót đã lộ ra so với lỗi ngầm.
- Hạn chế: cần tự đọc lại các lý do và giải thích được khi giảng viên hỏi. Đồng thuận 100% chưa thay thế việc kiểm tra với đáp án giảng viên.
- Phần phối hợp tiếp theo: tiếp tục hỗ trợ Tuấn review `pilot_plan.yaml` và hồ sơ launch v0 sau khi nhóm ghép đầy đủ các phần.
