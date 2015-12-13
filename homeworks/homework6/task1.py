import requests
from lxml import etree
import re


def uniq(input):
    output = []
    for i in input:
        if i not in output:
            output.append(i)
    return output


def wiki_urls(URL):
    data = requests.get(URL).text

    parser = etree.HTMLParser()
    tree = etree.fromstring(data, parser)
    urls = ""
    REG = []

    for element in tree.iter("div"):
        ea = list(dict.values(dict(element.attrib)))
        for i in range(len(ea)):
            if ea[i] == "content":
                div = etree.tostring(element, encoding="unicode", method="html")
                reg1 = re.findall("<a\s+(?:[^>]*?\s+)?href=\"([^\"]*)\"", div)
                for k in range(len(reg1)):
                    regp = re.findall("/wiki/", reg1[k])
                    regn = re.findall("/wiki/((Help)|(File)|(Wikipedia)|(Category)|(Portal)|(Template)|(Special))", reg1[k])
                    if regp and not regn:
                        if "#" in reg1[k]:
                            regc = re.findall("(.+)#", reg1[k])
                            REG.append(regc[0])
                        elif "//" not in reg1[k]:
                            REG.append(reg1[k])

    start_url = "https://en.wikipedia.org"

    if REG:
        UREG = uniq(REG)
        for i in range(len(UREG)):
            UREG[i] = start_url + UREG[i]
    else:
        UREG = []
    return(UREG)


def search_link_in_three_clicks(urlstart, urltarget):

    urls_list1 = wiki_urls(urlstart)
    found_path = ""
    
    #click 1
    for i in range(len(urls_list1)):
        if urls_list1[i] == urltarget:
            found_path = urlstart+"\n"+urls_list1[i]
            break
    #click2
    if not found_path:
        for i in range(len(urls_list1)):
            urls_list2 = wiki_urls(urls_list1[i])
            for k in range(len(urls_list2)):
                if urls_list2[k] == urltarget:
                    found_path = urlstart+"\n"+urls_list1[i]+"\n"+urls_list2[k]
                    break
    #click 3
    if not found_path:
        for i in range(len(urls_list1)):
            urls_list2 = wiki_urls(urls_list1[i])
            for k in range(len(urls_list2)):
                urls_list3 = wiki_urls(urls_list2[k])
                for j in range(len(urls_list3)):
                    if urls_list3[j] == URLTARGET:
                        found_path = URLSTART+"\n"+urls_list1[i]+"\n"+urls_list2[k]+"\n"+urls_list3[j]
                        break

    if found_path:
        return(found_path)
    else:
        return("Not Found in 3 clicks")


URLSTART = 'https://en.wikipedia.org/wiki/Gone_Maggie_Gone'
URLTARGET = 'https://en.wikipedia.org/wiki/Theia_(planet)'
result = search_link_in_three_clicks(URLSTART, URLTARGET)
print(result)
