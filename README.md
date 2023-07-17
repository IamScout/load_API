# load_API
축구 데이터를 수집하기위한 API server

해당 서버는 airflow가 순수하게 cordinator 로 사용하기 위해 build 한 단순한 API 서버입니다.

Projects 구조

```
.
├── README.md
├── __init__.py
├── config
│   ├── config.ini
│   └── humming-bird-383304-fa3fcb3047b6.json
├── datas
│   ├── json
│   │   └── season_23
│   │       ├── fixtures
│   │       ├── fixtures_events
│   │       ├── fixtures_headtohead
│   │       ├──   :
│   │       ├── teams
│   │       └── teams_statistics
│   └── logs
├── dockerfile
├── main.py
├── requirements.txt
├── routers
│   ├── __init__.py
│   └── load_data_func.py
└── utils
    ├── __init__.py
    └── scout_modules.py

```
