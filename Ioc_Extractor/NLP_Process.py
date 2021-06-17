from nltk.tokenize import word_tokenize
import en_core_web_sm



nlp = en_core_web_sm.load()
all_stopwords = nlp.Defaults.stop_words
malWords = ['malicious', 'malware', 'ddos', 'phishing', 'threat', 'ransomware', 'ransom', 'ransoms']#TODO:de completat


def sentencesplit(text:str):
    doc=nlp(text)
    return [sent.string.strip() for sent in doc.sents]

def removeStopwords(text:str):
    text_tokens = word_tokenize(text)
    tokens_without_sw = [word for word in text_tokens if not word in all_stopwords]
    str1 = " "
    return (str1.join(tokens_without_sw))

def NLPisValidIOC(sentence:str,ioc:str):


    triggered=0

    doc=nlp(removeStopwords(sentence))
    for token in doc:
        #print(token.text, token.dep_, token.head.text, token.head.pos_,
         #       [child for child in token.children])

        for child in token.children:#parcurgem toti copii (vrem sa ajungem la toate radacinile)
            if str(child)==ioc:
                triggered=1
        if triggered==1:
            for child in token.children:
                for word in malWords:
                    if str(child).lower()==word:
                        return True
            if str(token)==ioc:
                for child in token.children:
                    for word in malWords:
                        if str(child).lower()==word:
                            return True
            if str(token) in malWords:
                for child in token.children:
                    if str(child).lower()==ioc:
                        return True
    return False







#doc="192.168.1.1 is not malicious"
#print(NLPisValidIOC(doc,"192.168.1.1"))




