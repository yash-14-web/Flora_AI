# Flora AI Workspace Rule: Design and Development Contract

Before starting any task in Flora AI:
1. Always reference and follow the project constitution in `MASTER_CONTEXT.md` and the 33 development rules in `DESIGN.md`.
2. Do not modify or redesign approved pages (like `landing.html`, `login.html`, `register.html`) when working on separate tasks.
3. Do not modify shared high-impact files (`base.html`, global theme styles, `settings.py`) unless strictly necessary and explicitly noted.
4. Maintain separation of concerns: Django Templates + CSS + JS for UI; Django views/APIs for backend; CNN model pipelines remain decoupled from web views.
5. Provide a short file-scope plan, execute minimal necessary changes, verify with tests/checks, and ensure zero regressions on existing pages.
