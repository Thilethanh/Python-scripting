# Continue Statement
def award_enchantments(start, end, step):
    counter = 0  # initialize before the loop

    for quest_number in range(start, end, step):
        counter += 1  # count quests seen

        if counter < 3:
            continue  # not enough quests yet

        # reached 3 quests
        enchantment_strength = quest_number * 5
        print(
            f"Enchantment of strength {enchantment_strength} awarded for completing {quest_number} quests!"
        )

        counter = 0  # reset after awarding


# Don't touch below this line


def test(start, end, step):
    print(f"Testing with quests {start} through {end - 1}:")
    award_enchantments(start, end, step)
    print("========================================")


def main():
    test(1, 11, 1)
    test(20, 24, 1)
    test(10, 12, 1)
    test(11, 19, 1)
    test(2, 8, 1)


main()

