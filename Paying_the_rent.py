# Paying the rent
# You are moving to a new city for an internship for a few months and have to rent a house for that purpose.
# You have to pay the full month's house rent even if you have lived for a few days for that month. i.e. if you start on 15th Jan and leave by 15th May, you still have to pay full rent for months of Jan and May too.

# Your task is to find the months that you have to pay rent for so that you can write post-dated cheques to your landlord.

# You will be given two dates as input and your task is to print all months between the dates including the months the dates are from.
# The input will contain the two dates in a list as follows:
# [2017,1,1,2017,3,4] which corresponds to 1st Jan, 2017 and 4th March, 2017. This date is in the format(yyyy,mm,dd)
# (the code for taking input has already been written for you, please don't modify that)
# The output should contain a list with names of months you have to pay the rent for(the list should be sorted chronologically  based on months, i.e May should come before August). You can assume that there won't be more than 12 months between two dates.
# You'll need to use the datetime module for this problem which can be referred to here. You can choose to use any other method too.

# Sample Input:
# [2017,1,1,2017,1,1]
# Sample Output:
# ['January']



import datetime
import ast,sys
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)
dateStart=datetime.date(input_list[0],input_list[1],input_list[2])
dateEnd=datetime.date(input_list[3],input_list[4],input_list[5])
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
ans = set()
while dateStart <= dateEnd:
	ans.add(dateStart.month)
	dateStart += datetime.timedelta(1)
print([months[x-1] for x in sorted(ans)])
