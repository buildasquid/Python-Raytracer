from color import Color # type: ignore
from vector import Vector # type: ignore
from point import Point # type: ignore
from sphere import Sphere # type: ignore
from light import Light # type: ignore
from material import Material # type: ignore

WIDTH = 960
HEIGHT = 540
RENDERED_IMG = "traffic_lights.ppm"
CAMERA = Vector(0, -0.35, -1)

OBJECTS = [
     # Red Sphere 
    Sphere(Point(0, 1.75, 2.0), 0.5, Material(Color.from_hex("#FF0000"))),

    # Yellow Sphere 
    Sphere(Point(0, 0.75, 2.0), 0.5, Material(Color.from_hex("#FFFF00"))),

    # Green Sphere 
    Sphere(Point(0, -0.25, 2.0), 0.5, Material(Color.from_hex("#00FF00")))
]

LIGHTS = [
    Light(Point(1.5, -0.5, -10), Color.from_hex("#FFFFFF"))
    
]
