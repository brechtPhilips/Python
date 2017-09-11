#Please take a look at the following list:
# checklist = ["Portugal", "Germany", "Munster", "Spain"]
#One of the items is not a country.
# Please use Python and the file containing the list of countries (attached) as data source to filter out the checklist  of non-country items.
# Once you have filtered out checklist , then print it out.

checklist = ["Portugal", "Germany", "Munster", "Spain"]

with open("Files/countries-clean.txt",'r') as file:
    countries = file.readlines()
    countries = [ i.strip("\n") for i in countries]

for check in checklist:
    if  check not in countries:
        checklist.remove(check)

print(checklist)