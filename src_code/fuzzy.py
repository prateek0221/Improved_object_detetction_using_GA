def fuzzy_logic_enhancement(detections):
   
    for det in detections:
        confidence = det[4]  
       
        if det[2] - det[0] < 50 or det[3] - det[1] < 50:
            confidence += 0.1
        det[4] = min(max(confidence, 0), 1)  

    return detections