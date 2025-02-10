import calendar
import datetime

def main():
    curr_bal = float(input(f'Whats the current balance?:'))
    curr_mth_adb = float(input(f'Whats the current month average daily balance?:'))
    day_idx = int(input(f'As at which day (key in the day of the month)?:'))
    adb_diff = float(input(f'Whats the ADB diff as of now?:'))
    min_increment = float(input(f'Whats the minimum increment to get rewards?:'))
    target_adb = curr_mth_adb - (adb_diff) + min_increment
    num_days = calendar.monthrange(datetime.datetime.now().year, datetime.datetime.now().month)[1]
    maintenance_amt = ((num_days*target_adb) - (curr_mth_adb*day_idx))/(num_days-day_idx)
    bal_diff = maintenance_amt - curr_bal

    print("==============================================================")
    print(f'Current ADB target to hit from now on is {maintenance_amt}')
    print(f'Amount to topup/withrdaw {bal_diff}')



if __name__ == '__main__':
    main()
