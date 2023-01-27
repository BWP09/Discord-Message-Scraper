import sys, json, re
import utils


users = {}

# Loads messages from a JSON output
with open(f"files/scraper/{sys.argv[1]}.json", encoding = "utf-8") as data:
    json_data = json.load(data)

# Correlates a user ID with a username, used for replacing mentions
for message in json_data:
    users[message["author_id"]] = f'{message["author_username"]}#{message["author_discriminator"]}'

# Actually replaces the ID mentions with username ones
# (normal mentions look kinda like this <@ID>, makes them look like @USERNAME)
for i, message in enumerate(json_data):
    if re.search(r"<@\d{18}>", message["content"]) != None:
        for user_mention in re.findall(r"<@\d{18}>", message["content"]):
            json_data[i]["content"] = re.sub(r"<@\d{18}>", "@" + users[user_mention.removeprefix("<@").removesuffix(">")], message["content"], 1)

# Replaces UTC timestamp
for i, message in enumerate(json_data):
    json_data[i]["timestamp"] = utils.parse_datetime(message["timestamp"])


# Writes processed input to a debug txt file just incase anything happens
with open(f"files/processor/debug-{sys.argv[2]}.txt", "w", encoding = "utf-8") as output:
    output.write(json.dumps(json_data))

json_load = json.loads(json.dumps(json_data))
json_dump = json.dumps(json_load, indent = 4)

# Writes processed JSON to the final output JSON file
with open(f"files/processor/{sys.argv[2]}.json", "w") as output:
    output.write(json_dump)

print("\nDone!")