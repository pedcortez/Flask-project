FROM --platform=linux/amd64 mysql

ENV MYSQL_DATABASE: todo_db
ENV MYSQL_ROOT_PASSWORD: password
ENV MYSQL_USER: user
ENV MYSQL_PASSWORD: password

ADD ./database/todo.sql /docker-entrypoint-initdb.d



# image: mysql:latest
#     container_name: db

#     environment:
#       MYSQL_DATABASE: todo_db
#       MYSQL_ROOT_PASSWORD: password
#       MYSQL_USER: user
#       MYSQL_PASSWORD: password

#     ports:
#       - "3307:3306"

#     volumes:
#       - ./dbdata:/var/lib/mysql