def ua_bot(t,search_query):
     url = "https://www.underarmour.com.sg"
     search_selector = '//input[@name="q"]'
     
     # search_query = "HOVR phantom" " men" "[enter]"
     # search_query= "apex" " men" "[enter]"
     search_query+= "[enter]"
     
     t.init()
     t.url(url)
     t.type(search_selector,search_query)
     count = t.count('//div[contains(@class," tile ")]//div[contains(@class,"name")]')
     if count>3: count = 3
     final_list = []
     for item in range(1,count+1):
          name = t.read(f'//div[contains(@class," tile ")][{item}]//div[contains(@class,"name")]')
          cost = t.read(f'//div[contains(@class," tile ")][{item}]//div[contains(@class,"pricing")]')
          final_list.append((name,cost))
          print(item,name,cost)
     t.close()
     return final_list