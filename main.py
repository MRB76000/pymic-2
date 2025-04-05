#hello world


from bs4 import BeautifulSoup
import urllib.request
import requests
import shutil
import os
from PIL import Image







def extractor(key, issue):
    pages = []
    issue = issue
    directory = r"/Users/mason/Library/CloudStorage/OneDrive-UniversityatBuffalo/comics" + key
    try:
        os.makedirs(r"/Users/mason/Library/CloudStorage/OneDrive-UniversityatBuffalo/comics/junk")
    except:
        None
    i = 1
    url = requests.get("https://comichubfree.com/" + key + "/issue-" + str(issue) + "/all").text
    soup = BeautifulSoup(url, 'html.parser')
    for page in soup.find_all("img", class_ = 'chapter_img lazyload'):
        start = (str(page).index("jpg")) - 2
        end  = (start - 4)
        number = ""
        if str(page)[start].isdigit():
            number = str(page)[start] + number
            if str(page)[start - 1].isdigit():
                number = str(page)[start-1] + number
                if str(page)[start - 2].isdigit():
                    number = str(page)[start-2] + number
        pages.append("page " + number + ".jpg")
        pageLink = page["data-src"]
        response = requests.get(pageLink, stream=True)
        if response.status_code == 200:
            with open("pages/page" + number + ".jpg", 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)


        
        
                
    


extractor("invincible", 63)






