# arXiv 论文抓取工具

这是一个自动从 arXiv 获取并筛选相关论文的工具，每天自动查找包含以下关键词的新论文：

- **KV Cache** / **KV cache** / **KVCache**
- **LLM Inference** / **Large Language Model Inference**
- **LLM Training (System)** - 需要同时包含 system 相关关键词
- **LLM Communication** - 通信优化相关（allreduce, all-gather, collective communication 等）
- **Video Generation (System)** - 需要同时包含 system 相关关键词

## 功能特性

- ✅ 每日自动抓取 arXiv 最新论文
- ✅ 智能关键词匹配（标题和摘要）
- ✅ 自动分类和标签
- ✅ 去重机制（避免重复记录）
- ✅ JSON 数据存储
- ✅ 每个分类生成独立的 Markdown 报告文件
- ✅ 总览报告文件（包含所有分类的链接）
- ✅ 日志记录
- ✅ 按日期组织文件夹（文件夹名包含日期，文件名不包含）

## 项目结构

```
arxiv_paper_fetcher/
├── src/                    # 源代码目录
│   ├── arxiv_fetcher.py   # 主程序
│   └── setup_daily_task.py # 定时任务设置脚本
├── test/                   # 测试文件目录
├── result/                 # 结果输出目录（按日期组织）
│   └── paper_data_YYYY.MM.DD/
├── config.json            # 配置文件（可选）
├── requirements.txt       # Python 依赖
└── README.md             # 说明文档
```

## 安装

1. 安装依赖：

```bash
pip install -r requirements.txt
```

## 使用方法

### 基本使用

```bash
# 获取今天的论文（默认）- 使用入口脚本（推荐）
python run.py

# 或者直接运行源文件
python src/arxiv_fetcher.py

# 获取最近3天的论文
python run.py --days 3

# 指定数据存储目录（默认会保存到 result/ 目录）
python run.py --data-dir my_papers

# 使用自定义配置文件
python run.py --config my_config.json

# 不生成 Markdown 报告
python run.py --no-report
```

### 配置文件

工具支持通过 JSON 配置文件自定义关键词和分类。如果配置文件不存在，将使用默认配置。

1. **复制示例配置文件**：
   ```bash
   cp config.json.example config.json
   ```

2. **编辑配置文件** (`config.json`)：
   - `keywords`: 定义各分类的关键词列表
   - `system_keywords`: 定义 system 相关关键词（用于需要 system 限制的分类）
   - `categories`: 定义分类及其配置（关键词组、是否需要 system 限制）

3. **配置文件示例** (`config.json.example`)：
   ```json
   {
     "keywords": {
       "kv_cache": ["KV cache", "KVCache"],
       "llm_inference": ["LLM inference", "large language model inference"]
     },
     "system_keywords": ["system", "architecture", "framework"],
     "categories": {
       "KV Cache": {
         "keywords": "kv_cache",
         "requires_system": false
       }
     }
   }
   ```

4. **添加新分类**：
   - 在 `keywords` 中添加新的关键词组
   - 在 `categories` 中添加新的分类配置
   - 分类名称会作为标签和文件名使用

### 作为 Python 模块使用

```python
import sys
from pathlib import Path

# 添加 src 目录到路径
sys.path.insert(0, str(Path(__file__).parent / "src"))

from arxiv_fetcher import ArxivPaperFetcher

# 创建抓取工具（使用默认配置，结果保存到 result/ 目录）
fetcher = ArxivPaperFetcher()

# 指定自定义数据目录
fetcher = ArxivPaperFetcher(data_dir="result/my_papers")

# 使用自定义配置文件
fetcher = ArxivPaperFetcher(config_file="my_config.json")

# 执行每日抓取
fetcher.run_daily_fetch(days_back=1, generate_report=True)
```

## 输出文件

工具会在 `result/paper_data_YYYY.MM.DD` 目录（或指定的数据目录）下生成以下文件：

### 分类报告文件（每个分类一个文件）
- `KV_Cache.md` - KV Cache 分类论文
- `LLM_Inference.md` - LLM Inference 分类论文
- `LLM_Training_System.md` - LLM Training (System) 分类论文
- `LLM_Communication.md` - LLM Communication 分类论文
- `Video_Generation_System.md` - Video Generation (System) 分类论文

### 其他文件
- `arxiv_report.md` - 总览报告（包含所有分类的统计和链接）
- `papers_YYYYMMDD.json` - JSON 格式的论文数据
- `recorded_papers.json` - 已记录论文ID（用于去重）
- `arxiv_fetcher.log` - 运行日志

**注意**：
- 文件夹名包含日期（如 `paper_data_2025.12.04`），但分类文件名不包含日期
- 默认输出目录为 `result/paper_data_YYYY.MM.DD/`
- 每天运行时会更新对应日期文件夹中的文件

## 定时任务设置

### Windows (任务计划程序)

1. 打开"任务计划程序"
2. 创建基本任务
3. 设置触发器：每天运行
4. 操作：启动程序
   - 程序：`python`
   - 参数：`D:\workspace\arxiv_paper_fetcher\src\arxiv_fetcher.py`
   - 起始于：`D:\workspace\arxiv_paper_fetcher`

或者使用提供的脚本：

```bash
python setup_daily_task.py
```

然后以管理员身份运行 PowerShell：

```powershell
schtasks /Create /TN "arXiv Paper Fetcher" /XML "arxiv_daily_task.xml" /F
```

### Linux/Mac (cron)

```bash
# 编辑 crontab
crontab -e

# 添加每天凌晨2点执行的任务
0 2 * * * cd /path/to/arxiv_paper_fetcher && python src/arxiv_fetcher.py >> /path/to/logs/arxiv.log 2>&1
```

## 分类说明

### KV Cache
- 匹配关键词：`kv cache`, `kvcache`
- 无额外限制

### LLM Inference
- 匹配关键词：`llm inference`, `large language model inference`
- 无额外限制

### LLM Training (System)
- 匹配关键词：`llm training`, `large language model training`
- **必须同时包含** system 相关关键词（system, architecture, framework, platform, infrastructure, deployment, runtime, engine, pipeline 等）

### LLM Communication
- 匹配关键词：`llm communication`, `communication optimization`, `communication efficient`, `allreduce`, `all-gather`, `collective communication`, `gradient communication`, `communication compression`
- 无额外限制

### Video Generation (System)
- 匹配关键词：`video generation`, `video synthesis`, `video generation model`
- **必须同时包含** system 相关关键词

## 自定义关键词

有两种方式自定义关键词：

### 方式一：使用配置文件（推荐）

1. 复制 `config.json.example` 为 `config.json`
2. 编辑 `config.json` 文件，修改关键词和分类配置
3. 运行工具时会自动加载配置文件

### 方式二：修改代码

编辑 `arxiv_fetcher.py` 中的 `_get_default_config()` 方法来修改默认配置：

1. **关键词列表**：修改 `keywords` 字典中的关键词组
2. **System 关键词**：修改 `system_keywords` 列表
3. **分类配置**：修改 `categories` 字典来添加或修改分类

配置文件格式说明：
- `keywords`: 关键词组字典，键为组名，值为关键词列表
- `system_keywords`: system 相关关键词列表
- `categories`: 分类配置字典，键为分类名称，值为配置对象
  - `keywords`: 引用的关键词组名
  - `requires_system`: 是否需要 system 限制（布尔值）

## 论文数据结构

每篇论文包含以下信息：

```json
{
  "id": "arxiv论文ID",
  "arxiv_id": "论文编号",
  "title": "论文标题",
  "authors": ["作者列表"],
  "summary": "摘要",
  "published": "发布时间",
  "updated": "更新时间",
  "categories": ["分类"],
  "tags": ["标签"],
  "pdf_url": "PDF下载链接",
  "arxiv_url": "arXiv页面链接",
  "found_date": "发现时间"
}
```

## 注意事项

- arXiv API 有速率限制，建议不要过于频繁地请求
- 每天运行一次即可获取最新论文
- 已记录的论文不会重复保存（基于论文ID去重）
- 文件夹按日期自动创建（格式：`result/paper_data_YYYY.MM.DD`）
- 分类文件名固定，每天运行时会更新对应日期文件夹中的文件
- 建议定期备份 `result/paper_data_*` 目录
- 配置文件路径相对于项目根目录
- LLM Training (System) 和 Video Generation (System) 需要同时包含 system 相关关键词才会被筛选


