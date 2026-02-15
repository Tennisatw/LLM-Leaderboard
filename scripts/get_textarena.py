from email import message_from_binary_file, policy
from bs4 import BeautifulSoup
import csv
import re

file_path = "pages/Text Arena _ LMArena.mhtml"
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

with open("leaderboards/leaderboard_textarena.csv", "w", newline="", encoding="utf-8") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["Name", "Score"])
    for row in rows:
        cols = row.find_all("td")
        if not cols:
            continue

        # Current structure: Rank / Rank Spread / Model / Score / Votes
        model_col = cols[2]
        score_col = cols[3]

        name_tag = model_col.select_one("a span.truncate")
        if name_tag is None:
            name_tag = model_col.select_one("span.truncate")
        name = name_tag.get_text(strip=True) if name_tag else model_col.get_text(" ", strip=True)

        score_text = score_col.get_text(" ", strip=True)
        score_match = re.search(r"\d{3,4}", score_text)
        arena_score = score_match.group(0) if score_match else score_text.replace("Preliminary", "").strip()

        csvwriter.writerow([name, arena_score])
