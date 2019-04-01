# -*- coding: utf-8 -*-


import csv
import os
import re
import sys
from collections import Counter
#解决CSV文件过大导致异常
csv.field_size_limit(sys.maxsize)

# 定义输入mpileup文件变量
mpileup = sys.argv[1]

# 判断输入文件是否存在
if not os.path.exists(mpileup): raise ValueError(u"输入文件%s不存在，请检查输入是否正确!" % mpileup)

# 输出表头
sys.stdout.write("Ref_name\tPos\tTotal_reads\tA\tT\tC\tG\n")

with open(mpileup, 'r') as f:
	cf = csv.reader(f, dialect="excel-tab")
	for row in cf:
		name, pos, ref_base, totalreads, allalts = row[:5]
		stastics = Counter([alt.group() for alt in re.finditer("\^?([\.\,\*ATCGNatcgN])|([\+\-][0-9]+[ATCGNatcgn]+)\$?", allalts, re.I)])
		stastics[ref_base] = stastics[ref_base] + stastics['.'] + stastics[',']
		atcg_num = [stastics[lb] + stastics[ub] for lb, ub in zip('atcg', 'ATCG')]
		sys.stdout.write("%s\t%s\t%s\t%d\t%d\t%d\t%d\n" % (name, pos, totalreads, atcg_num[0], atcg_num[1], atcg_num[2], atcg_num[3]))