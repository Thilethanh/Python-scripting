def calculate_damage(sword, arrow, spear, dagger, fireball):
    damages = [sword, arrow, spear, dagger, fireball]

    total_damage = sum(damages)
    average_damage = total_damage / len(damages)
    return total_damage, average_damage
