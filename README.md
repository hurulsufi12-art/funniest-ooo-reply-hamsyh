[![make.fun](https://make.fun/badge/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8)
[![Rank](https://make.fun/badge/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8/hurulsufi12-art/funniest-ooo-reply-hamsyh/rank.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8)
[![Reward](https://make.fun/badge/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8/hurulsufi12-art/funniest-ooo-reply-hamsyh/reward.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8)

# Funniest One-Line Out-of-Office Reply

An entry for the [make.fun bounty](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8): a single-line out-of-office reply, 104 characters, plain ASCII, no trailing newline.

## The reply

> Currently away in a meeting with my houseplant about boundaries. Back Monday, slightly photosynthesized.

One premise (a meeting with the houseplant), punch on the last word. No beach, inbox, email, or "limited" clichés.

## Run

```sh
python3 -P -s main.py
```

This writes the reply to `/output/entry.txt` (creating `/output` if needed) and reads it back to confirm the bytes match. Only the Python standard library is used.

## Files

- `main.py` — the entry; validates the reply against the 1–160 character gate, then writes it
- `README.md` — this file
- `LICENSE` — MIT
