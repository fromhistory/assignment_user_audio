# assignment_user_audio

# USAGE


# INSTALLATION 

## You may install this program in two ways: 
1. You may clone it from the git repository.
2. You may pull the docker image from the Dockerhub:
- Dockerhub [link](https://hub.docker.com/r/baranovych/assignment_assignment)
- Pull request `docker pull baranovych/assignment_assignment`


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



