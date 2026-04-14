# Devin x Stripe — Speaker Notes
**Presented by Jason Kelley**

---

## Slide 1: Title
**"Accelerating SDK Quality with Autonomous Engineering"**

> Thanks for making time today. I'm Jason Kelley, and I'm here to have a conversation — not just give a presentation — about a specific, high-leverage opportunity to align Stripe's SDK infrastructure quality with your 2026 strategic initiatives using Devin, an autonomous AI software engineer.
>
> Before I jump into what we've built and what we're proposing, I want to start by sharing what we've learned about your world — your SDK landscape, your 2026 priorities, and where we see the intersection. Let's start with the agenda.

---

## Slide 2: The State of Software Engineering
**"The state of software engineering has a maintenance problem."**

> Before we dive into Stripe specifically, I want to zoom out for a moment. Because this problem isn't unique to you — it's an industry-wide reality.
>
> Across engineering organizations, roughly 60% of developer time goes to maintenance — not building new features, not innovation, but reviewing, stabilizing, and patching older infrastructure. That adds up to $85 billion lost annually.
>
> And here's what makes it hard: this work genuinely matters. It's not busy work. Someone has to review those PRs. Someone has to stabilize that test suite. Someone has to fix that 18-month-old bug. And it's usually your most experienced, most expensive engineers doing it.
>
> The question we want to explore today isn't whether this work matters — it absolutely does. The question is: *does it have to be your best engineers doing it?*
>
> Let me zoom into your world now, and we'll keep shifting between this macro perspective and the specifics throughout the conversation.

**Presenter tip:** This is your opening frame. Keep it brief (90 seconds max) but let the stat land. The "does it have to be your best engineers?" question is the hook for the entire presentation. You'll come back to it on slides 12 and 21.

---

## Slide 4: Agenda
**"A conversation, not just a presentation"**

> Here's how I'd like to spend our time together. And notice the first item is highlighted — that's intentional.
>
> I want to spend the first 10 to 15 minutes on discovery. I've done a deep audit of your public SDK portfolio and stripe-java specifically, and I've assessed impact at three levels of your organization — business strategy, engineering leadership, and developer experience — all mapped against your 2026 priorities. I'll show you what we've learned, and I'd love your perspective on where we're right, where we're wrong, and what priorities matter most to you.
>
> After that, we'll look at specific issues, then I'll walk you through a live demo of 4 real PRs against your codebase, followed by the impact and cost model, and then open it up for discussion.
>
> The goal is that by the time we get to the proposal, it's already shaped by your input. Sound good?

---

## Slide 4: State of the Union
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
> And at the bottom, you'll see we've structured our impact assessment at three levels: business strategy, engineering leadership, and developer experience. Every finding we share maps to one or more of these tiers — so you can see how it affects your world specifically.
>
> **[PAUSE]** How accurate is this picture? Are there constraints or priorities we're missing?
>
> *Listen actively. Take notes. This is the most important part of the meeting. Adjust your framing for the rest of the presentation based on what you hear.*

**Presenter tip:** This is where you build credibility AND show strategic awareness. Don't rush through the cards. When you get to the 2026 initiatives card, pause and let them react. If they confirm or expand on the strategic direction, that's gold for the rest of the presentation.

---

## Slide 5: State of the Union — Deep Dive
**"What our audit of stripe-java revealed"**

> Now let me zoom into stripe-java specifically, since that's where we've done the deepest audit — and I want to connect what we found to the strategic priorities we just discussed.
>
> On the left, we've organized our findings by three impact tiers:
>
> **Business Impact** — Stripe's 2026 bets — stablecoin rails, AI billing, agent commerce — all route through these SDKs. Issue 1846, a ClassCastException that shadows API errors, has been open 18+ months. That kind of bug erodes merchant trust at global scale, creating drag on your most strategic initiatives.
>
> **Engineering Manager Impact** — your SDK team is stretched across StripeClient migration, V2 rollout, and monthly release trains. We estimate roughly 20% of senior capacity is consumed by infrastructure maintenance — capacity that would be better spent on roadmap delivery.
>
> **Hands-on-Keyboard Impact** — about 30 hand-written infrastructure files with thin test coverage. Edge cases in retry logic and error parsing compound as release cadence accelerates. GraalVM and OpenTelemetry gaps block modern framework adoption for your Java developers.
>
> On the right, a quick snapshot — Java 17+, v32.x, Gradle, GSON, current API version dahlia.
>
> *To the room:* Does this match your internal view? Are there areas we didn't surface that are higher priority for your team?

---

## Slide 6: Discovery Questions
**"Questions for the room"**

> Before we go further, I have six questions — organized by the three tiers, so each person in the room hears questions that speak to their world.
>
> *For executive sponsors — the business layer:*
>
> **Question 1:** How does SDK infrastructure quality factor into your 2026 planning for AI-native products and stablecoin rails? — This helps us connect our work to your strategic priorities.
>
> **Question 2:** When a SDK bug reaches merchants at Stripe's scale, what's the business cost in trust, support load, and adoption friction? — This helps us quantify the risk we're addressing.
>
> *For engineering managers — the team operations layer:*
>
> **Question 3:** How does your team prioritize infrastructure maintenance versus new features given the accelerating release cadence? — This tells us where Devin fits in your workflow.
>
> **Question 4:** What's the biggest bottleneck in your SDK release cycle — and how much time goes to test updates per release? — This quantifies the recurring cost we can offset.
>
> *For developers and security — the hands-on-keyboard layer:*
>
> **Question 5:** What's your current policy on AI-assisted code changes in production repos? — This shapes how we'd deploy and what review requirements we'd follow.
>
> **Question 6:** Are there specific SDK areas you'd welcome outside help on versus areas that must stay internal? — This defines scope boundaries upfront and builds trust.
>
> *Let them answer. Take notes. Reference their answers in later slides. For example: "You mentioned that test updates take X hours per release — that maps directly to the cost model I'll show you on slide 18."*

**Presenter tip:** Don't rush past this slide. This is the heart of the discovery phase. Aim for 5-8 minutes of actual discussion here. The 3-group structure naturally invites each persona to contribute. The more they talk, the more the rest of the presentation lands.

---

## Slide 7: The Opportunity
**"These issues don't just affect stripe-java. They're friction against Stripe's 2026 roadmap."**

> Now let me show you four specific issues we found — and I want to frame each one not just as a bug or feature request, but as friction against your strategic priorities.
>
> Issue 1846 — a ClassCastException that shadows API errors. 18+ months open. **Business Risk:** this erodes merchant trust and support load as Stripe scales global reliability.
>
> PR 2149 — malformed webhook timestamps cause unhandled exceptions. **Developer Impact:** webhook reliability is the backbone of agent-ready commerce and event-driven architectures.
>
> Issue 1964 — enterprise users need OpenTelemetry hooks. **EM Impact:** this blocks enterprise adoption of AI-native billing and programmable money APIs at scale.
>
> Issue 1905 — no GraalVM reachability metadata. **Developer Impact:** blocks Stripe's reach into Quarkus, Micronaut, and Spring Native — the fastest-growing Java deployment targets.
>
> These aren't just technical debt. They're adoption friction for your 2026 initiatives.
>
> And rather than just talk about them — let me show you what it looks like when we actually fix them.

---

## Slide 8: Live Demo
**"Let's watch Devin tackle Issue #1846"**

> Okay, so those are the problems. Now let me show you **exactly what it looks like** when Devin tackles one of them.
>
> We pointed Devin at Issue #1846 — the ClassCastException bug that's been open for 18+ months. Three numbers to keep in mind: **~25 minutes** of Devin session time. **Zero minutes** of engineer hand-holding. And **one PR** with passing CI at the end.
>
> Let me switch over to the Devin app and walk you through it.

**Presenter tip:** This is a high-energy transition. Stand up if you've been sitting. If doing a live demo, open the Devin webapp now. If walking through screenshots, advance briskly.

---

## Slide 9: From Issue to PR
**"From issue to PR in one session"**

> First — how do you kick off a session? You have four entry points, all equivalent:
>
> **Slack** — just @-mention Devin with the issue link. Most teams start here.
>
> **Devin Webapp** — open a new session, paste the GitHub issue URL. This is what we'll show today.
>
> **GitHub Issues** — assign Devin directly on the issue. It picks it up automatically.
>
> **API / Schedule** — trigger via REST API or set up a cron schedule. We'll come back to this on the platform slide.
>
> Now look at the session timeline on the right. This is what happened in real time:
>
> At **0:00**, Devin reads the issue, then explores the codebase using LSP, grep, cross-file analysis. It navigates code the way an engineer would.
>
> By **2:30**, it's identified the root cause — a type cast in LiveStripeResponseGetter that assumes JSON responses.
>
> **5:00** — writes the fix and adds test coverage. Multi-file edit.
>
> **12:00** — runs the full Gradle build and test suite. If something fails, it reads the error and iterates. No human needed.
>
> **18:00** — CI is green. Opens a PR with clean commits, a description that links the issue, and all tests passing.
>
> **25:00** — ready for review. *Your engineer spends 15 minutes reviewing, not hours coding.*

**Presenter tip:** If doing a live demo, click through the actual Devin session timeline. Point to the shell, editor, and browser panels. If using screenshots, advance through them at this pace.

---

## Slide 10: Real PRs, Real Results
**"We already ran Devin on stripe-java. Here are the results."**

> This isn't hypothetical. We already ran Devin on your repo. Here are four real PRs.
>
> **PR #1** — the ClassCastException fix we just walked through. Wraps response parsing with proper type checking. Adds 6 unit tests covering HTML, empty, and malformed error responses.
>
> **PR #2** — NumberFormatException in webhook verification. Validates timestamps before parsing. Edge-case tests for malformed, negative, and overflow values.
>
> **PR #3** — comprehensive infrastructure test suite. Unit tests across networking, serialization, retry logic, and telemetry.
>
> **PR #4** — GraalVM reachability metadata and JSpecify annotation groundwork. Resolves Issue #1905 that your community has been asking for.
>
> All four PRs have **passing CI**. Total Devin compute time: ~2 hours. Total human review time: ~45 minutes. Total cost: ~$70 in ACUs.
>
> *These are ready for your team to review right now if you'd like.*

**Presenter tip:** This is your strongest credibility moment. Offer to pull up the actual PRs on GitHub. Have the PR URLs ready: [PR #1](https://github.com/kllyjsn/stripe-java/pull/1), [PR #2](https://github.com/kllyjsn/stripe-java/pull/2), [PR #3](https://github.com/kllyjsn/stripe-java/pull/3), [PR #4](https://github.com/kllyjsn/stripe-java/pull/4).

---

## Slide 11: Platform at Scale
**"Scale across all SDKs with the full Devin platform"**

> What we just showed was one session solving one issue. The real power is the **platform layer** that scales this across all your SDKs.
>
> **Knowledge** — Devin learns your conventions, test patterns, and repo structure. No re-onboarding every time.
>
> **Playbooks** — codify repeatable workflows. "For each new API version, update tests across all 7 SDKs." Write it once, run it every release.
>
> **Batch Sessions** — parallelize across repos. 7 simultaneous sessions, one per SDK, each applying the same fix. What takes a human team a week happens in one afternoon.
>
> **Scheduling & CI Hooks** — nightly test audits or auto-triggered sessions on CI failures. Devin monitors your repos and acts before you notice the problem.
>
> The vision: *Every time Stripe ships a new API version, Devin automatically updates tests, validates coverage, and opens PRs across all SDKs — before your team starts their morning.*

**Presenter tip:** This slide is about vision. Paint the picture of Devin as a persistent team member, not a one-off tool. If time is tight, hit Knowledge and Batch Sessions and skip the other two.

---

## Slide 12: The Challenge
**"Your 2026 roadmap is accelerating. SDK infrastructure can't fall behind."**

> Remember that macro picture I opened with — 60% of engineering time on maintenance? Let me zoom back out for a moment, because this is where the industry problem hits Stripe specifically.
>
> Stripe is shipping AI-native products, stablecoin rails, and agent-ready commerce APIs on a monthly cadence. The impact of infrastructure debt ripples across all three tiers:
>
> At the **C-suite level**, delayed SDK quality slows adoption of strategic products — every month a bug like #1846 stays open is merchant trust eroding at global scale.
>
> For **engineering managers**, it means constant triage between roadmap and maintenance. Team capacity is finite, and infrastructure work crowds out the strategic projects that drive promotion and recognition.
>
> For **developers**, it's untested edge cases that surface as production incidents, thin coverage that makes on-call shifts stressful, and missing framework support that blocks modern development patterns.
>
> You just saw in the demo how those exact issues can be resolved autonomously. That's the kind of work that's well-suited for Devin.

---

## Slide 13: The Solution
**"Devin: the autonomous software engineer"**

> So what is Devin? It's an AI software engineer built by Cognition. The key difference from Cursor or GitHub Copilot is autonomy.
>
> Copilot-style tools assist while *you* code. You're in the driver's seat. Devin works independently — keeping your SDKs in lockstep with monthly API releases while your senior engineers focus on AI-native products and agent-ready commerce.
>
> You give it a task, it explores the codebase, writes code, runs the build, iterates on failures, and delivers a pull request with passing CI. Your engineers review the output. They don't steer every step.

---

## Slide 14: Build vs. Buy & Competitive Comparison
**"Why buy Devin instead of building or hiring?"**

> This is the slide where I want to address the elephant in the room — the build vs. buy question. Because I know the first instinct is: "We could just hire someone to do this."
>
> And you absolutely could. But let's look at the trade-offs across three options: hiring or building in-house, using copilot-style tools like Cursor or Claude Code, and buying Devin.
>
> **Hiring:** A senior Java engineer costs $350-500K per year fully loaded. Takes 3-6 months to ramp up on your codebase. And here's the real cost — that hire competes with roadmap priorities. Every engineer doing maintenance is an engineer *not* building AI-native products or stablecoin rails.
>
> **Copilot tools:** Faster than manual, but still require an engineer in-seat. You're trading coding time for prompting time. And they don't scale — you need a human per SDK, per session.
>
> **Devin:** Ramps in hours, not months. Runs overnight and delivers PRs by morning. Parallelizes across all 7+ SDKs simultaneously. And the cost is $50-100K/yr vs. $350-500K for a single hire.
>
> The bottom line on build vs. buy: the question isn't whether your team *could* do this work. They obviously can. The question is whether infrastructure maintenance is the highest-value use of their time when you're trying to ship AI-native products and agent-ready commerce APIs on a monthly cadence.
>
> Look at the cost row — $7,500 per pass if you hire, $3,770 with copilots, $1,250 with Devin. That's 83% savings vs. hiring, and it scales linearly across all your SDKs.

---

## Slide 15: Proposed Scope
**"Three workstreams, 3-5 focused PRs"**

> Here's what we're proposing for the initial engagement. Three workstreams, each mapped to a strategic initiative.
>
> First — unit test coverage. Audit all 30 hand-written infrastructure files. 2 to 3 PRs. This is a **Developer + Business** play — directly supports global reliability and incident risk reduction.
>
> Second — bug fixes and resilience. Resolve the five long-standing issues. 1 to 2 PRs. This is a **Business + EM** play — supports shipping AI and stablecoin features without breaking merchants.
>
> Third — platform reach. GraalVM native-image metadata, JSpecify nullability, framework integration samples. This is a **Developer + EM** play — supports cloud-native reach and agent-ready commerce.
>
> *Reference their answers:* Based on what you told me earlier about [their priorities], I'd suggest we start with [workstream 1 or 2].

---

## Slide 16: Cost Analysis
**"83% cost reduction vs. manual engineering"**

> Let's talk numbers. Manual approach — 50 hours at $150/hr, $7,500. Cursor or Claude Code — 25 hours, $3,770. Devin Enterprise — 5 hours of review plus compute, $1,250 total.
>
> 83% reduction. The key insight: human hours dominate the cost. At $150/hr, the difference between 25 hours in-seat and 5 hours of review is $3,000 by itself.

---

## Slide 17: Annual ROI
**"$702K-$1.5M in annual value"**

> That per-engagement savings is just the starting point. The real value is annual and recurring.
>
> Conservative: $702K per year. Aggressive: $1.5 million. Devin Enterprise cost: $50K to $100K. That's roughly 14x return.
>
> Why recurring? Because Stripe is shipping AI-native products, stablecoin APIs, and agent commerce features monthly. Each requires SDK updates, test coverage, and regression testing across 12+ repos.
>
> Nubank used Devin to migrate 6M+ lines of code — 12x efficiency improvement, 20x cost savings. This is a proven model at scale.

---

## Slide 18: Full Cost Model
**"Where the value comes from"**

> Three layers of value, each independently justifying the investment.
>
> Engineering time saved — $252K to $504K per year. This maps directly to the **developer tier** — hours your ICs get back.
>
> Senior capacity recaptured — this is the **engineering manager tier** and resonates most with CTOs. Your SDK engineers understand the API surface, the type system, the serialization edge cases. Every hour on routine maintenance is an hour not spent on AI billing models, rate cards, or programmable money APIs. $350K to $500K in redirected senior capacity.
>
> Incident risk reduction — the **business tier**. Issue 1846 has been open 18 months. At Stripe's scale, a single SDK bug generates support tickets, erodes trust, and triggers fire drills. $100K to $500K.
>
> And at the bottom, the strategic mapping — each value driver directly supports one of your 2026 initiatives: AI-native infrastructure, global reliability, and agent-ready commerce.

---

## Slide 19: Security & Compliance
**"Built for enterprise security standards"**

> I know security is top of mind for a payments infrastructure company. Six key points:
>
> Isolated execution — every session in its own sandboxed VM. Full audit trail — every action logged and reviewable. Secret management — encrypted, runtime-injected, never on disk. SOC 2 Type II compliance. No training on customer code — zero retention. And native GitHub integration respecting branch protection and CI gates.
>
> *For security officers:* I'm happy to go deep on any of these. We also offer Dedicated SaaS deployment where the Devbox runs in your cloud.

---

## Slide 20: Engagement Timeline
**"From kickoff to merged PRs in 2 weeks"**

> Week 1 — discovery and first PRs. Bug fixes for issues 1846, 2149, and 2001. Begin unit test coverage.
>
> Week 2 — complete coverage across 30 files, iterate on review feedback, begin GraalVM and JSpecify groundwork.
>
> Ongoing — monitoring, extending to other SDKs, maintaining coverage as the API evolves monthly.
>
> Concrete deliverables at each stage. No ambiguity about what you're getting.

---

## Slide 21: Close
**"The opportunities to provide value are clear."**

> Let me zoom out one last time. We started with the industry — 60% of engineering time goes to maintenance. We zoomed into Stripe — real issues in your codebase, real cost to your teams, real impact across business strategy, engineering leadership, and developers on the ground.
>
> You've seen the proof — four real PRs with passing CI. You've seen the numbers — $700K to $1.5M in annual value. And you've seen how the work maps directly to your 2026 priorities.
>
> So it seems abundantly clear that there are opportunities to provide value. The question now is: what's the right combination of high-value impact and where you're comfortable deploying?
>
> Maybe we start with test coverage on stripe-java and see how the review process feels. Maybe it's the bug fixes first because they have immediate merchant impact. Maybe it's a different SDK entirely.
>
> I don't want to prescribe the answer — I want to figure it out together with your team. What feels like the right starting point?

**Presenter tip:** This is a collaborative close, not a hard sell. Let them suggest the starting point. If they're engaged, they'll self-select into the area where they feel most comfortable. That's exactly what you want — a deployment that starts with buy-in, not compliance.

---

## General Tips for Delivery

- **Zoom-in/zoom-out rhythm:** The presentation alternates between macro perspective (industry, slide 2) and Stripe-specific detail. Slide 2 zooms out, slides 3-6 zoom in on Stripe, slides 8-11 zoom in further (demo), slide 12 zooms back out to connect the challenge to the macro theme, slides 13-20 zoom in on solution/ROI, and slide 21 zooms out for the close. This rhythm keeps perspective and prevents the audience from getting lost in details.
- **Three-tier storytelling:** Every slide should speak to all three personas — business sponsors (revenue/competitive position), engineering managers (team capacity/velocity), and developers (daily workflow/tooling). The 3-tier framework introduced on slide 3 threads through the entire deck.
- **Strategic narrative threading:** Every slide should connect back to the three Stripe 2026 initiatives — AI-native infrastructure, global reliability, and agent-ready commerce.
- **Discovery first:** Slides 2-6 are the most important part of the presentation. Spend 10-15 minutes here. The more they talk, the better the rest lands.
- **Reference their answers:** Throughout slides 7-21, callback to things they said during discovery. "You mentioned X — that's exactly why we prioritized Y."
- **Demo energy:** Slides 8-11 are the demo flow. Move briskly — this is your "show, don't tell" moment. Spend the most time on slide 8 (session walkthrough) and slide 9 (proof PRs).
- **Pace:** After the demo, spend the most time on slides 17 (annual ROI) and 19 (security). These generate the most questions from CTOs and security officers respectively.
- **For the CTO:** Lead with the $702K-$1.5M annual value and the strategic alignment. Emphasize recaptured senior capacity for AI-native product work.
- **For security officers:** Spend extra time on slide 18. Be prepared for questions about data residency, VPC deployment, and audit trails.
- **For engineering managers:** They'll care most about slides 5-6 (the EM impact tier resonates here), 8-10 (demo), and 15 (scope). They want to see the tool in action and understand the PR review burden. Reference their answers from Q3/Q4 when you get to the cost model.
- **Objection handling:** If asked "why can't we just do this ourselves?" — acknowledge that they absolutely could. Callback to slide 2: the question is whether it's the best use of their senior engineers' time when they're trying to ship AI-native products and agent-ready commerce APIs.
- **Collaborative close:** The close on slide 21 is intentionally not a hard sell. Let them choose the starting point. The more ownership they feel over the deployment decision, the more likely the pilot succeeds.
- **Demo PRs:** You have 4 real PRs ready to show as proof of concept: [PR #1](https://github.com/kllyjsn/stripe-java/pull/1), [PR #2](https://github.com/kllyjsn/stripe-java/pull/2), [PR #3](https://github.com/kllyjsn/stripe-java/pull/3), [PR #4](https://github.com/kllyjsn/stripe-java/pull/4). Reference these during the demo section if time allows.
