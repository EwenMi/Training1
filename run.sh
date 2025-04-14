#!/bin/bash
cd ~/app
pip3 install -r requirements.txt
nohup python3 app.py &
