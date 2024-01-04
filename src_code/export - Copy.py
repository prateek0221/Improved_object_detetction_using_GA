# fuzzy_logic.py

def fuzzy_logic_enhancement(detections):
    # Example fuzzy logic adjustment of confidence scores
    # Modify confidence scores based on specific criteria/rules
    for det in detections:
        confidence = det[4]  # Assuming the confidence score is at index 4
        # Apply fuzzy logic rules to adjust confidence score
        # Example: if the object is small, increase confidence by 0.1
        if det[2] - det[0] < 50 or det[3] - det[1] < 50:
            confidence += 0.1
        det[4] = min(max(confidence, 0), 1)  # Clip confidence score between 0 and 1

    return detections
