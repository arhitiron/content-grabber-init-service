# Content grabber

This project created just for fun and it's a first project on python,
so if you will find some bugs or deviation from styleguide, submit a pull request.

This service provides content from url and starts recursive grabbing.
By service means collection of services (init service, link service,
doc service, doc storage and raw cache).

## Run by using docker-compose

1. Install [Docker](https://www.docker.com/).

2. Install [Docker-compose](https://docs.docker.com/compose/install/).

3. Run:
```
$ docker-compose up
```

## TODO LIST

* Create DSL for parsing content and fetching only necessary items
* Refactoring needed
* API gateway
* Doc projection service
* Add default values instead of using env vars

## DEPENDS ON
All of this projects are on github. But they should be built (in some reason you need to use `sudo`).
```
$ docker build -t ${name} .
```


* Link service [https://github.com/arhitiron/content-grabber-link-servie](https://github.com/arhitiron/content-grabber-link-servie)
* Doc service [https://github.com/arhitiron/content-grabber-doc-service](https://github.com/arhitiron/content-grabber-doc-service)
* Doc storage [https://github.com/arhitiron/content-grabber-doc-storage](https://github.com/arhitiron/content-grabber-doc-storage)
* Raw cache [https://github.com/arhitiron/content-grabber-raw-cache](https://github.com/arhitiron/content-grabber-raw-cache)

## Simple schema

![simple-parser](simple-parser.png?raw=true "simple-parser")