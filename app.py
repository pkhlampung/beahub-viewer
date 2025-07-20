from flask import Flask, Response
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def scrape_santrihub():
    url = "https://santrihub.id/info-beasiswa/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    content = soup.find("div", {"data-id": "dc5a89e"})

    if content:
        html = f"""
        <html>
        <head>
            <meta charset="UTF-8">
            <title>SantriHub Beasiswa</title>
        </head>
        <body>
            {content}
        </body>
        </html>
        """
        return Response(html, mimetype="text/html")
    else:
        return "Konten tidak ditemukan", 404

if __name__ == "__main__":
    app.run(debug=True)
