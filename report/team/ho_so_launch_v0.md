# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Nhóm Coffee · Lớp L3B · Bản rà soát trước duyệt chéo

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | **4.472 đ** trên toàn mẫu và **3.414 đ** trong phạm vi nội địa + hàng nặng, chưa cộng cố định (`simulated`). Trong phạm vi này, tổng **3.072.513 đ** chia cho **900** việc thành công (`simulated`). | Giả lập | Người viết code |
| 2 · Ba yếu tố nhạy nhất | Trên toàn mẫu, gấp đôi số ca làm lại **+51,8%**, gấp đôi tỉ lệ xem lại **+40,7%**, tăng lương 25% **+23,1%** (`simulated`). | Giả lập | Người kiểm số |
| 3 · So với nhân viên tự làm | Mốc **12.000 đ/yêu cầu**. Phạm vi nội địa + hàng nặng đạt **4.131 đ/yêu cầu** khi dự phòng nhân viên xử lý 82 ca trợ lý chưa làm thành công, chưa cộng cố định (`simulated`). Quốc tế **22.515 đ/việc thành công**. Đối tác **10.215 đ/việc thành công** và có điều khoản riêng (`simulated`). Cả hai loại nằm ngoài phạm vi đề xuất. | Giả lập | PM trợ lý hoàn phí |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Đợt chạy thử ghi nhận **82,83%** đóng trong 24 giờ và không mở lại trong 7 ngày (994/1.200), **27,12%** gợi ý bị sửa hoặc bỏ (48/177 ca xem lại), **4,25%** mở lại trong 7 ngày (51/1.200). Cần xác nhận nguồn event trong [đặc tả chỉ số](chi_so.md). | Chưa | Người kiểm số |
| 5 · Bảng lỗi và cách khắc phục | [Bảng CP3](bang_loi.md) có **20** tình huống để gắn nhãn và phương án cho **5** loại lỗi. Tỉ lệ đồng thuận cần hai bộ nhãn. | Chưa | Người gắn nhãn 2 kiêm giữ hồ sơ |
| 6 · Pilot plan | Phương án để nhóm duyệt gồm đối chứng cùng thời gian, chia ngẫu nhiên theo nhân viên **20 + 20**, tối thiểu **299 yêu cầu/người** để phát hiện chênh lệch **6 điểm %** với power 80% (khoảng 64% ở mức 5 điểm %). Mở lại trong phạm vi hiện là **39/982 (3,97%)**. Cần chốt phạm vi, lịch và 3 luật dừng trong [kế hoạch pilot](pilot_plan.yaml). | Chưa | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Gấp đôi số ca làm lại đưa chi phí toàn mẫu lên **6.787 đ/việc**. Trong phạm vi đề xuất, xem lại 100% đưa chi phí lên **11.743 đ/việc** với 9 phút làm lại/ca, hoặc **12.415 đ/việc** với 15,3 phút/ca (`simulated`). Ở khối lượng toàn hệ thống **45.000 yêu cầu/tháng**, chi phí trong phạm vi đạt **4.599 đ/việc thành công** sau cộng cố định, và **5.784 đ/việc** khi khối lượng giảm một nửa (`simulated`). | Giả lập | PM trợ lý hoàn phí |

<details>
<summary>Cách đối chiếu số</summary>

- Từ [CSV lần chạy](../../src/logix_runs.csv), cộng `(26 × token vào + 130 × token ra) / 1.000 + 15 × số lần gọi tool` cho mọi lần chạy. Từ [CSV yêu cầu](../../src/logix_requests.csv), cộng 2.000 đ cho mỗi phút ở hai cột `_simulated`. Toàn mẫu được 4.373.585,13 đ chia 978 việc thành công (`simulated`).
- Mục 3 dùng cùng đơn vị đ/yêu cầu và dự phòng 12.000 đ cho mỗi ca trợ lý chưa làm thành công. Trong phạm vi đề xuất, `(3.072.513,274 + 82 × 12.000) / 982 ≈ 4.131 đ/yêu cầu` (`simulated`). Phần cố định ở mục 7 dùng `40.000.000 / (45.000 × 900 / 1.200) ≈ 1.185 đ/việc thành công` và gấp đôi khi khối lượng giảm một nửa.
- Với B4, `(224.513,274 + 948 × 5 × 2.000 + 48 × phút làm lại × 2.000) / 900`. Dùng 9 phút theo đề và 15,3 phút là trung bình đã làm tròn từ toàn mẫu (`simulated`). Nhóm cần đối chiếu với [bảng A/B](bang_chi_phi.md) và [công thức của lab](../../docs/du_lieu_va_cong_thuc.md).

</details>

**Đề xuất dự thảo · No-go ở lần rà soát này.** Quay lại Gate 2a cho phạm vi nội địa + hàng nặng sau khi người giữ hồ sơ đối chiếu đủ **20 ca** và **5 phương án**, người kiểm số xác nhận đo được **3 chỉ số** và định lượng chi phí xem lại, Giám đốc vận hành duyệt thiết kế **20 + 20**, **3 luật dừng** và kiểm thử chặn hoàn trùng.
