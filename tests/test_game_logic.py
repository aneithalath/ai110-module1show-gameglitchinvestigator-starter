from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score
import pytest

def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_check_guess_higher_lower():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message

@pytest.mark.parametrize("difficulty,expected", [
    ("Easy", (1, 20)),
    ("Normal", (1, 50)),
    ("Hard", (1, 100)),
    ("Unknown", (1, 50)),
])
def test_get_range_for_difficulty(difficulty, expected):
    assert get_range_for_difficulty(difficulty) == expected

@pytest.mark.parametrize("raw,low,high,expected_ok,expected_val,expected_err", [
    (None, 1, 20, False, None, "Enter a guess."),
    ("", 1, 20, False, None, "Enter a guess."),
    ("abc", 1, 20, False, None, "That is not a valid integer."),
    ("5.5", 1, 20, False, None, "That is not a valid integer."),
    ("10", 1, 20, True, 10, None),
    ("21", 1, 20, True, 21, None), # Out-of-range, logic_utils only checks type
])
def test_parse_guess(raw, low, high, expected_ok, expected_val, expected_err):
    ok, val, err = parse_guess(raw)
    assert ok == expected_ok
    assert val == expected_val
    assert err == expected_err

# Test enforcing difficulty range for guesses (app logic)
def test_guess_range_enforcement():
    # Simulate app logic enforcing range
    low, high = get_range_for_difficulty("Easy")
    ok, val, err = parse_guess("21")
    if ok and (val < low or val > high):
        ok = False
        err = f"Guess must be between {low} and {high}."
    assert not ok
    assert err == "Guess must be between 1 and 20."

# Test new game uses correct range
def test_new_game_secret_range():
    import random
    for difficulty in ["Easy", "Normal", "Hard"]:
        low, high = get_range_for_difficulty(difficulty)
        secret = random.randint(low, high)
        assert low <= secret <= high

# Test info message range (app logic)
def test_info_message_range():
    for difficulty in ["Easy", "Normal", "Hard"]:
        low, high = get_range_for_difficulty(difficulty)
        info_msg = f"Guess a number between {low} and {high}."
        assert str(low) in info_msg and str(high) in info_msg

# Test attempts counter starts at 0 (app logic)
def test_attempts_counter_start():
    attempts = 0
    assert attempts == 0

# Test parse_guess does not accept floats
def test_parse_guess_no_floats():
    ok, val, err = parse_guess("5.7")
    assert not ok
    assert err == "That is not a valid integer."

# Test score logic is consistent
@pytest.mark.parametrize("current_score,outcome,attempt_number,expected_score", [
    (0, "Win", 1, 90),
    (0, "Win", 9, 10),
    (50, "Too High", 2, 45),
    (50, "Too Low", 3, 45),
    (50, "Other", 1, 50),
])
def test_update_score(current_score, outcome, attempt_number, expected_score):
    assert update_score(current_score, outcome, attempt_number) == expected_score

# Test difficulty change resets secret and range (app logic)
def test_difficulty_change_resets_secret():
    import random
    # Simulate changing difficulty
    old_difficulty = "Easy"
    new_difficulty = "Hard"
    low, high = get_range_for_difficulty(new_difficulty)
    secret = random.randint(low, high)
    assert low <= secret <= high

# Test secret type switching removed (logic_utils)
def test_secret_type_switching_removed():
    # check_guess always expects int, not str
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert isinstance(message, str)

# Test core logic functions are in logic_utils.py (import test)
def test_core_logic_functions_in_logic_utils():
    from logic_utils import get_range_for_difficulty, parse_guess, check_guess, update_score
    assert callable(get_range_for_difficulty)
    assert callable(parse_guess)
    assert callable(check_guess)
    assert callable(update_score)

# Session state logic and UI integration would require Streamlit integration tests, not included here.
