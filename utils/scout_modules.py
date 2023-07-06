
#무야호
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
    with open(f"{DIRECTORY}/{FILENAME}", "w") as file:
        json.dump(response, file, indent=4)
    return(FILENAME + " load is done")