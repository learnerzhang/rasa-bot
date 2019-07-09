#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-11 19:07
# @Author  : zhangzhen
# @Site    : 
# @File    : run_app.py.py
# @Software: PyCharm
from rasa_core.channels.slack import SlackInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
import yaml
from rasa_core.utils import EndpointConfig

nlu_interpreter = RasaNLUInterpreter('./models/current/nlu')
action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
agent = Agent.load('./models/current/dialogue', interpreter=nlu_interpreter, action_endpoint=action_endpoint)

input_channel = SlackInput('xoxb-236655948598-a0Zsqx1VI3idWm0LHEANxWGy'  # your bot user authentication token
                           )

agent.handle_channels([input_channel], 5004, serve_forever=True)
