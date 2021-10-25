# CDK Serverless Pytest Example

This project is an example for serverless pythonistas.
Writing unittest will helps developers collaborate with colleagues when they are working on shared CDK Stacks.

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

# Cleanup

```bash
$ cdk destroy "*"
```