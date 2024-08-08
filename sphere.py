from math import sqrt

class Sphere:
    """only 3D shape implemented. has radius center and material"""

    def __init__(self,center,radius,material):
        self.center= center
        self.radius= radius
        self.material =material

    def intersects(self, ray):
        """checks if ray intersects sphere. returns distance to intersection or none if theres no intersection"""
        sphere_to_ray= ray.origin - self.center
        #a=1
        b=2*ray.direction.dot_product(sphere_to_ray)
        c= sphere_to_ray.dot_product(sphere_to_ray) - self.radius * self.radius
        discriminant = b*b - 4*c

        if discriminant >=0:
            dist= (-b - sqrt(discriminant)) /2
            if dist>0:
                return dist
        return None
    
    def normal(self,surface_point):
        """returns surface normal to the point on spheres surface"""
        return (surface_point - self.center).normalize()