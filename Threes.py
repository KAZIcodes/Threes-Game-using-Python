import pygame
import random

n = 4
mat = [[0]*4 for i in range(4)]
for i in range(9):
    r,c = random.randint(0,3), random.randint(0,3)
    while mat[r][c]!=0:
        r,c = random.randint(0,3), random.randint(0,3)
    mat[r][c] = random.randint(1,3)
[print(" ".join([str(x) for x in r])) for r in mat]


# ye tabe bara inke harja khasim check konim bebinim tamoome bazi ya na mitoonim edame bedim    
def finished():    
    for i in range(n):
        for j in range(n):
            if j != n-1 and mat[i][j] != 1 and mat[i][j] != 2:  #if there is equal adjacent numbers other than 1 and 2 in a row 
                if mat[i][j]==mat[i][j+1]:
                    return False
            if mat[i][j] == 0:  #if there is an empty place 
                return False
            if j != n-1 and mat[j][i] != 1 and mat[j][i] != 2:  #if there is equal adjacent numbers other than 1 and 2 in a column
                if mat[j][i]==mat[j+1][i]:
                    return False
            if j != n-1:                        #if we have adjacent 1and2 s
                if (mat[i][j] == 1 and mat[i][j+1] == 2) or (mat[i][j] == 2 and mat[i][j+1] == 1):   
                    return False
                if (mat[j][i] == 1 and mat[j+1][i] == 2) or (mat[j][i] == 2 and mat[j+1][i] == 1):
                    return False
    return True

#RGB Colors
White = (255, 255, 255)
Black = (0,0,0)
Red = (255,51,51)
Blue = (51,51,255)
#initialize all imported pygame modules
pygame.init()
#making the game screen
size = (600,700)
surface = pygame.display.set_mode(size)
surface.fill((204,255,255))
# grid:
grid_node_width = size[0]//4  
grid_node_height = size[1]//4
def createSquare(x, y, color,BR=0):
    pygame.draw.rect(surface, color, [x, y, grid_node_width, grid_node_height],border_radius = BR)

font_name, font_size = "Times new Roman", 100
font = pygame.font.SysFont(font_name, font_size)

miniX = (size[0]//4)
miniY = (size[1]//4)
def visualizeGrid(miniX, miniY):
    y = 0  # we start at the top of the screen
    for row in mat:
        x = 0 # for every row we start at the left of the screen again
        for item in row:
            if item == 1:
                createSquare(x, y, (167, 232, 231))
                createSquare(x+3, y+3, Blue,BR=15)
                createSquare(x+3, y+150, (0,0,204),BR=15)
                text = font.render("1", True, Black)
                surface.blit(text,(x + (miniX-text.get_width())//2,y + (miniY- text.get_height())//2))
                
                    
            elif item == 2:
                createSquare(x, y, (167, 232, 231))
                createSquare(x+3, y+3, Red,BR=15)
                createSquare(x+3, y+150, (204,0,0),BR=15)
                text = font.render("2", True, Black)
                surface.blit(text,(x + (miniX-text.get_width())//2,y + (miniY- text.get_height())//2))
               
                    
            elif item == 0:
                createSquare(x, y, (167, 232, 231))
                createSquare(x+3, y+3, (123, 179, 177),BR=15)
                
                
            else:
                createSquare(x, y, (167, 232, 231))
                createSquare(x+3, y+3, White,BR=15)
                createSquare(x+3, y+150, (255,178,102),BR=15)
                text = font.render(str(item), True, Black)
                surface.blit(text,(x + (miniX-text.get_width())//2,y + (miniY- text.get_height())//2))
                
        
            x += grid_node_width # for ever item/number in that row we move one "step" to the right 
        y += grid_node_height   # for every new row we move one "step" downwards
    pygame.display.update()    


visualizeGrid(miniX,miniY)  
#main loop of the game (key preeses)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            exit(0)
            break
        #back end starts:
        #making the mat copy for later
        mat_copy = []
        for t in range(n):
            mat_copy += [[0]*n]   
        for t in range(n):
            for k in range(n):
                mat_copy[t][k] = mat[t][k]
                
        key_input = pygame.key.get_pressed()        
        key = ""        
        if key_input[pygame.K_DOWN]:
            key = "D"
            for j in range(n):
                for z in range(n-1,-1,-1): #az paeen har setoon iterate kone byad bala
                    if z == n-1 or mat[z][j] == 0:  #agar satre akhar bood ke ja nadare va kolanam agar be 0 residim skip konim
                        continue
                    if mat[z+1][j] == 0: #agar ziresh khali bood ke ye doone byad paeen
                        (mat[z][j],mat[z+1][j]) = (mat[z+1][j],mat[z][j])
                    elif mat[z][j] == mat[z+1][j] and mat[z][j] != 1 and mat[z][j] != 2: #agar ba paeeni mosavi bood ke edgham shan
                        mat[z][j] = 0
                        mat[z+1][j] = (mat[z+1][j])*2
                    elif (mat[z][j] == 1 and mat[z+1][j] == 2) or (mat[z][j] == 2 and mat[z+1][j] == 1): # agar 2 va 1 boodan kenar ham
                        mat[z][j] = 0
                        mat[z+1][j] = 2+1  #intori minvisiam ke bedoonim jame 3 az koja oomade
                    else:
                        continue
                        
            
        elif key_input[pygame.K_UP]:
            key = "U"
            for j in range(n):
                for z in range(n):
                    if z == 0 or mat[z][j] == 0: #agar satr aval bashe ke bala neitoone bere va kolan age khali bood khune he skip kone
                        continue
                    if mat[z-1][j] == 0: #agar balash khali bood
                        (mat[z-1][j],mat[z][j]) = (mat[z][j],mat[z-1][j])
                    elif (mat[z][j] == mat[z-1][j]) and mat[z][j] != 2 and mat[z][j] != 1: #agar ba balee mosavi bood
                        mat[z][j] = 0
                        mat[z-1][j] = (mat[z-1][j])*2
                    elif (mat[z][j] == 1 and mat[z-1][j] == 2) or (mat[z][j] == 2 and mat[z-1][j] == 1):
                        mat[z][j] = 0
                        mat[z-1][j] = 2+1
                    else:
                        continue
            
            
        elif key_input[pygame.K_RIGHT]:
            key = "R"
            for j in range(n):
                for z in range(n-1,-1,-1):
                    if z == n-1 or mat[j][z] == 0:
                        continue
                    if mat[j][z+1] == 0:
                        (mat[j][z],mat[j][z+1]) = (mat[j][z+1],mat[j][z])
                    elif (mat[j][z] == mat[j][z+1]) and mat[j][z] != 2 and mat[j][z] != 1:
                        mat[j][z] = 0
                        mat[j][z+1] = (mat[j][z+1])*2
                    elif (mat[j][z] == 1 and mat[j][z+1] == 2) or (mat[j][z] == 2 and mat[j][z+1] == 1):
                        mat[j][z] = 0
                        mat[j][z+1] = 2+1
                    else:
                        continue
        
        
        elif key_input[pygame.K_LEFT]:
            key = "L"
            for j in range(n):
                for z in range(n):
                    if z == 0 or mat[j][z] == 0: #agar setoone aval bashe ke chap nemitoone bere agaram be sefr residim skip mikonim
                        continue
                    if mat[j][z-1] == 0: #agar chapesh khali bood
                        (mat[j][z],mat[j][z-1]) = (mat[j][z-1],mat[j][z])
                    elif (mat[j][z] == mat[j][z-1]) and mat[j][z] != 2 and mat[j][z] != 1: #agar ba chapish barabar bood
                        mat[j][z] = 0
                        mat[j][z-1] = (mat[j][z-1])*2
                    elif (mat[j][z] == 1 and mat[j][z-1] == 2) or (mat[j][z] == 2 and mat[j][z-1] == 1): #agar 1 va 2 boodan
                        mat[j][z] = 0
                        mat[j][z-1] = 2+1
                    else:
                        continue
                    
        
        if mat != mat_copy:
            
            if key == "D":  #add to satr aval
                m = 0 # tedad khune khali dar satr marboote bade taghir
                place_dict = []  #index esh mese key dict amal mikone 
                for c in range(n):
                    if mat[0][c] == 0:
                        m += 1
                        place_dict += [c]
                place =  random.randint(0,3)% m   #place o min khune i ke sefre va adad jadid bayad gharar begire toosh    
                d = random.randint(0,3)   #adad jadidi ke bayad gharar begire
                mat[0][place_dict[place]] = d #gharar dadan adad
                
                
            
            if key == "L": #add to setoon akhar
                m = 0 # tedad khune khali dar setoone marboote bade taghir
                place_dict = []  #index esh mese key dict amal mikone 
                for c in range(n):
                    if mat[c][n-1] == 0:
                        m += 1
                        place_dict += [c]
                place = random.randint(0,3) % m   #place o min khune i ke sefre va adad jadid bayad gharar begire toosh    
                d = random.randint(0,3)   #adad jadidi ke bayad gharar begire
                mat[place_dict[place]][n-1] = d
            
            if key == "U": #add to satr akhar
                m = 0 # tedad khune khali dar satr marboote bade taghir
                place_dict = []  #index esh mese key dict amal mikone 
                for c in range(n):
                    if mat[n-1][c] == 0:
                        m += 1
                        place_dict += [c]
                place = random.randint(0,3) % m   #place o min khune i ke sefre va adad jadid bayad gharar begire toosh    
                d = random.randint(0,3)   #adad jadidi ke bayad gharar begire
                mat[n-1][place_dict[place]] = d
            
            
            if key == "R": #add to setoon aval
                m = 0 # tedad khune khali dar satr marboote bade taghir
                place_dict = []  #index esh mese key dict amal mikone 
                for c in range(n):
                    if mat[c][0] == 0:
                        m += 1
                        place_dict += [c]
                place = random.randint(0,3) % m   #place o min khune i ke sefre va adad jadid bayad gharar begire toosh    
                d = random.randint(0,3)    #adad jadidi ke bayad gharar begire
                mat[place_dict[place]][0] = d
        
        visualizeGrid(miniX,miniY) #visualizing on pygame
        
        if finished():
            flag = True
             #printing the result matrix and calculating the result score
            score = 0            
            for i in range(n):
                for j in range(n):
                    x = mat[i][j]
                    if x != 1 and x != 2 and x != 0:
                        count = 0
                        while x%2==0:
                            count += 1
                            x = x//2 
                        score += 3**(count+1)
                      
            surface.fill(White)
            text = font.render("The final", True, Black)
            surface.blit(text,((size[0]-text.get_width())//2, (size[1]- text.get_height())//2-100))
            text = font.render("score is", True, Black)
            surface.blit(text,((size[0]-text.get_width())//2, (size[1]- text.get_height())//2))
            text = font.render(str(score), True, Black)
            surface.blit(text,((size[0]-text.get_width())//2, (size[1]- text.get_height())//2+100))
            pygame.display.update()  #to visualize the score
            
    
            
            
        
                        
