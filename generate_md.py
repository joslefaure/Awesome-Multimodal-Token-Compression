import csv
import re
import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import urlparse

def get_arxiv_authors(arxiv_url):
    """
    从arXiv URL获取作者信息
    """
    if not arxiv_url or not arxiv_url.strip():
        return ""
    
    try:
        # 确保URL格式正确
        if 'arxiv.org' not in arxiv_url:
            return ""
        
        # 将PDF链接转换为abs链接
        if '/pdf/' in arxiv_url:
            arxiv_url = arxiv_url.replace('/pdf/', '/abs/')
        
        # 发送请求获取页面内容
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(arxiv_url, headers=headers, timeout=10)
        response.raise_for_status()
        
        # 解析HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # 查找作者信息
        authors_div = soup.find('div', class_='authors')
        if authors_div:
            authors = []
            # 提取所有作者链接
            author_links = authors_div.find_all('a')
            for link in author_links:
                author_name = link.get_text().strip()
                if author_name and author_name not in authors:
                    authors.append(author_name)
            
            if authors:
                # # 如果作者数量较多，只取前3个
                # if len(authors) > 3:
                #     return ", ".join(authors[:3]) + " et al."
                # else:
                #     return ", ".join(authors)
                return ", ".join(authors)
        
        # 备用方法：查找meta标签中的作者信息
        meta_authors = soup.find('meta', attrs={'name': 'citation_author'})
        if meta_authors:
            return meta_authors.get('content', '').strip()
        
        return ""
        
    except Exception as e:
        print(f"Error fetching authors from {arxiv_url}: {str(e)}")
        return ""

def get_cached_authors(cache_dict, arxiv_url):
    """
    带缓存的作者信息获取
    """
    if arxiv_url in cache_dict:
        return cache_dict[arxiv_url]
    
    authors = get_arxiv_authors(arxiv_url)
    cache_dict[arxiv_url] = authors
    
    # 添加延迟避免请求过快
    time.sleep(0.5)
    
    return authors

input_csv_path = "test.csv"

required_fields = ["Title", "Code", "arXiv", "Publish", "Author"]
output_list = []

# 作者信息缓存
authors_cache = {}

with open(input_csv_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        # use for pass some rows with empty fields (TODO@kele, keda)
        # if any(not row[field].strip() for field in required_fields):
        #     continue

        # for field_name, value in row.items():
        #     print(f"{field_name}: {value}")
        # exit(0)
        
        # 从arXiv URL获取作者信息
        arxiv_url = row['arXiv'].strip()
        # scraped_authors = get_cached_authors(authors_cache, arxiv_url) if arxiv_url else ""
        
        # 获取完整的 arXiv 编号用于排序
        paper_release_time = ""
        if arxiv_url:
            match = re.search(r'arxiv\.org/(?:abs|pdf)/(\d{4}\.\d+)', arxiv_url)
            if match:
                paper_release_time = match.group(1)  # 获取完整的编号，如 2301.12345
        
        entry = {
            'paper_name': row['Title'].strip(),
            'paper_url': arxiv_url,
            'github_url': row['Code'].strip(),
            # 'author_name': scraped_authors,  # 使用爬取的作者信息
            # 'image_path': 'figures/.png',
            'conference': row['Publish'].strip().replace(' ', '_').replace('-', '_'),
            'areas': row['Areas'].strip().split(','),
            'class_0': row['Class_0'].strip().split(','),
            'cost': row['Cost'].strip(),
            'paper_release_time': paper_release_time
        }
        if row['\ufeffPerson'].strip() == 'Sicheng Feng' \
        or entry['paper_name'] == '' \
        or entry['areas'] == ['LLM']:
            continue
        output_list.append(entry)

papers = output_list

star_format = '[![Star](https://img.shields.io/github/stars/{}.svg?style=social&label=Star)](https://github.com/{})'
conference_format = " [![Publish](https://img.shields.io/badge/{}-{}-blue)]()"
arxiv_format = " [![Arxiv](https://img.shields.io/badge/arXiv-{}-red)]()"
main_item_format = '[{}]({}) <br> {} |'
image_format = '<img width="1002" alt="image" src="{}"> |'
github_format = '[Github]({}) <br> '
paper_format = '[Paper]({})'

author_format = '{}'
area_format = " [![Area](https://img.shields.io/badge/{}-purple)]()"
class_0_format = " [![Type](https://img.shields.io/badge/{}-green)]()"
cost_format = " [![Cost](https://img.shields.io/badge/{}-yellow)]()"

month = time.strftime("%m", time.localtime())
day = time.strftime("%d", time.localtime())
timestamp = f"[//]: #{month}/{day}"

# 按照论文发布时间排序，从早到晚
papers = sorted(papers, key=lambda x: x['paper_release_time'] or '0000.00000')

for paper in papers:
    final_str = "* "
    if paper['conference'] and paper['conference'].lower() != 'arxiv':
        # 尝试从 conference 字符串中提取年份
        match = re.search(r'(\d{4})', paper['conference'])
        year = match.group(1) if match else ""
        conf_name = paper['conference'].replace('_' + year, '') if year else paper['conference']
        final_str += conference_format.format(conf_name, year) + " "
    elif paper['paper_url']:
        match = re.search(r'arxiv\.org/(?:abs|pdf)/(\d{4})', paper['paper_url'])
        if match:
            yymm = match.group(1)
            year = '20' + yymm[:2]
            month = yymm[2:]
            arxiv_time = f"{year}\.{month}"
        else:
            arxiv_time = ""
        final_str += arxiv_format.format(arxiv_time) + " "
    
    if paper['github_url']:
        github_item = '/'.join(paper['github_url'].split('/')[-2:])
        final_str += star_format.format(github_item, github_item) + " "
        
    final_str += "[{}]({})\n".format(
        paper['paper_name'], paper['paper_url'])
    
    # if paper['author_name']:
    #     final_str += author_format.format(paper['author_name']) + "\n"
        
    final_str += "[[Paper]]({})".format(paper['paper_url'])
    
    
    if paper['github_url']:
        final_str += "[[Github]]({})".format(paper['github_url'])
    if paper['areas']:
        for area in paper['areas']:
            area = area.strip().replace(' ', '_').replace('-', '_')
            if area:
                final_str += area_format.format(area)
    if paper['class_0']:
        for class_0 in paper['class_0']:
            if class_0.strip() == 'KV Cache':
                continue
            class_0 = class_0.strip().replace(' ', '_').replace('-', '_')
            if class_0:
                final_str += class_0_format.format(class_0)
    if paper['cost']:
        cost = paper['cost'].strip().replace(' ', '_').replace('-', '_')
        if cost:
            final_str += cost_format.format(cost)
    
    # 只有当areas包含"image llm"时才输出
    if any("audio llm" in area.lower() for area in paper['areas']):
        print(final_str)