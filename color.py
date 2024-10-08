from vector import Vector # type: ignore

class Color(Vector):
    """stores color as rgb triplets . an alias for vector"""
    @classmethod
    def from_hex(cls, hexcolor="#000000"):
        x= int(hexcolor[1:3], 16) /255.0
        y= int(hexcolor[3:5], 16) /255.0
        z= int(hexcolor[5:7], 16) /255.0
        return cls(x,y,z)
    