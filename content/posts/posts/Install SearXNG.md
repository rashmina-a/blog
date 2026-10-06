---
title: Installed SearXNG - Private & Self-hosted search engine
date: 2026-10-06
draft: false
tags:
  - searxng
  - New
  - Brand_new
  - self_host
  - Open_Source
  - Development
  - upgrade
---
Today I installed **SearXNG** which is a *Privacy Focused* Search engine which is self hosted , I personally host it using docker desktop and also the docker cli with a docker-compose.yaml file i got from a youtuber ,Here the link to that .yaml file [docker-compose.yaml](https://code.dbt3ch.com/jy9PkROF)
or the code 
```
services:
  redis:
    container_name: redis
    image: docker.io/valkey/valkey:8-alpine
    command: valkey-server --save 30 1 --loglevel warning
    restart: unless-stopped
    networks:
      - searxng
    volumes:
      - valkey-data:/data
    cap_drop:
      - ALL
    cap_add:
      - SETGID
      - SETUID
      - DAC_OVERRIDE
    logging:
      driver: "json-file"
      options:
        max-size: "1m"
        max-file: "1"

  searxng:
    container_name: searxng
    image: docker.io/searxng/searxng:latest
    restart: unless-stopped
    networks:
      - searxng
    ports:
      - "8181:8080" #change 8181 as needed, but not 8080
    volumes:
      - searxng:/etc/searxng:rw
    environment:
      - SEARXNG_BASE_URL=http://your.docker.server.ip:8080/ #Change "your.docker.server.ip" to your Docker server's IP
      - UWSGI_WORKERS=4 #You can change this
      - UWSGI_THREADS=4 #You can change this
    cap_drop:
      - ALL
    cap_add:
      - CHOWN
      - SETGID
      - SETUID
    logging:
      driver: "json-file"
      options:
        max-size: "1m"
        max-file: "1"

networks:
  searxng:

volumes:
  valkey-data: #redis storage
  searxng: #searxng storage

```
and it worked when i ran it the first time without any more configuration ,This is the basic interface
!![Image Description](/images/Pasted%20image%2020261006231339.png)
and its pretty minimal and its fine - tunable if you want it to be , And you also have a Preferences page,
!![Image Description](/images/Pasted%20image%2020261006231837.png)
where you can customize literally anything. I like because *"I dont wan't to be **Sold**"*.Here are some useful links
[SearXNG docs](https://docs.searxng.org/)
[SearXNG github](https://github.com/searxng/searxng)


