import re
valid_date = re.compile(r"\["
    # Jan, Mar, May, Jul, Aug, Oct, Dec (31 days)
    "(0[13578]|1[02])-(0[1-9]|[12][0-9]|3[01])\]"
    # Feb
    "|\[02-(0[1-9]|1[0-9]|2[0-8])\]|"
    # Apr, Jun, Sept, Nov
    "\[(0[469]|11)-(0[1-9]|[12][0-9]|30)"
    "\]")

print(valid_date.search("[01-23]"))