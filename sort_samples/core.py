#!/usr/bin/env python3
from pathlib import Path
import shutil
import logging
import re


# ---------------- IMPORT CONFIG ---------------- #
from sort_samples.config_user import COPY_FILES, SOURCE_DIR, TARGET_DIR, USER_CATEGORIES
# ------------------------------------------------ #

__all__ = ['infer_category']

# Create TOKEN_MAP for fast lookups:
TOKEN_MAP: dict[str, str] = {
    synonym: category
    for category, syns in USER_CATEGORIES.items()
    for synonym in syns
}
TOKEN_SPLIT = re.compile(r"[\W_]+")  # Non-word characters and underscores


def _tokenize(text: str) -> list[str]:
    return [t for t in TOKEN_SPLIT.split(text.lower()) if t]


def _build_token_map(categories: dict[str, list[str]]) -> dict[str, str]:
    return {
        synonym: category
        for category, syns in categories.items()
        for synonym in syns
    }


def infer_category(path: Path, categories: dict[str, list[str]] = USER_CATEGORIES) -> str:
    token_map = _build_token_map(categories)

    parts = _tokenize(path.stem)
    for folder in path.parents:
        parts.extend(_tokenize(folder.name))

    for tok in parts:
        if tok in token_map:
            return token_map[tok]

        base = tok.rstrip("0123456789")
        if base and base in token_map:
            return token_map[base]

    return '_unsorted'


def _create_output_folders(target: Path) -> None:
    for folder in list(USER_CATEGORIES) + ['_unsorted']:
        (target / folder).mkdir(parents=True, exist_ok=True)


def sort_samples(source: Path, target: Path, copy_files: bool) -> None:
    _create_output_folders(target)

    for file in source.rglob('*'):
        if not file.is_file():
            continue

        dest = target / infer_category(file) / file.name

        if dest.exists():
            logging.warning("Skipping existing %s", dest)
            continue

        logging.info("%s %s → %s",
                     "Copying" if copy_files else "Moving", file, dest)

        if copy_files:
            shutil.copy2(file, dest)
        else:
            shutil.move(file, dest)

    if not copy_files:
        # Clean up empty dirs left behind by moves
        for folder in sorted(source.glob('**/*'), reverse=True):
            if folder.is_dir() and not any(folder.iterdir()):
                folder.rmdir()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    if SOURCE_DIR.resolve() == TARGET_DIR.resolve():
        raise ValueError("SOURCE_DIR and TARGET_DIR must differ.")

    sort_samples(SOURCE_DIR, TARGET_DIR, COPY_FILES)
    logging.info("Sorting completed.")
