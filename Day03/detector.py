
import cv2
import numpy as np


def count_vesicles(image, center_x, center_y, hole_radius):
    """
    Detect vesicle candidates inside a selected
    carbon-grid hole in a TEM image.
    """

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Improve local contrast
    clahe = cv2.createCLAHE(
        clipLimit=2.0,
        tileGridSize=(8, 8)
    )
    enhanced = clahe.apply(gray)

    # Reduce background noise
    blurred = cv2.GaussianBlur(enhanced, (5, 5), 1.2)

    # Detect circular vesicle candidates
    circles = cv2.HoughCircles(
        blurred,
        cv2.HOUGH_GRADIENT,
        dp=1,
        minDist=10,
        param1=80,
        param2=15,
        minRadius=4,
        maxRadius=16
    )

    vesicles = []
    result = image.copy()

    if circles is not None:
        for x, y, radius in np.round(circles[0]).astype(int):

            distance = np.hypot(
                x - center_x,
                y - center_y
            )

            # Count only circles fully inside the grid hole
            if distance + radius < hole_radius:
                vesicles.append((x, y, radius))

    # Draw the selected grid hole in yellow
    cv2.circle(
        result,
        (center_x, center_y),
        hole_radius,
        (0, 255, 255),
        2
    )

    # Draw detected vesicles and their numbers
    for number, (x, y, radius) in enumerate(vesicles, start=1):

        cv2.circle(
            result,
            (x, y),
            radius,
            (0, 255, 0),
            2
        )

        cv2.putText(
            result,
            str(number),
            (x + 5, y - 5),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.4,
            (0, 0, 255),
            1
        )

    # Write total count on the result image
    cv2.putText(
        result,
        f"Detected vesicles: {len(vesicles)}",
        (15, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 0),
        2
    )

    return len(vesicles), result
