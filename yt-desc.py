from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Replace API_KEY with your actual API key
API_KEY = 'AIzaSyC3ElvfankD9Hf6ujrk3MUH1WIm_cu87XI'

# Replace VIDEO_ID with the ID of the video you want to get the description of
VIDEO_ID = 'gIl_4W-x65s'

youtube = build('youtube', 'v3', developerKey=API_KEY)

try:
    response = youtube.videos().list(
        part='snippet',
        id=VIDEO_ID
    ).execute()

    description = response['items'][0]['snippet']['description']
    desc = description.replace('\n', '')
    print(desc)

except HttpError as e:
    print('An error occurred: %s' % e)

