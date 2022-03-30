from goose3 import Goose


def scrap_text(url):
    print("Coletando Dados")
    g = Goose()
    content = g.extract(url)
    print("Dados Coletados Com Sucesso!")
    return {
        "title": content.title,
        "body": content.cleaned_text
    }


if __name__ == '__main__':
    scrap_text("https://www.farmprogress.com/grapes/scientists-finding-new-life-wine-grape-residue")
