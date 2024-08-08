from color import Color # type: ignore
from vector import Vector # type: ignore
from point import Point # type: ignore
from sphere import Sphere # type: ignore
from light import Light # type: ignore
from material import Material, ChequeredMaterial # type: ignore

WIDTH = 960
HEIGHT = 540
RENDERED_IMG = "7balls.ppm"
CAMERA = Vector(0, -0.35, -1)

OBJECTS = [
    # Sphere 1 with Chequered Material
    Sphere(Point(0, 10000.5, 1), 10000.0, ChequeredMaterial(color1=Color.from_hex("#FF0000"), color2=Color.from_hex("#FFFF00"), ambient=0.2, reflection=0.2)),

    # Sphere 2 - Blue
    Sphere(Point(1.5, -0.2, 3), 0.4, Material(Color.from_hex("#0000FF"))),

    # Sphere 3 - Green
    Sphere(Point(-1.5, 0.3, 2.5), 0.4, Material(Color.from_hex("#00FF00"))),

    # Sphere 4 - Purple
    Sphere(Point(0.5, 1.0, 1.75), 0.3, Material(Color.from_hex("#800080"))),

    # Sphere 5 - Orange
    Sphere(Point(-0.5, -1.0, 3.5), 0.5, Material(Color.from_hex("#FFA500"))),

    # Sphere 6 - Cyan
    Sphere(Point(1.0, 0.5, 2.0), 0.35, Material(Color.from_hex("#00FFFF"))),

    # Sphere 7 - Pink
    Sphere(Point(-1.0, -0.8, 2.2), 0.45, Material(Color.from_hex("#FFC0CB")))
]

LIGHTS = [
    Light(Point(1.5, -0.5, -10), Color.from_hex("#FFFFFF")),
    Light(Point(-0.5, -10.5, 0), Color.from_hex("#FFFFFF"))
]
