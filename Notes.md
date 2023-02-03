Get All js Files- gau cdn.robinhood.com |  httpx -silent | grep '.js$'

How To

Step 1: Use `collectJsFiles.sh` to collect all the js files from a file containing subdomains </br></br>
Step 2: Run `filterByStatusCode.py` it will retrun all the js files having response code of `200` that means they are alive </br></br>
Step 3: Run `findSensitiveInJs.py` it will find all the sensitive strings inside those js files (sending request to each js file and finding the matching strings inside the response)
