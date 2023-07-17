import os
from fastapi import APIRouter, Request, Query
from utils.scout_modules import *
from urllib.parse import unquote

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_dir = os.path.join(base_dir, 'datas','json', 'season_22')

router = APIRouter()


@router.get("/teams-statistics/")
async def get_team_statics_data(league:str, team:str, season:str, date:str):
    base_url = "https://v3.football.api-sports.io/teams/statistics?league={}&team={}&season={}&date={}".format(league, team, season, date)
    return make_json(base_url, "/api/app/datas/json/season_22/teams_statistics")

@router.get("/teams/")
async def get_team_data(league:str, season:str):
    base_url = "https://v3.football.api-sports.io/teams?league={}&season={}".format(league, season)
    return make_json(base_url, "/api/app/datas/json/season_22/teams")

@router.get("/standings/")
async def get_standing_data(league:str, season:str):
    base_url = "https://v3.football.api-sports.io/standings?league={}&season={}".format(league, season)
    return make_json(base_url, "/api/app/datas/json/season_22/standings")

@router.get("/predictions/")
async def get_predictions_data(fixture: str):
    base_url = "https://v3.football.api-sports.io/predictions?fixture={}".format(fixture)
    return make_json(base_url, "/api/app/datas/json/season_22/predictions")

@router.get("/players-topscorers/")
async def get_topscorers_data(league:str, season:str):
    base_url = "https://v3.football.api-sports.io/players/topscorers?league={}&season={}".format(league, season)
    return make_json(base_url, "/api/app/datas/json/season_22/players-topscorers")    

@router.get("/players-squads/")
async def get_squads_data(team:str):
    base_url = "https://v3.football.api-sports.io/players/squads?team={}".format(team)
    return make_json(base_url, "/api/app/datas/json/season_22/players-squads")

@router.get("/players/")
async def get_players_data(league:str, team:str, season:str, page:str):
    base_url = "https://v3.football.api-sports.io/players?league={}&team={}&season={}&page={}".format(league, team, season, page)
    return make_json(base_url, "/api/app/datas/json/season_22/players")

@router.get("/leagues/")
async def get_leagues_data(league: str, season:str):
    base_url = "https://v3.football.api-sports.io/leagues?id={}&season={}".format(league, season)
    return make_json(base_url, "/api/app/datas/json/season_22/leagues")

@router.get("/fixtures/")
async def get_fixtures_data(league:str, season:str, date:str, timezone:str):
    base_url = "https://v3.football.api-sports.io/fixtures?league={}&season={}&date={}&timezone={}".format(league, season, date, timezone)
    return make_json(base_url, "/api/app/datas/json/season_22/fixtures")

@router.get("/fixtures-events/")
async def get_events_data(fixture:str):
    base_url = "https://v3.football.api-sports.io/fixtures/events?fixture={}".format(fixture)
    return make_json(base_url, "/api/app/datas/json/season_22/fixtures_events")

@router.get("/fixtures-headtohead/")
async def get_headtohead_data(h2h: str, date:str, timezone:str):
    base_url = "https://v3.football.api-sports.io/fixtures/headtohead?h2h={}&date={}&timezone={}".format(h2h, date, timezone)
    return make_json(base_url, "/api/app/datas/json/season_22/fixtures_headtohead")

@router.get("/fixtures-lineups/")
async def get_lineups_data(fixture: str):
    base_url = "https://v3.football.api-sports.io/fixtures/lineups?fixture={}".format(fixture)
    return make_json(base_url, "/api/app/datas/json/season_22/fixtures_lineups")

@router.get("/fixtures-players/")
async def get_fplayers_data(fixture: str):
    base_url = "https://v3.football.api-sports.io/fixtures/players?fixture={}".format(fixture)
    return make_json(base_url, "/api/app/datas/json/season_22/fixtures_players")

@router.get("/fixtures-statistics/")
async def get_fsattistics_data(fixture:str):
    base_url = "https://v3.football.api-sports.io/fixtures/statistics?fixture={}".format(fixture)
    return make_json(base_url,  "/api/app/datas/json/season_22/fixtures_statistics")





