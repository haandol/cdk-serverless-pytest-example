FROM public.ecr.aws/lambda/python:3.8

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

RUN mkdir -p /src
COPY lib/functions/ /src/

RUN pip install -e /src

ENV AWS_DEFAULT_REGION="ap-northeast-2"

WORKDIR /src

ENTRYPOINT [ "pytest" ]