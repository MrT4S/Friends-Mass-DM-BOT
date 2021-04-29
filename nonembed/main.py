import discord
import json

mdmbot = discord.Client()

with open("config.json", "r") as config:
    get = json.load(config)
    token = get["token"]
    message = get["message"]

@mdmbot.event
async def on_connect():
  print("User Logged Into:")
  print("-----------------")
  print(mdmbot.user.name)
  print(mdmbot.user.id)
  print("-----------------")
  print("Started massing..")
  print("-----------------")

  for user in mdmbot.user.friends:
    try:

      await user.send(message)

      print(f"Successfully message sent to: {user.name}")
    except:
       print(f"Failed to send message to: {user.name}")

mdmbot.run(token, bot=False)