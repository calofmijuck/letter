## Message Receiver

사용자로부터 메시지를 받아 저장합니다.

- `/letters` 아래에 저장합니다.

### Secret Key

`mysite` 아래에 `.env` 파일을 생성하고 아래와 같이 내용을 채워줍니다.

```
SECRET_KEY=<your_secret_key>
```

### Run container

```
docker build . -t calofmijuck/message_receiver
docker run -d -p 8080:80 calofmijuck/message_receiver:latest
```

### Check!

`localhost:8080` 을 확인해봅니다!
