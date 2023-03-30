restaurants = [["liz", True, 3, 2, 'givat yoav', ''],
               ["emma", 1.68, 2, 1],
               ["mom", 1.71, 1, 4],
               ["dad", 1.89, 2, 3]],
restaurants

kosher = int(input('kosher 1=yes 2=no:'))
type = int(input('type: milky=1 beef=2 vegan=3'))
opening_hours = int(input('choose opening hours: 1=morning 2=noon 3=evening 4=all the time: '))


def res_details(name ,kosher ,type ,opening_hours ,place ,website_link):
    for i in range(restaurants.__len__()):
         if kosher == restaurants[i][1] and type == restaurants[i][2] and opening_hours == restaurants[i][3]:
                rus = kosher, type, opening_hours
                return rus

print(res_details(name=restaurants , kosher=kosher, type=type, opening_hours=opening_hours, place=place, website_link=webstie_link))
# result = res_details(name ,kosher ,type ,opening_hours ,place ,website_link)

