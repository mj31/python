
class Learn(object):
    def test(self,x=1):
        return x
    def demo(self,**kwargs):
        return kwargs


print(Learn().demo(name="张飒喊",age=12))