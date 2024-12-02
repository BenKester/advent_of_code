# advent_of_code
Submission repo for adventofcode.com

## Automation
This script/repo/tool does follow the automation guidelines on the /r/adventofcode community wiki (and link to this article that you're currently reading right now [https://reddit.com/r/adventofcode/wiki/faqs/automation] somewhere). Specifically:

- Throttle isn't implemented for this single user single download case
- Once inputs are downloaded, they are cached locally (download.load)
  - Not supporting manualDownloadFunction() until needed
- The User-Agent header in download.get_agent_header() is set to me since I maintain this tool :)
