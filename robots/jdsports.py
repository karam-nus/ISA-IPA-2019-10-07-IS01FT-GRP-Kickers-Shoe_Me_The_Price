import tagui as t

url = "https://www.jdsports.com.sg"
closeLightbox_selector = ""
search_selector = '//input[@name="q"]'

search_query = "HOVR phantom" " men" "[enter]"
search_query = "apex" " men" "[enter]"

t.init()
t.url(url)
t.wait(3)
if t.present():
     
     t.type(search_selector, search_query)
count = t.count('//div[contains(@class," tile ")]//div[contains(@class,"name")]')
if count > 3: count = 3
for item in range(1, count + 1):
     name = t.read(f'//div[contains(@class," tile ")][{item}]//div[contains(@class,"name")]')
     cost = t.read(f'//div[contains(@class," tile ")][{item}]//div[contains(@class,"pricing")]')
     print(item, name, cost)
