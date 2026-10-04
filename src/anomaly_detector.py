import cv2
import numpy as np


def detect_anomalies(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blurred = cv2.GaussianBlur(gray, (21, 21), 0)
    difference = cv2.absdiff(gray, blurred)

    # Only keep the strongest 2% of unusual regions
    threshold_value = np.percentile(difference, 98)

    _, anomalies = cv2.threshold(
        difference,
        max(30, threshold_value),
        255,
        cv2.THRESH_BINARY
    )

    # Remove tiny noisy regions
    kernel = np.ones((5, 5), np.uint8)
    anomalies = cv2.morphologyEx(anomalies, cv2.MORPH_OPEN, kernel)

    return anomalies > 0