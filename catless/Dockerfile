from debian

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=America/New_York

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y socat

COPY start.sh /start.sh
RUN chmod 755 /start.sh

RUN rm /bin/cat
COPY ./flag.txt /flag.txt

RUN mkdir /nonexistent

RUN useradd -ms /bin/bash bob
EXPOSE 31337/tcp
CMD ["./start.sh"]

