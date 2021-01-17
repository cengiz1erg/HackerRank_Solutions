Regex_Pattern = r"^(\d{8}|(\d\d\-\d\d\-\d\d\-\d\d))$"	   #  using backreferences  ------->  ^\d\d(-?)(\d\d\1){2}\d\d$    

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
