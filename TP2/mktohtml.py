import re

def linhas_iniciais(texto):

    match1 = re.match(r"#\s+(.+)", texto)
    match2 = re.match(r"##\s+(.+)", texto)
    match3 = re.match(r"###\s+(.+)", texto)

    if match1:
        print("<h1>"+match1.group(1)+"</h1>")
    elif match2:
        print("<h2>"+match2.group(1)+"</h2>")
    elif match3:
        print("<h3>"+match3.group(1)+"</h3>")
    else:
        print("Erro")

def bold(texto):
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>",texto)

def italico(texto):
    return re.sub(r"\*(.+?)\*", r"<i>\1</i>",texto)

def listas_numerada(texto):
    html = "<ol>\n"

    for linha in texto.split("\n"):
        match = re.match(r"\d+\.\s+(.+)", linha)
        if match:
            html += "<li>" + match.group(1) + "</li>\n"

    html += "</ol>"
    return html

def link(texto):
    return re.sub(r"\[(.+?)\]\((.+?)\)", r'<a href="\2">\1</a>', texto)

def imagem(texto):
    return re.sub(r"!\[(.+?)\]\((.+?)\)", r'<img src="\2" alt="\1"/>', texto)


