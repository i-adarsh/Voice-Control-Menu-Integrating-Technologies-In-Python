import getpass
import boto3
import subprocess
from gtts import gTTS
import playsound
import datetime
import pync
import os
import pip
from googletrans import Translator
import speech_recognition as sr
from sys import platform
from plyer import notification
from sys import platform

r = sr.Recognizer()  # Voice Recognition



def detect_os():
    if platform == "linux" or platform == "linux2":
        return 'clear'
    elif platform == "darwin":
        return 'clear'
    elif platform == "win32":
        return 'cls'

#
# speak('Welcome to the आदर्श Automation World')
# speak('Here is the list of Services which we can automate for you')


clear_cmd = detect_os()


def speak(text):
    tts = gTTS(text=text, lang='hi', slow=False)
    tts.save("voice.mp3")
    playsound.playsound('voice.mp3', True)


def translate(text):
    translator = Translator()
    translation = translator.translate(text, dest='hi')
    return translation.text


def listen():
    try:
        with sr.Microphone() as source:
            voice = r.listen(source)
            speak('We are Processing your request ...')
        if voice:
            command = r.recognize_google(voice)
            command = command.lower()
            return command
        else:
            speak("Sorry Sir I won't get you, Please Try Again")
    except Exception as e:
        listen()


# def hadoop_config():
#     while True:
#         os.system(clear_cmd)
#         print()
#         print()
#         print()
#         print()
#         speak('Here is the list of Services which we can support in Hadoop')
#         print('''\033[33m
#                                       :/-` ./oyyyyssso-
#                                       : -yho/-.......:ohs.
#                                       .hy.```.........../yy/
#                                    :yss+::-..............-:+ys.   `++.                                  \033[92m Select your choice:\033[33m
#                              `-:+ods--oy+/--....:+-.......---/d+`+do+do
#                          :oyys++my..-ss/-.......+-...--.----odmmys+/-:N-                         \033[92m----------------------------------\033[33m
#               `  ./   .sho-```oh-`..+---..:-....-.-yNMh:----+shh------yy
#             :+`+shd``yh:````-h/`...--.....o/.....-:+/o:----//o-y------om                             \033[94m 1. \033[93mHadoop Installation\033[33m
#             : ss-my/m+``...:d.`...--......+y-...------------:--+------+N
#               -h+dsN/`.....m:`...-........-m:.-----------------------:sd                             \033[94m 2. \033[93mConfigure Hadoop Cluster\033[33m
#                -sshs`......+d:.-/-.........m/------------------------/m/
#                   m-......../dss-........--m/--------/:-------------/ds                              \033[94m 3. \033[93mConfigure NameNode\033[33m
#                   m:.........+d-......---:od/-------::os+:-------:+yd:
#                   ho.........+d:....-+syyoo/:--/++/---mMMMymyyyyys+-                                 \033[94m 4. \033[93mCheck Connected Nodes\033[33m
#                  :Nm-.........-syssyy+::--------/yNho:dmdsd/
#                :hy:oh-........-----------------:/dm/:yysso.                                          \033[94m 5. \033[93mConfigure DataNode\033[33m
#                dy..-oh-......-:-------/-------:/ho+N`
#                .dy:-:od-..----/dyyyhhhy-------/hs//N-                                                \033[94m 6. \033[93mUpload File\033[33m
#                  :yhhdN------:om `dh+-------:+do///d+
#                     .No----::om.  hh---::::ohNyssssm/                                                \033[94m 7. \033[93mExit !\033[33m
#                     .dds+/://mo    yd/://yd+``.....`
#                       `-/+ssyo`     :hhhho
#
#                       \033[96m
#             oooo                        .o8
#             `888                       "888
#              888 .oo.    .oooo.    .oooo888   .ooooo.   .ooooo.  oo.ooooo.
#              888P"Y88b  `P  )88b  d88' `888  d88' `88b d88' `88b  888' `88b
#              888   888   .oP"888  888   888  888   888 888   888  888   888
#              888   888  d8(  888  888   888  888   888 888   888  888   888
#             o888o o888o `Y888""8o `Y8bod88P" `Y8bod8P' `Y8bod8P'  888bod8P'
#                                                                   888
#                                                                  o888o
#             \033[0m''')
#         speak('Tell me, what do you want to do ?')
#         print('listening . . .')
#         cmd = listen()
#         if 'Installation' in cmd or 'install' in cmd:
#             speak('please enter IP of your Device and Press Enter')
#             ip = input('Enter IP of Device: ')
#             file = open('/Users/adarshkumar/Documents/PycharmProjects/PythonProject/Linux/hadoop/inventory', 'w+')
#             file.write('[install]\n')
#             file.write(ip + "\n\n")
#             file.close()
#             speak('Okay, Starting Hadoop Installation Please Wait ...')
#             print('Starting Installation, Please Wait...')
#             os.system('ansible-playbook install_hadoop.yml -i inventory')
#             speak('Hadoop Installation Successfull')
#             print('Hadoop Installation Successfull')
#             speak('Press Enter to go Back !')
#             print('Press Enter to go Back !')
#             input()
#         elif 'cluster' in cmd or 'hadoop cluster' in cmd:
#             speak('Please Eneter IP of your MasterNode and DataNode')
#             mIP = input("Enter Master's IP : ")
#             sIP = input("Enter Slave's IP :")
#             file = open('/Users/adarshkumar/Documents/PycharmProjects/PythonProject/Linux/hadoop/inventory', 'w+')
#             file.write('[master]\n')
#             file.write(mIP + "\n\n")
#             file.write('\n\n[slave]\n')
#             file.write(sIP + "\n")
#             file.close()
#             speak('Okay, Starting Configuring Hadoop Cluster, Please Wait ...')
#             print('Starting Configuring Hadoop Cluster, Please Wait...')
#             os.system('ansible-playbook configure_hadoop_cluster.yml -i inventory')
#             speak('Hadoop Installation Successfull')
#             print('Hadoop Installation Successfull')
#             speak('Press Enter to go Back !')
#             print('Press Enter to go Back !')
#             input()
#         elif 'namenode' in cmd:
#             speak('please enter IP of your Device and Press Enter')
#             ip = input('Enter IP of Device: ')
#             file = open('/Users/adarshkumar/Documents/PycharmProjects/PythonProject/Linux/hadoop/inventory', 'w+')
#             file.write('[master]\n')
#             file.write(ip + "\n\n")
#             file.close()
#             speak('Okay, Starting Configuring NameNode Please Wait ...')
#             print('Configuring NameNode, Please Wait...')
#             os.system('ansible-playbook configure_namenode.yml -i inventory')
#             speak('Namenode Configured Successfully')
#             print('Namenode Configured Successfully')
#             speak('Press Enter to go Back !')
#             input()
#         elif 'datanode' in cmd:
#             speak('please enter IP of your Device and Press Enter')
#             ip = input('Enter IP of Device: ')
#             file = open('/Users/adarshkumar/Documents/PycharmProjects/PythonProject/Linux/hadoop/inventory', 'w+')
#             file.write('[slave]\n')
#             file.write(ip + "\n\n")
#             file.close()
#             speak('Okay, Starting Configuring DataNode Please Wait ...')
#             print('Configuring DataNode, Please Wait...')
#             os.system('ansible-playbook configure_datanode.yml -i inventory')
#             speak('DataNode Configured Successfully')
#             print('DataNode Configured Successfully')
#             speak('Press Enter to go Back !')
#             input()
#         elif 'connected' in cmd:
#             speak('please enter IP of your Device and Press Enter')
#             ip = input('Enter IP of Device: ')
#             file = open('/Users/adarshkumar/Documents/PycharmProjects/PythonProject/Linux/hadoop/inventory', 'w+')
#             file.write('[slave]\n')
#             file.write(ip + "\n\n")
#             file.close()
#             speak('Okay, Starting Configuring DataNode Please Wait ...')
#             print('Configuring DataNode, Please Wait...')
#             os.system('ansible-playbook configure_datanode.yml -i inventory')
#             speak('DataNode Configured Successfully')
#             print('DataNode Configured Successfully')
#             speak('Press Enter to go Back !')
#             input()
#         elif 'upload' in cmd:
#             speak('please enter IP of your datanode and Press Enter')
#             ip = input('Enter IP of Datanode: ')
#             speak('Enter Path of the file to be Uploaded')
#             path = input('Enter Path of the file to be Uploaded : ')
#             file = open('/Users/adarshkumar/Documents/PycharmProjects/PythonProject/Linux/hadoop/inventory', 'w+')
#             file.write('[slave]\n')
#             file.write(ip + "\n\n")
#             file.close()
#
#             path_file = open(
#                 '/Users/adarshkumar/Documents/PycharmProjects/PythonProject/Linux/hadoop/roles/hadoop_file_upload/vars/main.yml',
#                 'w+')
#             path_file.write(f'''
#                 file_path: {path}
#                 upload: hadoop fs - put {path} /
#                 ''')
#             path_file.close()
#             os.system('ansible-playbook hadoop_file_upload.yml -i inventory')
#             speak('File Uploaded Successfully')
#             print('File Uploaded Successfully')
#             input()
#         elif 'exit' in cmd or 'quit' in cmd or 'back' in cmd or 'back menu' in cmd or 'menu' in cmd:
#             speak('Press Enter to go to the Main Menu !')
#             input()
#             os.system(clear_cmd)
#             break
#         else:
#             speak("Sorry, I didn't get You, Please Try Again")


# def kubernetes_config():
#     print('''\033[34m
#                                             `-/syyyo/-`
#                                         `:+syyyyyyyyyyys+-`
#                                     .:+yyyyyyyyyyyyyyyyyyyys+:.                                          \033[92m Select your choice:\033[34m
#                                 ./oyyyyyyyyyyyyyo/syyyyyyyyyyyyyo/.
#                            `-/oyyyyyyyyyyyyyyyyy- :yyyyyyyyyyyyyyyyyo/-`
#                           /yyyyyyyyyyyyyyyyyyyyy/ +yyyyyyyyyyyyyyyyyyyyy:                            \033[92m--------------------------------\033[34m
#                          -yyyyyyyyyyyyyyyyyyso+/` ./+oyyyyyyyyyyyyyyyyyyy.
#                          oyyyyyyo-:syyyys/-`           `-+yyyyys:-oyyyyyy+
#                         .yyyyyyys:` :oo-   .:+oo   so+:.   -o+- ./yyyyyyyy`                         \033[94m 1. \033[93mConfigure Master Node\033[34m
#                         +yyyyyyyyyys.    /syyyyo   syyyys:    .syyyyyyyyyy/
#                        `yyyyyyyyyyyo`     -oyyy+   oyyy+-     `syyyyyyyyyyy`                        \033[94m 2. \033[93mConfigure Slave Node\033[34m
#                        +yyyyyyyyyys`  +s:   `:+.   -+-   `:s/  `yyyyyyyyyyy/
#                       `yyyyyyyyyyy:  :yyyy/`           `/yyyy.  /yyyyyyyyyyy                        \033[94m 3. \033[93mSetup Multi - Node Cluster\033[34m
#                       /yyyyyyyyyyy`  oyyyyyo   .oso.   oyyyyy+  .yyyyyyyyyyy:
#                      `yyyyyyyyyyyy`  //:.`     -yyy.     `-://  `yyyyyyyyyyys                       \033[94m 4. \033[93mExit\033[34m
#                      :yyyyyyyo++/-       `.--    `    --.`       :/++oyyyyyyy-
#                      syyyyyyo``-/+/   +yyyyyy`   `   .yyyyyy+   /+/-``oyyyyyys
#                      syyyyyyyyyyyyy+   +yyyy-  `oy+   -yyyy+   oyyyyyyyyyyyyyo
#                      `+yyyyyyyyyyyyyo`  .oy:  `syyyo`  /yo.  `oyyyyyyyyyyyyy/
#                        .syyyyyyyyyyyyy/`  `  `syyyyys`  `  `/yyyyyyyyyyyyyo.
#                          :yyyyyyyyyyyyyy+.     `...`     .oyyyyyyyyyyyyyy:
#                           `+yyyyyyyyyyyyy. /+/:--.--:/+: -yyyyyyyyyyyyy+`
#                             -syyyyyyyyys. /yyyyyyyyyyyyy/ .syyyyyyyyys.
#                               /yyyyyyyyo-/yyyyyyyyyyyyyyy:-syyyyyyyy/
#                                .oyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyo`
#                                  :yyyyyyyyyyyyyyyyyyyyyyyyyyyyyys-
#                                   `+yyyyyyyyyyyyyyyyyyyyyyyyyyy/
#                                     `.-----------------------.
#
#      \033[36m
#    `sy:                .sy-                                             ``
#    `yy:                .yy-                                            oys
#    `yy: :ss: -ss` .ss- .yysyys+`  `+syys+`  +syyy+ /syyyyo.   /syyyo.  oyysso  :oyyyo:  .oyyyy-
#    `yyosy+`  :yy` .yy- .yy:`.oys `yy+..oys  yy+``` oys``oys  oys.`/yy. oys``` /yy-`-yy: +yy-``
#    `yysyy/   :yy` .yy- .yy-  /yy`-yysooooo  yy/    oys  /yy  yysooooo. oys    oyyooooo: `:oyys:
#    `yy:`oys. .yyo:/yy- .yy/:/yy/  oys/::/.  yy/    oys  /yy  /yy/::/-  /yy/:: -yy+::::  ::--sys
#     //.  ://` `:+++//` `//+++:.    -/+++/.  //-    :/:  -//   .:+++/-   -/++/` `:++++/  :++++:`
#     \033[0m
#     ''')


# def docker_config():
#     print(''' \033[96m
#                                            /yssssssy.
#                                            /y++++++h.                                                    \033[92m Select your choice:\033[96m
#                                            /y++++++h.
#                              .-------------+yooooood-                  `                              \033[92m----------------------------\033[96m
#                             `yysssssyysssssshssssssd.                `/so-`
#                             `hsoooooys+++++ohooooood.                /yooyo.
#                             `hsoooooys+++++ohooooood.               `ys+++sy.                       \033[94m 1. \033[93mDocker Configuration\033[96m
#                      .///////hysssssyyoooooshssssssh+//////-        `ho++++ss..---..`
#                      -hsssssshsoooooyysssssshoooooohssssssh/        `ss++++ohsyyssyss+`             \033[94m 2. \033[93mInstall Docker\033[96m
#                      -hooooooho+++++syooooosy++++++hooooooh/         -yoo++oooooooosy+`
#                      -hsoooooho+++++syooooosy++++++hooooooh+     ```.:syooooooosssso-               \033[94m 3. \033[93mCheck all created os \033[96m
#                :oooooshyyyyyyhysssssyyyyyyyyysssssshyyyyyyhsoooooossssooooyssso+/:.
#           `    oyooo++++++++++++++++o+++++++++++++++o++++++++++++++++ooooys`                        \033[94m 4. \033[93mDownload Docker Image\033[96m
#          `o/.``oyooooosso+++++++++++ooyyoo++++++o+osysoo++++++++++ooysssys` ```-o:`
#      ``-/ossso+shyyyyhhhhyyyssssyyyyhhhhhyyyssssyyyhhhhhyyysssssyyhhhhhhy+///+osss+:.`              \033[94m 5. \033[93mStart Docker Container Network Connectivity\033[96m
#                `hyyyssssssssssssssssssssssssssssssssssssssssssssyyyyyyh+
#                 +hyyysssssssssssss O ossssssssssssssssssssssyyyyyyyyyy-                             \033[94m 6. \033[93mCheck Docker Images\033[96m
#                 `ohyyyssssssssssss/ys/ssssssssssssssssssssyyyyyyyyyh/`
#                  `+hyyyyysssyyyyyysoossssssssssssssssssyyyyyyyyyyy+`                                \033[94m 7. \033[93mCreate and Configure Webserver\033[96m
#                    :ys+++++//:-..+sssssssssssssssyyyyyyyyyyyyyhs:`
#                     `/s+:-------.-/sssssssyyyyyyyyyyyyyyyyyys/.`                                    \033[94m 8. \033[93mCheck running os\033[96m
#                       `-+o+/--------+syyyyyyyyyyyyyyyyyys+:.
#                          `./+oo++//:::/oyyyyyyyyyyso+/-``                                           \033[94m 9. \033[93mDelete all created os \033[96m
#                              ``.-:://///++//::-.```
#                 ``                    \033[34m             `                                                \033[94m 10. \033[93mDelete Container Image !\033[34m
#                  -yy`                               sy:
#                  :dd`                               dd/                                             \033[94m 11. \033[93mDelete a Container !\033[34m
#         `-/+oo+:.:dd`   `-/+oo+/-`      `-/+oo+/-   dd/  ./+.   `.:+ooo/:.       .:/++-
#       `+yhyoooshhydd` `/yhysoosyhs:   `/yhyo++sys.  dd/`/yhs.  -shyso+oyhy+`   .oyhyso-             \033[94m 12. \033[93mExit !\033[34m
#      .yhy-`   `.+hhd``shy:`    ./hh+ `ohy:`    ``   dhsyhs:`  /hh+.`   .ohh+  -hho-`
#      /dh.        +dd`:dd.        /dd`-dd:           dhhy:`   `hd+    ./yhy/` `yds
#      +dh`        /dd`:dd`        :dd.-dd-           ddhs.    .hh+ `-ohhs-`   `yh+
#      .ydo.     `:hho `yds.`    `-yds `sdy-`         dhyhh+.   +dh/shho-``    `yh+
#       .shho/:/+shy/`  .ohhs+//+shh+`  `ohhs+//+so`  dd/-ohh+`  /yhdho/+os-   `yh+
#        `-/syyyso:.      -/osyyso:.      -/osyyso/`  oy-  -oy-   `:+syyyo/.    oy:
#
#     	\033[0m''')



def aws_config():
    print("\033[33m Please wait while downloading the dependency !")
    pip.main(['install', 'boto3'])
    import boto3
    ec2 = boto3.client('ec2')
    s3 = boto3.client('s3')
    os.system(clear_cmd)
    print()
    print()
    print('''\033[97m
       `.---::-.   `:::`-:/:` .-::.      .---.
      `.---.-::/:  `/++++oooo/ossss+   :syyyyys/   +ssssooo+  `-///:.    ... `..`                           \033[92m Select your choice:\033[97m
      ``..   -://` .+++/.-oooo/:+sss- .syy/-:yyy/  /ooosssso `ossoooo+`  /+/://::-                      \033[92m--------------------------------\033[97m
        `..--:://` .+++-  /ooo  .sss-  .--``.syy+     -ssso` /sso  :oo+  +++/.-:::`
      `.---..-://` .+++.  /ooo  .sss-  :oyyyyyyy+    /yyy+   sss/  `ooo. +++.  :::.                     \033[94m 1. \033[93m Installing Amazon CLI\033[97m
      .---   -://` .+++.  /ooo  .sss- :yyy:``syy+  `+yyy:    sss/   ooo- ++/.  -::`                     \033[94m 2. \033[93m List All AvailabilityZone !\033[97m
      .---``.:://- .+++.  /ooo  .sss- +yyy  .yyyo `oyyys+/-` +ss+  `ooo. ++/.  -::`                     \033[94m 3. \033[93m Configuring AWS CLI Tools\033[97m
      `.----:--:/- .+++.  /ooo  .sss- :yyyssyyyyy:.yyyyyysss`.sss:-/oo/  ++/.  -::`                     \033[94m 4. \033[93m List All Instances \033[97m
        ````   .`   .--`  .::-  `///`  -+ooo:`/o: `+:..`.-/+` .+soooo:`  ///`  -:-` \033[33m                    \033[94m 5. \033[93m Launch an Instance\033[33m
                 /+:`                             ./osyyso. *                                           \033[94m 6. \033[93m List All KeyPairs \033[33m
                  `/so/-`                         `-.-.-sh:                                             \033[94m 7. \033[93m Attach A Volume\033[33m
                    `:oyys+:-`                  `-/oyy/ yy`                                             \033[94m 8. \033[93m List All SecurityGroups\033[33m
                       ./oyyyyyso++//:::://++oyhhhho:` /y-                                              \033[94m 9. \033[93m Create S3 Bucket\033[33m
                          `-/+syyyyhhhhhhhhhhhyo/-`    +.                                               \033[94m 10. \033[93mList All Subnets\033[33m
                                `--://///::-.                                                           \033[94m 11. \033[93mAttach S3 bucket to CloudFront\033[33m
    		   	                                                                                \033[94m 12. \033[93mList All InstanceTypeOfferings!\033[33m
    			                                                                                \033[94m 13. \033[93mTerminate os\033[33m
    			                                                                                \033[94m 14. \033[93mList All Volume Created\033[33m
    			                                                                                \033[94m 15. \033[93mList All VolumeOffering\033[33m
                                                                                                        \033[94m 16. \033[93mExit\033[33m    					
    \033[0m''')


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning आदर्श Sir")

    elif 12 <= hour < 18:
        speak("Good Afternoon आदर्श Sir")

    else:
        speak("Good Evening आदर्श Sir")
    speak("How can i Help you Sir")


os.system(clear_cmd)
USER = getpass.getuser()
# print()
# print()
# print()
# print('''\033[91m		             .
# 		     -`     +`
# 		      /-   ++  -:`
# 		       :o. ys o:``
# 		      `.-ssoN+d +` -+`
# 		  `/shhyysyhNMMsd+:y`                \033[91m▄▀█ █▀▄ ▄▀█ █▀█ █▀ █░█   ▄▀█ █░█ ▀█▀ █▀█ █▀▄▀█ ▄▀█ ▀█▀ █ █▀█ █▄░█   █ █ █
# 		 `+oso+/:.+y:NMMMNNy                 \033[91m█▀█ █▄▀ █▀█ █▀▄ ▄█ █▀█   █▀█ █▄█ ░█░ █▄█ █░▀░█ █▀█ ░█░ █ █▄█ █░▀█   ▄ ▄ ▄
# 	      -/sdNNdsoss+--+sdMMmsd+
# 	   .+yydNMNy++m+`   ./+NMhymNh:`
# 	   -..yNMmys. -   `-:y:sNs+:ydNy`                                  \033[92mWelcome user\033[37m @\033[36m''', USER, '''\033[91m
# 	    .dNMMsMmo:  `ddoshhmN/-o``s.
# 	    yyyMM/NmMs  yMNd/-:-..``/-.`
# 	    o`sMMy/yhNy:hyh:s:       `-`
# 	    ` +MhMh/:/hNh..+`o         .`
# 	      .d.yMNho//:..- :
# 	       ::yoh+mNmdys+/:--..``
# 	       `hMh/:.+dNNhdNMNy//:/::.`
# 	       .yMMm.`.-/yh+::+ooo/:/oydho-`
# 	       .yMM/-o/:--...`     `.-+/hNh/-
# 		-dMsNh+:-.`           :h+sMm:
# 		 `omNNs/:-`           `ym+mMN+
# 		  `--:.```.`          .+ddyM+y/
# 	      `/+o+/+:..`           `:sdNyhM/`+`
# 	    .ohdyosydMdmh//:``--`.//+hmNh/MM-
# 	   /mh/` `.:+syhdmdmmy/ymsoMNdho/NMy
# 	  -Ns`       `-+ydmNNNNdNNmdhhyyoMy`
# 	  sM-             ``.--:ymmmho-`o+`
# 	  .Ms`             `-:/+/:.`  `-`
# 	   yMh/`       `..           `-:
# 	   `hMMNs+///:::.````   `:+::+/.
# 	     oNmmNmdhyso+/:.`   :/+/-`
# 	      -s/-+hNdysyssssoo+/-`
# 		./:.`:oo/-`
# 		   `-.`  .--.``
# 	\033[0m''')
#
# speak('Welcome to Adarsh Automation ')
# speak('Here is the list of Services which we can automate for you')
os.system(clear_cmd)
print()
print()
print()
# print('''\033[91m		             .
# 		     -`     +`
# 		      /-   ++  -:`
# 		       :o. ys o:``
# 		      `.-ssoN+d +` -+`
# 		  `/shhyysyhNMMsd+:y`                \033[91m▄▀█ █▀▄ ▄▀█ █▀█ █▀ █░█   ▄▀█ █░█ ▀█▀ █▀█ █▀▄▀█ ▄▀█ ▀█▀ █ █▀█ █▄░█   █ █ █
# 		 `+oso+/:.+y:NMMMNNy                 \033[91m█▀█ █▄▀ █▀█ █▀▄ ▄█ █▀█   █▀█ █▄█ ░█░ █▄█ █░▀░█ █▀█ ░█░ █ █▄█ █░▀█   ▄ ▄ ▄
# 	      -/sdNNdsoss+--+sdMMmsd+
# 	   .+yydNMNy++m+`   ./+NMhymNh:`
# 	   -..yNMmys. -   `-:y:sNs+:ydNy`                                  \033[92mWelcome user\033[37m @\033[36m''', USER, '''\033[91m
# 	    .dNMMsMmo:  `ddoshhmN/-o``s.
# 	    yyyMM/NmMs  yMNd/-:-..``/-.`
# 	    o`sMMy/yhNy:hyh:s:       `-`                                            \033[92m Select your choice:\033[91m
# 	    ` +MhMh/:/hNh..+`o         .`
# 	      .d.yMNho//:..- :                                                \033[92m------------------------------------\033[91m
# 	       ::yoh+mNmdys+/:--..``
# 	       `hMh/:.+dNNhdNMNy//:/::.`                                                   \033[94m 1. \033[93mBasic Linux\033[91m
# 	       .yMMm.`.-/yh+::+ooo/:/oydho-`
# 	       .yMM/-o/:--...`     `.-+/hNh/-                                              \033[94m 2. \033[93mYum\033[91m
# 		-dMsNh+:-.`           :h+sMm:
# 		 `omNNs/:-`           `ym+mMN+                                             \033[94m 3. \033[93mDocker\033[91m
# 		  `--:.```.`          .+ddyM+y/
# 	      `/+o+/+:..`           `:sdNyhM/`+`                                           \033[94m 4. \033[93mHadoop\033[91m
# 	    .ohdyosydMdmh//:``--`.//+hmNh/MM-
# 	   /mh/` `.:+syhdmdmmy/ymsoMNdho/NMy                                               \033[94m 5. \033[93mAmazon\033[91m
# 	  -Ns`       `-+ydmNNNNdNNmdhhyyoMy`
# 	  sM-             ``.--:ymmmho-`o+`                                                \033[94m 6. \033[93mAnsible\033[91m
# 	  .Ms`             `-:/+/:.`  `-`
# 	   yMh/`       `..           `-:                                                   \033[94m 7. \033[93mKubernetes\033[91m
# 	   `hMMNs+///:::.````   `:+::+/.
# 	     oNmmNmdhyso+/:.`   :/+/-`                                                     \033[94m 8. \033[93mExit\033[91m
# 	      -s/-+hNdysyssssoo+/-`
# 		./:.`:oo/-`
# 		   `-.`  .--.``
# 	\033[0m''')
#
# # speak('Shweta, Shweta, Shweta, Bolo na Shweta, aaaahhh, aaaaaaaaaaaahhhhhh, aaaaaaaaaahhhhhhhhh, aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaahhhhhhhhhhhhhhhhhhhhhhh')
#
# speak('What do want to Configure ? ')
#
# print('Listening . . .')
# cmd = listen()
# cmd = cmd.lower()
# print(cmd)

# if 'hadoop' in cmd:
#     hadoop_config()

#kubernetes_config()
# docker_config()
# aws_config()
