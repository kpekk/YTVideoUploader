from datetime import datetime, timedelta
from pathlib import Path
import time
from YTUploader import get_authenticated_client, upload_video

description = "We live on an amazing planet full of all kinds of animals. I post interesting facts about all kinds of animals. Do you have a favourite wild animal? Leave a comment so that i could make the next video about your favourite animal! Subscribe for more!"
tags = ["shorts", "animals"]
categoryId = "15" # pets and animals
language = "en"
title = "Animal fact you probably didn't know"
location = "New York City"

status = "private"

youtubeClient = get_authenticated_client()

# reveal each video 24h after the previous one
day = 0
for file in Path("videos").iterdir():
    # TODO delete files after upload? (may not be the best idea)

    path_to_video = f"videos/{file.name}"
    publish_at_time = (datetime.utcnow() + timedelta(hours=(24*day), minutes=5)).isoformat() + "Z"

    video = {
        "path": path_to_video,
        "title": title,
        "description": description,
        "tags": tags,
        "categoryId": categoryId,
        "language": language,
        "location": location,
        "status": status,
        "publish_at_time": publish_at_time,
    }

    print(f"[info] Uploading {file.name}")
    upload_video(youtubeClient, video)

    day+=1
    time.sleep(2)