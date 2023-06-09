"""
Instructions
Complete the solution so that the function will break up camel casing, using a space between words.
Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
"""

def solution(s):
    result = ""
    for letter in s:
        if letter != letter.upper():
            result += letter
        else:
            result += " " + letter
    return result
  
#OR
  
def solution(s):
    return "".join(" " + l if l.isupper() else l for l in s)
