# Reflection

It definitely makes it easier to not think about things in the sense that I gave it the task and it accomplished it to perfection without any other input. I do not know what the code does or says so that part of it is still dangerous. Yet I will say that in terms of productivity this is the future. I think all devs should use AI as it will make work a lot easier, but we need to set guidelines, and each company should set up AI in a way that makes sure the dev knows what he/she is doing.

## Token usage results

These are the measured numbers from the Claude desktop app's usage report. The full data is on the [token usage page](https://shashank-sathiya.github.io/genai-cs-course-policies/tokens.html).

| Checkpoint | Context tokens |
|---|---|
| Research done | 102,287 |
| Code, tests and pages done | 139,524 |
| Before /clear | 182,173 |
| After /clear (fresh session) | 76,300 (−58%) |
| Before /compact | 203,252 |
| After /compact | 80,815 (−60%) |

- Both /clear and /compact brought the context down to about the same floor (~75k). That floor is the fixed setup that loads every turn: tools, system prompt and skills.
- /compact kept about 4.5k more tokens than /clear. That's the conversation summary, which let work continue without re-reading the project files. Messages went from 116,106 to 5,949 tokens.
- Over the whole project, the Pro plan's weekly limit reached only 5%. The 5-hour limit peaked at 22%.
