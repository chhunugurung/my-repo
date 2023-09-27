num=0
sum=0
count=0
average=0
while True:
    num=input("done")
    if num=="done":
        break
    try:
        input_num=float(num)
        sum=sum + input_num
        count=count + 1
    except:
        print(" enter only numbers or type done to end")
        if count == 0:
            print(" you cannot proceed")
            break
average=sum/count       
print("sum of the number is",sum)
print("count of the number is",count)
print("average of the number is",average)

