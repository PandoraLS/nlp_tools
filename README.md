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
安装pyltp的时候因为其需要编译，大约花费10min
如果使用官方提供的模型，需要提前下载后解压,[下载地址](http://ltp.ai/download.html)
