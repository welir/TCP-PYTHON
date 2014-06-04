class Auto:
    color = 'red'
    model = 'bmw'
    a = 6
    def Gen(self, a):
        c = 2
        b = 3
        return b + pow(a, c)
    def Change_color(self, newcolor):
        self.color = newcolor
    def change_model(self,newmodel):
        self.model = newmodel
def print_array(array):
    for i in range(1):
        print(array[i].color)
        print(array[i].model)
ford = [Auto() for x in range(1)]

ford[0].Change_color('black')
ford[0].Gen(4)
ford[0].change_model('ford')

print_array(ford)