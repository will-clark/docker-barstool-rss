FROM python:2
MAINTAINER email@willclark.org
EXPOSE 8000
WORKDIR /usr/src/app
COPY requirements.txt ./
COPY run.py ./
COPY rss.mako ./
RUN pip install --no-cache-dir -r requirements.txt
RUN rm requirements.txt
CMD ["python", "./run.py"]