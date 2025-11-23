# Minimal Photon Theme

A clean, elegant, and responsive academic homepage template for researchers and students. Based on the [Minimal Light](https://github.com/yaoyao-liu/minimal-light) theme.

## Features

- **Clean Design**: Minimalist aesthetic suitable for academic portfolios.
- **Responsive**: Looks good on desktop and mobile.
- **Easy Configuration**: Most settings are in `_config.yml`.
- **Data-Driven**: Manage publications, news, and experience via YAML files.
- **Intro Animation**: A stylish typewriter intro animation.
- **Publication Filters**: (Optional) Filter publications by tags.

## Getting Started

### 1. Fork and Clone

Fork this repository and clone it to your local machine.

### 2. Configuration

Edit `_config.yml` to update your personal information:

- **Basic Info**: Name, position, affiliation, email.
- **SEO**: Keywords, description.
- **Social Links**: GitHub, Google Scholar, LinkedIn, etc.
- **Images**: Update `avatar` and `favicon` paths.

### 3. Content

#### Homepage (`index.md`)
Edit `index.md` to update your "About Me", "Research Interests", and "Miscellaneous" sections.

#### Experience (`_data/experience.yml`)
Add your education and work experience.

```yaml
- title: "University Name"
  details: "(2022.09-Present) B.S in Computer Science"
  image: ./assets/img/logo.png
  image_width: 40px
  image_height: 40px
```

#### News (`_data/news.yml`)
Add your latest news.

```yaml
- date: Dec. 2024
  content: 📃 Paper accepted at CVPR!
```

#### Publications (`_data/publications.yml`)
You can manage your publications in two ways:

**Option 1: Manual Edit (Simple)**
Edit `_data/publications.yml` directly.

```yaml
- title: "Paper Title"
  authors: "<strong>Your Name</strong>, Co-author"
  url: "link_to_pdf"
  code: "link_to_code"
  page: "link_to_project_page"
  image: "./assets/img/pub/image.png"
  notes: "Conference Name"
  tags: "Tag1, Tag2"
```

**Option 2: Using BibTeX (Advanced)**
1. Add your BibTeX entries to `_data/references.bib`.
   - Supported fields: `title`, `author`, `url`, `code`, `page`, `image`, `notes`, `tags`.
2. Edit `scripts/update_pubs.py` and update `MY_NAME` to your name (for bolding).
3. Run the script:
   ```bash
   python3 scripts/update_pubs.py
   ```
   This will automatically generate `_data/publications.yml` and individual BibTeX files in `assets/bibs/`.

### 4. Customization

- **Intro Animation**: Edit `assets/js/intro-animation.js` to change the typing text.
- **Publication Filters**: Uncomment the filter section in `_includes/publications.md` and update the buttons to match your tags.

### 5. Deployment

This theme is designed to be hosted on GitHub Pages.

1. Go to your repository settings on GitHub.
2. Navigate to "Pages".
3. Select the `main` branch as the source.
4. Your site will be live at `https://yourusername.github.io/repository-name/`.

## License

This project is licensed under the MIT License.

## Acknowledgements

This theme is based on [Minimal Light](https://github.com/yaoyao-liu/minimal-light).
