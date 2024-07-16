#Priyanka M.
#07/16/2024
#Clickbait Headline Generator
#init
#functions
def celeb_headline():
    celeb=input("Enter a celebritie's name: ")
    return("Rumours Are Spreading That Justin Beiber Is Getting Divorced; Inside Sources Say That "+celeb+" Came in Between Him and His Wife.")
def gen_alpha_headline():
    object=input("Enter an Object: ")
    return("Due to Generation Alpha, "+object+" Quantities Are Running Extremely Low: What Experts Have to Say")
def city_headline():
    city=input("Enter a city name: ")
    number=input("Enter a number: ")
    return(number+" Things You Never Knew About "+city+"(Number "+number+" Will Shock You!)")
def space_headline():
    food=input("Please Enter a Food: ")
    planet=input("Please Enter a Planet Name: ")
    return("Astronauts are ASTONISHED! "+food+" Was Found On the Planet "+planet)
def politician_headline():
    politician=input("Please Enter the Name of a Politician: ")
    return("Why Did "+politician+" Eat a Breakfast Burrito in a Diaper? How This Can Affect Their Campaign.")
def clickbait():
    print(celeb_headline())
    print(gen_alpha_headline())
    print(city_headline())
    print(space_headline())
    print(politician_headline())



#main
while True:
    print("Welcome TO The Clickbait Headline Generator.")
    clickbait()
    ans=input("Would you like to generate more headlines? yes or no")
    if ans=="no":
        break
