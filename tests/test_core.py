import pytest
from sort_samples.core import infer_category
from tests.config_tests import TEST_CATEGORIES, TEST_CATEGORIES_2
from pathlib import Path

EXAMPLES = {
    # direct filename tokens
    "kick_808.wav":            "kick",
    "snare_top.wav":           "snare",
    "hat-loop.wav":            "hat",
    "fx_impact.mp3":           "fx",
    "vocal_dry.wav":           "vox",
    "sd_layer.aif":            "snare",

    # folders triggering match
    "Drums/Snare/sn_01.wav":   "snare",
    "FX/transition.wav":       "fx",
    "Reverb/FX_hit.wav":       "fx",
    "Loops/hh_top.wav":        "hat",
    "Bass/808_sub.wav":        "bass",

    # folder tokens with multiple hits → first token wins
    "Kick/Bass/xyz.wav":       "bass",

    # filename wins over folder tokens
    "Kick/hat.wav":            "hat",

    # suffix stripping
    "clap3.wav":               "clap",
    "pad01.flac":              "synth",
    "sub_synth_pad.flac":      "bass",

    # multiple hits → first token wins
    "fx_crash.wav":            "fx",

    # no match
    "randomfile.wav":          "_unsorted",
    "random_sound.wav":        "_unsorted",
    "misc/strangefile.mp3":    "_unsorted",
}


@pytest.mark.parametrize("rel_path, expected", EXAMPLES.items())
def test_infer_category(rel_path, expected):

    assert isinstance(rel_path, str), "Path must be a string"
    assert isinstance(expected, str), "Expected category must be a string"

    result = infer_category(Path(rel_path), categories=TEST_CATEGORIES)

    assert result == expected, f"ERROR {rel_path!r}: got {result!r}, expected {expected!r}"


def test_infer_clonk():
    result = infer_category(Path("magic_clonk.wav"),
                            categories=TEST_CATEGORIES_2)
    assert result == "clonk"
