# src/main.py 

import argparse 

def main():
    parser = argparse.ArgumentParser(description="Command-line To-Do List Application")
    args = parser.parse_args()

import argparse

def main():
    parser = argparse.ArgumentParser(description="Command-line To-Do List Application")
    subparsers = parser.add_subparsers(dest='command')