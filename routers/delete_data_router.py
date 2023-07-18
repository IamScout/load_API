import os
from fastapi import APIRouter
from utils.scout_modules import *
from urllib.parse import unquote

router = APIRouter()

directory_mappings = {
    "teams-statistics": "/api/app/datas/json/season_22/teams_statistics",
    "teams": "/api/app/datas/json/season_22/teams",
    "standings": "/api/app/datas/json/season_22/standings",
    "predictions": "/api/app/datas/json/season_22/predictions",
    "players-topscorers": "/api/app/datas/json/season_22/players_topscorers",
    "players-squads": "/api/app/datas/json/season_22/players_squads",
    "players": "/api/datas/json/season_22/players",
    "leagues": "/api/app/datas/json/season_22/leagues",
    "fixtures": "/api/app/datas/json/season_22/fixtures",
    "fixtures-events": "api/app/datas/json/season_22/fixtures_events",
    "fixtures-headtohead": "api/app/datas/json/season_22/fixtures_headtohead",
    "fixtures-lineups": "api/app/datas/json/season_22/fixtures_lineups",
    "fixtures-players": "api/app/datas/json/season_22/fixtures_players",
    "fixtures-statistics": "api/app/datas/json/season_22/fixtures_statistics",
}

@router.get("/delete/{directory}/")
async def delete_directory_routes(directory: str):
    directory_path = directory_mappings.get(directory)
    if directory_path is None:
        return {"error": "invaled"}

    result = delete_directory_contents(directory_path)
    if result.startswith("directory"):
        return {"message": result}
    else:
        return {"error": result}