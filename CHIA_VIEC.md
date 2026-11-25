Phụ trách `report/team/bang_loi.md`.

Cần thực hiện đúng quy tắc: hai bộ nhãn phải được thực hiện độc lập trước khi trao đổi.

Các nhóm lỗi gồm:

- Do người dùng.
- Hệ thống.
- Ngữ cảnh.
- Giới hạn hệ thống.
- Lỗi ngầm.

Yêu cầu đầu ra:

- Hai bộ nhãn độc lập cho 20 ca.
- Tỉ lệ đồng thuận tối thiểu `16/20 = 80%`.
- Quy tắc phân biệt các ca dễ nhầm.
- Bảng khắc phục 5 ca, mỗi loại một ca.
- Mỗi dòng phải có:
  - Cách phát hiện đo được.
  - Ngưỡng hoặc tần suất.
  - Cách khắc phục.
  - Một vai trò chịu trách nhiệm cụ thể.

Không ghi người phụ trách là “cả đội”.

### Phần D: Kế hoạch pilot

Phụ trách `report/team/pilot_plan.yaml`.

Cần tính và điền:

- Cỡ mẫu theo yêu cầu: `1.251 yêu cầu mỗi nhóm`.
- Cỡ mẫu theo nhân viên với `m = 75`: khoảng `3.103 mỗi nhóm`.
- Với 20 nhân viên mỗi nhóm: tối đa khoảng `1.000` mẫu hiệu dụng, không đủ cho mức chênh 5 điểm.
- Với 6 depot mỗi nhóm: tối đa khoảng `300` mẫu hiệu dụng.
- Nếu chấp nhận mức chênh 6 điểm: cần khoảng `859` mẫu hiệu dụng mỗi nhóm và khoảng `299` yêu cầu mỗi nhân viên.
- Chọn cách chia theo nhân viên, 20 người mỗi nhóm, và ghi rõ đánh đổi: phát hiện được mức chênh 6 điểm nhưng power chỉ khoảng `0,64` nếu tác động thật sự chỉ là 5 điểm.

### Các điều kiện bắt buộc trong YAML

- Có nhóm đối chứng.
- Phân bổ ngẫu nhiên, có seed.
- Phân tầng theo depot.
- Có ít nhất 20 cụm mỗi nhóm.
- Có các trường `identifiability`, `interim_looks`, `simulated_inputs`.
- Không còn dấu `?` ngoài chú thích.
- Có ít nhất 3 luật dừng theo mẫu:

`NẾU – TRONG – THÌ – KHÔNG THÌ`

Nên kiểm tra thêm:

- Tỉ lệ mở lại hiện tại: `4,25%`.
- Không đặt ngưỡng an toàn thấp đến mức pilot dừng ngay trong tuần đầu.
- Có người có quyền dừng, ví dụ Giám đốc vận hành.

---

## Người 3 — Chỉ số, hồ sơ launch và tổng hợp

### Phần E: Chỉ số và rủi ro

Phụ trách `report/team/chi_so.md`.

Cần ghi:

- Chỉ số chính:
  - Đóng trong 24 giờ và không mở lại trong 7 ngày.
  - Kết quả tham khảo: `82,83%`, tức `994/1.200`.
- Chỉ số sử dụng:
  - Tỉ lệ bỏ qua gợi ý.
  - Kết quả tham khảo: `27,12%`, tức `48/177`.
- Chỉ số an toàn:
  - Tỉ lệ mở lại trong 7 ngày.
  - Kết quả tham khảo: `4,25%`, tức `51/1.200`.
- Đề xuất thêm một chỉ số sử dụng và một chỉ số an toàn.
- Ít nhất 6 event có `trace_id`, nên sử dụng các event như:
  - `refund_request_created`
  - `agent_run_completed`
  - `agent_suggestion_shown`
  - `staff_review_decision`
- `staff_rework_completed`
  - `refund_ledger_write`
  - `handoff_to_staff`
  - `ticket_closed`
  - `ticket_reopened`
  - `audit_sample_checked`
- Ít nhất 2 rủi ro kinh tế lấy trực tiếp từ bảng độ nhạy, ví dụ:
  - Số ca làm lại tăng gấp đôi làm chi phí tăng `51,8%`, lên khoảng `6.787 đ`.
  - Xem lại 100% có thể làm chi phí lên `11.743 đ`, hoặc `12.414 đ` nếu thời gian làm lại theo dữ liệu thực tế.
  - Khối lượng thấp làm chi phí cố định tăng thêm khoảng `2.370 đ/việc`.

Lưu ý không viết “trợ lý đã nâng chỉ số”, vì dữ liệu chưa có nhóm đối chứng. Chỉ viết “chỉ số trong đợt chạy thử là…”.

### Hồ sơ launch v0

Phụ trách `report/team/ho_so_launch_v0.md`.

Hồ sơ cần có 7 mục:

1. Chi phí mỗi việc thành công.
2. Ba yếu tố nhạy nhất.
3. So sánh với nhân viên tự làm.
4. Chỉ số chính, chỉ số sử dụng và chỉ số an toàn.
5. Bảng lỗi và cách khắc phục.
6. Kế hoạch pilot.
7. Rủi ro kinh tế.

Mỗi mục phải có:

- Con số chính.
- Trạng thái: `Xong, có bằng chứng`, `Chưa` hoặc `Giả lập`.
- Một vai trò phụ trách.

Đề xuất cuối nên là:

**Go có điều kiện** cho phạm vi `noi_dia + hang_nang`.

Các điều kiện nên nêu:

- Sửa lỗi chống trùng và đối soát sổ cái.
- Được Giám đốc vận hành chấp nhận mức chênh 6 điểm.
- Bật đầy đủ event có `trace_id`.
- Thay số phút `simulated` bằng số đo thật sau tuần đầu.
- Có kế hoạch giảm tỉ lệ xem lại.

### Tổng hợp

Người 3 cũng nên phụ trách:

- `report/team/group_report.md`.
- Kiểm tra các file có thống nhất số liệu hay không.
- Kiểm tra nhãn `simulated`.
- Tổng hợp đóng góp của từng người.
- Chuẩn bị nội dung báo cáo và đề xuất cuối.

---

## Công việc chung của cả 3 người

### Đầu buổi

- Điền `TEAM.md`.
- Chia vai trò rõ ràng.
- Cài môi trường Python.
- Chạy thử `src/lab13.py`.
- Kiểm tra không sửa hai file dữ liệu CSV.

### Trước 17:00

- Hoàn thiện `ho_so_launch_v0.md`.
- Gửi hồ sơ cho nhóm được phân công chấm.
- Kiểm tra đề xuất, phạm vi và các số bất lợi.

### Từ 17:00 đến 17:45

- Cả nhóm đọc hồ sơ nhóm khác.
- Hoàn thiện `phieu_cham.md`.
- Chuẩn bị một câu hỏi phản biện, ví dụ:
  - Chi phí sẽ là bao nhiêu nếu phải xem lại 100%?
  - Nhóm có đủ 20 cụm mỗi bên không?
  - Ngưỡng an toàn có khiến pilot dừng ngay không?

### Trước khi nộp

Kiểm tra lần cuối:

- `python lab13.py` chạy hết.
- Ba phép thử A1 đều đạt.
- Đủ sáu file hồ sơ trong `report/team/`.
- Có báo cáo cá nhân của cả 3 người.
- `pilot_plan.yaml` đọc được bằng `yaml.safe_load`.
- Không còn dấu `?` ngoài chú thích.
- Mọi số lấy từ cột `_simulated` đều có nhãn `simulated`.
- Không dùng từ `production`.
- Không ghi người phụ trách là “cả đội”.
- Đề xuất là một trong ba dạng: `Go`, `Go có điều kiện`, `No-go`.
- Đã commit và push.
- Mỗi thành viên tự nộp link repo trên LMS.

## Thứ tự phối hợp nên dùng

Người 1 hoàn thành các số liệu A–B trước vì người 2 và người 3 cần dùng các số này. Trong lúc đó, người 2 có thể làm độc lập phần phân loại 20 lỗi. Người 3 bắt đầu dựng khung hồ sơ và danh sách event, sau đó cập nhật số liệu từ người 1 và kế hoạch pilot từ người 2.

Luồng phụ thuộc nên là:

`Người 1: A–B → Người 3: rủi ro và hồ sơ`

`Người 2: C–D → Người 3: pilot plan và hồ sơ`

`Cả 3 người → kiểm tra chéo → commit/push/nộp bài`
