# SkyNet

SkyNet is a tool used to monitor contributions accross a GitHub organization.  By simply running a python script, you will get a report of user activity over all repositories in the org over the given time period

## Requirements

Python version 3.9.5 or newer. [link](https://www.python.org/downloads/)

PIP version 21.1.3 or newer. [link](https://pip.pypa.io/en/stable/installing/)

## Installing Modules

run `pip install -r requirements.txt`

## Configuration

You will need to create a configuration file named `SkyNetConfig.json`

The file should be placed in the same directory as your `script.py` file

The `SkyNetConfig.json` file needs to contain 2 fields
- `"org"`: the name of the organization you want to monitor
- `"token"`: the GitHub API token associated with the org 
  - must have `org:admin` access level
  - for instruction on how to generate your own API token, look [here](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token)

### Example Configuration File

``` 
{
    "org": "2102Mule-Nick",
    "token": "laksdhfOIHSDFOlksadhf203948"
} 
```

## Execution

To run SkyNet, simply run the command `py script.py` in the directory of the `script.py`.

This will give you a list of all contributers to all repos in your org for the last 24 hours and give you a total of numbers of lines added and number of lines removed accross all commits on all reops.

### Arguments

SkyNet takes up to one or two arguments.  Either a start date, or a start and end date.  If given just a start date, SkyNet will only look at commits for a 24 hr period starting on the date specified.  If given a start and end date, it will only look at commites between those two dates.

Arguments must be given in the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.  ie. YYYY-MM-DDTHH:MM:SSZ

Example running Skynet for the day of March 17th, 2021 `py script.py 2021-03-17T00:00:00Z`

Example running Skynet for the time between March 17th and March 19th 2021 `py script.py 2021-03-17T00:00:00Z 2021-03-19T23:59:59Z`

## Output

SkyNet will begin by outputting the Start date and End date selected for this execution.  Then it will output the name of each repository as it is being checked.  Finally it will print out the results in the form of a JSON object.

The result JSON will have keys of the usernames of each contributor to the org.  Each key will have a JSON object value that will have the `linesAdded` and  `linesRemoved`

#### Example Output

```
Start date: 2021-03-17T00:00:00Z
End date: 2021-03-18T00:00:00Z
Checking repo: 2102-mule-nick-week1java-tugbaozdn
Checking repo: gael_gohoungo_p1
Checking repo: IyadClient
Checking repo: DivyeshClient
Checking repo: davronsoapclient3
Checking repo: Josh_Cushing_Project1.3
Checking repo: Brian_Callahan_P1
Checking repo: DanielBeintemaP1
Checking repo: Keyur_Patel_P1
Checking repo: divyeshkumar_patel_p1
Checking repo: diego_franchi_p1
Checking repo: zephyr_zambrano_p2
Checking repo: carlos_quimson_p2
Checking repo: iyad_shobaki_p2
Checking repo: chris_proutt_p2
Checking repo: tugba_ozden_p2
{   'BrianCallahan': {'linesAdded': 678, 'linesRemoved': 95},
    'Gael22': {'linesAdded': 1305, 'linesRemoved': 0},
    'IyadShobaki': {'linesAdded': 1244, 'linesRemoved': 0},
    'cproutt': {'linesAdded': 561, 'linesRemoved': 23},
    'davrontairov': {'linesAdded': 521, 'linesRemoved': 0},
    'didoi': {'linesAdded': 2420, 'linesRemoved': 22079},
    'diegofranchi': {'linesAdded': 481, 'linesRemoved': 0},
    'divyesh4878': {'linesAdded': 1644, 'linesRemoved': 0},
    'jurczakn': {'linesAdded': 508, 'linesRemoved': 27},
    'kevnovikov': {'linesAdded': 326, 'linesRemoved': 0},
    'melodyxmw': {'linesAdded': 609, 'linesRemoved': 0},
    'tugbaozdn': {'linesAdded': 817, 'linesRemoved': 9},
    'web-flow': {'linesAdded': 58, 'linesRemoved': 1},
    'zephyrzambrano': {'linesAdded': 4591, 'linesRemoved': 0}}
    
```
