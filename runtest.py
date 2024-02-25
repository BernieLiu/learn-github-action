import pytest
import os


if __name__ == '__main__':
    dir = os.path.abspath((os.path.dirname(''))) + os.path.sep + 'testcases' +  os.path.sep
    args = []
    plugins = []
    args.append(dir)    # 指定用例目录
    args.append('--clean-alluredir')
    args.append('--alluredir=allure-results')

    print(args)
    pytest.main(args)
    os.system(r"allure generate -c -o allure-report")