import tagui as t


def get_shoe(shoe, gender, email):
    t.init(visual_automation=True)
    t.url("https://www.farfetch.com/sg/")
    details = []
    if gender == ' men':
        t.click('(//span[@class="tabs__span"])[.="Men"]')
        t.type('//input[@class="js-searchboxABTest force-ltr"]',
               shoe + " Shoes")
        t.click('//form[@class="ff-search"]/button')
        t.wait(3)
        count = t.count('(//li[@data-test="productCard"])')
        if count!= 0:
            for i in range(1, min(count, 4)):
                name = t.read(
                    f'(//li[@data-test="productCard"])[{i}]//div[@data-test="information"]/p')
                price = t.read(
                    f'(//li[@data-test="productCard"])[{i}]//div[@data-test="information"]/div').replace('$', '')
                img = t.read(f'(//li[@data-test="productCard"])[{i}]//img/@src')
                link = "https://www.farfetch.com" + t.read(f'(//li[@data-test="productCard"])[{i}]/a/@href')
                details.append({"email": email, "name": name,
                                "price": price, "img": img, "Company": "Farfetch", "link" : link})
                print(f"name: {name}, price: {price} img_source = {img}")
        else:
            details.append({"email": email, "name": "NA",
                                "price": "NA", "img": "NA", "Company": "Farfetch", "link" : "NA"})

    elif gender == ' women':
        t.click('(//span[@class="tabs__span"])[.="Women"]')
        t.type('//input[@class="js-searchboxABTest force-ltr"]',
               shoe + " Shoes")
        t.click('//form[@class="ff-search"]/button')
        t.wait(3)
        count = t.count('(//li[@data-test="productCard"])')
        if count!= 0:
            for i in range(1, min(count, 4)):
                name = t.read(
                    f'(//li[@data-test="productCard"])[{i}]//div[@data-test="information"]/p')
                price = t.read(
                    f'(//li[@data-test="productCard"])[{i}]//div[@data-test="information"]/div').replace('$', '')
                img = t.read(f'(//li[@data-test="productCard"])[{i}]//img/@src')
                link = "https://www.farfetch.com" + t.read(f'(//li[@data-test="productCard"])[{i}]/a/@href')
                details.append({"email": email, "name": name,
                                "price": price, "img": img, "Company": "Farfetch", "link" : link})
                print(f"name: {name}, price: {price} img_source = {img}")
        else:
            details.append({"email": email, "name": "NA",
                                "price": "NA", "img": "NA", "Company": "Farfetch", "link" : "NA"})
    else:
        t.type('//input[@class="js-searchboxABTest force-ltr"]',
               shoe + " Shoes")
        t.click('//form[@class="ff-search"]/button')
        t.wait(3)
        count = t.count('(//li[@data-test="productCard"])')
        if count!= 0:
            for i in range(1, min(count, 4)):
                name = t.read(
                    f'(//li[@data-test="productCard"])[{i}]//div[@data-test="information"]/p')
                price = t.read(
                    f'(//li[@data-test="productCard"])[{i}]//div[@data-test="information"]/div').replace('$', '')
                img = t.read(f'(//li[@data-test="productCard"])[{i}]//img/@src')
                link = "https://www.farfetch.com" + t.read(f'(//li[@data-test="productCard"])[{i}]/a/@href')
                details.append({"email": email, "name": name,
                                "price": price, "img": img, "Company": "Farfetch", "link" : link})
                print(f"name: {name}, price: {price} img_source = {img}")
        else:
            details.append({"email": email, "name": "NA",
                                "price": "NA", "img": "NA", "Company": "Farfetch", "link" : "NA"})

    t.close()

    return details