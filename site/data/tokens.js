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
  }
 ]
};
