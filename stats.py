
def get_num_single(text):
    dic = {}
    for key in text:
        low = key.lower()
        if (low in dic) and (low.isalpha()):
            dic[low] += 1
        elif low not in dic and low.isalpha():
            dic[low] = 1
    return dic
        
    
def get_num_words(text):
     words = text.split()
     return words

def dics_list(dic):
    liste = []
    for key in dic:
        liste.append({"char": key, "num": dic[key]})
    liste.sort(reverse = True, key=sorting)
    return liste

def dic_einzel(liste):
    for eintrag in liste:
        print(f"{eintrag['char']}: {eintrag['num']}")
        
def sorting(liste):
    return liste["num"]