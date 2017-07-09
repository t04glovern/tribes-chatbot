# Digital Tribes - Chatbot
[![GitHub Issues](https://img.shields.io/github/issues/t04glovern/tribes-chatbot.svg)](https://github.com/t04glovern/tribes-chatbot/issues)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)

Chatbot for Digital Tribes 2017.

<p align="center"><img width=40%% src="https://github.com/t04glovern/tribes-chatbot/blob/master/images/demo-01.png"></p>

It aims to a broad range of users (both technical and non-technical) to important safety data using Amazon LEX, Lambda and Slack chat integration.

In the future integration to Facebook messenger, Cisco Spark and practically any other chat client will be added.

## Install

### Setup AWS CLI

To develop on AWS easily I recommend you setup the AWS Command Line Interface tool chain. The instructions can be found on the AWS [Command Line Interface docs page](http://docs.aws.amazon.com/cli/latest/userguide/installing.html)

TLDR;

1. Check pip (Python 3 version) is installed, if not install it

```bash
# Is pip installed?
$ pip --version
$ pip3 --version

# No?
$ curl -O https://bootstrap.pypa.io/get-pip.py
$ python3 get-pip.py --user
```

2. Install AWS CLI over pip

```bash
$ pip3 install --user --upgrade awscli
```

3. Use the [guide here](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) to configure AWS CLI to use your details.

**NOTE**: *you must used the **us-east-1** region as Lex is only available in that region currently.

```bash
$ aws configure
AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
Default region name [None]: us-east-1
Default output format [None]: json
```

### Lambda Functions

#### `get_sensor_data`

1. From the root directory of this repo run `build-lambda.sh` to build the zip file including pip dependencies.
2. Upload this zip (placed in the `builds` folder of the root directory) to the lambda dashboard.
3. Use the following settings when defining the lambda function:

```
Runtime:        Python 3.6
Handler:        get_sensor_data.lambda_handler
Role:           Choose an existing role (this bit is up to you though)
Existing Role:  lambda_basic_execution
Description:    Functions used to get sensor data for bot
```

### Lex Bot Overview

#### Bots

**Name:** TribeBot

#### Intents

**Name:** GetSensorData

<p align="center"><img width=100%% src="https://github.com/t04glovern/tribes-chatbot/blob/master/images/bot-image-01.png"></p>

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D
