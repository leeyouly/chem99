#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import defaultdict

def table_to_list(table):
    dct = table_to_2d_dict(table)
    return list(iter_2d_dict(dct))


def table_to_2d_dict(table):
    result = defaultdict(lambda : defaultdict(unicode))
    for row_i, row in enumerate(table.xpath('./tr|./tbody/tr')):
        for col_i, col in enumerate(row.xpath('./td|./th')):
            colspan = int(col.get('colspan', 1))
            rowspan = int(col.get('rowspan', 1))
            col_data = col.text_content()
            while row_i in result and col_i in result[row_i]:
                col_i += 1
            for i in range(row_i, row_i + rowspan):
                for j in range(col_i, col_i + colspan):
                    result[i][j] = col_data
    return result


def iter_2d_dict(dct):
    for i, row in sorted(dct.items()):
        cols = []
        for j, col in sorted(row.items()):
            cols.append(col)
        yield cols
        

        
def trans_table(rows):
    newrows = []
    if len(rows) == 0:
        return newrows
    rowcount = len(rows)
    colcount = len(rows[0])
    for rowindex in range(0, colcount):
        newrow = []
        for colindex in range(0, rowcount):
            newrow.append(rows[colindex][rowindex])
        newrows.append(newrow)
    return newrows

        
        
        
        