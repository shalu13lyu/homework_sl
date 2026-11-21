
import cv2
import numpy as np
import pytest

from detector import count_vesicles


# Test 1: A completely black image
def test_black_image():
    image = np.zeros((300, 300, 3), dtype=np.uint8)

    count, result = count_vesicles(
        image, 150, 150, 100
    )

    assert count == 0


# Test 2: A uniform gray image
def test_gray_image():
    image = np.full(
        (300, 300, 3),
        150,
        dtype=np.uint8
    )

    count, result = count_vesicles(
        image, 150, 150, 100
    )

    assert count == 0


# Test 3: A synthetic circular vesicle
def test_single_circle():
    image = np.full(
        (300, 300, 3),
        180,
        dtype=np.uint8
    )

    # Draw a dark circular membrane
    cv2.circle(
        image,
        (150, 150),
        10,
        (40, 40, 40),
        2
    )

    count, result = count_vesicles(
        image, 150, 150, 100
    )

    assert count == 1


# Test 4: A circle outside the grid hole
def test_circle_outside_hole():
    image = np.full(
        (300, 300, 3),
        180,
        dtype=np.uint8
    )

    # Draw a circle outside the selected region
    cv2.circle(
        image,
        (270, 270),
        10,
        (40, 40, 40),
        2
    )

    count, result = count_vesicles(
        image, 150, 150, 80
    )

    assert count == 0


# Test 5: Output image dimensions
def test_output_dimensions():
    image = np.zeros((300, 400, 3), dtype=np.uint8)

    count, result = count_vesicles(
        image, 200, 150, 100
    )

    assert result.shape == image.shape
    assert isinstance(count, int)
