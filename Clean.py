import os
import datetime
import send2trash


#Send files to trash in folder C:\Users\nicks\Downloads after 30 days


output_log = open('C:\\Users\\nicks\PycharmProjects\\CleanDownloads\\Log.txt', 'a')
today = datetime.datetime.now()
output_log.write('\n' + str(today) + ' Ran @. \n')


for file in os.listdir('C:\\Users\\nicks\\Downloads'):
    file_date = datetime.datetime.fromtimestamp(os.path.getctime('C:\\Users\\nicks\\Downloads\\' + file))
    if (today.day - file_date.day) >= 14 and file != 'desktop.ini':
        send2trash.send2trash('C:\\Users\\nicks\\Downloads\\' + file)
        output_log.write(file + ' was deleted. \n')

output_log.close()


