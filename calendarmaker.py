from datetime import datetime,timedelta
name=input("enter your name: ").strip().title()
DAYS=('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Sartuday')
MONTHS=('January','February','March','April','May','June','July','August','September','October','November','December')
current=lambda str: datetime.now().date().strftime(str)#get current year or month
print(f'Calendar generated {name}.')

while True:
    response=input("Enter the year for the calendar: ").strip()
    if response.isdecimal() and int(response)>0:
        year=int(response)
        break
    print(f'Enter a numeric year,like {current("%Y")}.')
    continue
monthNumber=MONTHS.index(current("%B"))+1 

while True:
  
    response=input(f"Enter the month for the calendar,1-12: ").strip()
    
    if not response.isdecimal():
        print(f'Enter a numeric month,like {monthNumber} for {current("%B")} ') 
        continue

    month=int(response)
    if 1<=month<=12:
        break
    print('Please enter a number from 1-12.')
     
def getCalendarFor(year,month):
    callText=''#will contain the string of our calendar
    callText+=(' '*34)+MONTHS[month-1]+ ' '+ str(year) + "\n" #put the month and year a the top of the calendar
    callText += "".join([day+"~~~|" for day in DAYS]) + "\n"  #add the days of the weeks to the calendar
    weekSeparator=("+----------"*7)+"+\n"#the horizontal line string that separate weeks

    blankRow=("|          "*7)+ '|\n'#10 blank spaces in between the | day separators
    print(f'{year}|{month}')
    '''get the first date in the month '''
    currentDate=datetime(year,month,1)
    '''Roll back currentDate until it is Sunday'''
    while currentDate.weekday() != 6:
        currentDate-=timedelta(days = 1)
    
    while True:# loop over each week in the month
        callText+=weekSeparator

        dayNumberRow=''#row with the day number labels
        for _ in range (len(DAYS)):
            dayNumberLabel=str(currentDate.day).rjust(2)
            dayNumberRow+='|'+dayNumberLabel+(" "*8)
            currentDate+=timedelta(days=1)#go to the next day
        dayNumberRow+="|\n" #add the vertical line after the Sartuday

        #Add the day number row and 3 blank rows to the calendar text
        callText+=dayNumberRow
        for _ in range(3):
            callText+=blankRow
        
        #check if we're done with the month
        if currentDate.month !=month:
            break
    callText+=weekSeparator #adds the horizontal line at the bottom of the calendar
    return callText

callText=getCalendarFor(year,month)
print(callText)
