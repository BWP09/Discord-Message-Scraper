# Good luck to whoever wants to read this...

import sys, json 
import utils


token = utils.read_yml("C:/Users/BWP09/Desktop/Code/Python/Discord/Client/Client_Scraper/config/token.yml")["token"]

data = []
last_message_id = 0


channel_id = sys.argv[2]
number_messages = int(sys.argv[3])
number_loops = int(utils.round_up(number_messages, 50) / 50)

print(f"\nScraping {number_messages} messages from {channel_id} in {number_loops} loops\n")

messages = utils.retrieve_messages(token, channel_id)

i = 0
main_i = 0
stop = False
while not stop:
    for message in messages:
        last_message_id = message["id"]
        
        data.append({
            "content": message["content"],
            "message_id": message["id"],
            "author_id": message["author"]["id"],
            "author_username": message["author"]["username"],
            "author_discriminator": message["author"]["discriminator"],
            "timestamp": message["timestamp"],
            "attachments": message["attachments"],
            "mentions": message["mentions"]
        })

        if "reactions" in message:
            data[i]["reactions"] = message["reactions"]

            for reaction_i, reaction in enumerate(data[i]["reactions"]):
                data[i]["reactions"][reaction_i] = {
                    "name": reaction["emoji"]["name"],
                    "count": reaction["count"]
                }

        else:
            data[i]["reactions"] = []

        for attachment_i, attachment in enumerate(data[i]["attachments"]):
            try:
                data[i]["attachments"][attachment_i] = attachment["url"]
            except:
                data[i]["attachments"][attachment_i] = attachment

        for mention_i, mention in enumerate(data[i]["mentions"]):
            data[i]["mentions"][mention_i] = {
                "id": mention["id"],
                "username": mention["username"],
                "discriminator": mention["discriminator"]
            }
        
        i += 1

    messages = utils.retrieve_messages_before(token, channel_id, last_message_id)
    
    
    print(f"Done with loop {main_i} of {number_loops}", end = "\r")
    
    main_i += 1
    
    if main_i >= number_loops: break


with open(f"files/scraper/debug-{sys.argv[1]}.txt", "w", encoding = "utf-8") as output:
    output.write(json.dumps(data))

json_load = json.loads(json.dumps(data))
json_data = json.dumps(json_load, indent = 4)

with open(f"files/scraper/{sys.argv[1]}.json", "w") as output:
    output.write(json_data)

print("\nDone!")
