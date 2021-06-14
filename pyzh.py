from dragonmapper import transcriptions, hanzi

def list_get(l, i, default=None):
    try:
        return l[i]
    except IndexError:
        return default

def split(text, delim=' '):
    c_acc = ""
    delim_acc = ""
    char_unseen = True
    result_acc = []
    result_delims = []

    for c in text:
        if c in delim:
            delim_acc += c
            if c_acc != "":
                result_acc.append(c_acc)
                c_acc = ""
        else:
            c_acc += c
            if delim_acc != "":
                result_delims.append(delim_acc)
                delim_acc = ""
                if char_unseen:
                    result_acc.append("")
            char_unseen = False

    if c_acc != "" or delim_acc != "":
        result_acc.append(c_acc)
        result_delims.append(delim_acc)

    return list(filter(lambda e: e != ("",""), [(elem, list_get(result_delims, i, "")) for i,elem in enumerate(result_acc)]))


def convert(text):

    result = ""

    for segment,delim in split(text, " (){},"):
        if transcriptions.is_zhuyin(segment):
            result += transcriptions.to_pinyin(segment) + delim
        elif transcriptions.is_pinyin(segment):
            result += transcriptions.to_zhuyin(segment) + delim
        else:
            result += segment + delim

    return result

def annotate(text):

    result = ""

    for segment,delim in split(text):
        if hanzi.has_chinese(segment):
            result += f"{segment}({hanzi.to_pinyin(segment)} / {hanzi.to_zhuyin(segment)}){delim}"
        else:
            result += segment + delim

    return result
