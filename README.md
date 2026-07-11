# __Duplicate-Finder__ 🔍

This program can find and remove duplicate files within a given folder by comparing file sizes and SHA-256 checksums.

You can use this program to quickly identify duplicate files without unnecessarily hashing every file, making the process faster and more efficient.

The program first filters files by size, then compares only matching files using SHA-256 checksums to confirm whether they are true duplicates.

## Features:
- Allows you to search for duplicates within a chosen folder
- Uses file size as a fast first-stage filter
- Uses SHA-256 checksums for accurate duplicate detection
- Avoids unnecessary file hashing to improve performance
- Displays all detected duplicate files
- Allows you to delete duplicate copies while keeping one version
- Supports any file type

## Requirements:
- Python 3.8+
- Read/write permissions for target folder