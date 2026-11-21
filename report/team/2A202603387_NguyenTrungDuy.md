# Báo cáo cá nhân — Nguyễn Trung Duy — 2A202603387

## 1. Thông tin thành viên

- Họ tên: Nguyễn Trung Duy
- MSSV: 2A202603387
- Email: duy321111@gmail.com
- Vai trò: Người 2, phụ trách kiểm số, bảng chi phí và phân tích độ nhạy B.

## 2. Phần việc phụ trách

Tổng hợp A1–A4 từ mô hình của Người 1, tính và kiểm tra B1–B4, chuẩn bị mã phần B để Người 1 tích hợp và viết phần A–B của báo cáo nhóm.

## 3. Đóng góp cụ thể

- Điền [bảng chi phí A–B](bang_chi_phi.md). B1 gồm chín kịch bản với mốc A2 là 4.472 đ/việc thành công (simulated). Ở B2, khi giá token và tỉ lệ xem lại cùng tăng gấp đôi, chi phí lên 6.543 đ/việc, tăng 46,3% (simulated).
- Tính cả chi phí nhân viên làm thay trong B3. Giới hạn hai lượt chạy cho tổng chi phí hệ thống thấp nhất, 6.901.220 đ trên 1.200 yêu cầu (simulated).
- Tính B4 trong phạm vi nội địa và hàng nặng. Khi xem lại 100% các yêu cầu có lượt chạy `ok`, chi phí là 11.743 đ/việc với 9 phút làm lại mỗi ca và 12.415 đ/việc với 15,3 phút mỗi ca (simulated).
- Chuẩn bị [mã tính B](../../src/lab13_b.py) để Người 1 tích hợp và viết phần A–B trong [báo cáo nhóm](group_report.md).

## 4. Bằng chứng

Commit `2bad982` trên nhánh `duy` chứa bảng chi phí, mã phần B và nội dung A–B của báo cáo nhóm. Số liệu A1–A4 dựa trên mô hình của Người 1 ở commit `0305c30`.

## 5. Công cụ AI đã dùng

Dùng Codex để hỗ trợ viết mã đối chiếu từ hai CSV, soát bảng và diễn đạt kết quả. Một phép kiểm tra có thể lặp lại là lấy 4.093.220 đ chi phí trợ lý ở giới hạn hai lượt, cộng 234 × 12.000 đ cho các yêu cầu nhân viên làm thay, ra 6.901.220 đ (simulated). Đối chiếu số này với hai hàng còn lại trong bảng B3 để kiểm tra kết luận.

## 6. Tự đánh giá

Kết quả B3 cho thấy cần xét chi phí của cả trợ lý và nhân viên khi chọn giới hạn lượt chạy. B4 cho thấy kết luận về tiết kiệm thay đổi theo thời gian làm lại. Để kiểm chứng khi pilot, cần đo thời gian xem lại và làm lại thực tế, vì cả hai kết quả B4 dựa trên giả định và dữ liệu giả lập.
