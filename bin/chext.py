#!/usr/bin/env python3
import os
import sys
import argparse

def fmt(ext):
    """Ensure ext format in lower case and starts with ., ex: .bat"""
    return '.' + ext.strip().strip('.').lower()


def cli():
    parser = argparse.ArgumentParser(
        description='Change ext for files in a dir',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument('-v', '--verbose', dest='verbose', action='store_true', help='Be verbose')
    parser.add_argument('--dry-run', dest='dry_run', action='store_true', help='Dry run')
    parser.add_argument('src_ext', help='Source ext, e.g.: .bat')
    parser.add_argument('dst_ext', help='Dest ext, e.g.: .cmd')
    parser.add_argument('folder', nargs='?', default='.', help='Working folder')
    return parser.parse_args()

def main():
    args = cli()
    src_ext = fmt(args.src_ext)
    dst_ext = fmt(args.dst_ext)

    total = 0
    # Loop through all files in the directory
    for filename in os.listdir(args.folder):
        # Check if the file has a expected extension
        if filename.lower().endswith(src_ext):
            new_filename = os.path.splitext(filename)[0] + dst_ext
            if not args.dry_run:
                os.rename(
                    os.path.join(args.folder, filename),
                    os.path.join(args.folder, new_filename)
                )
            print(f"Renamed {filename} => {new_filename}")
            total += 1
    print(f'total renamed: {total}')


if __name__ == '__main__':
    main()

