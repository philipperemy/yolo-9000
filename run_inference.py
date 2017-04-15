import os

if __name__ == '__main__':
    filename = '00115.jpg'
    request = './darknet detector test cfg/combine9k.data cfg/yolo9000.cfg weights/yolo9000.weights {}'.format(filename)
    print('->', request)
    os.system(request)
