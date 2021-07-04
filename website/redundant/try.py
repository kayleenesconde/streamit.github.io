import csv
data = 'glee'
showname=''
showyear=0
showage =0
showimbd = 0
showrate = ''
showloc1=0
showloc2=0
showloc3=0
showloc4=0
showloc=''
show_exists= False
shows=[]
dat=[]
throw=[]
throw.append(["TITLE","YEAR","AGE","IMBD","RATINGS","LOCATION"])
print('')
print (" ")
print ("Searching...")
print (" ")
with open('tv_shows (1).csv', 'r', encoding="utf-8") as file:
    reader = csv.reader(file)
    for r in reader:
        shows.append(r)
for showinfo in shows:
    if (data.lower() in showinfo[0].lower()):
        show_exists= True
        showname=showinfo[0]
        showyear=showinfo[1]
        showage = showinfo[2]
        showimbd = showinfo[3]
        showrate = showinfo[4]
        showloc1= showinfo[5]
        showloc2= showinfo[6]
        showloc3=showinfo[7]
        showloc4=showinfo[8]
        if (int(showinfo[5])==1):
            showloc='Netflix'
        elif (int(showinfo[6])==1):
            showloc='Hulu'
        elif (int(showinfo[7])==1):
            showloc='Prime Video'
        elif (int(showinfo[8])==1):
            showloc='Disney+'
        dat.append(showname)
        dat.append(showyear)
        dat.append(showage)
        dat.append(showimbd)
        dat.append(showrate)
        dat.append(showloc)
        throw.append(dat)
        break
if (show_exists): 
    print(throw)
            #return render_template('correct.html', showname=showname, showyear=showyear)
else:
    print ('The show is not on Disney+.')
    print (throw)