import discord
import config

mdmbot = discord.Client()

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

      await user.send(config.dm_message)

      print(f"Successfully message sent to: {user.name}")
    except:
       print(f"Failed to send message to: {user.name}")

mdmbot.run(config.token, bot=False)
