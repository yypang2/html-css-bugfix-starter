from bs4 import BeautifulSoup
import os

def grade(html_path, css_path):
    score = 0
    max_score = 10

    with open(html_path, 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')

    with open(css_path, 'r') as f:
        css = f.read().replace(" ", "").replace("\n", "").lower()

    html = open(html_path).read().lower()

    if "<!doctypehtml>" in html:
        score += 1
    if soup.html and soup.html.get("lang") == "en":
        score += 1
    if soup.find("nav"):
        score += 1
    if soup.find("link", rel="stylesheet") and 'style.css' in html:
        score += 1
    if "display:grid" in css and "grid-template-columns" in css:
        score += 1
    if "object-fit:cover" in css or "width:100%" in css:
        score += 1
    if ".current:hover{text-decoration:underline;}" in css:
        score += 1
    if ".card{" in css and ("display:grid" in css or "display:flex" in css):
        score += 1
    if soup.find("h2") and "</h2>" in html:
        score += 1
    if not soup.body.get("style"):
        score += 1

    return score, max_score

if __name__ == "__main__":
    html_path = "index.html"
    css_path = "style.css"
    score, total = grade(html_path, css_path)
    print(f"✅ Your Score: {score}/{total}")
