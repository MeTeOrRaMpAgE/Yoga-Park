import cv2
import mediapipe as mp
from math import atan2, pi, degrees
import streamlit as st


mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
cap = cv2.VideoCapture(0)
col1, col2 = st.columns(2)

st.sidebar.image("Logo.png")

bar = st.progress(0)
fw = col1.image([])
refpose = st.markdown(
    "<h2 >Warrior Pose or Virabhadrasana</h2>", unsafe_allow_html=True)
reffw = col2.image("warrior.jpg")
refinfo = st.text("""1. Spread your legs around 3-4 ft wide.
2. Move your right toe in an angle of 90-degrees and the left one at an angle 
   of 45-degrees.
3. Turn your neck towards your right and fix your gaze ahead.
4. Raise your arms to your shoulder level keeping them parallel to the ground. 
   Your palms must face the ground. 
5. Bend your right knee. Try to keep it perpendicular to the floor.
6. Make sure to keep your back straight. Hold the pose till the bar reaches the
    end.""")


warrior = [

    170.77573580334,
    274.39104033569555,
    188.95374429375164,
    80.621315054376,
    150.36931262768405,
    229.0124061497212,
    239.76446145899877,
    179.52796521210834,
    112.09380071603549,
    223.1385064086832

]
mountain = [

    169.90659804448086,
    354.3869607603357,
    186.13387209980334,
    6.781402620051102,
    86.79571065216427,
    270.62800777013973,
    175.82246361527157,
    182.23105917621496,
    176.7450855994398,
    181.46472097862167

]
tree = [

    317.2712576853365,
    338.83244046321937,
    45.470245214688916,
    13.83001314129887,
    96.30191198661441,
    249.29129386214157,
    179.899237643545,
    29.781832213900696,
    177.33247043211506,
    213.9518420405694

]
rest = []
done = []


def calculate_angle(point1, point2, point3):
    point1x, point1y = point1[0]-point2[0], point1[1]-point2[1]
    point3x, point3y = point3[0]-point2[0], point3[1]-point2[1]
    a = atan2(point1y, point1x)
    c = atan2(point3y, point3x)
    if a < 0:
        a += pi*2
    if c < 0:
        c += pi*2
    if a > c:
        angle = pi*2 + c - a
    else:
        angle = (c - a)

    return degrees(angle)


def check_angle(sample):
    flag = False
    for i in range(len(sample)):
        if abs(sample[i] - joint_angles[i] > 20):
            flag = True
            break
    if flag:
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                  mp_drawing.DrawingSpec(
                                      color=(255, 255, 255), thickness=2, circle_radius=2),
                                  mp_drawing.DrawingSpec(
                                      color=(255, 255, 255), thickness=2, circle_radius=2)
                                  )
    else:
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                  mp_drawing.DrawingSpec(
                                      color=(124, 252, 0), thickness=2, circle_radius=2),
                                  mp_drawing.DrawingSpec(
                                      color=(124, 252, 0), thickness=2, circle_radius=2)
                                  )
    return flag


poses = [warrior, rest, mountain, tree, done]

n = 0


# Setup mediapipe instance
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5, model_complexity=2) as pose:
    n = 0

    i = 0
    while cap.isOpened():

        ret, frame = cap.read()

        # Recolor image to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        # Make detection
        results = pose.process(image)

        image.flags.writeable = True

        # Extract landmarks
        try:
            landmarks = results.pose_landmarks.landmark

            Lshoulder = [
                landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y,
                landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].z,
            ]
            Lelbow = [
                landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y,
                landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].z,
            ]
            Lwrist = [
                landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y,
                landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].z,
            ]
            Rshoulder = [
                landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y,
                landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].z,
            ]
            Relbow = [
                landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
                landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y,
                landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].z,
            ]
            Rwrist = [
                landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
                landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y,
                landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].z,
            ]
            Lhip = [
                landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
                landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y,
                landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].z,
            ]
            Lknee = [
                landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,
                landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y,
                landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].z,
            ]
            Lankle = [
                landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,
                landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y,
                landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].z,
            ]
            Rhip = [
                landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,
                landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y,
                landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].z,
            ]
            Rknee = [
                landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,
                landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y,
                landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].z,
            ]
            Rankle = [
                landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x,
                landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y,
                landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].z,
            ]

            joint_angles = [
                calculate_angle(
                    Lshoulder, Lelbow, Lwrist
                ),  # Calculates angle of left elbow
                calculate_angle(
                    Lhip, Lshoulder, Lelbow
                ),  # Calculates angle of left shoulder
                calculate_angle(
                    Rshoulder, Relbow, Rwrist
                ),  # Calculates angle of right elbow
                calculate_angle(
                    Rhip, Rshoulder, Relbow
                ),  # Calculates angle of right shoulder
                calculate_angle(
                    Lknee, Lhip, Rhip
                ),  # Calculates angle of left hip
                calculate_angle(
                    Rknee, Rhip, Lhip
                ),  # Calculates angle of right hip
                calculate_angle(
                    Lhip, Lknee, Lankle
                ),  # Calculates angle of left knee
                calculate_angle(
                    Rhip, Rknee, Rankle
                ),  # Calculates angle of right knee
                calculate_angle(
                    Lshoulder, Lhip, Lknee
                ),  # Calculates outer angle of left hip
                calculate_angle(
                    Rshoulder, Rhip, Rknee
                ),  # Calculates outer angle of right hip
            ]

            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                      mp_drawing.DrawingSpec(
                                          color=(255, 255, 255), thickness=2, circle_radius=2),
                                      mp_drawing.DrawingSpec(
                                          color=(255, 255, 255), thickness=2, circle_radius=2)
                                      )

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

            flag1 = check_angle(poses[n])

            if flag1 == False:
                i += 1
                bar.progress(i)

            if flag1:
                i = 0
                bar.progress(0)

            if i >= 100:
                i = 0
                bar.progress(0)
                n += 1
                if n == 1:
                    refpose.subheader("Rest")
                    reffw.image("Logo.png")
                    refinfo.text("Take a breather")

                elif n == 2:
                    refpose.subheader("Mountain Pose")
                    reffw.image("Mountain.jpg")
                    refinfo.text("""1. Stand with your big toes touching and your heels slightly apart.
2. Allow your arms to hang down at your sides. Your palms should face forward.
3. Relax your shoulders and open your heart center.
4.  Make sure to keep your back straight. Hold the pose till the bar reaches the
    end.""")
                elif n == 3:
                    refpose.subheader("Treepose")
                    reffw.image("Treepose.jpg")
                    refinfo.text("""1. Bear your weight on your right foot.
2. Bring your right foot to your left calf, or thigh.
3. Bring your arms in prayer pose in front of your chest.
4. Keep your gaze focused on a point on the floor in front of you.
5.. Remain in this pose for up to 1 minute.
""")

                elif n == 4:
                    refpose.subheader("Congratulations, workout complete!")
                    reffw.image(st.balloons())
                    refinfo.text("""You have officially compelted one session of your yoga therapy.
                     Make sure you log in tomorrow!""")
                    

            fw.image(image)

        except:
            pass


cap.release()
cv2.destroyAllWindows()
