docker run -d \
    -v `pwd`/mysite:/letter_django:ro \
    -p 8888:80 \
    -it \
    python:latest \
    /bin/bash
