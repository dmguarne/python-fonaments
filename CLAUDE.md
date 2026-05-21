# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

Personal repository for programming exercises from online courses. Organized by language.

## Structure

```
python/       # Python exercises
javascript/   # JavaScript/Node.js exercises
sql/          # SQL exercises and schemas
```

Each subfolder may contain course-specific subfolders (e.g., `python/curs-nom/`).

## Python

```bash
# Run a script
python3 python/<path>/exercise.py

# Run tests (if pytest is used)
pytest python/<path>/

# Interactive
python3 -i python/<path>/exercise.py
```

Dependencies are managed per-exercise or per-course with a local `requirements.txt`:
```bash
pip install -r python/<course>/requirements.txt
```

## JavaScript

```bash
# Run a script with Node
node javascript/<path>/exercise.js

# Run tests (if Jest is used)
npx jest javascript/<path>/

# Install deps if a package.json exists
npm install
```

## SQL

SQL files contain schema definitions and queries. Run against a local database:

```bash
# SQLite
sqlite3 :memory: < sql/<path>/exercise.sql

# PostgreSQL
psql -d <db> -f sql/<path>/exercise.sql
```

## Conventions

- One file per exercise unless the exercise itself requires multiple files.
- Exercises are standalone; avoid shared utilities unless a course explicitly builds a project.
