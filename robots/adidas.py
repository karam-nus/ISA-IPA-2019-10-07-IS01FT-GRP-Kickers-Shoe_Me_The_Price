#https://www.adidas.com.sg/
#exec(open('adidas.py').read())

import tagui as t

shoe = input("Enter shoe name")
t.init(visual_automation = True)
t.url('https://www.adidas.com.sg/')
t.type('//input[@data-auto-id = "searchinput"]', shoe)
### TO BE COMPLETED
t.click('//div[@class = "search-icon___izpuX"]')
t.click('//a[@class = "product-card__link-overlay"][contains(.,"LeBron")]')
price = t.read('(//div[@data-test="product-price"])[1]')
name = t.read('(//h1[@id = "pdp_product_title"])[1]')

print(name , price)