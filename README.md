## 🈯 説明言語 / Language Selection
- [🇯🇵 日本語版](#japanese)
- [🇺🇸 English Version](#English)
---

# <a name="japanese"></a>🇯🇵 日本語版
# 📘 Python機械学習（教材）
この教材は、小学生高学年〜高校生を対象に、Pythonを使って楽しく機械学習を学ぶことを目的とした体験型教材です。Jupyter Notebook形式で提供され、分類・回帰・強化学習を順に学び、最後は自分だけのAI作品を作ることができます。
## 🔖 教材の構成
## 📚 目次
- [🟦 第1回 – 機械学習とは？](#lesson1)
- [🟩 第2回 – 分類学習（1）：分類とは？](#lesson2)
- [🟨 第3回 – 分類学習（2）：精度と改善](#lesson3)
- [🟧 第4回 – 回帰学習（1）：予測って何？](#lesson4)
- [🟥 第5回 – 回帰学習（2）：精度と応用](#lesson5)
- [🟪 第6回 – 強化学習（1）：試して覚える](#lesson6)
- [🟫 第7回 – 強化学習（2）：上達するAI](#lesson7)
- [🔁 第8回 – 振り返りとまとめ](#lesson8)
- [🎓 最終回 – 作品づくり：自分のAIをつくろう！](#lesson_final)
- [✅ 備考](#備考)
- [📁 ファイル構成](#ファイル構成)

### <a name="lesson1"></a>🟦 第1回 – 機械学習とは？
**目的：機械学習の全体像を知る**
- 機械学習ってなに？どんなことができるの？
- 人とコンピュータの違い、なぜ学習が必要？
- 機械学習の３つのタイプ  
  └ 分類（分類とは何か、日常の例）  
  └ 回帰（予測するとはどういうことか）  
  └ 強化学習（ゲームやロボットと学習）
- 実例紹介（画像認識、音声認識、推薦システムなど）

**アクティビティ**
- 絵カードを使った「これは何の動物？」ゲーム
- 「AIはこんなことができるよ」動画視聴と感想共有

**プログラミング**
- Pythonで簡単な画像分類デモ（事前学習済モデル使用）

**演習問題あり**

---

### <a name="lesson2"></a>🟩 第2回 – 分類学習（1）：分類とは？
**目的：分類の考え方と基礎的な流れを学ぶ**
- 特徴量（色、形、大きさ）とは？
- データセットの概念（あやめの花、犬と猫）
- 学習とテストに分ける理由

**アクティビティ**
- お菓子分けゲーム
- 紙カードを使って分類

**プログラミング**
- Irisデータセットでの分類モデル（Pandas + scikit-learn）

**演習問題あり**

---

### <a name="lesson3"></a>🟨 第3回 – 分類学習（2）：精度と改善
**目的：分類モデルの精度と改善を学ぶ**
- 正解率と混同行列の理解
- モデルが間違える理由と改善方法（特徴量／データ量）

**アクティビティ**
- 手書き数字を描いて分類ゲーム

**プログラミング**
- MNISTを使った手書き数字分類（深層学習導入前）

**演習問題あり**

---

### <a name="lesson4"></a>🟧 第4回 – 回帰学習（1）：予測って何？
**目的：回帰の概念と線形予測を理解する**
- 回帰と分類の違い
- 線形回帰と「未来を当てる」考え方

**アクティビティ**
- 身長と靴のサイズから予測
- 線を引いて未来を予測しよう

**プログラミング**
- アイス売上 × 気温の線形回帰モデル作成

**演習問題あり**

---

### <a name="lesson5"></a>🟥 第5回 – 回帰学習（2）：精度と応用
**目的：精度向上の方法と他の手法の紹介**
- 外れ値、多変量回帰、決定木回帰など

**アクティビティ**
- サイコロの目の平均を考えよう
- 異常値を見つけるクイズ

**プログラミング**
- 面積・部屋数 → 家賃の予測（多変量回帰）

**演習問題あり**

---

### <a name="lesson6"></a>🟪 第6回 – 強化学習（1）：試して覚える
**目的：試行錯誤型学習の仕組みを知る**
- エージェント／環境／報酬
- ゴールへ向かう行動の最適化

**アクティビティ**
- 紙の迷路ゲーム（失敗から学ぶ）

**プログラミング**
- OpenAI Gym で迷路シミュレーション

**演習問題あり**

---

### <a name="lesson7"></a>🟫 第7回 – 強化学習（2）：上達するAI
**目的：繰り返し学習とQ学習の入門**
- ε-greedy法・Q学習の基本
- 実社会での応用（ロボット、自動運転）

**アクティビティ**
- 条件の違う迷路で再挑戦

**プログラミング**
- 迷路でQ-learningを体験

**演習問題あり**

---

### <a name="lesson8"></a>🔁 第8回 – 振り返りとまとめ
**目的：これまでの学びをつなげる**
- 分類／回帰／強化学習の違いと活用法
- AIを使ってできること・できないことを考える

**アクティビティ**
- 「AIで何をしたい？」ワークと発表

**演習問題あり**

---

### <a name="lesson_final"></a>🎓 最終回 – 作品づくり：自分のAIをつくろう！
**目的：学んだ技術を応用し、自分の作品を作る**

**自由課題例**
- フルーツ分類アプリ
- 自分の勉強時間から成績を予測するアプリ
- 強化学習でキャラクターを動かすゲーム

**発表会**
- 各自またはチームで成果発表＋フィードバック

---

## <a name="備考"></a>✅ 備考
- 各回の教材は `.ipynb`（Jupyter Notebook）形式で提供
- Pythonによる実装中心、図解と体験を重視
- 対象：小学生（高学年）〜高校生


## <a name="ファイル構成"></a>📁 ファイル構成
```
ML_lecture/
├── README.md                 # 教材の概要と構成（このファイル）
├── materials/                # 各回のJupyter Notebook教材（.ipynb形式）
│   ├── lesson_one.ipynb
│   ├── lesson_two.ipynb
│   └── ...（第8回＋作品制作）
├── problem/                  # 各回のPython演習問題とテストコード
│   ├── lesson_one/
│   │   ├── problems/         # 実装課題ファイル（problem_1.py ~ problem_15.py）
│   │   └── tests/            # 各課題に対するテストコード
│   ├── lesson_two/
│   │   └── ...
│   ├── ...（lesson_three ~ lesson_eight）
│   ├── other/                # 自由課題・作品制作用問題とテスト
│   └── run.py                # テスト一括実行などの補助スクリプト
```
- `materials/` ディレクトリには、各回の学習内容を記述したJupyter Notebookがあります。1つのノートブックで理論解説＋コード実演＋演習があります。
- `problem/` ディレクトリには、各レッスンに対応するPython演習課題と、それに対応する自動テストコードがあります。
- `run.py` は補助的なスクリプトで、テストの一括実行などに使用します。

---
# <a name="English"></a>🇺🇸 English Version
# 📘 Python Machine Learning (Educational Materials)
This educational material is an interactive curriculum designed for upper elementary to high school students to enjoy learning machine learning using Python. Provided in Jupyter Notebook format, it covers classification, regression, and reinforcement learning step by step, culminating in the creation of a personalized AI project.

## 🔖 Lesson Structure
## 📚 Table of Contents
- [🟦 Lesson 1 – What is Machine Learning?](#lesson1_en)
- [🟩 Lesson 2 – Classification (1): What is classification?](#lesson2_en)
- [🟨 Lesson 3 – Classification (2): Accuracy and improvement](#lesson3_en)
- [🟧 Lesson 4 – Regression (1): What is prediction?](#lesson4_en)
- [🟥 Lesson 5 – Regression (2): Accuracy and applications](#lesson5_en)
- [🟪 Lesson 6 – Reinforcement Learning (1): Learn through trial and error](#lesson6_en)
- [🟫 Lesson 7 – Reinforcement Learning (2): Learn by repeating](#lesson7_en)
- [🔁 Lesson 8 – Review and Reflection](#lesson8_en)
- [🎓 Final Lesson – Create Your Own AI Project!](#lesson_final_en)
- [✅ Notes](#Notes)
- [📁 Directory Structure](#Directory_Structure)

### <a name="lesson1_en"></a>🟦 Lesson 1 – What is Machine Learning?
**Objective: Understand the overall concept of machine learning**
- What is machine learning? What can it do?
- Differences between humans and computers, and why learning is necessary
- Three types of machine learning  
  └ Classification (what is classification, everyday examples)  
  └ Regression (what does it mean to make predictions?)  
  └ Reinforcement Learning (learning through games or robotics)
- Real-world examples (image recognition, speech recognition, recommendation systems)

**Activities**
- “What animal is this?” game using picture cards  
- Watch videos showing “What AI can do” and share reflections

**Programming**
- Simple image classification demo using a pre-trained Python model

**Includes practice problems**

---

### <a name="lesson2_en"></a>🟩 Lesson 2 – Classification (1): What is classification?
**Objective: Learn the concept of classification and its basic process**
- What are features? (color, shape, size)
- What is a dataset? (e.g., iris flowers, dogs and cats)
- Why do we split data into training and testing?

**Activities**
- Candy sorting game  
- Classification using paper cards

**Programming**
- Build a classification model using the Iris dataset (Pandas + scikit-learn)

**Includes practice problems**

---

### <a name="lesson3_en"></a>🟨 Lesson 3 – Classification (2): Accuracy and improvement
**Objective: Learn how to evaluate model accuracy and improve it**
- Understanding accuracy and the confusion matrix
- Why models make mistakes and how to improve them (feature engineering, more data)

**Activities**
- Draw your own handwritten numbers and classify them

**Programming**
- Classify handwritten digits using the MNIST dataset (pre-deep learning)

**Includes practice problems**

---

### <a name="lesson4_en"></a>🟧 Lesson 4 – Regression (1): What is prediction?
**Objective: Understand the concept of regression and linear prediction**
- The difference between regression and classification
- Using linear regression to make future predictions

**Activities**
- Predict shoe size based on height  
- Draw a line to predict future values

**Programming**
- Build a linear regression model: Ice cream sales × temperature

**Includes practice problems**

---

### <a name="lesson5_en"></a>🟥 Lesson 5 – Regression (2): Accuracy and applications
**Objective: Improve prediction accuracy and learn other methods**
- Why predictions fail (outliers, insufficient data)
- Multivariable regression, decision tree regression

**Activities**
- Guess the average dice roll  
- Find outliers in data

**Programming**
- Use multiple features to predict house rent (e.g., area, number of rooms)

**Includes practice problems**

---

### <a name="lesson6_en"></a>🟪 Lesson 6 – Reinforcement Learning (1): Learn through trial and error
**Objective: Understand the structure of trial-and-error-based learning**
- What is reinforcement learning? (actions and rewards)
- Logic of finding a path to the goal
- Relationship between agent, environment, and rewards

**Activities**
- Paper maze game (learn from choices and results)

**Programming**
- Simulate a maze with OpenAI Gym

**Includes practice problems**

---

### <a name="lesson7_en"></a>🟫 Lesson 7 – Reinforcement Learning (2): Learn by repeating
**Objective: Understand continuous learning in reinforcement learning**
- Learning curves and improvement through practice
- Introduction to ε-greedy strategy and Q-learning
- Connections to robotics and self-driving technology

**Activities**
- Try a modified maze with new rules

**Programming**
- Implement basic Q-learning in a maze environment

**Includes practice problems**

---

### <a name="lesson8_en"></a>🔁 Lesson 8 – Review and Reflection
**Objective: Summarize and connect everything learned**
- Differences and similarities among classification, regression, and reinforcement learning
- Think about how machine learning can (or cannot) be used

**Activities**
- Workshop: “What kind of AI do you want to build?” + sharing

**Includes practice problems**

---

### <a name="lesson_final_en"></a>🎓 Final Lesson – Create Your Own AI Project!
**Objective: Apply everything you’ve learned to create a personalized project**

**Example project ideas**
- Fruit classification app  
- Predict your own test scores based on study time  
- Build a game with a character that learns using reinforcement learning

**Final Presentation**
- Individual or team presentations + feedback session

---

## <a name="Notes"></a>✅ Notes
- Each lesson is provided in `.ipynb` format (Jupyter Notebook)
- Focus on Python-based implementation, visualization, and interactive activities
- Designed for: Upper elementary to high school students

---

## <a name="Directory_Structure"></a>📁 Directory Structure
```
ML_lecture/
├── README.md                # Curriculum overview
├── materials/               # Jupyter Notebooks for each lesson
│   ├── lesson_one.ipynb
│   ├── lesson_two.ipynb
│   └── ... (up to lesson 8 and final project)
├── problem/                 # Practice problems and test scripts
│   ├── lesson_one/
│   │   ├── problems/        # problem_1.py ~ problem_15.py
│   │   └── tests/           # test_problem_1.py ~ test_problem_15.py
│   ├── lesson_two/
│   │   └── ...
│   ├── ... (lesson_three ~ lesson_eight)
│   ├── other/               # Final project problems and tests
│   └── run.py               # Script to run all tests at once
```
- `materials/`: Contains the Jupyter Notebooks for each lesson, including theory explanations, code demonstrations, and exercises.
- `problem/`: Contains Python practice problems and their corresponding automated test scripts for each lesson.
- `run.py`: Utility script to easily run all test cases.