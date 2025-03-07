import pytest
import sys
import os
import glob

def run_test(chapter, problem=None):
    test_dir = f"{chapter}/tests/"
    
    if not os.path.exists(test_dir):
        print(f"❌ {chapter}のテストフォルダが見つかりません。")
        return

    if problem:  
        test_file = f"{test_dir}/test_problem_{problem}.py"
        if not os.path.exists(test_file):
            print(f"❌ {chapter}の{problem}問目のテストが見つかりません。")
            return
        test_files = [test_file]
    else:  
        test_files = glob.glob(f"{test_dir}/test_problem_*.py")

    print(f"🔍 {chapter}の{'すべての問題' if not problem else f'{problem} 問目'}をテスト中...\n")

    failed_tests = []
    for test_file in test_files:
        print(f"▶️ テスト実行中: {test_file}")
        result = pytest.main(["-q", test_file, "--disable-warnings"])
        
        if result != 0:
            failed_tests.append(test_file)

    print("\n===============================")
    if not failed_tests:
        print(f"🎉 {chapter}の{'すべての問題' if not problem else f'{problem}問目'}クリア！")
    else:
        print(f"❌ {chapter}の以下の問題でエラーが発生しました。コードを修正してください。\n")
        for failed in failed_tests:
            print(f"   - {failed.replace(test_dir, '').replace('.py', '')}")
    print("===============================\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❗ 実行方法: python run.py 第1回 [問題番号]  (例: python run.py 第1回 1)")
        print("❗ 実行方法: python run.py 第[レッスン番号]回  (例: python run.py 第1回)")
    else:
        chapter = sys.argv[1]
        problem = sys.argv[2] if len(sys.argv) > 2 else None
        run_test(chapter, problem)