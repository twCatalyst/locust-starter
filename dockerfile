FROM locustio/locust

WORKDIR /
COPY . /
RUN pip3 install -r requirements.txt
WORKDIR /org/thoughtworks/
