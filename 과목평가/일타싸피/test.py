"""
Stage 1
Data Received: 64/64/250/122/-1/-1/-1/-1/-1/-1/-1/-1/
Data Sent: 72.681062/97.416631/
           각도/속도/"""

import math

width = 254
height = 127
r = 5.73 / 2

holes = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]
number_of_balls = 6
balls = [[0, 0] for _ in range(number_of_balls)]

server_data = "64/64/250/122/-1/-1/-1/-1/-1/-1/-1/-1/"

data = server_data[: len(server_data) - 1].split("/")
data = [int(n) for n in data]

idx = 0
for i in range(number_of_balls):
    for j in range(2):
        balls[i][j] = data[idx]
        idx += 1
print(balls)


target_ball_idx = 1
target_hole_idx = 5

x1 = balls[target_ball_idx][0] - balls[0][0]
y1 = balls[target_ball_idx][1] - balls[0][1]
white_target = math.sqrt(abs(x1) ** 2 + abs(y1) ** 2)
radian1 = math.atan2(x1, y1)

x2 = holes[target_hole_idx][0] - balls[target_ball_idx][0]
y2 = holes[target_hole_idx][1] - balls[target_ball_idx][1]

hole_target = math.sqrt(abs(x2) ** 2 + abs(y2) ** 2)

x3 = holes[target_hole_idx][0] - balls[0][0]
y3 = holes[target_hole_idx][1] - balls[0][1]

hole_white = math.sqrt(abs(x3) ** 2 + abs(y3) ** 2)


hole_angle = math.acos(
    (hole_target**2 + hole_white**2 - white_target**2) / (2 * hole_white * hole_target)
)

white_goal = math.sqrt(
    hole_white**2
    + (hole_target + 2 * r) ** 2
    - 2 * hole_white * hole_target * math.cos(hole_angle)
)

radian2 = math.acos(
    (hole_white**2 + white_goal**2 - (hole_target + 2 * r) ** 2)
    / (2 * hole_white * white_goal)
)

theta_radian = radian1 + radian2

theta = math.degrees(theta_radian)

print(theta)
