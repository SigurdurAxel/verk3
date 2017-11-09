from bottle import run, route, static_file, error
import os
@route('/static/<skraarnafn>')
def static_skrar(skraarnafn):
    return static_file(skraarnafn, root='./static')

@route('/')
def index():
    return "<h1>Steve jobs er flottur</h1>" \
           "<a href='/sida/1'>siða 1</a><a href='/sida/2'>siða 2</a><a href='/sida/3'>siða 3</a>"\
           "<img src = '/static/stevejobs.jpeg'>" \
           "<head><link rel = 'stylesheet' href = '/static/still.css'></head>" \
           "<a href = '/verk2' class ='fart' > verkefni 2 </a>" \
           "<a href = '/undirsidu' class ='fart2' > undir síðu</a>"



@route('/sida/<nr>')
def sida1(nr):
    if nr == "1":
        return "<h1>Mario</h1>"\
                "<p>Long ago, during the classic era of console gaming in the eighties, came a title called Donkey Kong (1981), and I'm sure most of you will know what that is as the Donkey Kong series of games continues to this day. The aim of this game was for 'Jump Man' to rescue his girlfriend Pauline from the evil clutches of a large monkey named Donkey Kong</p>"\
                "<img src = '/static/mario.png'>"\
                "<head><link rel = 'stylesheet' href = '/static/still.css'></head>"
    elif nr == "2":
        return "<h1>Link</h1>"\
               "<p>Link (リンク Rinku?, Hylian LHylian IHylian NHylian K) is the main protagonist of the Legend of Zelda series. He is the everlasting hero of the setting, having appeared throughout the ages in a neverending line of incarnations. The various heroes who use the name of Link are courageous young boys or teenagers in green clothing who leave their homes to save the world from evil forces threatening it.</p>"\
               "<img src = '/static/ling.png'>" \
               "<head><link rel = 'stylesheet' href = '/static/still.css'></head>"


    elif nr == "3":
        return "<h1>Donkey Kong</h1>"\
               "<p>You know you remember Donkey Kong! Not the one from Donkey Kong Country though, but the old school Donkey Kong who kidnapped the princess and did battle with Mario. This is the remake of the original Donky Kong arcade game. You can only play the first board in this version of Donkey Kong, but it is fun nonetheless! You play the role as mario and you must navigate up the ladders to rescue the princess.</p>" \
               "<img src = '/static/DonkeyKong.png'>" \
               "<head><link rel = 'stylesheet' href = '/static/still.css'></head>"







@route('/verk2')
def verk2():
    return "<a href='verk2/1'><img src = '/static/stevejobs.jpeg'></a>" \
           "<a href='verk2/2'><img src = '/static/mario.png'></a>" \
           "<a href='verk2/3'><img src = '/static/ling.png'></a>" \
           "<a href='verk2/4'><img src = '/static/DonkeyKong.png'></a>" \
           "<a href='verk2/5'><img src = '/static/bill.jpg'></a>" \
           "<a href='verk2/6'><img src = '/static/ryu.png'></a>" \
           "<head><link rel = 'stylesheet' href = '/static/still2.css'></head>"
list = ("Þetta er Steve Jobs","Þetta er Mario","Þetta er link","Þetta er Donkey Kong","Þetta er Bill Gates","Þetta er Ryu")
@route('/verk2/<mynd>')
def verk2(mynd):
    if mynd == "1":
        return list[0]
    elif mynd == "2":
        return list[1]
    elif mynd == "3":
        return list[2]
    elif mynd == "4":
        return list[3]
    elif mynd == "5":
        return list[4]
    elif mynd == "6":
        return list[5]

@error(404)
def villa(error):
    return "Þessi síða er ekki til...."




run(host='0.0.0.0', port=os.environ.get('PORT'))