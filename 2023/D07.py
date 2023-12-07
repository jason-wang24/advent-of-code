from functools import cmp_to_key


def part1(file_path):
    def type_tiebreak(a, b):
        ORDER = 'AKQJT98765432'
        for i in range(5):
            if ORDER.find(a[0][i]) < ORDER.find(b[0][i]):
                return -1
            if ORDER.find(a[0][i]) > ORDER.find(b[0][i]):
                return 1
        return 0

    with open(file_path) as input:
        lines = input.readlines()
        NUM_TYPES = 7
        asc_types = [[] for _ in range(NUM_TYPES)]
        for line in lines:
            hand, bid = line.strip().split(' ')
            card_counts = {}
            for card in hand:
                card_counts[card] = card_counts.get(card, 0) + 1

            type_index = 0  # High card (len(card_count) == 5)
            if len(card_counts) == 1:
                type_index = 6
            if len(card_counts) == 2:
                type_index = 5 if max(card_counts.values()) == 4 else 4
            elif len(card_counts) == 3:
                type_index = 3 if max(card_counts.values()) == 3 else 2
            elif len(card_counts) == 4:
                type_index = 1
            asc_types[type_index].append((hand, int(bid)))

        total = 0
        rank = 1
        for hand_type in asc_types:
            sorted_type = sorted(hand_type, key=cmp_to_key(
                type_tiebreak), reverse=True)
            for _, bid in sorted_type:
                total += rank * bid
                rank += 1

        return total


print(part1("input/D07.txt"))


def part2(file_path):
    def type_tiebreak(a, b):
        ORDER = 'AKQT98765432J'
        for i in range(5):
            if ORDER.find(a[0][i]) < ORDER.find(b[0][i]):
                return -1
            if ORDER.find(a[0][i]) > ORDER.find(b[0][i]):
                return 1
        return 0

    with open(file_path) as input:
        lines = input.readlines()
        NUM_TYPES = 7
        asc_types = [[] for _ in range(NUM_TYPES)]
        for line in lines:
            hand, bid = line.strip().split(' ')
            card_counts = {}
            joker_count = 0
            for card in hand:
                if card == 'J':
                    joker_count += 1
                else:
                    card_counts[card] = card_counts.get(card, 0) + 1
            if len(card_counts) > 0:
                max_count_card = max(card_counts, key=card_counts.get)
                card_counts[max_count_card] += joker_count

            type_index = 6  # Five of a kind (len(card_count) == 0 or 1)
            if len(card_counts) == 2:
                type_index = 5 if max(card_counts.values()) == 4 else 4
            elif len(card_counts) == 3:
                type_index = 3 if max(card_counts.values()) == 3 else 2
            elif len(card_counts) == 4:
                type_index = 1
            elif len(card_counts) == 5:
                type_index = 0
            asc_types[type_index].append((hand, int(bid)))

        total = 0
        rank = 1
        for hand_type in asc_types:
            sorted_type = sorted(hand_type, key=cmp_to_key(
                type_tiebreak), reverse=True)
            for _, bid in sorted_type:
                total += rank * bid
                rank += 1

        return total


print(part2("input/D07.txt"))
