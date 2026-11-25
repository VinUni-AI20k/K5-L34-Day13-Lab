# CP4 · Nguyễn Tiến Đạt · Cỡ mẫu khi chia nhóm theo nhân viên hoặc depot

**Kết luận D1(b–d).** Với 40 nhân viên hoặc 12 depot và hai nhánh bằng nhau, cả hai cách chia đều thiếu cỡ mẫu để phát hiện mức tăng từ 70% lên 75% với power 80%. Các số bên dưới tính **cho từng nhánh** (trợ lý hoặc đối chứng).

## Mốc đối chiếu

Theo công thức so sánh hai tỉ lệ với α hai phía 0,05 và power 0,80, D1(a) cho 1.250,72, làm tròn lên **1.251 yêu cầu độc lập mỗi nhánh**. Khi nhiều yêu cầu đến từ cùng một nhân viên hoặc depot, chúng có tương quan. Với ICC = 0,02, mỗi nhánh có `c` cụm và mỗi cụm có `m` yêu cầu, hệ số thiết kế là `DE = 1 + (m − 1) × 0,02`. Cỡ mẫu hiệu dụng là `c × m / DE`. [Công thức của lab](../../docs/du_lieu_va_cong_thuc.md)

| Câu | Phép tính mỗi nhánh | Kết luận cho pilot |
| --- | --- | --- |
| D1(b) · 75 yêu cầu mỗi nhân viên | DE = 1 + 74 × 0,02 = 2,48. Cần 1.251 × 2,48 = 3.102,48, làm tròn lên 3.103 yêu cầu. Làm tròn 3.103 / 75 lên thành **42 nhân viên**. | Hai nhánh cần 84 người, vượt 44 người so với 40 người hiện có. |
| D1(c) · 20 nhân viên mỗi nhánh | Với 75 yêu cầu/người, 1.500 yêu cầu cho cỡ mẫu hiệu dụng 1.500 / 2,48 ≈ **605**. Khi tăng số yêu cầu/người, cỡ mẫu hiệu dụng tiến tới 20 / 0,02 = **1.000**. | Ngay cả giới hạn 1.000 cũng thấp hơn 1.251. Kéo dài pilot với cùng 20 người mỗi nhánh không đủ để phát hiện chênh lệch 5 điểm ở power mục tiêu. |
| D1(d) · 6 depot mỗi nhánh | Khi tăng số yêu cầu/depot, cỡ mẫu hiệu dụng tiến tới 6 / 0,02 = **300**. | Mỗi nhánh chỉ có 6 cụm và trần 300 thấp hơn 1.251. |

## Bàn giao cho Hải

Hải dùng ba dòng trên cho phần chú thích D1(b–d) của [kế hoạch pilot](pilot_plan.yaml). Nếu nhóm chọn chia 20 nhân viên mỗi nhánh theo phương án D1(e) của Phúc, ghi mục tiêu **6 điểm phần trăm**. Với 299 yêu cầu/người, mỗi nhánh có 5.980 yêu cầu thực tế, DE = 6,96 và cỡ mẫu hiệu dụng 5.980 / 6,96 ≈ 859. Với tác động thực chỉ 5 điểm, power ước tính còn khoảng 64%. [Bàn giao D1(e) và D2 của Phúc](tv3_ban_giao.md)
