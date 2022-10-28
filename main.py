import json

class UnitTest:
  def __init__(self, persons_name: str):
    self.persons_name = persons_name

  

  
with open("people.json", "r") as people_file:
  people_file_obj = json.loads(people_file.read())
  for people in people_file_obj["people"]["Garnette"]:
    print(people.keys)