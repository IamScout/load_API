import os
from fastapi import APIRouter, Request
from utils.scout_modules import *

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_dir = os.path.join(base_dir, 'datas','json', 'season_23')

router = APIRouter()

@router.get("/teams-statistics/")
async def get_team_statics_data(request: Request):
    url = str(request.url).split("?url=")[-1]
    make_json(url, "/API/app/datas/json/season_23/teams_statistics/")

@router.get("/teams/")
async def get_team_data(request: Request):
    url = str(request.url).split("?url=")[-1]
    make_json(url, "/API/app/datas/json/season_23/teams/")

@router.get("/standings/")
    url = str(request.url).split("?url=")[-1]
    make_json(url, "/API/app/datas/json/season_23/standings/")

@router.get("/predictions/")
    url = str(request.url).split("?url=")[-1]
    make_json(url, "/API/app/datas/json/season_23/predictions/")

@router.get("/players-topscorers/")
    url = str(request.url).split("?url=")[-1]
    make_json(url, "/API/app/datas/json/season_23/players-topscorers/")    

@router.get("/players-squads/")
    url = str(request.url).split("?url=")[-1]
    make_json(url, "/API/app/datas/json/season_23/players-squads/")

@router.get("/players/")
    url = str(request.url).split("?url=")[-1]
    make_json(url, "/API/app/datas/json/season_23/players/")

@router.get("/leagues/")
    url = str(request.url).split("?url=")[-1]
    make_json(url, "/API/app/datas/json/season_23/leagues/")

@router.get("/fixtures/")
    url = str(request.url).split("?url=")[-1]
    make_json(url, "/API/app/datas/json/season_23/fixtures/")

@router.get("/fixtures-events/")
    url = str(request.url).split("?url=")[-1]
    make_json(url, "/API/app/datas/json/season_23/fixtures_events/")

@router.get("/fixtures-headtohead/")
    url = str(request.url).split("?url=")[-1]
    make_json(url, "/API/app/datas/json/season_23/fixtures_headtohead/")

@router.get("/fixtures-lineups/")
    url = str(request.url).split("?url=")[-1]
    make_json(url, "/API/app/datas/json/season_23/fixtures_lineups/")

@router.get("/fixtures-players/")
    url = str(request.url).split("?url=")[-1]
    make_json(url, "/API/app/datas/json/season_23/fixtures_players/")

@router.get("/fixtures-statistics/")
    url = str(request.url).split("?url=")[-1]
    make_json(url,  "/API/app/datas/json/season_23/fixtures_statistics/")





