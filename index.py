import re
import collections


def process_large_data(file_path):
    words_count=collections.Counter()


    with open(file_path,'r',encoding='utf-8') as file:
        for line in file:
            words=re.findall(r'\b[a-z]+\b', line.lower())
            words_count.update(words)

    print(words_count)

    top_words=words_count.most_common(10)

    for word,count in top_words:
        print(f"{word}: {count}")






file_path=file_name
process_large_data(file_path)
