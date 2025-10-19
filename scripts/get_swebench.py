from email import message_from_binary_file, policy
from bs4 import BeautifulSoup
import csv

file_path = "pages/SWE-bench.mhtml"
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
table = soup.find("div", {"class": "background-primary overflow-x-auto sm:overflow-x-hidden"})
rows = table.find_all("a")
with open("leaderboards/leaderboard_swebench.csv", "w", newline="", encoding="utf-8") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["Name", "Score"])
    for row in rows:
        ps = row.find_all("p")
        name = ps[1].get_text(strip=True)
        score = ps[2].get_text(strip=True).split("%")[0]

        csvwriter.writerow([name, score])
