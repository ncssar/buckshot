#
# buckshot - given a set of numbers and a marker name, make sarsoft markers
#  corresponding to all three lat-lon coordinate systems
#

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import regex as re
from parse import *
import sys
import requests
import json

from buckshot_ui import Ui_buckshot

class MyWindow(QDialog,Ui_buckshot):
	def __init__(self,parent):
		QDialog.__init__(self)
		self.setWindowFlags(self.windowFlags()|Qt.WindowMinMaxButtonsHint)
		self.parent=parent
		self.ui=Ui_buckshot()
		self.ui.setupUi(self)
		self.setAttribute(Qt.WA_DeleteOnClose)
		self.coordDdStringList=[]
		self.coordDMmStringList=[]
		self.coordDMSsStringList=[]


	# calcLatLon - make guesses about actual coordinates based on a string of numbers
	#  called from textChanged of numbersField

	# assumptions:
	#  - Degrees Latitude is a two-digit number starting with 2, 3, or 4
	#  - Degrees Longitude is a three-digit number starting with one, second digit
	#   either 0, 1, or 2
	#  - space or minus sign is a known delimiter and assumed to be correct

	def calcLatLon(self):

### code to get overlapping matches (i.e. each possible longitude whole number) and their indeces:
##import regex as re
##matches=re.finditer("1[012][0123456789]",numbers,overlapped=True)
##[match.span() for match in matches]

		numbers=self.ui.numbersField.text()
		self.coordDdStringList=[]
		self.coordDMmStringList=[]
		self.coordDMSsStringList=[]
		latDegIndex=0
		lonDegIndex=-1
		pattern=re.compile('1[012][0123456789]') # assume longitude 100-129 west
		matches=pattern.finditer(numbers,2,overlapped=True)
##		print(str([match.span() for match in matches]))
		for lonDegMobj in matches:
			print(str(lonDegMobj.span()))
##		lonDegMobj=pattern.search(numbers,2) # skip the first two characters
##		if lonDegMobj!=None:
			lonDegIndex=lonDegMobj.start()
			lonDeg=lonDegMobj.group()
			print("lonDegIndex: '"+str(lonDegIndex)+"'")
			print("Longitude Degrees: '"+lonDeg+"'")
			lonRestIndex=lonDegIndex+3
			lonRest=numbers[lonRestIndex:]
			print("Longitude rest: '"+lonRest+"'")
			if int(numbers[0])>1 and int(numbers[0])<5: #assume latitude 20-49 north
				latDeg=numbers[0:2]
				latRest=numbers[2:lonDegIndex]
				print("Latitude degrees: '"+latDeg+"'")
				print("Latitude rest: '"+latRest+"'")

				# initialize whole minutes and seconds to unrealizable values
				#  for use in the 'possible' section below
				latMin1="99"
				latMin2="99"
				latSec11="99"
				latSec12="99"
				latSec21="99"
				latSec22="99"

				lonMin1="99"
				lonMin2="99"
				lonSec11="99"
				lonSec12="99"
				lonSec21="99"
				lonSec22="99"

				# initialize "rest" arguments to blank strings
				latMin1Rest=""
				latMin2Rest=""
				latSec11Rest=""
				latSec12Rest=""
				latSec21Rest=""
				latSec22Rest=""

				lonMin1Rest=""
				lonMin2Rest=""
				lonSec11Rest=""
				lonSec12Rest=""
				lonSec21Rest=""
				lonSec22Rest=""

				# parse minutes and seconds from the rest of the string
				# whole minutes and whole seconds could be one digit or two digits
				if len(latRest)>0:
					print("t1")
					latMin1=latRest[0]
					if len(latRest)>1:
						print("t2")
						latMin1Rest=latRest[1:]
						latMin2=latRest[0:2]
						if len(latRest)>2:
							print("t2.5")
							latMin2Rest=latRest[2:]
						if len(latMin1Rest)>0:
							print("t3")
							latSec1=latMin1Rest[0:]
							if len(latSec1)>0:
								print("t4")
								latSec11=latSec1[0]
								if len(latSec1)>1:
									print("t5")
									latSec11Rest=latSec1[1:]
									latSec12=latSec1[0:2]
									if len(latSec1)>2:
										print("t5.5")
										latSec12Rest=latSec1[2:]
									if len(latMin2Rest)>0:
										print("t6")
										latSec2=latMin2Rest[0:]
										if len(latSec2)>0:
											print("t7")
											latSec21=latSec2[0]
											if len(latSec2)>1:
												print("t8")
												latSec21Rest=latSec2[1:]
												latSec22=latSec2[0:2]
												if len(latSec2)>2:
													print("t9")
													latSec22Rest=latSec2[2:]
								else:
									latSec2="0" # account for implied zero seconds
									latSec21="0"
						else:
							latSec1="0" # account for implied zero seconds
							latSec11="0"

				if len(lonRest)>0:
					lonMin1=lonRest[0]
					if len(lonRest)>1:
						lonMin1Rest=lonRest[1:]
						lonMin2=lonRest[0:2]
						if len(lonRest)>2:
							lonMin2Rest=lonRest[2:]
						if len(lonMin1Rest)>0:
							lonSec1=lonMin1Rest[0:]
							if len(lonSec1)>0:
								lonSec11=lonSec1[0]
								if len(lonSec1)>1:
									lonSec11Rest=lonSec1[1:]
									lonSec12=lonSec1[0:2]
									if len(lonSec1)>2:
										lonSec12Rest=lonSec1[2:]
									if len(lonMin2Rest)>0:
										lonSec2=lonMin2Rest[0:]
										if len(lonSec2)>0:
											lonSec21=lonSec2[0]
											if len(lonSec2)>1:
												lonSec21Rest=lonSec2[1:]
												lonSec22=lonSec2[0:2]
												if len(lonSec2)>2:
													lonSec22Rest=lonSec2[2:]
								else:
									lonSec2="0" # account for implied zero seconds
									lonSec21="0"
						else:
							lonSec1="0" # account for implied zero seconds
							lonSec11="0"


				# set flags as to which ones are possible
				# (whole min/sec <60 (2-digit) or <10 (1-digit))
				latMin1Possible=int(latMin1)<10
				latMin2Possible=int(latMin2)<60
				latSec11Possible=int(latSec11)<10
				latSec12Possible=int(latSec12)<60
				latSec21Possible=int(latSec21)<10
				latSec22Possible=int(latSec22)<60

				lonMin1Possible=int(lonMin1)<10
				lonMin2Possible=int(lonMin2)<60
				lonSec11Possible=int(lonSec11)<10
				lonSec12Possible=int(lonSec12)<60
				lonSec21Possible=int(lonSec21)<10
				lonSec22Possible=int(lonSec22)<60

				print("latMin1Possible:"+str(latMin1Possible)+":"+latMin1+":"+latMin1Rest)
				print("latMin2Possible:"+str(latMin2Possible)+":"+latMin2+":"+latMin2Rest)
				print("latSec11Possible:"+str(latSec11Possible)+":"+latSec11+":"+latSec11Rest)
				print("latSec12Possible:"+str(latSec12Possible)+":"+latSec12+":"+latSec12Rest)
				print("latSec21Possible:"+str(latSec21Possible)+":"+latSec21+":"+latSec21Rest)
				print("latSec22Possible:"+str(latSec22Possible)+":"+latSec22+":"+latSec22Rest)

				print("lonMin1Possible:"+str(lonMin1Possible)+":"+lonMin1+":"+lonMin1Rest)
				print("lonMin2Possible:"+str(lonMin2Possible)+":"+lonMin2+":"+lonMin2Rest)
				print("lonSec11Possible:"+str(lonSec11Possible)+":"+lonSec11+":"+lonSec11Rest)
				print("lonSec12Possible:"+str(lonSec12Possible)+":"+lonSec12+":"+lonSec12Rest)
				print("lonSec21Possible:"+str(lonSec21Possible)+":"+lonSec21+":"+lonSec21Rest)
				print("lonSec22Possible:"+str(lonSec22Possible)+":"+lonSec22+":"+lonSec22Rest)

				# zero-pad right-of-decimal if needed, i.e. no blank strings right-of-decimal

				latRest=latRest or "0"
				lonRest=lonRest or "0"
				latMin1Rest=latMin1Rest or "0"
				latMin2Rest=latMin2Rest or "0"
				lonMin1Rest=lonMin1Rest or "0"
				lonMin2Rest=lonMin2Rest or "0"
				latSec11Rest=latSec11Rest or "0"
				latSec12Rest=latSec12Rest or "0"
				latSec21Rest=latSec21Rest or "0"
				latSec22Rest=latSec22Rest or "0"
				lonSec11Rest=lonSec11Rest or "0"
				lonSec12Rest=lonSec12Rest or "0"
				lonSec21Rest=lonSec21Rest or "0"
				lonSec22Rest=lonSec22Rest or "0"

				# build the lists of possible coordinate strings for each coordinate system
				#  (if only one of lat/lon per pair is possible, then the pair is
				#   not possible)

				self.coordDdStringList.append(str(latDeg+"."+latRest+"deg N x "+lonDeg+"."+lonRest+"deg W"))

				if latMin1Possible and lonMin1Possible:
					self.coordDMmStringList.append(str(latDeg+"deg "+latMin1+"."+latMin1Rest+"min N x "+lonDeg+"deg "+lonMin1+"."+lonMin1Rest+"min W"))
				if latMin1Possible and lonMin2Possible:
					self.coordDMmStringList.append(str(latDeg+"deg "+latMin1+"."+latMin1Rest+"min N x "+lonDeg+"deg "+lonMin2+"."+lonMin2Rest+"min W"))
				if latMin2Possible and lonMin1Possible:
					self.coordDMmStringList.append(str(latDeg+"deg "+latMin2+"."+latMin2Rest+"min N x "+lonDeg+"deg "+lonMin1+"."+lonMin1Rest+"min W"))
				if latMin2Possible and lonMin2Possible:
					self.coordDMmStringList.append(str(latDeg+"deg "+latMin2+"."+latMin2Rest+"min N x "+lonDeg+"deg "+lonMin2+"."+lonMin2Rest+"min W"))

				if latSec11Possible and lonSec11Possible:
					self.coordDMSsStringList.append(str(latDeg+"deg "+latMin1+"min "+latSec11+"."+latSec11Rest+"sec N x "+lonDeg+"deg "+lonMin1+"min "+lonSec11+"."+lonSec11Rest+"sec W"))
				if latSec11Possible and lonSec12Possible:
					self.coordDMSsStringList.append(str(latDeg+"deg "+latMin1+"min "+latSec11+"."+latSec11Rest+"sec N x "+lonDeg+"deg "+lonMin1+"min "+lonSec12+"."+lonSec12Rest+"sec W"))
				if latSec11Possible and lonSec21Possible:
					self.coordDMSsStringList.append(str(latDeg+"deg "+latMin1+"min "+latSec11+"."+latSec11Rest+"sec N x "+lonDeg+"deg "+lonMin2+"min "+lonSec21+"."+lonSec21Rest+"sec W"))
				if latSec11Possible and lonSec22Possible:
					self.coordDMSsStringList.append(str(latDeg+"deg "+latMin1+"min "+latSec11+"."+latSec11Rest+"sec N x "+lonDeg+"deg "+lonMin2+"min "+lonSec22+"."+lonSec22Rest+"sec W"))
				if latSec12Possible and lonSec11Possible:
					self.coordDMSsStringList.append(str(latDeg+"deg "+latMin1+"min "+latSec12+"."+latSec12Rest+"sec N x "+lonDeg+"deg "+lonMin1+"min "+lonSec11+"."+lonSec11Rest+"sec W"))
				if latSec12Possible and lonSec12Possible:
					self.coordDMSsStringList.append(str(latDeg+"deg "+latMin1+"min "+latSec12+"."+latSec12Rest+"sec N x "+lonDeg+"deg "+lonMin1+"min "+lonSec12+"."+lonSec12Rest+"sec W"))
				if latSec12Possible and lonSec21Possible:
					self.coordDMSsStringList.append(str(latDeg+"deg "+latMin1+"min "+latSec12+"."+latSec12Rest+"sec N x "+lonDeg+"deg "+lonMin2+"min "+lonSec21+"."+lonSec21Rest+"sec W"))
				if latSec12Possible and lonSec22Possible:
					self.coordDMSsStringList.append(str(latDeg+"deg "+latMin1+"min "+latSec12+"."+latSec12Rest+"sec N x "+lonDeg+"deg "+lonMin2+"min "+lonSec22+"."+lonSec22Rest+"sec W"))
				if latSec21Possible and lonSec11Possible:
					self.coordDMSsStringList.append(str(latDeg+"deg "+latMin2+"min "+latSec21+"."+latSec21Rest+"sec N x "+lonDeg+"deg "+lonMin1+"min "+lonSec11+"."+lonSec11Rest+"sec W"))
				if latSec21Possible and lonSec12Possible:
					self.coordDMSsStringList.append(str(latDeg+"deg "+latMin2+"min "+latSec21+"."+latSec21Rest+"sec N x "+lonDeg+"deg "+lonMin1+"min "+lonSec12+"."+lonSec12Rest+"sec W"))
				if latSec21Possible and lonSec21Possible:
					self.coordDMSsStringList.append(str(latDeg+"deg "+latMin2+"min "+latSec21+"."+latSec21Rest+"sec N x "+lonDeg+"deg "+lonMin2+"min "+lonSec21+"."+lonSec21Rest+"sec W"))
				if latSec21Possible and lonSec22Possible:
					self.coordDMSsStringList.append(str(latDeg+"deg "+latMin2+"min "+latSec21+"."+latSec21Rest+"sec N x "+lonDeg+"deg "+lonMin2+"min "+lonSec22+"."+lonSec22Rest+"sec W"))
				if latSec22Possible and lonSec11Possible:
					self.coordDMSsStringList.append(str(latDeg+"deg "+latMin2+"min "+latSec22+"."+latSec22Rest+"sec N x "+lonDeg+"deg "+lonMin1+"min "+lonSec11+"."+lonSec11Rest+"sec W"))
				if latSec22Possible and lonSec12Possible:
					self.coordDMSsStringList.append(str(latDeg+"deg "+latMin2+"min "+latSec22+"."+latSec22Rest+"sec N x "+lonDeg+"deg "+lonMin1+"min "+lonSec12+"."+lonSec12Rest+"sec W"))
				if latSec22Possible and lonSec21Possible:
					self.coordDMSsStringList.append(str(latDeg+"deg "+latMin2+"min "+latSec22+"."+latSec22Rest+"sec N x "+lonDeg+"deg "+lonMin2+"min "+lonSec21+"."+lonSec21Rest+"sec W"))
				if latSec22Possible and lonSec22Possible:
					self.coordDMSsStringList.append(str(latDeg+"deg "+latMin2+"min "+latSec22+"."+latSec22Rest+"sec N x "+lonDeg+"deg "+lonMin2+"min "+lonSec22+"."+lonSec22Rest+"sec W"))
			else:
				print("Latitiude not found.")
		else:
			print("Longitude not found.")

		self.ui.DdField.setPlainText("\n".join(self.coordDdStringList))
		self.ui.DMmField.setPlainText("\n".join(self.coordDMmStringList))
		self.ui.DMSsField.setPlainText("\n".join(self.coordDMSsStringList))

		print("Possible Dd coordinates:\n"+str(self.coordDdStringList))
		print("Possible DMm coordinates:\n"+str(self.coordDMmStringList))
		print("Possible DMSs coordinates:\n"+str(self.coordDMSsStringList))

	def createMarkers(self):
		print("createMarkers called")
		DdIdx=0
		DMmIdx=0
		DMSsIdx=0
		DdIdxFlag=len(self.coordDdStringList)>1
		DMmIdxFlag=len(self.coordDMmStringList)>1
		DMSsIdxFlag=len(self.coordDMSsStringList)>1

		markerName=self.ui.markerNameField.text()
		if markerName=="":
			markerName="X"

		# build a list of markers; each marker is a list:
		# [markerName,lat,lon,color]
		markerList=[]
		for DdString in self.coordDdStringList:
			DdIdx=DdIdx+1
			print("  Dd : '"+DdString+"'")
			r=parse("{:g}deg N x {:g}deg W",DdString)
			print(r)
			if DdIdxFlag:
				idx=str(DdIdx)
			else:
				idx=""
			markerList.append([markerName+"_Dd"+idx,r[0],-r[1],"#FF0000"])
		for DMmString in self.coordDMmStringList:
			DMmIdx=DMmIdx+1
			print("  DMm : "+DMmString)
			r=parse("{:g}deg {:g}min N x {:g}deg {:g}min W",DMmString)
			print(r)
			if DMmIdxFlag:
				idx=str(DMmIdx)
			else:
				idx=""
			markerList.append([markerName+"_DMm"+idx,r[0]+r[1]/60.0,-(r[2]+r[3]/60.0),"#FF00FF"])
		for DMSsString in self.coordDMSsStringList:
			DMSsIdx=DMSsIdx+1
			print("  DMSs: "+DMSsString)
			r=parse("{:g}deg {:g}min {:g}sec N x {:g}deg {:g}min {:g}sec W",DMSsString)
			print(r)
			if DMSsIdxFlag:
				idx=str(DMSsIdx)
			else:
				idx=""
			markerList.append([markerName+"_DMSs"+idx,r[0]+r[1]/60.0+r[2]/3600.0,-(r[3]+r[4]/60.0+r[5]/3600.0),"#0000FF"])

		print("Final marker list:")
		print(str(markerList))

		s=requests.session()
		s.get(self.ui.URLField.text())
		for marker in markerList:
			j={}
			j['label']=marker[0]
			j['folderId']=None
			j['url']=marker[3]
			j['comments']=""
			j['position']={"lat":marker[1],"lng":marker[2]}
			r=s.post("http://localhost:8080/rest/marker/",data={'json':json.dumps(j)})


def main():
	app = QApplication(sys.argv)
	w = MyWindow(app)
	w.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
    main()
