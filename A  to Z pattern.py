# # A

# row=0
# while row<5:
#     column=0
#     while column <5:
#         if (row==0 and column%4!=0) or (row==3 and column%4!=0) or (row!=0 and column==0)or (row!=0 and column ==4):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#         column+=1
#     row+=1
#     print()

# # B

# for row in range(7):
#     for column in range(5):
#         if (column==0) or (column!=4 and row==0) or (column!=4 and row==3) or (column!=4 and row==6) or (column==4 and row%6!=0) or (column==4 and row%6!=0):
#                 print("*", end=" ")
#         else:
#             print(" ", end=" ")

#     print()        

# # C

# for  i in range(7):
#     for  j in range(5):
#         if j==0 or i==0 or i==6:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
    
# # D
# for  i in range(7):
#     for  j in range(5):
#         if (j==0) or (i==0 and j%4!=0) or (i==6 and j%4!=0) or (i%6!=0 and j==4):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# # E

# for  i in range(7):
#     for  j in range(5):
#         if (j==0) or (i==0) or (i==3) or (i==6):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# # F

# for  i in range(7):
#     for  j in range(5):
#         if (j==0) or (i==0) or (i==3):
#             print("#", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# # G
# for  i in range(7):
#     for  j in range(5):
#         if (j==0) or (i==0) or (i==6) or (j!=1 and i==4) or (i==5 and j==4):
#             print("#", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# # H

# for  i in range(7):
#     for  j in range(5):
#         if (j==0) or (j==4) or (i==3 and j%4!=0):
#             print("#", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# # I
# for  i in range(7):
#     for  j in range(5):
#         if j==0:
#             print("#", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# # J

# for  i in range(7):
#     for  j in range(5):
#         if (i==0) or (j==2) or (i>2 and j==0):
#             print("#", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# # K

# for  i in range(7):
#     for  j in range(5):
#         if (j==0) or (i+j==3) or (i-j==3):
#             print("#", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# # L

# for  i in range(7):
#     for  j in range(5):
#         if (j==0) or (i==6):
#             print("#", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# # M

# for  i in range(5):
#     for  j in range(5):
#         if (j==0) or (j==4) or (i==1 and j==1) or (i==2 and j==2) or (i==1 and j==3):
#             print("#", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# # N

# for  i in range(5):
#     for  j in range(5):
#         if (j==0) or (j==4) or (i==j):
#             print("#", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# # O

# for  i in range(7):
#     for  j in range(5):
#         if (i==0 and j%4!=0) or (i==6 and j%4!=0) or (i%6!=0 and j==0) or (i%6==0 and j==4):
#             print("#", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# # P

# for  i in range(7):
#     for  j in range(5):
#         if (j==0) or (j!=4 and i==0) or(i==3 and j!=4) or (i==1 and j==4) or (i==2 and j==4):
#             print("#", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# # Q

# for  i in range(7):
#     for  j in range(5):
#         if (i==0 and j%4!=0) or (i==6 and j%4!=0) or (i%6!=0 and j==0) or(i%6!=0 and j==4) or (i==4 and j==2) or(i==5 and j==3):
#             print("#", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# # R
# for  i in range(7):
#     for  j in range(5):
#         if (j==0) or (j!=4 and i==0) or (i==3 and j!=4) or (i==1 and j==4) or(i-j==2):
#             print("#", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# # S
# for  i in range(7):
#     for  j in range(5):
#         if (i==0 and j!=0) or (i==6 and j!=4) or (i==3 and j%4!=0) or(i==1 and j==0) or (i==2 and j==0) or(i==4 and j==4) or (i==5 and j==4):
#             print("#", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# # T
# for  i in range(6):
#     for  j in range(5):
#         if (i==0) or (j==2):
#             print("#", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# # U
# for  i in range(7):
#     for  j in range(5):
#         if (i==6 and j%4!=0) or (j==0) or (j==4):
#             print("#", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# # V
# for  i in range(7):
#     for  j in range(5):
#         if (i==0 and j==0) or (i==0 and j==4) or (i==2 and j==0) or(i==2 and j==4) or (i==4 and j==1) or(i==4 and j==3) or (i==6 and j==2):
#             print("#", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# # W
# for  i in range(7):
#     for  j in range(5):
#         if (j==0) or (j==4) or (i==4 and j==2) or (i==5 and j==1) or(i==5 and j==3):
#             print("#", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# # x
# for  i in range(5):
#     for  j in range(5):
#         if (i==j) or (i+j==4):
#             print("#", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# # Y
# for  i in range(7):
#     for  j in range(5):
#         if ((i==j==1) or(i==j==0)) or (i+j==4):
#             print("#",end=" ")
#         else:
#             print(" ", end=" ")
#     print()     

# # Z
# for  i in range(7):
#     for  j in range(5):
#         if (i==0) or(i==6) or (i+j==5):
#             print("#",end=" ")
#         else:
#             print(" ", end=" ")
#     print()     








