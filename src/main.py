import cv2

from image_loader import load_image
from anomaly_detector import detect_anomalies

image = load_image("data/images/polonolo.jpeg")

anomalies = detect_anomalies(image)
anomaly_percentage = (anomalies.sum() / anomalies.size) * 100

# Convert anomaly mask to an image
mask = anomalies.astype("uint8") * 255

# Find separate anomaly regions
contours, _ = cv2.findContours(
    mask,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

result = image.copy()

count = 0

for contour in contours:
    area = cv2.contourArea(contour)

    if area > 20:
        x, y, w, h = cv2.boundingRect(contour)

        cv2.rectangle(
            result,
            (x, y),
            (x + w, y + h),
            (0, 0, 255),
            2
        )

        count += 1
cv2.putText(
    result,
    f"Anomalies: {count} | {anomaly_percentage:.2f}%",
    (20, 40),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (0, 0, 255),
    2
)
print("Anomaly regions detected:", count)
print("Anomaly percentage:", round(anomaly_percentage, 2), "%")

cv2.imwrite(
    "data/results/anomaly_boxes.jpg",
    result
)

print("Result saved to data/results/anomaly_boxes.jpg")