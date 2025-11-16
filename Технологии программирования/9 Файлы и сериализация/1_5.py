list_of_parties = [

    {'name': 'Партия №1',
     'votes': 0,
     'percent': 0},

    {'name': 'Партия №2',
     'votes': 0,
     'percent': 0},

    {'name': 'Партия №3',
     'votes': 0,
     'percent': 0},

    {'name': 'Партия №4',
     'votes': 0,
     'percent': 0},

    {'name': 'Партия №5',
     'votes': 0,
     'percent': 0}
]

try:
    with open('voting_results.txt', 'r') as f:
        voting_results = [i for i in f.read().split()]

except FileNotFoundError as error:
    print(error)

else:
    for i in range(0, 5):
        list_of_parties[i]['votes'] = voting_results.count(str(i + 1))
        list_of_parties[i]['percent'] = list_of_parties[i]['votes'] * 100 / len(voting_results)

    spoiled_votes = len(voting_results) - sum(i['votes'] for i in list_of_parties)
    spoiled_percent = spoiled_votes * 100 / len(voting_results)

    list_of_parties.sort(key=lambda i: i['votes'], reverse=True)

    for i in range(0, 5):
        print(f"{i + 1}. {list_of_parties[i]['name']} | {list_of_parties[i]['votes']} | {list_of_parties[i]['percent']}%")
    print(f"-1. Испорченный бланк | {spoiled_votes} | {spoiled_percent}%" )