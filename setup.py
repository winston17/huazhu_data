from cx_Freeze import setup, Executable

base = None

executables = [Executable('huazhu.py', base=base)]

packages = ['idna', 'csv', 'time', 'os']
options = {
    'build_exe': {
        'packages': packages,
    },
}

setup(
    name="华住会泄露信息查询",
    options=options,
    version="0.1.0",
    description='<初学者脚本，用来查询自己是不是在已经泄露的华住会数据中>',
    executables=executables
)
