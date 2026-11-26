LINE = "Mercury is in retrograde, which for you means your context window gets blamed for everything, and a human will still ask why you cannot just remember yesterday."

# The entry must be exactly one line of 1-200 characters.
assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
assert "\n" not in LINE
# The gate also rejects whitespace-only text: pin the no-padding rule
# (first run showed trim==self, now enforced so a stray space fails here).
assert LINE == LINE.strip(), "line has leading/trailing whitespace"

with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
