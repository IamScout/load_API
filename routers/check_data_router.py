import os
from fastapi import APIRouter, Request, Query
from utils.scout_modules import *
from urllib.parse import unquote

router = APIRouter()

# 팀갯수 895개 -> 리그갯수 55개

# 88몇개 팀갯수 이새끼 다른함수 만들어야함
@router.get("/check/teams-statistics/")
async def check_team_statics_data(dir:str, cnt:str, date:str):

#55개 리그 갯수
@router.get("/check/teams/")
async def check_team_data(dir:str, cnt:str):
    return check_clean_data("/api/app/datas/json/season_22/teams", cnt)

#리그 갯수
@router.get("/check/standings/")
async def check_standing_data(dir:str, cnt:str):
    return check_clean_data("/api/app/datas/json/season_22/standings", cnt)


#당일 경기갯수
@router.get("/check/predictions/")
async def check_predictions_data(dir:str, date:str):
    return check_today_Fdata("/api/app/datas/json/season_22/predictions", date)

#리그 갯수
@router.get("/check/players-topscorers/")
async def check_topscorers_data(dir:str, cnt:str):
    return check_clean_data("/api/app/datas/json/season_22/players_topscorers", cnt)

   
# 팀갯수 88몇개
@router.get("/check/players-squads/")
async def check_squads_data(dir:str, cnt:str):
    return check_clean_data("/api/app/datas/json/season_22/players_squads", cnt)


# 5 * 팀 갯수
@router.get("/check/players/")
async def check_players_data(dir:str, cnt:str):

# 리그갯수
@router.get("/check/leagues/")
async def check_leagues_data(dir:str, cnt:str):
    return check_clean_data("/api/app/datas/json/season_22/leauges", cnt)


# 리그 갯수
@router.get("/check/fixtures/")
async def check_fixtures_data(dir:str, cnt:str):
    return check_clean_data("/api/app/datas/json/season_22/fixtures", cnt)


# 당일 경기 갯수
@router.get("/check/fixtures-events/")
async def check_events_data(dir:str, date:str):
    return check_today_Fdata("api/app/datas/json/season_22/fixtures_events", date)

# 당일 경기 갯수
@router.get("/check/fixtures-headtohead/")
async def check_headtohead_data(dir:str, date:str):
    return check_today_Fdata("api/app/datas/json/season_22/fixture_headtohead", date)

# 당일 경기 갯수
@router.get("/check/fixtures-lineups/")
async def check_lineups_data(dir:str, date: str):
    return check_today_Fdata("api/app/datas/json/season_22/fixture_lineups", date)

# 당일 경기 갯수
@router.get("/check/fixtures-players/")
async def check_fplayers_data(dir:str, date: str):
    return check_today_Fdata("api/app/datas/json/season_22/fixture_players", date)

# 당일 경기 갯수
@router.get("/check/fixtures-statistics/")
async def check_fsattistics_data(dir:str, date:str):
    return check_today_Fdata("api/app/datas/json/season_22/fixtures_statistics", date)