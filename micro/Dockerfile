FROM python:latest
RUN pip install flask
RUN pip install datetime
COPY ./static /home/microweb_app/static/
COPY ./templates /home/microweb_app/templates/
COPY ./flask_app.py /home/microweb_app/
EXPOSE 5090
CMD python/home/microweb_app/flask_app.py