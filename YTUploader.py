import googleapiclient.discovery
import googleapiclient.errors
from google_auth_oauthlib.flow import InstalledAppFlow

def get_authenticated_client():
    # Define the scopes you need for the YouTube Data API
    SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

    # Create the OAuth 2.0 flow
    flow = InstalledAppFlow.from_client_secrets_file(
        "client_secret.json", scopes=SCOPES
    )
    # Authenticate and authorize the application
    credentials = flow.run_local_server(port=8080, open_browser=True)
    client = googleapiclient.discovery.build("youtube", "v3", credentials=credentials)

    return client

def upload_video(client, video):
    request_body = {
        "snippet": {
            "title": video["title"],
            "description": video["description"],
            "tags": video["tags"],
            "categoryId": video["categoryId"],
            "defaultLanguage": video["language"],
            "locationDescription": video["location"],
        },
        "status": {
            "privacyStatus": video["status"],
            "publishAt": video["publish_at_time"],
        },
    }

    try:
        response = client.videos().insert(
            part = "snippet,status",
            body = request_body,
            media_body = video["path"],
        ).execute()

        print("Video uploaded successfully. Video ID:", response["id"])

    except googleapiclient.errors.HttpError as e:
        print("An error occurred:", e)