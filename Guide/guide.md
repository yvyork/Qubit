### Deployment on Server

1. Get repo https://github.com/yvyork/Qubit.git with ```git clone```
2. Move to directory Qubit and execute ```docker-compose build```
(You can ignore the red warnings)
3. After build is complete, execute ```docker-compose up -d``` 
4. List the containers with ```docker ps``` and open a shell in the backend container with ```docker exec -it <hash backend> /bin/bash```
4.1 Make data base migrations ```python3 manage.py migrate```
4.2 Make updates ```apt-get update```
4.3 Install nano and poppler-utils ```apt-get install nano && apt-get install poppler-utils```
4.4 Exit the container with ```exit```
5. Now open a shell session in the postgres container ```docker exec -it <hash postgres> /bin/bash```
5.1 Execute ```psql -U postgres -d postgres -W```
5.2 Enter PW
5.3 Execute 
```sql
INSERT INTO ticketing_counter (id, counter_name)
VALUES (1, 'Schalter 1'),
(2, 'Schalter 2'),
(3, 'Schalter 3');
// This is the dummy ticket. It needs to be in the DB at all times. 
INSERT INTO ticketing_ticket (id, number, timestamp, wait, called)
VALUES (1, 100, now(), 5, true);

```

Now the system is set up and should work :-) 

### Delete all containers and images correctly

1. ```sudo su```
2. ```docker kill $(docker ps -q)```
3. ```docker container prune```
4. ```docker image prune -a```
5. ```rm -rf Qubit/```


### Install locally 

Get your clone from the repo above. 
__Please__ make your own branch and __DO NOT__ push into remote main branch! Unless you know what you're doing ;) 
Better make a pull request.  

*I had trouble installing brother_ql on Mac M1. Perhaps best you run the whole thing in docker containers. You need to change the docker-compose.yml file for that and create a volume so changes will be automatically detected. You can make a copy of the compose file for your local development. But please add it to .gitignore* 

__Backend__
1. Make a virtual environment in Qubit/backend ```python3 -m venv venv```
2. Activate ```source venv/bin/activate```
3. Install requirements ```pip3 install -r requirements.txt```
4. Install poppler-utils and brother_ql
4. Start server ```python3 manage.py runserver``` 

Depending on your preference, in Qubit/backend/qubitbackend/settings.py you can either choose a Postgres or MYSQL DB
__IMPORTANT__ for deployment ONLY use Postgres DB. 

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'qubit',
#         'HOST': 'localhost',
#         'USER': 'root',
#         'PASSWORD': 'a_opK-CM9k.o_4zh',
#     }
# }
```

__Frontend__
1. Go to Qubit/frontend
2. Run ```npm install```
3. Start development server ```npm run dev```

__IMPORTANT__
For now you have to change the different ips for the services manually in the following files:
- Qubit/backend/ticketing/services/paul.py (ip for PauL)
- Qubit/backend/ticketing/services/printing.py (ip for printer)
- Qubit/frontend/src/components/TicketForm.svelte (local/server one instance)
- Qubit/frontend/src/routes/queue.svelte (local/server three instances)


### Printing

Uses a python library: https://pypi.org/project/brother-ql/ for more information

