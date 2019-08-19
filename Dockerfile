FROM python:3

# USER app
# RUN mkdir /db
#RUN chown app:app -R /db

RUN mkdir /app

WORKDIR /app

ADD requirements.txt /temp/

RUN set -ex; \
    apt-get update -y; \
    apt-get upgrade -y; \
    apt-get install -y build-essential; \
    apt-get install -y python-dev;\
    pip install -U -v setuptools; \
    pip install --no-cache-dir -r /temp/requirements.txt; \
    pip install ipdb; \
    apt-get clean; \
    apt-get autoclean; \
    apt-get autoremove; \
    rm -rf /tmp/* /var/tmp/*; \
    rm -rf /var/lib/apt/lists/*; \
    rm -rf /var/cache/apt/archives/*.deb \
        /var/cache/apt/archives/partial/*.deb \
        /var/cache/apt/*.bin; \