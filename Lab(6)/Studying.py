def DrawShpe(hight):
   if hight == 1:
       return 1
   factorial =  hight * DrawShpe(hight-1)
   return factorial

print DrawShpe(5)