from math import *

def convert_decimal_number(response):
	decimal_value =input("Enter Decimal number:- ")
	response=int(response);
	if(response==1 or response==3):
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
		print("\033[0m"+"Hex value is "+"\033[1;32;40m"+"0x"+hex_value+"\033[0m");
	if(response==2 or response==3):
		binary_value=""
		remainder=0;
		divisor=1;
		dividend=int(decimal_value);
		while(dividend>0):
			divisor=int(dividend/2);
			remainder=int(dividend%2);
			binary_value=str(remainder)+binary_value;
			dividend=divisor;
		print("Binary value is "+"\033[1;32;40m"+binary_value);

response=input("1.Convert Decimal to Hex\n"
	           "2.Convert Decimal to Binary\n"
	           "3.Convert Decimal to both Hex and Binary\n");
convert_decimal_number(response);

