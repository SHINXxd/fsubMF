FROM python:3.11

#update pkg &&  installing
RUN apt-get -y update && \
    apt-get install -y --no-install-recommends git curl wget gnupg2 ffmpeg && \
    rm -rf /var/lib/apt/lists/*

RUN pip install setuptools wheel yarl multidict

RUN git clone https://github.com/SHINXxd/fsubMF app

WORKDIR app

# instaalling req
RUN pip install -U -r requirements.txt

#run cmd
CMD ["bash", "start"]
