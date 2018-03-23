
try:
    1/0
except Exception as e:
    print("异常信息")
finally:
    print("finally")