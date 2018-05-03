from WebApp import functions


# list = functions.get_match_link_lists("https://www.iplt20.com/results")
list = []
with open("links.txt","r") as f:
    for line in f:
        list.append(line)
# with open("batmans.csv","w") as f:
#     f.write("")
#     f.close()
# with open("bowlers.csv","w") as f:
#     f.write("")
#     f.close()
for link in list:
    print(link)
    functions.get_scoreboards(link)