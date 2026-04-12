# Devin x Stripe — Speaker Notes
**Presented by Jason Kelley**

---

## Slide 1: Title
**"Accelerating SDK Quality with Autonomous Engineering"**

> Thanks for making time today. I'm Jason Kelley, and I'm here to talk about a specific, high-leverage opportunity to improve the quality of Stripe's SDK infrastructure — starting with stripe-java — using Devin, an autonomous AI software engineer.
>
> This isn't a general AI pitch. I've done a deep audit of the stripe-java codebase, identified real open issues and coverage gaps, and I want to walk you through exactly what we can fix, how fast, and what it saves you.

---

## Slide 2: The Opportunity
**"stripe-java powers millions of businesses. Its infrastructure code deserves deeper coverage."**

> Let me start with what I found. These are four real, open issues in stripe-java right now.
>
> Issue 1846 — a ClassCastException that shadows API errors. When Stripe's API returns a non-JSON error, your users don't get a StripeException — they get an uninformative ClassCastException. This has been open since August 2024. That's almost two years.
>
> PR 2149 — malformed webhook timestamps cause an unhandled NumberFormatException. A community contributor submitted a fix in January, but it's still sitting open.
>
> Issue 1964 — enterprise users are asking for OpenTelemetry and Micrometer hooks. Right now the workaround is wrapping the entire library, which is fragile and hard to maintain.
>
> And issue 1905 — GraalVM native image support. Five upvotes, increasingly critical as Quarkus, Micronaut, and Spring Native adoption grows.
>
> These aren't obscure edge cases. They affect production error handling and developer experience for your largest customers.

---

## Slide 3: The Challenge
**"SDK engineers are stretched between generated code and infrastructure quality"**

> Here's the root cause. stripe-java is primarily auto-generated from your OpenAPI spec — which is the right architecture. But the hand-written infrastructure layer — networking, serialization, error handling, webhook verification, retry logic — that's where the real bugs live.
>
> Your SDK team is small. Based on the PR authors I see — jar-stripe, xavdid-stripe, mbroshi-stripe — you have maybe 5 to 10 engineers covering all the SDKs. They're focused on shipping new API versions, maintaining the code generator, and supporting the V2 API migration.
>
> Infrastructure quality improvements — better test coverage, fixing long-tail bugs — those accumulate in the backlog. That's not a criticism. That's a resourcing reality. And it's exactly the kind of work that's well-suited for automation.

---

## Slide 4: The Solution
**"Devin: the autonomous software engineer"**

> So what is Devin? Devin is an AI software engineer built by Cognition. The key difference from tools like Cursor or GitHub Copilot is autonomy.
>
> Copilot-style tools assist while *you* code. You're in the driver's seat, pointing the tool at files, prompting it, reviewing suggestions line by line.
>
> Devin works independently. You give it a task — "add unit test coverage for the webhook verification module" — and it explores the codebase on its own using LSP, grep, and cross-file analysis. It reads existing tests to learn your conventions. It writes code, runs the build, iterates on failures, and delivers a pull request with passing CI.
>
> Your engineers review the output. They don't steer every step. That's the fundamental shift — from coding time to review time.

---

## Slide 5: Competitive Comparison
**"Why Devin, not Cursor or Claude Code?"**

> I want to be direct about this comparison because I know you're evaluating multiple tools.
>
> Autonomy — Cursor and Claude Code are human-driven, file-at-a-time. Devin runs fully autonomous sessions. Your engineer reviews the PR, not every keystroke.
>
> Codebase exploration — with Cursor, you manually select which files to feed it. Devin uses LSP, grep, and cross-file analysis to discover coverage gaps without guidance.
>
> Build and CI — this is a big one. With Cursor, you run the build, read the error, go back to the tool, paste the error, get a fix, run the build again. Devin does that loop autonomously. It reads CI logs and iterates.
>
> And async execution — Cursor requires an engineer in the seat. Devin runs in the background while your team does other work. For a team that's already stretched thin, that's the real differentiator.

---

## Slide 6: Proposed Scope
**"Three workstreams, 3-5 focused PRs"**

> Here's what I'm proposing for the initial engagement. Three workstreams.
>
> First — unit test coverage. We audit all 30 hand-written infrastructure files, identify gaps, and add edge-case tests for error handling, serialization round-trips, webhook parsing, retry logic, HTTP client behavior, and telemetry. That's 2 to 3 PRs.
>
> Second — bug fixes. We resolve the five long-standing issues I showed earlier. The ClassCastException, the NumberFormatException, the serialization round-trip bug, API version constants, and builder null handling. That's 1 to 2 PRs.
>
> Third — developer experience groundwork. JSpecify nullability annotations, GraalVM reachability metadata, improved Javadoc. This is incremental and sets the stage for the high-demand features your community is asking for.
>
> Total: 3 to 5 focused, well-tested PRs. Designed to require minimal review effort from your team.

---

## Slide 7: Cost Analysis
**"83% cost reduction vs. manual engineering"**

> Let's talk numbers. This is the cost comparison for the initial stripe-java engagement.
>
> Manual approach — 50 engineer hours at $150 per hour fully loaded. That's $7,500 and 2 to 3 weeks of wall-clock time. And that's an engineer who isn't working on API features during that time.
>
> Cursor or Claude Code — cuts the coding time roughly in half, but you still need 25 hours of an engineer in the seat. $3,770.
>
> Devin Enterprise — 5 hours of engineer time for PR review, plus about $500 in compute. $1,250 total. That's an 83% reduction.
>
> The key insight is that human hours dominate the cost. At $150 an hour, the difference between 25 hours in-seat and 5 hours of review is $3,000 by itself. Devin's compute cost is a fraction of that.

---

## Slide 8: Annual ROI
**"$702K-$1.5M in annual value across Stripe's SDK portfolio"**

> Now here's where it gets interesting. That $6,250 savings per engagement is just the starting point. The real value is annual and recurring.
>
> Conservative estimate: $702K per year. Aggressive: $1.5 million. And the Devin Enterprise cost is $50K to $100K annually. That's roughly a 14x return.
>
> Why is it recurring? Because Stripe ships new API versions roughly monthly. Each version requires test updates, regression testing, and maintenance across all SDKs. This isn't a one-time cleanup — it's an ongoing engineering function that Devin can own.
>
> And for precedent — Nubank used Devin to migrate their core ETL monolith, over 6 million lines of code. They achieved a 12x efficiency improvement in engineering hours and 20x cost savings. Migrations that were projected to take months completed in weeks. This is a proven model at scale.

---

## Slide 9: Full Cost Model
**"Where the value comes from"**

> Let me break down the three layers of value.
>
> First — direct engineering time saved. At roughly 20 hours per month saved per SDK, across 7 SDKs, at $150 per hour, that's $252K to $504K per year depending on scope.
>
> Second — and this is the one that resonates most with CTOs — recaptured senior capacity. Your SDK engineers are some of your most experienced people. They understand the API surface, the type system, the serialization edge cases. Every hour they spend on routine test maintenance is an hour not spent on Stripe Connect, Billing, Issuing, or the V2 API migration. If Devin recaptures even 20% of their time, that's $350K to $500K in redirected senior engineering capacity.
>
> Third — incident risk reduction. Issue 1846 has been open for 18 months. At Stripe's scale, a single SDK bug that causes production errors for merchants generates support tickets, erodes trust, and triggers engineering fire drills. Hard to quantify precisely, but conservatively $100K per year, potentially $500K or more if a serious incident hits.
>
> And notice the two callouts at the bottom — this model only covers 7 SDKs. The real portfolio is 12 to 15 repos when you include stripe-android, stripe-ios, stripe-react-native, and stripe-terminal. And the value recurs monthly with every API release.

---

## Slide 10: Security & Compliance
**"Built for enterprise security standards"**

> I know security is top of mind, especially for a company handling payments infrastructure. Let me address this directly.
>
> Isolated execution — every Devin session runs in its own sandboxed VM. No shared state between sessions. Your code stays within the security perimeter.
>
> Full audit trail — every action Devin takes — every file read, every command executed, every PR created — is logged and reviewable. Your security team can inspect any session after the fact.
>
> Secret management — credentials are encrypted and injected at runtime. Never written to disk, never exposed in logs or commits.
>
> SOC 2 Type II — Cognition maintains SOC 2 Type II compliance. Enterprise SSO, role-based access control, and data retention policies are all available.
>
> And critically — Devin does not train on customer code. Your proprietary logic stays yours. Zero data retention after the session ends.
>
> On the SCM side, Devin integrates natively with GitHub. It respects branch protection rules, required reviews, and CI gates. Devin never pushes directly to main.

---

## Slide 11: Engagement Timeline
**"From kickoff to merged PRs in 2 weeks"**

> Here's what the timeline looks like.
>
> Week 1 — Discovery and first PRs. Devin clones the repo, analyzes the codebase structure, identifies test coverage gaps, and submits the first bug fix PRs for issues 1846, 2149, and 2001. It also begins the unit test coverage work.
>
> Week 2 — Coverage and polish. Complete test coverage across all 30 infrastructure files, iterate on any PR review feedback from your team, begin the JSpecify and GraalVM groundwork, and deliver a final coverage report.
>
> Ongoing — once the initial engagement proves the model, we extend to monitoring new issues and regressions, expanding to other Stripe SDKs, maintaining test coverage as the API evolves, and scaling to broader infrastructure work.
>
> The deliverables are concrete: 2 to 3 bug fix PRs and a coverage gap report in week one. 2 to 3 test coverage PRs and a DX improvement PR in week two. Then ongoing PRs and multi-SDK coverage after that.

---

## Slide 12: Call to Action
**"Let's ship better SDKs, faster."**

> So here's what I'm proposing. Start with stripe-java. It's the right proving ground — mature codebase, clear coverage gaps, real open issues with community demand.
>
> We prove the model in two weeks with measurable results — merged PRs, quantified coverage improvements, resolved issues.
>
> Then we scale across the portfolio. stripe-node, stripe-python, stripe-ruby, stripe-go — the same patterns apply with minimal incremental cost.
>
> Your engineers focus on what they do best — designing APIs, building features, serving developers. We handle the infrastructure quality layer.
>
> I'd love to either start a pilot or schedule a deeper technical demo where we walk through a live Devin session on your codebase. What works best for your team?

---

## Slide 13: Appendix
**"Detailed Issue Breakdown"**

> This is reference material for your team. It breaks down each issue by type, estimated effort, current status, and Devin's approach.
>
> The key takeaway — the total estimated effort across all seven issues is roughly 45 hours of manual engineering. With Devin, we're looking at a fraction of that in active human time, with the bulk of the work handled autonomously.
>
> I'm happy to dive deeper into any specific issue if your engineering managers want to discuss the technical approach.

---

## General Tips for Delivery

- **Pace:** Spend the most time on slides 2 (the opportunity), 8 (annual ROI), and 10 (security). These are the slides that will generate the most questions from a CTO, security officers, and engineering managers respectively.
- **For the CTO:** Lead with the $702K-$1.5M annual value and the 14x ROI. Emphasize recaptured senior capacity — that's the language CTOs respond to.
- **For security officers:** Spend extra time on slide 10. Be prepared for questions about data residency, VPC deployment options, and the audit trail. Know that Cognition offers Dedicated SaaS deployment where the Devbox runs in the customer's cloud.
- **For engineering managers:** They'll care most about slides 2, 5, and 6. They want to know the issues are real, the approach is sound, and the PRs won't create review burden. Emphasize that Devin follows existing test conventions and delivers passing CI.
- **Objection handling:** If asked "why can't we just do this ourselves?" — acknowledge that they absolutely could. The question is whether it's the best use of their senior engineers' time when Devin can handle it at 14x ROI while their team focuses on features.
