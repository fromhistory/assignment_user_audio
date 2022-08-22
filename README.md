# assignment_user_audio

# USAGE

This program is a webserver that hosts REST APIs to fetch information from the Google SQL database. It does CRUD operations and a number of searches regarding the user and the audio information linked to each user. You may use the program by sending API requests through POSTMAN or through your terminal in the form of CURL requests. Please see the endpoints provided below. 


# INSTALLATION 

## You may install this program in two ways: 
1. You may clone it from the git repository: `https://github.com/fromhistory/assignment_user_audio.git`
2. You may pull the docker image from the Dockerhub:
- Dockerhub [link](https://hub.docker.com/r/baranovych/assignment_assignment)
- Pull request: `docker pull baranovych/assignment_assignment`
- Docker run: `docker run -d -it docker.io/baranovych/assignment_assignment /bin/bash`


# ENDPOINTS 

## ADD A USER

```
curl --location --request POST 'https://feisty-ceiling-359617.uc.r.appspot.com/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "Mark Zukerberg",
    "email": "facebook@gmail.com",
    "address": "SFO",
    "image": null
}'
```

## GET A USER 

```
curl --location --request GET 'https://feisty-ceiling-359617.uc.r.appspot.com'

```

## UPDATE A USER

```
curl --location --request PUT 'https://feisty-ceiling-359617.uc.r.appspot.com/' \
--header 'Content-Type: application/json' \
--data-raw '   {
        "address": "Chicago",
        "email": "homecare@gmail.com",
        "id": 7,
        "image": null,
        "name": "Jason"
    }'
```

## DELETE A USER

```
curl --location --request DELETE 'https://feisty-ceiling-359617.uc.r.appspot.com/' \
--header 'Content-Type: application/json' \
--data-raw '    {
        "address": "SFO",
        "email": "facebook@gmail.com",
        "id": 13,
        "image": null,
        "name": "Mark Zukerberg"
    }'
```

## SEARCH A USER BY ID 

```
curl --location --request GET 'https://feisty-ceiling-359617.uc.r.appspot.com/id/1' \
--data-raw ''

```

## SEARCH A USER BY NAME 

```
curl --location --request GET 'https://feisty-ceiling-359617.uc.r.appspot.com/name/aman'
```

## SEARCH A USER BY EMAIL

```
curl --location --request GET 'https://feisty-ceiling-359617.uc.r.appspot.com/email/1123@gmail.com'

```

## SEARCH A USER BY ADDRESS

```
curl --location --request GET 'https://feisty-ceiling-359617.uc.r.appspot.com/address/Chicago'

```

## ADD AUDIO

```
curl --location --request POST 'https://feisty-ceiling-359617.uc.r.appspot.com/audio' \
--header 'Content-Type: application/json' \
--data-raw '{
    "ticks": [-89.33, -21.33, -93.47, -89.03999999999999, -84.61, -80.18, -75.75, -71.32, -66.89, -62.46, -58.03, -53.6, -49.17, -44.74, -40.31],
    "selected_tick": 10,
    "step_count": 0,
    "user_id": 12
}'
```

## GET AUDIO

```
curl --location --request GET 'https://feisty-ceiling-359617.uc.r.appspot.com/audio'

```

## UPDATE AUDIO

```
curl --location --request PUT 'https://feisty-ceiling-359617.uc.r.appspot.com/audio' \
--header 'Content-Type: application/json' \
--data-raw '{
        "selected_tick": 2,
        "session_id": 1,
        "step_count": 1,
        "ticks": [-10, -12, -13, -14, -15.6, -16.9, -17.1, -18.004, -19, -99, -88, -99, -55, -66, -77],
        "user_id": 2
    }'
```

## GET AUDIO BY SESSION 

```
curl --location --request GET 'https://feisty-ceiling-359617.uc.r.appspot.com/audio/session_id/12'

```


## TABLE SCHEMAS

```
create table users(
id INT NOT NULL AUTO_INCREMENT,
name VARCHAR(255),
email VARCHAR(255),
address VARCHAR(255),
image BLOB,
PRIMARY KEY(id)
);
```

```
create table audio(

session_id INT NOT NULL AUTO_INCREMENT,
ticks VARCHAR(255),
step_count INT,
selected_tick INT,
user_id INT NOT NULL,
PRIMARY KEY(session_id),
FOREIGN KEY (user_id)
	REFERENCES users(id)
);
```

## LIMITATIONS: 

The application is running on google sql. To fetch information, use curl commands or postman. As of now, it does not run on the localhost. 


## FUTURE ITERATIONS:

1. Adding Swagger UI could improve user experience as requests could be sent without using the terminal or postman.  
2. Enhance security with an API token 
3. Make possible to upload and pull image from the database. 
4. Do analysis on SQL server data to capture important metrics such as total number of users by location etc. 






