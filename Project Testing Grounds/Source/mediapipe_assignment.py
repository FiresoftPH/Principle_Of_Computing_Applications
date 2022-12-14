import cv2
import mediapipe as mp
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose
cont_count = 0
# For static images:
IMAGE_FILES = []
BG_COLOR = (192, 192, 192) # gray
with mp_pose.Pose(
    static_image_mode=True,
    model_complexity=2,
    enable_segmentation=True,
    min_detection_confidence=0.5) as pose:
  for idx, file in enumerate(IMAGE_FILES):
    image = cv2.imread(file)
    image_height, image_width, _ = image.shape
    # Convert the BGR image to RGB before processing.
    results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    if not results.pose_landmarks:
      continue
    print(
        f'Nose coordinates: ('
        f'{results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].x * image_width}, '
        f'{results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].y * image_height})'
    )

    annotated_image = image.copy()
    # Draw segmentation on the image.
    # To improve segmentation around boundaries, consider applying a joint
    # bilateral filter to "results.segmentation_mask" with "image".
    condition = np.stack((results.segmentation_mask,) * 3, axis=-1) > 0.1
    bg_image = np.zeros(image.shape, dtype=np.uint8)
    bg_image[:] = BG_COLOR
    annotated_image = np.where(condition, annotated_image, bg_image)
    # Draw pose landmarks on the image.
    mp_drawing.draw_landmarks(
        annotated_image,
        results.pose_landmarks,
        mp_pose.POSE_CONNECTIONS,
        landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
    cv2.imwrite('/tmp/annotated_image' + str(idx) + '.png', annotated_image)
    # Plot pose world landmarks.
    mp_drawing.plot_landmarks(
        results.pose_world_landmarks, mp_pose.POSE_CONNECTIONS)

# For webcam input:
cap = cv2.VideoCapture(1)
with mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as pose:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # Flip the image horizontally for a later selfie-view display, and convert
    # the BGR image to RGB.
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    results = pose.process(image)

    # Draw the pose annotation on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    mp_drawing.draw_landmarks(
        image,
        results.pose_landmarks,
        mp_pose.POSE_CONNECTIONS,
        landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
    cv2.imshow('MediaPipe Pose', image)
    if not results.pose_landmarks:
      continue 
    if abs(results.pose_landmarks.landmark[12].y - results.pose_landmarks.landmark[11].y)<=1:
      cont_count+=1
      print(cont_count)
    if abs(results.pose_landmarks.landmark[14].y - results.pose_landmarks.landmark[13].y)<=1:
      cont_count+=1
      print(cont_count)
    if abs(results.pose_landmarks.landmark[14].y - results.pose_landmarks.landmark[13].y)<=1:
      cont_count+=1
      print(cont_count)
    if abs(results.pose_landmarks.landmark[15].y - results.pose_landmarks.landmark[16].y)<=1:
      cont_count+=1
      print(cont_count)
    if abs(results.pose_landmarks.landmark[15].x - results.pose_landmarks.landmark[16].x)<=1:
      cont_count+=1
      print(cont_count)
    if abs(results.pose_landmarks.landmark[17].y - results.pose_landmarks.landmark[18].y)<=1:
      cont_count+=1
      print(cont_count)
    if abs(results.pose_landmarks.landmark[17].x - results.pose_landmarks.landmark[18].x)<=1:
      cont_count+=1
      print(cont_count)
    if abs(results.pose_landmarks.landmark[19].y - results.pose_landmarks.landmark[20].y)<=1:
      cont_count+=1
      print(cont_count)
    if abs(results.pose_landmarks.landmark[19].x - results.pose_landmarks.landmark[20].x)<=1:
      cont_count+=1
      print(cont_count)
    if abs(results.pose_landmarks.landmark[21].y - results.pose_landmarks.landmark[22].y)<=1:
      cont_count+=1
      print(cont_count)
    if abs(results.pose_landmarks.landmark[21].x - results.pose_landmarks.landmark[22].x)<=1:
      cont_count+=1
      print(cont_count)
    if abs(results.pose_landmarks.landmark[32].y - results.pose_landmarks.landmark[25].y)<=1:
      cont_count+=1
      print(cont_count)
    if abs(results.pose_landmarks.landmark[32].x - results.pose_landmarks.landmark[25].x)<=1:
      cont_count+=1
      print(cont_count)
    if abs(results.pose_landmarks.landmark[31].y - results.pose_landmarks.landmark[26].y)<=1:
      cont_count+=1
      print(cont_count)
    if abs(results.pose_landmarks.landmark[31].x - results.pose_landmarks.landmark[26].x)<=1:
      cont_count+=1
      print(cont_count)

    if cont_count > 10: #15
      if cv2.waitKey(5) & 0xFF == 27:
      # print(results.pose_landmarks)
        break
cap.release()

print(cont_count)
#results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].x (print x)
#results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].y (print y)