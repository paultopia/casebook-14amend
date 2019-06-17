import sys
sys.path.insert(0, '../lawpy/')

import lawpy

sess = lawpy.courtlistener()

wch = sess.fetch_cases_by_cite("300 U.S. 379")

with open("west_coast_hotel.md", "w") as hotel:
    hotel.write(wch[0].opinions[0].markdown)
