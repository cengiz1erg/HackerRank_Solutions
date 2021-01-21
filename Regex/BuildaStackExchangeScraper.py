import re, sys

string_file = sys.stdin.read()

pattern_identifier = r'question-summary-([0-9]{5})'
pattern_hyperlink = r'class="question-hyperlink">(.*)</a></h3>'
pattern_time = r'asked.*"relativetime">(.*)</span>'

list_identifiers = re.findall(pattern_identifier, string_file)
list_hypelinks = re.findall(pattern_hyperlink, string_file)
list_times = re.findall(pattern_time, string_file)

for a,b,c in zip(list_identifiers, list_hypelinks, list_times):
    print(a + ";" + b + ";" + c)
