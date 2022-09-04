import gspread
import discord
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# ***.json　は各自ダウンロードしたjsonファイル名に変更してください
credentials = ServiceAccountCredentials.from_json_keyfile_name('winnerbot-879f2b229551.json', scope)
gc = gspread.authorize(credentials)

# スプレッドシートのキーを入れてください
SPREAD_SHEET_KEY = "1Qoj0zJcr4TCl7oIPMlMxmhOVxFwNoRMIi_RLyZcsVEA"
workbook = gc.open_by_key(SPREAD_SHEET_KEY)

#DiscordのBotのTokenを入れてください。
DISCORD_TOKEN = "MTAxNTc3MjYxOTAyNDM3NTkzMA.GXucEj.KR8cWIPAp__E8QvqHjMBinwRCif4vMzsDtMUjs"
client = discord.Client()

@client.event
async def on_message(message):  # メッセージを受け取ったときの挙動
    if message.author.bot:  # Botのメッセージは除く
        return
    print(message.content)
    worksheet_list = workbook.worksheets()
    #　1つ目のシートのセル(1,1)をDiscordに送ったメッセージ内容で更新
    worksheet_list[0].update_cell(1, 1, message.content)

client.run(DISCORD_TOKEN)