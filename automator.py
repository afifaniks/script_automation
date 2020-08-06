#!/usr/bin/env python
"""
This script will schedule a list of tasks to execute at a given time
__author__: Afif Al Mamun
__date__: August, 4, 2020
"""

import schedule
import time
import os


def execute_file(files):
    for file in files:
        print("Executing script: " + file)
        os.system('python ' + file)


class Automator:
    def __init__(self, file_path, day, exec_time):
        """
        This class will create a scheduler to execute scripts at a given time periodically
        :param file_path: Path of the script
        :param day: Day of the week
        Accepted args: ["friday", "saturday", "sunday", "monday", "tuesday", "wednesday", "thursday", "everyday"]
        :param exec_time: Time of execution in 24H format HH:MM
        """

        self.file_path = file_path
        self.day = day
        self.exec_time = exec_time

    def start(self):
        file_path = self.file_path
        day = self.day
        exec_time = self.exec_time

        print("Handler started...")
        print("Execution time: each " + day + " at " + exec_time)

        if day.lower() == "friday":
            schedule.every().friday.at(exec_time).do(lambda: execute_file(file_path))
        elif day.lower() == "saturday":
            schedule.every().saturday.at(exec_time).do(lambda: execute_file(file_path))
        elif day.lower() == "sunday":
            schedule.every().sunday.at(exec_time).do(lambda: execute_file(file_path))
        elif day.lower() == "monday":
            schedule.every().monday.at(exec_time).do(lambda: execute_file(file_path))
        elif day.lower() == "tuesday":
            schedule.every().tuesday.at(exec_time).do(lambda: execute_file(file_path))
        elif day.lower() == "wednesday":
            schedule.every().wednesday.at(exec_time).do(lambda: execute_file(file_path))
        elif day.lower() == "thursday":
            schedule.every().thursday.at(exec_time).do(lambda: execute_file(file_path))
        elif day.lower() == "everyday":
            schedule.every().day.at(exec_time).do(lambda: execute_file(file_path))

        while True:
            schedule.run_pending()
            time.sleep(1)



