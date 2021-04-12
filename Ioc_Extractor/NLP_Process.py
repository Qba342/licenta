from nltk.tokenize import word_tokenize
import en_core_web_sm



nlp = en_core_web_sm.load()
all_stopwords = nlp.Defaults.stop_words



doc = 'European authorities fined Google a record $5.1 billion on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices'
#doc="ransoms demanded on google.com"

def removeStopwords(text:str):
    text_tokens = word_tokenize(text)
    tokens_without_sw = [word for word in text_tokens if not word in all_stopwords]
    str1 = " "
    return (str1.join(tokens_without_sw))

def NLPisValidIOC(sentence:str,ioc:str):
    malWords=['malicious','malware','ddos','phishing','threat','ransomware','ransom','ransoms']

    triggered=0

    doc=nlp(removeStopwords(sentence))
    for token in doc:
       # print(token.text, token.dep_, token.head.text, token.head.pos_,
         #       [child for child in token.children])

        for child in token.children:#parcurgem toti copii (vrem sa ajungem la toate radacinile)
            if str(child)==ioc:#orice ioc din lista...TODO
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
    return False








#print(NLPisValidIOC(doc,"google.com"))




