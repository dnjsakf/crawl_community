FROM ubuntu:latest
MAINTAINER heo "dnjsakf@gmail.com"

RUN sed -i 's/archive.ubuntu.com/kr.archive.ubuntu.com/g' /etc/apt/sources.list
RUN apt-get update && apt-get install -y \
	python-pip \
	python-dev \
	build-essential \
	curl

COPY . /app
WORKDIR /app 
RUN pip install -r requirements.txt
ENTRYPOINT ["scrapyrt"]
CMD ["-p 3001"]

# docker build -t ubuntu:latest .
# docker run -d -p 5000:5000 scrapy-api
