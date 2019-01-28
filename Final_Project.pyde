add_library('sound')
import os,random,time
import math
path=os.getcwd()
class Game:
    def __init__(self,w,h,g):
        self.w=w
        self.h=h
        self.g=g
        self.falcon=Falcon(50,50,self.g,110,'car.png','car1.png','camel.png','camel1.png','car2.png','car3.png','camel2.png','camel3.png','camel4.png','camel5.png','camel6.png','camel7.png','car4.png','car5.png','car6.png','car7.png','car8.png','car9.png','car10.png','car11.png','car12.png','car13.png','car14.png','car15.png','turbo.png',220,220,220,220,0)
        self.x=0
        self.bg=loadImage(path+'/landscape.jpg')
        self.menu=loadImage(path+'/menu.png')
        self.End=loadImage(path+'/end.png')
        self.scores=loadImage(path+'/scores.png')
        self.music=SoundFile(this,path+'/themeSong.mp3')
        self.coinSound=SoundFile(this,path+'/coin.mp3')
        self.collisionSound=SoundFile(this,path+'/collide.mp3')
        self.pause=False
        self.pauseSound=SoundFile(this,path+'/pause.mp3')
        self.state='menu'
        self.name=""
        self.sec=0
        self.mint=0
        self.timecnt=0
        self.secsec=0
        self.highScore=False
        
        self.obstacles=[]
        for i in range(7):
            self.obstacles.append(Obstacles(1000+i*1200,self.g-80,self.g-140,40,str(i)+".png",200,200)) 
    
        self.stars=[]
        for i in range(25):
            self.stars.append(Star(700+i*300,random.randint(200,400),20,self.g,"star.png",40,40,6)) 
    
    def display(self):
        if self.state=='menu':
            image(self.menu,0,0,self.w,self.h)
            textSize(40)
            text(self.name,120,40)

        elif self.state=='play':
            self.timecnt=(self.timecnt+1)%60
            if self.timecnt == 0:
                self.sec+=1
                self.secsec+=1
                if self.sec==60:
                    self.mint+=1
                    self.sec=0
            if self.x<=8781:
                x = self.x%(self.w*6)
                image(self.bg,0,0,self.w,self.h,0+x,0,self.w+x,self.h)
            for s in self.stars:
                s.display()
            for t in self.obstacles:
                t.display()
            self.falcon.display()
            textSize(40)
            fill(0,0,255) 
            text('Coins: '+str(self.falcon.cnt),10,50)
            if self.sec>=10:
                text("Time 0"+str(self.mint)+":"+str(self.sec),1100,50)
            else:
                text("Time 0"+str(self.mint)+":0"+str(self.sec),1100,50)

class Falcon:
    def __init__(self,x,y,g,r,img,img2,img3,img4,img5,img6,img7,img8,img9,img10,img11,img12,img13,img14,img15,img16,img17,img18,img19,img20,img21,img22,img23,img24,img25,w1,w2,h1,h2,F):
        self.x=x
        self.y=y
        self.vx=0
        self.vy=0
        self.cnt=0
        self.turbo=0
        self.turboTime=0
        self.turbocnt=0
        self.w1=w1
        self.w2=w2
        self.h1=h1
        self.h2=h2
        self.r=r
        self.g=g
        self.F=F
        self.f=0
        self.o=0
        self.q=0
        self.keyHandler={RIGHT:False,LEFT:False,UP:False}
        self.img=loadImage(path+'/'+img)
        self.img2=loadImage(path+'/'+img2)
        self.img3=loadImage(path+'/'+img3)
        self.img4=loadImage(path+'/'+img4)
        self.img5=loadImage(path+'/'+img5)
        self.img6=loadImage(path+'/'+img6)
        self.img7=loadImage(path+'/'+img7)
        self.img8=loadImage(path+'/'+img8)
        self.img9=loadImage(path+'/'+img9)
        self.img10=loadImage(path+'/'+img10)
        self.img11=loadImage(path+'/'+img11)
        self.img12=loadImage(path+'/'+img12)
        self.img13=loadImage(path+'/'+img13)
        self.img14=loadImage(path+'/'+img14)
        self.img15=loadImage(path+'/'+img15)
        self.img16=loadImage(path+'/'+img16)
        self.img17=loadImage(path+'/'+img17)
        self.img18=loadImage(path+'/'+img18)
        self.img19=loadImage(path+'/'+img19)
        self.img20=loadImage(path+'/'+img20)
        self.img21=loadImage(path+'/'+img21)
        self.img22=loadImage(path+'/'+img22)
        self.img23=loadImage(path+'/'+img23)
        self.img24=loadImage(path+'/'+img24)
        self.img25=loadImage(path+'/'+img25)
        self.dir=1
        self.i=1
        self.hit=False
        self.numHit=0
        self.gameOver=False
        self.collide=0
    
    def gravity(self):
        if self.y+self.r<self.g:
            self.vy+=0.1
        else:
            self.vy=0
    
        if self.g-(self.y+self.r)<self.vy:
            self.vy=self.g-(self.y+self.r)

    def collision(self):
        for s in Play.stars:
            if self.distance(s) <= self.r+s.r: 
                Play.stars.remove(s)
                del s
                self.cnt+=1
                self.numHit=1
                Play.coinSound.play()
                
        if self.cnt==5:
            if self.hit:
                self.hit=False
            else:
                self.turboTime=4
            self.cnt=0

        for e in Play.obstacles:
            if e.x+20<=self.x+self.r and self.x-self.r<=e.x+(e.w//2)+(e.r//2)-20 and self.y>=e.y-e.h:
                if e.x+20==(self.x+self.r-10) or e.x+20==(self.x-self.r-10):
                    Play.collisionSound.play()
                self.collide=0
                self.vx=0
                self.hit=True
                self.turboTime=0
                if self.collide==0:
                    self.collide+=1
    
    def distance(self,target):
        return ((self.x-target.x)**2+(self.y-target.y)**2)**0.5

    def update(self):
        if self.x+self.r>=8781:
            self.gameOver=True
        if not self.gameOver:
            self.gravity()
            self.collision()
            if self.keyHandler[RIGHT]: 
                if self.hit:
                    self.vx=2
                else:
                    self.vx=4 
                self.dir=1
            elif self.keyHandler[LEFT]:
                if self.hit:
                    self.vx=-2
                else:
                    self.vx=-4 
                self.dir=-1
            else:
                self.vx=0
                
            if self.turboTime>0 and self.hit==False:
                image(self.img25,580,100)
                if self.keyHandler[RIGHT]: 
                    self.vx=7
                elif self.keyHandler[LEFT]:
                    self.vx=-7
                else:
                    self.vx=0
                    
                self.turbocnt=(self.turbocnt+1)%60
                if self.turbocnt==0:
                    self.turboTime-=1
                    
            if self.keyHandler[UP] and self.vy==0:
                self.vy=-7.5
                
            self.x+=self.vx
            self.y+=self.vy
            
            if self.x >= Play.w//2 and self.x < 8718:       
                Play.x+=self.vx
            
            if self.x+self.r < (2*self.r):
                self.x=self.r
        else:
            Play.state='over'
            if Play.state=='over' and not Play.highScore:
                fill(255,0,0)
                textSize(25)
                results=open('highScores.csv','a')
                results.write(Play.name+","+str(Play.secsec))
                results.write(' \n')
                results.close()
        
    def display(self):
        self.update()
        if self.hit:
            if self.vx!=0:
                if self.dir >=0:
                    if self.vy!=0:
                        image(self.img7,self.x-Play.x-self.r,self.y-self.r,self.w2,self.h2)
                    else:
                        if int(self.q)==0:
                            image(self.img3,self.x-Play.x-self.r,self.y-self.r,self.w2,self.h2)
                            self.q+=0.1
                            
                        elif int(self.q)==1:
                            image(self.img7,self.x-Play.x-self.r,self.y-self.r,self.w2,self.h2)
                            self.q+=0.1
                            
                        elif int(self.q)==2:
                            image(self.img9,self.x-Play.x-self.r,self.y-self.r,self.w2,self.h2)
                            self.q+=0.1   
                        
                        elif int(self.q)==3:
                            image(self.img11,self.x-Play.x-self.r,self.y-self.r,self.w2,self.h2)
                            self.q+=0.1                    
                            if self.q > 4.0:
                                self.q=0
                else:
                    if self.vy!=0:
                        image(self.img8,self.x-Play.x-self.r,self.y-self.r,self.w2,self.h2)
                    else:
                        if int(self.q)==0:
                            image(self.img4,self.x-Play.x-self.r,self.y-self.r,self.w2,self.h2)
                            self.q+=0.1
                            
                        elif int(self.q)==1:
                            image(self.img8,self.x-Play.x-self.r,self.y-self.r,self.w2,self.h2)
                            self.q+=0.1
                                
                        elif int(self.q)==2:
                            image(self.img10,self.x-Play.x-self.r,self.y-self.r,self.w2,self.h2)
                            self.q+=0.1   
                        
                        elif int(self.q)==3:
                            image(self.img12,self.x-Play.x-self.r,self.y-self.r,self.w2,self.h2)
                            self.q+=0.1                    
                            if self.q > 4.0:
                                self.q=0                            
            else:
                if self.dir >=0:
                    if self.vy!=0:
                        image(self.img7,self.x-Play.x-self.r,self.y-self.r,self.w2,self.h2)
                    else:    
                        image(self.img3,self.x-Play.x-self.r,self.y-self.r,self.w2,self.h2) 
                else:
                    if self.vy!=0:
                        image(self.img8,self.x-Play.x-self.r,self.y-self.r,self.w2,self.h2)
                    else:
                        image(self.img4,self.x-Play.x-self.r,self.y-self.r,self.w2,self.h2) 
        else:
            if self.turboTime==0:
                if self.dir >=0:
                    if int(self.f)==0:
                        image(self.img,self.x-Play.x-self.r,self.y-self.r,self.w2,self.h2)
                        self.f+=0.1
                        
                    elif int(self.f)==1:
                        image(self.img13,self.x-Play.x-self.r,self.y-self.r,self.w2,self.h2)
                        self.f+=0.1
                        
                    elif int(self.f)==2:
                        image(self.img15,self.x-Play.x-self.r,self.y-self.r,self.w2,self.h2)
                        self.f+=0.1   
                    
                    elif int(self.f)==3:
                        image(self.img17,self.x-Play.x-self.r,self.y-self.r,self.w2,self.h2)
                        self.f+=0.1
                        
                    elif int(self.f)==4:
                        image(self.img19,self.x-Play.x-self.r,self.y-self.r,self.w2,self.h2)
                        self.f+=0.1                    
                        if self.f > 5.0:
                            self.f=0
                else:
                    if int(self.f)==0:
                        image(self.img2,self.x-Play.x-self.r,self.y-self.r,self.w2,self.h2)
                        self.f+=0.1
                        
                    elif int(self.f)==1:
                        image(self.img14,self.x-Play.x-self.r,self.y-self.r,self.w2,self.h2)
                        self.f+=0.1
                        
                    elif int(self.f)==2:
                        image(self.img16,self.x-Play.x-self.r,self.y-self.r,self.w2,self.h2)
                        self.f+=0.1   
                    
                    elif int(self.f)==3:
                        image(self.img18,self.x-Play.x-self.r,self.y-self.r,self.w2,self.h2)
                        self.f+=0.1
                        
                    elif int(self.f)==4:
                        image(self.img20,self.x-Play.x-self.r,self.y-self.r,self.w2,self.h2)
                        self.f+=0.1                    
                        if self.f > 5.0:
                            self.f=0
            else:
                if self.dir >=0:
                    if int(self.o)==0:
                        image(self.img5,self.x-Play.x-self.r,self.y-self.r,self.w2,self.h2)
                        self.o+=0.1
                        
                    elif int(self.o)==1:
                        image(self.img21,self.x-Play.x-self.r,self.y-self.r,self.w2,self.h2)
                        self.o+=0.1
                            
                    elif int(self.o)==2:
                        image(self.img23,self.x-Play.x-self.r,self.y-self.r,self.w2,self.h2)
                        self.o+=0.1                  
                        if self.o > 3.0:
                            self.o=0
                else:
                    if int(self.o)==0:
                        image(self.img6,self.x-Play.x-self.r,self.y-self.r,self.w2,self.h2)
                        self.o+=0.1
                        
                    elif int(self.o)==1:
                        image(self.img22,self.x-Play.x-self.r,self.y-self.r,self.w2,self.h2)
                        self.o+=0.1
                            
                    elif int(self.o)==2:
                        image(self.img24,self.x-Play.x-self.r,self.y-self.r,self.w2,self.h2)
                        self.o+=0.1                  
                        if self.o > 3.0:
                            self.o=0
                                
class Star:
    def __init__(self,x,y,r,g,img,w,h,F):
        self.x=x
        self.y=y
        self.vx=1
        self.vy=2
        self.w=w
        self.h=h
        self.r=r
        self.g=g
        self.y1=200
        self.y2=400
        self.img=loadImage(path+'/star.png')
        
    def update(self):
        if self.y < self.y1 or self.y > self.y2:
            self.vy*=-1
      
        self.y+=self.vy
        
        image(self.img,self.x-Play.x,self.y,self.w,self.h)

    def display(self):
        self.update()
        
class Obstacles:
    def __init__(self,x,y,g,r,img,w,h):
        self.x=x
        self.y=y
        self.g=g
        self.r=r
        self.w=w
        self.h=h
        self.img=loadImage(path+'/'+img)

    def display(self):
        image(self.img,self.x-Play.x-self.r,self.g-self.r,self.w,self.h)

Play=Game(1480,854,700)

def generate2dList(inputtedList):
    print(inputtedList)
    newList = []
    for i in inputtedList:
        innerList = i.split(",")
        innerList[1] = int(innerList[1])
        newList.append(innerList)
    return newList

def sortList(innerList):
    for j in range(len(innerList)):
        minIndex = j
        min = innerList[j][1]
        for i in range(len(innerList[j:])):
            if innerList[j+i][1] < min:
                minIndex = j+i
        temp = innerList[j]
        innerList[j] = innerList[minIndex]
        innerList[minIndex] = temp
    return(innerList)       
            

    
def setup():
    size(Play.w,Play.h)
    background(0)
def draw():
    if Play.state=='over' and not Play.highScore:
        image(Play.End,0,0,Play.w,Play.h)
        fill(255,0,0)
        textSize(90)
        text(str(Play.secsec)+' seconds',800,270)
    elif Play.highScore:
        image(Play.scores,0,0,Play.w,Play.h)
        textSize(25)
        results=open('highScores.csv','r')
        addv=0
        scores = []
        for line in results:
            scores.append(line)
            
        scores = generate2dList(scores)
        scores = sortList(scores)
        for i in scores:
            fill(0,0,255)
            textSize(50)
            text(i[0]+" " + str(i[1])+ " seconds",600,200+addv)
            addv+=70
        
            
    elif not Play.pause:
        background(0)  
        Play.display()
    else:
        textSize(40)
        fill(0,0,255)
        text("Paused",Play.w//2,Play.h//2)
           
def keyPressed():
    if Play.state=="menu":
        fill(0,0,255)
        if 97 <= ord(key) <= 97+26 or 65<= ord(key)<=65+26 or keyCode == 32:
            Play.name+=key
        elif keyCode == 8:
            Play.name = Play.name[:len(Play.name)-1]
    
    if keyCode == 80:
        if Play.pause:
            Play.pause=False
            Play.music.play()
        else:
            Play.pause=True
            Play.pauseSound.play()
            Play.music.stop()

    if keyCode==LEFT:
        Play.falcon.keyHandler[LEFT]=True
    elif keyCode==RIGHT:
        Play.falcon.keyHandler[RIGHT]=True
    elif keyCode==UP:
        Play.falcon.keyHandler[UP]=True
        
def keyReleased():
  if keyCode==LEFT:
    Play.falcon.keyHandler[LEFT]=False
  elif keyCode==RIGHT:
    Play.falcon.keyHandler[RIGHT]=False
  elif keyCode==UP:
    Play.falcon.keyHandler[UP]=False

def mouseClicked():
    if Play.state=='menu' and 650<=mouseX<=970 and 400<=mouseY<=600:
        Play.state='play'
        Play.music.play()
    if Play.state=='over' and not Play.highScore:
        Play.highScore = True
        Play.music.stop()
    elif Play.highScore:
        Play.__init__(Play.w,Play.h,Play.g)    