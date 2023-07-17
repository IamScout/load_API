import shutil
import requests,json,os
#from google.cloud import storage

#RAW DATA 수집
def make_json(uri, DIRECTORY):
    print(uri)
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
    conn.close()

    folder_path = file_dir
    file_list = os.listdir(folder_path)
    file_count = len(file_list)

    if file_count == int(today_round):
        os.system(f'touch {file_dir}/DONE')
        return "Check {file_dir} data success"
    else:
        return "Check {file_dir} data failed"

#디렉토리 파일 갯수 확인
def check_clean_data(file_dir, cnt):

    folder_path = file_dir
    file_list = os.listdir(folder_path)
    file_count = len(file_list)
    if file_count == int(cnt):

        os.system(f'touch {file_dir}/DONE')
        return f"check {file_dir} data success"
    else:
        return f"check {file_dir} data failed"

#디렉토리 데이터 클렌징
def delete_directory_contents(directory):
    # 디렉토리 존재 확인
    if not os.path.exists(directory):
        print(f"{directory} not exists!")
        return

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"{file_path} deleting while err:", str(e))
    
    return (f"{directory} deleting complete")

#경로 받아서 해당 디렉토리 데이터레이크 던지기
def blob_data(point_dir):
    json_path = "/api/app/config/abstract-robot-390510-cb4515df5695.json"
    #json_path = 'C:/Users/user/PycharmProjects/soccer_pipe_line/pipeline_scout/humming-bird-383304-fa3fcb3047b6.json'
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = json_path

    client = storage.Client()

    bucket_name = 'scouter_dl'
    bucket = client.get_bucket(bucket_name)

    # API 데이터 경로
    local_directory = point_dir

    # 로컬 디렉토리의 모든 파일을 반복
    for dirpath, dirs, files in os.walk(local_directory):
        for file_name in files:
            local_file_path = os.path.join(dirpath, file_name)
        
            gcs_object_name = local_file_path.replace(local_directory, '')
            gcs_object_name = gcs_object_name.replace(os.path.sep, '/')
            
            blob = bucket.blob(gcs_object_name)
            with open(local_file_path, 'rb') as file:
                load_blob = blob.upload_from_file(file)
                print(f"{local_file_path} uploaded to gs://{bucket_name}/{gcs_object_name}")


