  #name , kosher , type(1 = meat , 2 = dairy , 3 = vegan) , hour opening (morning 1 = 7:00 - 12:00 ,noon 2 = 12:00 - 16:00 ,night 3 = 16:00 - 21:00+ , 4 = all together) , palce , website link
restaurants = [["Moshbutz" , 2 , 1 ,  4  ,"ramot", "https://moshbutz.co.il/" ],
                ["bukrim restaurants" , 1 ,1 , 4 , "marom golan" , "https://www.meromgolantourism.co.il/restaurants"],
                ["Meatshos" , 1, 1 , 4 , " katzrin ", "https://www.meatshos.co.il/index.php?dir=site&page=content&cs=5024" ],
                ["Hanchatam" , 1, 2 , 4 , "bnei yehuda" , "https://www.hanahtom.com"],
                ["amiros" , 1, 2 , 4 , "shaal" , "https://www.rest.co.il/rest/80353867/" ],
                ["Machlabt Natur" , 1, 2 , 2 , "Natur" , "https://natur-cheese.co.il/"],
                ["Coffe anan" , 2, 2  ,  2  , "bantel mountain" , "https://tourgolan.org.il/listing/coffee_anan/"],
                ["Hahummusiya " , 2, 3 , 2 , "Ein Zivan" , "https://www.enzivan.co.il/%D7%94%D7%97%D7%95%D7%9E%D7%95%D7%A1%D7%99%D7%99%D7%94-%D7%A7%D7%99%D7%91%D7%95%D7%A5-%D7%A2%D7%99%D7%9F-%D7%96%D7%99%D7%95%D7%95%D7%9F" ],
                ["rak haumus " , 1, 3 , 2 , "katzrin" , "https://www.rakhummus.com/" ],
                ["Mamajda" , 1, 3 , 4 , "givat yoav" , "https://mamzda.business.site/"]]


kosher = int(input('kosher 1=yes 2=no:'))
type = int(input('type: milky=1 beef=2 vegan=3'))
opening_hours = int(input('choose opening hours: 1=morning 2=noon 3=evening 4=all the time: '))


def res_details(kosher ,type ,opening_hours):
    total_list = []
    for i in range(restaurants.__len__()):
         if kosher == restaurants[i][1] and type == restaurants[i][2] and opening_hours == restaurants[i][3]:
                total_list.append(restaurants[i])
                return total_list

print(res_details(kosher ,type ,opening_hours))
