FROM python:3.5
MAINTAINER Alex <liangbinsi@gmail.com>

# App path /code
ENV INSTALL_PATH=/code
RUN mkdir -p $INSTALL_PATH
WORKDIR $INSTALL_PATH

# install requirements
ADD requirements.txt $INSTALL_PATH
RUN pip install -i https://pypi.doubanio.com/simple/ -r requirements.txt

ADD . $INSTALL_PATH