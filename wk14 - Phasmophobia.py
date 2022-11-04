'''Week 14 - Phasmophobia'''


def main():
    '''Main Function'''

    ghost = {
        'EMF Level 5': ['Banshee', 'Jinn', 'Oni', 'Phantom', 'Revenant', 'Shade'],
        'Ghost Writing': ['Demon', 'Oni', 'Revenant', 'Shade', 'Spirit', 'Yurei'],
        'Fingerprints': ['Banshee', 'Poltergeist', 'Revenant', 'Spirit', 'Wraith'],
        'Spirit Box': ['Demon', 'Jinn', 'Mare', 'Oni', 'Poltergeist', 'Spirit', 'Wraith'],
        'Freezing Temperatures': ['Banshee', 'Demon', 'Mare', 'Phantom', 'Wraith', 'Yurei'],
        'Ghost Orb': ['Jinn', 'Mare', 'Phantom', 'Poltergeist', 'Shade', 'Yurei']
    }

    evidence_list = []

    for _ in range(3):
        evidence = input()

        if evidence != 'No evidence':
            evidence_list.append(evidence)

    if not evidence_list:
        total = set()

        for evidence_type in ghost:
            total = total | set(ghost[evidence_type])

        print(*sorted(total), sep='\n')
        return

    ghost_list = set()

    if len(evidence_list) == 1:
        ghost_list = set(ghost[evidence_list[0]])
    if len(evidence_list) == 2:
        ghost_list = set(ghost[evidence_list[0]]).intersection(
            ghost[evidence_list[1]])
    if len(evidence_list) == 3:
        ghost_list = set(ghost[evidence_list[0]]).intersection(
            ghost[evidence_list[1]], ghost[evidence_list[2]])

    ghost_list = list(ghost_list)

    if not ghost_list:
        print('Not yet discovered')
        return

    print(*sorted(ghost_list), sep='\n')


main()
