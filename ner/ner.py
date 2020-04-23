# -*- coding: utf-8 -*-

import os
from pprint import pprint
from pyltp import *
import platform
import time


class LtpToolFast:
    def __init__(self, lexicon_filepath='', display=False):
        # fsd_computer = platform.node() != 'DESKTOP-OJ37RMB'
        # ltp_data_dir = r'F:\Coding\ltp_data' if fsd_computer else r'C:\Users\ll\Downloads\ltp\3.4'
        ltp_data_dir = '/home/lisen/uestc/nlp_research/ltp_data_v3.4.0'
        # 模型下载地址:http://model.scir.yunfutech.com/model/ltp_data_v3.4.0.zip 
        # 下载后解压即可

        # self.lexicon = "F:\Coding\ltp_data\lexicon"
        # 成员函数是否直接展示结果
        self.display = display
        self.lexicon_filepath = lexicon_filepath
        # 分词
        self.segmentor = Segmentor()
        cws_model_path = os.path.join(ltp_data_dir, 'cws.model')
        if lexicon_filepath:
            self.segmentor.load_with_lexicon(cws_model_path, lexicon_filepath)
        else:
            self.segmentor.load(cws_model_path)
        # 词性标注
        self.postagger = Postagger()
        pos_model_path = os.path.join(ltp_data_dir, 'pos.model')
        if lexicon_filepath:
            self.postagger.load_with_lexicon(pos_model_path, lexicon_filepath)
        else:
            self.postagger.load(pos_model_path)
        # 命名实体识别
        self.recognizer = NamedEntityRecognizer()
        ner_model_path = os.path.join(ltp_data_dir, 'ner.model')
        self.recognizer.load(ner_model_path)
        # # 依存句法
        # self.parser = Parser()
        # parser_model_path = os.path.join(ltp_data_dir, 'parser.model')
        # self.parser.load(parser_model_path)
        # # 语义分析
        # self.labeller = SementicRoleLabeller()
        # pisrl_model_path = os.path.join(ltp_data_dir, 'pisrl_win.model')
        # self.labeller.load(pisrl_model_path)

    def __del__(self):
        self.segmentor.release()
        self.postagger.release()
        self.recognizer.release()
        # self.parser.release()
        # self.labeller.release()


    """
    一波在ltp接口上直接封装的函数
    函数不会进行嵌套调用
    """
    def segment(self, sentence):
        return list(self.segmentor.segment(sentence))

    def tag(self, words):
        return list(self.postagger.postag(words))

    # def dependency(self, words, tags):
    #     return self.parser.parse(words, tags)

    def ner(self, words, tags):
        netags = self.recognizer.recognize(words, tags)  # 命名实体识别
        if self.display:
            print('命名实体识别:', list(netags))
        return list(netags)

    # def labelRole(self, words, tags, arcs):
    #     roles = self.labeller.label(words, tags, arcs)  # 语义角色标注
    #     if self.display:
    #         print('\n', '-' * 8, "语言角色", '-' * 8)
    #         for role in roles:
    #             print(role.index, "".join(
    #                 ["%s:(%d,%d)" % (arg.name, arg.range.start, arg.range.end) for arg in role.arguments]))
    #     return roles


if __name__ == "__main__":
    # sen = " 新华社记者翟健岚摄新华社北京9月26日电(记者郑明达)全国政协主席汪洋26日在全国政协礼堂会见了刚果(金)参议院第一副议长、刚中友好协会主席莫科洛"
    # print("-"*30, "句法语义分析抽取事件", "-"*30)
    # ltp = LtpToolFast()
    # a, b = ltpSynSem(ltp, sen, "1")
    # pprint(a)
    # pprint(b)
    # print("-" * 30, "end", "-" * 30)

    some_str = [
        '东方证券首席经济学家邵宇',
        '中国国家主席习近平',
        '商务部国际贸易谈判代表兼副部长傅自应',
        '国务院发言人诺尔特',
        '民主党参议员珍妮',
        'Abby Burkhardt 在布里奇波特 2016 年 · · 在 University of Bridgeport 开始了新工作 2016 年 — International Admissions Counselorr'
    ]
    ltp = LtpToolFast()
    for s in some_str:
        print(s)
        # print('-' * 10)
        # print(ltp.segment(s))
        word_list = ltp.segment(s)
        tag = ltp.tag(word_list)
        # print(word_list)
        print(tag)
        ner_list = ltp.ner(word_list, tag)
        print(ner_list)
        