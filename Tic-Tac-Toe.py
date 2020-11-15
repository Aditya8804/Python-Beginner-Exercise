#Follows a co-ordinate system with a,b,c for rows and 1,2,3 for columns
# Ex: to enter value in First square, enter a1 
pCount=False#P1-True,P2=False
posList={'a1':' ','a2':' ','a3':' ','b1':' ','b2':' ','b3':' ','c1':' ','c2':' ','c3':' '}
col,row=['1','2','3'],['a','b','c']
characters=['X','O']
print('start',posList['a1'])
def printer(): 
   print('      1     2     3')
   count=0
   while count<3:
      print("{}  {}  |  {}  |  {}  |".format(row[count],posList[f'{row[count]}{col[0]}'],posList[f'{row[count]}{col[1]}'],posList[f'{row[count]}{col[2]}']))
      count=count+1
def userInput():
   a=input(f'{"P1" if pCount else "P2"}, enter your position:')
   return a
def listChange(a):
   try:
      if posList[a]==' ':
         posList[a]=(characters[0] if pCount else characters[1]) 
   except(ValueError):
      print('Enter usable value')
      return False
   return True

def winCheck():
   winConfig=[['a1','a2','a3'],['b1','b2','b3'],['c1','c2','c3'],['a1','b2','c3'],['a3','b2','c1']]
   check=True
   for x in winConfig:
      check=True
      c=0
      while c<2 and check:
         check=(posList[x[c]]==posList[x[c+1]]) and posList[x[c]]!=' '
         c=c+1
      if check:
         break
   return check
      
def drawCheck():
   val=0
   for x in posList:
      if posList[x]==' ':
         val=val+1
   return(val==0)
val=True
printer()
while(not winCheck()):
   pCount=not pCount if val else pCount
   if drawCheck():
      print('Game Over: DRAW')
      break
   val=listChange(userInput())
   printer()
else:
   print(f'Game Over: {"P1" if pCount else "P2"} HAS WON!')
   #print(posList)
