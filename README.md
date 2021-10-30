# CDK Serverless Pytest Example

This project is an example for pythonistas on serverless land.

Writing unittest will help developers to collaborate with colleagues when they are working on shared CDK Stacks.

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
