def collides_with(self, obj):
    # Bullet size
    b_stretch_wid, b_stretch_len, _ = self.shapesize()
    b_width = b_stretch_len * 20
    b_height = b_stretch_wid * 20
    bx, by = self.xcor(), self.ycor()

    # Object size
    o_stretch_wid, o_stretch_len, _ = obj.shapesize()
    o_width = o_stretch_len * 20
    o_height = o_stretch_wid * 20
    ox, oy = obj.xcor(), obj.ycor()

    # Half-dimensions
    bw = b_width / 2
    bh = b_height / 2
    ow = o_width / 2
    oh = o_height / 2

    # Check AABB (axis-aligned bounding box) collision
    return (
        abs(bx - ox) < (bw + ow) and
        abs(by - oy) < (bh + oh)
    )