
import cv2
import numpy as np


def count_vesicles(image, center_x, center_y, hole_radius):
    """
    Detect approximately circular vesicle candidates
    inside a selected TEM carbon-grid hole.
    """

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Improve contrast
    clahe = cv2.createCLAHE(
        clipLimit=1.5,
        tileGridSize=(8, 8)
    )
    enhanced = clahe.apply(gray)

    # Reduce small-scale image noise
    smooth = cv2.bilateralFilter(
        enhanced, 9, 35, 35
    )

    # Detect dark circular boundaries
    edges = cv2.Canny(smooth, 40, 90)

    # Join small gaps in circular outlines
    kernel = cv2.getStructuringElement(
        cv2.MORPH_ELLIPSE, (3, 3)
    )
    edges = cv2.morphologyEx(
        edges, cv2.MORPH_CLOSE, kernel
    )

    contours, _ = cv2.findContours(
        edges,
        cv2.RETR_LIST,
        cv2.CHAIN_APPROX_SIMPLE
    )

    candidates = []

    for contour in contours:
        area = cv2.contourArea(contour)
        perimeter = cv2.arcLength(contour, True)

        if perimeter == 0:
            continue

        # Ignore very small and very large objects
        if area < 35 or area > 1200:
            continue

        # Calculate shape circularity
        circularity = 4 * np.pi * area / (perimeter ** 2)

        if circularity < 0.75:
            continue

        # Calculate circle around the contour
        (x, y), radius = cv2.minEnclosingCircle(contour)

        if radius < 4 or radius > 20:
            continue

        # Check that the object is inside the grid hole
        distance = np.hypot(
            x - center_x,
            y - center_y
        )

        if distance + radius >= hole_radius - 5:
            continue

        candidates.append((
            int(round(x)),
            int(round(y)),
            int(round(radius)),
            float(circularity)
        ))

    # Remove overlapping detections
    # Keep higher-circularity candidates first
    candidates.sort(key=lambda item: item[3], reverse=True)

    vesicles = []

    for x, y, radius, circularity in candidates:
        duplicate = False

        for vx, vy, vr in vesicles:
            distance = np.hypot(x - vx, y - vy)

            if distance < max(radius, vr):
                duplicate = True
                break

        if not duplicate:
            vesicles.append((x, y, radius))

    # Create annotated output
    result = image.copy()

    # Selected carbon-grid hole in yellow
    cv2.circle(
        result,
        (center_x, center_y),
        hole_radius,
        (0, 255, 255),
        2
    )

    # Detected vesicles in green
    for number, (x, y, radius) in enumerate(vesicles, 1):
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
            (x + radius + 2, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.35,
            (0, 0, 255),
            1
        )

    # Add total count
    cv2.putText(
        result,
        f"Detected: {len(vesicles)}",
        (10, 25),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.65,
        (0, 255, 0),
        2
    )

    return len(vesicles), result
