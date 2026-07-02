import requests


def download_images(url, image_id):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        r.raw.decode_content = True
        file_name = f"images/{image_id}.jpg"
        with open(file_name, "wb") as f:
            f.write(r.content)
        print(f"Downloaded image {file_name}")
    else:
        print(f"Failed to retrieve image {image_id}")
