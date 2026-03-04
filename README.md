# IROD Lab Website

This is the official website for the Interactive Robot Design (IRoD) Lab, built with [Quarto](https://quarto.org) and hosted on [GitHub Pages](https://pages.github.com).

**🌐 Website:** [irodlab.com](https://irodlab.com)  
**📝 CMS:** [irodlab.netlify.app/admin](https://irodlab.netlify.app/admin)  
**📦 Repository:** IROD-Lab/irod_lab_website

---

## 📋 Table of Contents

- [Quick Start](#quick-start)
- [Folder Structure](#folder-structure)
- [Contributing](#contributing)
- [Content Management System (CMS)](#content-management-system-cms)
- [Adding Your Personal Profile](#adding-your-personal-profile)
- [Adding Other Content](#adding-other-content)
- [Managing Publications](#managing-publications)
- [Technical Details](#technical-details)

---

## 🚀 Quick Start

### Prerequisites

- [uv](https://docs.astral.sh/uv/) package manager
- Git

### Setup & Preview

1. **Clone the repository:**
   ```bash
   git clone https://github.com/IROD-Lab/irod_lab_website.git
   cd irod_lab_website
   ```

2. **Install dependencies:**
   ```bash
   uv sync
   ```
   This installs all Python dependencies including `quarto-cli`, so you don't need to install Quarto separately.

3. **Activate the virtual environment:**
   ```bash
   # On Windows (PowerShell)
   .venv\Scripts\Activate.ps1
   
   # On macOS/Linux
   source .venv/bin/activate
   ```

4. **Preview the website:**
   ```bash
   quarto preview
   ```
   This will start a local development server. Open your browser to the displayed URL (typically `http://localhost:4200`) to see the website. Changes to files will automatically refresh the preview.

---

## 📁 Folder Structure

```
irod_group/
├── content/                    # Main content directory
│   ├── people/
│   │   └── members/           # Member profiles (one folder per person)
│   ├── research/
│   │   ├── featured/          # Research project pages
│   │   └── references.bib     # Main publication database
│   ├── news/
│   │   └── cms/               # News posts
│   └── openings/
│       └── positions/         # Job postings
├── images/                    # Site-wide images (logo, favicon, defaults)
├── admin/                     # Decap CMS configuration
│   └── config.yml
├── components/                # Reusable components
│   └── auto_pubs.qmd         # Auto-generated publication list
├── scripts/                   # Python scripts
│   └── list_pubs.py          # Publication parser/generator
├── _site/                     # Generated website (do not edit)
├── _quarto.yml               # Quarto configuration
└── pyproject.toml            # Python dependencies (managed by uv)
```

### Key Directories

- **`content/people/members/`**: Each member has their own folder (e.g., `firstname.lastname/`) containing `index.qmd` and their profile image
- **`content/research/featured/`**: Research projects, each in its own folder with `index.qmd`, images, and optional `references.bib`
- **`content/news/cms/`**: News articles managed through CMS
- **`content/openings/positions/`**: Job postings and opportunities
- **`images/`**: Site-wide assets (logo, favicon, default images like `blank.jpg`)
- **`_site/`**: Auto-generated output (don't manually edit files here)

---

## 🤝 Contributing

We use a standard Git workflow with pull requests.

### Workflow

1. **Create a new branch** for your changes:
   ```bash
   git checkout -b your-descriptive-branch-name
   ```
   Examples: `add-new-member`, `update-research-project`, `fix-typo`

2. **Make your changes** (edit files, add images, etc.)

3. **Commit your changes:**
   ```bash
   git add .
   git commit -m "Descriptive commit message"
   ```

4. **Push your branch:**
   ```bash
   git push origin your-descriptive-branch-name
   ```

5. **Open a Pull Request** on GitHub:
   - Go to the repository on GitHub
   - Click "Pull requests" → "New pull request"
   - Select your branch and create the PR
   - Request review from lab administrators

6. **After approval**, your changes will be merged to `main` and automatically deployed

---

## 🖥️ Content Management System (CMS)

The easiest way to add or edit content is through our web-based CMS interface.

### Accessing the CMS

**URL:** [irodlab.netlify.app/admin](https://irodlab.netlify.app/admin)

### Requirements

To access the CMS, you need:

1. **GitHub account** with access to the IROD-Lab organization
2. **Repository access** to `irod_lab_website`
3. **Netlify authentication** (handled automatically through GitHub)

### Requesting Access

Contact the lab administrators to:
- Be added to the IROD-Lab GitHub organization
- Get write access to the repository

Once you have access, log in to the CMS using your GitHub credentials.

### What Can Be Managed via CMS

- ✅ Member profiles
- ✅ Research projects
- ✅ News posts
- ✅ Job openings
- ✅ Main site pages (home, about, etc.)
- ❌ Publications (see [Managing Publications](#managing-publications))

---

## 👤 Adding Your Personal Profile

You can add or edit your profile using either the **CMS (recommended)** or **direct file editing**.

### Method 1: Using the CMS (Recommended)

1. **Log in** to [irodlab.netlify.app/admin](https://irodlab.netlify.app/admin)
2. Click **"Members"** in the left sidebar
3. Click **"New Member"**
4. Fill in the required fields:
   - **Title**: Your full name (e.g., "Nguyen Van Nam")
   - **Role**: Select your position (PI, Post-Doc, PhD, MSc, RA, Alumni)
   - **Image**: Click to upload your profile photo
   - **Body**: Write your bio, research interests, etc. (supports Markdown and HTML)
5. Click **"Save"** (draft) or **"Publish"** (make live immediately)

### Method 2: Direct File Editing

1. **Create a folder** under `content/people/members/` with your name:
   ```
   content/people/members/firstname.lastname/
   ```

2. **Add your profile image** to this folder (any image format):
   ```
   content/people/members/firstname.lastname/photo.jpg
   ```

3. **Create `index.qmd`** with this template:
   ```yaml
   ---
   title: "Your Full Name"
   role: "msc"  # Options: pi, pd, phd, msc, ra, alumni
   image: photo.jpg  # Just the filename (not the full path)
   ---
   
   Write your bio here. You can use Markdown or HTML formatting.
   
   ## Education
   - Your degree information
   
   ## Research Interests
   - Your interests
   ```

4. **Commit and push** your changes (see [Contributing](#contributing))

### Profile Image Guidelines

- **Format**: Any image format (JPG, PNG, AVIF, WebP, etc.)
- **Size**: Keep file size reasonable (< 2 MB recommended)
- **Storage**: Place image in your member folder (not in `images/`)
- **Reference**: Use just the filename in frontmatter (e.g., `image: photo.jpg`)
- **Fallback**: If no image is provided, defaults to `/images/blank.jpg`

### Available Roles

- `pi`: Principal Investigator / Professor
- `pd`: Post-Doctoral Researcher
- `phd`: PhD Student
- `msc`: Master's Student
- `ra`: Research Assistant
- `alumni`: Former Lab Member

---

## 📄 Adding Other Content

### Research Projects

**Location:** `content/research/featured/`

Each project is a folder containing:
- `index.qmd` - Project description with frontmatter (title, date, categories, image, etc.)
- Local images (referenced by filename)
- Optional `references.bib` - Project-specific publications

**Example structure:**
```
content/research/featured/my-project-2024/
├── index.qmd
├── project-photo.jpg
└── references.bib (optional)
```

**Via CMS:** Login → "Research Projects" → "New Research Project"  
**Via Files:** Copy an existing project folder as a template

### News Posts

**Location:** `content/news/cms/`

**Via CMS:** Login → "News" → "New News"  
**Via Files:** Create a dated folder (e.g., `YYYY-MM-DD-slug/index.qmd`)

### Job Openings

**Location:** `content/openings/positions/`

**Via CMS:** Login → "Openings" → "New Opening"  
**Via Files:** Create a folder with descriptive name (e.g., `phd-position-2025/index.qmd`)

---

## 📚 Managing Publications

**⚠️ Important:** Publications are **NOT managed through the CMS**. They must be edited directly in the BibTeX file.

### Publication Database

**File:** `content/research/references.bib`

This is the main BibTeX database containing all lab publications. The publication list is automatically generated and displayed on the research page.

### Adding a New Publication

1. **Open** `content/research/references.bib`

2. **Add a BibTeX entry** in the appropriate format:
   ```bibtex
   @article{yourkey2024,
     title = {Your Paper Title},
     author = {Author1 and Author2 and Author3},
     journal = {Journal Name},
     year = {2024},
     volume = {10},
     number = {5},
     pages = {123--145},
     doi = {10.1234/example.doi},
     url = {https://doi.org/10.1234/example.doi}
   }
   ```

3. **Save the file** and commit your changes

### How It Works

1. **BibTeX File**: All publications stored in `content/research/references.bib`
2. **Python Script**: `scripts/list_pubs.py` parses the BibTeX file and categorizes publications
3. **Auto-Generated Component**: `components/auto_pubs.qmd` includes the Python script
4. **Display**: Publications automatically appear on the research page

### Entry Types Supported

- `@article` - Journal articles
- `@inproceedings` / `@conference` - Conference papers
- `@book` / `@incollection` - Books and book chapters
- `@phdthesis` / `@mastersthesis` - Theses

### Special Features

- **Duplicate DOI Handling**: The script automatically handles duplicate DOI entries (common in Zotero exports)
- **Automatic Categorization**: Publications are sorted into categories (Journal Articles, Conference Papers, Books, Theses)
- **Chronological Sorting**: Most recent publications appear first

### Tips

- Export from reference managers (Zotero, Mendeley, etc.) to BibTeX format
- Ensure each entry has a unique key (e.g., `nguyen2024a`, `nguyen2024b`)
- Include DOI when available for better linking
- The script handles formatting automatically

---

## 🔧 Technical Details

### Tech Stack

- **Framework**: [Quarto](https://quarto.org) (v1.4+)
- **Package Manager**: [uv](https://docs.astral.sh/uv/)
- **Python**: 3.12+
- **CMS**: [Decap CMS](https://decapcms.org/) (formerly Netlify CMS)
- **Hosting**: GitHub Pages (main site) + Netlify (CMS authentication)

### Python Dependencies

Defined in `pyproject.toml`:
- `quarto-cli` - Quarto command-line tools
- `pybtex` - BibTeX parsing for publications
- `matplotlib`, `numpy`, `pandas`, `plotly` - Data visualization
- `ipykernel` - Jupyter notebook support

### Dynamic Content

- **Listings**: Quarto's listing feature dynamically displays members, projects, news, etc.
- **Role-Based Filtering**: Members page automatically groups people by role
- **Auto-Generated Publications**: Python script parses BibTeX and generates HTML

### Themes

- **Light**: Flatly
- **Dark**: Darkly
- **Custom CSS**: `styles.css` (Google Sans font)

### Editing Configuration

- **Quarto**: `_quarto.yml`
- **Python**: `pyproject.toml`
- **CMS**: `admin/config.yml`

---

## 📝 Additional Notes

- Changes to `main` branch automatically trigger deployment
- Preview your changes locally before pushing
- The CMS creates commits directly to your branch
- Images are stored locally with content (not in a central folder)
- For questions or issues, contact lab administrators

---

**Last Updated:** March 2026