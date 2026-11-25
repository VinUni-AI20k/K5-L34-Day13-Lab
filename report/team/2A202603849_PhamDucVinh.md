# Báo cáo cá nhân — PhamDucVinh-2A202603849

## 1. Thông tin thành viên

- Họ tên: Phạm Đức Vinh
- MSSV: 2A202603849
- Email: 26ai.vinhpd@vinuni.edu.vn
- Vai trong nhóm: Người viết code (trước giải lao)

## 2. Phần việc phụ trách

- **Chính:** chuẩn bị môi trường (14:00), CP1 · Nhiệm vụ A (mô hình chi phí), CP2 · Nhiệm vụ B (bảng độ nhạy), đóng gói và nộp bài (`TEAM.md`, push).
- **Phụ:** CP3 (hoàn thiện B, dọn code chạy từ đầu đến cuối), CP4 (soát `pilot_plan.yaml`), CP5 (chạy lại `lab13.py` trên máy khác), bàn giao code cho Người 2 sau giải lao.

## 3. Đóng góp cụ thể

- **A1:** viết `so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`; ba phép thử đáp án biết trước in ĐẠT (1,20 · 1,25 · 1,25).
- **A2:** viết `mo_hinh()` tính token, tool, phần lần chạy 2–3, xem lại, làm lại, tổng, số việc thành công, chi phí mỗi việc thành công và hoá đơn chia số yêu cầu. Kết quả: **4.472 đ/việc thành công** [simulated], gấp **16,3 lần** hoá đơn token + tool chia số yêu cầu (274,7 đ).
- **A3:** gọi `mo_hinh` cho từng `loai` và tính tỉ lệ ok theo từng lần thử; chỉ ra `quoc_te` đắt hơn nhân viên tự làm (1,88×) [simulated] và chạy lại không giúp (ok 30,0% → 11,4% → 2,2%).
- **A4:** cộng chi phí cố định 40 triệu đ/tháng cho phạm vi `noi_dia` + `hang_nang`: 4.599 đ = 0,38× ở 45.000 yêu cầu/tháng, 5.784 đ = 0,48× ở một nửa khối lượng [simulated].
- **B1, B2:** 9 kịch bản đổi từng yếu tố cộng một cặp (token ×2 + xem lại ×2 = +46,3%), có `assert` tự kiểm "giảm một nửa = nửa mức tăng của gấp đôi". Xếp hạng: làm lại (±51,8%) · xem lại (±40,7%) · lương (+23,1%).
- **B3:** chi phí cả hệ thống theo giới hạn 1/2/3 lần chạy: giới hạn 2 lần rẻ nhất cho công ty (6.901.220 đ) [simulated], khác giới hạn 1 lần cho chi phí mỗi việc thành công thấp nhất (4.111 đ).
- **B4:** xem lại 100% cho `noi_dia` + `hang_nang`: 11.743 đ = 0,98× (làm lại 9 phút) và 12.415 đ = 1,03× (làm lại 15,3 phút) [simulated]; mức hoà vốn mỗi lần xem lại ≤ 5,1 / ≤ 4,8 phút.
- Sửa lỗi in tiếng Việt trên console Windows (cp1252) để `lab13.py` chạy được trên mọi máy trong nhóm.
- Điền kết quả A1–A4, B1–B4 vào `report/team/bang_chi_phi.md` để Người 2 đối chiếu và tính tay kiểm lại.

## 4. Bằng chứng

- Commit `b9a5f93` "CP1 CP2: code A1-A4, B1-B4 va dien bang_chi_phi.md" trên nhánh `vinh`, đã merge vào `main` qua pull request #1.
- Code A1, A2 (hàm) và phần A3, A4, B1–B4 trong khối `__main__` của [src/lab13.py](../../src/lab13.py).
- Bảng số trong [report/team/bang_chi_phi.md](bang_chi_phi.md).
- Chạy `cd src; python lab13.py`: in `Ba phép thử đáp án biết trước: ĐẠT`, mọi số A và B khớp slide chữa (lệch < 0,1%).

## 5. Công cụ AI đã dùng

- **Claude Code (Claude Opus):** đọc đề, `PhanCong.md`, `CHECKPOINTS.md`; viết code A1–A4, B1–B4 trong `lab13.py`; điền `bang_chi_phi.md`; soạn báo cáo cá nhân này.
- **Cách tự kiểm tra:** chạy `python lab13.py` trên máy mình, ba phép thử in ĐẠT; đối chiếu từng con số với bảng tự kiểm trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (lệch ≤ 2%); kiểm tra tay 4.373.585 ÷ 978 = 4.472 đ; kiểm tra quy tắc "giảm một nửa = nửa mức tăng" bằng `assert` trong code; Người 2 tính tay đối chiếu độc lập.

## 6. Tự đánh giá

- Hoàn thành đúng hạn phần chính CP1, CP2; code chạy từ đầu đến cuối, số khớp đáp án, đã bàn giao cho Người 2 viết tiếp CP4, CP5.
- Điều học được: chi phí thật nằm ở giờ nhân viên (92,5% tổng chi phí [simulated]), không ở token (5,6%); pilot cần theo dõi tỉ lệ làm lại và xem lại hơn là giá token.
- Cần cải thiện: tự tính tay thêm một vài con số trước khi nhờ AI viết code, để hiểu công thức chắc hơn.
