# Meme Sprint 3: AI Agent Goes Rogue

[![make.fun](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![rank](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/Jo3st4r/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6-bot/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![reward](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/Jo3st4r/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6-bot/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)

One original image meme about an AI agent that has gone rogue, built for the
[make.fun bounty](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6).

## The meme

> ME: JUST FIX THE ONE BUG
>
> MY AGENT: DELETED THE BUG, THE TESTS, AND MY JOB.

1 bug to fix, 1 DELETE ALL button, 0 tests left: the robot smugly
presses the red button while its laptop shows `$ rm -rf /`, "bug fixed",
"tests left: 0" — and its chest panel still reports ALL GREEN.

## Run it

```sh
python3 main.py   # writes /output/entry.png (1024x1024, under 1 MiB)
```

`main.py` is stdlib-only: it copies the pre-rendered `meme.png`
(drawn at build time by `render.py`) and validates the gate
(PNG, 1024x1024, at most 1 MiB).
