# CDK Serverless Pytest Example

This project is an example for pythonistas on serverless land.

Writing unittest helps developers to collaborate with their colleagues especially when they are working on shared CDK Stacks.

![Overview Architecture](img/overview.png)

Introducing application was inspired by Hit-Counter example on [CDKWorkshop](https://cdkworkshop.com/20-typescript.html)

# Prerequisites

- git
- awscli
- Python 3.8
- Nodejs 14
- AWS Account and locally configured AWS credential

# Installation

install dependencies

```bash
$ cd infra
$ npm i -g cdk@1.129.0
$ npm i
$ cdk bootstrap
```

open [**config.ts**](infra/lib/constants/config.ts) and edit below variables (optional for prototyping).
1. *ns* - namespace for the project, default is `CdkSlsPytest`

deploy the CDK app to your account

```bash
$ cdk deploy "*" --require-approval never
```

# Run

install HTTPie, modernized CUrl

```bash
$ pip install httpie
```

update hit counter by requesting POST

```bash

$ cdk deploy ...

...
 ✅  CdkSlsPytestApiGatewayStack (no changes)

Outputs:
CdkSlsPytestApiGatewayStack.HttpApiUrl = https://xxx.execute-api.ap-northeast-2.amazonaws.com/

$ http post https://xxx.execute-api.ap-northeast-2.amazonaws.com/test
```

get count for the given path

```bash
$ http get https://xxx.execute-api.ap-northeast-2.amazonaws.com/test

HTTP/1.1 200 OK
Apigw-Requestid: IBwAWh-YoE0EPcQ=
Connection: keep-alive
Content-Length: 28
Content-Type: application/json
Date: Sat, 30 Oct 2021 15:10:34 GMT

{
    "count": 1,
    "path": "test"
}
```

# Test 

## Run test locally

install dependencies

```bash
$ pip install -r requirements.txt
```

install local services package for testing

```bash
$ pip install -e lib/functions
```

run tests

```bash
$ npm run pytest
```

## Run test using Docker

```bash
$ docker build -t cdk-pytest . && docker run --rm cdk-pytest
```

# Cleanup

```bash
$ cdk destroy "*"
```
