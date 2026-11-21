# Báo cáo cá nhân — HoAnhDung-ITCSIU21172

## 1. Thông tin thành viên
- **Họ tên:** Hồ Anh Dũng
- **MSSV:** ITCSIU21172
- **Email:** 118713346+ITCSIU21172@users.noreply.github.com
- **Vai trong nhóm:** Người 1 — Người viết code chính (nửa đầu buổi) kiêm phụ trách đặc tả chỉ số & event tracking

## 2. Phần việc phụ trách
- **CP1 – Nhiệm vụ A (A1, A2, A3):** Viết ba hàm tính toán kinh tế chạy lại trong `src/lab13.py` đạt 100% kiểm thử đáp án biết trước; xây dựng hàm mô hình chi phí `mo_hinh(runs, reqs, ...)` từ dữ liệu trace và bóc tách theo từng loại yêu cầu để cung cấp số liệu gốc cho Người 2 điền bảng.
- **CP2 – Nhiệm vụ B (B1, B2, B3, B4):** Lập trình tính toán 9 kịch bản phân tích độ nhạy, kịch bản thay đổi một cặp yếu tố, tối ưu giới hạn số lần chạy trên toàn hệ thống và kịch bản xem lại 100% phạm vi `noi_dia` + `hang_nang`.
- **CP5 – Nhiệm vụ E (E1, E2):** Thiết kế đặc tả các chỉ số đo lường (chính, sử dụng, an toàn), đề xuất 2 chỉ số mới, thiết kế danh mục 10 sự kiện (event tracking) chuẩn hóa có `trace_id` và phân tích rủi ro kinh tế trong `report/team/chi_so.md`.
- **Hỗ trợ kỹ thuật Git:** Hợp nhất mã nguồn với phần code CP4 của Người 2, giải quyết xung đột (conflict) mượt mà và đảm bảo toàn bộ mã nguồn nhóm chạy thông suốt.

## 3. Đóng góp cụ thể
- **Hoàn thành 3 hàm cốt lõi A1:** Cài đặt chính xác công thức toán học cho `so_lan_chay_ky_vong(p, k)`, `ti_le_thanh_cong(p, k)` và `he_so_chi_phi_moi_viec_thanh_cong(p, k)`. Chạy hàm `kiem_tra_dap_an_biet_truoc()` đạt tuyệt đối cả 3 test case (1,20 · 1,25 · 1,25).
- **Xây dựng mô hình chi phí A2 & bóc tách A3:**
  - Tính chính xác tổng chi phí thực tế: **4.373.585 đ** cho 978 việc thành công $\rightarrow$ Chi phí mỗi việc thành công (CPS): **4.472 đ [simulated]**, gấp **16,3 lần** hoá đơn token + tool (274,7 đ).
  - Tách theo loại yêu cầu: chỉ rõ `quoc_te` đắt gấp 1,88× nhân viên tự làm (22.515 đ) và tỉ lệ thành công chỉ 27,3%, chạy lại không hiệu quả (lần 3 chỉ đúng 2,2%) nên đề xuất loại khỏi pilot.
- **Lập trình phân tích độ nhạy B1–B4:**
  - B1: Chạy 9 kịch bản chứng minh tính cộng tuyến tính (giảm một nửa giảm đúng 1/2 mức tăng gấp đôi).
  - B2: Xác định xếp hạng 3 yếu tố nhạy nhất: 1. Số ca làm lại (+51,8%) · 2. Tỉ lệ xem lại (+40,7%) · 3. Lương nhân viên (+23,1%).
  - B3: Chứng minh giới hạn 2 lần chạy là tối ưu nhất cho toàn công ty (**6.901.220 đ**), rẻ hơn giới hạn 1 lần (7.449.781 đ) và 3 lần (7.037.585 đ).
  - B4: Tính toán kịch bản xem lại 100% cho thấy chi phí lên tới 11.743 đ (0,98×) đến 12.415 đ (1,03×), chỉ ra điều then chốt pilot phải học là cách giảm tỉ lệ xem lại an toàn.
- **Hoàn thiện đặc tả chỉ số và tracking E1 trong `chi_so.md`:**
  - Tính toán thực tế trên 1.200 yêu cầu: Chỉ số chính (82,83%), chỉ số sử dụng (27,12%), chỉ số an toàn (4,25%).
  - Thiết kế bảng 10 event có thuộc tính `trace_id` gắn kết xuyên suốt toàn bộ vòng đời yêu cầu (từ app khách hàng $\rightarrow$ agent $\rightarrow$ duyệt CSKH $\rightarrow$ làm lại $\rightarrow$ sổ cái $\rightarrow$ đối soát kiểm toán).
  - Đối chiếu logic đo lường: đảm bảo 100% chỉ số đều có event tương ứng để tính toán.

## 4. Bằng chứng
- File mã nguồn [src/lab13.py](file:///c:/Users/THINKPAD/Documents/K5-L3A-DAY13-Soopi-LaunchEconomics/src/lab13.py): Đầy đủ code sạch, chạy thông suốt từ CP1 đến CP4, in ra kết quả khớp 100% với đáp án hướng dẫn.
- File đặc tả [report/team/chi_so.md](file:///c:/Users/THINKPAD/Documents/K5-L3A-DAY13-Soopi-LaunchEconomics/report/team/chi_so.md): Hoàn chỉnh toàn bộ bảng chỉ số, 10 event tracking có `trace_id` và 3 kịch bản rủi ro kinh tế.
- Kết quả chạy kiểm thử trên máy:
  ```text
  === A1: BA PHÉP THỬ ĐÁP ÁN BIẾT TRƯỚC ===
  Ba phép thử đáp án biết trước: ĐẠT
  === A2: MÔ HÌNH CHI PHÍ TỪ TRACE ===
  tong              4,373,585.13
  thanh_cong              978.00
  cps                   4,471.97
  Chi phí mỗi việc thành công gấp: 16.3 lần hoá đơn/yc
  ```

## 5. Công cụ AI đã dùng
- **Công cụ:** Antigravity AI Assistant.
- **Mục đích:** Hỗ trợ tính toán nhanh các công thức xác suất kỳ vọng của việc chạy lại (A1), thiết kế khung mô hình chi phí tối ưu hiệu năng trên pandas DataFrame và chuẩn hóa bộ 10 event tracking theo mô hình quan sát phân tán (trace-based observability).
- **Tự kiểm tra:** Tự tay chạy kiểm thử `kiem_tra_dap_an_biet_truoc()`, rà soát từng dòng mã nguồn, đối chiếu số liệu độ nhạy và xử lý xung đột Git độc lập trên máy local trước khi tích hợp vào nhánh nhóm.

## 6. Tự đánh giá
- **Mức độ hoàn thành:** 100% các nhiệm vụ được phân công trong bảng phân vai (CP1-A1, CP2-B, CP5-E1, E2).
- **Tinh thần làm việc:** Hoàn thành sớm phần việc để cung cấp số liệu kịp thời cho Người 2 và Người 4; chủ động phối hợp đồng bộ và giải quyết xung đột mã nguồn chung của nhóm.
