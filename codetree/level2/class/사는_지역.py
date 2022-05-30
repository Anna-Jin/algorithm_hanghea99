class Region:
    def __init__(self, name, address, city):
        self.name = name
        self.address = address
        self.city = city

    def print_profile(self):
        print(f'name {self.name}')
        print(f'addr {self.address}')
        print(f'city {self.city}')



n = int(input())
lst = [tuple(input().split()) for _ in range(n)]

people = [Region(name, address, city) for name, address, city in lst]


idx = 0
for i, person in enumerate(people):
    if person.name > people[idx].name:
        idx = i

people[idx].print_profile()