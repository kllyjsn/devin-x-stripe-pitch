# Devin x Stripe — Speaker Notes
**Presented by Jason Kelley**

---

## Slide 1: Title
**"Accelerating SDK Quality with Autonomous Engineering"**

> Thanks for making time today. I'm Jason Kelley, and I'm here to have a conversation — not just give a presentation — about a specific, high-leverage opportunity to align Stripe's SDK infrastructure quality with your 2026 strategic initiatives using Devin, an autonomous AI software engineer.
>
> Before I jump into what we've built and what we're proposing, I want to start by sharing what we've learned about your world — your SDK landscape, your 2026 priorities, and where we see the intersection. Let's start with the agenda.

---

## Slide 2: Agenda
**"A conversation, not just a presentation"**

> Here's how I'd like to spend our time together. And notice the first item is highlighted — that's intentional.
>
> I want to spend the first 10 to 15 minutes on discovery. I've done a deep audit of your public SDK portfolio and stripe-java specifically, and I've mapped our findings against Stripe's 2026 strategic priorities — AI-native infrastructure, agent-ready commerce, global reliability. I'll show you what we've learned, and I'd love your perspective on where we're right, where we're wrong, and what priorities matter most to you.
>
> After that, we'll look at specific issues, then I'll walk you through a live demo of 4 real PRs against your codebase, followed by the impact and cost model, and then open it up for discussion.
>
> The goal is that by the time we get to the proposal, it's already shaped by your input. Sound good?

---

## Slide 3: State of the Union
**"Here's what we know about Stripe's SDK landscape"**

> So let me show you what we've learned. This is our State of the Union on Stripe's SDK ecosystem, mapped against your strategic direction.
>
> *Point to each card as you go:*
>
> You maintain 7+ server SDKs — Java, Node, Python, Ruby, Go, .NET, PHP — each with its own infrastructure layer, test suite, and release process.
>
> On top of that, 5+ mobile and client SDKs — Android, iOS, React Native, Terminal, Stripe.js — often with separate teams.
>
> You're on a roughly monthly API release cadence — we've tracked the naming convention: acacia, basil, clover, and most recently dahlia. Each release requires coordinated SDK updates across all repos.
>
> Based on commit history, we estimate 5 to 10 engineers focused on SDK work — we've seen names like jar-stripe, xavdid-stripe, mbroshi-stripe, richardm-stripe.
>
> You're on v32.x of the Java SDK with the new StripeClient pattern, CI running JDK 21 through 24, and continuous monthly upgrades tracking Billing, Tax, and V2 resources. That's a fast-moving target.
>
> And here's the strategic context — your 2026 initiatives around AI-native infrastructure, agent-ready commerce, stablecoin rails, and global reliability all depend on SDK quality. If the SDKs can't keep pace, those initiatives hit friction at the developer adoption layer.
>
> **[PAUSE]** How accurate is this picture? Are there constraints or priorities we're missing?
>
> *Listen actively. Take notes. This is the most important part of the meeting. Adjust your framing for the rest of the presentation based on what you hear.*

**Presenter tip:** This is where you build credibility AND show strategic awareness. Don't rush through the cards. When you get to the 2026 initiatives card, pause and let them react. If they confirm or expand on the strategic direction, that's gold for the rest of the presentation.

---

## Slide 4: State of the Union — Deep Dive
**"What our audit of stripe-java revealed"**

> Now let me zoom into stripe-java specifically, since that's where we've done the deepest audit — and I want to connect what we found to the strategic priorities we just discussed.
>
> On the left, three themes we identified:
>
> Infrastructure quality debt — 24 open issues affecting production error handling. Issue 1846, a ClassCastException that shadows API errors, has been open 18+ months. That kind of bug erodes merchant trust — which is a direct risk to your global reliability goals.
>
> Test coverage gaps — about 30 hand-written infrastructure files with thin unit coverage. As Stripe ships AI billing, stablecoin rails, and agent APIs on a monthly cadence, untested edge cases in retry logic and error parsing become compounding risk.
>
> And roadmap-blocking feature requests — GraalVM native image support blocks your reach into cloud-native ecosystems like Quarkus and Micronaut. OpenTelemetry hooks block enterprise observability. These gate Stripe's ability to reach modern Java deployment targets.
>
> On the right, a quick snapshot — Java 17+, v32.x, Gradle, GSON, current API version dahlia.
>
> *To the room:* Does this match your internal view? Are there areas we didn't surface that are higher priority for your team?

---

## Slide 5: Discovery Questions
**"Questions for the room"**

> Before we go further, I have six questions — three for engineering leadership and three around security and process. These will help me tailor the rest of the conversation to what actually matters to you.
>
> *For engineering leadership:*
>
> **Question 1:** How does your team currently prioritize infrastructure maintenance versus new features? — Specifically, as you're shipping AI-native products and agent-ready commerce APIs, how do you balance that against SDK infrastructure debt?
>
> **Question 2:** What's the biggest bottleneck in your SDK release cycle today? — This tells us where automation would have the highest leverage.
>
> **Question 3:** How much time per API version release goes to test updates and regression testing? — This helps us quantify the recurring cost we can offset.
>
> *For security and process:*
>
> **Question 4:** What's your current policy on AI-assisted code changes in production repos? — This shapes how we'd deploy and what review requirements we'd follow.
>
> **Question 5:** Do external contributors go through the same CI and review gates as internal PRs? — This ensures Devin integrates with your existing workflow rather than creating a parallel process.
>
> **Question 6:** Are there specific SDK areas you'd welcome outside help on versus areas that must stay internal? — This defines scope boundaries upfront and builds trust.
>
> *Let them answer. Take notes. Reference their answers in later slides. For example: "You mentioned that test updates take X hours per release — that maps directly to the cost model I'll show you on slide 14."*

**Presenter tip:** Don't rush past this slide. This is the heart of the discovery phase. Aim for 5-8 minutes of actual discussion here. The more they talk, the more the rest of the presentation lands.

---

## Slide 6: The Opportunity
**"These issues don't just affect stripe-java. They're friction against Stripe's 2026 roadmap."**

> Now let me show you four specific issues we found — and I want to frame each one not just as a bug or feature request, but as friction against your strategic priorities.
>
> Issue 1846 — a ClassCastException that shadows API errors. 18+ months open. **Impact:** this erodes merchant trust as Stripe scales global reliability.
>
> PR 2149 — malformed webhook timestamps cause unhandled exceptions. **Impact:** webhook reliability is critical for agent-ready commerce and event-driven architectures.
>
> Issue 1964 — enterprise users need OpenTelemetry hooks. **Impact:** this blocks adoption of AI-native billing and programmable money APIs by large Java platforms.
>
> Issue 1905 — no GraalVM reachability metadata. **Impact:** blocks Stripe's reach into Quarkus, Micronaut, and Spring Native — the fastest-growing Java deployment targets.
>
> These aren't just technical debt. They're adoption friction for your 2026 initiatives.
>
> And rather than just talk about them — let me show you what it looks like when we actually fix them.

---

## Slide 7: Live Demo
**"Let's see Devin in action on your own codebase"**

> So let me show you exactly what this looks like in practice — on your own codebase. I've prepared 4 real pull requests against stripe-java, each demonstrating a different mode of human-AI collaboration.
>
> *Point to each PR card:*
>
> **PR #1 — Bug Fix.** The webhook timestamp parsing issue I just showed you. Devin found the bug, wrote a defensive fix with try-catch, added 3 new test cases, and had a passing PR in under 3 minutes. This is the "speed" story.
>
> **PR #2 — Cross-File Fix.** The ClassCastException error handling issue. This one required Devin to trace the error path across multiple files, understand the GSON deserialization flow, and add proper type checking. 4 new tests. This is the "depth" story.
>
> **PR #3 — Test Coverage.** RequestTelemetry had zero unit tests. Devin audited the class, identified 11 distinct behaviors to test — header formatting, thread safety, max queue size, metrics tracking — and wrote a complete test suite from scratch. This is the "scale" story.
>
> **PR #4 — Feature Build.** I designed the API for public version constants, and Devin implemented the entire class plus 4 tests. Human judgment on the interface, AI execution on the implementation. This is the "collaboration" story.
>
> *[Open each PR in a browser tab and walk through the code changes. Spend ~2-3 min per PR.]*
>
> **Links:**
> - [PR #1: Webhook timestamp fix](https://github.com/kllyjsn/stripe-java/pull/1)
> - [PR #2: ClassCastException fix](https://github.com/kllyjsn/stripe-java/pull/2)
> - [PR #3: RequestTelemetry tests](https://github.com/kllyjsn/stripe-java/pull/3)
> - [PR #4: ApiVersion constants](https://github.com/kllyjsn/stripe-java/pull/4)

**Presenter tip:** This is the proof point — the moment belief shifts from "interesting concept" to "this actually works." Have the PR tabs pre-loaded in your browser before the meeting. Show the actual diffs — the audience wants to see real code, not slides. Spend the most time on PR #2 (cross-file analysis) and PR #3 (scale) — these are the hardest to replicate with copilot-style tools. After walking through the PRs, transition with: "Now that you've seen what Devin can do, let me put that in the context of your 2026 roadmap."

---

## Slide 8: The Challenge
**"Your 2026 roadmap is accelerating. SDK infrastructure can't fall behind."**

> Here's the root cause — and this isn't a criticism, it's a resourcing reality in the context of your accelerating roadmap.
>
> Stripe is shipping AI-native products, stablecoin rails, and agent-ready commerce APIs on a monthly cadence. Each release requires SDK updates across Java, Node, Python, Ruby, Go, .NET, and PHP.
>
> Your SDK team is focused on the StripeClient migration, V2 API rollout, and monthly version trains. That's the right priority. But infrastructure quality — the hand-written 15% where real bugs like #1846 live — accumulates in the backlog.
>
> You just saw in the demo how those exact issues can be resolved autonomously. That's the kind of work that's well-suited for Devin.

---

## Slide 9: The Solution
**"Devin: the autonomous software engineer"**

> So what is Devin? It's an AI software engineer built by Cognition. The key difference from Cursor or GitHub Copilot is autonomy.
>
> Copilot-style tools assist while *you* code. You're in the driver's seat. Devin works independently — keeping your SDKs in lockstep with monthly API releases while your senior engineers focus on AI-native products and agent-ready commerce.
>
> You give it a task, it explores the codebase, writes code, runs the build, iterates on failures, and delivers a pull request with passing CI. Your engineers review the output. They don't steer every step.

---

## Slide 10: Competitive Comparison
**"Why Devin, not Cursor or Claude Code?"**

> I want to be direct about this comparison because I know you're evaluating multiple tools.
>
> The six differentiators that matter most: autonomy, codebase exploration, build and CI iteration, multi-file refactoring, async execution, and pattern consistency.
>
> The bottom line — with Cursor, you trade coding time for prompting time. You're still in the seat. With Devin, you trade it for review time, which is 5 to 10x less.
>
> For a team that's already stretched between shipping new AI-native features and maintaining SDK infrastructure, async execution is the real differentiator. Devin runs in the background while your team does other work.

---

## Slide 11: Proposed Scope
**"Three workstreams, 3-5 focused PRs"**

> Here's what we're proposing for the initial engagement. Three workstreams, each mapped to a strategic initiative.
>
> First — unit test coverage. Audit all 30 hand-written infrastructure files. 2 to 3 PRs. This directly supports **global reliability and incident risk reduction**.
>
> Second — bug fixes and resilience. Resolve the five long-standing issues. 1 to 2 PRs. This supports **shipping AI and stablecoin features without breaking merchants**.
>
> Third — platform reach. GraalVM native-image metadata, JSpecify nullability, framework integration samples. This supports **cloud-native reach and agent-ready commerce**.
>
> *Reference their answers:* Based on what you told me earlier about [their priorities], I'd suggest we start with [workstream 1 or 2].

---

## Slide 12: Cost Analysis
**"83% cost reduction vs. manual engineering"**

> Let's talk numbers. Manual approach — 50 hours at $150/hr, $7,500. Cursor or Claude Code — 25 hours, $3,770. Devin Enterprise — 5 hours of review plus compute, $1,250 total.
>
> 83% reduction. The key insight: human hours dominate the cost. At $150/hr, the difference between 25 hours in-seat and 5 hours of review is $3,000 by itself.

---

## Slide 13: Annual ROI
**"$702K-$1.5M in annual value"**

> That per-engagement savings is just the starting point. The real value is annual and recurring.
>
> Conservative: $702K per year. Aggressive: $1.5 million. Devin Enterprise cost: $50K to $100K. That's roughly 14x return.
>
> Why recurring? Because Stripe is shipping AI-native products, stablecoin APIs, and agent commerce features monthly. Each requires SDK updates, test coverage, and regression testing across 12+ repos.
>
> Nubank used Devin to migrate 6M+ lines of code — 12x efficiency improvement, 20x cost savings. This is a proven model at scale.

---

## Slide 14: Full Cost Model
**"Where the value comes from"**

> Three layers of value, each independently justifying the investment.
>
> Engineering time saved — $252K to $504K per year.
>
> Senior capacity recaptured — this resonates most with CTOs. Your SDK engineers understand the API surface, the type system, the serialization edge cases. Every hour on routine maintenance is an hour not spent on AI billing models, rate cards, or programmable money APIs. $350K to $500K in redirected senior capacity.
>
> Incident risk reduction — issue 1846 has been open 18 months. At Stripe's scale, a single SDK bug generates support tickets, erodes trust, and triggers fire drills. $100K to $500K.
>
> And at the bottom, the strategic mapping — each value driver directly supports one of your 2026 initiatives: AI-native infrastructure, global reliability, and agent-ready commerce.

---

## Slide 15: Security & Compliance
**"Built for enterprise security standards"**

> I know security is top of mind for a payments infrastructure company. Six key points:
>
> Isolated execution — every session in its own sandboxed VM. Full audit trail — every action logged and reviewable. Secret management — encrypted, runtime-injected, never on disk. SOC 2 Type II compliance. No training on customer code — zero retention. And native GitHub integration respecting branch protection and CI gates.
>
> *For security officers:* I'm happy to go deep on any of these. We also offer Dedicated SaaS deployment where the Devbox runs in your cloud.

---

## Slide 16: Engagement Timeline
**"From kickoff to merged PRs in 2 weeks"**

> Week 1 — discovery and first PRs. Bug fixes for issues 1846, 2149, and 2001. Begin unit test coverage.
>
> Week 2 — complete coverage across 30 files, iterate on review feedback, begin GraalVM and JSpecify groundwork.
>
> Ongoing — monitoring, extending to other SDKs, maintaining coverage as the API evolves monthly.
>
> Concrete deliverables at each stage. No ambiguity about what you're getting.

---

## Slide 17: Call to Action
**"Let's ship better SDKs, faster."**

> Start with stripe-java. Prove the model. Scale across the portfolio. Your engineers focus on what matters — AI-native products, agent-ready commerce, stablecoin rails — while Devin handles the infrastructure quality layer.
>
> I'd love to either start a pilot or schedule a deeper technical demo where we walk through a live Devin session on your codebase. What works best for your team?
>
> *Reference their earlier answers:* Based on what you shared about [priority/bottleneck], I think the fastest way to prove value is [specific workstream]. We could have the first PR up within days.

---

## General Tips for Delivery

- **Strategic narrative threading:** Every slide should connect back to the three Stripe 2026 initiatives — AI-native infrastructure, global reliability, and agent-ready commerce.
- **Discovery first:** Slides 2-5 are the most important part of the presentation. Spend 10-15 minutes here. The more they talk, the better the rest lands.
- **Demo is the proof point:** Slide 7 is where belief shifts from "interesting concept" to "this actually works." Have PR tabs pre-loaded and walk through real code diffs. Spend 10-12 minutes here.
- **Reference their answers:** Throughout slides 8-17, callback to things they said during discovery. "You mentioned X — that's exactly why we prioritized Y."
- **Pace:** After discovery, spend the most time on slides 13 (annual ROI) and 15 (security). These generate the most questions from CTOs and security officers respectively.
- **For the CTO:** Lead with the $702K-$1.5M annual value and the strategic alignment. Emphasize recaptured senior capacity for AI-native product work.
- **For security officers:** Spend extra time on slide 15. Be prepared for questions about data residency, VPC deployment, and audit trails.
- **For engineering managers:** They'll care most about slides 6-7 (the issues + demo), 10 (comparison), and 11 (scope). They want to know the issues are real, the approach is sound, and the PRs won't create review burden.
- **Objection handling:** If asked "why can't we just do this ourselves?" — acknowledge that they absolutely could. The question is whether it's the best use of their senior engineers' time when they're trying to ship AI-native products and agent-ready commerce APIs. Then point to the demo: "You saw 4 PRs that would've taken a senior engineer 2-3 days. Devin did it while we were preparing this meeting."
- **Demo PRs:** You have 4 real PRs ready to show as proof of concept: [PR #1](https://github.com/kllyjsn/stripe-java/pull/1), [PR #2](https://github.com/kllyjsn/stripe-java/pull/2), [PR #3](https://github.com/kllyjsn/stripe-java/pull/3), [PR #4](https://github.com/kllyjsn/stripe-java/pull/4). These are shown during the live demo on slide 7.
