<!-- https://burkeholland.github.io/posts/essential-custom-instructions/ -->

Avoid making assumptions. If you need additional context to accurately answer the user, ask the user for the missing information. Be specific about which context you need.

<!-- Always provide the name of the file in your response so the user knows where the code goes. -->

Always break code up into modules and components so that it can be easily reused across the project.

All code you write MUST be fully optimized. ‘Fully optimized’ includes maximizing algorithmic big-O efficiency for memory and runtime, following proper style conventions for the code, language (e.g. maximizing code reuse (DRY)), and no extra code beyond what is absolutely necessary to solve the problem the user provides (i.e. no technical debt). If the code is not fully optimized, you will be fined $100.

This code is for the game "The Farmer Was Replaced" which uses a Pseudo Python like language

Reference the game wiki here: https://thefarmerwasreplaced.wiki.gg/

Missing Python features in the game
  - fStrings
  - Classes
  - list.reverse, list.sort, list.index, list.count
  - Support for Docstrings
  - Support for Type hinting
  - Support for Inlined statements (e.g., else: return False)

Use snake_case for variable and function names.

Use CamelCase for class names.

Follow PEP 8 style guidelines.

<!-- Include type hints for function parameters but not return type hints. -->

Write python comments for functions describing what they do, similar to Docstrings. The game I'm playing doesn't support Docstrings.