#######################################################
#
# COSC 140 Homework 2, "bus trip planner" problem
#
#######################################################

'''
depature = input("When are you departing (HH:MM) ")
aHour=int(depature[0:2])
aMin=int(depature[3:])
aSec=0
distance= int(input("How far are you traveling (km) "))
stops= int(input("How many stops will the bus do "))


#Compute the arrival time assuming the bus travels, on average, at 40 km/h, and that each stop takes 30 seconds.  Your input departure time can just be in hours/minutes, but your output should include hours, minutes, and seconds.


#Find total time of travel
#calculating whether to add stops time in mins or seconds
if stops%2==0:
  stopTime= (30* stops)/60
  aMin+=stopTime
else:
  stopTime= (30* stops)//60
  stopTimeSeconds= (30* stops)%60
  aMin+=stopTime
  aSec+=stopTimeSeconds
# calculating if whether to add distance in hours or 
#in mins 

dMins= ((distance/40)*60) 

if (dMins%1) != 0 :    # TAKE CARE OF SECS FROM KM TRAVEL
  aSec += (dMins%1)*60


if dMins<60:
  aMin+=dMins
else:
  aHour+= dMins//60
  aMin+= dMins%60
# handle kilometers 



#Handle outside condtions 
if aSec>59:
  aMin+=1
  aSec= aSec%60
if aMin>59:
  aHour+=1
  aMin= aMin%60
if aHour>=24:
  aHour= 0 + aHour%24

print(f"You will arrive at {int(aHour):02d}:{int(aMin):02d}:{int(aSec):02d} GMT ")

'''