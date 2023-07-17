import requests,json,os

#RAW DATA 수집
def make_json(uri, DIRECTORY):
    start_index = uri.find("io/") + 3
    end_index = uri.find("?")

    if start_index != -1 and end_index != -1:
        words = uri[start_index:end_index].split("/")
        english_words = [word for word in words if word.isalpha()]
        FILENAME = "-".join(english_words)

    params = uri.split("&")
    for param in params:
        key, value = param.split("=")
        if key != "season":
            FILENAME += f"-{value}"
    headers = {
        'x-rapidapi-host': "v3.football.api-sports.io",
        'x-rapidapi-key': "e6b9fb7ce7a7ad7b239595f76e546384"
    }

    # GET RESPONSE
    response = requests.request("GET", uri, headers=headers).json()
    
    # FILE WRITE
    try:
        with open(f"{DIRECTORY}/{FILENAME}.json", "w") as file:
            json.dump(response, file, indent=4)
        return (FILENAME + " load is done")
    except:
        return (FILENAME + " load failed")

#당일 축구 경기 몇개있는지 확인하기
def check_today_Fdata(file_dir, date):
    import mysql.connector as mc
    import os, subprocess

    conn = mc.connect(user='root', password='tmzkdnxj1', host='34.64.200.213', database='pipeline_scout', port='3306')

    cursor = conn.cursor()
    QUERY = f"SELECT api_fixture_id FROM pipe_round WHERE date = '{date}'"
    cursor.execute(QUERY)
    fetched = cursor.fetchall()
    today_round = len(fetched)

    folder_path = file_dir
    file_list = os.listdir(folder_path)
    file_count = len(file_list)
    
    if file_count == today_round:

        os.system(f'touch {file_dir}/DONE')
        return "Check {file_dir} data success"
    else:
        return "Check {file_dir} data failed"

def check_clean_data(file_dir, cnt):

    folder_path = file_dir
    file_list = os.listdir(folder_path)
    file_count = len(file_list)

    if file_count == cnt:
        os.system(f'touch {file_dir}/DONE')
        return f"check {file_dir} data success"

    else:
        return f"check {file_dir} data failed"




