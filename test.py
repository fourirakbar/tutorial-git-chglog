import json
import time
import requests
from slackclient import SlackClient

webhook_url = 'https://hooks.slack.com/services/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'
slack_data = {'text': "[Test] Klop"}
delay = 60 

site_urls = [["https://kredivo.id", 1], ["https://finaccel.co", 1]]

def send_slack(text):
  print("masuk")
  slack_token = "T0F6M3DV1/B01A9685NUF/fGsIiV7j1phQ4w5rP8fu6Njc" # tapi better di taruh .env
  sc = SlackClient(slack_token)

  sc.api_call(
    "chat.postMessage",
    channel="#grafana-alerts",
    text="Test send notif to slack, please ignore"
  )
  print("masuk lagi hehe")
  return requests.post('https://slack.com/api/chat.postMessage', {
      'token': 'T0F6M3DV1/B01A9685NUF/fGsIiV7j1phQ4w5rP8fu6Njc', #better di taruh env tapi pak, biar aman
      'channel': '#operation-team-jira',
      'text': text
  }).json()  

if __name__ == "__main__":
  while 1:
    for site_url in site_urls:    
      resp = requests.head(site_url[0])

      if resp.status_code != 200:
        text = "Web %s UP again. Response is:\n%s", site_url[0], resp.status_code

        if site_url == site_urls[0][0] and site_urls[0][-1] == 0:
          site_urls[0][-1] = 1
          send_slack(text)
          
        elif site_url == site_urls[1][0] and site_urls[1][-1] == 0:
          site_urls[1][-1] = 1
          send_slack(text)
      
      else:
        if site_url == site_urls[0][0]:
          site_urls[0][-1] = 0
        else:
          site_urls[1][-1] = 0

        text = "Request to slack returned an error %s, the response is:\n%s", site_url[0], resp.status_code
        send_slack(text)

    time.sleep(delay)



        