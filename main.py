import nest_asyncio
nest_asyncio.apply()
import discord
import random
import time

intents = intents=discord.Intents.all()
intents.messages = True
client = discord.Client(intents=intents)

textList=["となりのきゃくはよくかきくうきゃくだ","いぬもあるけばぼうにあたる","あとのまつり","いろはにほへと","いんたーねっと","とまるなきけん","いんたーねっと","さんにんよればもんじゅのちえ",
          "とかげ","あめのひはさむい","はれのひはあつい","いしのうえにもさんねん","いそがばまわれ","おににかなぼう","しらぬがほとけ","さるもきからおちる","こっぺぱん","せんりのみちもいっぽから","ふくそすう","かんすう",
          "やまありたにあり","のーとぱそこん"]
chnannelData=[]
userData=[]
textNumber=0
channelNumber=-1
userNumber=-1


# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    #Botのメッセージは除外
    if message.author.bot:
        return
    #条件に当てはまるメッセージかチェックし正しい場合は返す
    global chnannelData
    global textNumber
    global channelNumber
    global userNumber

    if chnannelData!=None:
        for i in range(0,len(chnannelData)):
            if chnannelData[i][0]==message.channel.id:
                channelNumber=i  

    if chnannelData!=None and channelNumber!=-1:
        for i in range(0,len(chnannelData[channelNumber])):
            if message.author.id==chnannelData[channelNumber][i]:
                userNumber=i
        if userNumber!=-1 and message.content==textList[chnannelData[channelNumber][1]] and message.channel.id==chnannelData[channelNumber][0]:
            chnannelData[channelNumber][userNumber+1]+=1

    if message.content=="!play":
        textNumber=random.randint(0, len(textList)-1)
        if channelNumber==-1:
            chnannelData.append([message.channel.id,textNumber,False,0])
            channelNumber=0
        await message.channel.send("問題{}: ".format(chnannelData[channelNumber][3]+1)+textList[textNumber]+"\n\n\n\n\n\n\n\n\n\入力をせよ")

    if channelNumber!=-1 and userNumber==-1:
        chnannelData[channelNumber].append(message.author.id)
        chnannelData[channelNumber].append(0)
        if chnannelData!=None and chnannelData[channelNumber][2]==False and message.content==textList[chnannelData[channelNumber][1]] and message.channel.id==chnannelData[channelNumber][0] :
            chnannelData[channelNumber][len(chnannelData[channelNumber])-1]+=1

    if channelNumber!=-1 and chnannelData!=None and chnannelData[channelNumber][2]==False:
        chnannelData[channelNumber][1]=textNumber
    if channelNumber!=-1 and chnannelData!=None and chnannelData[channelNumber][2]==False and message.content==textList[chnannelData[channelNumber][1]] and message.channel.id==chnannelData[channelNumber][0] :
        await message.channel.send("<@{}>正解".format(message.author.id))
        chnannelData[channelNumber][3]+=1
        #chnannelData[channelNumber][2]=True 
        
        if chnannelData!=None and chnannelData[channelNumber][3]!=10:
            textNumber=random.randint(0, len(textList)-1)
            chnannelData[channelNumber][2]=False
            chnannelData[channelNumber][1]=textNumber
            await message.channel.send("問題{}: ".format(chnannelData[channelNumber][3]+1)+textList[textNumber]+"\n\n\n\n\n\n\n\n\n\入力をせよ")
        else:
           time.sleep(1)
           await message.channel.send("10問終了しました") #".format(chnannelData[channelNumber][userNumber])+"{},問正解".format(chnannelData[channelNumber][userNumber+1]
           if userNumber<len(chnannelData[channelNumber]):
              for i in range(4,len(chnannelData[channelNumber])-1):
                  if i%2!=1:
                      await message.channel.send("<@{}>".format(chnannelData[channelNumber][i])+"{}問正解".format(chnannelData[channelNumber][i+1]))
           del chnannelData[channelNumber]
    channelNumber=-1
    print(chnannelData)
    userNumber=-1
    


client.run("トークン")