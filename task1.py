import spacy, argparse
from collections import Counter


def read_file(path_file):
    text_file = open(path_file, "r")
    text = text_file.read()
    return nlp(text)


def create_html(doc):
    list_words = []
    for tok in doc:
        if tok.pos_ == "PROPN" or tok.pos_ == "NUM":
            list_words.append(tok)

    c = Counter(list_words)
    body = f"""
        <html>
          <head>
            <meta charset="utf-8">
          </head>
            <table border="1">
              %s
            </table>
          </html>
        """
    full_str = ""
    for k,v in c.items():
        full_str += f'<tr><td>{k}</td><td>{v}</td></tr>'
    html = body % full_str
    with open("output.html", 'w') as file:
        file.write(html)


if __name__ == '__main__':
    parse_my = argparse.ArgumentParser(description='some tips')
    parse_my.add_argument('-inputFile', '--inputFile')
    args = parse_my.parse_args()
    path = args.inputFile
    if path:
        nlp = spacy.load("en_core_web_sm")
        doc = read_file(path)
        create_html(doc)
    else:
        print("need args -inputFile:\n Example -inputFile /home/myfile.txt")