# -*- coding: UTF-8 -*-
# use slackclient==2.9.3
#import logging
#logging.basicConfig(level=logging.DEBUG)

import os, sys
from slack import WebClient
from slack.errors import SlackApiError

slack_token = os.environ["SLACK_API_TOKEN"]
channel = os.environ["SLACK_CHANNEL"]
client = WebClient(token=slack_token)

def sendmsg(msg='Hello!'):
  try:
    response = client.chat_postMessage(
      channel=channel,
      text=msg
    )
  except SlackApiError as e:
    assert e.response["error"]  

if len(sys.argv) > 1:
  sendmsg(sys.argv[1])
else:
  lines = ''
  for line in sys.stdin:
    lines += line + '\n'
  sendmsg(lines)
