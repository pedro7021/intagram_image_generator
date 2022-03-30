def urls():
    with open("urls.txt") as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content


if __name__ == "__main__":
    print(urls())
