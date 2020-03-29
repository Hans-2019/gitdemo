# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 12:25:15 2019

@author: qiansihan
"""
from tkinter import *
import tkinter.messagebox as mes
import tkinter.simpledialog as sim
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['Simhei']
import webbrowser

root=Tk()
root.geometry('750x560')
root.title('文本编辑器')
mes.showinfo('Welcome','欢迎使用文本编辑器!')
Label(root,text='欢迎使用文本编辑器',fg='blue',font=50).place(x=300,y=30)
Label(root,text='文本输入',fg='green',font=30).place(x=10,y=80)
text1=Text(root,bd=3,fg='red')
text1.place(x=110,y=80)

filetext=open('english.txt','r')
lines=list(filetext.readlines())
line0=''.join(lines)
text1.insert(INSERT,line0)
wenben0=text1.get('1.0',INSERT)

textb=Text(root,width=80,height=2)
textb.insert(INSERT,"点击打开163邮件服务器首页(不信你试试( iwi ))--------------------")
textb.tag_add('link','1.2','1.12')
textb.tag_config('link',foreground='green',underline=True,background='pink')
def show_hand_cursor(event):
    textb.config(cursor='arrow')
def click(event):
    webbrowser.open('https://mail.163.com/')
def show_arrow_cursor(event):
    textb.config(cursor='xterm')
textb.tag_bind('link','<Enter>',show_hand_cursor)
textb.tag_bind('link','<Button-1>',click)
textb.tag_bind('link','<Leave>',show_arrow_cursor)
textb.place(x=110,y=460)

wenben=wenben0.lower()
wenben1=[] #所有的words
wenben2=[] #不重复的words
wenben3=[] #除去停词的不重复的words
cishu1=[] #wenben3中每个word的次数
a=''
b=''
for i in wenben:
    if i not in [',','.','/','?','\'','\"',';',':','[',']','{','}','!','`','~','#','(',')','*']:
             wenben1.append(i)
for i in wenben1:
    a=a+i
wenben1=a.split()
for i in wenben1:
    if i not in wenben2:
        wenben2.append(i)
for i in wenben2:
    if i not in ["d","ll","m","re","s","t","ve","ZT","ZZ","a","as","able","about","above","abst","accordance","according","accordingly","across","act","actually","added","adj","adopted","affected","affecting","affects","after","afterwards","again","against","ah","aint","all","allow","allows","almost","alone","along","already","also","although","always","am","among","amongst","an","and","announce","another","any","anybody","anyhow","anymore","anyone","anything","anyway","anyways","anywhere","apart","apparently","appear","appreciate","appropriate","approximately","are","area","areas","aren","arent","arent","arise","around","as","aside","ask","asked","asking","asks","associated","at","auth","available","away","awfully","b","back","backed","backing","backs","be","became","because","become","becomes","becoming","been","before","beforehand","began","begin","beginning","beginnings","begins","behind","being","beings","believe","below","beside","besides","best","better","between","beyond","big","biol","both","brief","briefly","but","by","c","cmon","cs","ca","came","can","cant","cannot","cant","case","cases","cause","causes","certain","certainly","changes","clear","clearly","co","com","come","comes","concerning","consequently","consider","considering","contain","containing","contains","corresponding","could","couldnt","couldnt","course","currently","d","date","definitely","describe","described","despite","did","didnt","differ","different","differently","discuss","do","does","doesnt","doing","dont","done","down","downed","downing","downs","downwards","due","during","e","each","early","ed","edu","effect","eg","eight","eighty","either","else","elsewhere","end","ended","ending","ends","enough","entirely","especially","et","et-al","etc","even","evenly","ever","every","everybody","everyone","everything","everywhere","ex","exactly","example","except","f","face","faces","fact","facts","far","felt","few","ff","fifth","find","finds","first","five","fix","followed","following","follows","for","former","formerly","forth","found","four","from","full","fully","further","furthered","furthering","furthermore","furthers","g","gave","general","generally","get","gets","getting","give","given","gives","giving","go","goes","going","gone","good","goods","got","gotten","great","greater","greatest","greetings","group","grouped","grouping","groups","h","had","hadnt","happens","hardly","has","hasnt","have","havent","having","he","hes","hed","hello","help","hence","her","here","heres","hereafter","hereby","herein","heres","hereupon","hers","herself","hes","hi","hid","high","higher","highest","him","himself","his","hither","home","hopefully","how","howbeit","however","hundred","i","id","ill","im","ive","id","ie","if","ignored","im","immediate","immediately","importance","important","in","inasmuch","inc","include","indeed","index","indicate","indicated","indicates","information","inner","insofar","instead","interest","interested","interesting","interests","into","invention","inward","is","isnt","it","itd","itll","its","itd","its","itself","j","just","k","keep","keeps","kept","keys","kg","kind","km","knew","know","known","knows","l","large","largely","last","lately","later","latest","latter","latterly","least","less","lest","let","lets","lets","like","liked","likely","line","little","long","longer","longest","look","looking","looks","ltd","m","made","mainly","make","makes","making","man","many","may","maybe","me","mean","means","meantime","meanwhile","member","members","men","merely","mg","might","million","miss","ml","more","moreover","most","mostly","mr","mrs","much","mug","must","my","myself","n","nt","na","name","namely","nay","nd","near","nearly","necessarily","necessary","need","needed","needing","needs","neither","never","nevertheless","new","newer","newest","next","nine","ninety","no","nobody","non","none","nonetheless","noone","nor","normally","nos","not","noted","nothing","novel","now","nowhere","number","numbers","o","obtain","obtained","obviously","of","off","often","oh","ok","okay","old","older","oldest","omitted","on","once","one","ones","only","onto","open","opened","opening","opens","or","ord","order","ordered","ordering","orders","other","others","otherwise","ought","our","ours","ourselves","out","outside","over","overall","owing","own","p","page","pages","part","parted","particular","particularly","parting","parts","past","per","perhaps","place","placed","places","please","plus","point","pointed","pointing","points","poorly","possible","possibly","potentially","pp","predominantly","present","presented","presenting","presents","presumably","previously","primarily","probably","problem","problems","promptly","proud","provides","put","puts","q","que","quickly","quite","qv","r","ran","rather","rd","re","readily","really","reasonably","recent","recently","ref","refs","regarding","regardless","regards","related","relatively","research","respectively","resulted","resulting","results","right","room","rooms","run","s","said","same","saw","say","saying","says","sec","second","secondly","seconds","section","see","seeing","seem","seemed","seeming","seems","seen","sees","self","selves","sensible","sent","serious","seriously","seven","several","shall","she","shell","shed","shes","should","shouldnt","show","showed","showing","shown","showns","shows","side","sides","significant","significantly","similar","similarly","since","six","slightly","small","smaller","smallest","so","some","somebody","somehow","someone","somethan","something","sometime","sometimes","somewhat","somewhere","soon","sorry","specifically","specified","specify","specifying","state","states","still","stop","strongly","sub","substantially","successfully","such","sufficiently","suggest","sup","sure","t","ts","take","taken","taking","tell","tends","th","than","thank","thanks","thanx","that","thatll","thats","thatve","thats","the","their","theirs","them","themselves","then","thence","there","therell","theres","thereve","thereafter","thereby","thered","therefore","therein","thereof","therere","theres","thereto","thereupon","these","they","theyd","theyll","theyre","theyve","theyd","theyre","thing","things","think","thinks","third","this","thorough","thoroughly","those","thou","though","thoughh","thought","thoughts","thousand","three","throug","through","throughout","thru","thus","til","tip","to","today","together","too","took","toward","towards","tried","tries","truly","try","trying","ts","turn","turned","turning","turns","twice","two","u","un","under","unfortunately","unless","unlike","unlikely","until","unto","up","upon","ups","us","use","used","useful","usefully","usefulness","uses","using","usually","uucp","v","value","various","very","via","viz","vol","vols","vs","w","want","wanted","wanting","wants","was","wasnt","way","ways","we","wed","well","were","weve","wed","welcome","well","wells","went","were","werent","what","whatll","whats","whatever","whats","when","whence","whenever","where","wheres","whereafter","whereas","whereby","wherein","wheres","whereupon","wherever","whether","which","while","whim","whither","who","wholl","whos","whod","whoever","whole","whom","whomever","whos","whose","why","widely","will","willing","wish","with","within","without","wont","wonder","words","work","worked","working","works","world","would","wouldnt","www","x","y","year","years","yes","yet","you","youd","youll","youre","youve","youd","young","younger","youngest","your","youre","yours","yourself","yourselves","z","zero","zt","zz"]:
        wenben3.append(i)
for i in wenben3:
    k=wenben1.count(i)
    cishu1.append(k)

def guanjianci(wenben11,cishu11):
    wenben111=[]
    for i in wenben11:
        wenben111.append(i)
    cishu111=[]
    for j in cishu11:
        cishu111.append(j)
    
    gjc={}
    a=max(cishu111)
    b=cishu111.index(a)
    gjc[wenben111[b]]=a
    cishu111.remove(a)
    wenben111.remove(wenben111[b])
    a=max(cishu111)
    b=cishu111.index(a)
    gjc[wenben111[b]]=a
    cishu111.remove(a)
    wenben111.remove(wenben111[b]) 
    a=max(cishu111)
    b=cishu111.index(a)
    gjc[wenben111[b]]=a
    cishu111.remove(a)
    wenben111.remove(wenben111[b])
    a=max(cishu111)
    b=cishu111.index(a)
    gjc[wenben111[b]]=a
    cishu111.remove(a)
    wenben111.remove(wenben111[b])    
    a=max(cishu111)
    b=cishu111.index(a)
    gjc[wenben111[b]]=a
    cishu111.remove(a)
    wenben111.remove(wenben111[b])
    a=max(cishu111)
    b=cishu111.index(a)
    gjc[wenben111[b]]=a
    return gjc

def gjc_print(gjc):
    a=list(gjc.keys())
    for i in a:
        print(i,end=' ')
    print('')
def gjccishu_print(gjc):
    a=list(gjc.keys())
    for i in a:
        print(str(i)+':'+str(gjc[i])+'次')
def gjchuitu(gjc):
    x=list(gjc.keys())
    y=[]
    for i in x:
        y.append(gjc[i])
    import matplotlib.pyplot as plt
    from pylab import mpl
    mpl.rcParams['font.sans-serif']=['SimHei']
    plt.bar(x,y,width=0.45,label='关键词分布')
    plt.ylabel('次数')
    plt.xlabel('关键词')
    plt.title('关键词表')
    plt.legend()
    plt.show()
  
def xianshiwenben():
    print(wenben0)
def dancichaijie():
    for i in wenben1:
        print(i)
def dancihebing():
    zzz=' '.join(wenben1)
    print(zzz)
def dancishuliangtongji():
    print('单词总数：'+str(len(wenben1))+'词')
def dancizhongleitongji():
    print('单词种类：'+str(len(wenben2))+'种')
def cipingtongji():
    for i in wenben2:
        k=wenben1.count(i)
        print(i+':'+str(k)+'次')
def guanjiancishengcheng():
    gjc_print(guanjianci(wenben3,cishu1))
def guanjianciciping():
    gjccishu_print(guanjianci(wenben3,cishu1))
def guanjiancizhuzhuangtu():
    gjchuitu(guanjianci(wenben3,cishu1))
def chazhaodanci():
    res1=sim.askstring('查找单词','请输入需要查找的单词')
    if res1 not in wenben1:
        mes.showwarning('错误','您查找的单词不存在')
    else:
        aaaa=wenben1.count(res1)
        print('文本中'+res1+'出现了'+str(aaaa)+'次。')
    
def log_in():
    if text1.get(1.0,INSERT)=='':
        mes.showwarning('错误','请输入文本')
    else:
        mes.showinfo('输入成功','可进行编辑')
        root.destroy()
        new_window()

def shanchudanci():
    wenben156=[]
    res1=sim.askstring('删除单词','请输入需要删除的单词')
    if res1 not in wenben1:
        mes.showwarning('错误','您删除的单词不存在')
    else:
        for i in wenben1:
            if i !=res1:
                wenben156.append(i)
        for i in range(len(wenben1)):
            wenben1.pop()
        for i in range(len(wenben2)):
            wenben2.pop()
        for i in range(len(wenben3)):
            wenben3.pop()
        for i in range(len(cishu1)):
            cishu1.pop()

        for i in wenben156:
            wenben1.append(i)
        for i in wenben1:
            if i not in wenben2:
                wenben2.append(i)
            
        for i in wenben2:
            if i not in ["d","ll","m","re","s","t","ve","ZT","ZZ","a","as","able","about","above","abst","accordance","according","accordingly","across","act","actually","added","adj","adopted","affected","affecting","affects","after","afterwards","again","against","ah","aint","all","allow","allows","almost","alone","along","already","also","although","always","am","among","amongst","an","and","announce","another","any","anybody","anyhow","anymore","anyone","anything","anyway","anyways","anywhere","apart","apparently","appear","appreciate","appropriate","approximately","are","area","areas","aren","arent","arent","arise","around","as","aside","ask","asked","asking","asks","associated","at","auth","available","away","awfully","b","back","backed","backing","backs","be","became","because","become","becomes","becoming","been","before","beforehand","began","begin","beginning","beginnings","begins","behind","being","beings","believe","below","beside","besides","best","better","between","beyond","big","biol","both","brief","briefly","but","by","c","cmon","cs","ca","came","can","cant","cannot","cant","case","cases","cause","causes","certain","certainly","changes","clear","clearly","co","com","come","comes","concerning","consequently","consider","considering","contain","containing","contains","corresponding","could","couldnt","couldnt","course","currently","d","date","definitely","describe","described","despite","did","didnt","differ","different","differently","discuss","do","does","doesnt","doing","dont","done","down","downed","downing","downs","downwards","due","during","e","each","early","ed","edu","effect","eg","eight","eighty","either","else","elsewhere","end","ended","ending","ends","enough","entirely","especially","et","et-al","etc","even","evenly","ever","every","everybody","everyone","everything","everywhere","ex","exactly","example","except","f","face","faces","fact","facts","far","felt","few","ff","fifth","find","finds","first","five","fix","followed","following","follows","for","former","formerly","forth","found","four","from","full","fully","further","furthered","furthering","furthermore","furthers","g","gave","general","generally","get","gets","getting","give","given","gives","giving","go","goes","going","gone","good","goods","got","gotten","great","greater","greatest","greetings","group","grouped","grouping","groups","h","had","hadnt","happens","hardly","has","hasnt","have","havent","having","he","hes","hed","hello","help","hence","her","here","heres","hereafter","hereby","herein","heres","hereupon","hers","herself","hes","hi","hid","high","higher","highest","him","himself","his","hither","home","hopefully","how","howbeit","however","hundred","i","id","ill","im","ive","id","ie","if","ignored","im","immediate","immediately","importance","important","in","inasmuch","inc","include","indeed","index","indicate","indicated","indicates","information","inner","insofar","instead","interest","interested","interesting","interests","into","invention","inward","is","isnt","it","itd","itll","its","itd","its","itself","j","just","k","keep","keeps","kept","keys","kg","kind","km","knew","know","known","knows","l","large","largely","last","lately","later","latest","latter","latterly","least","less","lest","let","lets","lets","like","liked","likely","line","little","long","longer","longest","look","looking","looks","ltd","m","made","mainly","make","makes","making","man","many","may","maybe","me","mean","means","meantime","meanwhile","member","members","men","merely","mg","might","million","miss","ml","more","moreover","most","mostly","mr","mrs","much","mug","must","my","myself","n","nt","na","name","namely","nay","nd","near","nearly","necessarily","necessary","need","needed","needing","needs","neither","never","nevertheless","new","newer","newest","next","nine","ninety","no","nobody","non","none","nonetheless","noone","nor","normally","nos","not","noted","nothing","novel","now","nowhere","number","numbers","o","obtain","obtained","obviously","of","off","often","oh","ok","okay","old","older","oldest","omitted","on","once","one","ones","only","onto","open","opened","opening","opens","or","ord","order","ordered","ordering","orders","other","others","otherwise","ought","our","ours","ourselves","out","outside","over","overall","owing","own","p","page","pages","part","parted","particular","particularly","parting","parts","past","per","perhaps","place","placed","places","please","plus","point","pointed","pointing","points","poorly","possible","possibly","potentially","pp","predominantly","present","presented","presenting","presents","presumably","previously","primarily","probably","problem","problems","promptly","proud","provides","put","puts","q","que","quickly","quite","qv","r","ran","rather","rd","re","readily","really","reasonably","recent","recently","ref","refs","regarding","regardless","regards","related","relatively","research","respectively","resulted","resulting","results","right","room","rooms","run","s","said","same","saw","say","saying","says","sec","second","secondly","seconds","section","see","seeing","seem","seemed","seeming","seems","seen","sees","self","selves","sensible","sent","serious","seriously","seven","several","shall","she","shell","shed","shes","should","shouldnt","show","showed","showing","shown","showns","shows","side","sides","significant","significantly","similar","similarly","since","six","slightly","small","smaller","smallest","so","some","somebody","somehow","someone","somethan","something","sometime","sometimes","somewhat","somewhere","soon","sorry","specifically","specified","specify","specifying","state","states","still","stop","strongly","sub","substantially","successfully","such","sufficiently","suggest","sup","sure","t","ts","take","taken","taking","tell","tends","th","than","thank","thanks","thanx","that","thatll","thats","thatve","thats","the","their","theirs","them","themselves","then","thence","there","therell","theres","thereve","thereafter","thereby","thered","therefore","therein","thereof","therere","theres","thereto","thereupon","these","they","theyd","theyll","theyre","theyve","theyd","theyre","thing","things","think","thinks","third","this","thorough","thoroughly","those","thou","though","thoughh","thought","thoughts","thousand","three","throug","through","throughout","thru","thus","til","tip","to","today","together","too","took","toward","towards","tried","tries","truly","try","trying","ts","turn","turned","turning","turns","twice","two","u","un","under","unfortunately","unless","unlike","unlikely","until","unto","up","upon","ups","us","use","used","useful","usefully","usefulness","uses","using","usually","uucp","v","value","various","very","via","viz","vol","vols","vs","w","want","wanted","wanting","wants","was","wasnt","way","ways","we","wed","well","were","weve","wed","welcome","well","wells","went","were","werent","what","whatll","whats","whatever","whats","when","whence","whenever","where","wheres","whereafter","whereas","whereby","wherein","wheres","whereupon","wherever","whether","which","while","whim","whither","who","wholl","whos","whod","whoever","whole","whom","whomever","whos","whose","why","widely","will","willing","wish","with","within","without","wont","wonder","words","work","worked","working","works","world","would","wouldnt","www","x","y","year","years","yes","yet","you","youd","youll","youre","youve","youd","young","younger","youngest","your","youre","yours","yourself","yourselves","z","zero","zt","zz"]:
                wenben3.append(i)
        for i in wenben3:
            k=wenben1.count(i)
            cishu1.append(k)
        hhhhhh=' '.join(wenben1)
        print(hhhhhh)

def tihuandanci():
    wenben156=[]
    res1=sim.askstring('替换前单词','请输入需要替换的单词')
    if res1 not in wenben1:
        mes.showwarning('错误','您替换的单词不存在')
    else:
        res2=sim.askstring('替换后单词','请输入需要替换后的单词')
        for i in wenben1:
            if i !=res1:
                wenben156.append(i)
            else:
                wenben156.append(res2)
        for i in range(len(wenben1)):
            wenben1.pop()
        for i in range(len(wenben2)):
            wenben2.pop()
        for i in range(len(wenben3)):
            wenben3.pop()
        for i in range(len(cishu1)):
            cishu1.pop()

        for i in wenben156:
            wenben1.append(i)
        for i in wenben1:
            if i not in wenben2:
                wenben2.append(i)
            
        for i in wenben2:
            if i not in ["d","ll","m","re","s","t","ve","ZT","ZZ","a","as","able","about","above","abst","accordance","according","accordingly","across","act","actually","added","adj","adopted","affected","affecting","affects","after","afterwards","again","against","ah","aint","all","allow","allows","almost","alone","along","already","also","although","always","am","among","amongst","an","and","announce","another","any","anybody","anyhow","anymore","anyone","anything","anyway","anyways","anywhere","apart","apparently","appear","appreciate","appropriate","approximately","are","area","areas","aren","arent","arent","arise","around","as","aside","ask","asked","asking","asks","associated","at","auth","available","away","awfully","b","back","backed","backing","backs","be","became","because","become","becomes","becoming","been","before","beforehand","began","begin","beginning","beginnings","begins","behind","being","beings","believe","below","beside","besides","best","better","between","beyond","big","biol","both","brief","briefly","but","by","c","cmon","cs","ca","came","can","cant","cannot","cant","case","cases","cause","causes","certain","certainly","changes","clear","clearly","co","com","come","comes","concerning","consequently","consider","considering","contain","containing","contains","corresponding","could","couldnt","couldnt","course","currently","d","date","definitely","describe","described","despite","did","didnt","differ","different","differently","discuss","do","does","doesnt","doing","dont","done","down","downed","downing","downs","downwards","due","during","e","each","early","ed","edu","effect","eg","eight","eighty","either","else","elsewhere","end","ended","ending","ends","enough","entirely","especially","et","et-al","etc","even","evenly","ever","every","everybody","everyone","everything","everywhere","ex","exactly","example","except","f","face","faces","fact","facts","far","felt","few","ff","fifth","find","finds","first","five","fix","followed","following","follows","for","former","formerly","forth","found","four","from","full","fully","further","furthered","furthering","furthermore","furthers","g","gave","general","generally","get","gets","getting","give","given","gives","giving","go","goes","going","gone","good","goods","got","gotten","great","greater","greatest","greetings","group","grouped","grouping","groups","h","had","hadnt","happens","hardly","has","hasnt","have","havent","having","he","hes","hed","hello","help","hence","her","here","heres","hereafter","hereby","herein","heres","hereupon","hers","herself","hes","hi","hid","high","higher","highest","him","himself","his","hither","home","hopefully","how","howbeit","however","hundred","i","id","ill","im","ive","id","ie","if","ignored","im","immediate","immediately","importance","important","in","inasmuch","inc","include","indeed","index","indicate","indicated","indicates","information","inner","insofar","instead","interest","interested","interesting","interests","into","invention","inward","is","isnt","it","itd","itll","its","itd","its","itself","j","just","k","keep","keeps","kept","keys","kg","kind","km","knew","know","known","knows","l","large","largely","last","lately","later","latest","latter","latterly","least","less","lest","let","lets","lets","like","liked","likely","line","little","long","longer","longest","look","looking","looks","ltd","m","made","mainly","make","makes","making","man","many","may","maybe","me","mean","means","meantime","meanwhile","member","members","men","merely","mg","might","million","miss","ml","more","moreover","most","mostly","mr","mrs","much","mug","must","my","myself","n","nt","na","name","namely","nay","nd","near","nearly","necessarily","necessary","need","needed","needing","needs","neither","never","nevertheless","new","newer","newest","next","nine","ninety","no","nobody","non","none","nonetheless","noone","nor","normally","nos","not","noted","nothing","novel","now","nowhere","number","numbers","o","obtain","obtained","obviously","of","off","often","oh","ok","okay","old","older","oldest","omitted","on","once","one","ones","only","onto","open","opened","opening","opens","or","ord","order","ordered","ordering","orders","other","others","otherwise","ought","our","ours","ourselves","out","outside","over","overall","owing","own","p","page","pages","part","parted","particular","particularly","parting","parts","past","per","perhaps","place","placed","places","please","plus","point","pointed","pointing","points","poorly","possible","possibly","potentially","pp","predominantly","present","presented","presenting","presents","presumably","previously","primarily","probably","problem","problems","promptly","proud","provides","put","puts","q","que","quickly","quite","qv","r","ran","rather","rd","re","readily","really","reasonably","recent","recently","ref","refs","regarding","regardless","regards","related","relatively","research","respectively","resulted","resulting","results","right","room","rooms","run","s","said","same","saw","say","saying","says","sec","second","secondly","seconds","section","see","seeing","seem","seemed","seeming","seems","seen","sees","self","selves","sensible","sent","serious","seriously","seven","several","shall","she","shell","shed","shes","should","shouldnt","show","showed","showing","shown","showns","shows","side","sides","significant","significantly","similar","similarly","since","six","slightly","small","smaller","smallest","so","some","somebody","somehow","someone","somethan","something","sometime","sometimes","somewhat","somewhere","soon","sorry","specifically","specified","specify","specifying","state","states","still","stop","strongly","sub","substantially","successfully","such","sufficiently","suggest","sup","sure","t","ts","take","taken","taking","tell","tends","th","than","thank","thanks","thanx","that","thatll","thats","thatve","thats","the","their","theirs","them","themselves","then","thence","there","therell","theres","thereve","thereafter","thereby","thered","therefore","therein","thereof","therere","theres","thereto","thereupon","these","they","theyd","theyll","theyre","theyve","theyd","theyre","thing","things","think","thinks","third","this","thorough","thoroughly","those","thou","though","thoughh","thought","thoughts","thousand","three","throug","through","throughout","thru","thus","til","tip","to","today","together","too","took","toward","towards","tried","tries","truly","try","trying","ts","turn","turned","turning","turns","twice","two","u","un","under","unfortunately","unless","unlike","unlikely","until","unto","up","upon","ups","us","use","used","useful","usefully","usefulness","uses","using","usually","uucp","v","value","various","very","via","viz","vol","vols","vs","w","want","wanted","wanting","wants","was","wasnt","way","ways","we","wed","well","were","weve","wed","welcome","well","wells","went","were","werent","what","whatll","whats","whatever","whats","when","whence","whenever","where","wheres","whereafter","whereas","whereby","wherein","wheres","whereupon","wherever","whether","which","while","whim","whither","who","wholl","whos","whod","whoever","whole","whom","whomever","whos","whose","why","widely","will","willing","wish","with","within","without","wont","wonder","words","work","worked","working","works","world","would","wouldnt","www","x","y","year","years","yes","yet","you","youd","youll","youre","youve","youd","young","younger","youngest","your","youre","yours","yourself","yourselves","z","zero","zt","zz"]:
                wenben3.append(i)
        for i in wenben3:
            k=wenben1.count(i)
            cishu1.append(k)
        hhhhhh=' '.join(wenben1)
        print(hhhhhh)

def new_window():
    top=Tk()
    top.geometry('750x560')
    top.title('欢迎进行文本编辑')
    button1=Button(top,text='显示原文本',font=20,bg='red',command=xianshiwenben)
    button2=Button(top,text='单词拆解',font=20,bg='red',command=dancichaijie)
    button12=Button(top,text='单词合并',font=20,bg='red',command=dancihebing)
    button3=Button(top,text='单词数量统计',font=20,bg='blue',command=dancishuliangtongji)
    button4=Button(top,text='单词种类统计',font=20,bg='blue',command=dancizhongleitongji)
    button5=Button(top,text='词频统计',font=20,bg='blue',command=cipingtongji)
    button6=Button(top,text='关键词生成',font=20,bg='orange',command=guanjiancishengcheng)
    button7=Button(top,text='关键词词频',font=20,bg='orange',command=guanjianciciping)
    button8=Button(top,text='关键词柱状图',font=20,bg='orange',command=guanjiancizhuzhuangtu)
    button9=Button(top,text='查找单词',bg='Magenta',font=20,command=chazhaodanci)
    button11=Button(top,text='删除单词',bg='Magenta',font=20,command=shanchudanci)
    button13=Button(top,text='替换单词',bg='Magenta',font=20,command=tihuandanci)
    button10=Button(top,text='退出编辑器',font=20,bg='Cyan',command=top.destroy)
    
    button1.place(x=50,y=70)
    button2.place(x=250,y=70)
    button12.place(x=450,y=70)
    button3.place(x=50,y=200)
    button4.place(x=250,y=200)
    button5.place(x=450,y=200)
    button6.place(x=50,y=330)
    button7.place(x=250,y=330)
    button8.place(x=450,y=330)
    button9.place(x=50,y=460)
    button11.place(x=250,y=460)
    button13.place(x=450,y=460)
    button10.place(x=600,y=500)
    
    Label(top,text='操作文本',fg='green',font=30).place(x=50,y=30)
    Label(top,text='数量统计',fg='green',font=30).place(x=50,y=160)
    Label(top,text='关键词',fg='green',font=30).place(x=50,y=290)
    Label(top,text='查找,删除,替换',fg='green',font=30).place(x=50,y=420)
    top.mainloop()
    
        

Button(root,text='文本编辑',width=20,command=log_in,fg='purple',bg='Cyan').place(x=290,y=414)
root.mainloop()
    





