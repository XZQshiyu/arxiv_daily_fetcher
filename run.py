#!/usr/bin/env python3
"""
arXiv Paper Fetcher - 入口脚本
"""

import sys
from pathlib import Path

# 添加 src 目录到 Python 路径
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

# 导入并运行主函数
from arxiv_fetcher import main

if __name__ == "__main__":
    main()

