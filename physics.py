import math
from math import sqrt
from pygame import Vector2
from shapes import Line, Circle


def closest_point_on_segment(seg, circle_pos):
    pt_v = circle_pos - seg.a  # vector ac (from a to center of the circle c)

    proj = pt_v.dot(seg.unit)  # length of vector from a to closest
    if proj <= 0:
        return seg.a  # closest point is start of the line
    if proj >= seg.length:
        return seg.b  # closest point is end of the line

    proj_v = seg.unit * proj  # vector from a to closest
    closest = proj_v + seg.a
    return closest


def normal_segment_circle(seg, circle):
    closest = closest_point_on_segment(seg, circle.pos)

    dist_v = circle.pos - closest
    return dist_v.normalize()


def segment_circle_collision(seg, circle):
    closest = closest_point_on_segment(seg, circle.pos)

    dist_v = circle.pos - closest
    if dist_v.length() > circle.radius:
        return False, dist_v.normalize(), None, closest

    depth = circle.radius - dist_v.length()
    return True, dist_v.normalize(), depth, closest


def segments_intersects(seg1, seg2):
    def on_segment(p, q, r):
        if max(p[0], q[0]) >= r[0] >= min(p[0], q[0]) and max(p[1], q[1]) >= r[1] >= min(p[1], q[1]):
            return True
        return False

    def orientation(p, q, r):
        val = ((q[1] - p[1]) * (r[0] - q[0])) - ((q[0] - p[0]) * (r[1] - q[1]))
        if val == 0:
            return 0
        return 1 if val > 0 else -1

    p1, q1 = seg1.a, seg1.b
    p2, q2 = seg2.a, seg2.b

    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    if o1 != o2 and o3 != o4:
        return True

    if o1 == 0 and on_segment(p1, q1, p2): return True
    if o2 == 0 and on_segment(p1, q1, q2): return True
    if o3 == 0 and on_segment(p2, q2, p1): return True
    if o4 == 0 and on_segment(p2, q2, q1): return True

    return False


def intersection_segments_point(seg1, seg2):
    r = seg1.vec
    s = seg2.vec

    rxs = r.cross(s)

    if rxs == 0:
        return None
    t = (seg2.a - seg1.a).cross(s)/rxs
    u = (seg2.a - seg1.a).cross(r)/rxs

    if rxs != 0 and 0 <= t <= 1 and 0 <= u <= 1:
        return seg1.a+t*r
    return None


def segment_circle_intersects(seg, circle):
    if seg.length == 0:
        return False

    closest = closest_point_on_segment(seg, circle.pos)

    dist_v = circle.pos - closest
    if dist_v.length() > circle.radius:
        return False
    return True


def intersection_circle_segment_point(seg, circle):
    collided = segment_circle_intersects(seg, circle)
    if not collided:
        return None

    dx, dy = seg.vec
    p1, q1 = seg.a
    p2, q2 = seg.b
    cx, cy = circle.pos

    a = dx**2 + dy**2
    b = 2 * (dx * (p1 - cx) + dy * (q1 - cy))
    c = cx**2 + cy**2

    c += p1**2 + q1**2
    c -= 2 * (cx * p1 + cy * q1)
    c -= circle.radius**2

    delta = b * b - 4 * a * c

    if delta < 0 or abs(a) < 0.000001:
        return None

    mu1 = (-b + sqrt(delta)) / (2 * a)
    mu2 = (-b - sqrt(delta)) / (2 * a)

    points = []
    if 0 <= mu1 <= 1:
        points.append(Vector2(p1 + mu1 * (p2 - p1), q1 + mu1 * (q2 - q1)))
    if 0 <= mu2 <= 1:
        points.append(Vector2(p1 + mu2 * (p2 - p1), q1 + mu2 * (q2 - q1)))

    if len(points) == 0:
        return None
    return points


def closest_intersection(lines, seg, current_pos):
    founded = []

    for line in lines:
        for shape in line.hitbox:
            if isinstance(shape, Line):
                intersection = intersection_segments_point(seg, shape)
                if intersection is not None:
                    founded.append([(intersection - current_pos).length(), intersection, line])
            if isinstance(shape, Circle):
                intersections = intersection_circle_segment_point(seg, shape)
                if intersections is not None:
                    for intersection in intersections:
                        founded.append([(intersection - current_pos).length(), intersection, line])

    if len(founded) == 0:
        return None
    return [x for x in founded if x[0] == min(founded, key=lambda x: x[0])[0]]


def check_collisions(walls, seg, ball):
    intersection = closest_intersection(walls, seg, ball.pos)
    if intersection is None:
        return False
    if len(intersection) == 2:
        _, inter_point, wall1 = intersection[0]
        _, _, wall2 = intersection[1]

        normal1 = normal_segment_circle(wall1, ball)
        normal2 = normal_segment_circle(wall2, ball)
        normal = (normal1+normal2).normalize()
    else:
        _, inter_point, wall = intersection[0]
        normal = normal_segment_circle(wall, ball)

    ball.pos.update(inter_point)
    ball.bounce(normal)
    return True


def point_in_rect(rect, point):
    x1, y1, x2, y2 = rect
    px, py = point
    return (x1 < px < x2) and (y1 < py < y2)


def point_in_circle(circle, point):
    cx, cy = circle.pos
    r = circle.radius + 5
    x, y = point
    return ((x - cx)**2 + (y - cy)**2) < (r**2)


def gravity(circle, ball):
    d = (circle.pos-ball.pos).length()

    force = 1/10 * ((circle.mass * ball.mass) / (d*100))
    normal = (circle.pos - ball.pos).normalize()

    return force*normal


def ball_rectangle_intersect(ball, rect):
    r1x1, r1y1 = ball.pos[0] - ball.radius, ball.pos[1] - ball.radius
    r1x2, r1y2 = r1x1 + ball.radius*2, r1y1 + ball.radius*2

    r2x1, r2y1 = rect.pos
    r2x2, r2y2 = r2x1 + rect.size, r2y1 + rect.size

    # If one rectangle is on left side of other]
    if (r1x1 >= r2x2) or (r2x1 >= r1x2):
        return False

    # If one rectangle is above other
    if (r1y1 <= r2y2) and (r2y1 <= r1y2):
        return True

    return False

