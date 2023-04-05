FROM locustio/locust

COPY . /
WORKDIR /
RUN pip3 install -r requirements.txt
WORKDIR /org/thoughtworks/
EXPOSE 8089

ENTRYPOINT [ "executable" ]
CMD [ "-f" , "locust_load.py"]