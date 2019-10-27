import tagui as t


def get_shoe(shoe, gender, email):
    t.url("https://www.farfetch.com/sg/")
    details = []
    if gender == 'male':
        t.click('(//span[@class="tabs__span"])[.="Men"]')
        t.type('//input[@class="js-searchboxABTest force-ltr"]',
               shoe + " Shoes")
        t.click('//form[@class="ff-search"]/button')
        t.wait(3)
        count = t.count('(//li[@data-test="productCard"])')
        for i in range(1, min(count, 4)):
            name = t.read(
                f'(//li[@data-test="productCard"])[{i}]//div[@data-test="information"]/p')
            price = t.read(
                f'(//li[@data-test="productCard"])[{i}]//div[@data-test="information"]/div').replace('$', '')
            img = t.read(f'(//li[@data-test="productCard"])[{i}]//img/@src')
            details.append({"email": email, "name": name,
                            "price": price, "img": img, "Company": "FF"})
            print(f"name: {name}, price: {price} img_source = {img}")

    elif gender == 'female':
        t.click('(//span[@class="tabs__span"])[.="Women"]')
        t.type('//input[@class="js-searchboxABTest force-ltr"]',
               shoe + " Shoes")
        t.click('//form[@class="ff-search"]/button')
        t.wait(3)
        count = t.count('(//li[@data-test="productCard"])')
        for i in range(1, min(count, 4)):
            name = t.read(
                f'(//li[@data-test="productCard"])[{i}]//div[@data-test="information"]/p')
            price = t.read(
                f'(//li[@data-test="productCard"])[{i}]//div[@data-test="information"]/div').replace('$', '')
            img = t.read(f'(//li[@data-test="productCard"])[{i}]//img/@src')
            details.append({"email": email, "name": name,
                            "price": price, "img": img, "Company": "FF"})
            print(f"name: {name}, price: {price} img_source = {img}")
    else:
        t.type('//input[@class="js-searchboxABTest force-ltr"]',
               shoe + " Shoes")
        t.click('//form[@class="ff-search"]/button')
        t.wait(3)
        count = t.count('(//li[@data-test="productCard"])')
        for i in range(1, min(count, 4)):
            name = t.read(
                f'(//li[@data-test="productCard"])[{i}]//div[@data-test="information"]/p')
            price = t.read(
                f'(//li[@data-test="productCard"])[{i}]//div[@data-test="information"]/div').replace('$', '')
            img = t.read(f'(//li[@data-test="productCard"])[{i}]//img/@src')
            details.append({"email": email, "name": name,
                            "price": price, "img": img, "Company": "FF"})
            print(f"name: {name}, price: {price} img_source = {img}")
