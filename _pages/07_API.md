from email.policy import default
from operator import truediv


---
layout: default
permalink: /sportspage/
title: Sports 🏟
search_exclude: true
---

import requests

url = "https://sportspage-feeds.p.rapidapi.com/teams"

querystring = {"league":"<REQUIRED>"}

headers = {
	"X-RapidAPI-Key": "f2586bd8c7mshe64d56ce3a69011p10e170jsn51b21e88070f",
	"X-RapidAPI-Host": "sportspage-feeds.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)