# Ultralyticsライブラリを用いたYoloによる姿勢推論サンプル

## プログラムの概要
姿勢推論を行い、取得した結果を利用するサンプルである。
姿勢推論の結果を取得し、対象の右手首の位置を記録、軌跡として描画している。


## 実行方法
事前にUltralyticsのライブラリをインストールする必要があります。
```
pip install ultralytics
```

処理する対象の動画ファイルは、ファイル名を`video.mp4`としてプロジェクトのルートディレクトリに配置します。

`main.py`ファイルを実行します。
```
python main.py
```

実行結果は動画ファイル`output_pose_with_right_hand_trajectory.mp4`として保存されます。

## 備考

行 39-42  
処理には必要ないが、推論結果の戻り値の内容を把握するためコンソールに出力している

results[0].boxesの仕様
https://docs.ultralytics.com/reference/engine/results/#ultralytics.engine.results.Boxes

results[0].boxesの仕様
https://docs.ultralytics.com/reference/engine/results/#ultralytics.engine.results.Keypoints

