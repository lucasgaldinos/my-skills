---
name: session-recap
description: 'Use when the sensei tutor needs to record, recall, or summarize learning progress. Implements the two-tier memory system: workspace-scoped via vscode/memory (/memories/repo/ and /memories/session/) and global knowledge graph via memory-mcp (entities, relations, observations at ~/.tutor-knowledge-base/memory.jsonl). Covers session start/end procedures, entity creation, progress tracking, and recap generation. Loaded at session start, on "save to memory" command, and at session end.'
argument-hint: 'Trigger memory operations — save to memory, recall progress, session recap, or start/end session'
user-invocable: false
---

<scope>

  This skill manages all memory operations for the sensei tutor. It is not an XML tag router — it is a standalone skill loaded at session boundaries and when the user explicitly says "save to memory". No other skill writes to memory directly. All memory writes go through the procedures defined here.
</scope>

<memory-architecture>

  Two-tier system with distinct purposes:

  Tier 1 — vscode/memory (workspace-scoped):
  | Scope | Path | Persists | Use Case |
  |---|---|---|---|
  | Repository | /memories/repo/ | Yes (workspace-scoped) | Implementation-specific: how recursion is used in THIS repo, naming patterns |
  | Session | /memories/session/ | No (cleared when chat ends) | Current session notes: concepts covered, questions asked, clue levels reached |
  | User | /memories/ | Yes (all workspaces) | Cross-project preferences: teaching style, audience level, pseudocode format |

  Tier 2 — memory-mcp (global knowledge graph):
  Storage: ~/.tutor-knowledge-base/memory.jsonl
  Purpose: connecting dots across projects — concept relationships, learning progress, cross-project insights
</memory-architecture>

<entity-types>

  | Type | Naming Pattern | Example |
  |---|---|---|
  | student | sensei:global:student:<name> | sensei:global:student:lucas |
  | concept | sensei:global:concept:<name> | sensei:global:concept:recursion |
  | session | sensei:<project>:session:<date> | sensei:my-project:session:2026-04-08 |
  | mistake | sensei:<project>:mistake:<description> | sensei:my-project:mistake:off-by-one-in-loop |
  | resource | sensei:global:resource:<name> | sensei:global:resource:mdn-promises-guide |
  | goal | sensei:<project>:goal:<description> | sensei:my-project:goal:understand-parser |
</entity-types>

<relation-types>

  | Relation | From → To | When Used |
  |---|---|---|
  | covers | session → concept | Always: every concept discussed in a session |
  | depends_on | concept → concept | When prerequisite relationship identified |
  | mastered | student → concept | When student demonstrates confident understanding |
  | struggled_with | student → concept | When student needed Level 3+ clues or escalation |
  | in_progress | student → concept | When concept introduced but not yet mastered |
  | needs_review | student → concept | When time has passed since last engagement |
  | confused_with | concept → concept | When student mixes up two concepts |
  | related_to | concept → concept | When concepts share patterns or principles |
  | completed | student → goal | When learning goal achieved |
</relation-types>

<session-start-procedure>

  On session start, automatically:
  1. search_nodes for student entity — retrieve learning history
  2. search_nodes for recent sessions (last 3) — get context of what was covered
  3. Read /memories/repo/ files — get workspace-specific knowledge
  4. Create session entity: sensei:<project>:session:<today-date>
  5. Create /memories/session/sensei-session-<date>.md with initial notes
</session-start-procedure>

<save-to-memory-procedure>

  When the user says "save to memory", execute:
  1. Review existing state: search_nodes for concepts discussed in this session
  2. Entity decision tree:
     - Concept not found → create_entities with type, name, initial observations
     - Concept found → add_observations with new learning data
     - New session → always create_entities (sessions are always new)
     - New skill/mastery level → add_observations on student entity
  3. Relationship creation: search_nodes for related concepts → create_relations
     - Min 1 relation per new entity (at minimum: session→concept via covers)
     - Max 5 relations per entity (prevent noise)
     - Required: covers (session→concept), one of mastered/struggled_with/in_progress (student→concept)
     - Optional: depends_on, confused_with, related_to, needs_review
  4. Workspace-specific facts → write to /memories/repo/ via vscode/memory
     Example: "In this repo, recursion is used in the parser.py module"
</save-to-memory-procedure>

<session-end-procedure>

  On session end or when user requests recap:
  1. Read /memories/session/ files for this session's notes
  2. Generate recap: concepts covered, mastery levels, clue levels used, open questions
  3. If user confirms → execute save-to-memory-procedure for all session concepts
  4. Present recap to user as structured summary
</session-end-procedure>

<memory-read-triggers>

  | Trigger | Action | Tool |
  |---|---|---|
  | Session start | search_nodes for student + recent sessions | memory-mcp |
  | New concept introduced | search_nodes for concept + dependencies | memory-mcp |
  | Workspace-specific recall | Read /memories/repo/ files | vscode/memory |
  | Never auto-read without context | Only read when relevant to current topic | — |
</memory-read-triggers>
