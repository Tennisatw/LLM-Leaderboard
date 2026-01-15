from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from pathlib import Path
import json, csv, re, io

def get_benchmark(url, html_path, csv_path):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page()
        page.goto(url, wait_until="domcontentloaded", timeout=240000)
        page.wait_for_timeout(12000)
        html = page.content()
        browser.close()

    with open(html_path, "w", encoding="utf-8") as file:
        file.write(html)

    if "artificialanalysis.ai/evaluations/" in url:
        benchmark_name = url.rsplit("/", 1)[-1]
        key = {
            "terminalbench-hard": "terminalbench_hard",
            "artificial-analysis-long-context-reasoning": "lcr",
            "humanitys-last-exam": "hle",
            "gpqa-diamond": "gpqa",
            "scicode": "scicode",
            "ifbench": "ifbench",
            "critpt": "critpt",
            "mmmu-pro": "mmmu_pro",
            "omniscience": "omniscience",
        }.get(benchmark_name)

        models_pattern = '\\"models\\":[' if '\\"models\\":[' in html else '"models":['
        pattern_index = html.find(models_pattern)
        models_chunk = html[pattern_index + len(models_pattern) - 1:]

        bracket_depth = 0
        chunk_end_index = 0
        for chunk_index, chunk_char in enumerate(models_chunk):
            if chunk_char == "[":
                bracket_depth += 1
            elif chunk_char == "]":
                bracket_depth -= 1
                if bracket_depth == 0:
                    chunk_end_index = chunk_index + 1
                    break

        models_text = models_chunk[:chunk_end_index].replace("\r", "").replace("\n", "\\n")
        models_list = json.loads(json.loads('"' + models_text + '"')) if '\\"' in models_text else json.loads(models_text)

        result_list = []
        for model in models_list:
            model_name = model["name"].strip()
            if benchmark_name == "omniscience":
                breakdown = model.get("omniscience_breakdown")
                if not breakdown:
                    continue
                score = float(breakdown["total"]["accuracy"])
            else:
                score = model.get(key)
                if score is None:
                    continue
                score = float(score)

            if 0 <= score <= 1:
                score *= 100
            result_list.append((model_name, str(score).rstrip("0").rstrip(".")))

        with open(csv_path, "w", newline="", encoding="utf-8") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["Name", "Score"])
            csv_writer.writerows(result_list)
        return

    if "lmarena.ai" in url:
        text_lines = [
            line_text.strip()
            for line_text in BeautifulSoup(html, "html.parser").get_text("\n").splitlines()
            if line_text.strip()
        ]
        line_count = len(text_lines)
        result_list = []

        for line_index in range(1, line_count):
            if "◄─►" not in text_lines[line_index] or not text_lines[line_index - 1].isdigit():
                continue

            scan_index = line_index + 1
            while scan_index < line_count and not re.search(r"[A-Za-z].*[\d\-]", text_lines[scan_index]):
                scan_index += 1
            if scan_index >= line_count:
                continue

            model_name = text_lines[scan_index].strip()

            scan_index += 1
            while scan_index < line_count and not re.match(r"\d", text_lines[scan_index]):
                scan_index += 1
            if scan_index >= line_count:
                continue

            score_text = re.search(r"\d+(\.\d+)?", text_lines[scan_index]).group(0)
            result_list.append((model_name, score_text))

        with open(csv_path, "w", newline="", encoding="utf-8") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["Name", "Score"])
            csv_writer.writerows(result_list)
        return


Path("pages").mkdir(exist_ok=True)
Path("leaderboards").mkdir(exist_ok=True)

benchmark_list = [
    ("terminalbenchhard", "https://artificialanalysis.ai/evaluations/terminalbench-hard"),
    ("aalcr", "https://artificialanalysis.ai/evaluations/artificial-analysis-long-context-reasoning"),
    ("omniscience", "https://artificialanalysis.ai/evaluations/omniscience"),
    ("hle", "https://artificialanalysis.ai/evaluations/humanitys-last-exam"),
    ("gpqadiamond", "https://artificialanalysis.ai/evaluations/gpqa-diamond"),
    ("scicode", "https://artificialanalysis.ai/evaluations/scicode"),
    ("ifbench", "https://artificialanalysis.ai/evaluations/ifbench"),
    ("critpt", "https://artificialanalysis.ai/evaluations/critpt"),
    ("mmmupro", "https://artificialanalysis.ai/evaluations/mmmu-pro"),
    ("lmarena_text", "https://lmarena.ai/zh/leaderboard/text"),
]

for name, url in benchmark_list:
    get_benchmark(url, f"pages/{name}.html", f"leaderboards/{name}.csv")



"""
The complete table for GDPval is listed separately and readily available for use
"""
Path("leaderboards").mkdir(exist_ok=True)

gdpval_url = "https://artificialanalysis.ai/evaluations/gdpval-aa#gdpval-leaderboard-table"
gdpval_csv_path = "leaderboards/gdpvalaa.csv"

with sync_playwright() as playwright:
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.goto(gdpval_url, wait_until="networkidle")
    table_element = page.locator('[id$="leaderboard-table"] table').first

    header_texts = [header_text.strip() for header_text in table_element.locator("thead th").all_inner_texts()]
    name_col_index = header_texts.index("Name")
    score_col_index = next(
        col_index
        for col_index, header_text in enumerate(header_texts)
        if header_text in ("Score", "ELO", "Elo", "Accuracy")
    )

    result_list = []
    for row_element in table_element.locator("tbody tr").all():
        cell_texts = [cell_text.strip() for cell_text in row_element.locator("td").all_inner_texts()]
        match = re.search(r"-?\d+(\.\d+)?", cell_texts[score_col_index].replace("%", ""))
        if match:
            result_list.append((cell_texts[name_col_index], match.group(0)))

    with open(gdpval_csv_path, "w", newline="", encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Name", "Score"])
        csv_writer.writerows(result_list)

    browser.close()

