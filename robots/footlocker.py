

#https://www.footlocker.sg/en/homepage
#exec(open('footlocker.py').read())

import tagui as t

def get_shoe(shoe, g, email):
	gender = g
	t.init(visual_automation = True)
	t.url('https://www.footlocker.sg/en/homepage')
	t.type('//input[@id = "searchTerm_Header"]', shoe + " shoes")
	t.click('//button[@data-testid = "fl-search-box-button"]')
	t.wait(3)

	#### for men
	print(gender)
	if gender == " men":
		

		t.click('//a[@data-category-path = "men"]')
		t.wait(3)
		count = t.count('//span[@class="fl-product-tile--name"]/span[@itemprop="name"]')
		details = []
		if count!= 0:

			for i in range(0,min(count,3)):
				k = i+1
				price = t.read(f'(//span[contains(@class,"fl-price--sale")])[{k}]')
				name = t.read(f'(//span[@class="fl-product-tile--name"])[{k}]/span[@itemprop="name"]')
				img = t.read(f'(//picture[contains(@class, "fl-picture")]/img/@srcset)[{k+1}]')
				img = 'http:' + img
				link = t.read(f'(//div[@class = "fl-product-tile--basic"])[{k}]/a/@href')
				print(name , price, img)
				details.append({"email" : email,"name" : name, "price": price, "img": img,"Company" : "Footlocker", "link" : link})
		else:
			details.append({"email" : email,"name" : "NA", "price": "NA", "img": "NA","Company" : "Footlocker", "link" : "NA"})	

	else:
		t.click('//a[@data-category-path = "women"]')
		t.wait(3)
		count = t.count('//span[@class="fl-product-tile--name"]/span[@itemprop="name"]')
		details = []
		if count!= 0:

			for i in range(0,min(count,3)):
				k = i+1
				price = t.read(f'(//span[contains(@class,"fl-price--sale")])[{k}]')
				name = t.read(f'(//span[@class="fl-product-tile--name"])[{k}]/span[@itemprop="name"]')
				img = t.read(f'(//picture[contains(@class, "fl-picture")]/img/@srcset)[{k+1}]')
				img = 'http:' + img
				link = t.read(f'(//div[@class = "fl-product-tile--basic"])[{k}]/a/@href')
				print(name , price, img)
				details.append({"email" : email,"name" : name, "price": price, "img": img,"Company" : "Footlocker", "link" : link})
		else:
			details.append({"email" : email,"name" : "NA", "price": "NA", "img": "NA","Company" : "Footlocker", "link" : "NA"})
	#t.close()

	return details
