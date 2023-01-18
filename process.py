import sys, json, re
import utils


users = {}

with open(f"files/scraper/{sys.argv[1]}.json", encoding = "utf-8") as data:
    json_data = json.load(data)
    
for message in json_data:
    users[message["author_id"]] = f'{message["author_username"]}#{message["author_discriminator"]}'

for i, message in enumerate(json_data):
    if re.search(r"<@\d{18}>", message["content"]) != None:
        for user_mention in re.findall(r"<@\d{18}>", message["content"]):
            json_data[i]["content"] = re.sub(r"<@\d{18}>", "@" + users[user_mention.removeprefix("<@").removesuffix(">")], message["content"], 1)

for i, message in enumerate(json_data):
    json_data[i]["timestamp"] = utils.parse_datetime(message["timestamp"])


with open(f"files/processor/debug-{sys.argv[2]}.txt", "w", encoding = "utf-8") as output:
    output.write(json.dumps(json_data))

json_load = json.loads(json.dumps(json_data))
json_dump = json.dumps(json_load, indent = 4)

with open(f"files/processor/{sys.argv[2]}.json", "w") as output:
    output.write(json_dump)

print("\nDone!")