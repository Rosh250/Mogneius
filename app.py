import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'LazyDeveloper'

os.system("git clone https://Rosh250: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@github.com/Rosh250/MdiskSearchBotV2 okk && cd okk && pip3 install -U -r requirements.txt && nohup python3 main.py &")
