FROM python:2-alpine



WORKDIR /app

RUN apk --update add python py-pip openssl ca-certificates py-openssl wget bash linux-headers
RUN apk --update add --virtual build-dependencies libffi-dev openssl-dev python-dev py-pip build-base \
  && pip install --upgrade pip \
  && pip install --upgrade pipenv\
  && apk del build-dependencies

COPY . /app

ENTRYPOINT [ "python" ]
CMD [ "install.py" ]
CMD [ "hello.py" ]
