FROM locustio/locust

COPY . /
RUN pip3 install -r requirements.txt
WORKDIR /org
cmd