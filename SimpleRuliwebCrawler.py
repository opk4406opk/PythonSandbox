import json, urllib, os, string, sys, re, threading
from bs4 import BeautifulSoup
# 루리웹 월페이퍼 게시판 이미지 크롤러  Simple 프로그램.

reload(sys)
sys.setdefaultencoding('utf-8')

class URLImgDownLoader(threading.Thread):
    def __init__(self, rootFolderName, fileName, imgTags):
        threading.Thread.__init__(self)
        self.rootFolderName = rootFolderName
        self.fileName = fileName
        self.imgTags = imgTags
    def run(self):
        fileIdx = 0
        for tag in self.imgTags:
            fixURL = string.replace(tag.contents[0]["src"], "img", "ori")
            urllib.urlretrieve(fixURL, self.rootFolderName + "/" + self.fileName + "__" + str(fileIdx) + ".jpg")
            fileIdx += 1



# json 파일로부터 url 추출.
print("extract from url list file(JSON)")
f = open("test.json", "r")
url_list = json.load(f)
f.close()
print("web pages extract success.")
# 각 웹페이지 url 로 부터 이미지들을 추출한다.
print("image download start.")
for url in url_list:
    htmlData = urllib.urlopen(url)
    htmlParser = BeautifulSoup(htmlData, 'html.parser')
    fixedTitle = re.sub("[^가-힣:a-z:A-Z:0-9]+", "_", str(htmlParser.title.string))
    os.mkdir(unicode(fixedTitle))
    try:
        worker = URLImgDownLoader(unicode(fixedTitle), unicode(fixedTitle), htmlParser.find_all("a", "img_load"))
        worker.start()
        # wait main thread.
        worker.join()
    except:
        print
    htmlData.close()

print("Finish all jobs.")