def predict_placement(score):

    if score >= 70:
        return "High Placement Probability"

    elif score >= 40:
        return "Medium Placement Probability"

    else:
        return "Low Placement Probability"