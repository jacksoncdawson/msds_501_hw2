import sys
import builtins
import contextlib
import importlib
import io
import pytest


# ----------------------------------------------------------------------
# Helper: run hw2.py once with a scripted sequence of user inputs
# ----------------------------------------------------------------------
def run_script(inputs, monkeypatch):
    """
    Execute hw2.py exactly once with the supplied `inputs`
    and return everything printed to stdout as a single string.
    """
    inp_iter = iter(inputs)

    def fake_input(_prompt=""):
        try:
            return next(inp_iter)
        except StopIteration:
            raise RuntimeError("ran out of test inputs") from None

    monkeypatch.setattr(builtins, "input", fake_input, raising=True)

    # import the module freshly
    sys.modules.pop("hw2", None)           # forget previous import
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        importlib.import_module("hw2")     # import executes the menu loop once

    return buf.getvalue()


# ----------------------------------------------------------------------
# Tests
# ----------------------------------------------------------------------
def test_option_1_unique_artists(monkeypatch):
    out = run_script(["1", "0"], monkeypatch)

    expected = (
        "Alex Warren, Benson Boone, Billie Eilish, Bruno Mars, "
        "Ed Sheeran, Lady Gaga, ROSÉ, Sabrina Carpenter"
    )
    assert expected in out


@pytest.mark.parametrize(
    "rank, expected",
    [
        ("3", "3: Sapphire by Ed Sheeran"),
        ("1", "1: APT. by ROSÉ, Bruno Mars"),
    ],
)
def test_option_2_valid_ranking(monkeypatch, rank, expected):
    out = run_script(["2", rank, "0"], monkeypatch)
    assert expected in out


def test_option_2_non_int(monkeypatch):
    out = run_script(["2", "abc", "0"], monkeypatch)
    assert "Invalid input. Please enter a number." in out


def test_option_2_out_of_range(monkeypatch):
    out = run_script(["2", "15", "0"], monkeypatch)
    assert "Ranking out of range." in out


def test_option_3_artist_found(monkeypatch):
    out = run_script(["3", "Lady gaga", "0"], monkeypatch).lower()
    assert "2: die with a smile" in out
    assert "10: abracadabra" in out


def test_option_3_artist_not_found(monkeypatch):
    out = run_script(["3", "Taylor Swift", "0"], monkeypatch)
    assert "No songs were found by Taylor Swift" in out


def test_option_4_longest_four(monkeypatch):
    out = run_script(["4", "4", "0"], monkeypatch)

    expected = [
        "Wildflower by Billie Eilish (261 seconds)",
        "Die With a Smile by Lady Gaga, Bruno Mars (251 seconds)",
        "Abracadabra by Lady Gaga (223 seconds)",
        "Manchild by Sabrina Carpenter (213 seconds)",
    ]

    # keep only lines that contain the word "seconds"
    song_lines = [ln for ln in out.splitlines() if "seconds" in ln]
    assert song_lines == expected


def test_option_4_shortest_three(monkeypatch):
    out = run_script(["4", "-3", "0"], monkeypatch)

    expected = [
        "APT. by ROSÉ, Bruno Mars (169 seconds)",
        "Espresso by Sabrina Carpenter (175 seconds)",
        "Sapphire by Ed Sheeran (179 seconds)"
    ]

    song_lines = [ln for ln in out.splitlines() if "seconds" in ln]
    assert song_lines == expected
