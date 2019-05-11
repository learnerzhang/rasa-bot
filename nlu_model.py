#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-11 15:50
# @Author  : zhangzhen
# @Site    : 
# @File    : nlu_model.py.py
# @Software: PyCharm

from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter


def train_nlu(data, configs, model_dir):
    training_data = load_data(data)
    trainer = Trainer(config.load(configs))
    trainer.train(training_data)
    model_directory = trainer.persist(model_dir, fixed_model_name='nlu')


def run_nlu():
    interpreter = Interpreter.load('./models/current/nlu')
    print(interpreter.parse(u"thank you"))


if __name__ == '__main__':
    train_nlu('./data/nlu_data.md', 'nlu_config.yml', './models/current/nlu')
    run_nlu()
