from ultralytics import YOLO
import cv2

# YOLOv8のポーズ推定モデルをロード
model = YOLO('yolov8n-pose.pt')  # 必要に応じてモデルを変更（例: yolov8s-pose.pt）

# 入力動画ファイルのパス
input_video_path = "video.mp4"
output_video_path = "output_pose_with_right_hand_trajectory.mp4"

# 動画を読み込む
cap = cv2.VideoCapture(input_video_path)
if not cap.isOpened():
    print(f"Error: Unable to open video file {input_video_path}")
    exit()

# 入力動画のプロパティを取得
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# 出力動画ファイルの設定
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

# 右手の軌跡を保存するためのリスト
right_hand_trajectory = []

# 動画処理ループ
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # 推論を実行
    results = model(frame)

    # 結果データをprint
    print("boxes:")
    print(results[0].boxes)         #バウンディングボックス
    print("keypoints:")
    print(results[0].keypoints)     #キーポイント

    # 推論結果の各人物について処理
    for pose in results[0].keypoints:

        # 右手（キーポイント6）を取得
        right_hand = pose.xy[0][10]  # キーポイントインデックスはモデル仕様に依存（6は右手）
        right_hand_conf = pose.conf[0][10]
        if right_hand_conf > 0.5:  # 信頼度が0.5以上の場合のみ使用
            # 右手の座標を保存
            x, y = int(right_hand[0]), int(right_hand[1])
            right_hand_trajectory.append((x, y))

    # 軌跡を描画
    for i in range(1, len(right_hand_trajectory)):
        cv2.line(frame, right_hand_trajectory[i - 1], right_hand_trajectory[i], (0, 255, 0), 2)

    # 推論結果を描画
    frame = results[0].plot()

    # 軌跡を描画したフレームを動画ファイルに書き込み
    out.write(frame)

# リソースを解放
cap.release()
out.release()

print(f"Pose estimation video with right hand trajectory saved to {output_video_path}")
