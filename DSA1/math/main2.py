'''
def get_follower_prediction(follower_count, influencer_type, num_months):
    # Determine growth rate r based on influencer type
    if influencer_type == "fitness":
        r = 4
    elif influencer_type == "cosmetic":
        r = 3
    else:
        r = 2

    # Geometric progression formula: total = a1 * r^n
    total = follower_count * (r ** num_months)

    # Return as integer
    return int(total)
'''


def get_follower_prediction(follower_count, influencer_type, num_months):
 
    if influencer_type == "fitness":
        follower_prediction = follower_count * 4**num_months
    elif influencer_type == "cosmetic":
        follower_prediction = follower_count * 3**num_months
    else:
        follower_prediction = follower_count * 2**num_months

    return follower_prediction



