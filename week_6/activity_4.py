# create the list of films
# create list w just ghostbusters in it

#input a film

# if in the list: print message
# if it is "Ghostbusters", extend gb list with fav films and print
# new_list = gblist.extend(fav_films)
#print new_list

#if not in list, append the list


fav_films = [
    "Jurassic Park",
    "Spiderman",
    "Shrek"
]

ghostbusters = [
    "Ghostbusters"
]

user_film = input("Type in a film   >   ").capitalize()

if user_film in fav_films:
    print("Yes, this is in the films list.")

elif user_film == "Ghostbusters":
    ghostbusters.extend(fav_films)
    print(ghostbusters)

else:
    fav_films.append(user_film)
    print(fav_films)

    






