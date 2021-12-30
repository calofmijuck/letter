
# 📬 Letter Site for Korean Army Training Center

육군훈련소(KATC)에 있는 훈련병에게 인터넷 편지를 보내주는 사이트입니다.

<img width="865" alt="Screen Shot 2021-12-30 at 12 57 57" src="https://user-images.githubusercontent.com/38686321/147720635-2f3ef5d3-4e51-4b8d-af0d-7fd165dec2b7.png">
<img width="864" alt="Screen Shot 2021-12-30 at 12 59 20" src="https://user-images.githubusercontent.com/38686321/147720642-317b9123-2a5e-4a53-b493-bcbb94e57eb9.png">

## 🛠️ Features

- `message-server` 는 인터넷 편지를 간편하게 보낼 수 있게 해줍니다.
  - 전송된 메시지는 모두 JSON 형태로 저장됩니다.
  - 30분마다 전송에 실패한 메시지가 있는지 확인하여 재전송 요청합니다.
- `news-crawler` 는 네이버 뉴스를 크롤링하여 인터넷 편지로 전송합니다.
  - 한국 시간 기준 9, 13, 17시에 뉴스를 전송합니다. (추후 변동 가능)

## 🔧 세팅 방법

- 도커를 사용하여 세팅할 수 있습니다. (아래 참고)

---

# 🐳 Using Docker

## 📮 message-server 

### ⚙️ 환경 변수 설정하기

- `env/.env.sample` 을 참고하여 `env/.env` 파일을 만들어 줍니다. 
  - `SECRET_KEY` 는 django secret key 입니다. 참고: [django secret key generator](https://djecrety.ir/)
  - `EMAIL`, `PASSWORD` 는 더캠프 계정 정보입니다.

### 📦 컨테이너 실행

- `message-server.sh` 를 실행하면 됩니다.

```
docker run -d \
    -v `pwd`/env:/env:ro \
    -p 8080:80 \
    calofmijuck/message-server:latest
```

### ❓ 참고

- 계정 및 기타 정보를 위해 `env` 를 mount 합니다.
- 서비스를 하기 위해 적당한 포트로 포워딩하면 됩니다.
- `calofmijuck/message-server` 는 Docker Hub 에 올라가 있습니다.

### ✔️ Check!

`localhost:8080` 을 확인해봅니다!

## 📰 news-crawler

**⚠️ Disclaimer: 이 폴더 내의 코드는 [SyphonArch/news-relay](https://github.com/SyphonArch/news-relay) 에서 가져왔습니다.**

### ⚙️ 환경 변수 설정하기

- `env/.env.sample` 을 참고하여 `env/.env` 파일을 만들어 줍니다. 
  - `SECRET_KEY` 는 이 컨테이너에서 사용하지 않습니다.
  - `EMAIL`, `PASSWORD` 는 더캠프 계정 정보입니다.

### 📦 컨테이너 실행

- `news-crawler.sh` 를 실행하면 됩니다.

```
docker run -d \
    -v `pwd`/env:/env:ro \
    calofmijuck/news-crawler:latest
```

### ❓ 참고

- 계정 및 기타 정보를 위해 `env` 를 mount 합니다.
- `calofmijuck/news-crawler` 는 Docker Hub 에 올라가 있습니다.
