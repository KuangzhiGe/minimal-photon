# Minimal Photon 主题

一个简洁、优雅且响应式的学术主页模板，适合研究人员和学生使用。基于 [Minimal Light](https://github.com/yaoyao-liu/minimal-light) 主题开发。

## 特性

- **简洁设计**：极简主义美学，非常适合学术展示。
- **响应式**：在桌面和移动设备上都能完美显示。
- **易于配置**：大多数设置都在 `_config.yml` 中。
- **数据驱动**：通过 YAML 文件管理出版物、新闻和经历。
- **开场动画**：时尚的打字机开场动画。
- **出版物筛选**：（可选）按标签筛选出版物。

## 快速开始

### 1. Fork 和 Clone

Fork 本仓库并将其克隆到你的本地机器。

### 2. 配置

编辑 `_config.yml` 以更新你的个人信息：

- **基本信息**：姓名、职位、所属机构、邮箱。
- **SEO**：关键词、描述。
- **社交链接**：GitHub、Google Scholar、LinkedIn 等。
- **图片**：更新 `avatar`（头像）和 `favicon`（图标）路径。
- **分析**：（可选）取消注释 `google_analytics` 并添加你的 ID。

### 3. 内容

#### 主页 (`index.md`)
编辑 `index.md` 以更新你的“关于我”、“研究兴趣”和“杂项”部分。
你也可以在 `index.md` 底部通过替换注释掉的代码块来添加访客地图（例如 ClustrMaps）。

#### 经历 (`_data/experience.yml`)
添加你的教育和工作经历。

```yaml
- title: "大学名称"
  details: "(2022.09-至今) 计算机科学学士"
  image: ./assets/img/logo.png
  image_width: 40px
  image_height: 40px
```

#### 新闻 (`_data/news.yml`)
添加你的最新新闻。

```yaml
- date: 2024年12月
  content: 📃 论文被 CVPR 接收！
```

#### 出版物 (`_data/publications.yml`)
你可以通过两种方式管理你的出版物：

**选项 1：手动编辑（简单）**
直接编辑 `_data/publications.yml`。

```yaml
- title: "论文标题"
  authors: "<strong>你的名字</strong>, 合著者"
  url: "pdf链接"
  code: "代码链接"
  page: "项目主页链接"
  image: "./assets/img/pub/image.png"
  notes: "会议名称"
  tags: "标签1, 标签2"
```

**选项 2：使用 BibTeX（高级）**
1. 将你的 BibTeX 条目添加到 `_data/references.bib`。
   - 支持的字段：`title`, `author`, `url`, `code`, `page`, `image`, `notes`, `tags`。
2. 编辑 `scripts/update_pubs.py` 并将 `MY_NAME` 更新为你的名字（用于自动加粗）。
3. 运行脚本：
   ```bash
   python3 scripts/update_pubs.py
   ```
   这将自动生成 `_data/publications.yml` 和 `assets/bibs/` 中的单独 BibTeX 文件。

### 4. 自定义

- **开场动画**：编辑 `assets/js/intro-animation.js` 以更改打字文本。
- **出版物筛选**：取消注释 `_includes/publications.md` 中的筛选部分，并更新按钮以匹配你的标签。

### 5. 部署

本主题设计用于在 GitHub Pages 上托管。

1. 转到 GitHub 上的仓库设置。
2. 导航到 "Pages"。
3. 选择 `main` 分支作为源。
4. 你的网站将在 `https://yourusername.github.io/repository-name/` 上线。

## 许可证

本项目采用 MIT 许可证。

## 致谢

本主题基于 [Minimal Light](https://github.com/yaoyao-liu/minimal-light)。
