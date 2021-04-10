# slackmsg

Sending a slack message from the command line for the shell script. It can be used for auto notify when the system executes a shell script thru cron.  

slackmsg.py is the main python script. You can simply copy it and use it from your own shell script. For an example, you can refer to 'Try It'

## Requirements

* Python 3
* slackclient

```
pip install slackclient
```

## Setup

1. *Slack API Token*: You can get your simple API Token from [Slack API](https://api.slack.com). You may refer to [slackclient](https://slack.dev/python-slackclient/auth.html) to setup: Assign chat.write permission to Bot Token Scopes, then Install App -> Install to Workspace.
1. *Channel*: Specify which channel which you want to send a message to. Please add your App to the channel before sending your first message.

```
export SLACK_API_TOKEN="xoxb-201907212200-201907220100-Abcdefg"
export SLACK_CHANNEL="random"
```

## Try It

You can try it with a test script in test directory.

```
cd test
sh testslack.sh
```

Result:
![Result of slackmsg](/tests/test_screenshot.png?raw=true "Result of slackmsg")
