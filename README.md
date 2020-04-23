# nlp_tools
nlp使用的工具
---

### 命名实体识别
中文命名实体识别使用的是哈工大的pyltp
[github](https://github.com/HIT-SCIR/pyltp)
[说明文档](https://pyltp.readthedocs.io/zh_CN/latest/)
首先需要安装pyltp,然后就可以使用了,`ner.py`是基本样例,`ner2json.py`是将`txt`文本中的数据识别后写入到`json`文件中
```bash
$ pip install pyltp
```
