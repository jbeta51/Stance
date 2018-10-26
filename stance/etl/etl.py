import cv2
import time
import numpy as np
from template_fit import get_points_from_image
from skeleton import Skeleton


def get_user_skeletons(video_input):
    """
    This function takes in a file path to a video of the user performing the motion. It then
    separates the video into frames and performing template_fit's get points from image
    to compute the wire skeleton.

    Parameters
    ----------
    video_input : String
        file path to the video source

    Returns
    -------
    user_skeletons : List[Skeletons]

    """
    vid_obj = cv2.VideoCapture(video_input)

    user_skeletons = []

    success = 1
    while success:
        success, image = vid_obj.read()

        user_skeletons.append(Skeleton(get_points_from_image(image)))

    return user_skeletons