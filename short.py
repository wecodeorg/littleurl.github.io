import json
import os
import shutil


def main():
    """Main Function"""
    html = "<html><script>window.location.replace('{url}');</script></html>"

    with open('urls.json') as f:
        links = json.load(f)

    shutil.rmtree('public', ignore_errors=True)
    os.mkdir('public')

    with open('public/CNAME', 'w') as f:
        f.write('littleurl.tech')

    for link in links:
        html_document = html.format(url=link['url'])
        file_path = f"public/{link['name']}.html"

        with open(file_path, 'w') as f:
            f.write(html_document)


if __name__ == "__main__":
    main()
