# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

The game loaded with a sidebar for settings and a main panel titled "Game Glitch Investigator" with an input box to guess a number. However, right at launch, the status box says "Attempts left: 7" even though I haven't submitted a single guess yet, which seems like an immediate bug since the sidebar states 8 attempts are allowed.

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
1. The hints were completely reversed. The game said "Go Higher" when it was supposed to say "Go Lower", and vice versa.
2. When I entered a number outside the 1-100 range, the game didn't say anything.
3. The game displayed an "Out of Attempts" message even though it indicated there was still "Attempts left: 1" remaining.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|Guess of 50 (secret is 59)|"Go Higher" hint|"Go Lower" hint|none|
|Guess of -200|warning or error about being out of range|gave no error and just said "Go Lower"|none|
|Clicking "Submit Guess" when 1 attempt was left|The game should let me submit the guess|displayed "Out of Attempts"|none|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Gemini and Claude.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

The AI correctly identified that initializing the game's attempt counter to 1 instead of 0 caused the game loop to count prematurely. This meant the player would run out of attempts one turn early. The AI suggested starting the counter at 0 so the game tracked the total attempts accurately.

I verified this manually by running the live Streamlit app in the browser, playing through to the maximum attempt limit, and confirming that I was allowed the exact number of guesses specified.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

When I first asked the AI to fix the assertion mismatch in the test suite, it modified test_game_logic.py but failed to properly account for the new data format. Because our updated check_guess() function returns a two-item tuple (outcome, message) instead of a single string, the AI's initial test refactor still caused an AssertionError because it tried to directly compare the entire tuple to a single string ("Win").

I ran python -m pytest in the terminal, and the test run immediately crashed with a series of red FAILED messages. It showed that comparing ("Win", "🎉 Correct!") == "Win" was mathematically false in Python, which proved the AI's test update was broken and required us to unpack the tuple elements explicitly.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I knew a bug was truly fixed when two things happened: all of the automated code tests in the terminal passed, and the live application ran smoothly in the browser without any errors or glitches when I tested it by hand.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
I ran the automated unit test test_guess_too_high using python -m pytest. It showed me that our refactored check_guess function in logic_utils.py accurately caught a high guess (evaluating a guess of 60 against a secret of 50) and cleanly returned the exact "Too High" string outcome we needed.
- Did AI help you design or understand any tests? How?
Yes. The AI helped me understand how to unpack data tuples in Python. Because our refactored game engine returns a multi-valued tuple (outcome, message), the AI showed me how to structure the test code using outcome, message = check_guess(...) so that the assertions could isolate and verify individual pieces of data cleanly.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Streamlit reruns the entire script every time a user interacts with the app, which means variables reset unless you save them. Session state is like memory that persists across reruns—without it, game hints and attempt counts would disappear. We learned this the hard way when our hints vanished after calling `st.rerun()`, so we had to store them in `st.session_state` first to make them stick around.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
I want to reuse the habit of writing and running targeted unit tests (like using `pytest`) before writing or changing the app code. Having failing tests clearly define the bug first gave me a precise target to fix and ensured I didn't break existing features when updating the game logic.

- What is one thing you would do differently next time you work with AI on a coding task?
Next time, I will explicitly ask the AI to explain the underlying logic or system architecture—such as how Streamlit manages state—before accepting code changes. This will prevent me from implementing quick fixes that inadvertently cause state amnesia or vanish after a rerun.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
This project made me realize that AI-generated code is a powerful starting point but cannot be blindly trusted. It requires intentional human oversight, structured testing, and a solid understanding of the framework to catch hidden logic flaws or backward messages.
