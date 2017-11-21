import urllib2
import json
import sys

location = raw_input("Enter the Coordinate: ");
radius = raw_input("Enter the radius (in meters) : ");
keyword = raw_input("Enter the keyword: ");

#url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=43.5831087,-79.6716622&radius=50000&keyword=pet&key=AIzaSyAO73ICYleowl51du_Ovk2Y_sbHK2maK1A';

base = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?";

def combineUrl(location, radius, keyword):
	return base + "location="+ location + "&radius=" + radius + "&keyword=" + keyword + "&key=AIzaSyAO73ICYleowl51du_Ovk2Y_sbHK2maK1A";

response = urllib2.urlopen(combineUrl(location, radius, keyword)).read();

j = json.loads(response);

results = j['results'];

def getAddr(text):
	rtn = '';
	for c in text:
		if c != ',':
			rtn += c;
	
	return rtn;
			


def output(jsonObject):
	for i in results:

		for j in i["types"]:
			print (i["name"] + ", " + getAddr(i["vicinity"]) + ", " + j + ", " + str(i["opening_hours"]["open_now"]));
	return;

#output(results);

def writeFn(jsonObject):
	f = open('output.csv', 'w');
	for i in results:

		for j in i["types"]:
			#print (i["name"] + ", " + getAddr(i["vicinity"]) + ", " + j + ", " + str(i["opening_hours"]["open_now"]));
			tmp = i["name"] + ", " + getAddr(i["vicinity"]) + ", " + j + ", " + str(i["opening_hours"]["open_now"]) + '\n';
			f.write(tmp);

	f.close();
	return;

writeFn(results);