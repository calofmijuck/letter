
# Letter Site for Korean Army Training Center

육군훈련소(KATC)에 있는 훈련병에게 인터넷 편지를 보내주는 사이트입니다.

![Screenshot from 2021-05-01 09-55-16](https://user-images.githubusercontent.com/38686321/116766190-32c2a280-aa64-11eb-9c17-956140f5950a.png)
![Screenshot from 2021-05-01 09-55-25](https://user-images.githubusercontent.com/38686321/116766192-33f3cf80-aa64-11eb-8487-9f4b5cc3063f.png)

## Using Docker

### 환경 변수 설정하기

- `env/.env.sample` 을 참고하여 `env/.env` 파일을 만들어 줍니다. 
  - `SECRET_KEY` 는 django secret key 입니다. 참고: [django secret key generator](https://djecrety.ir/)
  - `EMAIL`, `PASSWORD` 는 더캠프 계정 정보입니다.

### 컨테이너 실행

- `message-server.sh` 를 실행하면 됩니다.

```
docker run -d \
    -v `pwd`/env:/env:ro \
    -p 8080:80 \
    calofmijuck/message-server:latest
```

### 참고

- 계정 및 기타 정보를 위해 `env` 를 mount 합니다.
- 서비스를 하기 위해 적당한 포트로 포워딩하면 됩니다.
- `calofmijuck/message-server` 는 Docker Hub 에 올라가 있습니다.

### Check!

`localhost:8080` 을 확인해봅니다!
