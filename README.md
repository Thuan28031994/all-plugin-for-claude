# Claude Plugins & Skills — Source Hub

Tổng hợp **14 mục trong danh sách gốc**: **13 kho GitHub** dưới dạng Git submodule và **1 plugin `frontend-design`** được tham chiếu từ thư mục con của `anthropics/skills`.

> **Đây là thư viện nguồn có ghim phiên bản, không phải một plugin Claude Code duy nhất.** Các dự án có cơ chế cài đặt và yêu cầu riêng. Hãy đọc README/LICENSE của từng nguồn trước khi cài hoặc thực thi.

## Danh mục 14 nguồn

| # | Tên | Nguồn chính thức | Nơi truy cập trong repo này |
|---|---|---|---|
| 1 | Superpowers | [obra/superpowers](https://github.com/obra/superpowers) | [plugins/superpowers](plugins/superpowers) |
| 2 | Skills (Matt Pocock) | [mattpocock/skills](https://github.com/mattpocock/skills) | [plugins/mattpocock-skills](plugins/mattpocock-skills) |
| 3 | Everything Claude Code (ECC) | [affaan-m/ECC](https://github.com/affaan-m/ECC) | [plugins/ecc](plugins/ecc) |
| 4 | Anthropic Skills | [anthropics/skills](https://github.com/anthropics/skills) | [plugins/anthropic-skills](plugins/anthropic-skills) |
| 5 | Ponytail | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | [plugins/ponytail](plugins/ponytail) |
| 6 | UI UX Pro Max | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | [plugins/ui-ux-pro-max](plugins/ui-ux-pro-max) |
| 7 | gstack | [garrytan/gstack](https://github.com/garrytan/gstack) | [plugins/gstack](plugins/gstack) |
| 8 | Caveman | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | [plugins/caveman](plugins/caveman) |
| 9 | Agent Skills | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | [plugins/agent-skills](plugins/agent-skills) |
| 10 | Claude Mem | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | [plugins/claude-mem](plugins/claude-mem) |
| 11 | Humanizer | [blader/humanizer](https://github.com/blader/humanizer) | [plugins/humanizer](plugins/humanizer) |
| 12 | NotebookLM Skill | [PleasePrompto/notebooklm-skill](https://github.com/PleasePrompto/notebooklm-skill) | [plugins/notebooklm-skill](plugins/notebooklm-skill) |
| 13 | Hyperframes | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | [plugins/hyperframes](plugins/hyperframes) |
| 14 | Frontend Design (Claude) | [Claude plugin](https://claude.com/plugins/frontend-design) · [mã nguồn](https://github.com/anthropics/skills/tree/main/skills/frontend-design) | [plugins/anthropic-skills/skills/frontend-design](plugins/anthropic-skills/skills/frontend-design) — dùng chung nguồn số 4 |

**Lưu ý:** `PleasePrompto/notebooklm-skill` đã được chủ sở hữu lưu trữ (archived), vì vậy có thể không phát sinh bản cập nhật mới. `frontend-design` không được tạo bản sao thứ hai.

## Tải đầy đủ các nguồn

```bash
git clone --recurse-submodules https://github.com/Thuan28031994/all-plugin-for-claude.git
cd all-plugin-for-claude
git submodule update --init --recursive
```

**Nếu đã clone repo mà chưa có nội dung trong `plugins/`:**

```bash
git submodule update --init --recursive
```

Nếu chỉ muốn xem và cài một plugin, **nên truy cập nguồn chính thức** từ bảng trên và làm theo hướng dẫn cài đặt riêng; nhiều dự án là bộ công cụ hoặc skill, không phải plugin cài chung được.

## Đồng bộ tự động

- **GitHub Actions** tại [`.github/workflows/sync-upstreams.yml`](.github/workflows/sync-upstreams.yml), theo lịch **mỗi 6 giờ** (`17 */6 * * *`, UTC), đồng thời có thể chạy thủ công bằng **Actions → Sync upstream plugins → Run workflow**.
- Workflow chỉ tra cứu commit HEAD của từng nhánh gốc và cập nhật **gitlink** của các submodule bằng `git update-index`, không chạy `install.sh`, không tải hay thực thi mã từ upstream trong CI.
- Nếu nguồn không thể truy cập, job báo lỗi và **không ghi commit cập nhật dở dang**. Nếu không có phiên bản mới, job không tạo commit.
- `sources.json` chứa danh mục chuẩn; `sources-lock.json` ghi SHA đã ghim. Git history cho phép xem và khôi phục một phiên bản cũ.
- Tác vụ này dùng **GitHub Actions**, **không cần VPS hoặc cronjob máy riêng**. Lịch chạy có thể trễ theo tải của GitHub; để đồng bộ ngay, chạy thủ công từ Actions.

## Bảo mật và bản quyền

- **Submodule tham chiếu nguyên kho gốc**, không sao chép hoặc thay đổi giấy phép. Giấy phép của mỗi dự án nằm ở chính kho đó; `anthropics/skills` có thể có điều khoản riêng theo từng skill.
- **Tự đồng bộ không đồng nghĩa tự động cài đặt hoặc tin cậy mã mới.** Mã tại các submodule có thể thay đổi khi upstream cập nhật. Xem commit mới trước khi sử dụng trên máy thật.
- Không sử dụng `git submodule foreach` để chạy mã, và không tự động tải/khởi chạy các dependency của bên thứ ba.

Danh sách và lịch đồng bộ được duy trì trong chính repo này.
