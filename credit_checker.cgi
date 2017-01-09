#--
import cgi
import cgitb
cgitb.enable()

#Prints form
def generate_form(name= '', hours=''):
	print ("<form method='get'> ")
	print ("<table>")

	print ("<tr><td>Enter name:</td><td><input type='text' name='name' value='" + name + "' /></td></tr>\n")
	print ("<tr><td>Credit Hours:</td><td><input type='text' name='hours' value='" + hours + "' /></tr>\n")
	print ("<tr><td><input type='submit' name='submitHours' /></td><td></td></tr>\n")
	print ("</table>")
	print ("</form>\n")
    
#Main Method
def main() :

	print("Content-Type: text/html\n\n")
	
	print("<style>body { padding: 50px; background-color: pink; } </style>")
	

	
	print("<h3>Credit Hour Checker</h3>\n")
	form = cgi.FieldStorage()
	if form :
		name=''
		hours=''
		name = form.getfirst('name', '')
		hours= form.getfirst('hours', '')
		print("Credit Hours: ",hours, " Name: ", name, "<br />\n")
		if hours == '' or name== '':
			print("<h3> you must enter data for both values </h3>\n")
			generate_form(name, hours)
		else:
			try:
				hours = int(hours)
				print (" Your hours: " , str(hours), "<br />\n")
				if hours <= 29:
					print ("Hi " +name + ". You are a Freshman because you have " + str(hours) + " credit hours")
				elif( hours > 29 and hours <= 59):
					print ("Hi " +name + ". You are a Sophomore because you have " + str(hours) + " credit hours")
				elif( hours > 59 and hours <= 89):
					print ("Hi " +name + ". You are a Junior because you have " + str(hours) + " credit hours")
				elif( hours > 89 and hours <= 120):
					print ("Hi " +name + ". You are a Senior because you have " + str(hours) + " credit hours")
				elif( hours > 121):
					print ("Hi " +name + ". You must be a graduate because you have" + str(hours) + " credit hours")
			except:
				hours=''
				print ("Please enter a whole number of credit hours. <br />\n")
				generate_form(name, hours)
	else:
		print ("<h4> Please enter data below:</h4>\n")
		generate_form()	

main()
