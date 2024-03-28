import argparse
import logging

from git_repo import get_repo
from logger_config import logger_config
from repo_data import extract
from create_graph import create_dot_graph


def main():
    logger = logging.getLogger(__name__)

    parser = argparse.ArgumentParser(description='GitHub Token for Forked Repository')
    parser.add_argument('--token', help='GitHub token for authentication')
    parser.add_argument('--log-to-file', action='store_true', help='Log to a file instead of stdout')
    parser.add_argument('--debug', action='store_true', help='Enable debug mode')
    args = parser.parse_args()

    # Configure the logger
    logger_config(args)

    args.token = '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'
    repo_url = 'https://api.github.com/repos/CTFd/CTFd'
    dir_path = '../graph'

    if args.token:
        github_token = args.token
        logger.info(f'GitHub Token: {github_token}')

        extract(github_token, repo_url)

        repo_request_url = f'https://{github_token}@github.com/CTFd/CTFd'
        repo = get_repo(github_token, repo_request_url)
        # my forked repo
        create_dot_graph(repo, dir_path, 'improve-language')

    else:
        logger.info('Please provide a GitHub token using --token')


if __name__ == "__main__":
    main()
