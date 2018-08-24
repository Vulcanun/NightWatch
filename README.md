# nightWatch
Night Watch is a defensive python script intended to implant bait directories wich log brute force directory listing attempts.


## Introduction
With the intent of detecting brute force directory listing, Night Watch selects random entries from common.txt (default wordlist for dirb, the most used tool for directory listing) and implants them with a bait script that logs client information.

## Usage
Night Watch's main parameter is the Main Directory, this directory is where the script will implant the bait directories and scripts.

```
python nightwatch.py <Main Directory> [<Additional Arguments>]

returns:

Testing received directory...
[+] We are good to go. 

Selecting random directories...
[+] 3 directories selected, creating...
[+] Successfully created ms-sql
[+]      ms-sql propulated with bait script.
[+] Successfully created email-a-friend
[+]      email-a-friend propulated with bait script.
[+] Successfully created baz
[+]      baz propulated with bait script.
```

## Limitations
As the scripts have to be interpreted by the server where the target application is hosted, the bait scripts have to be writen in the server's supported languages.
As of this moment, Night Watch only ships with the default index.php file as bait, although the -s | --source argument allows for the usage of custom bait scripts.

## Future Implementations
Additional bait scripts.
Log management web interface.
