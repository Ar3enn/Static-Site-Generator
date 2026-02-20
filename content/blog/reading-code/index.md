# The Most Underrated Skill in Software Engineering

[< Back Home](/)

![A terminal showing a codebase being navigated](/images/terminal.png)

> "Programs must be written for people to read, and only incidentally for machines to execute."
>
> -- Harold Abelson, _Structure and Interpretation of Computer Programs_

Ask a junior developer what skills they want to build and you will hear: algorithms, system design, a new framework, a new language. These are good answers. But there is one skill that improves every area of your work and almost nobody talks about it deliberately.

**Reading code.** Specifically, reading code you did not write, quickly, accurately, and without getting lost.

## Why It Is Underrated

### We Optimise for Writing

The entire mental model of "becoming a better developer" is skewed toward *output*. Build projects. Write more code. Ship things. This is not wrong, but it creates a blind spot.

In a real job, the ratio of reading to writing is enormous:

1. **Onboarding to a codebase**: You spend days or weeks reading before you write a single line.
2. **Code review**: Every PR you review is a reading task.
3. **Debugging**: Finding a bug is almost always a reading task before it is a fixing task.
4. **Using libraries**: Understanding what a dependency does means reading its source or tests.

If writing code is 20% of the job, reading code is 60%. The rest is meetings.

## What Good Code Reading Looks Like

### It Is a Skill, Not a Personality Trait

Some people seem to navigate unfamiliar codebases effortlessly. This feels like intuition but it is actually a set of learnable habits:

- **Start with the entry point**: Find `main`, `index`, `app.py` — wherever execution begins. Trace the first call chain before jumping around.
- **Read tests before source**: A good test suite tells you what the code is *supposed* to do, which makes the implementation much easier to follow.
- **Use your tools**: `grep`, `go to definition`, call hierarchies. Do not read linearly if you can jump directly to what matters.
- **Summarise in your own words**: After reading a function or module, write one sentence describing what it does. If you cannot, you do not understand it yet.

## Building the Habit

### Deliberate Practice

You can practice reading code the same way you practice writing it:

```
# Instead of building yet another todo app, try:
# 1. Clone an open source project you use
# 2. Pick one feature you understand from the outside
# 3. Find every file involved in that feature
# 4. Trace the execution path end to end
```

Do this for a few hours and you will learn more about software architecture than most tutorials teach.

## The Compound Effect

### Reading Makes You a Better Writer

This is the part that surprises people. Developers who read a lot of code write better code, for the same reason that writers who read a lot of books write better prose.

You absorb patterns:

- How to name things so the intent is obvious
- How to structure a module so the important parts are easy to find
- How to write a function that does not need a comment to explain itself

These things are hard to learn in the abstract. They click when you have seen them done well — and done badly — across many codebases.

## Conclusion

The next time you finish a feature and have an hour spare, resist the urge to start the next one. Instead, go read something: a library you depend on, an open source project you admire, a PR from a colleague. Read it slowly. Ask why decisions were made. Look for patterns you could steal.

It is the highest-leverage thing you can do for your long-term growth as an engineer, and almost nobody does it on purpose.
