## python version 3.5 ##

для установки необходимых библиотек `pip install -r requirements.txt`

файл               | за что отвечвет
------------------ | ----------------
config.py          | настройеи для проекта и создание connect-а к MongoDB
data_generator.py  | создание треков, пользователей и связей между ними 
docker-compose.yml | настройни для docker-compose
main.py            | основные классы обработчиков 
models.py          | модели классов для User Track
requirements.txt   | список библиотек необходимых для проекта
setup.py           | исполняемый файл

для запуска `python3 setup.py` и следовать инструкциям

---

необходимое ПО (при отсутствии mongoDB)
* [docker](https://docs.docker.com/get-started/)
* [docker-compose](https://docs.docker.com/compose/)


для установки (ubuntu)

```sudo curl -L https://github.com/docker/compose/releases/download/1.20.1/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose```

```sudo chmod +x /usr/local/bin/docker-compose```

для того чтоб "поднять" docker-compose ```sudo docker-compose up```

----



