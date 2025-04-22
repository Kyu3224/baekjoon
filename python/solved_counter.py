import os
import ast

def count_functions_in_file(file_path):
    """파일 내에서 `_`로 시작하는 함수 정의 개수 반환"""
    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            tree = ast.parse(f.read(), filename=file_path)
            return sum(
                isinstance(node, ast.FunctionDef) and node.name.startswith('_')
                for node in ast.walk(tree)
            )
        except SyntaxError:
            print(f"[SyntaxError] {file_path} 파일을 파싱할 수 없습니다.")
            return 0

def count_functions_in_directory(root_dir):
    """디렉토리 내 모든 .py 파일의 함수 정의 개수 총합 반환"""
    total_functions = 0
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".py"):
                full_path = os.path.join(dirpath, filename)
                func_count = count_functions_in_file(full_path)
                print(f"{full_path} -> {func_count} functions")
                total_functions += func_count
    return total_functions


if __name__ == "__main__":
    directory = f"{os.getcwd()}"
    total = count_functions_in_directory(directory)
    print(f"\n총 함수 개수: {total}")
