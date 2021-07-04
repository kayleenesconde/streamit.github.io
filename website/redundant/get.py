import csv

showname=" "
showyear=0
show_exists= False
shows=[]
dat=[]
throw=[]
throw.append(["TITLE","YEAR"])
print('')
show = "recess"
print (" ")
print ("Searching...")
print (" ")
with open('tvshows.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    for r in reader:
        shows.append(r)
for showinfo in shows:
    if (show.lower() in showinfo[0].lower()):
        show_exists= True
        showname=showinfo[0]
        showyear=showinfo[1]
        dat.append(showname)
        dat.append(showyear)
        throw.append(dat)
        break
if (show_exists):
    print ('exists')
    print(throw)
else:
    print ('The show is not on Disney+.')
