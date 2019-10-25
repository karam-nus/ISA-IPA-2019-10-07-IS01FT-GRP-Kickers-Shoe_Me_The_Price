import tagui as t

url = "https://sg.puma.com"

t.init()
t.url(url)
t.click('//input[@id="search-submit"]')
t.type('(//input[@id="search-inputor"])[1]','Courts FF')
