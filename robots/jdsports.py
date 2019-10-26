# shoe_name,gender, email
import tagui as t


def get_shoe(shoe_name, g, email):
    """
    Get shoe details from jdsports.com.sg
    :param shoe_name: name of the shoe to search for
    :param gender: gender of the subscriber
    :param email: email id of the subscriber
    :return: details, list of shoe details.
    """
    details = []
    t.init(visual_automation=True)
    t.url('https://www.jdsports.com.sg/')
    t.wait(5)
    final_command =  shoe_name + '[enter]'
    t.keyboard('[esc]')
    t.type('//input[@id = "srchInput"]', final_command )
    #t.click('//input[@id ="srchButton"]')
    t.wait(3)

    if g == 'male':
        if t.read('(//a[@data-e2e="plp-filterMenu-catItem"]/span)[contains(.,"Men")]'):
            t.click('(//a[@data-e2e="plp-filterMenu-catItem"]/span)[1]')
            count = t.count('//ul[@id="productListMain"]//li[@class="productListItem "]')
            t.wait(3)

            if count!= 0:
                for i in range(1, min(count, 4)):
                    price = t.read(f'(//span[@class="pri"])[{i}]')
                    name = t.read(f'(//span[@class="itemTitle"])[{i}]')
                    img = t.read(f'(//a[@class="itemImage"]/picture/img/@srcset)[{i}]')
                    details.append({"email": email, "name": name,
                                    "price": price, "img": img, "Company": "JDsports"})
            else:
                details.append({"email": email, "name": "NA",
                                    "price": "NA", "img": "NA", "Company": "JDsports"})

    elif g == 'female':
        if t.read('(//a[@data-e2e="plp-filterMenu-catItem"]/span)[contains(.,"Women")]'):
            t.click('(//a[@data-e2e="plp-filterMenu-catItem"]/span)[.="Women"]')
            count = t.count('//ul[@id="productListMain"]//li[@class="productListItem "]')
            t.wait(3)

            if count != 0:

                for i in range(1, min(count, 4)):
                    price = t.read(f'(//span[@class="pri"])[{i}]')
                    name = t.read(f'(//span[@class="itemTitle"])[{i}]')
                    img = t.read(f'(//a[@class="itemImage"]/picture/img/@srcset)[{i}]')
                    details.append({"email": email, "name": name, "price": price,
                                    "img": img, "Company": "JDsports"})
            else:
                details.append({"email": email, "name": "NA", "price": "NA",
                                    "img": "NA", "Company": "JDsports"})
    else:
        count = t.count('//ul[@id="productListMain"]//li[@class="productListItem "]')
        t.wait(3)
        if count != 0:

            for i in range(1, min(count, 4)):
                price = t.read(f'(//span[@class="pri"])[{i}]')
                name = t.read(f'(//span[@class="itemTitle"])[{i}]')
                img = t.read(f'(//a[@class="itemImage"]/picture/img/@srcset)[{i}]')
                details.append({"email": email, "name": name, "price": price,
                                "img": img, "Company": "JDsports"})
        else:
            details.append({"email": email, "name": "NA", "price": "NA",
                                    "img": "NA", "Company": "JDsports"})
    t.close()
    return details
    # shoe_name,gender, email
import tagui as t


def get_shoe_jd(shoe_name, gender, email):
    """
    Get shoe details from jdsports.com.sg
    :param shoe_name: name of the shoe to search for
    :param gender: gender of the subscriber
    :param email: email id of the subscriber
    :return: details, list of shoe details.
    """
    details = []
    t.init(visual_automation=True)
    t.url('https://www.jdsports.com.sg/')
    t.type('//input[@id = "srchInput"]', shoe_name + " shoes")
    t.click('//input[@id ="srchButton"]')
    t.wait(3)

    if gender == 'male':
        if t.read('(//a[@data-e2e="plp-filterMenu-catItem"]/span)[contains(.,"Men")]'):
            t.click('(//a[@data-e2e="plp-filterMenu-catItem"]/span)[1]')
            count = t.count('//ul[@id="productListMain"]//li[@class="productListItem "]')
            t.wait(3)
            for i in range(1, min(count, 4)):
                price = t.read(f'(//span[@class="pri"])[{i}]')
                name = t.read(f'(//span[@class="itemTitle"])[{i}]')
                img = t.read(f'(//a[@class="itemImage"]/picture/img/@srcset)[{i}]')
                details.append({"email": email, "name": name,
                                "price": price, "img": img, "Company": "JDsports"})
    elif gender == 'female':
        if t.read('(//a[@data-e2e="plp-filterMenu-catItem"]/span)[contains(.,"Women")]'):
            t.click('(//a[@data-e2e="plp-filterMenu-catItem"]/span)[.="Women"]')
            count = t.count('//ul[@id="productListMain"]//li[@class="productListItem "]')
            t.wait(3)
            for i in range(1, min(count, 4)):
                price = t.read(f'(//span[@class="pri"])[{i}]')
                name = t.read(f'(//span[@class="itemTitle"])[{i}]')
                img = t.read(f'(//a[@class="itemImage"]/picture/img/@srcset)[{i}]')
                details.append({"email": email, "name": name, "price": price,
                                "img": img, "Company": "JDsports"})
    else:
        count = t.count('//ul[@id="productListMain"]//li[@class="productListItem "]')
        t.wait(3)
        for i in range(1, min(count, 4)):
            price = t.read(f'(//span[@class="pri"])[{i}]')
            name = t.read(f'(//span[@class="itemTitle"])[{i}]')
            img = t.read(f'(//a[@class="itemImage"]/picture/img/@srcset)[{i}]')
            details.append({"email": email, "name": name, "price": price,
                            "img": img, "Company": "JDsports"})
    t.close()
    return details