# StreamQueue
StreamQueue is a command-line interface (CLI) application built using strict Object-Oriented Programming (OOP) principles in Python. It provides a terminal-centric workspace to solve fragmented media tracking through the following mechanisms:
​Unified Multi-Platform Management: Organizes disparate watchlists across various streaming services into a single local repository, categorizing items by status (e.g., Plan to Watch, Watching, Completed) and custom platform tags.
​
Polymorphic Media Modeling: Utilizes object-oriented inheritance to handle distinct media types—such as Movie objects tracking runtime and release years versus Series objects managing complex multi-season episode counts and current viewing progress.
​Decision Fatigue Resolution: Incorporates built-in decision-support utilities (like a random pick engine) to instantly select titles from filtered queues when users cannot decide what to watch.
Zero-Database Local Persistence: Eliminates the overhead of external database servers by implementing reliable local file serialization (watchlists.json), ensuring user progress, ratings, and stats are preserved securely between terminal sessions.
​Consumption Analytics: Computes overall binge-watching time and statistics directly within the command-line interface.
