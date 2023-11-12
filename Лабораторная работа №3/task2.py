participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

def find_common_participants(group1, group2, delimiter=','):

    participants1 = group1.split(delimiter)
    participants2 = group2.split(delimiter)

    set1 = set(participants1)
    set2 = set(participants2)

    common_participants = set1.intersection(set2)

    return sorted(list(common_participants))
