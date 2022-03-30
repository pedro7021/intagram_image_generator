from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.luhn import LuhnSummarizer


def summarize_text(clean_content):
    print("Resumindo Texto")
    parser = PlaintextParser.from_string(clean_content["body"], Tokenizer("portuguese"))
    summarizer = LuhnSummarizer()
    summarized_content = summarizer(parser.document, 8)
    list_of_sentences = []
    for sentence in summarized_content:
        list_of_sentences.append(sentence)
    list_of_sentences.insert(0, clean_content["title"])
    print("Texto Resumido Com Sucesso!!")
    return list_of_sentences
