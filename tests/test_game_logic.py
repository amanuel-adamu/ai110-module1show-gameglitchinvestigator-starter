from logic_utils import check_guess, update_score

# FIX: Fixed with agent - check_guess() returns tuple (outcome, message) not just outcome
def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

def test_high_low_hint_bug_fix():
    """
    Targets the bug where hint messages were backwards.
    When guess is too high, message should say "Go LOWER!" (not "Go HIGHER!").
    When guess is too low, message should say "Go HIGHER!" (not "Go LOWER!").
    """
    # Test high guess - should recommend going lower
    outcome_high, message_high = check_guess(60, 50)
    assert outcome_high == "Too High", "Outcome should be 'Too High'"
    assert "LOWER" in message_high, f"Message should suggest going LOWER, got: {message_high}"
    assert "HIGHER" not in message_high, f"Message should NOT suggest going HIGHER, got: {message_high}"
    
    # Test low guess - should recommend going higher
    outcome_low, message_low = check_guess(40, 50)
    assert outcome_low == "Too Low", "Outcome should be 'Too Low'"
    assert "HIGHER" in message_low, f"Message should suggest going HIGHER, got: {message_low}"
    assert "LOWER" not in message_low, f"Message should NOT suggest going LOWER, got: {message_low}"

# FIX: Added with agent - targets the attempts initialization bug we fixed
def test_first_attempt_win_scoring():
    """
    Test that validates the attempts initialization bug fix.
    If attempts started at 1 instead of 0, the first user guess would be 
    attempt #2, causing wrong scoring. With correct initialization to 0,
    the first guess should be attempt #1, earning 80 points (100 - 10*2).
    """
    # First attempt (attempt_number=1) winning guess should give 80 points
    score = update_score(0, "Win", 1)
    assert score == 80, f"Expected 80 points for first attempt win, got {score}"
