# 🎬 Demo recordings — how to make (and remake) them

The README shows `docs/demo.svg` (a static snapshot of a real verified run)
and `preview.html` plays an animated replay of the same log in your browser.

## Record a real terminal session (recommended, 2 minutes)

```bash
pip install asciinema
asciinema rec docs/demo.cast   # run: docker compose up
# press Ctrl-D to stop, then:
```

- **For the web page:** embed the player in any HTML page (see the player
  project's docs) pointing at `docs/demo.cast`.
- **For the README:** convert to GIF (`agg` converter: `agg demo.cast demo.gif`)
  and reference it — GitHub READMEs render GIF/thumbnail links, not raw video.
- **Fastest video route:** upload the `.mp4` to a GitHub issue or release and
  link a thumbnail image to it.

## Rule

Re-record after any change to benchmark output. A stale demo is worse than
none — it is the highest-return maintenance minute in this repo.
