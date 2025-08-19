# Download the mhtml webpage.
# https://artificialanalysis.ai/evaluations/artificial-analysis-long-context-reasoning?models=o4-mini%2Co3%2Cgpt-oss-120b%2Cgpt-oss-20b%2Cgpt-4-1%2Cgpt-5-nano%2Cgpt-5-medium%2Cgpt-5-minimal%2Cgpt-5%2Cgpt-4o-chatgpt%2Cgpt-5-low%2Cgpt-5-mini%2Cllama-3-3-instruct-70b%2Cllama-4-scout%2Cllama-4-maverick%2Cgemma-3-12b%2Cgemini-2-5-flash%2Cgemini-2-5-flash-reasoning%2Cgemini-2-5-pro%2Cclaude-4-sonnet%2Cclaude-4-opus-thinking%2Cclaude-4-sonnet-thinking%2Cclaude-4-opus%2Cdevstral-medium%2Cmistral-small-3-2%2Cmistral-medium-3%2Cmistral-medium-3-1%2Cdeepseek-r1%2Cgrok-4%2Cgrok-3-mini-reasoning%2Cnova-premier%2Cminimax-m1-80k%2Cllama-nemotron-super-49b-v1-5%2Cllama-nemotron-super-49b-v1-5-reasoning%2Cllama-3-1-nemotron-ultra-253b-v1-reasoning%2Ckimi-k2%2Cgranite-3-3-8b-instruct%2Cexaone-4-0-32b-reasoning%2Cglm-4.5%2Ccommand-a%2Cqwen3-coder-480b-a35b-instruct%2Cqwen3-235b-a22b-instruct-2507%2Cqwen3-235b-a22b-instruct-2507-reasoning%2Cllama-3-1-instruct-8b%2Cgemini-2-0-flash%2Cmistral-small-3-1%2Cdeepseek-v3-0324%2Cnova-pro%2Cnova-lite%2Cnova-micro

from email import message_from_binary_file, policy
from bs4 import BeautifulSoup
import csv

file_path = "page_aalcr.mhtml"
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
graph = soup.find("div", class_="h-80")

# texts = table.get_text("\n", strip=True).split("\n")
texts = [text.get_text(strip=True) for text in graph.find_all("text")]
model_names = [text for text in texts if not "%" in text][1:]
values = [text for text in texts if "%" in text]

with open("leaderboard_aalcr.csv", "w", newline="", encoding="utf-8") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["Name", "Score"])
    for model_name, value in zip(model_names, values):
        score = value.replace("%", "")
        csvwriter.writerow([model_name, score])