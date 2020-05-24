def closest_point_on_seg(seg, circle_pos):
    pt_v = circle_pos - seg.a  # vector ac (from a to center of the circle c)

    proj = pt_v.dot(seg.unit)  # length of vector from a to closest
    if proj <= 0:
        return seg.a  # closest point is start of the line
    if proj >= seg.length:
        return seg.b  # closest point is end of the line

    proj_v = seg.unit * proj  # vector from a to closest
    closest = proj_v + seg.a
    return closest


def segment_circle(seg, circle):
    closest = closest_point_on_seg(seg, circle.pos)

    dist_v = circle.pos - closest
    if dist_v.length() > circle.radius:
        return False, dist_v.normalize(), None, closest

    depth = circle.radius - dist_v.length()
    return True, dist_v.normalize(), depth, closest


def intersects(seg1, seg2):
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


def intersection_point(seg1, seg2):
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

