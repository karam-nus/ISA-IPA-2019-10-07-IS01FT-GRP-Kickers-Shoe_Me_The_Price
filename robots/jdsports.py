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
    final_command =  shoe_name + " shoes" + '[enter]'
    t.keyboard('[esc]')
    t.type('//input[@id = "srchInput"]', final_command )
    #t.click('//input[@id ="srchButton"]')
    t.wait(3)

    if g == ' men':
        if t.read('(//a[@data-e2e="plp-filterMenu-catItem"]/span)[contains(.,"Men")]'):
            t.click('(//a[@data-e2e="plp-filterMenu-catItem"]/span)[1]')
            count = t.count('//ul[@id="productListMain"]//li[@class="productListItem "]')
            t.wait(3)

            if count!= 0:
                for i in range(1, min(count, 4)):
                    price = t.read(f'(//span[@class="pri"])[{i}]')
                    name = t.read(f'(//span[@class="itemTitle"])[{i}]')
                    img = t.read(f'(//a[@class="itemImage"]/picture/img/@srcset)[{i}]')
                    link = "https://www.jdsports.com.sg" + t.read(f'(//span[@class = "itemTitle"])[{i}]/a/@href')
                    details.append({"email": email, "name": name,
                                    "price": price, "img": img, "Company": "JD", "link" : link})
            else:
                details.append({"email": email, "name": "NA",
                                    "price": "NA", "img": "NA", "Company": "JD", "link" : "NA"})

    elif g == ' women':
        if t.read('(//a[@data-e2e="plp-filterMenu-catItem"]/span)[contains(.,"Women")]'):
            t.click('(//a[@data-e2e="plp-filterMenu-catItem"]/span)[.="Women"]')
            count = t.count('//ul[@id="productListMain"]//li[@class="productListItem "]')
            t.wait(3)

            if count != 0:

                for i in range(1, min(count, 4)):
                    price = t.read(f'(//span[@class="pri"])[{i}]')
                    name = t.read(f'(//span[@class="itemTitle"])[{i}]')
                    img = t.read(f'(//a[@class="itemImage"]/picture/img/@srcset)[{i}]')
                    link = "https://www.jdsports.com.sg" + t.read(f'(//span[@class = "itemTitle"])[{i}]/a/@href')
                    details.append({"email": email, "name": name, "price": price,
                                    "img": img, "Company": "JD", "link" : link})
            else:
                details.append({"email": email, "name": "NA", "price": "NA",
                                    "img": "NA", "Company": "JD", "link" : "NA"})
    else:
        count = t.count('//ul[@id="productListMain"]//li[@class="productListItem "]')
        t.wait(3)
        if count != 0:

            for i in range(1, min(count, 4)):
                price = t.read(f'(//span[@class="pri"])[{i}]')
                name = t.read(f'(//span[@class="itemTitle"])[{i}]')
                img = t.read(f'(//a[@class="itemImage"]/picture/img/@srcset)[{i}]')
                link = "https://www.jdsports.com.sg" + t.read(f'(//span[@class = "itemTitle"])[{i}]/a/@href')
                details.append({"email": email, "name": name, "price": price,
                                "img": img, "Company": "JD", "link" : link})
        else:
            details.append({"email": email, "name": "NA", "price": "NA",
                                    "img": "NA", "Company": "JD", "link" : "NA"})
    #t.close()
    if len(details)==0:
        details.append({"email": email, "name": "NA", "price": "NA",
                        "img": "NA", "Company": "JD", "link": "NA"})
    print("JD BOT",details)
    return details
    # shoe_name,gender, email
