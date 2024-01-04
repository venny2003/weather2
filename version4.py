n = int(input("Enter the value"))
for i in range(0,n):
    T = int(input("Enter the Temp"))
    H = int(input("Enter the Humidit"))
    w = int(input("Enter the cloudy"))
    W=(0.5)*(T**2)-(0.2)*H+(0.1)*w-15
    if W>300:
        ans = "Sunny"
    elif 200<W<=300:
        ans = "Cloudy"
    elif 100<W<=200:
        ans = "Rainy"
    else:
        ans = "Stormy"

    print(W)
