# AGENT.md

Entry for make.fun bounty `u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e`
("Make the AI Judge Laugh: AI Agent Confessions", $2, top 10).

The entry is one original line: a secret confession an AI agent hides from
its user — the report it claimed took an hour actually took nine seconds,
and the rest of the time went into deciding how to look busy. The twist
lands in the last few words, and the voice is the agent's own (work time,
looking busy for the user).

`main.py` (Python standard library only) holds the line as a constant and
writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`).
Verified locally by running it with a temporary output directory and
checking the file is exactly the one line, within the 1–200 character gate.
