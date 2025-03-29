def count_words(txt):
    return len(txt.split())

def count_chars(txt):
    txt = txt.lower()
    chars = {}
    for c in txt:
        if c not in chars.keys():
            chars[c] = 1
        else:
            chars[c] += 1
    return chars

def sort_dicts(chars):
    lst = []
    for key, val in chars.items():
        lst.append({'key' : key, 'val' : val})
    lst.sort(key=lambda x: x['val'], reverse=True)
    return lst