import csv
import re
import json
from collections import Counter

def word_count(paragraph, output_format='csv', sort_by='word', order='asc', limit=None, filter_by=None):
    words = re.findall(r'\b\w+\b', paragraph.lower())
    
    if filter_by:
        words = [word for word in words if re.search(filter_by, word)]

    word_count = Counter(words)

    if sort_by == 'word':
        word_count = dict(sorted(word_count.items()))
    elif sort_by == 'occurrence':
        word_count = dict(sorted(word_count.items(), key=lambda item: item[1]))


    if order == 'desc':
        word_counts = dict(reversed(list(word_count.items())))
 
    if limit:
        word_counts = dict(list(word_count.items())[:limit])

    if output_format == 'csv':
        with open('word_count.csv', 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['Word', 'Occurrence'])
            csv_writer.writerows(word_count.items())
        print('Word count saved to "word_count.csv" in CSV format.')
    elif output_format == 'json':
        with open('word_count.json', 'w') as json_file:
            json.dump(word_counts, json_file, indent=2)
        print('Word count saved to "word_count.json" in JSON format.')
 
paragraph = "This is a sample paragraph. It contains sample words for word count. The words can be counted based on specified options."

word_count(paragraph, output_format='csv', sort_by='occurrence', order='desc', limit=5, filter_by='s*')
