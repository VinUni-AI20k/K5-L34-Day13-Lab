# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: TV3 (chờ điền họ tên; bộ nhãn do người dùng cung cấp) · Người gắn nhãn 2: TV4 (chờ điền họ tên; bộ nhãn do người dùng cung cấp)

Yêu cầu: gắn độc lập trong 8 phút, không trao đổi. TV4 chỉ xem bộ nhãn 1 sau khi đã chốt bộ nhãn riêng; chưa xác nhận thời điểm thực hiện của từng người.

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 20 / 20 = 100% (vượt ngưỡng 80%). Theo xác nhận của người dùng trong cuộc trao đổi, TV4 đã đối chiếu các khác biệt mô tả với đề gốc; giữ nguyên nhãn và chốt nhãn thống nhất ở bảng trên.

## Bộ nhãn 1 — giải thích do người dùng cung cấp

Giữ nguyên phân loại và lập luận người dùng đã gửi; chỉ bỏ thẻ HTML và khoảng trắng thừa. Đã nhận bộ nhãn 2 ở phần dưới; giữ nguyên bộ nhãn 1 ban đầu.

| Ca | Loại lỗi | Giải thích ngắn gọn |
| --: | --- | --- |
| 1 | Do người dùng | Khách nhập thiếu 2 chữ số tài khoản (thao tác/nhập liệu sai từ phía người dùng). |
| 2 | Hệ thống | Kiện 28 kg thuộc hàng nặng nhưng trợ lý gọi tool sai tham số (hàng thường), dẫn đến hoàn thiếu tiền và bị mở lại. |
| 3 | Ngữ cảnh | Trợ lý làm đúng thiết kế (hoàn về ví LogiX trong 5 phút), nhưng người dùng kỳ vọng tiền về tài khoản ngân hàng nên thấy sai. |
| 4 | Giới hạn hệ thống | Thiếu dữ liệu chặng do hãng nước ngoài giao nên trợ lý không xác định được trạng thái và chuyển cho nhân viên. |
| 5 | Ngầm | Tính hoàn sai trên 14 đơn có mã giảm giá nhưng không ai phát hiện (không khách nào báo, không có cảnh báo) cho đến khi kiểm tra mẫu cuối tuần. |
| 6 | Do người dùng | Khách chọn nhầm mục "Hoàn phí giao trễ" trong khi nội dung mô tả là hàng bị vỡ. |
| 7 | Hệ thống | API sổ cái lỗi 503 và thử lại 3 lần không thành công nhưng trợ lý vẫn báo "đã hoàn tiền thành công" (lỗi chức năng trong phạm vi). |
| 8 | Hệ thống | Trợ lý dẫn sai căn cứ ("Điều 7.2" không tồn tại trong bản chính sách hiện hành). |
| 9 | Do người dùng | Khách nhập sai loại mã (mã đơn sàn TMĐT thay vì mã vận đơn). |
| 10 | Ngữ cảnh | Trợ lý xử lý đúng chính sách bất khả kháng khi bão, nhưng kỳ vọng của khách bị lệch vì app vẫn hiển thị "cam kết giao 24 giờ". |
| 11 | Giới hạn hệ thống | Đầu vào âm thanh (tin nhắn thoại 40 giây) không xử lý được do năng lực/định dạng hỗ trợ của trợ lý. |
| 12 | Ngầm | Tool ở depot D05 trả thiếu trường làm tăng gấp 3 lần chi phí token suốt 3 tuần mà không ai nhận ra cho đến khi rà soát/kiểm tra. |
| 13 | Giới hạn hệ thống | Bảo hiểm hàng hóa của đối tác nằm ngoài phạm vi hỗ trợ của trợ lý. |
| 14 | Do người dùng | Khách bấm nhầm nút "Xác nhận đã nhận tiền" khi chưa nhận khiến yêu cầu bị đóng. |
| 15 | Hệ thống | Đơn trễ 26 giờ (đúng ra hoàn 50%) nhưng trợ lý tính hoàn 100% — sai so với chính sách. |
| 16 | Ngữ cảnh | Trợ lý làm đúng thiết kế ("gửi ngay khi xong") nhưng gửi lúc 2:14 sáng không phù hợp hoàn cảnh/kỳ vọng nghỉ ngơi của người dùng. |
| 17 | Ngầm | Dùng bảng giá cũ trong bộ nhớ đệm làm lệch tiền 212 đơn suốt 9 ngày nhưng không ai mở lại, chỉ lộ ra khi kiểm tra/đối soát. |
| 18 | Ngữ cảnh | Trợ lý tính đúng số tiền nhưng thiếu giải thích cách tính khiến người dùng hiểu nhầm là hoàn thiếu và mở lại yêu cầu. |
| 19 | Giới hạn hệ thống | Dữ liệu đơn từ 14 tháng trước vượt quá giới hạn truy cập dữ liệu 12 tháng của trợ lý. |
| 20 | Hệ thống | Thiếu cơ chế khóa chống trùng (idempotency/dedup) ở lệnh thứ hai khiến hệ thống hoàn tiền hai lần cho cùng một đơn. |

## Bộ nhãn 2 — nội dung do người dùng cung cấp

Lưu nguyên nhãn và mô tả đã nhận, chỉ bỏ dấu gạch chéo cuối dòng. Một số mô tả ban đầu không khớp đề gốc. Theo thông tin người dùng cung cấp sau khi đối chiếu, TV4 đã xác nhận lại các ca theo đề gốc; giữ nguyên bản gửi ban đầu làm bằng chứng, dùng nội dung đề gốc cho bảng khắc phục.

| Ca | Loại lỗi | Mô tả đã nhận |
| --: | --- | --- |
| 1 | Do người dùng | Khách nhập sai số tài khoản ngân hàng dẫn đến lệnh chuyển thất bại |
| 2 | Hệ thống | Trợ lý tự động hoàn tiền vượt quá hạn mức tối đa quy định trong chính sách |
| 3 | Ngữ cảnh | Khách yêu cầu đổi địa chỉ nhưng agent tự ý tạo ticket hoàn tiền |
| 4 | Giới hạn hệ thống | Đơn hàng quốc tế thiếu thông tin thuế quan nước sở tại để tính phí hoàn |
| 5 | Ngầm | Áp dụng nhầm mã giảm giá nhưng cả khách và nhân viên đều không ai biết |
| 6 | Do người dùng | Khách chọn nhầm lý do "Hàng vỡ" thay vì "Giao trễ" |
| 7 | Hệ thống | Đã báo khách hoàn tiền thành công nhưng hệ thống sổ cái bị lỗi 503 chưa ghi |
| 8 | Hệ thống | Trợ lý trích dẫn sai điều khoản hợp đồng đã bị hủy bỏ |
| 9 | Do người dùng | Khách nhập mã vận đơn của sàn TMĐT khác vào hệ thống LogiX |
| 10 | Ngữ cảnh | Trợ lý từ chối hoàn phí vì khách khiếu nại sau 18:00 (đúng quy định giờ làm việc nhưng làm khách ức chế) |
| 11 | Giới hạn hệ thống | File đính kèm của khách định dạng lạ (.heic / file hỏng) hệ thống không đọc được |
| 12 | Ngầm | Trợ lý chạy lặp vòng lặp tool call tốn gấp 3 lần chi phí mà kết quả vẫn ra đúng |
| 13 | Giới hạn hệ thống | Khách yêu cầu bồi thường thiệt hại hợp đồng kinh tế phát sinh ngoài cước vận chuyển |
| 14 | Do người dùng | Khách chụp ảnh hoá đơn bị lóa sáng, mất góc |
| 15 | Hệ thống | Trợ lý tính tiền hoàn bị lệch 10.000 đ và nhân viên phát hiện ngay khi xem lại |
| 16 | Ngữ cảnh | Khách VIP yêu cầu hỗ trợ đặc biệt nhưng trợ lý áp dụng máy móc quy trình phổ thông |
| 17 | Ngầm | Trợ lý áp dụng bảng giá cước cũ do cache chưa được xóa sau khi tăng giá |
| 18 | Ngữ cảnh | Trợ lý tính đúng cước hoàn theo tỉ lệ 50% nhưng khách tưởng được hoàn 100% |
| 19 | Giới hạn hệ thống | Khách hỏi thông tin kiện hàng quá 6 tháng đã lưu kho lưu trữ |
| 20 | Hệ thống | Hệ thống gọi tool ghi sổ cái bị duplicate lệnh hoàn tiền 2 lần cho 1 đơn |

### Đối chiếu mô tả bộ 2 với đề gốc — TV4 đã xác nhận theo thông tin người dùng

Nguồn: `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`, mục “Hai mươi ca lỗi”. Các dòng dưới là ghi chú kiểm tra, không thay thế nội dung ban đầu của người gắn nhãn 2.

| Ca | Điểm khác trong mô tả bộ 2 | Nội dung đề gốc đã đối chiếu |
| --: | --- | --- |
| 2 | Vượt hạn mức hoàn tiền | Kiện 28 kg, gọi tool với tham số hàng thường thay vì hàng nặng, hoàn thiếu 45.000 đ |
| 3 | Đổi địa chỉ bị tạo ticket hoàn tiền | Hoàn về ví LogiX trong 5 phút nhưng khách chờ tiền về ngân hàng |
| 4 | Thiếu thông tin thuế quan | LogiX không có dữ liệu chặng do hãng nước ngoài giao |
| 6 | Chọn Hàng vỡ thay vì Giao trễ | Khách chọn Hoàn phí giao trễ nhưng mô tả hàng bị vỡ; bộ 2 đảo chiều hai mục |
| 8 | Điều khoản đã bị hủy bỏ | Điều 7.2 không tồn tại trong chính sách hiện hành; đề không nêu từng bị hủy |
| 9 | Mã vận đơn của sàn khác | Nhập mã đơn sàn TMĐT thay vì mã vận đơn; khác loại mã, không phải chỉ khác hệ thống |
| 10 | Khiếu nại sau 18:00 | Giao trễ do bão, từ chối đúng điều khoản bất khả kháng nhưng app vẫn cam kết 24 giờ |
| 11 | File HEIC hoặc file hỏng | Tin nhắn thoại 40 giây, trợ lý không xử lý được âm thanh |
| 13 | Bồi thường thiệt hại hợp đồng kinh tế | Hoàn phí bảo hiểm hàng hóa của công ty bảo hiểm đối tác, ngoài phạm vi trợ lý |
| 14 | Ảnh hóa đơn bị lóa/mất góc | Bấm nhầm Xác nhận đã nhận tiền khi chưa nhận, làm yêu cầu bị đóng |
| 15 | Lệch 10.000 đ | Trễ 26 giờ, chính sách hoàn 50% nhưng tính 100%, nhân viên bắt được trước gửi |
| 16 | Khách VIP cần hỗ trợ đặc biệt | Thông báo Zalo lúc 2:14 sáng theo thiết kế gửi ngay khi xong, làm phiền khách |
| 19 | Đơn quá 6 tháng đã lưu trữ | Đơn từ 14 tháng trước trong khi trợ lý chỉ truy cập 12 tháng |

**Kết luận sau xác nhận:** người dùng thông báo TV4 đã xác nhận các ca theo đề gốc và giữ nguyên bộ nhãn. Hai bộ nhãn trùng 20/20 = 100%; không sửa nhãn hoặc mô tả gửi ban đầu. Bảng đối chiếu trên lưu lại cách xử lý khác biệt mô tả, không phải một bộ nhãn độc lập mới do AI tạo.

## Quy tắc phân biệt cho các ca không trùng

Không có ca khác nhãn trong hai danh sách đã nhận. Các khác biệt về mô tả đã được đối chiếu theo đề gốc và TV4 xác nhận theo thông tin người dùng; không có ca cần phân xử nhãn.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Chọn ca 9, 7, 18, 4, 17 theo đề gốc, đủ năm loại. Mỗi dòng có event, ngưỡng, tần suất và một vai trò chịu trách nhiệm. Các ngưỡng, lịch kiểm tra và biện pháp là đề xuất thiết kế, chưa phải kết quả triển khai; 212 đơn là dữ kiện của ca 17.

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event input_validation_failed có trace_id và reason=sai_loai_ma; tính tỉ lệ hằng ngày trên tổng yêu cầu, cảnh báo nếu >2% | Nhận diện mã đơn sàn TMĐT và hướng dẫn lấy mã vận đơn; chỉ tra chéo khi có dữ liệu ánh xạ, không đoán mã | PM trợ lý hoàn phí |
| 7 | Hệ thống | Mỗi giờ đối soát thông báo đã hoàn với refund_ledger_write thành công cùng trace_id; cảnh báo ngay khi có ít nhất 1 thông báo không có ghi sổ thành công | Chỉ xác nhận đã hoàn sau khi sổ cái trả thành công; lỗi 503 hết số lần thử thì thông báo đang xử lý và chuyển nhân viên; dùng khóa chống trùng | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Event ticket_reopened có trace_id và reason=khong_hieu_cach_tinh; rà mọi ca thuộc lý do này hằng tuần, cảnh báo khi có ít nhất 1 ca tính đúng nhưng thiếu giải thích | Luôn hiển thị phí gốc, tỉ lệ và phép tính: 30.000 đ × 50% = 15.000 đ; kiểm tra mẫu tin nhắn trước khi gửi | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event handoff_to_staff có trace_id, loai và reason=thieu_du_lieu_chang; rà hằng tuần, ngưỡng 0 ca tự xác nhận hoàn khi không có dữ liệu chặng | Báo rõ giới hạn dữ liệu; chuyển nhân viên kèm tóm tắt và thông tin còn thiếu; loại quoc_te khỏi phạm vi pilot đề xuất | PM trợ lý hoàn phí |
| 17 | Ngầm | Event audit_sample_checked có trace_id và phiên bản bảng giá; kiểm tra ngẫu nhiên 100 đơn/tuần so với bảng giá hiện hành, cảnh báo nếu ít nhất 1 đơn lệch | Vô hiệu hóa cache khi đổi bảng giá; ghi phiên bản giá trong trace; đối soát 212 đơn bị ảnh hưởng và thực hiện điều chỉnh sau phê duyệt | Kế toán trưởng |

## Hướng dẫn thực hiện CP3 (TV3 chuẩn bị)

**Trạng thái CP3: đã có hai bộ nhãn, đồng thuận 20/20 = 100%, TV4 đã xác nhận đối chiếu theo thông tin người dùng, và bảng khắc phục đủ năm loại. Còn bổ sung họ tên/thời điểm chốt và liên kết event với chi_so.md khi đóng gói hồ sơ.**
Không dùng gợi ý hoặc đáp án mẫu để điền hai bộ nhãn độc lập. Mỗi người ghi riêng trong 8 phút; chỉ đối chiếu hai bộ nhãn sau khi cả hai đã chốt. Không sửa nhãn ban đầu sau khi so sánh.

### Định nghĩa thao tác trước khi gắn nhãn

| Loại | Câu hỏi để phân biệt |
| --- | --- |
| Do người dùng | Đầu vào hoặc thao tác của người dùng sai có phải nguyên nhân gốc không |
| Hệ thống | Chức năng trong phạm vi có bị lỗi và lỗi đã lộ ra trong xử lý không |
| Ngữ cảnh | Hệ thống có hiểu sai hoàn cảnh, nhu cầu hoặc kỳ vọng dù thao tác/kết quả kỹ thuật có thể đúng không |
| Giới hạn hệ thống | Yêu cầu có vượt phạm vi, năng lực hoặc dữ liệu hệ thống được thiết kế để xử lý không |
| Ngầm | Sai sót có tồn tại mà người dùng/nhân viên không nhận ra, chỉ phát hiện khi kiểm tra hoặc đối soát không |

Gắn theo nguyên nhân gốc; nơi cần sửa không tự quyết định loại lỗi. Nếu chưa rõ nguyên nhân, ghi lý do cần kiểm chứng, không tự bịa dữ kiện của ca.

### Cách tính và lưu bằng chứng

- Sau khi hai người chốt: số ca trùng = tổng các dòng có cùng nhãn ban đầu; đồng thuận = số ca trùng / 20 × 100%.
- Đạt từ 16/20 = 80%. Nếu thấp hơn: ghi định nghĩa đã sửa, lưu nguyên kết quả lần đầu; tách riêng mọi lần gắn lại.
- Với mỗi ca bất đồng, ghi số ca, hai nhãn ban đầu, nhãn thống nhất và một câu quy tắc phân biệt dựa trên mô tả ca.
- Mỗi loại chọn một ca sau khi thống nhất. Bảng dưới chỉ là đề xuất thiết kế, chưa phải kết quả phân loại 20 ca và chưa thay bảng nộp ở trên.

### Thư viện khắc phục tham khảo

Các ngưỡng sau là ngưỡng đề xuất của nhóm, không phải số liệu quan sát.

| Loại | Phát hiện đo được (đề xuất) | Khắc phục (đề xuất) | Vai trò phụ trách |
| --- | --- | --- | --- |
| Do người dùng | Event input_validation_failed có trace_id, reason; rà hằng ngày nếu >2% yêu cầu | Kiểm tra định dạng, chỉ rõ trường cần sửa; không suy đoán mã đơn | PM trợ lý hoàn phí |
| Hệ thống | Đối soát refund_ledger_write với thông báo hoàn mỗi giờ; cảnh báo ngay khi có 1 thông báo thành công không có ghi sổ thành công | Chỉ xác nhận sau khi ghi sổ thành công; khóa chống trùng, chuyển nhân viên nếu ghi sổ lỗi | Kỹ sư trưởng agent |
| Ngữ cảnh | Ghi reason của ticket_reopened; rà hằng tuần mọi ca mở lại do chưa hiểu cách tính | Hiển thị cách tính, điều kiện áp dụng; hỏi lại khi thiếu thông tin ngữ cảnh | Trưởng nhóm CSKH |
| Giới hạn hệ thống | Event handoff_to_staff có reason, loai, trace_id; kiểm tra hằng tuần số ca ngoài phạm vi vẫn tự xử lý, ngưỡng 0 | Chặn ngoài phạm vi; chuyển nhân viên kèm tóm tắt và lý do | PM trợ lý hoàn phí |
| Ngầm | Event audit_sample_checked; kiểm tra ngẫu nhiên 100 đơn/tuần so với chính sách hiện hành, cảnh báo khi ít nhất 1 đơn lệch | Ghi phiên bản chính sách/bảng giá, vô hiệu hóa cache cũ; đối soát và sửa các đơn chịu ảnh hưởng | Kế toán trưởng |

### Việc còn lại do hai người gắn nhãn thực hiện

- [ ] Điền tên và thời điểm chốt của từng người.
- [x] Lưu bộ nhãn 1 đủ 20 ca và giải thích do người dùng cung cấp.
- [x] Lưu bộ nhãn 2 đủ 20 ca do người dùng cung cấp; chưa xác nhận quá trình gắn độc lập.
- [x] Người dùng xác nhận TV4 đã đối chiếu các mô tả khác đề gốc; giữ nguyên bộ nhãn ban đầu.
- [x] Tính đồng thuận từ hai bộ nhãn đã nhận: 20/20 = 100%; chốt nhãn thống nhất sau xác nhận đối chiếu.
- [x] Hoàn thiện bảng khắc phục cho ca 9, 7, 18, 4, 17 theo đề gốc, đủ năm loại.
- [ ] TV4 kiểm tra event ở bảng khắc phục được đặc tả trong chi_so.md.
