FROM python:3.10

ENV PIP_DISABLE_PIP_VERSION_CHECK=on

WORKDIR /task_manager

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x docker/*.sh
