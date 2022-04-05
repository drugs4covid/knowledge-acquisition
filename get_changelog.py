#!/usr/bin/python3
 
import sys
import re
import json

def get_changelog(day):
    """
    Function to download the changelog of the selected day from the web.
    
    Parameters:
    
    - day (String): Date of the publication of the changelog to be downloaded.
    
    Returns:
    
    - False (Boolean): If the request failed or no changelog file was found for the day specified.
    - r.text (String): Contents of the changelog file.
    
    """
    import requests
    import re
    try:
        r = requests.get("https://ai2-semanticscholar-cord-19.s3-us-west-2.amazonaws.com/{}/changelog".format(day), stream=True)
    except Exception:
        print("Warning, the request failed, ", Exception)
        return False
    
    if r.status_code != 200:
        return False
    
    return r.text


def extract_latest_changelog(changelog):
    """
    Function to extract only the latest changes from the changelog file.
    
    Parameters:
    
    - changelog (String): Contents of the changelog file
    
    Returns:
    
    - latest_changelog (String): Latest changes specified on the changelog file.
    """
    
    import re
    
    text = changelog.split("\n")
    latest_changelog = []
    i = 0
    finished = False
    
    while not finished:
        latest_changelog.append(text[i])
        i += 1
        if re.search(r'20\d\d-\d\d-\d\d', text[i]):
            finished=True
        if i > 99:
            finished=True

    latest_changelog = "\n".join(latest_changelog)
    return latest_changelog
    

if __name__ == "__main__":
    
    input_date = str(sys.stdin)
    if re.search(r'No update was found', input_date):
        sys.stdout.write("No update found")
        exit
    
    changelogs = get_changelog(str(sys.stdin))
    changelog = extract_latest_changelog(changelogs)
    sys.stdout.write(json.dumps({"changelog":changelog}))
    