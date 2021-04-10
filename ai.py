from PIL import Image

#code from web
img = Image.open('test.png').convert('L')
width, height = img.size
data = list(img.getdata())
data = [data[offset:offset+width] for offset in range(0, width*height, width)]

#input layor
x = [data[0][0] // 255, data[0][1] // 255, data[1][0] // 255, data[1][1] // 255]

#weights
w = [[[1, -1, -1, 1],[-1, 1, 1, -1]],[[1, -1],[-1, 1],[1, 1]]]

#biases
b = [[0, 0],[0, 0, 3]]

#hidden layor 1
y = [x[0] * w[0][0][0] + x[1] * w[0][0][1] + x[2] * w[0][0][2] + x[3] * w[0][0][3] + b[0][0],
     x[0] * w[0][1][0] + x[1] * w[0][1][1] + x[2] * w[0][1][2] + x[3] * w[0][1][3] + b[0][1]]

#hidden layor 2
z = [y[0] * w[1][0][0] + y[1] * w[1][0][1] + b[1][0], y[0] * w[1][1][0] + y[1] * w[1][1][1] + b[1][1], y[0] * w[1][2][0] + y[1] * w[1][2][1] + b[1][2]]

#output, checks which of the neurons from hidden layor 2 that is largest
if z[0] > z[1] and z[0] > z[2]:
    print("it's a checkerboard pattern like this:")
    print("X..")
    print("..X")

if z[0] < z[1] and z[2] < z[1]:
    print("it's a checkerboard pattern like this:")
    print("..X")
    print("X..")

if z[0] < z[2] and z[2] > z[1]:
        print("it's NOT a checkerboard pattern")