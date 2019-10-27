#https://www.nike.com/sg/
#exec(open('nike.py').read())

import tagui as t

#shoe = input("Enter shoe name")
def get_shoe(shoe, g, email):
	gender = g
	# print('[nike]',gender)
	t.init(visual_automation = False)
	t.url('https://www.nike.com/sg/')
	t.type('//input[@id = "TypeaheadSearchInput"]', shoe + " shoes" + gender)
	t.click('//button[@class = "btn-search z2 bg-transparent"]')
	t.wait(3)
	count = t.count('//a[contains(@class , "product-card__link-overlay")]')
	# print('[nike]',count)
	details = []

	if count != 0:
		for i in range(0,min(count,3)):
			k = i+1
			name = t.read(f'(//a[@class = "product-card__link-overlay"])[{k}]')
			price = t.read(f'(//div[@data-test="product-price"])[{k}]')
			img = t.read(f'(//div[contains(@class, "product-card__hero")]/picture/img)[{k}]/@src')
			link = t.read(f'(//a[contains(@class,"product-card")])[{k}]/@href')
			# print('[nike]',name , price, img)
			details.append({"email" : email, "name" : name, "price": price, "img": img,"Company" : "Nike", "link": link})
	else:
		details.append({"email" : email, "name" : "NA", "price": "NA", "img": "NA","Company" : "Nike", "link": "NA"})

	t.close()
	return details