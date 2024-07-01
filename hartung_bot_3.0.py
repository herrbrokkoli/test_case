import matplotlib.pyplot as plt
import math

#верштина графа (одна клеточка поля)
class Peak:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.parent=None
        self.g=None
        self.h=None
        
    def add_to_front(self,front):
        front.append(self)
    def del_from_front(self,front):
        front.remove(self)
    def add_to_explored(self,table,explored):
        explored.append(self)

    def show_param(self):
        print('x=',self.x,'y=',self.y,' parent=',self.parent.x,self.parent.y,' g=',self.g,' h=',self.h)
        
def show(ls):
    for i in ls:
        print(i.x,i.y)
            #,'',i.parent.x,i.parent.y,'',i.g,i.h)
    #print('__')

#расчет эвристики Эвклидового расстояния     
def evclide(first,second):
    return math.hypot(first.x - second.x,second.y - first.y)
#расчет эвристики Манхеттенского расстояния 
def manhettn(first,second):
    return abs(first.x - second.x)+abs(second.y - first,y)
#поиск новых частей фронта.
def get_front(table,peak):
    friend=[]
    for i in table:
        if (((i.x==peak.x-1 or i.x==peak.x+1) and i.y==peak.y) or ((i.y==peak.y-1 or i.y==peak.y+1) and i.x==peak.x)) and check(i,explored)==False:
            if check(i,front):    
                if i.g>peak.g+1:
                    i.g=peak.g+1
                    i.parent=peak
            else:
                i.g=peak.g+1
                i.parent=peak
            #можно использовать Манхеттен вместо Эвклида
            i.h=evclide(i,finish)
            friend.append(i)
    return friend

#проверка присутствия точки в списке
def check(point,li):
    for i in li:
        if point.x==i.x and point.y==i.y:
            return True
    return False

#добавляем точки во фронт, если там их ещё нет
def add_new_to_front(front,new):
    for i in new:
        if front.count(i)==0 and check(i,explored)==False:
            i.add_to_front(front)
            
#выбираем куда шагнуть        
def choose_step(front):
    if len(front)==0:
        return None
    point=front[0]
    for i in front:
        if (i.g+i.h)<=(point.g+point.h):
            point=i
    return point

#ищет маршрут от старта к финишу
def path_find(start,finish,explored):
    while path[-1].x!=start.x or path[-1].y!=start.y:
        for i in explored:
            if path[-1].x==i.x and path[-1].y==i.y:
                path.append(i.parent)
                break
            
#отпимизация поворотов (предпологаем, что нужно их минимальное количество, а не угол)
b=round(math.sqrt(2),3)
def path_optimal(path):
    for i in range(len(path)):
        if i<(len(path)-2):
            if round(evclide(path[i],path[i+2]),3)==b:
               path.pop(i+1)
        
#размеры сетки      
row=15
col=15
#препятствия
'''
stone=[Peak(1,2),Peak(2,2),Peak(3,2),Peak(4,2),Peak(5,2),Peak(8,9),
        Peak(9,8),Peak(10,7),Peak(6,6),Peak(7,5),Peak(6,0),
        Peak(5,7),Peak(7,10),Peak(6,11),Peak(8,4),Peak(6,1)]
'''
stone=[
        Peak(4,3),Peak(5,3),Peak(6,3),Peak(7,3),Peak(8,3),Peak(9,3),Peak(10,3),
        Peak(4,9),Peak(5,9),Peak(6,9),Peak(7,9),Peak(8,9),Peak(9,9),Peak(10,9),
        Peak(10,4),Peak(10,5),Peak(10,6),Peak(10,7),Peak(10,8)
        ]
'''
stone=[
        Peak(1,3),Peak(1,4),Peak(1,5),Peak(1,6),
        Peak(5,3),Peak(5,4),Peak(5,5),Peak(5,6),
        Peak(7,3),Peak(7,4),Peak(7,5),Peak(7,6),
        Peak(9,3),Peak(9,4),Peak(9,5),Peak(9,6),
        Peak(13,3),Peak(13,4),Peak(13,5),Peak(13,6),
        Peak(2,3),Peak(4,3),Peak(3,4),Peak(3,5),
        Peak(8,8),Peak(8,9),Peak(8,10),Peak(8,11),
        Peak(11,8),Peak(11,9),Peak(11,10),Peak(11,11),
        Peak(3,8),Peak(3,9),Peak(3,10),Peak(3,11),
        Peak(6,8),Peak(6,9),Peak(6,10),Peak(6,11),
        Peak(9,8),Peak(10,8),Peak(9,11),Peak(10,11),
        Peak(4,10),Peak(5,9),
        Peak(8,4),Peak(8,6),Peak(11,3),Peak(11,5),Peak(11,6),Peak(12,3),Peak(12,5)
        ]
'''
#список неисследованных точек сетки
table=[]
#точки старта и финиша
start=Peak(1,1)
start.g=0
start.h=0
start.parent=Peak(-1,-1)
finish=Peak(13,13)
#список "фронта" исследования
front=[]
#список исследованных точек сетки
explored=[]
#искомый путь
path=[finish]

#создаем поле точек
for i in range(row):
    for j in range(col):
        peak=Peak(i,j)
        peak.parent=Peak(-1,-1)
        peak.g=0
        peak.h=0
        table.append(peak)
#убираем из поля точек точки-препятствия, по которым ходить нельзя        
for i in stone:
    for j in table:
        if i.x==j.x and i.y==j.y:
            table.remove(j)
            break

start.add_to_front(front)

while len(front)!=0:
    #print('FRONT')
    #show(front)
    #print('__')
    step=choose_step(front)
    step.show_param()
    if (step.x==finish.x) and (step.y==finish.y):
        step.add_to_explored(table,explored)
        print('FIND!')
        break
    new=get_front(table,step)
    #show(new)
    add_new_to_front(front,new)
    step.del_from_front(front)
    step.add_to_explored(table,explored)
    #print("EXPLORED")
    #show(explored)
    #print("____")
    
if len(front)==0:  
    print('NO WAY!')

path_find(start,finish,explored)
    
#подготовка данных для графика визуализации
def make_plot_data(point_list):
    x=[]
    y=[]
    data=[]
    for i in point_list:
        x.append(i.x)
        y.append(i.y)
    data.append(x)
    data.append(y)
    return data
        
    
#print(path)
plt.figure(figsize=(0.41*col, 0.41*row))
#plt.tick_params(which='major', length=10, width=10)

data=make_plot_data(table)
plt.plot(data[0],data[1],'gs',markersize=20)
data=make_plot_data(explored)
plt.plot(data[0],data[1],'bs',markersize=20)
data=make_plot_data(front)
plt.plot(data[0],data[1],'ys',markersize=20)
data=make_plot_data(stone)
plt.plot(data[0],data[1],'ks',markersize=20)

data=make_plot_data(path)
plt.plot(data[0],data[1],'r-')

path_optimal(path)
data=make_plot_data(path)
plt.plot(data[0],data[1],'w-')

#srart
plt.plot(start.x,start.y,'ro',markersize=12)
#finish
plt.plot(finish.x,finish.y,'wo',markersize=12)
plt.show()
