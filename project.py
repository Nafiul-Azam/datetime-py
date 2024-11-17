from datetime import datetime

# বর্তমান সময়, তারিখ এবং মাস পাওয়ার জন্য
current_time = datetime.now()

# সময়, তারিখ এবং মাস প্রদর্শন করা
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")  # তারিখ এবং সময়
formatted_date = current_time.strftime("%d-%m-%Y")  # তারিখ (দিন-মাস-বছর)
formatted_month = current_time.strftime("%B")  # পূর্ণ মাসের নাম

print("Today:", formatted_time)
print("date:", formatted_date)
print("month:", formatted_month)
