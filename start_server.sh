#!/bin/bash

gunicorn server:app \
--reload \
--bind 127.0.0.1:8000 \
--env API_GATEWAY=api.test.com \
--env MODE=develop \
--env DB_NAME=test \
--env DB_USER=test \
--env DB_HOST=test.com \
--env DB_PORT=0001 \
--env DB_PASSWORD=test \
--env _ENABLE_API_SERVICE_CONSOLE=1 #是否开启ui控制台