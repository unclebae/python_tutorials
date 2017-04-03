from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

# 페이지 내에서 발견한 링크를 리스트로 만든다
def getInternalLinks(bsObj, includeUrl) :
    internalLinks = []
    for link in bsObj.findAll("a", href=re.compile("^(|.*"+includeUrl+")")):
        if link.attrs['href'] is not None :
            if link.attrs['href'] not in internalLinks :
                internalLinks.append(link.attrs['href'])
    return internalLinks

# 페이지에서 발견한 외부 링크를 모두 목록으로 만든다.
def getExternalLinks(bsObj, excludeUrl) :
    externalLinks = []
    for link in bsObj.findAll("a", href=re.compile("^(http|www)((?!" + excludeUrl + ").)*$")) :
        if link.attrs['href'] is not None :
            if link.attrs['href'] not in externalLinks :
                externalLinks.append(link.attrs['href'])
    return externalLinks

def splitAddress(address) :
    addressParts = address.replace("http://", "").split("/")
    return addressParts

def getRandomExternalLink(startingPage) :
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html, "html.parser")
    externalLinks = getExternalLinks(bsObj, splitAddress(startingPage)[0])
    if len(externalLinks) == 0 :
        internalLinks = getInternalLinks(startingPage)
        return getExternalLinks(internalLinks[random.randint(0, len(externalLinks) - 1)])
    else :
        return externalLinks[random.randint(0, len(externalLinks) - 1)]

def followExternalOnly(startingSite) :
    externalLinks = getRandomExternalLink("https://apply.lh.or.kr/LH/index.html?gv_url=SIL::CLCC_SIL_0030.xfdl&gv_menuId=1010203&gv_param=LCC:Y,TAB_PAGE:3,UPP_AIS_TP_CD:06#MN::CLCC_MN_0010:")
    print("Random external link is : " + externalLinks)
    followExternalOnly(externalLinks)

followExternalOnly("https://apply.lh.or.kr/LH/index.html?gv_url=SIL::CLCC_SIL_0030.xfdl&gv_menuId=1010203&gv_param=LCC:Y,TAB_PAGE:3,UPP_AIS_TP_CD:06#MN::CLCC_MN_0010:")