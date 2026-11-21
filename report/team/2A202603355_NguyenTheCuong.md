# Báo cáo cá nhân — HoVaTen-MSSV

## 1. Thông tin thành viên

- Họ tên: <Nguyễn Thế Cường>
- MSSV: <2A202603355>
- Email: <26ai.cuongnt2@vinuni.edu.vn>
- Vai trong nhóm: người viết code (nhiệm vụ A, B); sau giải lao kiểm số D1 cho người viết code mới

## 2. Phần việc phụ trách

- Nhiệm vụ A (CP1): ba hàm A1, hàm `mo_hinh()` (A2), tách theo loại yêu cầu (A3), chi phí cố định (A4) trong `src/lab13.py`.
- Nhiệm vụ B (CP2): bảng độ nhạy 9 kịch bản (B1), đổi cặp và xếp hạng (B2), giới hạn số lần chạy (B3), xem lại 100% (B4).
- Điền toàn bộ `report/team/bang_chi_phi.md` (A1–A4, B1–B4).
- Kiểm chéo câu e của D1 cho người viết code phần D.

## 3. Đóng góp cụ thể

- Viết `mo_hinh()` nhận sẵn tham số giá, hệ số và `max_lan_chay`, để A3, A4, B1–B4 chỉ cần gọi lại hàm này; hàm tự lọc lần chạy theo `request_id` nên tách theo loại không phải lọc tay.
- Tính chi phí mỗi việc thành công **4.472 đ** [simulated], gấp **16,3 lần** hoá đơn token chia số yêu cầu; làm lại chiếm 51,8%, xem lại 40,7% [simulated].
- Chỉ ra quoc_te không đáng để trợ lý xử lý: **1,88×** của 12.000 đ [simulated], tỉ lệ ok giảm 30% → 11,4% → 2,2% qua ba lần thử, nên phạm vi pilot là noi_dia + hang_nang.
- A4: cộng chi phí cố định cho phạm vi pilot: 4.599 đ = 0,38× ở 45.000 yêu cầu/tháng, 5.784 đ = 0,48× khi khối lượng còn một nửa [simulated].
- Xếp hạng độ nhạy: 1. số ca làm lại (+51,8%) · 2. tỉ lệ xem lại (+40,7%) · 3. lương (+23,1%) [simulated]; giá token chỉ +5,6%.
- B3: giới hạn 2 lần rẻ nhất cho công ty (6.901.220 đ [simulated]), khác giới hạn 1 lần có chi phí mỗi việc thành công thấp nhất; giới hạn 1 lần đẩy thêm 85 yêu cầu sang nhân viên.
- B4: xem lại 100% cho 11.743 đ = 0,98× (12.415 đ = 1,03× nếu làm lại 15,3 phút như dữ liệu) [simulated]; hoà vốn khi mỗi lần xem lại ≤ 5,1 phút.
- Kiểm chéo D1 câu e: n = 859 mỗi nhóm ở mức chênh 6 điểm, m ≥ 299 yêu cầu mỗi nhân viên, hệ số thiết kế 6,96; power ở mức 5 điểm chỉ 0,64.

## 4. Bằng chứng

- Commit trên nhánh `ntc`:
  - `28695bd` CP1: A1-A4 mô hình chi phí mỗi việc thành công
  - `b81ec83` CP1: A1-A4 mô hình chi phí và bảng chi phí phần A
  - `5e444db` CP2: B1-B4 bảng độ nhạy và bảng chi phí phần B
- File: `src/lab13.py` (phần A1, A2, A3, A4, B1–B4), `report/team/bang_chi_phi.md`.
- `cd src && python lab13.py` in `Ba phép thử đáp án biết trước: ĐẠT` và đủ các bảng A2, A3, A4, B1–B4.

## 5. Công cụ AI đã dùng

- **Claude Code (Claude, Anthropic)**, dùng trong VS Code: đọc đề và hướng dẫn, gợi ý cách chia việc cho nhóm, viết code A1–A4 và B1–B4 theo từng phần nhỏ, điền bảng `bang_chi_phi.md`. Tôi review từng phần trước khi cho làm phần tiếp theo.
- **Cách tự kiểm tra:**
  - A1: ba phép thử `assert` trong code (1,20 · 1,25 · 1,25), đối chiếu tay: 1 + 0,2 = 1,20; 1,24 ÷ 0,992 = 1,25.
  - A2: tính lại tổng token trực tiếp từ CSV bằng một dòng pandas riêng, không qua `mo_hinh`: ra 245.585 đ, khớp.
  - A3: `pd.crosstab(loai, ket_qua)` cho 783 + 117 + 41 + 37 = 978 việc thành công, khớp A2; 148 + 74 = 222 ca không thành công.
  - A4, B3, B4: tính lại tổng chi phí phạm vi (3.072.513 đ, 900 việc), ba dòng giới hạn chạy và kịch bản xem lại 100% (948 yêu cầu, 48 ca, 11.743 đ) bằng lệnh pandas độc lập; đều khớp.
  - B1, B2: tính tay bảy kịch bản từ các khoản A2 (ví dụ (4.373.585 + 245.585) ÷ 978 = 4.723 đ); "giảm một nửa" đúng bằng nửa mức tăng của "gấp đôi"; cặp đổi +46,3% = 5,6% + 40,7%.
  - Mọi số đều đối chiếu với số trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`, lệch không quá 2% (B4 với 15,3 phút: 12.415 đ so với 12.414 đ do làm tròn).
- Không dùng AI để bịa số: mọi con số trong bảng do `src/lab13.py` in ra hoặc tính tay có ghi cách tính.

## 6. Tự đánh giá

**Làm tốt**

- Hoàn thành đủ A1–A4 và B1–B4; mọi số khớp đáp án trong sai số 2%, mọi số tính từ cột `_simulated` có nhãn `simulated`.
- Không tin ngay số do code in ra: mỗi phần đều có một phép kiểm chéo độc lập (lệnh pandas riêng hoặc tính tay), nên chắc chắn được A2–B4 đúng trước khi gửi số cho nhóm.
- Viết `mo_hinh()` một lần, nhận đủ tham số, nên B1–B4 chỉ là gọi lại hàm, ít chỗ sai.

**Chưa tốt**

- Xếp hạng độ nhạy ở B2 so các kịch bản theo mức đề cho (gấp đôi so với +25% lương), chưa cùng một thước đo; nếu cùng +25% thì lương ảnh hưởng mạnh nhất. Tôi đã ghi nhận điểm này nhưng chưa đưa vào bảng.
- Không tham gia gắn nhãn ở nhiệm vụ C (đúng phân vai), nên hiểu phần bảng lỗi ít hơn phần chi phí.

**Tự giải thích được khi hội đồng hỏi**

- Vì sao tử số tính mọi lần chạy còn mẫu số chỉ đếm việc thành công: lần chạy lỗi vẫn tốn token và tool thật, còn công ty chỉ nhận giá trị từ việc thành công; chia cho 1.200 sẽ làm chi phí trông rẻ hơn thực tế (274,7 đ so với 4.472 đ [simulated]).
- Vì sao không so thẳng 4.472 đ với 12.000 đ: còn 222 ca nhân viên làm thay; chi phí cả hệ thống là 5.865 đ/yêu cầu = 0,49× [simulated].
- Vì sao giới hạn chạy rẻ nhất cho công ty (2 lần) khác giới hạn có chi phí mỗi việc thành công thấp nhất (1 lần): giới hạn 1 lần bỏ qua ca khó, đẩy thêm 85 việc sang nhân viên.
- Vì sao cặp đổi bằng tổng hai tác động riêng: mô hình chỉ cộng các khoản, không có khoản nào nhân với nhau.
- Vì sao xem lại 100% gần như không tiết kiệm: tiền xem lại chiếm khoảng 90% chi phí, đưa lên 0,98× (1,03× nếu làm lại 15,3 phút) [simulated].
