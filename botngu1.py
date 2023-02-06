import discord
import requests
import json
import random
import db

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

sad_words = ("buồn", "depressed", "unhappy", "chán", "sad")

name = ("nam","Nam",
        "Hiệp","Hiep", "hiep", "hiệp",
        "Hải", "hai","Hai","Hải","hải", 
        "Hà", "ha","hà","Ha",
        "thái","thai","Thái",
        "tùng","Tùng","tung",
        "chử","Chử","chu",
        "hoang","hoàng","Hoàng",
        "huy","Huy",
        "Tú","tú","Tu",
        "Vinh","vinh",
        "tùng","Tùng")
name1 = ("thịnh","thinh","Thịnh")

starter_encouragements = (
  "kệ mẹ mày.",
  "buồn con mẹ mày",
  "đéo quan tâm"
)

chuichetmemay = ("ăn cứt",
                 "óc con chó", 
                 "con mẹ mày loz to", 
                 "là 1 con súc vật", 
                 "cả nhà ăn cứt",
                 "cả nhà chết sạch"
            )

nice=("Đẹp zai","Khoai to","Cu bự")

# if "responding" not in db.keys():
#   db["responding"] = True

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]["q"] + " -" + json_data[0]["a"]
  return(quote)

# def update_encouragements(encouraging_message):
#   if "encouragements" in db.keys():
#     encouragements = db["encouragements"]
#     encouragements.append(encouraging_message)
#     db["encouragements"] = encouragements
#   else:
#     db["encouragements"] = [encouraging_message]

# def delete_encouragment(index):
#   encouragements = db["encouragements"]
#   if len(encouragements) > index:
#     del encouragements[index]
#   db["encouragements"] = encouragements

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith("đạo lý"):
    quote = get_quote()
    await message.channel.send(quote)
    
  if msg.startswith (sad_words):
      await message.channel.send(random.choice(starter_encouragements))

  if msg.startswith (name):
      await message.channel.send(msg + " "+ random.choice(chuichetmemay))
      
  if msg.startswith (name1):
      await message.channel.send(msg +" " + random.choice(nice))
      
#   if msg in sad_words:
#       await message.channel.send(random.choice(starter_encouragements))
#   if db["responding"]:
#     options = starter_encouragements
#     if "encouragements" in db.keys():
#       options = options + db["encouragements"]

    # if msg.startswith (sad_words):
    #   await message.channel.send(random.choice(starter_encouragements))

#   if msg.startswith("$new"):
#     encouraging_message = msg.split("$new ",1)[1]
#     update_encouragements(encouraging_message)
#     await message.channel.send("New encouraging message added.")

#   if msg.startswith("$del"):
#     encouragements = []
#     if "encouragements" in db.keys():
#       index = int(msg.split("$del",1)[1])
#       delete_encouragment(index)
#       encouragements = db["encouragements"]
#     await message.channel.send(encouragements)

#   if msg.startswith("$list"):
#     encouragements = []
#     if "encouragements" in db.keys():
#       encouragements = db["encouragements"]
#     await message.channel.send(encouragements)
    
#   if msg.startswith("$responding"):
#     value = msg.split("$responding ",1)[1]

#     if value.lower() == "true":
#       db["responding"] = True
#       await message.channel.send("Responding is on.")
#     else:
#       db["responding"] = False
#       await message.channel.send("Responding is off.")

client.run("MTAxNDA2OTg0NzI3MDg4NzQyNA.GWf_AO.Er9k_jBEXXp8Tbux5D0UQ77BBArbW_fY3PVcXA")