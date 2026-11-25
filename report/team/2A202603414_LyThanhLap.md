# Báo cáo cá nhân — LyThanhLap-2A202603414

## 1. Thông tin thành viên

- Họ tên: Lý Thành Lập
- MSSV: 2A202603414
- Email:
- Lớp: L3A · Nhóm: Neon
- Vai trong nhóm: Người kiểm số (14:00–15:20), người viết code (từ 15:35). Chủ file `bang_chi_phi.md`, `chi_so.md`, `group_report.md`.

## 2. Phần việc phụ trách

- **CP1–CP2:** kiểm số độc lập cho nhiệm vụ A và B; điền bảng A2, A3, A4, B1, B3; tự kiểm tuyến tính; tính tay B4.
- **CP3–CP4:** viết code D1 (cỡ mẫu theo ba cách chia, mức chênh 6 điểm, power ở 5 điểm) và tính tỉ lệ mở lại 7 ngày cho luật dừng an toàn.
- **CP5:** tính thử 3 chỉ số E1, điền `chi_so.md`.
- **Đóng gói:** điền `group_report.md`, commit và push bản cuối, ghi commit chốt vào `TEAM.md`.

## 3. Đóng góp cụ thể

- **Kiểm số A:** tính lại token (245.585 đ), tool (84.000 đ), 978 việc thành công, chi phí mỗi việc thành công 4.472 đ (`simulated`), hoá đơn 274,7 đ mỗi yêu cầu. Script kiểm số không gọi `mo_hinh`, khớp `src/lab13.py`.
- **Kiểm số B:**
  - 9 kịch bản B1 khớp code.
  - Tự kiểm tuyến tính bằng đồng: token +251,1 / −125,6 đ; xem lại +1.820,0 / −910,0 đ; làm lại +2.314,9 / −1.157,5 đ. Tỉ số = 2,000 ở cả ba cặp.
  - B4 tính tay: 948 × 5 × 2.000 + 48 × 9 × 2.000 + 224.513 = 10.568.513 đ; chia 900 việc thành công = 11.743 đ = 0,98× (`simulated`).
- **Code D1** (`co_mau`, `he_so_thiet_ke`, `m_toi_thieu`, `in_bang_d1`):
  - a) 1.251 mỗi nhóm
  - b) DE 2,48, 3.103 mỗi nhóm, cần 84 người > 40
  - c) tối đa 1.000
  - d) tối đa 300
  - e) m ≥ 299, DE 6,96
  - Power ở 5 điểm: 0,64
- **Dữ liệu cho luật dừng** (`in_ti_le_mo_lai`): mở lại 7 ngày 4,25% toàn mẫu, 3,97% trong phạm vi; khoảng 30,7 yêu cầu mỗi nhân viên mỗi ngày trong phạm vi, nên 299 yêu cầu mỗi người cần khoảng 10 ngày làm việc.
- **E1** (`in_bang_e1`): chính 82,83% (994/1.200), bỏ qua gợi ý 27,12% (48/177), mở lại 4,25% (51/1.200).

## 4. Bằng chứng

- Commit `6558362`, `333975a` và các commit sau đó trên `main`.
- `src/lab13.py`: hàm D1, D3, E1; `python lab13.py` in đủ từ A1 đến E1.
- `report/team/bang_chi_phi.md`: bảng tự kiểm tuyến tính, đoạn "Kiểm số độc lập".
- `report/team/chi_so.md`: bảng E1, 11 event, kiểm tra chéo.

## 5. Công cụ AI đã dùng

- **Claude Code (Claude Opus 5.5):**
  - Đọc slide và tài liệu đề, đề xuất phân công.
  - Viết script kiểm số độc lập cho A và B.
  - Viết các hàm D1, E1 trong `src/lab13.py`.
  - Soạn nháp `pilot_plan.yaml`, `chi_so.md`, mục 4, 6, 7 của hồ sơ và `group_report.md`.
- **Cách tự kiểm tra:**
  - Chạy `python lab13.py`, ba phép thử A1 in ĐẠT.
  - So số của script kiểm số với số của `lab13.py`: lệch dưới 0,01%.
  - Tính tay lại câu D1 e: 20m ≥ 859 × (0,98 + 0,02m) → 2,82m ≥ 841,82 → m ≥ 299.
  - Chạy `yaml.safe_load` cho `pilot_plan.yaml` và lệnh tìm `?` ngoài chú thích.
  - Chạy lệnh grep tìm từ cấm (quy tắc 5 của lab) trong `report/team`, không in gì.

## 6. Tự đánh giá

**Nắm chắc:**

- Tử số tính mọi lần chạy: lần lỗi vẫn tốn token, tool và giờ nhân viên. Mẫu số chỉ đếm việc thành công vì đó là phần công ty nhận được. Kết quả: 4.472 đ, gấp 16,3 lần hoá đơn chia yêu cầu (`simulated`).
- Cỡ mẫu hiệu dụng: n = c × m / DE < c / ICC. Với 20 cụm, trần là 1.000 < 1.251, nên số cụm quyết định chứ không phải tổng số yêu cầu. Tự giải tay câu e: m ≥ 299.
- Go có điều kiện: `noi_dia` + `hang_nang` rẻ hơn nhân viên (0,22×, 0,69×), nhưng còn lỗi ca 7 và ca 20, power 0,64, phút xem lại giả lập, xem lại 100% lên 0,98–1,03×.

**Cần hỏi thêm:**

- Cách ước ICC thật từ dữ liệu tuần đầu. Nếu ICC là 0,05 thì trần chỉ còn 400.
- Ngưỡng an toàn +2 điểm có đủ nhạy ở bước 0.10 (4 nhân viên) không.
