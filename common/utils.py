import os
import shutil
from datetime import datetime


def rename_locust_report(report_folder,file_name):
    # Generate a new name for the report file based on the current timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    new_report_file = f'report_'+file_name+'_'+timestamp+'.html'
    oldFile = report_folder+'/report.html'
    newFile = report_folder+'/'+ new_report_file

    # Rename the report file
    #shutil.move(oldFile, newFile)

    print(f'Report file renamed to: {new_report_file}')

