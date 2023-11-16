# -*- coding: utf-8 -*-
import sys
import random
from naoqi import ALProxy
import time

def main(robot_ip, robot_port):
    # Initialize connection with NAO robot
    try:
        tts = ALProxy("ALTextToSpeech", robot_ip, robot_port)
        dialog = ALProxy("ALDialog", robot_ip, robot_port)
        posture=ALProxy("ALRobotPosture",robot_ip, robot_port)
        motion= ALProxy("ALMotion", robot_ip,robot_port)
        audio_player = ALProxy("ALAudioPlayer", robot_ip, robot_port)
        memory = ALProxy("ALMemory", robot_ip, robot_port)
        
   
    except Exception as e:
        print("Error connecting to the robot:", e)
        sys.exit(1)
    
    posture.goToPosture("SitRelax", 1.0)

    #tts.say("Hello")
    def headShake():
        try:
             audio_player.playFile("incorrect.wav")
        except Exception as e:
            tts.say("Error occurred while playing sound:", str(e))
        time.sleep(3)
         # Joint name for the head
        joint_name = "HeadYaw"

        # Set the stiffness of the head
        stiffness = 1.0
        time_to_reach_stiffness= 1.0
        motion.stiffnessInterpolation(joint_name, stiffness,time_to_reach_stiffness)

        # Set the target angles for left to right movement
        target_angles_left_to_right = [-1, 1, 0.0]
        target_times_left_to_right = [1.0, 3.0, 5.0]
        is_absolute = True
        motion.angleInterpolation(joint_name, target_angles_left_to_right, target_times_left_to_right, is_absolute)

        # Remove the stiffness on the head
        stiffness = 0.0
        time_to_reach_stiffness= 1.0
        motion.stiffnessInterpolation(joint_name, stiffness,time_to_reach_stiffness)

    def nod():
        try:
             audio_player.playFile("correct.wav")
        except Exception as e:
            tts.say("Error occurred while playing sound:", str(e))

        time.sleep(3)
        joint_name = "HeadPitch"
        stiffness = 1.0
        time_to_reach_stiffness = 1.0

        # Make sure the head is stiff to be able to move it
        motion.stiffnessInterpolation(joint_name, stiffness, time_to_reach_stiffness)

        target_angles = [0.5, -0.5, 0.0]
        # Set the corresponding time lists, in seconds
        target_times = [1.0, 2.0, 3.0]
        # Specify that the desired angles are absolute
        is_absolute = True

        # Call the angle interpolation method. The joint will reach the desired angles at the desired times
        motion.angleInterpolation(joint_name, target_angles, target_times, is_absolute)

        # Remove the stiffness on the head
        stiffness = 0.0
        motion.stiffnessInterpolation(joint_name, stiffness, time_to_reach_stiffness)

    dialog.setLanguage("English")  
    dialog.setConfidenceThreshold("English",0.3) 
    
    # Create a dialog topic for questions and responses
    topic_content = (  'topic: ~brokentelephone()\n'#1
                       'language:enu\n'#2
                       'concept:(fruits)[Apple Banana Orange Grape Strawberry Blueberry Watermelon Mango Pineapple Kiwi]\n'#3
                       'u:(~fruits) ^call(nod())\n'#4
                       'proposal:%onename What are your names children,choose one person to represent all of you,can they introduce themselves? \n'#5
                       'proposal:%childname What is your name? \n'#6
                       'proposal:%anotherchild Please children choose another person to play next..........,^goto(childname) \n'#7
                       'proposal:%game Do you want us to play a game,say yes if you want us to play,you can also say no if you do not want to play right now \n' #8
                       
                       'u:(Hello nao)Hello,^goto(onename)\n'#9
                       'u:(["my name is _*""my names are _*"])nice too meet you $1 ,^goto(game) $name=$1\n'#10
                       'u:(game)^goto(game) \n'#11
                       'u:(yes)Great,$name,i will tell you a fruit name and you will tell your playmates,choose a another child  that will say back the word back to me,say fruit if you want me to give you a word \n'#12
                       'u:(fruit) ^rand~fruits\n'#13
                       'u:(Apple)Apples float in water because they are made up of about 25 percent air ^clear(name) ^goto(anotherchild) \n'#14
                       'u:(Banana)Bananas are berries, and the plant they grow on is not a tree but a giant herb ^clear(name) ^sameProposal \n'#15
                       'u:(Orange)Oranges are an excellent source of vitamin C, which is essential for a healthy body ^clear(name) ^sameProposal\n'#16
                       'u:(Grape)Grapes can be tiny like little balls, and they come in different colors like red, green, and purple. People use them to make yummy grape juice. ^clear(name) ^sameProposal\n'#17
                       'u:(Strawberry)Strawberries are the only fruit with seeds on the outside ^clear(name) ^sameProposal\n'#18
                       'u:(Blueberry)Blueberry are blue, and you can pop them into your mouth like candy. They are great for making your pancakes or muffins super yummy. ^clear(name) ^sameProposal\n'#19
                       'u:(Watermelon)Watermelon is over   90 percent water, making it a refreshing fruit ^clear(name) ^sameProposal\n' #20
                       'u:(Mango)Mango is known as the king of fruits and is one of the most popular fruits in the world. ^clear(name) ^sameProposal\n'#21
                       'u:(Pineapple)Pineapples are  super sweet and juicy inside, like a big, fruity treasure chest. You can have them in fruit salads or as a special treat on pizza! ^clear(name) ^sameProposal\n'#22
                       'u:(Kiwi)Kiwi fruit has more vitamin C per serving than an equivalent amount of oranges. ^clear(name) ^sameProposal\n'#23
                        
                      'u:(no) I was hoping you would say yes, I was really looking forward to play the game with you $name. ^clear(name)\n'#24
                      'u:([e:SaidMisunderstood ~fruits]) ^call(headshake()) Try again!\n'#24
                      )
    
                       

    
   
    # Load the dialog topic
    # topic_content_str='\n'.join(topic_content)
    # print(topic_content_str)
    topic_name = dialog.loadTopicContent(topic_content)
   

    dialog.subscribe('brokentelephone')
    # Activate the dialog topic
    dialog.activateTopic(topic_name)
    
  

    # Keep the program running until Ctrl + C is pressed
    try:
        while True:
            pass
    except KeyboardInterrupt:
        pass  # print(topic_content_str)

    dialog.deactivateTopic(topic_name)
    dialog.unloadTopic(topic_name)
    # Deactivate the dialog topic and unload it before exiting
    dialog.unsubscribe("brokentelephone")
    

if __name__ == "__main__":
    robot_ip = "127.0.0.1"  # Replace with the IP address of your NAO robot
    robot_port = 9559
  # print(topic_content_str)
    main(robot_ip, robot_port)
   # 'concept:(fruits) [Apple Banana Orange Grape Strawberry Blueberry Watermelon Mango Pineapple Kiwi]\n'
