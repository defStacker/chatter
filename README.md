IMPORT
>Install rabbitmq 
>Install Postgres database 
>Import database from the database folder all.sql


>Grant permission to the user to do CRUD Operations
```
psql mydatabase -c "GRANT ALL ON ALL TABLES IN SCHEMA public to admin;"
psql mydatabase -c "GRANT ALL ON ALL SEQUENCES IN SCHEMA public to admin;"
psql mydatabase -c "GRANT ALL ON ALL FUNCTIONS IN SCHEMA public to admin;"
```

>Install requirements
>Install Python 3.5 or grater
>pip3 install -r requirements.txt
>python3 manage.py makemigrations
>python3 manage.py migrate
>python3 manage.py runserver

>In the folder websockets run the next command
```
node install
node index.js
```

>For the messaging between rabbitmq should set up a cron job in linux to run at certain time it should not run at the same time is created because it should run independent from the application.
The file will be created along side of manage.py, the names of the files are receive.py, end.py, csv_file.py

>Execute external python for rabbitmq
```
python3 receive.py
python3 send.py
python3 csv_file.py
```

>For the csv_file.py to get the data correctly of the company, have to put the root of the csv file, the file in the project 
is in the folder services  'aapl.us.csv'

>The url to the project 
```
http://127.0.0.1:8000/
```

please use the following users
```
dave@gmail.com
crack@live.com
```

Password  for both
```
Iamtheone1?
```

https://jee-appy.blogspot.com/2017/01/deply-django-with-nginx.html
