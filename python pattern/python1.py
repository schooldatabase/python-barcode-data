import time
n = 5
print("########################################")
def right_angle_triangle1(n):
     
    for i in range(1, n + 1):
        # time.sleep(1)
        print(i , end =" = ")
        # print()
        for j in range(i):
            # print(j, end=" ")
            print("*", end ="")
        print()
# n = int(input("Enter a number = "))   
right_angle_triangle1(n)
 
print()