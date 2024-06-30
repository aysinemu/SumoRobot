# Yolo Uno (Using CodeBlock)
from ultrasonic import *
from pins import *
from motor import *
from mdv2 import *
from drivebase import *

# Mô tả hàm này...
async def Fly():
  global l, r, f
  if f > 40 and l > 40:
    robot.speed(42, min_speed=42)
    robot.move_right()

# Mô tả hàm này...
async def ATT():
  global l, r, f
  if f <= 40 and f >= 0 or l <= 40 and l >= 0:
    robot.forward()

# Mô tả hàm này...
async def LINE_L():
  global l, r, f
  if (pin_D3.read_digital() == 1) and (pin_D5.read_digital() == 0) and (pin_D7.read_digital() == 1) and (pin_D9.read_digital() == 1):
    await robot.move_right_for(1, unit=SECOND, then=STOP)
    await robot.backward_for(0.5, unit=SECOND, then=BRAKE)

# Mô tả hàm này...
async def DEF():
  global l, r, f
  if f < 8 and f >= 0:
    await robot.backward_for(0.1, unit=SECOND, then=BRAKE)
    await robot.forward_for(0.5, unit=SECOND, then=BRAKE)

# Mô tả hàm này...
async def LINE_S():
  global l, r, f
  if (pin_D3.read_digital() == 1) and (pin_D5.read_digital() == 1) and (pin_D7.read_digital() == 1) and (pin_D9.read_digital() == 0):
    await robot.forward_for(0.5, unit=SECOND, then=BRAKE)

# Mô tả hàm này...
async def LINE_F():
  global l, r, f
  if (pin_D3.read_digital() == 0) and (pin_D5.read_digital() == 1) and (pin_D7.read_digital() == 1) and (pin_D9.read_digital() == 1):
    await robot.backward_for(0.5, unit=SECOND, then=BRAKE)

# Mô tả hàm này...
async def LINE_R():
  global l, r, f
  if (pin_D3.read_digital() == 1) and (pin_D5.read_digital() == 1) and (pin_D7.read_digital() == 0) and (pin_D9.read_digital() == 1):
    await robot.backward_for(0.5, unit=SECOND, then=BRAKE)
    await robot.move_left_for(1, unit=SECOND, then=BRAKE)

# Mô tả hàm này...
async def LINE_FRL():
  global l, r, f
  if (pin_D3.read_digital() == 0) and (pin_D5.read_digital() == 0) and (pin_D7.read_digital() == 0) and (pin_D9.read_digital() == 1):
    await robot.backward_for(0.5, unit=SECOND, then=BRAKE)

# Mô tả hàm này...
async def LINE_SRL():
  global l, r, f
  if (pin_D3.read_digital() == 1) and (pin_D5.read_digital() == 0) and (pin_D7.read_digital() == 0) and (pin_D9.read_digital() == 0):
    await robot.forward_for(0.5, unit=SECOND, then=BRAKE)

# Mô tả hàm này...
async def LINE_FSL():
  global l, r, f
  if (pin_D3.read_digital() == 0) and (pin_D3.read_digital() == 0) and (pin_D3.read_digital() == 1) and (pin_D3.read_digital() == 0):
    await robot.backward_for(0.5, unit=SECOND, then=BRAKE)
    await robot.move_right_for(1, unit=SECOND, then=BRAKE)

# Mô tả hàm này...
async def LINE_FSR():
  global l, r, f
  if (pin_D3.read_digital() == 0) and (pin_D3.read_digital() == 1) and (pin_D3.read_digital() == 0) and (pin_D3.read_digital() == 0):
    await robot.backward_for(0.5, unit=SECOND, then=BRAKE)
    await robot.move_left_for(1, unit=SECOND, then=BRAKE)

# Mô tả hàm này...
async def LINE_SL():
  global l, r, f
  if (pin_D3.read_digital() == 1) and (pin_D5.read_digital() == 0) and (pin_D7.read_digital() == 1) and (pin_D9.read_digital() == 0):
    await robot.backward_for(0.5, unit=SECOND, then=BRAKE)
    await robot.move_right_for(1, unit=SECOND, then=BRAKE)

# Mô tả hàm này...
async def LINE_FL():
  global l, r, f
  if (pin_D3.read_digital() == 0) and (pin_D3.read_digital() == 0) and (pin_D3.read_digital() == 1) and (pin_D3.read_digital() == 1):
    await robot.backward_for(0.5, unit=SECOND, then=BRAKE)
    await robot.move_right_for(1, unit=SECOND, then=BRAKE)

# Mô tả hàm này...
async def LINE_SR():
  global l, r, f
  if (pin_D3.read_digital() == 1) and (pin_D5.read_digital() == 1) and (pin_D7.read_digital() == 0) and (pin_D9.read_digital() == 0):
    await robot.backward_for(0.5, unit=SECOND, then=BRAKE)
    await robot.move_left_for(1, unit=SECOND, then=BRAKE)

# Mô tả hàm này...
async def LINE_FR():
  global l, r, f
  if (pin_D3.read_digital() == 0) and (pin_D5.read_digital() == 1) and (pin_D7.read_digital() == 0) and (pin_D9.read_digital() == 1):
    await robot.backward_for(0.5, unit=SECOND, then=BRAKE)
    await robot.move_left_for(1, unit=SECOND, then=BRAKE)

l = None
r = None
f = None
ultrasonic_A1_A2 = Ultrasonic(A1_PIN, A2_PIN)
ultrasonic_A2_A3 = Ultrasonic(A2_PIN, A3_PIN)
ultrasonic_A3_A6 = Ultrasonic(A3_PIN, A6_PIN)
pin_D3 = Pins(D3_PIN)
pin_D5 = Pins(D5_PIN)
pin_D7 = Pins(D7_PIN)
pin_D9 = Pins(D9_PIN)
md_v2 = MotorDriverV2()
motor1 = DCMotor(md_v2, M1, reversed=False)
motor2 = DCMotor(md_v2, M2, reversed=False)
motor3 = DCMotor(md_v2, M3, reversed=False)
motor4 = DCMotor(md_v2, M4, reversed=False)
robot = DriveBase(MODE_4WD, m1=motor1, m2=motor3, m3=motor2, m4=motor4)

def deinit():
  robot.stop()

import yolo_uno
yolo_uno.deinit = deinit

async def task_D_H_G_i():
  global l, r, f
  while True:
    await asleep_ms(10)
    l = ultrasonic_A1_A2.distance_cm()
    r = ultrasonic_A2_A3.distance_cm()
    f = ultrasonic_A3_A6.distance_cm()

async def task_forever():
  global l, r, f
  while True:
    await asleep_ms(50)
    if (pin_D3.read_digital() == 1) and (pin_D5.read_digital() == 1) and (pin_D7.read_digital() == 1) and (pin_D9.read_digital() == 1):
      robot.speed(225, min_speed=225)
      await ATT()
      await Fly()
    else:
      robot.speed(40, min_speed=40)
      await LINE_FRL()
      await LINE_FSL()
      await LINE_FSR()
      await LINE_SRL()
      await LINE_FL()
      await LINE_FR()
      await LINE_SL()
      await LINE_SR()
      await LINE_L()
      await LINE_R()
      await LINE_S()
      await LINE_F()

async def setup():
  global l, r, f
  print('App started')
  neopix.show(0, hex_to_rgb('#00ff00'))
  await asleep_ms(2100)
  neopix.show(0, hex_to_rgb('#800080'))
  r = 0
  f = 0
  l = 0
  robot.speed(40, min_speed=40)

  create_task(task_D_H_G_i())
  create_task(task_forever())

async def main():
  await setup()
  while True:
    await asleep_ms(100)

run_loop(main())
