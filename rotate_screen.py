import rotatescreen
import time

screen = rotatescreen.get_primary_display()
start = screen.current_orientation

for i in range():
    a = abs((start - i * 90) % 360)
    screen.rotate_to(a)
    time.sleep(1)


    # pip install rotate-screen