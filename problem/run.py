import pytest
import sys
import os
import glob

def run_test(chapter, problem=None):
    test_dir = f"{chapter}/tests/"
    
    # テストディレクトリが存在しない場合
    if not os.path.exists(test_dir):
        print(f"❌ {chapter}のテストフォルダが見つかりません。")
        return

    # 特定の問題だけをテスト
    if problem:  
        test_file = f"{test_dir}/test_problem_{problem}.py"
        if not os.path.exists(test_file):
            print(f"❌ {chapter}の{problem}問目のテストが見つかりません。")
            return
        test_files = [test_file]
    else:  
        # すべての問題をテスト
        test_files = glob.glob(f"{test_dir}/test_problem_*.py")

    print(f"🔍 {chapter}の{'すべての問題' if not problem else f'{problem} 問目'}をテスト中...\n")

    failed_tests = []

    for test_file in test_files:
        print(f"▶️ テスト実行中: {test_file}")
        result = pytest.main(["-q", test_file, "--disable-warnings"])
        if result != 0:
            failed_tests.append(test_file)

    # 結果の集計
    total_tests = len(test_files)
    failed_count = len(failed_tests)
    success_count = total_tests - failed_count

    print("\n===============================")

    if failed_count == 0:
        print(f"🎉 {chapter}の{'すべての問題' if not problem else f'{problem}問目'}クリア！")
    else:
        print(f"❌ {chapter}の以下の問題でエラーが発生しました（{total_tests}問中{failed_count}問不正解）:\n")

        def extract_problem_number(filepath):
            name = os.path.basename(filepath)
            num_part = name.replace("test_problem_", "").replace(".py", "")
            return int(num_part)

        failed_tests_sorted = sorted(failed_tests, key=extract_problem_number)

        for f in failed_tests_sorted:
            problem_name = os.path.basename(f).replace("test_", "").replace(".py", "")
            print(f"   - {problem_name}")

    print("\n✅ 正解: ", success_count)
    print("❌ 不正解: ", failed_count)
    print("===============================\n")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❗ 実行方法: python run.py lesson_one [問題番号]  (例: python run.py lesson_one 1)")
        print("❗ 実行方法: python run.py [レッスン名]  (例: python run.py lesson_one)")
    else:
        chapter = sys.argv[1]
        problem = sys.argv[2] if len(sys.argv) > 2 else None
        run_test(chapter, problem)
