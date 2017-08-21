# coding=utf-8

import re

content = """
Mr. Smith bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it. Did he mind? Adam Jones Jr. thinks he didn't. In any case, this isn't true... Well, with a probability of .9 it isn't. 
"""

# regular = '.*?\.(?=\s+(?:[A-Z]|$))'
# regular = '(?=\s+(?:[A-Z]|$))'
regular = '.*?[\.\?](?=\s+(?:[A-Z]|$))'
# regular = '.*?(?!\bMr\b)[\.\?](?=\s+(?:[A-Z]|$))'
# regular = r'[\s\,\.]+'
re_sentence = re.compile(regular)

# items = zz.split(text)
items = re_sentence.findall(content)

for item in items:

    print("^" + item + "$")
