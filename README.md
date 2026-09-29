<img alt="Vishnu Vashishth — backend engineer, distributed systems" width="100%" src="https://raw.githubusercontent.com/Vishnu-vashishth/Vishnu-vashishth/main/assets/header.svg" />

<br/>

I spend most of my time in the unglamorous half of the stack — the part that has to be correct at 3am.

Mostly that means **payment infrastructure** and the plumbing around a set of AI chat products: three microservices, fourteen shared libraries, and the migrations that keep years of message history honest. I care about the failure cases more than the happy path, because the happy path takes care of itself.

<br/>

<img alt="GitHub activity" width="100%" src="https://raw.githubusercontent.com/Vishnu-vashishth/Vishnu-vashishth/main/assets/stats.svg" />

<br/>

## What I work on

### Payment platform

One provider-agnostic service owns checkout for several products, rather than each product growing its own half-correct Stripe integration.

Provider abstraction and registry with per-app configuration, so products differ as data and never as branches in the service. Webhook intake through API Gateway → Lambda → SQS for providers that notify exactly once. Idempotent settlement: a webhook delivered twice settles once, and one never delivered gets recovered. Subscription updates guarded against stale writes, and gRPC contracts between the service and the apps that consume it.

### Telemetry and logging

A correlation id minted for every request rather than trusted from the caller, and request scope opened for every gRPC handler so a node's facts actually reach the log.

Bounded JSON log fields that shed their largest value first, in linear time — a capped field stays parseable instead of being truncated mid-token, and a failed child keeps the context that explains it.

### LLM infrastructure

Multi-provider routing where provider quirks are handled at the edge instead of assumed away: stop-sequence limits differ between OpenAI and Groq, so the limit is enforced per provider.

Bounded chat history per turn, prompt management shared across the generation services, and telemetry that records the sampling settings a failed call actually resolved to — not the ones it was asked for.

### Async media pipeline

Character image generation moved off the request path onto a BullMQ queue, and the image-generation service split out of the monolith into its own deployable, alongside text generation.

### Data recovery

Rebuilt a RocksDB whose `CURRENT` and `MANIFEST` were lost. Repaired a gap in a Delta change data feed. Reconstructed what reads of a PostgreSQL table returned during an incident.

### Admin platform

An admin API and panel for workflows, routes and engines, behind required admin auth.

<br/>

## Stack

|  |  |
| :-- | :-- |
| **Languages** | TypeScript · JavaScript · Python |
| **Backend** | NestJS · Node.js · gRPC · Protocol Buffers · BullMQ |
| **Data** | MongoDB · Mongoose · Redis · Typesense |
| **Cloud** | AWS — SQS, S3, KMS, Secrets Manager, Firehose, Lambda, API Gateway · Docker |
| **Payments** | Stripe · PayPal |
| **Tooling** | GitHub Actions · Jest · Axiom · GrowthBook |

<br/>

<!-- Contribution graph — hidden for now.
     Your public contribution graph shows ~4 contributions, because the work lives in
     private org repos. Turn on Settings → Public profile → "Include private
     contributions on my profile", then delete these comment markers to show it.

## Contributions

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Vishnu-vashishth/Vishnu-vashishth/output/github-snake-dark.svg" />
  <img alt="Contribution graph" src="https://raw.githubusercontent.com/Vishnu-vashishth/Vishnu-vashishth/output/github-snake.svg" width="100%" />
</picture>

-->

---

<sub>
Open to conversations about backend architecture, payments, or anything that has to stay up —
<a href="mailto:vishnuvashisth31273@gmail.com">vishnuvashisth31273@gmail.com</a>
<!-- LinkedIn: paste your URL and uncomment → · <a href="https://www.linkedin.com/in/YOUR-HANDLE/">LinkedIn</a> -->
</sub>
