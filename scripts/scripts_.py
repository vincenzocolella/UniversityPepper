from pepper_cmd import *
import pepper_cmd
import os
import sys
import time
import csv
import wave
import contextlib
import math
from numpy.random import choice

def start_interaction(speech):
    speech.say("Hi,I'm pepper")
    gesture=Gestures()
    gesture.sayhi()
    speech.say("touch my head to interact with me!.")
    return gesture.head_touch(wait_ = 10.0) 

begin()
class InitRobot():

	def __init__(self, alive=True, speed=200):
		pepper_cmd.robot.setAlive(alive)
		pepper_cmd.robot.tts_service.setParameter("speed", 200)
  
class Gestures:
	def __init__(self, head=False):
		InitRobot(speed=100)
		# joint angles should be given in radians
		# 0 -  HeadYaw,        1 -  HeadPitch
		# 2 -  LShoulderPitch, 3 -  LShoulderRoll, 4 -  LElbowYaw, 5 -  LElbowRoll, 6 -  LWristYaw
		# 7 -  RShoulderPitch, 8 -  RShoulderRoll, 9 -  RElbowYaw, 10 - RElbowRoll, 11 - RWristYaw
		# 12 - LHand,          13 - RHand, 		 14 - HipRoll, 	 15 - HipPitch,   16 - KneePitch
		self.jointNames = ["HeadYaw", "HeadPitch",
                     "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw",
                     "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw",
                     "LHand", "RHand", "HipRoll", "HipPitch", "KneePitch"]
		self.head = head

	def change_pose(self, indices, values, pose):
     
		for idx, val in zip(indices, values):
			pose[idx] = val
		pepper_cmd.robot.setPosture(pose)
		
		return pose

	def head_touch(self, wait_=20.0):

		curr_time = time.time()  # start timer

		pepper_cmd.robot.startSensorMonitor()
		print("Waiting a touch to start")
		while not self.head and (time.time() - curr_time < wait_):
			p = pepper_cmd.robot.sensorvalue()
			self.head = (p[3] > 0)  # head sensor
		pepper_cmd.robot.stopSensorMonitor()

		if self.head:
			print("Touch detected.")
			pose = pepper_cmd.robot.getPosture()
			self.change_pose([0, 1], [0.0, -0.5], pose)
			pepper_cmd.robot.normalPosture()

		return self.head

	def sayhi(self):
		a=math.pi/180
  
		self.change_pose([7,8,10], 
							[-20*a,-90*a,120*a],
							pepper_cmd.robot.getPosture())
		self.change_pose([7,8,10],
							[-20*a,-90*a,60*a],
							pepper_cmd.robot.getPosture())

		return pepper_cmd.robot.getPosture()

class Sonar:

	def __init__(self):
		InitRobot()

	def listen(self, detected=False, threshold=1.0, curr_time=0.0, wait_time=3.0):

		pepper_cmd.robot.startSensorMonitor()

		if not detected:
			print("Waiting approach...")
			try:
				while not detected:
					p = pepper_cmd.robot.sensorvalue()
					detected = (0.0 < p[1] < threshold)
					curr_time = time.time()
			except KeyboardInterrupt:
				pepper_cmd.robot.stopSensorMonitor()
				sys.exit(0)
			return self.listen(True, 1.0, curr_time, 3.0)
		else:
			print("Person approached")
			while detected:
				p = pepper_cmd.robot.sensorvalue()
				detected = (0.0 < p[1] < threshold)
				if time.time() - curr_time >= wait_time:
					print("Person stayed for more than {} seconds.".format(wait_time))
					pepper_cmd.robot.stopSensorMonitor()
					if (0.0 < p[1] < threshold): return 'front' 
			print("Person walked away.")
			return self.listen(False, 1.0, 0.0, 3.0)
class Speech:

	def __init__(self, speed=100):
		InitRobot(speed=speed)

	def say(self, sentence, answ=False):
		pepper_cmd.robot.say(sentence)
		if answ:
			return self.listen(timeout=30)

	def listen(self, vocabulary=["Play, Indication"], timeout=30):
		answer = pepper_cmd.robot.asr(vocabulary=vocabulary, timeout=timeout)
		while not answer:
			answer = self.say(
				sentence="Sorry, I didn't understand, repeat please.", answ=True)
		return answer
end()
