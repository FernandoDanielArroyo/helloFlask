FROM python:3.10.6

RUN pip install Flask	

WORKDIR /hello_flask 

COPY . /hello_flask

ENTRYPOINT [ "python3" ]

CMD [ "helloflask.py" ]
