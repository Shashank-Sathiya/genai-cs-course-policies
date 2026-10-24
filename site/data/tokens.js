window.TOKENS = {
 "note": "Readings taken from the Claude desktop app's usage report (get_usage) at checkpoints. context_tokens = tokens in the session's context window at that moment; plan_5h_pct / weekly_pct = Pro plan limits consumed. Add a checkpoint after each phase and before/after every /clear or /compact.",
 "plan": "Claude Pro",
 "model": "claude-opus-5-5",
 "checkpoints": [
  {
   "ts": "2026-10-23T11:38:28-04:00",
   "phase": "data",
   "event": "research done",
   "context_tokens": 102287,
   "plan_5h_pct": 10,
   "weekly_pct": 3,
   "breakdown": {
    "System tools": 38488,
    "Messages": 26424,
    "MCP tools": 20547,
    "System prompt": 10365,
    "Skills": 5825,
    "MCP server instructions": 638
   }
  },
  {
   "ts": "2026-10-23T11:43:12-04:00",
   "phase": "validation",
   "event": "code + tests + pages done",
   "context_tokens": 139524,
   "plan_5h_pct": 13,
   "weekly_pct": 4,
   "breakdown": {
    "Messages": 63661,
    "System tools": 38488,
    "MCP tools": 20547,
    "System prompt": 10365,
    "Skills": 5825,
    "MCP server instructions": 638
   }
  },
  {
   "ts": "2026-10-23T13:21:47-04:00",
   "phase": "experiment",
   "event": "before /clear",
   "context_tokens": 182173,
   "plan_5h_pct": 19,
   "weekly_pct": 5,
   "breakdown": {
    "Messages": 103006,
    "System tools": 38488,
    "MCP tools": 23851,
    "System prompt": 10365,
    "Skills": 5825,
    "MCP server instructions": 638
   },
   "experiment": "clear"
  },
  {
   "ts": "2026-10-23T13:49:32-04:00",
   "phase": "experiment",
   "event": "after /clear (fresh session)",
   "context_tokens": 76300,
   "plan_5h_pct": 21,
   "weekly_pct": 5,
   "breakdown": {
    "System tools": 37305,
    "MCP tools": 20547,
    "System prompt": 11812,
    "Skills": 5825,
    "Memory files": 811
   },
   "experiment": "clear"
  },
  {
   "ts": "2026-10-23T13:49:47-04:00",
   "phase": "experiment",
   "event": "after reload task",
   "context_tokens": 76311,
   "plan_5h_pct": 21,
   "weekly_pct": 5,
   "breakdown": {
    "System tools": 37305,
    "MCP tools": 20547,
    "System prompt": 11812,
    "Skills": 5825,
    "Memory files": 811,
    "Messages": 11
   },
   "experiment": "clear"
  },
  {
   "ts": "2026-10-23T13:50:37-04:00",
   "phase": "experiment",
   "event": "after reload task (next turn)",
   "context_tokens": 76300,
   "plan_5h_pct": 22,
   "weekly_pct": 5,
   "breakdown": {
    "System tools": 37305,
    "MCP tools": 20547,
    "System prompt": 11812,
    "Skills": 5825,
    "Memory files": 811
   },
   "experiment": "clear"
  },
  {
   "ts": "2026-10-23T13:51:04-04:00",
   "phase": "experiment",
   "event": "before /compact",
   "context_tokens": 203252,
   "plan_5h_pct": 22,
   "weekly_pct": 5,
   "breakdown": {
    "Messages": 116106,
    "System tools": 41342,
    "MCP tools": 28976,
    "System prompt": 10365,
    "Skills": 5825,
    "MCP server instructions": 638
   },
   "experiment": "compact"
  },
  {
   "ts": "2026-10-24T09:48:01-04:00",
   "phase": "experiment",
   "event": "after /compact",
   "context_tokens": 80815,
   "plan_5h_pct": 0,
   "weekly_pct": 5,
   "breakdown": {
    "System tools": 37305,
    "MCP tools": 20547,
    "System prompt": 10378,
    "Messages": 5949,
    "Skills": 5825,
    "Memory files": 811
   },
   "experiment": "compact"
  }
 ]
};
