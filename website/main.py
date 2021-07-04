from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")

@app.route('/click', methods=['POST'])
def getvalue():
    if (request.method=='POST'):
        data=request.form['dshow']
        showname=''
        showyear= 0
        showage = ''
        showimbd = 0
        showrate = " "
        showloc1= 0
        showloc2= 0
        showloc3= 0
        showloc4= 0
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
                showloc1= showinfo[5]
                showloc2= showinfo[6]
                showloc3=showinfo[7]
                showloc4=showinfo[8]
                if ((showinfo[2])==''):
                    showage='18'
                elif ((showinfo[2])=='all'):
                    showage='7+'
                else:
                    showage=showinfo[2]
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
            if (showloc=='Netflix'):
                return render_template('netflix.html', showname=showname, showyear=showyear, showage=showage, showimbd=showimbd, showloc=showloc)
            elif (showloc=='Disney+'):
                return render_template('disney.html', showname=showname, showyear=showyear, showage=showage, showimbd=showimbd,showloc=showloc)
            elif (showloc=='Hulu'):
                return render_template('hulu.html', showname=showname, showyear=showyear, showage=showage, showimbd=showimbd,showloc=showloc)
            else:
                return render_template('amazon.html', showname=showname, showyear=showyear, showage=showage, showimbd=showimbd, showloc=showloc)
        else:
            return render_template ('none.html')

if __name__ == "__main__":
    app.run(debug=True)