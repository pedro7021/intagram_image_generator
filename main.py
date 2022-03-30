from scrap_text import scrap_text
from summarize_text import summarize_text
from create_images import create_images
from read_urls import urls
if __name__ == '__main__':
    index = 0
    for url in urls():
        index += 1
        try:
            print(f"Criando Imagens da Url Número {index}")
            create_images(summarize_text(scrap_text(url)))
        except Exception as e:
            print(f"Ocorreu um erro ao criar as Imagens da Url Número {index}")
            print(e)
