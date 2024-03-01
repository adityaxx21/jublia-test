# Jublia Mail Recipient
Apps created to handle mail sending with queue using backend with flask and frontend with react 

## Requirement
- node: v20
- python: 3.10
- postgresql
- redis
- mailhog

## How To Setup
Don't forget to fill up .env file

For setup backend, run the following command
```bash
  cd backend
  source ./bin/activate
  pip install -r requirements.txt
```

For setup frontend, run the following command
```bash
  npm install
```


## How To Run
For running backend, run the following command
```bash
  cd backend
  celery -A run.celery worker  --loglevel=info
  celery -A run.celery beat --loglevel=info
  python run.py
```
For running backend, run the following command
```bash
  cd frontend
  npm run
```

## API Reference

#### Get all email

```http
  GET /get_emails
```
#### Create email
```http
  POST /save_emails
```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `event_id`      | `int` |  id of event |
| `mail_subject`      | `string` |  input subject of email |
| `mail_content`      | `string` |  content of email |

#### Send email without specific time

```http
  POST /send_mail/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` |  Id of item to fetch |



#### Get all recipient

```http
  GET /recipient
```
#### Get specific recipient

```http
  GET /recipient/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` |  Id of item to fetch |

#### Create recipient
```http
  POST /recipient
```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `email`      | `string` |  email of recipient |


#### Delete recipient

```http
  DELETE /recipient
```
#### Update recipient

```http
  PUT /recipient/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` |  Id of item to fetch |
| `email`      | `string` |  Email recipient |


## Additional Information
For default will be running in port
- backend: localhost:5000
- frontend: localhost:3000


