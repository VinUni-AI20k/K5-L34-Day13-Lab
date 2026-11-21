# Báo cáo cá nhân — MaiTuAnAnh-2A202603574

## 1. Thông tin thành viên

- Họ tên: Mai Tuấn Anh
- MSSV: 2A202603574
- Email: 
- Vai trong nhóm: Người gắn nhãn 1 (thành viên thứ 3)

## 2. Phần việc phụ trách

- Nhiệm vụ C (CP3 · Bảng lỗi và cách khắc phục): Đọc đề bài, nghiên cứu 20 ca lỗi từ tài liệu `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`.
- Thực hiện gắn nhãn độc lập cả 20 ca lỗi vào 5 loại lỗi theo chuẩn Google PAIR trong 8 phút, không trao đổi với người gắn nhãn 2.
- Theo dõi các điều kiện nghiệm thu "Xong khi" của nhiệm vụ C (tỉ lệ đồng thuận >= 80%, quy tắc phân biệt, phát hiện đo được và vai trò phụ trách).
- Chuẩn bị cơ sở lý luận, câu hỏi nhận diện và quy tắc phân biệt cho các ca dễ nhầm lẫn để đối chiếu và thống nhất với người gắn nhãn 2.

## 3. Đóng góp cụ thể

- Hoàn thành độc lập bộ nhãn thứ nhất (cột "Nhãn người 1") cho toàn bộ 20 ca lỗi trong `report/team/bang_loi.md`:
  + **Do người dùng** (4 ca): Ca 1, Ca 6, Ca 9, Ca 14.
  + **Hệ thống** (5 ca): Ca 2, Ca 7, Ca 8, Ca 15, Ca 20.
  + **Ngữ cảnh** (4 ca): Ca 3, Ca 10, Ca 16, Ca 18.
  + **Giới hạn hệ thống** (4 ca): Ca 4, Ca 11, Ca 13, Ca 19.
  + **Ngầm** (3 ca): Ca 5, Ca 12, Ca 17.
- Phân tích nguyên nhân gốc (root cause) thay vì chỗ cần sửa cho từng ca lỗi theo đúng câu hỏi nhận biết của Google PAIR:
  + Ca 6, 9: Do người dùng nhập/chọn sai, việc trợ lý thiếu gợi ý thuộc phần giải pháp khắc phục.
  + Ca 8, 15: Lỗi hệ thống do vi phạm chính sách/dẫn sai điều khoản và lỗi đã lộ ra (hoặc nhân viên bắt được), không phải lỗi ngầm.
  + Ca 12: Lỗi ngầm vì câu trả lời bề ngoài vẫn đúng nhưng chi phí token nhân 3 âm thầm suốt 3 tuần không ai phát hiện cho đến khi rà soát.
  + Ca 13: Giới hạn hệ thống vì nằm ngoài phạm vi xử lý (sản phẩm bảo hiểm đối tác).
  + Ca 18: Lỗi ngữ cảnh vì số tiền hoàn đúng chính sách, chỉ giả định "khách tự hiểu cách tính" là không khớp hoàn cảnh khách hàng.

## 4. Bằng chứng

- File [bang_loi.md](file:///c:/Users/Admin/OneDrive/Documents/K5-L3A-DAY13-Soopi-LaunchEconomics/report/team/bang_loi.md): Đã điền đầy đủ 20 nhãn độc lập tại cột **Nhãn người 1**.
- Danh sách phân loại 20 ca lỗi kèm giải thích nguyên nhân gốc và câu hỏi đối chiếu Google PAIR.

## 5. Công cụ AI đã dùng

- Công cụ: Trợ lý AI (Antigravity)
- Mục đích: Hỗ trợ đọc nhanh đề bài `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`, hệ thống hóa 5 loại lỗi Google PAIR (Do người dùng, Hệ thống, Ngữ cảnh, Giới hạn hệ thống, Ngầm) và rà soát các trường hợp biên.
- Tự kiểm tra: Tự đọc hiểu, phân tích bản chất từng ca theo nguyên tắc "gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa", phân biệt rõ ràng giữa lỗi hệ thống (sai sót đã lộ diện) và lỗi ngầm (chỉ phát hiện qua kiểm tra định kỳ), đảm bảo tính chính xác và logic.

## 6. Tự đánh giá

- Mức độ hoàn thành: Hoàn thành 100% phần việc được giao ở mốc CP3 (gắn nhãn độc lập bộ nhãn 1 cho 20 ca lỗi).
- Tinh thần làm việc: Nghiêm túc, tuân thủ đúng nguyên tắc gắn nhãn độc lập không trao đổi trước.
