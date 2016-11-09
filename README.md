This application is for benchmarking  site loading times. Its made in Python using the Bottle Framework (http://bottlepy.org/docs/dev/)

For starting the aplication follow the steps (NOTICE: the apllication was made to run in Python 3.5):

1- Create virtualenv - virtualenv -p (path to python version executable) <env_name>

2 - activate virtualenv

3 - pip install -r requirements.txt 

4 - run  - python app.py

5 - edit the urls.txt file and put all the urls you wish to measure seperated by ';'

6 - open browser on localhost:8080/benchmarking

If you want to change urls and verify other ones you can change the urls.txt content. The urls are separated by ; wich is 
the delimiter character.
