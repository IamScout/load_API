import os
from fastapi import APIRouter, Request
from utils.scout_modules import *

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_dir = os.path.join(base_dir, 'datas','json', 'season_23')

router = APIRouter()

@router.get("/teams-statistics/")
async def get_team_statics_data(request: Request):
    url = str(request.url).split("?url=")[-1]
    make_json(url, "/api/app/datas/json/season_23/teams_statistics")

@router.get("/teams/")
async def get_team_data(request: Request):
    url = str(request.url).split("?url=")[-1]
    make_json(url, "/api/app/datas/json/season_23/teams")

@router.get("/standings/")
async def get_standing_data(request: Request):
    url = str(request.url).split("?url=")[-1]
    make_json(url, "/api/app/datas/json/season_23/standings")

@router.get("/predictions/")
async def get_predictions_data(request: Request):
    url = str(request.url).split("?url=")[-1]
    make_json(url, "/api/app/datas/json/season_23/predictions")

@router.get("/players-topscorers/")
async def get_topscorers_data(request: Request):
    url = str(request.url).split("?url=")[-1]
    make_json(url, "/api/app/datas/json/season_23/players-topscorers")    

@router.get("/players-squads/")
async def get_squads_data(request: Request):
    url = str(request.url).split("?url=")[-1]
    make_json(url, "/api/app/datas/json/season_23/players-squads")

@router.get("/players/")
async def get_players_data(request: Request):
    url = str(request.url).split("?url=")[-1]
    make_json(url, "/api/app/datas/json/season_23/players")

@router.get("/leagues/")
async def get_leagues_data(request: Request):
    url = str(request.url).split("?url=")[-1]
    make_json(url, "/api/app/datas/json/season_23/leagues")

@router.get("/fixtures/")
async def get_fixtures_data(request: Request):
    url = str(request.url).split("?url=")[-1]
    make_json(url, "/api/app/datas/json/season_23/fixtures")

@router.get("/fixtures-events/")
async def get_events_data(request: Request):
    url = str(request.url).split("?url=")[-1]
    make_json(url, "/api/app/datas/json/season_23/fixtures_events")

@router.get("/fixtures-headtohead/")
async def get_headtohead_data(request: Request):
    url = str(request.url).split("?url=")[-1]
    make_json(url, "/api/app/datas/json/season_23/fixtures_headtohead")

@router.get("/fixtures-lineups/")
async def get_lineups_data(request: Request):
    url = str(request.url).split("?url=")[-1]
    make_json(url, "/api/app/datas/json/season_23/fixtures_lineups")

@router.get("/fixtures-players/")
async def get_fplayers_data(request: Request):
    url = str(request.url).split("?url=")[-1]
    make_json(url, "/api/app/datas/json/season_23/fixtures_players")

@router.get("/fixtures-statistics/")
async def get_fsattistics_data(request: Request):
    url = str(request.url).split("?url=")[-1]
    make_json(url,  "/api/app/datas/json/season_23/fixtures_statistics")





