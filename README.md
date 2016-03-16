## DSS
Django, Solr and Scrapy integration (example project). This example project can be used as boilerplate code 
to setup a vertical search engine. As an example, this application collects reddit usernames and makes them searchable.


#### How to use:

1. Download
2. Fix all dependencies
3. Edit to suit your project

#### Dependencies
Install with pip install:

- Django==1.6.5
- Scrapy==0.22.0
- django-haystack==2.4.0
- pysolr==3.3.2

Solr is provided with the application.

#### Database creation

Before the application can be used, we first need to create a database with the following command:

`python manage.py syncdb`

Django versions newer than 1.6, may use different methods.

#### Useful commands
Run these commands from the project root to start the application.

- Start Solr:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`cd solar; java -jar start.jar`
- Crawl Reddit:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`scrapy crawl reddit`        
- Rebuild Index:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`python manage.py rebuild_index`
- Run the webserver:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`python manage.py runserver`

The application should now be accesible at http://127.0.0.1:8000/.


