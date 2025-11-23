# Minimal Photon Theme

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Jekyll](https://img.shields.io/badge/Built%20with-Jekyll-red.svg)](https://jekyllrb.com/)

**Minimal Photon** is a clean, elegant, and responsive academic homepage template designed for researchers, professors, and students. It is built on top of the [Minimal Light](https://github.com/yaoyao-liu/minimal-light) theme, featuring enhanced data management, automated publication updates from BibTeX, and a stylish typewriter intro animation.

[**🇨🇳 中文说明 (Chinese README)**](./README_zh_Hans.md)

---

## ✨ Features

- **📖 Clean & Academic**: Optimized for presenting research, publications, and portfolios.
- **📱 Fully Responsive**: Perfectly adapts to desktops, tablets, and mobile devices.
- **⚙️ Easy Configuration**: Centralized settings in `_config.yml`.
- **🗂️ Data-Driven**: Manage content (News, Experience, Publications) via simple YAML files.
- **🤖 Automation**: Automatically generate publication lists from BibTeX using Python.
- **✨ Interactive**: Stylish typewriter intro animation and publication filtering.
- **📈 Analytics & SEO**: Built-in support for Google Analytics and SEO optimization.

---

## 📂 Project Structure

Understanding the folder structure will help you customize the theme effectively.

```text
.
├── _config.yml              # ⚙️ Main configuration file (Personal info, SEO, Links)
├── index.md                 # 🏠 Homepage content (About Me, Research Interests)
├── _data/                   # 🗃️ Data files for dynamic content
│   ├── experience.yml       #    - Work & Education experience
│   ├── news.yml             #    - Latest news updates
│   ├── publications.yml     #    - Publication list (can be auto-generated)
│   └── references.bib       #    - BibTeX source for publications
├── _includes/               # 🧩 Reusable HTML components (News, Pubs, Experience)
├── _layouts/                # 📐 Page templates
├── assets/                  # 🎨 Static assets
│   ├── css/                 #    - Stylesheets
│   ├── img/                 #    - Images (Profile, Favicon, Pub thumbnails)
│   ├── js/                  #    - JavaScript files (Animation, Filters)
│   └── bibs/                #    - Individual BibTeX files (Auto-generated)
└── scripts/                 # 🛠️ Utility scripts
    └── update_pubs.py       #    - Script to convert BibTeX to YAML
```

---

## 🚀 Quick Start

### 1. Fork & Clone
Fork this repository to your GitHub account and clone it locally:
```bash
git clone https://github.com/yourusername/minimal-photon.git
cd minimal-photon
```

### 2. Install Dependencies
Ensure you have [Ruby](https://www.ruby-lang.org/en/documentation/installation/) and [Bundler](https://bundler.io/) installed.
```bash
bundle install
```

### 3. Run Locally
Start the local server to preview your site:
```bash
bundle exec jekyll serve
```
Visit `http://localhost:4000` in your browser.

---

## 🛠️ Configuration

Most global settings are located in `_config.yml`. Open it and update the following:

- **Basic Info**: `title`, `position`, `affiliation`, `email`.
- **URL Settings**: `url` (your domain), `baseurl` (repository name if not using a custom domain).
- **SEO**: `keywords`, `description`.
- **Social Links**: Update URLs for GitHub, Google Scholar, LinkedIn, etc.
- **Images**: Set paths for `avatar` and `favicon`.
- **Analytics**: Uncomment `google_analytics` and add your Measurement ID (e.g., `G-XXXXXXXXXX`) to enable tracking.

---

## 📝 Managing Content

### 1. Homepage (`index.md`)
Edit `index.md` to update the **About Me**, **Research Interests**, and **Miscellaneous** sections. Markdown is fully supported.

### 2. News (`_data/news.yml`)
Add your latest updates here.
```yaml
- date: Dec. 2024
  content: 📃 Paper accepted at CVPR 2025!
```

### 3. Experience (`_data/experience.yml`)
List your education and work history.
```yaml
main:
  - title: "University Name"
    details: "(2022 - Present) Ph.D. Student"
    image: ./assets/img/logo.png
```

### 4. Publications (`_data/publications.yml`)
You have two options to manage publications:

#### **Option A: Automated (Recommended)**
1.  Paste your BibTeX entries into `_data/references.bib`.
2.  Open `scripts/update_pubs.py` and set `MY_NAME` to your name (this bolds your name in the author list).
3.  Run the script:
    ```bash
    python3 scripts/update_pubs.py
    ```
    This will automatically update `_data/publications.yml` and generate individual `.bib` files in `assets/bibs/`.

#### **Option B: Manual**
Directly edit `_data/publications.yml` following the existing format.

---

## 🎨 Advanced Customization

- **Intro Animation**: Modify the typing text in `assets/js/intro-animation.js`.
- **Visitor Map**: To add a visitor map (e.g., ClustrMaps), edit `index.md` and replace the placeholder comment at the bottom with your script code.
- **Styles**: Custom CSS can be added to `assets/css/style.scss`.

---

## 📦 Deployment

This theme is ready for **GitHub Pages**.

1.  Push your changes to GitHub.
2.  Go to **Settings** > **Pages**.
3.  Under **Source**, select `main` branch (or `master`).
4.  Your site will be live at `https://yourusername.github.io/minimal-photon/`.

---

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgements

Based on the [Minimal Light](https://github.com/yaoyao-liu/minimal-light) theme by [Yaoyao Liu](https://github.com/yaoyao-liu).
