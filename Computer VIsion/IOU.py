def calculate_iou(box1,box2):
    '''
    Calculate intersection over union of two boxes
    '''

    # Extract coordinates of both boxes
    x1_box1,y1_box1,x2_box1,y2_box1 = box1
    x1_box2,y1_box2,x2_box2,y2_box2 = box2

    # Calculate intersection coordinates
    x1_intersection = max(x1_box1,x1_box2)
    y1_intersection = max(y1_box1,y1_box2)
    x2_intersection = min(x2_box1,x2_box2)
    y2_intersection = min(y2_box1,y2_box2)

    # Calculate width and length of intersection
    intersection_width = abs(x2_intersection-x1_intersection)
    intersection_length = abs(y2_intersection-y1_intersection)

    # Calculate intersection area
    intersection_area = intersection_width * intersection_length

    # Calculate area of both boxes
    box1_area = (x2_box1-x1_box1)*(y2_box1-y1_box1)
    box2_area = (x2_box2-x1_box2)*(y2_box2-y1_box2)

    # Calculate union area
    union_area = box1_area + box2_area - intersection_area

    # Calculate intersection over union
    if intersection_area > 0:
        if union_area > 0:
            iou = intersection_area / union_area
        else:
            iou = 0
    else:
        iou = 0

    return iou


# Define two bounding boxes (format: [x1, y1, x2, y2])
box1 = [2, 2, 6, 6]
box2 = [4, 4, 8, 8]

# Calculate IoU
iou = calculate_iou(box1, box2)
print(f"Intersection over Union (IoU): {iou:.2f}")