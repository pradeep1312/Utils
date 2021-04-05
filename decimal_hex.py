from math import *

def convert_decimal_to_hex():
	decimal_value =input("Enter Decimal number:- ")
	hex_value=""
	remainder=0;
	divisor=1;
	dividend=int(decimal_value);
	while(dividend>0):
		divisor=int(dividend/16);
		remainder=int(dividend%16);
		if(remainder>9):
			if(remainder==10):
				hex_value="A"+hex_value;
			if(remainder==11):
				hex_value="B"+hex_value;
			if(remainder==12):
				hex_value="C"+hex_value;
			if(remainder==13):
				hex_value="D"+hex_value;
			if(remainder==14):
				hex_value="E"+hex_value;
			if(remainder==15):
				hex_value="F"+hex_value;

		else:
			hex_value=str(remainder)+hex_value;
		dividend=divisor;
	print("Hex value is "+"\033[1;32;40m"+"0x"+hex_value);

convert_decimal_to_hex();

