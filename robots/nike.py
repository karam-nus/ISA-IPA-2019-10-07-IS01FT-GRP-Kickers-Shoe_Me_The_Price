#https://www.nike.com/sg/
#exec(open('nike.py').read())


def nike_bot(t,shoe_name):
     shoe = input("Enter shoe name")
     t.init()
     t.url('https://www.nike.com/sg/')
     t.type('//input[@id = "TypeaheadSearchInput"]', shoe)
     t.click('//button[@class = "btn-search z2 bg-transparent"]')
     t.click('//a[@class = "product-card__link-overlay"][contains(.,"Max")]')
     price = t.read('(//div[@data-test="product-price"])[1]')
     name = t.read('(//h1[@id = "pdp_product_title"])[1]')
     
     print(name , price)
     
     t.close()