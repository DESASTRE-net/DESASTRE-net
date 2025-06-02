import os

banner_path = os.path.join(os.path.dirname(__file__), "banner.txt")

if os.path.isfile(banner_path):
    with open(banner_path, "r", encoding="utf-8") as f:
        print(f.read())
