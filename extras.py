import struct
from vector import *
from textures import *
import random

def shaders(renderizado, **kwargs):
    y = kwargs['aaa']
    numero = random.randint(0, 10)
    if(y<1024 and y>=774) and numero != 2:
        #Amarillo
        return color(93, 109, 126 )
    elif(y<774 and y>=734) and numero != 2:
        #Amarillo
        return color(46, 64, 83)
    elif(y<734 and y>=650) and numero != 2:
        #Amarillo
        return color(185, 119, 14 )
    elif(y<650 and y>=625) and numero != 2:
        #Bashe
        return color(240, 178, 122 )
    elif(y<625 and y>=575) and numero != 2:
        #Naranja
        return color(214, 137, 16)
    elif(y<575 and y>=450) and numero != 2:
        #Bashe
        return color(240, 178, 122 )
    elif(y<450 and y>=430) and numero != 2:
        #Cafe
        return color(185, 119, 14 )
    elif(y<430 and y>=375) and numero != 2:
        #Bashe
        return color(240, 178, 122 )
    elif(y<374 and y>=325) and numero != 2:
        #Cafe
        return color(229, 152, 102 )
    elif(y<325 and y>=275) and numero != 2:
        #Gris Oscuro
        return color(46, 64, 83)
    elif(y<275 and y>=250) and numero != 2:
        #Gris
        return color(93, 109, 126 )
    else:
        #Negro
        return color(0,0,0)

    # w, u, v = kwargs['bar']
    # L = V3(1,0,1)
    # A, B, C = kwargs['vertices']
    # tA, tB, tC = kwargs['texture_coords']
    # nA, nB, nC = kwargs['normals']

    # # print(str(type(nA)),str(type(nB)),str(type(nC)))



    # if renderizado.texture:
    #     iA = nA.normalize() @ L.normalize()

    #     iB = nB.normalize() @ L.normalize()

    #     iC = nC.normalize() @ L.normalize()


    #     i = iA * w + iB * u + iC * v

    #     tx = tA.x * w + tB.x * u + tC.x * v
    #     ty = tA.y * w + tB.y * u + tC.y * v

    #     r,g,b = renderizado.texture.GetColorIntensity(tx,ty,i)

    #     return color(b,g,r)
    # else:

    #     iA = nA.normalize() @ L.normalize()

    #     iB = nB.normalize() @ L.normalize()

    #     iC = nC.normalize() @ L.normalize()


    #     i = iA * w + iB * u + iC * v

    #     rojo    = round(255*i)
    #     verde   = round(255*i)
    #     azul    = round(255*i)

    #     return color(max(min(rojo,255),0),max(min(verde,255),0) ,max(min(azul,255),0))

        # normal_triangulo =  (C-A) * (B-A)
        # # print(str(type(normal_triangulo)))
        # # print(str(type(L.normalize())))

        # i = L.normalize() @ normal_triangulo.normalize()

        # print(normal_triangulo.normalize())
        # if i < 0:
        #     return
        # rojo    = round(255*i)
        # verde   = round(255*i)
        # azul    = round(255*i)
        # return color(max(min(rojo,255),0),max(min(verde,255),0) ,max(min(azul,255),0))

def bounding_box(A,B,C):
    coors = [(A.x, A.y), (B.x, B.y), (C.x, C.y)]

    xmin = 999999
    xmax = -999999
    ymin = 999999
    ymax = -999999

    for (x,y) in coors:
        if x < xmin:
            xmin = x
        if x > xmax:
            xmax = x
        if y < ymin:
            ymin = y
        if y > ymax:
            ymax = y

    return V3(xmin, ymin), V3(xmax, ymax)

def mul_externa(v0,v1):
    return(
        v0.y * v1.z - v0.z * v1.y,
        v0.z * v1.x - v0.x * v1.z,
        v0.x * v1.y - v0.y * v1.x
    )

def barycentric(A,B,C,P):
    cx,cy, cz = mul_externa(
                    V3(B.x - A.x, C.x - A.x, A.x-P.x),
                    V3(B.y - A.y, C.y - A.y, A.y-P.y) )

    if cz == 0:
        u = 0
        v = 0
        w = 0.0001
    else:
        u = cx/cz
        v = cy/cz
        w = 1-(u+v)

    return(w,v,u)

def color(r,g,b):
    return bytes([b, g, r])

def dword(d):
    #4bytes
    return struct.pack('=l', d)

def word(w):
    #2bytes
    return struct.pack('=h', w)

def char(c):
    #1 byte
    return struct.pack('=c', c.encode('ascii'))


