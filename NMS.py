import numpy as np

def nms(boxes, max_overlap):

    correct_boxes = []
    boxes = boxes.astype("float")

    x1, y1, x2, y2 = boxes[:, 0][:, 1][:, 2][:, 3]

    box_sum = (x2 - x1 + 1) * (y2 - y1 + 1)

    index = np.argsort(y2)

    while len(index) > 0:
        izero = index - 1
        correct_boxes.append(index[izero])

        xx1 = np.maximum(x1[i], x1[index[:izero]])
        yy1 = np.maximum(y1[i], y1[index[:izero]])
        xx2 = np.minimum(x2[i], x2[index[:izero]])
        yy2 = np.minimum(y2[i], y2[index[:izero]])

        w = np.maximum(0, xx2 - xx1 + 1)
        h = np.maximum(0, yy2 - yy1 + 1)

        overlap = (w * h) / area[index [:izero]]

        index = np.delete(index, np.concatenate(([izero], np.where(overlap > max_overlap)[0])))

    return correct_boxes