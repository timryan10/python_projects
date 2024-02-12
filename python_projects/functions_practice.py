def hello():
    print("Hello user")
hello()

def pack(shirt, pants, socks):
    return [shirt, pants, socks]
print(pack("shirt", "pants", "socks"))

def eat_lunch(lunch):
    if len(lunch) == 0:
        print("My lunchbox is empty!")
    else:
        for i in range(len(lunch)):
            if i == 0:
                print(f"First I eat my {lunch[0]}")
            else: 
                print(f"Next I eat my {lunch[i]}")
eat_lunch([])
eat_lunch(["sandwich"])
eat_lunch(["fruit", "sandwhich", "desert"])

