from Object import *
import gl
from vector import *
from textures import *
import MatricesSimuladas as MatrizSimulada


def crear():


    scale_factor = (500,500,600)
    translate_factor = (525, 500,0)

    cube = Obj('./Objts/sphere.obj')

    # scale_factor = (12,12,12)
    # translate_factor = (500, 50,0)

    # cube = Obj('Bigmax_White_Obj')

    for face in cube.faces:
        f1 = face[0][0] - 1
        f2 = face[1][0] - 1
        f3 = face[2][0] - 1

        v1 = transform_vertex(cube.vertices[f1], scale_factor, translate_factor)
        v2 = transform_vertex(cube.vertices[f2], scale_factor, translate_factor)
        v3 = transform_vertex(cube.vertices[f3], scale_factor, translate_factor)

        if len(face) == 4:

            f4 = face[3][0] - 1
            v4 = transform_vertex(cube.vertices[f4], scale_factor, translate_factor)

            gl.glLine3(v1[0][0], v1[0][1], v2[0][0],v2[0][1])
            gl.glLine3(v2[0][0], v2[0][1], v3[0][0],v3[0][1])
            gl.glLine3(v3[0][0], v3[0][1], v4[0][0],v4[0][1])
            gl.glLine3(v4[0][0], v4[0][1], v1[0][0],v1[0][1])

        elif len(face) == 3:


            gl.glLine3(v1[0][0], v1[0][1], v2[0][0],v2[0][1])
            gl.glLine3(v2[0][0], v2[0][1], v3[0][0],v3[0][1])
            gl.glLine3(v3[0][0], v3[0][1], v1[0][0],v1[0][1])

def transform_vertex(vertex, scale, translate):

    return [
        (
            (vertex[0] * scale[0]) + translate[0], #X.
            (vertex[1] * scale[1]) + translate[1] #Y.
        )
    ]

def transform_vertex_v3(vertex, scale, translate):

    return V3(
            (vertex[0] * scale[0]) + translate[0], #X.
            (vertex[1] * scale[1]) + translate[1], #Y.
            (vertex[2] * scale[2]) + translate[2] #Z.
    )

def crear_v3():
    renderizado = gl.RenderizadoFuncio()

    # #Bmax
    # scale_factor = (12,12,12)
    # translate_factor = (500, 50,0)
    # cube = Obj(',/Bigmax_White_Obj.obj')


    # # taza
    # scale_factor = (9,9,10)
    # translate_factor = (500, 50,0)
    # cube = Obj(',/taza.obj')

    #Cara Clase
    scale_factor = (450,450,600)
    translate_factor = (525, 500,0)
    cube = Obj('./Objts/model.obj')
    renderizado.texture = Texture('./Textrs/model.bmp')

    # #Perro
    # scale_factor = (2000,2000,3000)
    # translate_factor = (850, 150,0)
    # cube = Obj('./Objts/Perro.obj')
    # renderizado.texture = Texture('./Textrs/Shiba.bmp')



    # # kakashi
    # scale_factor = (9,9,10)
    # translate_factor = (500, 50,0)
    # cube = Obj('./kakashi.obj')

    # # woman
    # scale_factor = (1,1,1)
    # translate_factor = (500, 500,0)
    # cube = Obj('./woman.obj')

    # # Faraon
    # scale_factor = (125,125,250)
    # translate_factor = (525, 50,0)
    # cube = Obj('faraon.obj')

    # # Mascara
    # scale_factor = (3000,3000,3000)
    # translate_factor = (7150,50,0)
    # cube = Obj('./Objts/Mask.obj')
    # renderizado.texture = Texture('./Textrs/Mask3.bmp')

    # # Caballo
    # scale_factor = (0.5,0.5,1)
    # translate_factor = (500,600,0)
    # cube = Obj('./Objts/juan.obj')
    # renderizado.texture = Texture('./Textrs/juan.bmp')
    # gl.EscrituraSobreTextura('./Objts/madara.obj','./Textrs/madara.bmp')

    # # Pato
    # scale_factor = (15,15,30)
    # translate_factor = (500,400,0)
    # cube = Obj('./Objts/Pato.obj')
    # renderizado.texture = Texture('./Textrs/Pato.bmp')
    # gl.EscrituraSobreTextura('./Objts/Pato.obj','./Textrs/Pato.bmp')

    # # Gato
    # scale_factor = (15,15,10)
    # translate_factor = (500,400,0)
    # cube = Obj('./Objts/Gato.obj')
    # renderizado.texture = Texture('./Textrs/Gato.bmp')
    # gl.EscrituraSobreTextura('./Objts/Gato.obj','./Textrs/Gato.bmp')

    for face in cube.faces:
        f1 = face[0][0] - 1
        f2 = face[1][0] - 1
        f3 = face[2][0] - 1

        v1 = transform_vertex_v3(cube.vertices[f1], scale_factor, translate_factor)
        v2 = transform_vertex_v3(cube.vertices[f2], scale_factor, translate_factor)
        v3 = transform_vertex_v3(cube.vertices[f3], scale_factor, translate_factor)

        if len(face) == 4:

            f4 = face[3][0] - 1
            v4 = transform_vertex_v3(cube.vertices[f4], scale_factor, translate_factor)

            if renderizado.texture:
                ft1 = face[0][1] - 1
                ft2 = face[1][1] - 1
                ft3 = face[2][1] - 1
                ft4 = face[3][1] - 1

                vt1 = V3(*cube.tvertices[ft1])
                vt2 = V3(*cube.tvertices[ft2])
                vt3 = V3(*cube.tvertices[ft3])
                vt4 = V3(*cube.tvertices[ft3])

                gl.triangulo_version_dos_textura((v1,v2,v3),(vt1,vt2,vt3))
                gl.triangulo_version_dos_textura((v1,v3,v4),(vt1,vt3,vt3))
            else:
                gl.triangulo_version_dos_textura((v1,v2,v3))
                gl.triangulo_version_dos_textura((v1,v3,v4))
            # gl.triangulo_version_dos(v1,v2,v3)
            # gl.triangulo_version_dos(v1,v3,v4)

            # gl.glLine3(v1[0][0], v1[0][1], v2[0][0],v2[0][1])
            # gl.glLine3(v2[0][0], v2[0][1], v3[0][0],v3[0][1])
            # gl.glLine3(v3[0][0], v3[0][1], v4[0][0],v4[0][1])
            # gl.glLine3(v4[0][0], v4[0][1], v1[0][0],v1[0][1])


        elif len(face) == 3:
            # gl.triangulo_version_dos(v1,v2,v3)
            # gl.glLine3(v1[0][0], v1[0][1], v2[0][0],v2[0][1])
            # gl.glLine3(v2[0][0], v2[0][1], v3[0][0],v3[0][1])
            # gl.glLine3(v3[0][0], v3[0][1], v1[0][0],v1[0][1])

            if renderizado.texture:
                ft1 = face[0][1] - 1
                ft2 = face[1][1] - 1
                ft3 = face[2][1] - 1

                vt1 = V3(*cube.tvertices[ft1])
                vt2 = V3(*cube.tvertices[ft2])
                vt3 = V3(*cube.tvertices[ft3])
                gl.triangulo_version_dos_textura((v1,v2,v3),(vt1,vt2,vt3))

            else:
                gl.triangulo_version_dos_textura((v1,v2,v3))

def transform_vertex_robusto(vertex):
    renderizado = gl.RenderizadoFuncio()
    # augmented_vertex = [c
    #     vertex[0],
    #     vertex[1],
    #     vertex[2],
    #     1
    # ]
    augmented_vertex = MatrizSimulada.matrix([[vertex[0]],[vertex[1]],[vertex[2]],[1]])
    transformed_vertex = renderizado.ViewPort @ renderizado.Projection @renderizado.View @ renderizado.Model @ augmented_vertex
    divisor = transformed_vertex.obtener_valor_unico(3,0)
    return V3(
        transformed_vertex.obtener_valor_unico(0,0)/divisor,
        transformed_vertex.obtener_valor_unico(1,0)/divisor,
        transformed_vertex.obtener_valor_unico(2,0)/divisor,

    )

def crear_robusto(Objeto, Textura,translate, scale, rotate):
    renderizado = gl.RenderizadoFuncio()
    # # Gato
    # scale_factor = (15,15,10)
    # translate_factor = (500,400,0)
    # rotate = (-pi/3,0,0)

    # renderizado.lookAt(V3(0,0,10), V3(0,0,0), V3(0,1,0))

    # renderizado.loadModelMatrix(translate_factor,scale_factor,rotate)
    # cube = Obj('./Objts/Gato.obj')
    # renderizado.texture = Texture('./Textrs/Gato.bmp')
    # gl.EscrituraSobreTextura('./Objts/Gato.obj','./Textrs/Gato.bmp')



    # #Bmax
    # scale_factor = (12,12,12)
    # translate_factor = (500, 50,0)
    # cube = Obj(',/Bigmax_White_Obj.obj')


    # # taza
    # scale_factor = (9,9,10)
    # translate_factor = (500, 50,0)
    # cube = Obj(',/taza.obj')

    #Cara Clase
    # scale_factor = (450,450,600)
    # translate_factor = (525, 500,0)
    # rotate = (0,0,0)

    renderizado.loadModelMatrix(translate,scale,rotate)
    cube = Obj(Objeto)
    if Textura == None:
        renderizado.texture = None
    else:
        renderizado.texture = Texture(Textura)
    # #Perro
    # scale_factor = (2000,2000,3000)
    # translate_factor = (850, 150,0)
    # cube = Obj('./Objts/Perro.obj')
    # renderizado.texture = Texture('./Textrs/Shiba.bmp')



    # # kakashi
    # scale_factor = (9,9,10)
    # translate_factor = (500, 50,0)
    # cube = Obj('./kakashi.obj')

    # # woman
    # scale_factor = (1,1,1)
    # translate_factor = (500, 500,0)
    # cube = Obj('./woman.obj')

    # # Faraon
    # scale_factor = (125,125,250)
    # translate_factor = (525, 50,0)
    # cube = Obj('faraon.obj')

    # # Mascara
    # scale_factor = (3000,3000,3000)
    # translate_factor = (7150,50,0)
    # cube = Obj('./Objts/Mask.obj')
    # renderizado.texture = Texture('./Textrs/Mask3.bmp')

    # # Caballo
    # scale_factor = (0.5,0.5,1)
    # translate_factor = (500,600,0)
    # cube = Obj('./Objts/juan.obj')
    # renderizado.texture = Texture('./Textrs/juan.bmp')
    # gl.EscrituraSobreTextura('./Objts/madara.obj','./Textrs/madara.bmp')

    # # Pato
    # scale_factor = (15,15,30)
    # translate_factor = (500,400,0)
    # cube = Obj('./Objts/Pato.obj')
    # renderizado.texture = Texture('./Textrs/Pato.bmp')
    # gl.EscrituraSobreTextura('./Objts/Pato.obj','./Textrs/Pato.bmp')


    for face in cube.faces:
        f1 = face[0][0] - 1
        f2 = face[1][0] - 1
        f3 = face[2][0] - 1

        v1 = transform_vertex_robusto(cube.vertices[f1])
        v2 = transform_vertex_robusto(cube.vertices[f2])
        v3 = transform_vertex_robusto(cube.vertices[f3])

        if len(face) == 4:

            f4 = face[3][0] - 1
            v4 = transform_vertex_robusto(cube.vertices[f4])


            ft1 = face[0][1] - 1
            ft2 = face[1][1] - 1
            ft3 = face[2][1] - 1
            ft4 = face[3][1] - 1

            vt1 = V3(*cube.tvertices[ft1])
            vt2 = V3(*cube.tvertices[ft2])
            vt3 = V3(*cube.tvertices[ft3])
            vt4 = V3(*cube.tvertices[ft4])

            fn1 = face[0][2] - 1
            fn2 = face[1][2] - 1
            fn3 = face[2][2] - 1
            fn4 = face[3][2] - 1

            vn1 = V3(*cube.tvertices[fn1])
            vn2 = V3(*cube.tvertices[fn2])
            vn3 = V3(*cube.tvertices[fn3])
            vn4 = V3(*cube.tvertices[fn4])

            gl.triangulo_version_dos_textura((v1,v2,v3),(vt1,vt2,vt3),(vn1,vn2,vn3))
            gl.triangulo_version_dos_textura((v1,v3,v4),(vt1,vt3,vt4),(vn1,vn3,vn4))
            # gl.triangulo_version_dos((v1,v2,v3))
            # gl.triangulo_version_dos((v1,v3,v4))

            # gl.glLine3(v1[0][0], v1[0][1], v2[0][0],v2[0][1])
            # gl.glLine3(v2[0][0], v2[0][1], v3[0][0],v3[0][1])
            # gl.glLine3(v3[0][0], v3[0][1], v4[0][0],v4[0][1])
            # gl.glLine3(v4[0][0], v4[0][1], v1[0][0],v1[0][1])


        elif len(face) == 3:
            # gl.triangulo_version_dos(v1,v2,v3)
            # gl.glLine3(v1[0][0], v1[0][1], v2[0][0],v2[0][1])
            # gl.glLine3(v2[0][0], v2[0][1], v3[0][0],v3[0][1])
            # gl.glLine3(v3[0][0], v3[0][1], v1[0][0],v1[0][1])


            ft1 = face[0][1] - 1
            ft2 = face[1][1] - 1
            ft3 = face[2][1] - 1

            vt1 = V3(*cube.tvertices[ft1])
            vt2 = V3(*cube.tvertices[ft2])
            vt3 = V3(*cube.tvertices[ft3])


            fn1 = face[0][2] - 1
            fn2 = face[1][2] - 1
            fn3 = face[2][2] - 1

            vn1 = V3(*cube.tvertices[fn1])
            vn2 = V3(*cube.tvertices[fn2])
            vn3 = V3(*cube.tvertices[fn3])

            gl.triangulo_version_dos_textura((v1,v2,v3),(vt1,vt2,vt3),(vn1,vn2,vn3))
            # gl.triangulo_version_dos((v1,v2,v3))
