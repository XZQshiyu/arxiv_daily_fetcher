#!/usr/bin/env python3
"""
测试配置文件功能
"""

import sys
import json
from pathlib import Path

# 添加 src 目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from arxiv_fetcher import ArxivPaperFetcher


def test_config_loading():
    """测试配置文件加载"""
    print("=" * 60)
    print("测试 1: 配置文件加载")
    print("=" * 60)
    
    # 测试加载存在的配置文件
    fetcher1 = ArxivPaperFetcher(data_dir="test_output", config_file="config.json")
    print(f"✓ 成功加载配置文件")
    print(f"  分类数量: {len(fetcher1.categories_config)}")
    print(f"  System关键词数量: {len(fetcher1.system_keywords)}")
    print(f"  关键词组数量: {len(fetcher1.keywords_map)}")
    
    # 测试默认配置（不存在的配置文件）
    fetcher2 = ArxivPaperFetcher(data_dir="test_output", config_file="nonexistent.json")
    print(f"\n✓ 使用默认配置（配置文件不存在）")
    print(f"  分类数量: {len(fetcher2.categories_config)}")
    print(f"  System关键词数量: {len(fetcher2.system_keywords)}")
    
    return fetcher1


def test_keyword_matching(fetcher):
    """测试关键词匹配逻辑"""
    print("\n" + "=" * 60)
    print("测试 2: 关键词匹配逻辑")
    print("=" * 60)
    
    # 创建模拟论文对象
    class MockPaper:
        def __init__(self, title, summary):
            self.title = title
            self.summary = summary
            self.entry_id = "test/1234"
            self.authors = []
            self.published = None
            self.updated = None
            self.categories = []
            self.pdf_url = ""
    
    test_cases = [
        {
            "title": "Efficient KV Cache Management for LLM Inference",
            "summary": "This paper presents a novel approach to KV cache optimization.",
            "expected_match": True,
            "expected_categories": ["KV Cache", "LLM Inference"]
        },
        {
            "title": "FFTrainer: Fast Failover in Large-Language Model Training System",
            "summary": "We propose a system for robust LLM training with fast failover.",
            "expected_match": True,
            "expected_categories": ["LLM Training (System)"]
        },
        {
            "title": "Communication Optimization for Distributed Training",
            "summary": "This work focuses on allreduce and collective communication optimization.",
            "expected_match": True,
            "expected_categories": ["LLM Communication"]
        },
        {
            "title": "Video Generation System for Real-time Applications",
            "summary": "We present a novel video generation system with efficient runtime.",
            "expected_match": True,
            "expected_categories": ["Video Generation (System)"]
        },
        {
            "title": "Random Paper About Machine Learning",
            "summary": "This paper discusses general machine learning techniques.",
            "expected_match": False,
            "expected_categories": []
        }
    ]
    
    passed = 0
    failed = 0
    
    for i, test_case in enumerate(test_cases, 1):
        paper = MockPaper(test_case["title"], test_case["summary"])
        matches = fetcher._check_keywords(paper)
        categories = fetcher._categorize_paper(paper)
        
        # 移除 "Other" 分类（如果存在）
        if "Other" in categories:
            categories.remove("Other")
        
        match_ok = matches == test_case["expected_match"]
        categories_ok = set(categories) == set(test_case["expected_categories"])
        
        if match_ok and categories_ok:
            print(f"✓ 测试 {i}: {test_case['title'][:50]}...")
            print(f"    匹配: {matches}, 分类: {categories}")
            passed += 1
        else:
            print(f"✗ 测试 {i}: {test_case['title'][:50]}...")
            print(f"    期望匹配: {test_case['expected_match']}, 实际: {matches}")
            print(f"    期望分类: {test_case['expected_categories']}, 实际: {categories}")
            failed += 1
    
    print(f"\n测试结果: {passed} 通过, {failed} 失败")
    return failed == 0


def test_config_structure(fetcher):
    """测试配置结构"""
    print("\n" + "=" * 60)
    print("测试 3: 配置结构验证")
    print("=" * 60)
    
    errors = []
    
    # 检查所有分类的关键词组是否存在
    for category_name, category_config in fetcher.categories_config.items():
        keyword_group = category_config.get('keywords')
        if keyword_group not in fetcher.keywords_map:
            errors.append(f"分类 '{category_name}' 引用的关键词组 '{keyword_group}' 不存在")
        requires_system = category_config.get('requires_system')
        if not isinstance(requires_system, bool):
            errors.append(f"分类 '{category_name}' 的 'requires_system' 必须是布尔值")
    
    # 检查关键词组不为空
    for group_name, keywords in fetcher.keywords_map.items():
        if not keywords:
            errors.append(f"关键词组 '{group_name}' 为空")
        if not isinstance(keywords, list):
            errors.append(f"关键词组 '{group_name}' 必须是列表")
    
    # 检查 system_keywords 不为空
    if not fetcher.system_keywords:
        errors.append("system_keywords 不能为空")
    
    if errors:
        print("✗ 发现配置错误:")
        for error in errors:
            print(f"  - {error}")
        return False
    else:
        print("✓ 配置结构验证通过")
        return True


def test_config_file_format():
    """测试配置文件格式"""
    print("\n" + "=" * 60)
    print("测试 4: 配置文件格式验证")
    print("=" * 60)
    
    config_file = Path(__file__).parent.parent / "config.json"
    
    if not config_file.exists():
        print("✗ 配置文件不存在")
        return False
    
    try:
        with open(config_file, 'r', encoding='utf-8') as f:
            config = json.load(f)
        
        # 检查必需字段
        required_fields = ['keywords', 'system_keywords', 'categories']
        for field in required_fields:
            if field not in config:
                print(f"✗ 缺少必需字段: {field}")
                return False
        
        print("✓ 配置文件格式正确")
        print(f"  关键词组: {list(config['keywords'].keys())}")
        print(f"  分类: {list(config['categories'].keys())}")
        return True
        
    except json.JSONDecodeError as e:
        print(f"✗ JSON 格式错误: {e}")
        return False
    except Exception as e:
        print(f"✗ 读取配置文件失败: {e}")
        return False


def main():
    """主测试函数"""
    print("\n" + "=" * 60)
    print("配置文件功能测试")
    print("=" * 60)
    
    # 测试1: 配置加载
    fetcher = test_config_loading()
    
    # 测试2: 关键词匹配
    match_ok = test_keyword_matching(fetcher)
    
    # 测试3: 配置结构
    structure_ok = test_config_structure(fetcher)
    
    # 测试4: 配置文件格式
    format_ok = test_config_file_format()
    
    # 总结
    print("\n" + "=" * 60)
    print("测试总结")
    print("=" * 60)
    
    all_passed = match_ok and structure_ok and format_ok
    
    if all_passed:
        print("✓ 所有测试通过！")
        return 0
    else:
        print("✗ 部分测试失败")
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(main())

