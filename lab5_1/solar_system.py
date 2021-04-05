import graphics as gr

SIZE_X = 800
SIZE_Y = 800

window = gr.GraphWin("Model", SIZE_X, SIZE_Y)

background = gr.Rectangle(gr.Point(0, 0), gr.Point(SIZE_X, SIZE_Y))
background.setFill('green')
background.draw(window)

coords = gr.Point(400, 700)
circle = gr.Circle(coords, 10)
circle.setFill('red')
circle.draw(window)

sun = gr.Circle(gr.Point(400, 400), 50)
sun.setFill('yellow')
sun.draw(window)

velocity = gr.Point(2, 0)
acceleration = gr.Point(0, 0)


def add(point_1, point_2):
    new_point = gr.Point((point_1.x + point_2.x), (point_1.y + point_2.y))
    return new_point


def sub(point_1, point_2):
    new_point = gr.Point((point_1.x - point_2.x), (point_1.y - point_2.y))
    return new_point


def check_coords(ball, ball_velocity):
    if ball.getCenter().x < 0 + 10 or ball.getCenter().x > SIZE_X - 10:
        ball_velocity.x = -ball_velocity.x
    if ball.getCenter().y < 0 + 10 or ball.getCenter().y > SIZE_Y - 10:
        ball_velocity.y = -ball_velocity.y


def update_velocity(ball_velocity, ball_acceleration):
    return add(ball_velocity, ball_acceleration)


def update_acceleration(ball, center_coords):
    diff = sub(ball.getCenter(), center_coords)
    distance_2 = (diff.x ** 2 + diff.y ** 2) ** (3 / 2)

    g = 2000

    return gr.Point(-diff.x * g / distance_2, -diff.y * g / distance_2)


while True:
    circle.move(velocity.x, velocity.y)

    acceleration = update_acceleration(circle, gr.Point(400, 400))
    velocity = update_velocity(velocity, acceleration)
    check_coords(circle, velocity)

    gr.time.sleep(0.02)
