#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-09 10:01
# @Author  : zhangzhen
# @Site    : 
# @File    : nlu_test.py
# @Software: PyCharm
from rasa_nlu.model import Metadata, Interpreter
import pprint

interpreter = Interpreter.load('./models/telegram-bot/nlu/')
result = interpreter.parse(u"which stock to buy today")

pprint.pprint(result)
