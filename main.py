#Gabriel Alejandro Vicente Lorenzo
#SR6 UVG

#Se importan los metodos solicitados por el ejercicios
import gl
import Creando
from vector import *
import extras as ex

gl.glInit()
#Se crea la Ventana (Que renderiza a.bmp)
gl.glCreateWindow(1024,1024)

renderizado = gl.RenderizadoFuncio()
#Camara
renderizado.lookAt(V3(0,0,10), V3(0,0,0), V3(0,1,0))

#Shader
renderizado.Shader = ex.shaders

#Modelo esfera clase
Creando.crear_robusto('./Objts/sphere-1.obj',None,translate = (0,0,0),scale = (1,1,1),rotate = (0,0,0))

gl.glFinish('a.bmp')
