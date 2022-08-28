"""
1,主逻辑
    开始游戏
    结束游戏
2，坦克：我方坦克，npc坦克
    移动
    射击
    展示
3.子弹
    移动
    展示
4.爆炸
    爆炸效果
5.墙壁
    碰撞体积
6.音效
    背景音乐
"""
import pygame#pygame可以改成其他简单的表示
import random
import time
class Maingame():
    window=None
    screen_width=800
    screen_height=500#a=(800，500)这种形式也可以
    tankp1=None
    npctank_list=[]#npc坦克列表
    npctank_count=random.randint(2,5)#npc坦克数量
    bullet_list=[]#子弹列表
    npcbullet_list = []
    explode_list=[]
    wall_list=[]
    def __init__(self):
        pass
    def startgame(self):
        pygame.display.init()#显示窗口
        Maingame.window=pygame.display.set_mode((Maingame.screen_width,Maingame.screen_height))#窗口大小
        self.creattank()
        self.npctank()#调用敌方坦克
        self.creatwall()
        pygame.display.set_caption('tank fight!!!—1.0')#窗口标题
        while True:
            Maingame.window.fill(color=pygame.Color(255,255,0))#设置窗口颜色
            self.event()#调用获取事件
            Maingame.window.blit(self.explain('剩余敌人：%d个'%len(Maingame.npctank_list)),(10,10))#在窗口上创建一个可指定位置的窗口来写出文字
            Maingame.window.blit(self.explain('上下左右—>移动，空格—>发射子弹，ESC—>复活坦克'), (10, 20))
            if Maingame.tankp1 and Maingame.tankp1.live:
                Maingame.tankp1.showtank()#调用坦克的显示
            else:
                del Maingame.tankp1
                Maingame.tankp1=None
            self.blitnpctank()
            if Maingame.tankp1 and not Maingame.tankp1.stop:
                Maingame.tankp1.move()
                Maingame.tankp1.hit_tank_wall()
                Maingame.tankp1.tank_npctank()
            self.blitwall()
            self.blitbullet()#调用子弹
            self.blitnpcbullet()
            self.blitexplode()
            time.sleep(0.01)#时间刷新，需要import time
            pygame.display.update()#刷新窗口以实现窗口常驻
    def creattank(self):
        Maingame.tankp1 = Mytank(350, 420)  # 设置坦克图片位置
        music=Music('music_2.wav')#选择音乐文件
        music.showmusic()#播放音乐
    def npctank(self):
        top=50
        for i in range(Maingame.npctank_count):
            speed = 1#速度随机,random.randint(a,b),使用import random
            left = random.randint(0, 7)
            ntank=Npctank(left*100,top,speed)#调用敌方坦克
            Maingame.npctank_list.append(ntank)#增加坦克列表
    def creatwall(self):
        for i in range(1,7):
            wall=Wall(100*i,200)
            Maingame.wall_list.append(wall)
    def blitwall(self):
        for i in Maingame.wall_list:
            if i.live:
                i.showwall()
            else:
                Maingame.wall_list.remove(i)
    def blitnpctank(self):
        for i in Maingame.npctank_list:#循环坦克列表
            if i.live:
                i.shownpctank()  # 展示坦克
                i.randmove()#调用随机移动
                i.hit_tank_wall()
                if Maingame.tankp1:
                    i.npctank_tank()#问题所在
                b=i.npcshot()#调用射击函数
                if b:
                    Maingame.npcbullet_list.append(b)#每射击一次，加入子弹列表
            else:
                Maingame.npctank_list.remove(i)
    def blitbullet(self):
        for i in Maingame.bullet_list:#遍历子弹列表
            if i.live:#如果子弹未到达墙边
                i.bulletshow()#调用展示子弹
                i.bulletmove()#调用子弹移动
                i.hitnpctank()#调用射击敌方坦克
                i.hitwall()#调用射击墙壁
            else:
                Maingame.bullet_list.remove(i)#删除当前子弹
    def blitexplode(self):
        for i in Maingame.explode_list:
            if i.live:
                i.showexplode()
            else:
                Maingame.explode_list.remove(i)
    def blitnpcbullet(self):
        for i in Maingame.npcbullet_list:#遍历子弹列表
            if i.live:
                i.bulletshow()#调用展示子弹
                i.bulletmove()#调用子弹移动
                i.hitwall()
                if Maingame.tankp1 and Maingame.tankp1.live:#判断坦克是否活着
                    i.hittank()#调用
            else:
                Maingame.npcbullet_list.remove(i)
    def event(self):
        eventlist=pygame.event.get()#获取事件，键盘鼠标的输入
        for i in eventlist:
            if i.type==pygame.QUIT:#判断类型，大写单词对应相应意思
                self.endgame()
            if i.type==pygame.KEYDOWN:
                if i.key == pygame.K_ESCAPE and not Maingame.tankp1:
                    self.creattank()
                if Maingame.tankp1 and Maingame.tankp1.live:
                    if i.key==pygame.K_UP:
                        print('坦克上移')
                        Maingame.tankp1.direction='N'#坦克方向
                        Maingame.tankp1.stop=False#调用坦克移动
                    elif i.key==pygame.K_DOWN:
                        print('坦克下移')
                        Maingame.tankp1.direction ='S'
                        Maingame.tankp1.stop=False
                    elif i.key==pygame.K_RIGHT:
                        print('坦克右移')
                        Maingame.tankp1.direction ='R'
                        Maingame.tankp1.stop=False
                    elif i.key == pygame.K_LEFT:
                        print('坦克左移')
                        Maingame.tankp1.direction ='L'
                        Maingame.tankp1.stop=False
                    elif i.key == pygame.K_SPACE:
                        if len(Maingame.bullet_list)<4:#判断并限制子弹数量，
                            print('坦克射击')
                            b=Bullet(Maingame.tankp1)
                            Maingame.bullet_list.append(b)
                            print('已经发射的子弹数量：%d' % len(Maingame.bullet_list))  # 提示剩余子弹
                            music=Music('music_3.wav')
                            music.showmusic()
                        else:
                            print('没子弹了！！！')
            if i.type == pygame.KEYUP:
                if (i.key==pygame.K_UP or i.key==pygame.K_DOWN or i.key==pygame.K_LEFT or i.key==pygame.K_RIGHT):
                    if Maingame.tankp1 and Maingame.tankp1.live:
                        Maingame.tankp1.stop=True
    def explain(self,text):
        pygame.font.init()#创建文字初始化
        #fontlist=pygame.font.get_fonts()#查看系统字体
        #print(fontlist)#同上
        font=pygame.font.SysFont('隶书',18)
        surface=font.render(text,True,(255,0,0))#(文字，抗锯齿，颜色)
        return surface
    def endgame(self):
        print('thanks for using')
        exit()#退出
class Baseitem(pygame.sprite.Sprite):#精灵碰撞调用
    def __init__(self):
        pygame.sprite.Sprite.__init__()
class Tank(Baseitem):#坦克类调用精灵碰撞类
    def __init__(self,left,top):#left=左距，top=上距
        self.images={
            'N':pygame.image.load('tank-N.png'),#设置不坦克同方向的图片
            'S':pygame.image.load('tank-S.png'),
            'R':pygame.image.load('tank-R.png'),
            'L':pygame.image.load('tank-L.png')
        }
        self.direction='N'#决定方向
        self.image=self.images[self.direction]
        self.rect=self.image.get_rect()#获取出现的位置
        self.rect.left=left#左距
        self.rect.top=top#上距
        self.speed=2#移动的速度不能小于1
        self.stop=True
        self.live=True
        self.beforeleft=self.rect.left
        self.beforetop=self.rect.top
    def move(self):
        self.beforeleft = self.rect.left
        self.beforetop = self.rect.top
        if self.direction=='N':#判断坦克方向
            if self.rect.top>19:#判断屏幕的移动范围
                self.rect.top -=self.speed#坦克的移动
        elif self.direction=='S':
            if self.rect.top+self.rect.height*0.5<Maingame.screen_height:
                self.rect.top += self.speed
        elif self.direction=='L':
            if self.rect.left>0:
                self.rect.left -= self.speed
        elif self.direction=='R':
            if self.rect.left+self.rect.width*2<Maingame.screen_width:
                self.rect.left += self.speed
    def stay(self):
        self.rect.left=self.beforeleft
        self.rect.top=self.beforetop
    def hit_tank_wall(self):
        for i in Maingame.wall_list:
            if pygame.sprite.collide_rect(i,self):
                self.stay()
    def shot(self):
        return Bullet(self)
    def showtank(self):
        self.image=self.images[self.direction]#获取方向
        Maingame.window.blit(self.image,self.rect)#出现图片
class Mytank(Tank):
    def __init__(self,left,top):
        super(Mytank,self).__init__(left,top)
    def tank_npctank(self):#坦克撞击地方坦克
        for i in Maingame.npctank_list:
            if pygame.sprite.collide_rect(i,self):
                self.stay()
class Npctank(Tank):
    def __init__(self,left,top,speed):
        super(Npctank,self).__init__(left,top)#调用父类live
        #self.live=True#同上
        self.images = {
            'N': pygame.image.load('tank-npc-N.png'),  # 设置不坦克同方向的图片
            'S': pygame.image.load('tank-npc-S.png'),
            'R': pygame.image.load('tank-npc-R.png'),
            'L': pygame.image.load('tank-npc-L.png')
        }
        self.direction = self.randdirection()#随机坦克方向
        self.image = self.images[self.direction]
        self.rect = self.image.get_rect()  # 获取出现的位置
        self.rect.left = left  # 左距
        self.rect.top = top  # 上距
        self.speed = speed  # 移动的速度不能小于1
        self.stop = True
        self.step=random.randint(10,400)

    def randdirection(self):
        num=random.randint(1,4)
        if num==1:
            return 'N'
        elif num==2:
            return 'S'
        elif num==3:
            return 'R'
        elif num==4:
            return 'L'
    def shownpctank(self):
        super().showtank()
    def randmove(self):#随机移动
        if self.step<20:#判断移动的距离
            self.direction=self.randdirection()#移动的方向
            self.step=random.randint(20,200)#随即移动的距离
        else:
            self.move()
            self.step-=1#记录移动距离
    def npcshot(self):
        num=random.randint(0,100)
        if num<=1:
            return Bullet(self)
    def npctank_tank(self):#敌方坦克撞击我方坦克
        if pygame.sprite.collide_rect(self,Maingame.tankp1):
            self.stay()
class Bullet(Baseitem):#子弹
    def __init__(self,tank):
        self.image=pygame.image.load('buttle.png')
        self.direction=tank.direction
        self.rect=self.image.get_rect()
        self.speed=random.randint(3,7)
        if self.direction=='N':
            self.rect.left=tank.rect.left+tank.rect.width/2-self.rect.width/2
            self.rect.top = tank.rect.top  - self.rect.height / 2
        elif self.direction=='S':
            self.rect.left = tank.rect.left + tank.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top + tank.rect.height - self.rect.height / 2
        elif self.direction=='L':
            self.rect.left = tank.rect.left
            self.rect.top = tank.rect.top +tank.rect.width /2-self.rect.height/2#有问题
        elif self.direction=='R':
            self.rect.left = tank.rect.left +tank.rect.width+ self.rect.width / 2
            self.rect.top = tank.rect.top +tank.rect.width/2-self.rect.height/2#有问题
        self.speed=4
        self.live=True#子弹抵达墙边

    def bulletmove(self):
        if self.direction=='N':#判断子弹方向，
            if self.rect.top>0+self.rect.height:#根据子弹位置，移动子弹
                self.rect.top-=self.speed
            else:
                self.live=False#
        elif self.direction=='S':
            if self.rect.top < Maingame.screen_height-self.rect.height:
                self.rect.top += self.speed
            else:
                self.live=False
        elif self.direction=='L':
            if self.rect.left > 0+self.rect.width:
                self.rect.left -= self.speed
            else:
                self.live=False
        elif self.direction=='R':
            if self.rect.left < Maingame.screen_width-self.rect.width:
                self.rect.left += self.speed
            else:
                self.live=False
    def bulletshow(self):
        Maingame.window.blit(self.image,self.rect)#子弹展示
    def hitnpctank(self):#子弹撞击敌方坦克
        for i in Maingame.npctank_list:
            if pygame.sprite.collide_rect(i,self):#collide_rect碰撞体积
                b=Explode(i)
                Maingame.explode_list.append(b)
                self.live=False
                i.live=False
    def hittank(self):
        if pygame.sprite.collide_rect(self,Maingame.tankp1):
            explode=Explode(Maingame.tankp1)
            Maingame.explode_list.append(explode)
            self.live=False
            Maingame.tankp1.live=False
    def hitwall(self):
        for i in Maingame.wall_list:
            if pygame.sprite.collide_rect(i,self):
                self.live=False
                i.hp-=1
                if i.hp==0:
                    i.live=False
class Explode():#爆炸
    def __init__(self,tank):
        self.rect=tank.rect
        self.step=0
        self.live=True
        self.images=[
            pygame.image.load('explode1.png'),
            pygame.image.load('explode2.png'),
            pygame.image.load('explode3.png'),
            pygame.image.load('explode4.png')
        ]
        self.image=self.images[self.step]
    def showexplode(self):
        if self.step<len(self.images):
            Maingame.window.blit(self.image,self.rect)
            self.image=self.images[self.step]
            self.step+=1
        else:
            self.live=False
            self.step=0
class Wall():
    def __init__(self,left,top):
        self.image=pygame.image.load('wall.png')
        self.rect=self.image.get_rect()
        self.rect.left=left
        self.rect.top=top
        self.live=True
        self.hp=2
    def showwall(self):
        Maingame.window.blit(self.image,self.rect)

class Music():
    def __init__(self,filename):
        self.filename=filename
        pygame.mixer.init()#混响器初始化
        pygame.mixer.music.load(self.filename)#加载音乐文件
    def showmusic(self):
        pygame.mixer.music.play(loops=0)#播放音乐，播放次数

class Test:
    def __init__(self):
        windo=0
    def test(self):

        Maingame.windo = pygame.display.set_mode((Maingame.screen_width, Maingame.screen_height))  # 窗口大小
        Maingame.windo.fill(color=pygame.Color(0, 0, 0))  # 窗口颜色

a=1
if a==0:
    Maingame().startgame()
else:
    print('已运行tankfight!!!')

