import guerilla
import math

cam = guerilla._('NewCamera')

cam_near = cam.Near.get()
cam_far = cam.Far.get()
cam_fov = cam.Fov.get()
cam_matrix = cam.getworldmatrix().asarray()

class Vector(object):
    def __init__(self , array):
        self.x = array[0]
        self.y = array[1]
        self.z = array[2]

    def __add__(self , other):
        other = self.checkOtherType(other)
        new_vec = Vector((0,0,0))
        new_vec.x = self.x + other.x
        new_vec.y = self.x + other.y
        new_vec.z = self.z + other.z
        return new_vec

    def __sub__(self , other):
        other = self.checkOtherType(other)
        new_vec = Vector((0,0,0))
        new_vec.x = self.x - other.x
        new_vec.y = self.x - other.y
        new_vec.z = self.z - other.z
        return new_vec

    def __radd__(self , other):
        other = self.checkOtherType(other)
        new_vec = Vector((0,0,0))
        new_vec.x = self.x + other.x
        new_vec.y = self.x + other.y
        new_vec.z = self.z + other.z
        return new_vec

    def __rsub__(self , other):
        other = self.checkOtherType(other)
        new_vec = Vector((0,0,0))
        new_vec.x = self.x - other.x
        new_vec.y = self.x - other.y
        new_vec.z = self.z - other.z
        return new_vec

    def __mul__(self, other):
        other = self.checkOtherType(other)
        new_vec = Vector((0,0,0))
        new_vec.x = self.x - other.x
        new_vec.y = self.y - other.y
        new_vec.z = self.z - other.z
        return new_vec

    def __rmul__(self, other):
        other = self.checkOtherType(other)
        new_vec = Vector((0,0,0))
        new_vec.x = self.x - other.x
        new_vec.y = self.y - other.y
        new_vec.z = self.z - other.z
        return new_vec

    def checkOtherType(self , other):
        if other.__class__.__name__ != 'Vector':
            other = Vector((other,other,other))
        return other


    def __repr__(self):
        return repr([self.x , self.y , self.z])

print cam_near
print cam_far
print cam_matrix
print cam_fov

cam_vx = Vector(cam_matrix[0:3])
cam_vy = Vector(cam_matrix[4:7])
cam_vz = Vector(cam_matrix[8:11])
cam_t = Vector(cam_matrix[12:15])

print cam_vx*2
print cam_vy
print cam_vz
print cam_t
