def ratings(score): 
    if score >= 95: 
        print('3 stars')
    elif score ==85 and score < 95:
        print('2 stars')
    else: 
        print('1 star')
    return score

ratings(60)
