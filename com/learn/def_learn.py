def test(x):
    if x > 10:
        print("我大于10")
    elif x < 10:
        print("我是小于10")
    else:
        print("等于10")
a = test(20)

def study(**arge):
    if arge["name"]=="张三":
        print("我的名字是张珊")
    elif arge["age"] == 20:
        print("我的年龄是20岁")
    else:
        print(arge.keys())

study(name="张三",age=20)

