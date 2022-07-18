import brawlstats
import aiohttp
import requests
import json

TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImZlZWQ4MmFlLWE3OTItNDEyMi1iODY0LWE5NmE5YmMzNGE3ZSIsImlhdCI6MTY0Mjg2NDgyOSwic3ViIjoiZGV2ZWxvcGVyLzgwYmIxMWM5LTYyNzEtMGYwNC04MzQyLTQyMmNiNDlhZWEwYSIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiNzguMTUxLjI0NC4xMTEiXSwidHlwZSI6ImNsaWVudCJ9XX0.SI5QTWdpKNk1gFpSN3Q1N_GTS_Wa5F1-pGLebSu7aGHzxXxtMlZMUqEvRtV8u9wjkt9psusXd8jfbM1fgg2wpQ'
headers = {"Authorization": f"Bearer {TOKEN}"}


def get_info(tag):
    connector = aiohttp.TCPConnector(use_dns_cache=False)
    bs = brawlstats.Client(TOKEN, connector=connector)
    player = bs.get_player(f"{tag}")
    return player


def get_rank(trophies):
    if 0 <= trophies < 1000:
        rank = "Wooden"
        emoji = "<:Wooden:854349021727162388>"
    elif 1000 <= trophies < 2000:
        rank = "Bronze"
        emoji = "<:Bronze:854349059711172649>"
    elif 2000 <= trophies < 3000:
        rank = "Silver"
        emoji = "<:Silver:854349070167703593>"
    elif 3000 <= trophies < 4000:
        rank = "Gold"
        emoji = "<:Gold:854349139902726145>"
    elif 4000 <= trophies < 6000:
        rank = "Diamond"
        emoji = "<:Diamond:854349164582404156>"
    elif 6000 <= trophies < 8000:
        rank = "Crystal"
        emoji = "<:Crystal:854349204352401409>"
    elif 8000 <= trophies < 10000:
        rank = "Master"
        emoji = "<:Master:854349216758759434>"
    elif 10000 <= trophies:
        rank = "Star"
        emoji = "<:Star:854349232725950465>"
    return rank, emoji


def get_logo(playertag):
    corrected_tag = playertag.split('#')
    tag = corrected_tag[1]
    r = requests.get(url=f"https://api.brawlstars.com/v1/players/%23{tag}", headers=headers)
    jdata = r.json()
    return jdata['icon']['id']