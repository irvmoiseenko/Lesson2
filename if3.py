performance = [
    {'school_class': '5a', 'scores': [1,5,5]},
    {'school_class': '5b', 'scores': [3,2,3]},
    {'school_class': '5c', 'scores': [4,4]}
]


a = []
for clas in performance:
    average = sum(clas['scores']) / len(clas['scores'])
    print(f"Средняя оценка по классу {clas['school_class']} {average}")
    for score in clas['scores']:
        a.append(score)

print(f"Средняя оценка по школе {sum(a) / len(a)}")
