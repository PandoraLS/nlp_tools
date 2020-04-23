# -*- coding: utf-8 -*-
"""
将txt中的自然语言读入，然后生成json文件
example是将ner_tiny.txt进行命名实体识别后写入到json文件中
Json读取进来是个列表，列表中的每一项分为4项
[
    [第1行：原始文本(字符串)]
    [第2行：分词后的结果(列表)]
    [第3行：对应的词性标注(列表)，与分词列表一一对应：（形容词，名词，动词等）参考：https://ltp.readthedocs.io/zh_CN/latest/appendix.html#id3]
    [第4行：命名实体识别(列表)，与分词列表一一对应：（人名（Nh）、地名（Ns）、机构名（Ni）），参考：https://ltp.readthedocs.io/zh_CN/latest/appendix.html#id4]
]

"""

from ner import LtpToolFast
import json

ltp = LtpToolFast()

res = []
with open('ner_tiny.txt', 'r', encoding='utf8') as f:
    for line in f:
        line = line.strip()
        line_seg = ltp.segment(line)
        tag = ltp.tag(words=line_seg)
        ner_list = ltp.ner(line_seg, tag)
        res.append((line, line_seg, tag, ner_list))

with open('ner_tiny.json', 'w',encoding='utf8') as f:
    json.dump(res, f, ensure_ascii=False, indent=2)
    

