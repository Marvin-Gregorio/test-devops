import argparse
import subprocess


def restart_service(service_name):
    try:
        result = subprocess.run(
            ['systemctl', 'restart',  service_name],
            check=True, capture_output=True, text=True
        )
        print(f'success: {result.stdout}')
    except subprocess.CalledProcessError as e:
        print(f'error: {e.stderr}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='restart a service')
    parser.add_argument('--name', type=str, help='Name of service')
    args = parser.parse_args()
    restart_service(args.name)
