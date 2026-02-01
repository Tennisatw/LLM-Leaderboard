from email import message_from_binary_file, policy
from bs4 import BeautifulSoup
import csv

file_path = "pages/LiveCodeBench Benchmark Leaderboard _ Artificial Analysis.mhtml"
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
graph = soup.find("div", class_="lg:overflow-visible")

# texts = table.get_text("\n", strip=True).split("\n")
text_element = graph.find_all("text")
texts = []
for elem in text_element:
    text = elem.get_text(strip=True)
    sibling = elem.find_next_sibling()
    if sibling and sibling.find(class_="lucide-lightbulb"):
        text = text + " reasoning"
    texts.append(text)

model_names = [text for text in texts if not "%" in text][1:]
values = [text for text in texts if "%" in text]

with open("leaderboards/leaderboard_livecodebench.csv", "w", newline="", encoding="utf-8") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["Name", "Score"])
    for model_name, value in zip(model_names, values):
        score = value.replace("%", "")
        csvwriter.writerow([model_name, score])