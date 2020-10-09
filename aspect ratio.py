#Exercise 4

def calc_new_height():
    w = int(input('Enter current width: '))
    h = int(input('Enter current height: '))
    new_w = int(input('Enter desired width: '))
    return new_h(w, h, new_w)


def new_h(w, h, new_w):
    ratio = new_w / w
    new_h = h * ratio
    return new_h

desired_height = calc_new_height()

print ('The corresponding height is: ', desired_height)
print(desired_height)
