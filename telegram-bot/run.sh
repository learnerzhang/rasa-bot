#!/usr/bin/env bash
# telegram-bot
# old way to
# train NLU model
python3 -m rasa_nlu.train -c telegram-bot/sklearn_spacy_config.yml --data data/telegram/nlu.md -o models --fixed_model_name nlu --project telegram-bot --verbose

# train CORE
python3 -m rasa_core.train -d telegram-bot/domain.yml -s data/telegram/stories.md -o models/telegram-bot/core

# endpoint
python3.7 -m rasa_core_sdk.endpoint --actions telegram-bot.actions

# run server
# python3.7 main.py --token <TOKEN> --tunnel <TUNNEL>
python3.7 main.py --token 664040200:AAED4xTe8CM5uM5I2Za_vKWrl4aFdI0l1Lc --tunnel https://52abee14.ngrok.io

python3.7 -m telegram-bot.main --token 664040200:AAED4xTe8CM5uM5I2Za_vKWrl4aFdI0l1Lc --tunnel https://52abee14.ngrok.io


# new way to train
rasa train nlu -h
rasa train nlu -c telegram-bot/config.yml --data data/telegram/nlu.md --out models --fixed-model-name nlu --verbose
