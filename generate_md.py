import csv

input_csv_path = "test.csv"

required_fields = ["Title", "Code", "arXiv", "Publish", "Author"]
output_list = []

with open(input_csv_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        # use for pass some rows with empty fields (TODO@kele, keda)
        # if any(not row[field].strip() for field in required_fields):
        #     continue

        entry = {
            'paper_name': row['Title'].strip(),
            'paper_url': row['arXiv'].strip(),
            'github_url': row['Code'].strip(),
            'author_name': row['Author'].strip(),
            'image_path': 'figures/.png',
            'conference': row['Publish'].strip().replace(' ', '_').replace('-', '_'),
        }
        output_list.append(entry)

papers = output_list

import time

star_format = '[![Star](https://img.shields.io/github/stars/{}.svg?style=social&label=Star)](https://github.com/{})'
conference_format = " [![Publish](https://img.shields.io/badge/Conference-{}-blue)]()"
main_item_format = '[{}]({}) <br> {} |'
image_format = '<img width="1002" alt="image" src="{}"> |'
github_format = '[Github]({}) <br> '
paper_format = '[Paper]({})'

month = time.strftime("%m", time.localtime())
day = time.strftime("%d", time.localtime())
timestamp = f"[//]: #{month}/{day}"


for paper in papers:
    final_str = "* "
    if paper['conference']:
        final_str += conference_format.format(paper['conference']) + " "
    if paper['github_url']:
        github_item = '/'.join(paper['github_url'].split('/')[-2:])
        final_str += star_format.format(github_item, github_item) + " "
    final_str += "[{}]({}). {}. [[Paper]]({})".format(
        paper['paper_name'], paper['paper_url'], paper['author_name'], paper['paper_url'])
    if paper['github_url']:
        final_str += "[[Github]]({})".format(paper['github_url'])
    print(final_str)