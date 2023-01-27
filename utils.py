import yaml, requests, json, datetime, tzlocal, pytz, math


# Reads from a YAML file and returns a dictionary
def read_yml(file_path: str):
    with open(file_path, "r") as file:
        return yaml.safe_load(file)

# Rounds a number *up* to a base
def round_up(x: int, base: int):
    return int(base * math.ceil(x / base))

# Parses UTC time (idk if it works 100% of the time)
def parse_datetime(input_time: str): #EXAMPLE: 2022-12-16T19:49:33.929000+00:00
    local_timezone = tzlocal.get_localzone()
    
    date = input_time.split("T")[0]
    utc_time = datetime.datetime.strptime(input_time.removesuffix("+00:00").split("T")[1].split(".")[0], "%H:%M:%S")
    
    local_time = str(utc_time.replace(tzinfo=pytz.utc).astimezone(local_timezone)).split(" ")[1].split("-")[0]
    
    year = date.split("-")[0]
    month = date.split("-")[1]
    day = date.split("-")[2]
    
    return f"{month}-{day}-{year} {local_time}"

# Retrieves and returns messages from a discord channel
def retrieve_messages(token: str, channel_id: int | str):
    header = { "authorization": token }
    
    r = requests.get(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers = header)
    return json.loads(r.text)

# Retrieves and returns messages from a discord channel after a specified message
def retrieve_messages_after(token: str, channel_id: int | str, after_id: int | str):
    header = { "authorization": token }
    
    r = requests.get(f"https://discord.com/api/v9/channels/{channel_id}/messages?limit=50&after={after_id}", headers = header)
    return json.loads(r.text)

# Retrieves and returns messages from a discord channel before a specified message
def retrieve_messages_before(token: str, channel_id: int | str, before_id: int | str):
    header = { "authorization": token }
    
    r = requests.get(f"https://discord.com/api/v9/channels/{channel_id}/messages?limit=50&before={before_id}", headers = header)
    return json.loads(r.text)