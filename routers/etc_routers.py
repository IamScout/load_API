import os
from fastapi import APIRouter, Request, Query
from utils.scout_modules import *
from urllib.parse import unquote

router = APIRouter()

# 팀갯수 895개 -> 리그갯수 55개

@router.get("/done-flag/")
async def flag_check_data(target_dir:str):
    return check_flag_directory(target_dir)

@router.get("/before/done-flag/")
async def before_flag_check(target_dir:str):
    return check_empty_directory(target_dir)


@router.get("/blob-data/")
async def blob_to_dl(target_dir:str):
    return blob_data(target_dir)
