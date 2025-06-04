from pathlib import Path

COPY_FILES = True  # True → copy, False → move
SOURCE_DIR = Path(r'C:\Users\You\Desktop\splice new\merged')
TARGET_DIR = Path(r'C:\Users\You\Desktop\Ableton\sorted')

TEST_CATEGORIES: dict[str, list[str]] = {
    'hat':          ['hat', 'hh', 'hihat'],
    'kick':         ['kick', 'kck', 'kik'],
    'snare':        ['snare', 'sd'],
    'clap':         ['clap', 'clps'],
    'perc':         ['perc', 'percussion'],
    'crash':        ['crash'],
    'cymbal':       ['cymbal', 'cym'],
    'bass':         ['bass', 'sub'],
    'synth':        ['synth', 'lead', 'pad', 'pluck'],
    'piano':        ['piano', 'keys'],
    'guitar':       ['guitar'],
    'vox':          ['vox', 'vocal', 'voice'],
    'fx':           ['fx', 'effect', 'sfx'],
    'tambourine':   ['tambourine', 'tamb'],
    'clave':        ['clave'],
    'shaker':       ['shaker', 'shk']
}

TEST_CATEGORIES_2: dict[str, list[str]] = {
    'clonk': ['clonk', 'klonk'],
    'boing': ['boing', 'boingg']
}
