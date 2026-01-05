def take_magic_damage(health, resist, amp, spell_power):
    total_max_damage = (spell_power * amp) - resist
    return health - total_max_damage
