# Download the mhtml webpage.
# https://mmmu-benchmark.github.io/

from email import message_from_binary_file, policy
from bs4 import BeautifulSoup
import csv

file_path = "page_mmmu.mhtml"
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

with open("leaderboard_mmmu.csv", "w", newline="", encoding="utf-8") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["Name", "Date", "Score"])
    for row in rows:
        cols = row.find_all("td")
        name = cols[0].get_text(strip=True)
        date = cols[2].get_text(strip=True)
        mmmu_score = cols[6].get_text(strip=True).replace("*", "")

        csvwriter.writerow([name, date, mmmu_score])
