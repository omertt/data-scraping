import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

data = {'Headline' : [], 'Author' : []}

""" 1
A request has been sent to the relevant website. The response received as a result of the request is assigned to the page variable.
"""

for i in range(1,27):
    url = "http://filelipota.com/category/yazilar/page/" + str(i) + "/"
    page = requests.get(url)

    """ 2
    With the HTML parser, the content of the page variable is parsed.
    """

    soup = BeautifulSoup(page.content,"html.parser")

    """ 3
    The block you want to get is in the "header-list-style" class. The desired block can be found by looking at the relevant html codes after right-click
    on that particular element and select the Inspect option. Then some string operations are done.
    """

    tempsoup = soup.findAll("div",{"class": "header-list-style"})
    tempsoup = str(tempsoup)
    pattern = 'href="http://filelipota.com(.*)</a><'
    result = re.findall(pattern,tempsoup)
    pattern2 = '/">(.*)'
    
    for i in range(0,len(result),2):
        headline = re.findall(pattern2,result[i])
        author = re.findall(pattern2,result[i+1])
        data['Headline'].append(headline[0])
        data['Author'].append(author[0])
        
df = pd.DataFrame(data)

