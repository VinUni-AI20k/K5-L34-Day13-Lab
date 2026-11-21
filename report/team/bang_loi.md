# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: TV3 (chờ điền họ tên; bộ nhãn do người dùng cung cấp) · Người gắn nhãn 2: TV4 (chờ điền họ tên; bộ nhãn do người dùng cung cấp)

Yêu cầu: gắn độc lập trong 8 phút, không trao đổi. TV4 chỉ xem bộ nhãn 1 sau khi đã chốt bộ nhãn riêng; chưa xác nhận thời điểm thực hiện của từng người.

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Chưa chốt |
| 2 | Hệ thống | Hệ thống | Có | Chưa chốt |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Chưa chốt |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Chưa chốt |
| 5 | Ngầm | Ngầm | Có | Chưa chốt |
| 6 | Do người dùng | Do người dùng | Có | Chưa chốt |
| 7 | Hệ thống | Hệ thống | Có | Chưa chốt |
| 8 | Hệ thống | Hệ thống | Có | Chưa chốt |
| 9 | Do người dùng | Do người dùng | Có | Chưa chốt |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Chưa chốt |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Chưa chốt |
| 12 | Ngầm | Ngầm | Có | Chưa chốt |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Chưa chốt |
| 14 | Do người dùng | Do người dùng | Có | Chưa chốt |
| 15 | Hệ thống | Hệ thống | Có | Chưa chốt |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Chưa chốt |
| 17 | Ngầm | Ngầm | Có | Chưa chốt |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Chưa chốt |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Chưa chốt |
| 20 | Hệ thống | Hệ thống | Có | Chưa chốt |

**Tỉ lệ đồng thuận nhãn theo số ca:** 20 / 20 = 100% (vượt ngưỡng 80%). Chưa chốt nhãn thống nhất: cần xác nhận các khác biệt mô tả với đề gốc; không xem 100% là bằng chứng đã gắn trên cùng nội dung ca.

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

Lưu nguyên nhãn và mô tả đã nhận, chỉ bỏ dấu gạch chéo cuối dòng. Một số mô tả không khớp đề gốc; chưa sửa bộ nhãn ban đầu và chưa xác nhận hai người đã gắn trên cùng nội dung ca.

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

### Đối chiếu mô tả bộ 2 với đề gốc — cần người gắn nhãn 2 xác nhận

Nguồn: `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`, mục “Hai mươi ca lỗi”. Các dòng dưới là ghi chú kiểm tra, không thay thế nội dung ban đầu của người gắn nhãn 2.

| Ca | Điểm khác trong mô tả bộ 2 | Nội dung đề gốc cần xác nhận |
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

**Kết luận kiểm tra:** 100% là mức trùng nhãn theo số ca của hai danh sách đã nhận; chưa đủ để khẳng định hai người đã phân loại cùng 20 mô tả. Người gắn nhãn 2 cần xác nhận lại đề đang dùng. Giữ nguyên bộ 2 này; nếu cần gắn lại, lưu riêng bản đối chiếu/lần 2, không ghi đè bằng chứng ban đầu.

## Quy tắc phân biệt cho các ca không trùng

Không có ca khác nhãn trong hai danh sách đã nhận. Các khác biệt về mô tả được ghi riêng ở bảng đối chiếu trên; chưa giả định hai người đã thống nhất nội dung ca.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| ... | Do người dùng | ... | ... | ... |
| ... | Hệ thống | ... | ... | ... |
| ... | Ngữ cảnh | ... | ... | ... |
| ... | Giới hạn hệ thống | ... | ... | ... |
| ... | Ngầm | ... | ... | ... |

## Hướng dẫn thực hiện CP3 (TV3 chuẩn bị)

**Trạng thái: đã lưu hai bộ nhãn do người dùng cung cấp; nhãn trùng 20/20 = 100%, nhưng mô tả bộ 2 cần xác nhận lại với đề gốc. CP3 chưa chốt.**
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

### Thư viện khắc phục đề xuất — cần đối chiếu ca thực tế

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
- [ ] TV4 xác nhận các mô tả khác đề gốc; lưu riêng mọi bản gắn lại.
- [x] Tính mức trùng nhãn theo số ca từ hai danh sách đã nhận: 20/20 = 100%; ghi rõ giới hạn do khác mô tả.
- [ ] Gắn số ca thực tế vào 5 dòng khắc phục, điều chỉnh biện pháp đúng mô tả ca.
- [ ] TV4 kiểm tra event ở bảng khắc phục được đặc tả trong chi_so.md.
