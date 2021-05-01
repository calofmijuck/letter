docker run -d \
    -v `pwd`/env:/env:ro \
    -p 8080:80 \
    calofmijuck/message-server:latest
