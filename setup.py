from setuptools import setup, find_packages

setup(
    name='git_repo_data',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # Add any dependencies here
    ],
    entry_points={
        'console_scripts': [
            'git_repo_data-command = git_repo_data.__main__:main',
        ],
    },
)

# python your_script.py --token YOUR_GITHUB_TOKEN_HERE
