# 

def check_cord19_update(number_of_days=7):
	"""
	Function to check if an update has been provided for the CORD-19 corpus in the last x days.
	
	Parameters:
	
	- number_of_days (Integer, default = 7): Number of days to check for an updated corpus.
	
	Returns:
	
	- day (String): A string indicating the day that the cord-19 was last updated.
	- False (Boolean): If no update was found in the last x days.
	"""
	from datetime import date, timedelta
	import wget
	today = date.today()
	range_days = []
	for day in range(number_of_days):
		range_days.append(str(today - timedelta(day)))
	
	for day in range_days:
		try:
			print("here I try to get the document cord-19_{}.tar.gz from the web".format(day))
			# prueba = wget.download("https://ai2-semanticscholar-cord-19.s3-us-west-2.amazonaws.com/historical_releases/cord-19_{}.tar.gz".format(day))
			next
		except Exception:
			print("CORD-19 was not updated in the day {}".format(day))

	print("No CORD-19 update was detected in the last {} days".format(number_of_days))
	return False
	
	
	
if __name__ == '__main__':
	import sys
	number_of_days=7
	if (len(sys.argv) > 1):
		number_of_days = int(sys.argv[1])
	check_cord19_update(number_of_days)