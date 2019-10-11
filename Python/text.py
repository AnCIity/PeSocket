def joinList(p_items, p_text=", "):
    if p_items is not str:
        p_items = map(str, p_items)

    itemStr = ""
    for item in p_items:
        if itemStr is not "":
            itemStr = itemStr + p_text
        itemStr = itemStr + item

    return itemStr
def joinKeyValue(p_items, p_text="="):
    keys = p_items.keys()
    itemList = []
    for key in keys:
        itemText = key + p_text + p_items[key]
        itemList.append(itemText)
    return itemList#List