# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

At the start, multiple things were broken. Firstly, the "lower" and "higher" prompts were flipped, with numbers being too big outputting "GO HIGHER" instead of "GO LOWER," and vice versa. Moreover, the medium difficulty has a range of 1-100 while the hard difficulty has a range of 1-50 (these should be flipped). Finally, no error message is shown for inputs that aren't in the range provided (e.g. user inputs "21" when the range is 1-20).
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used ChatGPT for this project. One example of a correct AI suggestion was how the parse_guess() function always checked for guesses between 1 and 100, regardless of the selected difficulty. I verified the result by manually testing the app and I saw that the correct answer was always between 1 and 100 regardless of the difficulty. A suggestion that was misleading was that it said the attempt counter started at 1 instead of 0, but whenever a new game was started, the actual attempt count was initialized at 0, not 1.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided a bug was really fixed by running multiple tests with sample values and expected outputs. One test I ran was to check the high/low logic on pytest to check if the correct message (TOO HIGH or TOO LOW) was shown. This showed me whether my code was actually checking it properly. I asked Copilot to design the test file for me, but I checked the test itself and wanted to control the input and output being tested. 
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?
The secret number kept changing in the original app because it was being regenerated every time the app reran, rather than being stored persistently. Streamlit re-ran the script from top to bottom every tim teh user interacted with the app. Session state acts like a persistent dictionary that remembers values between reruns so things like the secret number don't get reset unless you explicitly change them.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit I want to resuse is writing targeted pytest cases for every bug I fix since it helps me confirm that my changes actually work. One thing I could do differently would be to be more proactive about double checking what the AI does, since the AI generated code often had multiplie simple mistakes that I would miss if I didn't review the code carefully. This project showed me clearly how AI-generated code can be really handy, but it could also be detrimental if not combined with careful testing and validation. 