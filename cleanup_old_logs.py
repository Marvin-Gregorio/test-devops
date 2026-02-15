from pathlib import Path
from time import time
import argparse


def cleanup_old_logs(directory, days=30, dry_run=True):
    now = time()
    seconds_in_a_day = 60 * 60 * 24
    seconds = days * seconds_in_a_day

    path = Path(directory)
    for file in path.rglob('*.log'):
        try:
            if file.stat().st_mtime < (now - seconds):
                if dry_run:
                    print(f'[DRY RUN] Deleted {file.name}')
                else:
                    file.unlink()
                    print(f'Deleted {file.name}')
        except PermissionError as e:
            print(f'File: {file.name} cannot be deleted due to {e}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Cleanup old log files.')
    parser.add_argument('dir', help='Directory of the logs you want to delete')
    parser.add_argument('--days', type=int, default=30, help='Days since a '
                        'logs has been updated. Default is 30 days.')
    parser.add_argument('--execute', action='store_false', dest='dry_run',
                        help='Add this arguments if you want to actually'
                        'delete log file.')
    parser.set_defaults(dry_run=True)

    args = parser.parse_args()

    cleanup_old_logs(args.dir, args.days, args.dry_run)
