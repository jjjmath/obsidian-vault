# Wiki Schema

## Domain
**高中数学教学知识库 (许宏杰老师，26年教龄)**
- **核心内容**：高中数学课程标准要求的所有知识点
- **教学体系**：26年教学经验总结的教学方法和策略
- **考试导向**：高考数学考点分析与备考指南
- **资源建设**：教学课件、试卷、习题、教案等资源
- **技术应用**：支持教学的数字工具和工作流
- **专业成长**：数学教师专业发展与反思

**边界说明**：
1. 聚焦高中数学教学，不涉及大学数学或竞赛数学的深度内容
2. 以教学实践为导向，强调可操作性
3. 结合高考要求，注重考点和应试技巧
4. 整合技术工具，提高教学效率

## Conventions
- **文件命名**: 小写，使用连字符，无空格 (例如：`function-derivative.md`)
- **文件格式**: 每个wiki页面必须有YAML frontmatter（见下方）
- **双向链接**: 使用`[[wikilinks]]`链接页面（每页至少2个出站链接）
- **更新规则**: 更新页面时，必须更新`updated`日期
- **索引规则**: 每个新页面必须添加到`index.md`的相应分类下
- **日志规则**: 每个操作必须追加到`log.md`
- **中文优先**: 文件名和内容使用中文，便于检索

## Frontmatter
```yaml
---
title: 页面标题
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | summary
tags: [从下方标签分类中选择]
sources: [raw/articles/来源文件.md]
---
```

## Tag Taxonomy
### 数学内容
- 代数：algebra, function, equation, inequality, sequence
- 几何：geometry, triangle, circle, solid-geometry
- 函数：function, derivative, integral, limit
- 概率统计：probability, statistics, distribution
- 向量：vector, matrix, transformation

### 教学维度
- 教学法：pedagogy, methodology, classroom-management
- 考点：exam-point, college-entrance-exam
- 难度：easy, medium, hard, challenge
- 题型：multiple-choice, fill-in-blank, proof, calculation

### 资源类型
- 课件：courseware, slide, ppt
- 试卷：exam-paper, test, quiz
- 教案：lesson-plan, teaching-design
- 素材：material, example, exercise

### 技术工具
- obsidian：obsidian, note-taking, knowledge-management
- pdf-conversion：pdf, ocr, conversion
- 技术：technology, ai, tool

**规则**: 每个页面上的标签必须来自此分类。如果需要新标签，先在此处添加，然后使用。

## Page Thresholds
- **创建新页面**: 当实体/概念出现在2+个来源中，或在一个来源中处于核心位置
- **更新现有页面**: 当来源提及已有的内容
- **不创建页面**: 对于仅提及一次、次要细节或领域外的内容
- **拆分页面**: 当页面超过~200行时，拆分为子主题并添加交叉链接
- **归档页面**: 当内容完全被新内容取代时，移动到`_archive/`并从索引中移除

## Entity Pages
每个重要实体的页面。包括：
- 概述 / 是什么
- 关键事实和日期
- 与其他实体的关系（[[wikilinks]]）
- 来源引用

## Concept Pages
每个概念或主题的页面。包括：
- 定义 / 解释
- 当前知识状态
- 开放问题或争议
- 相关概念（[[wikilinks]]）

## Comparison Pages
对比分析页面。包括：
- 对比内容和原因
- 对比维度（推荐表格格式）
- 结论或综合
- 来源

## Update Policy
当新信息与现有内容冲突时：
1. 检查日期 - 新来源通常替代旧来源
2. 如果真正矛盾，注明两种观点及日期和来源
3. 在frontmatter中标记矛盾：`contradictions: [页面名称]`
4. 在lint报告中标记供用户审查

## 中文命名规则
- 优先使用中文文件名，便于在Obsidian中搜索
- 特殊术语可用英文，如`derivative.md`
- 保持文件名简洁、描述性

## 与现有Obsidian文件的兼容性
- 现有文件保持原状，不会被修改
- 新文件遵循此schema
- 逐步将重要内容迁移到wiki结构