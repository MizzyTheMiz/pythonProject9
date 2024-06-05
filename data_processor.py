import json
from datetime import datetime
from person import Person

class PersonDataProcessor:

    def __init__(self):
        self.content = []

    def read_file_contents(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            self.content.clear()
            for item in data:
                birth_date = datetime.strptime(item['sundinud'], '%Y-%m-%d')
                death_date = datetime.strptime(item['surnud'], '%Y-%m-%d') if item['surnud'] != "0000-00-00" else None
                self.content.append(Person(item['nimi'], birth_date, item['amet'], death_date))

    def get_total_persons(self):
        return len(self.content)

    def get_longest_name(self):
        longest_name = max(self.content, key=lambda x: len(x.name))
        return {"name": longest_name.name, "length": len(longest_name.name)}

    def get_oldest_living_person(self):
        today = datetime.today()
        living_people = [p for p in self.content if p.death_date is None]
        oldest = min(living_people, key=lambda x: x.birth_date)
        age = today.year - oldest.birth_date.year - (
                    (today.month, today.day) < (oldest.birth_date.month, oldest.birth_date.day))
        birth = oldest.birth_date.strftime("%d.%m.%Y")
        return {"name": oldest.name, "age": age, "dateofbirth": birth}

    def get_oldest_deceased_person(self):
        deceased_people = [p for p in self.content if p.death_date is not None]
        oldest = max(deceased_people, key=lambda x: x.death_date.year - x.birth_date.year)
        age = oldest.death_date.year - oldest.birth_date.year - (
                    (oldest.death_date.month, oldest.death_date.day) < (oldest.birth_date.month, oldest.birth_date.day))
        birth = oldest.birth_date.strftime("%d.%m.%Y")
        death = oldest.death_date.strftime("%d.%m.%Y")
        return {"name": oldest.name, "age": age, "dateofbirth": birth, "dateofdeath": death}

    def get_actor_count(self):
        return len([p for p in self.content if "näitleja" in p.profession.lower()])

    def get_births_in_1997(self):
        return len([p for p in self.content if p.birth_date.year == 1997])

    def get_unique_professions(self):
        return len(set(p.profession for p in self.content))

    def get_names_with_more_than_two_parts(self):
        return len([p for p in self.content if len(p.name.split()) > 2])

    def get_same_birth_death_month_day(self):
        return len([p for p in self.content if p.death_date is not None and p.birth_date.month == p.death_date.month and p.birth_date.day == p.death_date.day])

    def get_living_and_deceased_counts(self):
        living = len([p for p in self.content if p.death_date is None])
        deceased = len([p for p in self.content if p.death_date is not None])
        return {"living": living, "deceased": deceased}
