# Báo cáo cá nhân — MaiVanThanh-2A202603696

## 1. Thông tin thành viên

- Họ tên: Mai Văn Thanh
- MSSV: 2A202603696
- Email: maivanthanh36tb@gmail.com
- Vai trong nhóm: Người gắn nhãn 2 kiêm giữ hồ sơ

## 2. Phần việc phụ trách

- CP1: điền bảng A2, A3 trong `bang_chi_phi.md` (nhãn *simulated*), bắt đầu điền `ho_so_launch_v0.md`.
- CP3: gắn nhãn 2 cho 20 ca lỗi độc lập; ghi hai bộ nhãn, tỉ lệ đồng thuận, quy tắc ca lệch và bảng khắc phục 5 loại vào `bang_loi.md`.
- CP4: điền `pilot_plan.yaml` (bỏ hết `?`, ba luật dừng, năm câu D2).
- CP5: hoàn thiện `ho_so_launch_v0.md` trước 17:00; điền `phieu_cham.md`, `group_report.md` và phần đóng góp trong `TEAM.md`.

## 3. Đóng góp cụ thể

- **Bảng A2, A3** (`bang_chi_phi.md`): chi phí mỗi việc thành công 4.472 đ [simulated], gấp 16,3 lần hoá đơn token + tool chia số yêu cầu (274,7 đ); làm lại chiếm 51,8%. Tách theo loại: noi_dia 0,22×, hang_nang 0,69×, quoc_te 1,88×, doi_tac 0,85× so với 12.000 đ [simulated]. Kết luận loại quoc_te khỏi phạm vi vì chạy lại không giúp (lần 1 đúng 30%, lần 2 11,4%, lần 3 2,2%).
- **pilot_plan.yaml**: tính năm câu D1 (1.251 · 3.103 · 1.000 · 300 · m ≥ 299) trước khi chọn cách chia. Chọn chia theo nhân viên 20 + 20 vì đủ 20 cụm và tách được tác động; chấp nhận mức chênh 6 điểm (859 yêu cầu/nhóm, DE 6,96) và ghi rõ power chỉ còn 0,64 nếu tác động thật là 5 điểm. Đặt luật an toàn theo tỉ lệ mở lại hiện tại 4,25% (3,97% trong phạm vi), so với đối chứng +2 điểm kèm trần 6%, thay vì ngưỡng tuyệt đối 3% sẽ dừng pilot ngay tuần đầu. Sau góp ý của Phụng: thêm điều kiện đủ 40 nhân viên (nếu chỉ 20 người thì 10 + 10, MDE 8 điểm), lịch thu mẫu ≥ 5.980 yêu cầu/nhóm cộng 7 ngày theo dõi, tách luật hoàn trùng thành luật dừng ngay. Sau đó sửa theo slide D3: bước 4 người chỉ dùng luật tuyệt đối (lệch 2 điểm so với đối chứng chỉ áp dụng từ 10 người), ngưỡng chi phí 8.000 đ không cộng 40 triệu cố định (nếu cộng, bước 4 người đã ≈ 15.300 đ), thêm luật báo "đã hoàn" mà sổ cái không ghi (tổng 5 luật dừng).
- **ho_so_launch_v0.md**: soạn trang hồ sơ bảy mục, đề xuất Go có điều kiện cho pilot noi_dia + hang_nang.
- **TEAM.md**: điền thông tin nhóm, phân vai, phần việc của từng người.
- **bang_loi.md**: tự gắn nhãn 20 ca (người gắn nhãn 2), đồng thuận 18/20 = 90% với người gắn nhãn 1; hai ca lệch là ca 8 (tôi gắn Ngầm, thống nhất Hệ thống vì trích dẫn sai nhìn thấy được) và ca 13 (tôi gắn Hệ thống, thống nhất Giới hạn vì gốc là ngoài phạm vi). Viết bảng khắc phục 5 ca (1, 20, 18, 19, 5) có event, ngưỡng, tần suất và vai phụ trách.

## 4. Bằng chứng

- File: `report/team/bang_chi_phi.md` (A2, A3), `report/team/pilot_plan.yaml`, `report/team/ho_so_launch_v0.md`, `report/team/bang_loi.md`, `TEAM.md`.
- Kiểm tra: `yaml.safe_load` đọc được `pilot_plan.yaml`; ngoài dòng chú thích không còn dấu `?`; lệnh tìm từ cấm theo `SUBMISSION.md` trong `report/team` không in gì.
- Commit (GitHub `MaiVanThanhDev`): `2212a77`, `2242982`, `369be1d`, `8f46aa6`; PR #2 và #3 đã merge vào `main` (`c44bfaa`).

## 5. Công cụ AI đã dùng

- **Claude Code (trong VS Code):** đọc đề và GUIDE để tóm tắt việc của tôi; viết script Python riêng (chỉ dùng thư viện chuẩn, không sửa `lab13.py` và CSV) để tính lại A2, A3, D1, tỉ lệ `mo_lai_trong_7_ngay` và ba chỉ số E1 từ hai file CSV; soạn nháp `pilot_plan.yaml`, bảng A2/A3, `ho_so_launch_v0.md`, `TEAM.md` và báo cáo này.
- **Không dùng AI để gắn nhãn 20 ca lỗi:** nhãn của tôi gắn độc lập, tự tay, theo RULES.md.
- **Cách tự kiểm tra:**
  - So từng số AI tính với số đối chiếu trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`: A2 (245.585 · 84.000 · 93.804 · 4.472), A3 bốn loại, D1 năm câu, mở lại 51/1.200 đều khớp.
  - Tính tay lại câu D1-e: 20m ≥ 859 × (0,98 + 0,02m) → 2,82m ≥ 841,82 → m ≥ 299; và DE câu b: 1 + 74 × 0,02 = 2,48.
  - Chạy `yaml.safe_load` và lệnh tìm dấu `?` cho `pilot_plan.yaml`.
  - Đọc lại từng luật dừng để chắc đủ bốn vế NẾU – TRONG – THÌ – KHÔNG THÌ và người phụ trách là một vai.

## 6. Tự đánh giá

- Tự giải thích được: vì sao tử số tính mọi lần chạy (lần lỗi vẫn tốn token, tool) còn mẫu số chỉ đếm việc thành công; vì sao chia theo cụm thì cỡ mẫu hiệu dụng bị giới hạn bởi c ÷ ICC nên số cụm quyết định chứ không phải tổng số yêu cầu; vì sao đề xuất Go có điều kiện thay vì Go.
- Điểm cần cải thiện:
  - Gắn nhãn còn lẫn hai cặp loại: ca 8 tôi gắn Ngầm vì số tiền vẫn đúng, nhưng trích dẫn sai đã hiện ra trước mắt khách nên là Hệ thống; ca 13 tôi gắn theo chỗ cần sửa (trợ lý trả lời lan man) thay vì nguyên nhân gốc (ngoài phạm vi). Lần sau hỏi trước "có ai nhìn thấy lỗi không" và "gốc lỗi ở đâu" rồi mới gắn.
  - Bản đầu của `pilot_plan.yaml` chưa kiểm giả định 40 nhân viên (dữ liệu chỉ có 20) và chưa có lịch thu mẫu; phải nhờ Phụng soát mới thấy. Lần sau đối chiếu mọi giả định với CSV trước khi chọn cách chia.
  - Luật dừng ban đầu áp dụng như nhau cho mọi bước rollout và cộng cả 40 triệu cố định vào ngưỡng 8.000 đ, nên sẽ dừng nhầm ở bước 4 người (≈ 15.300 đ/việc). Tôi cần tự thử luật dừng với số của từng bước thay vì chỉ kiểm đủ bốn vế.
  - Còn dựa nhiều vào AI để soạn nháp và tính số; tôi cần tự tính tay nhiều hơn, nhất là D1 và hệ số thiết kế, để tự trả lời được khi hội đồng hỏi.
