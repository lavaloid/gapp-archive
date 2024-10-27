"""
This will generate the table rows that will be included in the
Mind the GAPP section. The output will not be formatted properly,
so further formatting is needed.
"""

from calendar import monthrange
from datetime import date
from dateutil.relativedelta import relativedelta

result = ""

vols_with_notes = [7, 10, 15, 21]


def generate_row(year: int, month: int, idx: int):
    _, days_in_month = monthrange(2022, month)

    start_date = f"{year}-{month:02}-01" if idx > 0 else "2021-10-27"
    end_date = f"{year}-{month:02}-{days_in_month}"

    if idx + 1 in vols_with_notes:
        note_link = f'<a href="#notes-{idx+1}">Notes</a>'
    else:
        note_link = ""

    return f"""
      <tr>
        <td>Mind the GAPP vol. {idx + 1}</td>
        <td>
          <time>{start_date}</time> to <time>{end_date}</time>
        </td>
        <td>
          <a href="archive/Mind_the_GAPP_vol_{(idx + 1):02}.pdf" target="_blank">Download</a>
        </td>
        <td>{note_link}</td>
      </tr>"""


for i in range(35):
    start_date = date(2021, 11, 1) + relativedelta(months=i)
    result += generate_row(start_date.year, start_date.month, i)

with open("generated-table.html", "w") as f:
    f.write(result)

print("Done!")
