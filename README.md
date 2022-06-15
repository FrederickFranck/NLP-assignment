# NLP-assignment


## Desciption

This is a web app that uses NLP to classify documents from the [*Belgische Staatblad*](https://www.ejustice.just.fgov.be/cgi/summary.pl)

## Usage 

A live version can be found [here](https://tax-predict.herokuapp.com/)


![site](./project/rsc/image_site.png)

## Installation

Install the required packages.

```bash
pip install -r project/requirements.txt
```

This script will scrape documents to use and generate & save the keywords. This needs to be done at least once before hosting the app locally or in docker. (This can take a while depending on your PC's specs)
```bash
python main.py
```

Host the app locally, it will be running on [localhost](http://localhost:5000/)

```bash
python app.py
```

### Docker

Build the docker image
```bash
docker build . -t tax-predict
```

Deploy the docker image to a container and run locally.
App will be running on [localhost](http://localhost:5000/)

```bash
docker run -d -p 5000:5000 tax-predict