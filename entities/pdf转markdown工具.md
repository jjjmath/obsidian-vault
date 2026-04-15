---
title: PDF转Markdown工具
created: 2026-04-15
updated: 2026-04-15
type: entity
tags: [技术工具, PDF转换, OCR, 自动化, 教学资源]
sources: [raw/articles/paddleocr-vl-api文档.md]
---

# PDF转Markdown工具

> 专门为数学教师设计的PDF文档转换工具，特别优化数学公式识别。

## 概述
这是一个基于paddleocr-vl API的PDF转Markdown工具，专门用于将数学试卷、教学资料等PDF文档转换为Markdown格式，特别优化了数学公式的识别和LaTeX格式输出。

## 核心特性

### 1. 数学公式识别
- 专门优化数学公式识别
- 输出LaTeX格式公式
- 支持复杂公式结构

### 2. 高性能转换
- 使用paddleocr-vl API
- 转换速度：约5.7秒/页
- 支持批量处理

### 3. 教学友好
- 保留原始文档结构
- 支持图片提取
- 输出Obsidian兼容格式

## 技术架构

### API配置
```yaml
API URL: https://oe16c1acp2yem7s9.aistudio-app.com/layout-parsing
API Token: fb078b2bdee49b30acb300bb8f875208d2d012b7
文件类型: 0 (PDF) / 1 (图像)
```

### 工具集
- **主转换脚本**: `pdf_to_markdown.py`
- **Web界面**: Flask应用，支持文件上传
- **分割工具**: 
  - `split_exam.py` - 试卷拆分（一题一文件）
  - `split_questions.py` - 题库分割（带YAML frontmatter）
- **启动器**: `launcher.py` - 图形化菜单界面

## 使用场景

### 1. 试卷数字化
将纸质数学试卷转换为数字格式，便于编辑和分享。

### 2. 题库建设
将大量PDF题库转换为结构化Markdown文件，建立教学知识库。

### 3. 教学资源整理
整理历年的教学资料，建立可搜索的文档库。

## 工作流程
```
PDF文档 → paddleocr-vl转换 → Markdown输出 → 题库分割 → Obsidian知识库
```

## 相关工具
- [[Obsidian]] - 知识管理工具
- [[Git]] - 版本控制
- [[Python]] - 开发语言
- [[Flask]] - Web框架

## 作者
- **许宏杰（老许）** - 高中数学教师，26年教龄
- 专注于教学资源数字化和知识管理

## 备注
这是教师个人开发的教学工具，专门为解决数学教学中的文档转换问题而设计。