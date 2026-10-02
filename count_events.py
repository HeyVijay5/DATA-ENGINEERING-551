import collections, json, pathlib

events = [json.loads(line) for line in
          pathlib.Path("/data/events.jsonl").read_text().splitlines() if line]
counts = collections.Counter((e["region"], e["event_type"]) for e in events)
for (region, event_type), n in sorted(counts.items()):
    print(f"{region:<12} {event_type:<20} {n}")
print(f"total {len(events)}")
