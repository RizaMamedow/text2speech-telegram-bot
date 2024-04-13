def match_lang(text):
    is_en = not set('abcdefghijklmnopqrstuwxyz').isdisjoint(text.lower())

    return is_en