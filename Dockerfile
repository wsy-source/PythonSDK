FROM python:3.8
WORKDIR /flask
COPY ./ /flask
RUN pip install -r ./requirements.txt
EXPOSE 5000
ENTRYPOINT ["python","app.py"]

