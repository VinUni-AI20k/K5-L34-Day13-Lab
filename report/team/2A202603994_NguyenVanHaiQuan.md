# Báo cáo cá nhân — NguyenVanHaiQuan-2A202603994

## 1. Thông tin thành viên

- Họ tên: Nguyễn Văn Hải Quân
- MSSV: 2A202603994
- Email: <nguyenhaiquan.data@gmail.com>
- Vai trong nhóm: người viết code, kiêm người kiểm số (Data & Stats Dev)

## 2. Phần việc phụ trách

- Sở hữu `report/team/bang_chi_phi.md`: bảng A1–A4 và B1–B4.
- Kiểm số độc lập cho nhiệm vụ A và B, đối chiếu với `src/lab13.py` của trưởng nhóm.
- Tính và kiểm chứng cỡ mẫu D1 bằng công thức và `statsmodels.NormalIndPower`, quy đổi ra thời lượng pilot, bàn giao cho người giữ hồ sơ điền `pilot_plan.yaml`.
- Viết phần rủi ro kinh tế (E2), bàn giao cho người phụ trách `chi_so.md`.

## 3. Đóng góp cụ thể

- Tính lại toàn bộ A2 từ trace: 4.472 đ mỗi việc thành công, gấp 16,3 lần hoá đơn 274,7 đ/yêu cầu [simulated]. Chỉ ra giờ nhân viên chiếm 92,5% tổng chi phí.
- Tách A3 theo loại và thêm bảng tỉ lệ ok theo lần thử. Kết quả cho thấy quoc_te (22.515 đ, 1,88×) [simulated] không đáng chạy, và chạy lại không giúp vì lần 3 chỉ đúng 2,2%.
- Tính A4 (cộng chi phí cố định 40 triệu đ/tháng): 4.599 đ ở 45.000 yêu cầu/tháng, 5.784 đ khi khối lượng còn một nửa [simulated].
- Hoàn thiện bảng độ nhạy B1 (9 kịch bản), B2 (6.543 đ, +46,3%), B3 (giới hạn 2 lần rẻ nhất cho công ty, 6.901.220 đ) và B4 (xem lại 100% là 11.743 đ = 0,98×), kèm mức hoà vốn ≤ 5,1 phút xem lại mỗi yêu cầu [simulated].
- D1: 1.251 / 3.103 / 1.000 / 300 / 859 (m = 299). Ở mức chênh 5 điểm, power chỉ còn 0,64 nếu dùng n = 859. Ước lượng pilot cần khoảng 4 tuần.
- E2: bốn dòng rủi ro kinh tế, số lấy từ bảng độ nhạy.

## 4. Bằng chứng

- File: `report/team/bang_chi_phi.md` (commit của tài khoản `haiquanng`).
- Bàn giao D1 và E2 gửi qua chat nhóm cho Trần Việt Anh (`pilot_plan.yaml`) và Nguyễn Ánh Dương (`chi_so.md`).
- Con số đối chiếu với đáp án trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`: tất cả lệch dưới 2%.

## 5. Công cụ AI đã dùng

- Claude Code: đọc đề và slide, gợi ý code cho script kiểm số (hàm `mo_hinh`, cỡ mẫu), soạn khung bảng trong `bang_chi_phi.md`.
- Cách tự kiểm tra: mọi con số đều do script chạy trên hai file CSV tính ra, không lấy số AI tự đưa. Mình đối chiếu từng con số với đáp án trong hướng dẫn (ngưỡng 2%) và với output của `src/lab13.py`. Mình cũng kiểm tra tay vài số: 4.373.585 ÷ 978 = 4.472; 1 + 74 × 0,02 = 2,48; 20 ÷ 0,02 = 1.000.
- Không dùng AI cho nhiệm vụ C (gắn nhãn lỗi).

## 6. Tự đánh giá

- Làm tốt: số trong `bang_chi_phi.md` khớp output `src/lab13.py` và đáp án hướng dẫn (lệch < 2%), có nhãn simulated. Bàn giao D1 và E2 đúng các mốc Sync 3 (16:10) và Sync 4 (16:30).
- Chưa tốt: lần đầu ghi ký hiệu ± cho độ nhạy ở B2 và sót nhãn simulated ở vài dòng lẻ. Lỗi được phát hiện khi soát lại và đã sửa trong PR #3.
- Mình tự giải thích được: vì sao tử số cộng mọi lần chạy còn mẫu số chỉ đếm 978 việc thành công; vì sao chia 20 + 20 nhân viên có trần 20 ÷ 0,02 = 1.000 < 1.251.
