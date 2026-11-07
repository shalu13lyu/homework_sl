
import cv2
import numpy as np


def count_vesicles(image, center_x, center_y, hole_radius):
    """
    Detect circular vesicle candidates inside
    a selected carbon-grid hole.
    """

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Reduce image noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 1.2)

    # Detect circular structures
    circles = cv2.HoughCircles(
        blurred,
        cv2.HOUGH_GRADIENT,
        dp=1,
        minDist=12,
        param1=100,
        param2=20,
        minRadius=4,
        maxRadius=18
    )

    vesicles = []
    result = image.copy()

    if circles is not None:
        for x, y, radius in np.round(circles[0]).astype(int):

            # Calculate distance from the grid-hole center
            distance = np.sqrt(
                (x - center_x)**2 +
                (y - center_y)**2
            )

            # Keep only circles inside the selected hole
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

    # Mark detected vesicle candidates in green
    for x, y, radius in vesicles:
        cv2.circle(
            result,
            (x, y),
            radius,
            (0, 255, 0),
            2
        )

    return len(vesicles), result
