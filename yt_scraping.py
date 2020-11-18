from googleapiclient.discovery import build

api_key = 'AIzaSyD8MPM4GvacunTqX8sWgiMZ7QdV1hUnxlE'
youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.channels().list(
    part='statistics',
    forUsername='schafer5'
)

response = request.execute()

print(response)
