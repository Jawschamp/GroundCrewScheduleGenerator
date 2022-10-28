# This file will check the day and parse through all the people that work that day

import datetime
import json
import os

os.chdir("../")
class Attendence:
  def __init__(self):
    self.todays_date = datetime.datetime.now()
    people_obj = open("")

  def check_whos_scheduled(self, persons_name: str):
    