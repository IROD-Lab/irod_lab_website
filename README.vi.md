# Website Phòng thí nghiệm IRoD

Đây là website chính thức của Phòng thí nghiệm Thiết kế Robot Tương tác (IRoD Lab), được xây dựng bằng [Quarto](https://quarto.org) và lưu trữ trên [GitHub Pages](https://pages.github.com).

**🌐 Website:** [irodlab.com](https://irodlab.com)  
**📝 CMS:** [irodlab.netlify.app/admin](https://irodlab.netlify.app/admin)  
**📦 Repository:** IROD-Lab/irod_lab_website

---

## 📋 Mục Lục

- [Bắt Đầu Nhanh](#bắt-đầu-nhanh)
- [Cấu Trúc Thư Mục](#cấu-trúc-thư-mục)
- [Đóng Góp](#đóng-góp)
- [Hệ Thống Quản Lý Nội Dung (CMS)](#hệ-thống-quản-lý-nội-dung-cms)
- [Thêm Trang Cá Nhân](#thêm-trang-cá-nhân)
- [Thêm Nội Dung Khác](#thêm-nội-dung-khác)
- [Quản Lý Danh Sách Công Bố](#quản-lý-danh-sách-công-bố)
- [Chi Tiết Kỹ Thuật](#chi-tiết-kỹ-thuật)

---

## 🚀 Bắt Đầu Nhanh

### Yêu Cầu

- Trình quản lý gói [uv](https://docs.astral.sh/uv/)
- Git

### Cài Đặt & Xem Trước

1. **Clone repository:**
   ```bash
   git clone https://github.com/IROD-Lab/irod_lab_website.git
   cd irod_lab_website
   ```

2. **Cài đặt các gói phụ thuộc:**
   ```bash
   uv sync
   ```
   Lệnh này sẽ cài đặt tất cả các gói Python cần thiết bao gồm `quarto-cli`, do đó bạn không cần cài đặt Quarto riêng.

3. **Kích hoạt môi trường ảo:**
   ```bash
   # Trên Windows (PowerShell)
   .venv\Scripts\Activate.ps1
   
   # Trên macOS/Linux
   source .venv/bin/activate
   ```

4. **Xem trước website:**
   ```bash
   quarto preview
   ```
   Lệnh này sẽ khởi động một máy chủ phát triển cục bộ. Mở trình duyệt và truy cập URL hiển thị (thường là `http://localhost:4200`) để xem website. Các thay đổi đối với tệp tin sẽ tự động làm mới trang xem trước.

---

## 📁 Cấu Trúc Thư Mục

```
irod_group/
├── content/                    # Thư mục nội dung chính
│   ├── people/
│   │   └── members/           # Trang cá nhân thành viên (mỗi người một thư mục)
│   ├── research/
│   │   ├── featured/          # Trang dự án nghiên cứu
│   │   └── references.bib     # Cơ sở dữ liệu công bố chính
│   ├── news/
│   │   └── cms/               # Bài viết tin tức
│   └── openings/
│       └── positions/         # Thông tin tuyển dụng
├── images/                    # Hình ảnh toàn site (logo, favicon, mặc định)
├── admin/                     # Cấu hình Decap CMS
│   └── config.yml
├── components/                # Các thành phần tái sử dụng
│   └── auto_pubs.qmd         # Danh sách công bố tự động
├── scripts/                   # Các script Python
│   └── list_pubs.py          # Phân tích/tạo danh sách công bố
├── _site/                     # Website đã được tạo (không chỉnh sửa)
├── _quarto.yml               # Cấu hình Quarto
└── pyproject.toml            # Các gói Python (quản lý bởi uv)
```

### Các Thư Mục Quan Trọng

- **`content/people/members/`**: Mỗi thành viên có thư mục riêng (vd: `firstname.lastname/`) chứa `index.qmd` và ảnh cá nhân
- **`content/research/featured/`**: Các dự án nghiên cứu, mỗi dự án trong một thư mục riêng với `index.qmd`, hình ảnh, và tùy chọn `references.bib`
- **`content/news/cms/`**: Các bài viết tin tức được quản lý qua CMS
- **`content/openings/positions/`**: Thông tin tuyển dụng và cơ hội việc làm
- **`images/`**: Tài sản toàn site (logo, favicon, hình ảnh mặc định như `blank.jpg`)
- **`_site/`**: Kết quả tự động tạo ra (không chỉnh sửa thủ công các tệp ở đây)

---

## 🤝 Đóng Góp

Chúng tôi sử dụng quy trình Git tiêu chuẩn với pull request.

### Quy Trình

1. **Tạo một nhánh mới** cho các thay đổi của bạn:
   ```bash
   git checkout -b ten-nhanh-mo-ta-cua-ban
   ```
   Ví dụ: `them-thanh-vien-moi`, `cap-nhat-du-an`, `sua-loi-chinh-ta`

2. **Thực hiện thay đổi** (chỉnh sửa tệp, thêm hình ảnh, v.v.)

3. **Commit các thay đổi:**
   ```bash
   git add .
   git commit -m "Thông điệp mô tả thay đổi"
   ```

4. **Push nhánh của bạn:**
   ```bash
   git push origin ten-nhanh-mo-ta-cua-ban
   ```

5. **Mở Pull Request** trên GitHub:
   - Truy cập repository trên GitHub
   - Nhấp "Pull requests" → "New pull request"
   - Chọn nhánh của bạn và tạo PR
   - Yêu cầu quản trị viên xem xét

6. **Sau khi được phê duyệt**, các thay đổi sẽ được merge vào `main` và tự động triển khai

---

## 🖥️ Hệ Thống Quản Lý Nội Dung (CMS)

Cách dễ nhất để thêm hoặc chỉnh sửa nội dung là thông qua giao diện CMS trên web.

### Truy Cập CMS

**URL:** [irodlab.netlify.app/admin](https://irodlab.netlify.app/admin)

### Yêu Cầu

Để truy cập CMS, bạn cần:

1. **Tài khoản GitHub** có quyền truy cập vào tổ chức IROD-Lab
2. **Quyền truy cập repository** `irod_lab_website`
3. **Xác thực Netlify** (được xử lý tự động thông qua GitHub)

### Yêu Cầu Quyền Truy Cập

Liên hệ quản trị viên phòng thí nghiệm để:
- Được thêm vào tổ chức IROD-Lab trên GitHub
- Nhận quyền ghi vào repository

Sau khi có quyền truy cập, đăng nhập vào CMS bằng thông tin đăng nhập GitHub của bạn.

### Nội Dung Có Thể Quản Lý Qua CMS

- ✅ Trang cá nhân thành viên
- ✅ Dự án nghiên cứu
- ✅ Bài viết tin tức
- ✅ Thông tin tuyển dụng
- ✅ Các trang chính của site (trang chủ, giới thiệu, v.v.)
- ❌ Danh sách công bố (xem [Quản Lý Danh Sách Công Bố](#quản-lý-danh-sách-công-bố))

---

## 👤 Thêm Trang Cá Nhân

Bạn có thể thêm hoặc chỉnh sửa trang cá nhân bằng **CMS (khuyến nghị)** hoặc **chỉnh sửa tệp trực tiếp**.

### Phương Pháp 1: Sử Dụng CMS (Khuyến Nghị)

1. **Đăng nhập** vào [irodlab.netlify.app/admin](https://irodlab.netlify.app/admin)
2. Nhấp **"Members"** ở thanh bên trái
3. Nhấp **"New Member"**
4. Điền các trường bắt buộc:
   - **Title**: Họ tên đầy đủ của bạn (vd: "Nguyen Van Nam")
   - **Role**: Chọn vị trí của bạn (PI, Post-Doc, PhD, MSc, RA, Alumni)
   - **Image**: Nhấp để tải lên ảnh đại diện của bạn
   - **Body**: Viết tiểu sử, sở thích nghiên cứu, v.v. (hỗ trợ Markdown và HTML)
5. Nhấp **"Save"** (bản nháp) hoặc **"Publish"** (công khai ngay lập tức)

### Phương Pháp 2: Chỉnh Sửa Tệp Trực Tiếp

1. **Tạo một thư mục** trong `content/people/members/` với tên của bạn:
   ```
   content/people/members/firstname.lastname/
   ```

2. **Thêm ảnh đại diện** vào thư mục này (bất kỳ định dạng hình ảnh nào):
   ```
   content/people/members/firstname.lastname/photo.jpg
   ```

3. **Tạo `index.qmd`** với mẫu này:
   ```yaml
   ---
   title: "Họ Tên Đầy Đủ Của Bạn"
   role: "msc"  # Tùy chọn: pi, pd, phd, msc, ra, alumni
   image: photo.jpg  # Chỉ tên tệp (không phải đường dẫn đầy đủ)
   ---
   
   Viết tiểu sử của bạn ở đây. Bạn có thể sử dụng định dạng Markdown hoặc HTML.
   
   ## Học Vấn
   - Thông tin về bằng cấp của bạn
   
   ## Sở Thích Nghiên Cứu
   - Các sở thích của bạn
   ```

4. **Commit và push** các thay đổi của bạn (xem [Đóng Góp](#đóng-góp))

### Hướng Dẫn Về Ảnh Đại Diện

- **Định dạng**: Bất kỳ định dạng hình ảnh nào (JPG, PNG, AVIF, WebP, v.v.)
- **Kích thước**: Giữ kích thước tệp hợp lý (khuyến nghị < 2 MB)
- **Lưu trữ**: Đặt hình ảnh trong thư mục thành viên của bạn (không phải trong `images/`)
- **Tham chiếu**: Chỉ sử dụng tên tệp trong frontmatter (vd: `image: photo.jpg`)
- **Mặc định**: Nếu không có ảnh, sẽ sử dụng `/images/blank.jpg`

### Các Vai Trò Có Sẵn

- `pi`: Giảng viên / Giáo sư
- `pd`: Nghiên cứu viên sau tiến sĩ
- `phd`: Nghiên cứu sinh tiến sĩ
- `msc`: Học viên cao học
- `ra`: Trợ lý nghiên cứu
- `alumni`: Cựu thành viên phòng thí nghiệm

---

## 📄 Thêm Nội Dung Khác

### Dự Án Nghiên Cứu

**Vị trí:** `content/research/featured/`

Mỗi dự án là một thư mục chứa:
- `index.qmd` - Mô tả dự án với frontmatter (tiêu đề, ngày tháng, danh mục, hình ảnh, v.v.)
- Hình ảnh cục bộ (tham chiếu bằng tên tệp)
- Tùy chọn `references.bib` - Công bố liên quan đến dự án

**Cấu trúc ví dụ:**
```
content/research/featured/du-an-cua-toi-2024/
├── index.qmd
├── anh-du-an.jpg
└── references.bib (tùy chọn)
```

**Qua CMS:** Đăng nhập → "Research Projects" → "New Research Project"  
**Qua Tệp:** Sao chép một thư mục dự án hiện có làm mẫu

### Bài Viết Tin Tức

**Vị trí:** `content/news/cms/`

**Qua CMS:** Đăng nhập → "News" → "New News"  
**Qua Tệp:** Tạo thư mục có ngày (vd: `YYYY-MM-DD-slug/index.qmd`)

### Thông Tin Tuyển Dụng

**Vị trí:** `content/openings/positions/`

**Qua CMS:** Đăng nhập → "Openings" → "New Opening"  
**Qua Tệp:** Tạo thư mục với tên mô tả (vd: `vi-tri-phd-2025/index.qmd`)

---

## 📚 Quản Lý Danh Sách Công Bố

**⚠️ Quan trọng:** Danh sách công bố **KHÔNG được quản lý qua CMS**. Chúng phải được chỉnh sửa trực tiếp trong tệp BibTeX.

### Cơ Sở Dữ Liệu Công Bố

**Tệp:** `content/research/references.bib`

Đây là cơ sở dữ liệu BibTeX chính chứa tất cả các công bố của phòng thí nghiệm. Danh sách công bố được tự động tạo và hiển thị trên trang nghiên cứu.

### Thêm Công Bố Mới

1. **Mở** `content/research/references.bib`

2. **Thêm một mục BibTeX** theo định dạng phù hợp:
   ```bibtex
   @article{key2024,
     title = {Tiêu Đề Bài Báo Của Bạn},
     author = {Tác giả 1 and Tác giả 2 and Tác giả 3},
     journal = {Tên Tạp Chí},
     year = {2024},
     volume = {10},
     number = {5},
     pages = {123--145},
     doi = {10.1234/example.doi},
     url = {https://doi.org/10.1234/example.doi}
   }
   ```

3. **Lưu tệp** và commit các thay đổi của bạn

### Cách Hoạt Động

1. **Tệp BibTeX**: Tất cả công bố được lưu trong `content/research/references.bib`
2. **Script Python**: `scripts/list_pubs.py` phân tích tệp BibTeX và phân loại công bố
3. **Component Tự Động**: `components/auto_pubs.qmd` bao gồm script Python
4. **Hiển thị**: Công bố tự động xuất hiện trên trang nghiên cứu

### Các Loại Mục Được Hỗ Trợ

- `@article` - Bài báo tạp chí
- `@inproceedings` / `@conference` - Bài báo hội nghị
- `@book` / `@incollection` - Sách và chương sách
- `@phdthesis` / `@mastersthesis` - Luận án

### Tính Năng Đặc Biệt

- **Xử Lý DOI Trùng Lặp**: Script tự động xử lý các mục DOI trùng lặp (phổ biến khi xuất từ Zotero)
- **Phân Loại Tự Động**: Công bố được sắp xếp vào các danh mục (Bài Báo Tạp Chí, Bài Báo Hội Nghị, Sách, Luận Án)
- **Sắp Xếp Theo Thời Gian**: Công bố mới nhất xuất hiện đầu tiên

### Mẹo

- Xuất từ các trình quản lý tài liệu tham khảo (Zotero, Mendeley, v.v.) sang định dạng BibTeX
- Đảm bảo mỗi mục có một key duy nhất (vd: `nguyen2024a`, `nguyen2024b`)
- Bao gồm DOI khi có sẵn để liên kết tốt hơn
- Script tự động xử lý định dạng

---

## 🔧 Chi Tiết Kỹ Thuật

### Công Nghệ Sử Dụng

- **Framework**: [Quarto](https://quarto.org) (v1.4+)
- **Trình Quản Lý Gói**: [uv](https://docs.astral.sh/uv/)
- **Python**: 3.12+
- **CMS**: [Decap CMS](https://decapcms.org/) (trước đây là Netlify CMS)
- **Hosting**: GitHub Pages (site chính) + Netlify (xác thực CMS)

### Các Gói Python

Được định nghĩa trong `pyproject.toml`:
- `quarto-cli` - Công cụ dòng lệnh Quarto
- `pybtex` - Phân tích BibTeX cho công bố
- `matplotlib`, `numpy`, `pandas`, `plotly` - Trực quan hóa dữ liệu
- `ipykernel` - Hỗ trợ Jupyter notebook

### Nội Dung Động

- **Listings**: Tính năng listing của Quarto hiển thị động các thành viên, dự án, tin tức, v.v.
- **Lọc Theo Vai Trò**: Trang thành viên tự động nhóm người theo vai trò
- **Công Bố Tự Động**: Script Python phân tích BibTeX và tạo HTML

### Giao Diện

- **Sáng**: Flatly
- **Tối**: Darkly
- **CSS Tùy Chỉnh**: `styles.css` (phông chữ Google Sans)

### Chỉnh Sửa Cấu Hình

- **Quarto**: `_quarto.yml`
- **Python**: `pyproject.toml`
- **CMS**: `admin/config.yml`

---

## 📝 Ghi Chú Bổ Sung

- Các thay đổi đối với nhánh `main` tự động kích hoạt triển khai
- Xem trước các thay đổi của bạn ở local trước khi push
- CMS tạo commit trực tiếp vào nhánh của bạn
- Hình ảnh được lưu cục bộ cùng với nội dung (không phải trong một thư mục trung tâm)
- Để biết câu hỏi hoặc vấn đề, liên hệ quản trị viên phòng thí nghiệm

---

**Cập Nhật Lần Cuối:** Tháng 3 năm 2026
