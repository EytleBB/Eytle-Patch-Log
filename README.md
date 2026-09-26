# Eytle Patch Log

This repository owns the writing published on [eytle.cn](https://eytle.cn/patchlog).
The website code lives in [eytlebb.github.io](https://github.com/EytleBB/eytlebb.github.io).

## 添加日志

1. 在 `logs/YYYY-MM-DD.txt` 中写正文。`logs/example.txt` 是原有示例，不列入正式日志。
2. 执行 `python3 scripts/update-index.py`，自动生成按日期倒序排列的 `logs/index.json`。
3. 检查并提交日志和索引，不要手工改索引。

克隆后执行 `git config core.hooksPath .githooks` 可在提交前自动刷新索引。
新增、修改和删除文章都只在本仓库操作。

## 网站使用

主站的 `content-sources.json` 固定本仓库的提交版本。发布会话先发布本仓库，
再更新主站的内容版本并组装网站。浏览器仍读取 `/logs/`，不需要访问 GitHub。
迁入的文件保留原始内容与文件名；主站历史提交未被改写。
