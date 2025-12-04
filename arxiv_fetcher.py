#!/usr/bin/env python3
"""
arXiv Paper Fetcher Tool
每天自动从 arXiv 获取更新的论文，并筛选出包含特定关键词的论文
"""

import arxiv
import json
import os
from datetime import datetime, timedelta
from typing import List, Dict, Set
import logging
from pathlib import Path

# 配置日志
import sys

# 设置控制台输出编码为 UTF-8（Windows 兼容）
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('arxiv_fetcher.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class ArxivPaperFetcher:
    """arXiv 论文抓取和筛选工具"""
    
    def __init__(self, data_dir: str = None):
        """
        初始化抓取工具
        
        Args:
            data_dir: 数据存储目录，如果为 None 则使用带日期的目录名
        """
        # 如果没有指定目录，使用带日期的目录名
        if data_dir is None:
            date_str = datetime.now().strftime("%Y.%m.%d")
            data_dir = f"paper_data_{date_str}"
        
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(exist_ok=True)
        
        # 关键词列表（不区分大小写）
        # 注意：Video Generation 和 LLM Training 需要额外检查 system 相关关键词
        self.keywords = [
            "KV cache",
            "KV Cache",
            "kv cache",
            "KVCache",
            "LLM inference",
            "llm inference",
            "large language model inference",
            "LLM training",
            "llm training",
            "large language model training",
            "LLM communication",
            "llm communication",
            "communication optimization",
            "communication efficient",
            "allreduce",
            "all-gather",
            "collective communication",
            "video generation",
            "video synthesis",
            "video generation model"  # Video Generation 需要 system 相关
        ]
        
        # System 相关关键词（用于 RL 和 Video Generation 的额外筛选）
        self.system_keywords = [
            "system",
            "systems",
            "architecture",
            "framework",
            "platform",
            "infrastructure",
            "deployment",
            "serving",
            "serving system",
            "inference system",
            "training system",
            "runtime",
            "engine",
            "pipeline"
        ]
        
        # 已记录的论文ID集合（用于去重）
        self.recorded_papers_file = self.data_dir / "recorded_papers.json"
        self.recorded_paper_ids = self._load_recorded_papers()
    
    def _load_recorded_papers(self) -> Set[str]:
        """加载已记录的论文ID"""
        if self.recorded_papers_file.exists():
            try:
                with open(self.recorded_papers_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    return set(data.get('paper_ids', []))
            except Exception as e:
                logger.warning(f"加载已记录论文失败: {e}")
                return set()
        return set()
    
    def _save_recorded_papers(self):
        """保存已记录的论文ID"""
        try:
            data = {
                'paper_ids': list(self.recorded_paper_ids),
                'last_updated': datetime.now().isoformat()
            }
            with open(self.recorded_papers_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            logger.error(f"保存已记录论文失败: {e}")
    
    def _check_keywords(self, paper: arxiv.Result) -> bool:
        """
        检查论文是否包含关键词
        
        Args:
            paper: arxiv 论文对象
            
        Returns:
            如果包含关键词返回 True，否则返回 False
        """
        import re
        # 检查标题和摘要
        text_to_check = f"{paper.title} {paper.summary}".lower()
        
        # 检查 KV Cache 和 LLM Inference（不需要 system 限制）
        if any(kw in text_to_check for kw in ["kv cache", "kvcache"]):
            return True
        
        if any(kw in text_to_check for kw in ["llm inference", "large language model inference"]):
            return True
        
        # LLM Training 必须包含 system 相关关键词
        training_keywords = ["llm training", "large language model training"]
        if any(train_kw in text_to_check for train_kw in training_keywords):
            if any(sys_kw in text_to_check for sys_kw in self.system_keywords):
                return True
        
        # LLM Communication 优化相关
        comm_keywords = [
            "llm communication",
            "communication optimization",
            "communication efficient",
            "allreduce",
            "all-gather",
            "collective communication",
            "gradient communication",
            "communication compression"
        ]
        if any(comm_kw in text_to_check for comm_kw in comm_keywords):
            return True
        
        # Video Generation 必须包含 system 相关关键词
        video_keywords = ["video generation", "video synthesis", "video generation model"]
        if any(video_kw in text_to_check for video_kw in video_keywords):
            # 检查是否包含 system 相关关键词
            if any(sys_kw in text_to_check for sys_kw in self.system_keywords):
                return True
        
        return False
    
    def _categorize_paper(self, paper: arxiv.Result) -> List[str]:
        """
        对论文进行分类
        
        Args:
            paper: arxiv 论文对象
            
        Returns:
            分类标签列表
        """
        categories = []
        text = f"{paper.title} {paper.summary}".lower()
        
        if any(kw in text for kw in ["kv cache", "kvcache"]):
            categories.append("KV Cache")
        
        if any(kw in text for kw in ["llm inference", "large language model inference"]):
            categories.append("LLM Inference")
        
        # LLM Training 必须包含 system 相关关键词
        training_keywords = ["llm training", "large language model training"]
        if any(train_kw in text for train_kw in training_keywords):
            if any(sys_kw in text for sys_kw in self.system_keywords):
                categories.append("LLM Training (System)")
        
        # LLM Communication 优化相关
        comm_keywords = [
            "llm communication",
            "communication optimization",
            "communication efficient",
            "allreduce",
            "all-gather",
            "collective communication",
            "gradient communication",
            "communication compression"
        ]
        if any(comm_kw in text for comm_kw in comm_keywords):
            categories.append("LLM Communication")
        
        # Video Generation 必须包含 system 相关关键词
        video_keywords = ["video generation", "video synthesis", "video generation model"]
        if any(video_kw in text for video_kw in video_keywords):
            if any(sys_kw in text for sys_kw in self.system_keywords):
                categories.append("Video Generation (System)")
        
        return categories if categories else ["Other"]
    
    def fetch_daily_papers(self, days_back: int = 1, max_results: int = 1000) -> List[Dict]:
        """
        获取最近几天的论文
        
        Args:
            days_back: 回溯天数，默认1天（今天）
            max_results: 最大结果数
            
        Returns:
            筛选后的论文列表
        """
        logger.info(f"开始获取最近 {days_back} 天的 arXiv 论文...")
        
        # 计算日期范围
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days_back)
        
        # 构建查询：获取最近更新的论文
        # arXiv 使用日期格式：YYYYMMDD
        date_str = start_date.strftime("%Y%m%d")
        query = f"submittedDate:[{date_str}000000 TO {end_date.strftime('%Y%m%d')}235959]"
        
        logger.info(f"查询条件: {query}")
        
        # 搜索论文
        search = arxiv.Search(
            query=query,
            max_results=max_results,
            sort_by=arxiv.SortCriterion.SubmittedDate,
            sort_order=arxiv.SortOrder.Descending
        )
        
        matched_papers = []
        total_checked = 0
        
        try:
            for paper in arxiv.Client().results(search):
                total_checked += 1
                
                # 跳过已记录的论文
                if paper.entry_id in self.recorded_paper_ids:
                    continue
                
                # 检查关键词
                if self._check_keywords(paper):
                    categories = self._categorize_paper(paper)
                    paper_info = {
                        'id': paper.entry_id,
                        'arxiv_id': paper.entry_id.split('/')[-1],
                        'title': paper.title,
                        'authors': [author.name for author in paper.authors],
                        'summary': paper.summary,
                        'published': paper.published.isoformat(),
                        'updated': paper.updated.isoformat(),
                        'categories': paper.categories,
                        'tags': categories,
                        'pdf_url': paper.pdf_url,
                        'arxiv_url': paper.entry_id,
                        'found_date': datetime.now().isoformat()
                    }
                    matched_papers.append(paper_info)
                    self.recorded_paper_ids.add(paper.entry_id)
                    
                    logger.info(f"找到匹配论文: {paper.title[:60]}...")
                    logger.info(f"  分类: {', '.join(categories)}")
                    logger.info(f"  arXiv ID: {paper.entry_id.split('/')[-1]}")
        
        except Exception as e:
            logger.error(f"获取论文时出错: {e}")
            raise
        
        logger.info(f"共检查 {total_checked} 篇论文，找到 {len(matched_papers)} 篇匹配论文")
        
        return matched_papers
    
    def save_papers(self, papers: List[Dict], filename: str = None):
        """
        保存论文信息到文件
        
        Args:
            papers: 论文信息列表
            filename: 文件名，如果为 None 则使用日期命名
        """
        if not papers:
            logger.info("没有新论文需要保存")
            return
        
        if filename is None:
            date_str = datetime.now().strftime("%Y%m%d")
            filename = f"papers_{date_str}.json"
        
        filepath = self.data_dir / filename
        
        # 如果文件已存在，合并数据
        existing_papers = []
        if filepath.exists():
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    existing_data = json.load(f)
                    existing_papers = existing_data.get('papers', [])
            except Exception as e:
                logger.warning(f"读取已有文件失败: {e}")
        
        # 合并并去重
        all_papers = existing_papers + papers
        seen_ids = set()
        unique_papers = []
        for paper in all_papers:
            if paper['id'] not in seen_ids:
                seen_ids.add(paper['id'])
                unique_papers.append(paper)
        
        # 保存
        data = {
            'fetch_date': datetime.now().isoformat(),
            'total_papers': len(unique_papers),
            'papers': unique_papers
        }
        
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            logger.info(f"已保存 {len(unique_papers)} 篇论文到 {filepath}")
        except Exception as e:
            logger.error(f"保存论文失败: {e}")
            raise
        
        # 更新已记录论文列表
        self._save_recorded_papers()
    
    def generate_markdown_report(self, papers: List[Dict], output_file: str = None):
        """
        生成 Markdown 格式的报告，为每个分类生成单独的文件
        
        Args:
            papers: 论文信息列表
            output_file: 总览文件路径（如果为 None 则自动生成）
        """
        if not papers:
            logger.info("没有论文需要生成报告")
            return
        
        date_str = datetime.now().strftime("%Y%m%d")
        
        # 按分类组织论文
        papers_by_category = {}
        for paper in papers:
            tags = paper.get('tags', ['Other'])
            for tag in tags:
                if tag not in papers_by_category:
                    papers_by_category[tag] = []
                papers_by_category[tag].append(paper)
        
        # 定义分类顺序
        category_order = [
            "KV Cache",
            "LLM Inference",
            "LLM Training (System)",
            "LLM Communication",
            "Video Generation (System)"
        ]
        
        # 为每个分类生成单独的文件
        generated_files = []
        for category in category_order:
            if category in papers_by_category:
                category_papers = papers_by_category[category]
                
                # 生成文件名（移除特殊字符，不加日期）
                safe_category_name = category.replace(" ", "_").replace("(", "").replace(")", "").replace("/", "_")
                category_file = f"{safe_category_name}.md"
                category_filepath = self.data_dir / category_file
                
                # 生成该分类的 Markdown 内容
                md_content = f"""# {category} - arXiv 论文报告

**生成时间**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

**分类**: {category}

**论文数量**: {len(category_papers)} 篇

---

"""
                
                for idx, paper in enumerate(category_papers, 1):
                    authors_str = ", ".join(paper['authors'][:5])
                    if len(paper['authors']) > 5:
                        authors_str += f" et al. ({len(paper['authors'])} authors)"
                    
                    # 显示所有标签
                    all_tags = paper.get('tags', [])
                    tags_display = ', '.join(all_tags) if all_tags else 'Other'
                    
                    md_content += f"""## {idx}. {paper['title']}

- **arXiv ID**: [{paper['arxiv_id']}]({paper['arxiv_url']})
- **作者**: {authors_str}
- **发布时间**: {paper['published']}
- **arXiv分类**: {', '.join(paper['categories'])}
- **标签**: {tags_display}
- **PDF**: [下载链接]({paper['pdf_url']})

**摘要**:
{paper['summary']}

---

"""
                
                try:
                    with open(category_filepath, 'w', encoding='utf-8') as f:
                        f.write(md_content)
                    logger.info(f"已生成分类报告: {category_filepath}")
                    generated_files.append((category, category_file))
                except Exception as e:
                    logger.error(f"生成分类报告失败 ({category}): {e}")
        
        # 生成总览文件
        if output_file is None:
            output_file = "arxiv_report.md"
        
        overview_filepath = self.data_dir / output_file
        
        # 生成总览内容
        category_summary = []
        for category in category_order:
            if category in papers_by_category:
                count = len(papers_by_category[category])
                # 生成文件名（不加日期）
                safe_category_name = category.replace(" ", "_").replace("(", "").replace(")", "").replace("/", "_")
                category_file = f"{safe_category_name}.md"
                category_summary.append(f"- **[{category}]({category_file})**: {count} 篇")
        
        overview_content = f"""# arXiv 论文筛选报告 - 总览

**生成时间**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

**总计**: {len(papers)} 篇论文

## 📊 分类统计

{chr(10).join(category_summary)}

---

## 📁 详细报告

每个分类的详细报告已单独生成，请点击上方链接查看。

"""
        
        try:
            with open(overview_filepath, 'w', encoding='utf-8') as f:
                f.write(overview_content)
            logger.info(f"已生成总览报告: {overview_filepath}")
        except Exception as e:
            logger.error(f"生成总览报告失败: {e}")
            raise
    
    def _print_category_summary(self, papers: List[Dict]):
        """
        打印分类统计摘要
        
        Args:
            papers: 论文信息列表
        """
        # 按分类组织论文
        papers_by_category = {}
        for paper in papers:
            tags = paper.get('tags', ['Other'])
            for tag in tags:
                if tag not in papers_by_category:
                    papers_by_category[tag] = []
                papers_by_category[tag].append(paper)
        
        # 定义分类显示顺序（与 generate_markdown_report 保持一致）
        category_order = [
            "KV Cache",
            "LLM Inference",
            "LLM Training (System)",
            "LLM Communication",
            "Video Generation (System)"
        ]
        
        logger.info("")
        logger.info("=" * 60)
        logger.info("📊 论文分类统计")
        logger.info("=" * 60)
        
        for category in category_order:
            if category in papers_by_category:
                category_papers = papers_by_category[category]
                logger.info(f"\n📁 {category}: {len(category_papers)} 篇")
                logger.info("-" * 60)
                for idx, paper in enumerate(category_papers, 1):
                    # 显示所有标签
                    all_tags = paper.get('tags', [])
                    tags_str = ', '.join(all_tags) if len(all_tags) > 1 else ''
                    tags_display = f" [{tags_str}]" if tags_str else ""
                    logger.info(f"  {idx}. {paper['title'][:70]}...{tags_display}")
                    logger.info(f"     arXiv ID: {paper['arxiv_id']}")
        
        logger.info("")
        logger.info("=" * 60)
    
    def run_daily_fetch(self, days_back: int = 1, generate_report: bool = True):
        """
        执行每日抓取任务
        
        Args:
            days_back: 回溯天数
            generate_report: 是否生成 Markdown 报告
        """
        logger.info("=" * 60)
        logger.info("开始执行每日 arXiv 论文抓取任务")
        logger.info("=" * 60)
        
        try:
            # 获取论文
            papers = self.fetch_daily_papers(days_back=days_back)
            
            if papers:
                # 保存 JSON 数据
                self.save_papers(papers)
                
                # 生成 Markdown 报告
                if generate_report:
                    self.generate_markdown_report(papers)
                
                # 输出分类统计
                self._print_category_summary(papers)
                
                logger.info(f"任务完成！共找到 {len(papers)} 篇新论文")
            else:
                logger.info("没有找到新的匹配论文")
        
        except Exception as e:
            logger.error(f"任务执行失败: {e}")
            raise


def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(description='arXiv 论文抓取工具')
    parser.add_argument(
        '--days',
        type=int,
        default=1,
        help='回溯天数（默认：1，即今天）'
    )
    parser.add_argument(
        '--data-dir',
        type=str,
        default=None,
        help='数据存储目录（默认：paper_data_YYYY.MM.DD，自动添加日期）'
    )
    parser.add_argument(
        '--no-report',
        action='store_true',
        help='不生成 Markdown 报告'
    )
    
    args = parser.parse_args()
    
    # 创建抓取工具并执行
    fetcher = ArxivPaperFetcher(data_dir=args.data_dir)
    fetcher.run_daily_fetch(
        days_back=args.days,
        generate_report=not args.no_report
    )


if __name__ == "__main__":
    main()

