#!/usr/bin/python3

## Code that checks the cord-19 update of the last 31 days

def cord19(date):
	"""
	Function to assess if an update to the CORD-19 was made at the day specified.
	
	Parameters:
	
	 - date (String): A string indicating the day to check for.
	 
	 Returns:
	 
	 - False (Boolean): If no update was made to the CORD-19 in the day specified.
	 - True (Boolean): If an update was detected on the day specified.
	"""
	import requests
	try:
		r = requests.get("https://ai2-semanticscholar-cord-19.s3-us-west-2.amazonaws.com/{}/document_parses.tar.gz".format(date), stream=True)
		if r.status_code == 200:
			return True
		
	except Exception:
		print("Warning, the request failed", Exception)
		pass
	return False


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
	
	today = date.today()
	range_days = []
	for day in range(number_of_days):
		range_days.append(str(today - timedelta(day)))		
	
	found_update=False
	for day in range_days:
		try:
			# print("here I try to get the document cord-19_{}.tar.gz from the web".format(day))
			if cord19(day):
				found_update=True
				break
			next
		except Exception:
			print("An error occurred while trying to assess if an update was made", Exception)

	
	if found_update:
		# print("An update was found on the CORD-19 at the date {}".format(day))
		return day
	
	# print("No update was found on the web in the last {} days".format(number_of_days))
	return False
	
	

if __name__ == "__main__":
    import sys
    number_of_days = 31
    #FIXME:
    # if (len(sys.argv) > 1):
    #     number_of_days = int(sys.argv[1])
    
    date = check_cord19_update(number_of_days)
    if not date:
        sys.stdout.write("No update was found")
    if date:
        sys.stdout.write(str(date))