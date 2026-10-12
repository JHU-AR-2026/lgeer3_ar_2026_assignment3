import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--x", type=float, default=0.3)
parser.add_argument("--y", type=float, default=-0.15)
parser.add_argument("--z", type=float, default=-6.0)
parser.add_argument("--W", type=float, default=800)
parser.add_argument("--H", type=float, default=600)
parser.add_argument("--n", type=float, default=0.2)
parser.add_argument("--f", type=float, default=20)
parser.add_argument("--fx", type=float, default=800)
parser.add_argument("--fy", type=float, default=800)
parser.add_argument("--ox", type=float, default=400)
parser.add_argument("--oy", type=float, default=400)
args = parser.parse_args()

W, H, n, f = args.W, args.H, args.n, args.f
fx, fy, ox, oy = args.fx, args.fy, args.ox, args.oy

# Q3a projection matrix from intrinsics
M = [
    [2 * fx / W, 0, (W - 2 * ox) / W, 0],
    [0, 2 * fy / H, (-H + 2 * oy) / H, 0],
    [0, 0, -(f + n) / (f - n), -2 * f * n / (f - n)],
    [0, 0, -1, 0],
]

P = [args.x, args.y, args.z, 1]

# clip = M * P
clip = []
for i in range(4):
    s = 0
    for j in range(4):
        s += M[i][j] * P[j]
    clip.append(s)

# Q3c divide by w
ndc = [clip[0] / clip[3], clip[1] / clip[3], clip[2] / clip[3]]

# Q3d
u = 0.5 * (ndc[0] + 1) * W
v = 0.5 * (ndc[1] + 1) * H

print("M =")
for row in M:
    print(row)
print("clip =", clip)
print("ndc =", ndc)
print("u =", u, "v =", v)
