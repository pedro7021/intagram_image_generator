from imgmaker import imgmaker
from pathlib import Path


def create_first_image(title, length, maker, path):
    print("Criando Imagem Número 1")
    maker.generate("html/first_pic.html",
                   {"title": title,
                    "background": "backgrounds/first_pic.png",
                    "counter": f"1/{length}",
                    },
                   output_file=f"{path}\\1 carousel image.png",
                   width=1080,
                   height=1080, )


def create_intermediary_image(text, image_number, length, maker, path):
    print(f"Criando Imagem Número {image_number}")
    maker.generate("html/intermediary_pic.html",
                   {"text": text,
                    "background": "backgrounds/intermediary_pic.png",
                    "counter": f"{image_number}/{length}",
                    },
                   output_file=f"{path}\\{image_number} carousel image.png",

                   width=1080,
                   height=1080, )


def create_last_image(length, maker, path):
    print(f"Criando Imagem Número {length}")
    maker.generate("html/last_pic.html",
                   {"background": "backgrounds/last_pic.png",
                    "counter": f"{length}/{length}",
                    },
                   output_file=f"{path}\\{length} carousel image.png",

                   width=1080,
                   height=1080, )


def create_images(images):
    print("Criando Imagens")
    folder = images[0]
    remove = ["/", "\\", ":", '"', "<", ">", "|", "?"]
    for i in remove:
        folder = folder.replace(i, "")
    path = rf"C:\Users\pedro\Documents\Negócios\Organic\posts insta\{folder}"
    Path(path).mkdir(parents=True, exist_ok=True)

    maker = imgmaker()

    try:
        images_length = len(images)
        create_first_image(title=images[0],
                           length=images_length + 1,
                           maker=maker,
                           path=path)

        for i in range(images_length - 1):
            create_intermediary_image(text=images[i + 1],
                                      image_number=i + 2,
                                      length=images_length + 1,
                                      maker=maker,
                                      path=path)

        create_last_image(length=images_length + 1,
                          maker=maker,
                          path=path)
        print("Imagens Criadas Com Sucesso!!!")
    except Exception as e:
        print("Erro ao Criar Imagens")
        print(e)
    maker.close()


if __name__ == "__main__":
    maker = imgmaker()
    try:
        path = r"C:\Users\pedro\Documents\Negócios\Organic\posts insta"
        Path(path).mkdir(parents=True, exist_ok=True)

        create_first_image(
            title="A expressão Lorem ipsum em design gráfico e editoração é um texto padrão em latim utilizado na produção gráfica para preencher os espaços de texto em publicações para testar e ajustar aspectos visuais antes de utilizar conteúdo real.",
            # image_number=1,
            length=1,
            maker=maker,
            path=path)
    except Exception as e:
        print(e)
    maker.close()
