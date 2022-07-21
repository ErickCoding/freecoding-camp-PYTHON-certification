army_time=""
new_army_time=''
new_ampm=''
new_mins=''
new_12oclockhourtime=''
new_date=''
days_past=''
how_many_days_after='1'
numeric_value_weekday={"Monday":1, "Tuesday":2, "Wednesday":3, 'Thursday':4, 'Friday':5, 'Saturday':6,'Sunday':7 }
def get_key(val):
    for key, value in numeric_value_weekday.items():
         if val == value:
             return key
def add_time(current_time,time_past,date=''):

    org_hours=current_time[0:current_time.find(":")]
    org_minutes=current_time[(current_time.find(":")+1):(current_time.find(" "))]
    org_ampm=current_time[(current_time.find(" ")+1):].lower()
    add_hour=time_past[0:time_past.find(":")]
    add_min=time_past[(time_past.find(":")+1):]
    if org_ampm=="pm":
        army_time=int(org_hours)%12+12
    new_army_time=army_time+int(add_hour)
    if (int(new_army_time/12)%2)==0:
        new_ampm= "AM"
    else:
        new_ampm="PM"
    new_mins=(int(org_minutes)+int(add_min))%60
    new_12oclockhourtime=int((new_army_time)%12+int(int(org_minutes)+int(add_min)/60))
    if new_12oclockhourtime==0:
        new_12oclockhourtime="12"
    if date=="":
        new_date=""
    else:
        new_date=", "+get_key(numeric_value_weekday[date.capitalize()]+(int(new_army_time/24))%7)
    if 2 > ((new_army_time) + int(int(org_minutes) + int(add_min) / 60)) / 24 >= 1:
        how_many_days_after = "next day"
    elif ((new_army_time) + int(int(org_minutes) + int(add_min) / 60)) / 24 >= 2:
        how_many_days_after = str(int(((new_army_time) + int(int(org_minutes) + int(add_min) / 60)) / 24)) + " days later"
    if new_mins==0:
        new_mins="00"
    print(str(new_12oclockhourtime)+":"+str(new_mins)+" "+new_ampm+new_date+" ("+how_many_days_after+')')
add_time("12:00 PM","36:00","Monday")






