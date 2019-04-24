#!/usr/bin/python

from flask import Flask
from flask_ask import Ask, statement, question, session

import rospy
import threading

from std_msgs.msg import Bool, String

"""
This node uses flask-ask server to listen on http server for a connection from Amazon Alexa Skill
ASK is named 
"""

app = Flask(__name__)
ask = Ask(app, '/')


@ask.launch
def launch():
	pass

@ask.intent('AMAZON.CancelIntent')
def cancel_intent():
	pass

@ask.intent('AMAZON.HelpIntent')
def help_intent():
	pass

@ask.intent('CassieSmile')
def smile_intent():
	rospy.loginfo("smile intent recived")
	util.clear_msgs()
	util.amsg = 'happy'
	util.pub.publish(util.amsg)
	return statement("  ")

@ask.intent('CassieDance')
def dance_intent():
	rospy.loginfo("dance intent recived")
	util.clear_msgs()
	util.amsg = 'dance'
	util.pub.publish(util.amsg)
	return statement(" ")

@ask.intent('CassieAngry')
def angry_intent():
	rospy.loginfo("angry intent recived")
	util.clear_msgs()
	util.amsg = 'angry'
	util.pub.publish(util.amsg)
	return statement(" ")
	
class Utils():
	"""docstring for Utils"""
	def __init__(self):
		rospy.init_node('alexa_listener')
		self.pub = rospy.Publisher('alexa_listener_commands', String, queue_size=1)
		rospy.loginfo("alexa_listener is running....")
		self.amsg = String()

	def clear_msgs(self):
		self.amsg.SMILE = False 
		self.amsg.DANCE = False 
		self.amsg.ANGRY = False
		self.amsg.SAD = False


def main():
	global util 

	util = Utils()

	alexa_thread = threading.Thread(target = app.run)
	alexa_thread.daemon = True
	rospy.loginfo("alexa_thread is running...........")
	alexa_thread.start()

	rospy.spin()


if __name__ == '__main__':
	main()
