from src.core import app
from pathlib import Path


def main(url):
    app.init(url)


if __name__ == "__main__":
    urls = Path('urls.txt').read_text(encoding='utf8').split('\n')
    for url in urls:
        if url.startswith('#'):
            continue
        main(url)
