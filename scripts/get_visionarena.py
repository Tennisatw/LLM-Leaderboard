from email import message_from_binary_file, policy
from bs4 import BeautifulSoup
import csv

file_path = "pages/Vision Arena _ LMArena.mhtml"
with open(file_path, "rb") as f:
    msg = message_from_binary_file(f, policy=policy.default)

html = None
for part in msg.walk():
    if part.get_content_type() == "text/html":
        html = part.get_content()  # 自动根据编码类型解码
        break
if html is None:
    raise ValueError("No HTML part found in the MHTML file.")

soup = BeautifulSoup(html, "html.parser")
table = soup.find("table")
tbody = table.find("tbody")
rows = tbody.find_all("tr")

with open("leaderboards/leaderboard_visionarena.csv", "w", newline="", encoding="utf-8") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["Name", "Score"])
    for row in rows:
        cols = row.find_all("td")
        name = cols[2].get_text(strip=True)
        arena_score = cols[3].get_text(strip=True).replace("Preliminary", "").strip()

        csvwriter.writerow([name, arena_score])
