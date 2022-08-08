from setuptools import setup, find_namespace_packages

setup(
    name='bot_helper',
    version='1.0.0',
    description='console bot helper that recognizes commands entered from the keyboard',
    url='https://github.com/DmytroLievoshko/lesson-nine-functions_decorators_closures.git',
    author='Dmytro Lievoshko',
    author_email='levka296@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    include_package_data=True,
    entry_points={'console_scripts': [
        'bot_helper = bot_helper.main:main',
        'bot_helper_help = bot_helper.main:print_help']}
)
