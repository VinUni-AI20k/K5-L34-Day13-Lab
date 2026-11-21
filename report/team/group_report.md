# Báo cáo nhóm

## 1. Thông tin nhóm

- Tên nhóm: VOI
- Lớp: L3A
- Thành viên: Vũ Đức Tâm, Nguyễn Trung Duy, Chu Mai Hồng, Phạm Việt Hưng và Trần Việt Tiến. [Thông tin nhóm](../../TEAM.md)

## 2. Mục tiêu và cách tiếp cận

Đánh giá chi phí của trợ lý hoàn phí LogiX-VN và dùng kết quả để thiết kế pilot cho Gate 2a. Nhóm dùng mẫu giả lập gồm 1.200 yêu cầu và 1.624 lượt chạy, với mốc nhân viên tự xử lý là 12.000 đ/yêu cầu.

## 3. Giải pháp

- **A.** Cộng chi phí token, tool, xem lại và làm lại trên toàn mẫu, rồi tính chi phí mỗi việc thành công theo loại yêu cầu và khi phân bổ chi phí cố định. [Bảng chi phí](bang_chi_phi.md#a2--mô-hình-chi-phí-từ-trace)
- **B.** Thử chín kịch bản riêng, một kịch bản kết hợp, ba giới hạn chạy và kịch bản xem lại 100% trong phạm vi pilot. [Bảng độ nhạy](bang_chi_phi.md#b1--đổi-từng-yếu-tố)
- **C.** Hai thành viên gắn nhãn độc lập 20 ca theo nguyên nhân gốc, sau đó đối chiếu và lập phương án phát hiện, khắc phục cho năm loại lỗi. [Bảng lỗi trên nhánh hong](https://github.com/vuductam20022004/K5-L3A-DAY13-VOI-LaunchEconomics/blob/9f14998/report/team/bang_loi.md)
- **D.** Thiết kế pilot ngẫu nhiên theo nhân viên, phân tầng theo depot, có đối chứng đồng thời, ba luật dừng và phương án quay về quy trình thủ công. [Kế hoạch pilot](pilot_plan.yaml)
- **E.** Tính ba chỉ số từ CSV, bổ sung chỉ số sử dụng và an toàn, đề xuất 12 event có `trace_id` và ngưỡng theo dõi rủi ro kinh tế. [Đặc tả chỉ số](chi_so.md)

## 4. Kết quả

- **A.** Có 978/1.200 yêu cầu thành công, với chi phí 4.472 đ/việc (simulated). Trong phạm vi nội địa và hàng nặng, chi phí gồm cố định đạt 4.599 đ/việc tại 45.000 yêu cầu/tháng và 5.784 đ/việc khi khối lượng giảm một nửa (simulated).
- **B.** Tăng gấp đôi số ca làm lại làm chi phí tăng 51,8%. Giới hạn 2 lượt cho chi phí hệ thống thấp nhất, 6.901.220 đ trên mẫu 1.200 yêu cầu. Nếu xem lại 100%, chi phí trong phạm vi pilot là 11.743–12.415 đ/việc theo hai giả định thời gian làm lại (simulated).
- **C.** Hai bộ nhãn trùng **20/20 ca (100%)**, vượt mốc 80%. Bảng khắc phục bao gồm đối soát thông báo đã hoàn với sổ cái và kiểm toán mẫu theo bảng giá hiện hành. Kết quả đối chiếu đã có ở commit `9f14998` trên nhánh `hong`.
- **D.** Phương án gồm 20 nhân viên mỗi nhánh và tối thiểu 299 yêu cầu mỗi nhân viên, tương đương 859,2 yêu cầu hiệu dụng mỗi nhánh. Thiết kế nhắm mức chênh tối thiểu 6 điểm phần trăm với power 0,80. Nếu tác động thật là 5 điểm, power khoảng 0,64. Ngày quyết định dự kiến **05/01/2027**.
- **E.** Trên mẫu giả lập, **82,83%** yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày, **27,12%** yêu cầu được xem lại có gợi ý bị sửa hoặc bỏ, và **4,25%** yêu cầu mở lại trong 7 ngày.
- **Đề xuất Gate 2a.** **Go có điều kiện** cho yêu cầu nội địa và hàng nặng. Trước khi bật pilot, cần kiểm thử chống hoàn trùng và đối soát sổ cái, phê duyệt thiết kế và luật dừng, bật event và xác nhận chạy lại bài trên máy thứ hai. Trong tuần đầu, đo thời gian xem lại và làm lại thực tế. [Hồ sơ Gate 2a](ho_so_launch_v0.md)
- **Duyệt chéo.** Kết quả hội đồng dành cho nhóm VOI đang chờ ghi nhận.

## 5. Khó khăn và cách xử lý

Khi chọn giới hạn lượt chạy, tối ưu chi phí trợ lý trên mỗi việc thành công dẫn đến chọn một lượt. Sau khi cộng 12.000 đ cho mỗi yêu cầu nhân viên phải làm thay, hai lượt cho tổng chi phí thấp nhất (simulated). Với pilot, việc chia theo nhân viên giới hạn cỡ mẫu hiệu dụng, nên nhóm nâng mức chênh cần phát hiện từ 5 lên 6 điểm phần trăm.

## 6. Tổng hợp đóng góp

Vũ Đức Tâm xây dựng mô hình A và tích hợp mã. Nguyễn Trung Duy kiểm số, phân tích B và tổng hợp báo cáo. Chu Mai Hồng phụ trách phân loại lỗi và phiếu duyệt chéo. Phạm Việt Hưng thiết kế pilot và gắn bộ nhãn thứ hai. Trần Việt Tiến phụ trách chỉ số, event và hồ sơ Gate 2a. [Chi tiết đóng góp](../../TEAM.md)

## 7. Hạn chế và hướng cải thiện

CSV là dữ liệu giả lập và thiếu nhóm đối chứng đồng thời. Tỉ lệ 82,83% mô tả mẫu, còn 70% là mốc giả định dùng để tính cỡ mẫu. Khi pilot, cần theo dõi hai nhánh trong cùng thời gian, chờ đủ cửa sổ 7 ngày sau đóng và cập nhật mô hình chi phí bằng thời gian nhân viên đo được.

## 8. Tài liệu tham khảo

- [Dữ liệu và công thức Lab 13](../../docs/du_lieu_va_cong_thuc.md)
- [Hướng dẫn thực hiện Lab 13](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md)
- [CSV yêu cầu](../../src/logix_requests.csv) và [CSV lượt chạy](../../src/logix_runs.csv)
