

#https://www.footlocker.sg/en/homepage
#exec(open('footlocker.py').read())

import tagui as t

shoe = input("Enter shoe name : ")
t.init(visual_automation = True)
t.url('https://www.footlocker.sg/en/homepage')
t.type('//input[@id = "searchTerm_Header"]', shoe)
t.click('//button[@data-testid = "fl-search-box-button"]')
t.wait(3)
price = t.read('(//span[contains(@class,"fl-price--sale")])[1]')
name = t.read('(//span[@class="fl-product-tile--name"])[1]/span[@itemprop="name"]')
print(name , price)	


