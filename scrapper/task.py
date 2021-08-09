from django.shortcuts import render, redirect
from selenium import webdriver
from django.http import JsonResponse
from selenium.webdriver.common.by import By
from django.db import transaction
import os
from .models import Article

# chrome_options = webdriver.ChromeOptions()
# chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--disable-dev-shm-usage")
# chrome_options.add_argument("--no-sandbox")

# option = webdriver.ChromeOptions()
# option.add_argument('headless')
# driver = webdriver.Chrome('path/to/chromedriver',options=option)

from selenium import webdriver  # for webdriver

# from selenium.webdriver.support.ui import WebDriverWait  # for implicit and explict waits
# from selenium.webdriver.chrome.options import Options  # for suppressing the browser


# driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
import chromedriver_binary  # Adds chromedriver binary to path
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from time import sleep
import pandas as DataFrame
from bs4 import BeautifulSoup as soup
import csv
import pandas as pd
import string
import json


from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.PhantomJS(executable_path=('C:\Users\folar\Downloads\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin')


def add(request):

    website = "https://www.readworks.org/"
    article_url = request.session.get("url")
    subheading = request.session.get("sub")
    n = int(request.session.get("char"))

    def crawler():
        # driver = webdriver.Chrome()
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(website)
        driver.find_element_by_class_name("log-in-button").click()
        driver.find_element_by_name("email").send_keys("xroydacute@yahoo.com")
        driver.find_element_by_name("password").send_keys("python")
        driver.find_element_by_class_name("submit").click()

        sleep(5)

        driver.get(article_url)

        sleep(2)
        url = driver.page_source
        return url

    url = crawler()
    soup1 = soup(url, "html.parser")

    def stringDivisor(n):
        passagescraped = soup1.find(
            "div", class_="vocab-popup-content-wrapper vocab-popup-enabled"
        )
        list = []
        p = passagescraped.find_all("p")
        for x in p:
            list.append(x.getText())
        listToStr = " ".join([str(elem) for elem in list])
        words = listToStr.split()
        subs = []

        for i in range(0, len(words), n):
            subs.append(" ".join(words[i : i + n]))
        return subs


    def PassageFrame(lst):
        columnsuffix = string.ascii_uppercase
        df = pd.DataFrame(
            lst, index=[f"Passage {j}" for _, j in list(zip(lst, columnsuffix))]
        ).T  # for Passage (alphabet)
        df = df.to_dict("list")
        #res_bytes = json.dumps(df).encode('utf-8')
        #db = Article(passage=res_bytes, Article_Title=subheading, url=article_url)
        #db.save()
        # df = pd.DataFrame(lst, index=[f'Passage {j}' for _, j in list(zip(lst, len(lst)))]).T  # for Passage (number)
        return df
    

    lst = stringDivisor(n)
    data = PassageFrame(lst)

    result = [data]
    return result
    
def json_result(request):
    result = add(request)    
    return JsonResponse(result, safe=False)


